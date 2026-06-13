# Cross-judge experiment for the Prompt Pattern Encyclopedia.
#
# An LLM-as-judge is only trustworthy if its scores don't swing with the judge's
# own identity. This tool runs ONE composed prompt against ONE target model, then
# has SEVERAL judges (across providers) score the SAME response set on the shared
# PromptEval rubric. It reports per-dimension disagreement and — when a judge
# shares the target's provider — flags possible self-preference bias.
#
# It imports PromptEval's runner, rubric, and provider-agnostic judge() so the
# scoring is identical to a normal eval; only the number of judges changes.
#
# Run:
#   op run --env-file=.env -- py CrossJudge.py prompt.txt --pattern role-persona \
#       --target claude-sonnet-4-6 --judges gpt-5.4-mini,claude-opus-4-8,gemini-2.5-flash
#
# Why the defaults: the target is a Claude model and the judge panel spans all
# three providers, so a Claude judge scoring the Claude target noticeably higher
# than the GPT/Gemini judges is visible self-preference.

import argparse
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path

import PromptEval as pe

DEFAULT_TARGET = "claude-sonnet-4-6"
DEFAULT_JUDGES = ["gpt-5.4-mini", "claude-opus-4-8", "gemini-2.5-flash"]


def cross_judge(spec, target, judges, runs):
    """Run the prompt once against `target`, score with each judge. Returns a record."""
    print(f"[target {target}] executing prompt ({runs} run(s))...")
    records = pe.run_prompt(spec["prompt_text"], target, runs)
    similarity = pe.lexical_similarity([r["text"] for r in records])
    dims = pe._judged_dims(runs)

    panel = []
    for j in judges:
        same = pe._provider(j) == pe._provider(target)
        flag = "  [SAME PROVIDER as target -- self-preference watch]" if same else ""
        print(f"[judge {j}]{flag} scoring...")
        verdict = pe.judge(j, spec, target, records, similarity)
        panel.append({
            "judge": j,
            "provider": pe._provider(j),
            "same_provider_as_target": same,
            "scores": {k: verdict[k]["score"] for k in dims},
            "summary": verdict["summary"],
            "verdict": verdict,
        })
    return {"records": records, "similarity": similarity, "dims": dims, "panel": panel}


def analyze(result):
    """Per-dimension spread/stdev across judges + a self-preference delta."""
    dims = result["dims"]
    panel = result["panel"]
    per_dim = {}
    for k in dims:
        scores = [p["scores"][k] for p in panel]
        per_dim[k] = {
            "scores": {p["judge"]: p["scores"][k] for p in panel},
            "min": min(scores),
            "max": max(scores),
            "spread": max(scores) - min(scores),
            "stdev": round(statistics.pstdev(scores), 2) if len(scores) > 1 else 0.0,
        }
    same = [p for p in panel if p["same_provider_as_target"]]
    cross = [p for p in panel if not p["same_provider_as_target"]]

    def _mean_total(group):
        return statistics.mean(sum(p["scores"].values()) for p in group) if group else None

    same_mean, cross_mean = _mean_total(same), _mean_total(cross)
    self_pref = None
    if same_mean is not None and cross_mean is not None:
        self_pref = round(same_mean - cross_mean, 2)  # positive = same-provider judges scored higher
    spreads = [d["spread"] for d in per_dim.values()]
    return {
        "per_dim": per_dim,
        "mean_spread": round(statistics.mean(spreads), 2),
        "max_spread": max(spreads),
        "contested_dims": [k for k, d in per_dim.items() if d["spread"] >= 2],
        "same_provider_mean_total": round(same_mean, 2) if same_mean is not None else None,
        "cross_provider_mean_total": round(cross_mean, 2) if cross_mean is not None else None,
        "self_preference_delta": self_pref,
    }


def write_reports(spec, target, result, analysis, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    base = out / f"crossjudge-{pe._slug(spec['pattern'])}__{stamp}"

    payload = {
        "tool": "CrossJudge v1.0",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "pattern": spec["pattern"],
        "target": target,
        "runs": len(result["records"]),
        "judges": [p["judge"] for p in result["panel"]],
        "lexical_similarity": result["similarity"],
        "analysis": analysis,
        "panel": [{k: p[k] for k in ("judge", "provider", "same_provider_as_target", "scores", "summary")}
                  for p in result["panel"]],
        "prompt": spec["prompt_text"],
        "outputs": [{"run": r["run"], "text": r["text"], "output_tokens": r["output_tokens"]}
                    for r in result["records"]],
    }
    base.with_suffix(".json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    base.with_suffix(".md").write_text(_render_markdown(spec, target, result, analysis), encoding="utf-8")
    return base.with_suffix(".md"), base.with_suffix(".json")


def _render_markdown(spec, target, result, analysis):
    panel = result["panel"]
    dims = result["dims"]
    lines = []
    add = lines.append
    add(f"# Cross-Judge: {spec['pattern']}")
    add("")
    add(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Target:** {target} | "
        f"**Runs:** {len(result['records'])} | **Judges:** {', '.join(p['judge'] for p in panel)}")
    add("")
    add("Same composed prompt + same target outputs, scored independently by each judge. "
        "Disagreement here is judge variance, not model variance.")
    add("")
    add("---")
    add("")
    add("## Judge agreement (score per dimension, 1–5)")
    add("")
    add("| Dimension | " + " | ".join(f"{p['judge']}{' *' if p['same_provider_as_target'] else ''}"
                                      for p in panel) + " | Spread | Stdev |")
    add("|" + "---|" * (len(panel) + 3))
    for k in dims:
        d = analysis["per_dim"][k]
        row = " | ".join(str(d["scores"][p["judge"]]) for p in panel)
        add(f"| {pe.RUBRIC[k]['name']} | {row} | {d['spread']} | {d['stdev']} |")
    totals = " | ".join(str(sum(p["scores"].values())) for p in panel)
    add(f"| **Total** | {totals} | | |")
    add("")
    add(f"`*` = same provider as the target model ({pe._provider(target)}).")
    add("")
    add("---")
    add("")
    add("## Disagreement summary")
    add("")
    add(f"- **Mean per-dimension spread:** {analysis['mean_spread']} "
        f"(max {analysis['max_spread']})")
    contested = analysis["contested_dims"]
    add(f"- **Contested dimensions (spread ≥ 2):** "
        + (", ".join(pe.RUBRIC[k]["name"] for k in contested) if contested else "none"))
    if analysis["self_preference_delta"] is not None:
        d = analysis["self_preference_delta"]
        direction = ("same-provider judges scored the target HIGHER"
                     if d > 0 else "same-provider judges scored the target LOWER" if d < 0
                     else "no same-vs-cross provider gap")
        add(f"- **Self-preference delta:** {d:+} total-score points "
            f"(same-provider mean {analysis['same_provider_mean_total']} vs cross-provider "
            f"{analysis['cross_provider_mean_total']}) — {direction}.")
    else:
        add("- **Self-preference delta:** N/A (panel doesn't mix same- and cross-provider judges).")
    add("")
    add("> Interpretation: low spread + a near-zero self-preference delta means the rubric "
        "scores are judge-robust. A consistently positive delta is evidence a judge favors its "
        "own provider's outputs — a reason to prefer a cross-provider judge or a multi-judge mean.")
    add("")
    add("---")
    add("")
    add("## Per-judge summaries")
    add("")
    for p in panel:
        tag = " (same provider as target)" if p["same_provider_as_target"] else ""
        add(f"**{p['judge']}**{tag}: {p['summary']}")
        add("")
    add("---")
    add("")
    add("## Prompt Under Test")
    add("")
    add("```text")
    add(spec["prompt_text"].rstrip())
    add("```")
    add("")
    add(f"## Target Output ({target}, run 1)")
    add("")
    add("```text")
    add(result["records"][0]["text"].rstrip())
    add("```")
    add("")
    return "\n".join(lines)


def parse_args():
    p = argparse.ArgumentParser(description="Cross-provider judge-disagreement experiment.")
    p.add_argument("prompt_file", nargs="?", help="File with the composed prompt (or --prompt / stdin)")
    p.add_argument("--prompt", help="Composed prompt as a literal string")
    p.add_argument("--pattern", required=True, help="Pattern(s) under test")
    p.add_argument("--target", default=DEFAULT_TARGET, help=f"Model under test (default {DEFAULT_TARGET})")
    p.add_argument("--judges", default=",".join(DEFAULT_JUDGES),
                   help=f"Comma-separated judge models, ideally cross-provider (default: {','.join(DEFAULT_JUDGES)})")
    p.add_argument("--runs", type=int, default=2, help="Runs of the target prompt (default 2; >=2 enables Consistency)")
    p.add_argument("--expected", help="What a correct answer should contain")
    p.add_argument("--format-spec", help="What format compliance means here")
    p.add_argument("--tone", help="Intended tone and audience")
    p.add_argument("--out-dir", default="evals", help="Output dir (default evals/)")
    return p.parse_args()


def main():
    args = parse_args()
    if args.prompt:
        prompt_text = args.prompt
    elif args.prompt_file:
        prompt_text = Path(args.prompt_file).read_text(encoding="utf-8")
    else:
        print("Paste the composed prompt, then EOF (Ctrl+Z then Enter on Windows):")
        prompt_text = sys.stdin.read()
    if not prompt_text.strip():
        sys.exit("Empty prompt.")

    judges = [j.strip() for j in args.judges.split(",") if j.strip()]
    spec = {"pattern": args.pattern, "prompt_text": prompt_text,
            "expected": args.expected, "format_spec": args.format_spec, "tone": args.tone}

    print(f"CrossJudge v1.0 -- pattern: {args.pattern}")
    print(f"Target: {args.target} | judges: {', '.join(judges)} | runs: {args.runs}\n")
    result = cross_judge(spec, args.target, judges, args.runs)
    analysis = analyze(result)
    md_path, json_path = write_reports(spec, args.target, result, analysis, args.out_dir)

    print("\n=== Judge scores (total / 35 max for 7 dims) ===")
    for p in result["panel"]:
        tag = " *" if p["same_provider_as_target"] else ""
        print(f"  {p['judge']}{tag}: {sum(p['scores'].values())}")
    print(f"  mean spread/dim: {analysis['mean_spread']} | self-preference delta: {analysis['self_preference_delta']}")
    print(f"\nReport:  {md_path}\nSidecar: {json_path}")


if __name__ == "__main__":
    main()
