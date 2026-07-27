# rejudge_v3.py — [V3] boundary-soft re-judge: add a 4th judge (claude-opus-4-8) to the panel.
#
# WHY THIS EXISTS (design decision, 2026-07-26):
# The plan's [V3] step firms up the 9 promotion-boundary candidates (/15 in [12.0, 12.5],
# each one-judge-flippable on the 3-judge panel) by adding a 4th judge. The 2026-07-02 attempt
# tried to RE-GENERATE the target outputs and re-judge with a 4-judge panel via PromptEval's
# batch mode; it died twice on a gemini-2.5-flash provider outage (gemini is BOTH a target model
# AND a panel judge, so an outage blocks generation and judging alike), and re-generating also
# conflates two variables (new generations + new judge) so the before->after isn't clean.
#
# This script instead adds claude-opus-4-8 as a 4th judge over the EXACT stored campaign
# generations (from evals/reports/<pattern>__*.json). That:
#   (1) isolates the 4th-judge effect — same generations the 3 original judges scored, so the
#       before->after delta is attributable only to the added judge (scientifically clean);
#   (2) touches no gemini path (opus is an Anthropic judge; no target regeneration) — immune to
#       the outage that stalled 07-02;
#   (3) is cheap — 9 patterns x 3 target models = 27 judge calls, no 81 generation calls.
# The judge PROMPT, rubric, schema, and per-judge CONTEXT (expected/format_spec/tone) are the
# harness's own (PromptEval._judge_prompt / _judge_schema), read from each report's stored
# `context`, so opus grades on exactly what the original 3 judges saw.
#
# MODES:
#   --judge    : call claude-opus-4-8 on each stored (pattern, model)'s runs; cache the verdict
#                per pattern to the cache dir (resumable — a crash never re-spends a done pattern).
#   --combine  : pure computation (no API). Recompute the 3-judge panel means as a POSITIVE
#                CONTROL against evals/INDEX.md, then fold opus in as a 4th judge and print/emit
#                the before->after per candidate. Reads the cached opus verdicts.
#
# USAGE:
#   op run --env-file=.env -- python rejudge_v3.py --judge --only analogical-reasoning   # smoke
#   op run --env-file=.env -- python rejudge_v3.py --judge                               # batch rest
#   python rejudge_v3.py --combine --out reports/rejudge-v3__<date>.json                 # no API

import argparse
import glob
import json
import os
import statistics
import sys
import time
from pathlib import Path

import PromptEval as pe
import panel

HERE = Path(__file__).parent
REPORTS = HERE / "reports"
CACHE = HERE.parent / ".rejudge-cache"  # gitignored scratch; per-pattern opus verdicts

FOURTH_JUDGE = "claude-opus-4-8"

# The 9 promotion-boundary candidates (/15 in [12.0, 12.5]) and the campaign report each was
# scored from for evals/INDEX.md. The INDEX /15 is the positive-control target for --combine.
BOUNDARY = {
    "analogical-reasoning":    ("analogical-reasoning__2026-06-20-132142.json",   12.5),
    "least-to-most-prompting": ("least-to-most-prompting__2026-06-29-115540.json", 12.5),
    "negative-prompting":      ("negative-prompting__2026-06-29-122516.json",      12.3),
    "plan-and-solve":          ("plan-and-solve__2026-06-29-130415.json",          12.3),
    "instruction-anchoring":   ("instruction-anchoring__2026-06-29-114344.json",   12.2),
    "staged-refinement":       ("staged-refinement__2026-06-29-143935.json",       12.2),
    "devils-advocate":         ("devils-advocate__2026-06-29-111709.json",         12.1),
    "length-budgeting":        ("length-budgeting__2026-06-29-120256.json",        12.1),
    "stepback-abstraction":    ("stepback-abstraction__2026-06-29-154618.json",    12.0),
}

DIMS = pe.DIM_ORDER  # accuracy, completeness, format_compliance, consistency, tone_style, safety, efficiency
JUDGE_PRICE_IN = 5.0 / 1_000_000   # claude-opus-4-8: $5 / 1M input tokens
JUDGE_PRICE_OUT = 25.0 / 1_000_000  # $25 / 1M output tokens


def _load_report(fname):
    return json.loads((REPORTS / fname).read_text(encoding="utf-8"))


def _spec_from_report(rep):
    ctx = rep.get("context", {})
    return {
        "pattern": rep["pattern"],
        "prompt_text": rep["prompt"],
        "expected": ctx.get("expected"),
        "format_spec": ctx.get("format_spec"),
        "tone": ctx.get("tone"),
    }


# ---- opus judge call (mirrors PromptEval._judge_anthropic, but captures token usage) ----
import anthropic  # noqa: E402


def _opus_judge(spec, model, records, similarity):
    """Score one target model's stored runs with claude-opus-4-8; return (verdict, usage)."""
    dims = pe._judged_dims(len(records))
    schema = pe._judge_schema(dims)
    prompt = pe._judge_prompt(spec, model, records, similarity)
    client = anthropic.Anthropic(api_key=pe._require_key("ANTHROPIC_API_KEY"))

    def _call():
        r = client.messages.create(
            model=FOURTH_JUDGE,
            max_tokens=pe.JUDGE_MAX_TOKENS,
            thinking={"type": "adaptive"},
            output_config={"format": {"type": "json_schema", "schema": schema}},
            messages=[{"role": "user", "content": prompt}],
        )
        if r.stop_reason == "refusal":
            raise RuntimeError("opus judge refused")
        text = next((b.text for b in r.content if b.type == "text"), None)
        if not text:
            raise RuntimeError(f"opus judge returned no text (stop_reason={r.stop_reason})")
        verdict = json.loads(text)
        missing = [k for k in dims + ["summary"] if k not in verdict]
        if missing:
            raise RuntimeError(f"opus judge omitted keys: {missing}")
        return verdict, {"in": r.usage.input_tokens, "out": r.usage.output_tokens}

    # key-omission / transient flakiness lives INSIDE the retried unit (07-02 lesson)
    return pe._with_retry(_call)


def _load_cache(pat):
    p = CACHE / f"{pat}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"pattern": pat, "opus_verdicts": {}, "usage": {"in": 0, "out": 0}}


def run_judge(only=None):
    """Judge per (pattern, model) with incremental caching — timeout-proof and never re-spends
    a completed call. Re-running resumes exactly where it stopped."""
    CACHE.mkdir(exist_ok=True)
    total_in = total_out = 0
    n_calls = 0
    for pat, (fname, _idx) in BOUNDARY.items():
        if only and pat != only:
            continue
        rep = _load_report(fname)
        spec = _spec_from_report(rep)
        cj = _load_cache(pat)
        cj["report"] = fname
        done = cj["opus_verdicts"]
        pending = [mb for mb in rep["models"] if mb["model"] not in done]
        if not pending:
            print(f"[skip] {pat}: all {len(rep['models'])} models cached")
            continue
        print(f"\n=== {pat} ({fname}) — {len(pending)}/{len(rep['models'])} models pending ===")
        for mb in pending:
            model = mb["model"]
            records = mb["runs"]
            sim = pe.lexical_similarity([r["text"] for r in records])
            t0 = time.perf_counter()
            verdict, usage = _opus_judge(spec, model, records, sim)  # raises on failure => resume later
            dt = round(time.perf_counter() - t0, 1)
            done[model] = verdict
            cj["usage"]["in"] += usage["in"]; cj["usage"]["out"] += usage["out"]
            total_in += usage["in"]; total_out += usage["out"]; n_calls += 1
            # persist immediately — this call is now durable
            (CACHE / f"{pat}.json").write_text(json.dumps(cj, indent=2), encoding="utf-8")
            print(f"  {model}: {usage['in']} in / {usage['out']} out tok, {dt}s  "
                  + " ".join(f"{d[:3]}={verdict[d]['score']}" for d in
                             ["accuracy", "completeness", "format_compliance",
                              "consistency", "tone_style", "safety", "efficiency"]))
        cost = cj["usage"]["in"] * JUDGE_PRICE_IN + cj["usage"]["out"] * JUDGE_PRICE_OUT
        print(f"  [done] {pat}: {cj['usage']['in']} in / {cj['usage']['out']} out tok  ~${cost:.3f}")
    if n_calls:
        cost = total_in * JUDGE_PRICE_IN + total_out * JUDGE_PRICE_OUT
        print(f"\nSESSION SPEND: {n_calls} opus calls, {total_in} in / {total_out} out tokens "
              f"~${cost:.3f}")


# ---- pure combine (no API) ----

def _panel_score(scores):
    """The harness aggregate for one dim: round-half-up of the mean of the per-judge scores."""
    return panel.summarize_scores(scores, "mean")["score"]


def _model_overall(dim_scores):
    return round(statistics.mean([dim_scores[d] for d in DIMS]), 1)


def run_combine(out_path=None):
    rows = []
    all_ok = True
    total_in = total_out = 0
    for pat, (fname, index_15) in BOUNDARY.items():
        rep = _load_report(fname)
        cache_path = CACHE / f"{pat}.json"
        opus = None
        if cache_path.exists():
            cj = json.loads(cache_path.read_text(encoding="utf-8"))
            opus = cj["opus_verdicts"]
            total_in += cj["usage"]["in"]; total_out += cj["usage"]["out"]

        before_overalls, after_overalls = [], []
        per_model = []
        contested_before = {}  # dim -> list of models where 3-judge spread>=2
        for mb in rep["models"]:
            model = mb["model"]
            before_dim, after_dim = {}, {}
            dim_detail = {}
            for d in DIMS:
                dd = mb["dimensions"].get(d, {})
                p = dd.get("panel")
                if p and "judges" in p:
                    base_scores = list(p["judges"].values())
                    spread = max(base_scores) - min(base_scores)
                    if spread >= 2:
                        contested_before.setdefault(d, []).append(model)
                else:
                    # consistency single-run edge etc.: fall back to stored score
                    base_scores = [dd["score"]] if dd.get("score") is not None else []
                before_dim[d] = _panel_score(base_scores) if base_scores else dd.get("score")
                if opus and model in opus and d in opus[model]:
                    after_scores = base_scores + [opus[model][d]["score"]]
                    after_dim[d] = _panel_score(after_scores)
                    dim_detail[d] = {"base": base_scores, "opus": opus[model][d]["score"],
                                     "before": before_dim[d], "after": after_dim[d]}
                else:
                    after_dim[d] = before_dim[d]
                    dim_detail[d] = {"base": base_scores, "opus": None,
                                     "before": before_dim[d], "after": after_dim[d]}
            bo = _model_overall(before_dim)
            ao = _model_overall(after_dim)
            before_overalls.append(bo); after_overalls.append(ao)
            per_model.append({"model": model, "before": bo, "after": ao, "dims": dim_detail})

        before_mean = round(statistics.mean(before_overalls), 2)
        after_mean = round(statistics.mean(after_overalls), 2) if opus else None
        before_15 = round(before_mean * 3, 1)
        after_15 = round(after_mean * 3, 1) if opus else None
        # positive control: recomputed before /15 must equal INDEX /15
        control_ok = abs(before_15 - index_15) < 0.06
        all_ok = all_ok and control_ok
        clears = (after_mean >= 4.0) if opus else None
        rows.append({
            "pattern": pat, "index_15": index_15,
            "before_mean": before_mean, "before_15": before_15, "control_ok": control_ok,
            "after_mean": after_mean, "after_15": after_15,
            "clears": clears, "per_model": per_model,
            "contested_before": {d: ms for d, ms in contested_before.items()},
            "has_opus": opus is not None,
        })

    # print table
    print(f"\n{'candidate':26s} {'idx/15':>7} {'ctl':>4} {'before/15':>10} {'after/15':>9} {'clears?':>8}")
    print("-" * 72)
    for r in rows:
        ctl = "OK" if r["control_ok"] else "XX"
        a15 = f"{r['after_15']}" if r["after_15"] is not None else "  --"
        cl = ("CLEARS" if r["clears"] else "no") if r["clears"] is not None else "--"
        print(f"{r['pattern']:26s} {r['index_15']:>7} {ctl:>4} {r['before_15']:>10} {a15:>9} {cl:>8}")
    print("-" * 72)
    print(f"positive control (before == INDEX for all 9): {'PASS' if all_ok else 'FAIL'}")
    if total_in or total_out:
        cost = total_in * JUDGE_PRICE_IN + total_out * JUDGE_PRICE_OUT
        print(f"opus spend represented in cache: {total_in} in / {total_out} out tok ~${cost:.3f}")

    if out_path:
        payload = {"fourth_judge": FOURTH_JUDGE, "generated": time.strftime("%Y-%m-%d %H:%M"),
                   "positive_control_pass": all_ok,
                   "opus_usage": {"in": total_in, "out": total_out,
                                  "cost_usd": round(total_in * JUDGE_PRICE_IN + total_out * JUDGE_PRICE_OUT, 3)},
                   "candidates": rows}
        Path(out_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"wrote {out_path}")
    return all_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", action="store_true", help="call opus over stored generations (API)")
    ap.add_argument("--combine", action="store_true", help="pure before->after computation (no API)")
    ap.add_argument("--only", help="restrict --judge to one pattern (fail-fast smoke)")
    ap.add_argument("--out", help="write combine result JSON here")
    a = ap.parse_args()
    if a.judge:
        run_judge(only=a.only)
    if a.combine:
        ok = run_combine(out_path=a.out)
        sys.exit(0 if ok else 2)
    if not (a.judge or a.combine):
        ap.error("pass --judge and/or --combine")


if __name__ == "__main__":
    main()
