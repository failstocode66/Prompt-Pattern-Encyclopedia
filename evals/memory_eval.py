# memory_eval.py — MemoryBench-style WITH/WITHOUT lesson-effectiveness eval ([C2]).
#
# Question: does having the relevant lesson(s) in context measurably improve the
# model's answer to a task the lesson applies to? This is the effectiveness signal
# the monthly lesson-synthesis agent lacks — it scores lesson *activity*, never *effect*.
#
# For each case: run the SAME task on the SAME model twice — WITHOUT (baseline) and
# WITH (the relevant lesson body(ies) prepended) — then have the Phase-A cross-provider
# panel score both answers on the rubric. Report delta = WITH - WITHOUT (panel-aggregate)
# per case + an overall "lessons lift" (mean delta) and win-rate. Because the SAME panel
# scores both conditions, any judge self-preference bias cancels in the delta.
#
# Reuses PromptEval's runner + judge and the panel.py aggregator — no new judge system.
#   op run --env-file=.env -- py evals/memory_eval.py --cases evals/memory/cases --no-... etc.

import argparse
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path

import yaml

import PromptEval as pe
import panel

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_JUDGES = ["gpt-5.4-mini", "claude-opus-4-8", "gemini-2.5-flash"]
DEFAULT_LESSONS_DIR = r"C:\Projects\claude-brain\Interactions\lessons"
WIN_THRESHOLD = 0.5   # |overall delta| >= this => win/lose; within => tie (judge-noise band)


# --- lesson + case loading --------------------------------------------------

def strip_frontmatter(text):
    """Drop a leading `--- ... ---` YAML frontmatter block; return the markdown body."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[nl + 1:] if nl != -1 else ""
    return text


def load_lesson_body(slug, lessons_dir):
    """Read a lesson note by slug and return its body (frontmatter stripped)."""
    path = Path(lessons_dir) / f"{slug}.md"
    return strip_frontmatter(path.read_text(encoding="utf-8")).strip()


def load_cases(path):
    """Load case dicts from a YAML file or a directory of YAML files.
    Each file holds one case (mapping) or a list of cases."""
    p = Path(path)
    files = sorted(p.glob("*.yaml")) + sorted(p.glob("*.yml")) if p.is_dir() else [p]
    cases = []
    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if data is None:
            continue
        cases.extend(data if isinstance(data, list) else [data])
    return cases


def inject(lesson_bodies, task):
    """Prepend the lesson body(ies) to the task (mirrors how SessionStart surfaces them)."""
    notes = "\n\n".join(lesson_bodies)
    return f"You may find the following note(s) from past work relevant:\n\n{notes}\n\n---\n\n{task}"


# --- one condition (WITH or WITHOUT) ----------------------------------------

def run_condition(task_text, reference, model, judges, runs, method="mean"):
    """Run `task_text` on `model` and panel-score the output. Returns scores + answer."""
    records = pe.run_prompt(task_text, model, runs)
    sim = pe.lexical_similarity([r["text"] for r in records])
    spec = {"pattern": "memory-eval", "prompt_text": task_text, "expected": reference,
            "format_spec": None, "tone": None}
    dims = pe._judged_dims(len(records))
    pv = panel.score_with_panel(
        judges, lambda j: pe.judge(j, spec, model, records, sim),
        dims, pe._provider(model), pe._provider, method=method)
    scores = {d: pv[d]["score"] for d in dims}
    return {"scores": scores, "panel": pv, "answer": records[0]["text"],
            "output_tokens": [r["output_tokens"] for r in records]}


def evaluate_case(case, model, judges, runs, lessons_dir, threshold=WIN_THRESHOLD):
    """WITH/WITHOUT a case's relevant lesson(s); return the delta + outcome record."""
    task = case["task"]
    reference = case.get("reference")
    target_dims = case.get("dimensions") or list(pe.JUDGED_DIMS)
    bodies = [load_lesson_body(s, lessons_dir) for s in case["relevant_lessons"]]

    without = run_condition(task, reference, model, judges, runs)
    with_ = run_condition(inject(bodies, task), reference, model, judges, runs)

    per_dim_delta = {d: with_["scores"][d] - without["scores"][d] for d in without["scores"]}

    def _overall(scores):
        present = [scores[d] for d in target_dims if d in scores]
        return round(statistics.mean(present), 2) if present else None

    ow, oo = _overall(with_["scores"]), _overall(without["scores"])
    delta = round(ow - oo, 2)
    outcome = "win" if delta >= threshold else "lose" if delta <= -threshold else "tie"
    return {
        "id": case.get("id", "?"),
        "lessons": case["relevant_lessons"],
        "model": model,
        "target_dims": target_dims,
        "without_overall": oo,
        "with_overall": ow,
        "delta": delta,
        "outcome": outcome,
        "per_dim_delta": per_dim_delta,
        "without": without,
        "with": with_,
    }


def summarize(results):
    n = len(results)
    wins = sum(1 for r in results if r["outcome"] == "win")
    losses = sum(1 for r in results if r["outcome"] == "lose")
    return {
        "n": n,
        "wins": wins,
        "losses": losses,
        "ties": n - wins - losses,
        "win_rate": round(wins / n, 2) if n else 0.0,
        "mean_delta": round(statistics.mean(r["delta"] for r in results), 2) if n else 0.0,
    }


# --- reports ----------------------------------------------------------------

def write_reports(results, summary, model, judges, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    base = out / f"memory-eff-{stamp}"
    payload = {
        "tool": "memory_eval v1.0",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "model": model,
        "judges": judges,
        "win_threshold": WIN_THRESHOLD,
        "summary": summary,
        "cases": [{k: r[k] for k in ("id", "lessons", "target_dims", "without_overall",
                                     "with_overall", "delta", "outcome", "per_dim_delta")}
                  | {"without_answer": r["without"]["answer"], "with_answer": r["with"]["answer"],
                     "without_scores": r["without"]["scores"], "with_scores": r["with"]["scores"]}
                  for r in results],
    }
    base.with_suffix(".json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    base.with_suffix(".md").write_text(_render_markdown(results, summary, model, judges), encoding="utf-8")
    return base.with_suffix(".md"), base.with_suffix(".json")


def _render_markdown(results, summary, model, judges):
    lines = []
    add = lines.append
    add("# Memory-effectiveness eval — does injecting the relevant lesson improve the answer?")
    add("")
    add(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Target:** {model} | "
        f"**Judge panel:** {', '.join(judges)} | **Win threshold:** ±{WIN_THRESHOLD}")
    add("")
    lift = summary["mean_delta"]
    add(f"**Lessons lift:** {lift:+} mean rubric points (WITH − WITHOUT) across "
        f"{summary['n']} case(s) · **win-rate {int(summary['win_rate']*100)}%** "
        f"({summary['wins']}W / {summary['losses']}L / {summary['ties']}T).")
    add("")
    add("> Positive lift ⇒ the lesson measurably improves the answer (earns its place). "
        "≈0 or negative ⇒ the model already knew it, or the lesson doesn't help → a "
        "reject/merge candidate for lesson-synthesis. The same panel scores both conditions, "
        "so judge self-preference cancels in the delta.")
    add("")
    add("---")
    add("")
    add("## Per-case results")
    add("")
    add("| Case | Lesson(s) | WITHOUT | WITH | Δ | Outcome |")
    add("|---|---|---|---|---|---|")
    for r in results:
        lessons = "<br>".join(r["lessons"])
        emoji = {"win": "✅ win", "lose": "❌ lose", "tie": "➖ tie"}[r["outcome"]]
        add(f"| {r['id']} | {lessons} | {r['without_overall']} | {r['with_overall']} "
            f"| **{r['delta']:+}** | {emoji} |")
    add("")
    for r in results:
        add("---")
        add("")
        add(f"## {r['id']} — Δ {r['delta']:+} ({r['outcome']})")
        add("")
        add(f"**Lesson(s):** {', '.join(r['lessons'])} · **Target dims:** {', '.join(r['target_dims'])}")
        add("")
        add("| Dimension | WITHOUT | WITH | Δ |")
        add("|---|---|---|---|")
        for d in r["without"]["scores"]:
            wo = r["without"]["scores"][d]
            wi = r["with"]["scores"][d]
            star = " *" if d in r["target_dims"] else ""
            add(f"| {pe.RUBRIC[d]['name']}{star} | {wo} | {wi} | {wi - wo:+} |")
        add("")
        add("`*` = a dimension the lesson is expected to improve (averaged into Δ).")
        add("")
        add("<details><summary>WITHOUT answer</summary>")
        add("")
        add("```text")
        add(r["without"]["answer"].rstrip())
        add("```")
        add("</details>")
        add("")
        add("<details><summary>WITH answer (lesson injected)</summary>")
        add("")
        add("```text")
        add(r["with"]["answer"].rstrip())
        add("```")
        add("</details>")
        add("")
    return "\n".join(lines)


# --- CLI --------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="MemoryBench-style WITH/WITHOUT lesson-effectiveness eval (Phase C).")
    p.add_argument("--cases", default="evals/memory/cases",
                   help="YAML case file or directory (default evals/memory/cases)")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Target model (default {DEFAULT_MODEL})")
    p.add_argument("--judges", default=",".join(DEFAULT_JUDGES),
                   help=f"Comma-separated judge panel (default {','.join(DEFAULT_JUDGES)})")
    p.add_argument("--runs", type=int, default=1, help="Runs per condition (default 1)")
    p.add_argument("--lessons-dir", default=DEFAULT_LESSONS_DIR, help="Where lesson notes live")
    p.add_argument("--out-dir", default="evals/reports", help="Output dir (default evals/reports)")
    return p.parse_args()


def main():
    # Windows consoles default to cp1252, which can't encode the report's Δ / em-dash in
    # progress prints (the report FILE is written utf-8 regardless). Make stdout utf-8-safe.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    args = parse_args()
    judges = [j.strip() for j in args.judges.split(",") if j.strip()]
    cases = load_cases(args.cases)
    if not cases:
        sys.exit(f"No cases found at {args.cases}")
    print(f"memory_eval v1.0 — {len(cases)} case(s) | target {args.model} | "
          f"panel {', '.join(judges)} | runs {args.runs}\n")

    results = []
    for n, case in enumerate(cases, 1):
        print(f"========== [{n}/{len(cases)}] {case.get('id', '?')} ==========")
        r = evaluate_case(case, args.model, judges, args.runs, args.lessons_dir)
        print(f"  WITHOUT {r['without_overall']} | WITH {r['with_overall']} | "
              f"Δ {r['delta']:+} ({r['outcome']})\n")
        results.append(r)

    summary = summarize(results)
    md_path, json_path = write_reports(results, summary, args.model, judges, args.out_dir)
    print("=== Memory-effectiveness summary ===")
    print(f"  Lessons lift: {summary['mean_delta']:+} mean points | "
          f"win-rate {int(summary['win_rate']*100)}% "
          f"({summary['wins']}W/{summary['losses']}L/{summary['ties']}T)")
    print(f"\nReport:  {md_path}\nSidecar: {json_path}")


if __name__ == "__main__":
    main()
