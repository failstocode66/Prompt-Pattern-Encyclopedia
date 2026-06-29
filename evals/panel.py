# panel.py — shared multi-judge panel scoring for the eval harness ([A1]).
#
# Both PromptEval (single-judge + the --judges panel mode) and CrossJudge import this
# so the multi-judge aggregation lives in ONE place instead of being duplicated.
#
# The module is deliberately PURE: it performs no API calls and does not import
# PromptEval. That (a) avoids a circular import — PromptEval/CrossJudge import panel,
# not the reverse — and (b) keeps every function unit-testable offline. The caller
# injects the two things that DO touch PromptEval:
#   • score_one(judge_model) -> verdict   the per-judge API scoring (pe.judge, pre-bound
#                                          to the spec/target/records/similarity)
#   • provider_of(model)      -> provider  pe._provider
#
# Contract (campaign plan [A1]): each judged dimension is scored by N judges; the
# aggregate is the mean rounded half-up (median is available as an outlier-robust
# option); we record each judge's per-dimension score, the spread (max-min), the
# population stdev, and a same-provider self-preference flag (a judge that shares the
# TARGET model's provider scoring it above the cross-provider judges). A SINGLE judge
# is the degenerate N=1 case — aggregate == that judge's score, spread/stdev 0, no
# self-preference signal, and per-dimension score/justification/evidence identical to
# the pre-panel single-judge path (so single-judge output is unchanged).

import statistics

AGG_METHODS = ("mean", "median")


def round_half_up(x):
    """Round to the nearest int, halves UP (2.5 -> 3, 4.5 -> 5). Scores are always >= 0."""
    return int(x + 0.5)


def summarize_scores(scores, method="mean"):
    """Aggregate one dimension's per-judge scores into the panel contract stats."""
    if method not in AGG_METHODS:
        raise ValueError(f"unknown aggregate method {method!r} (use one of {AGG_METHODS})")
    if not scores:
        raise ValueError("summarize_scores needs at least one score")
    mean = statistics.mean(scores)
    median = statistics.median(scores)
    chosen = mean if method == "mean" else median
    return {
        "scores": list(scores),
        "score": round_half_up(chosen),
        "mean": round(mean, 2),
        "median": median,
        "min": min(scores),
        "max": max(scores),
        "spread": max(scores) - min(scores),
        "stdev": round(statistics.pstdev(scores), 2) if len(scores) > 1 else 0.0,
    }


def self_preference(judge_rows, dim):
    """Flag when judges sharing the target's provider score `dim` ABOVE the cross-provider judges.

    judge_rows: [{"same_provider_as_target": bool, "scores": {dim: int}}, ...]
    Returns {"flag": bool, "delta": float|None}; delta = same_mean - cross_mean
    (None when either group is empty — there's nothing to compare).
    """
    same = [r["scores"][dim] for r in judge_rows if r["same_provider_as_target"]]
    cross = [r["scores"][dim] for r in judge_rows if not r["same_provider_as_target"]]
    if not same or not cross:
        return {"flag": False, "delta": None}
    delta = round(statistics.mean(same) - statistics.mean(cross), 2)
    return {"flag": delta > 0, "delta": delta}


def _representative(judge_results, dim, target_score):
    """The judge whose `dim` score is closest to the aggregate (ties -> first listed).
    Its justification/evidence become the panel's single-line fields, so the text stays a
    real, coherent rationale rather than a merge of several."""
    best = min(judge_results, key=lambda jr: abs(jr["verdict"][dim]["score"] - target_score))
    return best["verdict"][dim]


def build_panel_verdict(judge_results, dims, target_provider, method="mean"):
    """Aggregate N judges' verdicts into a panel verdict shaped like a single verdict.

    judge_results: [{"judge","provider","same_provider_as_target","verdict"}], where
                   verdict is a pe.judge() output ({dim: {score,justification,evidence}, "summary"}).
    Returns {dim: {score, justification, evidence, panel:{...}}, "summary": ..., "_panel_meta": {...}}.
    The per-dim `score`/`justification`/`evidence` keys are exactly what PromptEval.build_results
    already consumes; the extra `panel` key (and top-level `_panel_meta`) ride alongside for the
    panel-aware report. For N=1 the consumed keys equal the lone judge's verdict (no behavior change).
    """
    if not judge_results:
        raise ValueError("build_panel_verdict needs at least one judge result")

    judge_rows = [{
        "judge": jr["judge"],
        "same_provider_as_target": jr["same_provider_as_target"],
        "scores": {d: jr["verdict"][d]["score"] for d in dims},
    } for jr in judge_results]

    out = {}
    for d in dims:
        scores = [jr["verdict"][d]["score"] for jr in judge_results]
        agg = summarize_scores(scores, method)
        rep = _representative(judge_results, d, agg["score"])
        out[d] = {
            "score": agg["score"],
            "justification": rep["justification"],
            "evidence": rep["evidence"],
            "panel": {
                "judges": {jr["judge"]: jr["verdict"][d]["score"] for jr in judge_results},
                "mean": agg["mean"],
                "median": agg["median"],
                "spread": agg["spread"],
                "stdev": agg["stdev"],
                "method": method,
                "self_preference": self_preference(judge_rows, d),
            },
        }

    # representative summary: the judge whose TOTAL across dims is the median total.
    totals = sorted((sum(jr["verdict"][d]["score"] for d in dims), i)
                    for i, jr in enumerate(judge_results))
    rep_summary = judge_results[totals[len(totals) // 2][1]]["verdict"]["summary"]

    # overall panel meta (generalizes CrossJudge.analyze's total-score self-preference delta).
    same_totals = [t for t, i in totals if judge_results[i]["same_provider_as_target"]]
    cross_totals = [t for t, i in totals if not judge_results[i]["same_provider_as_target"]]
    sp_delta = (round(statistics.mean(same_totals) - statistics.mean(cross_totals), 2)
                if same_totals and cross_totals else None)
    spreads = [out[d]["panel"]["spread"] for d in dims]

    out["summary"] = rep_summary
    out["_panel_meta"] = {
        "judges": [jr["judge"] for jr in judge_results],
        "providers": {jr["judge"]: jr["provider"] for jr in judge_results},
        "method": method,
        "n_judges": len(judge_results),
        "target_provider": target_provider,
        "mean_spread": round(statistics.mean(spreads), 2) if spreads else 0.0,
        "max_spread": max(spreads) if spreads else 0,
        "contested_dims": [d for d in dims if out[d]["panel"]["spread"] >= 2],
        "self_preference_delta": sp_delta,
    }
    return out


def score_with_panel(judges, score_one, dims, target_provider, provider_of,
                     method="mean", on_judge=None):
    """Orchestrate: score the target's outputs with each judge, then aggregate.

    judges: [judge_model, ...]  (a 1-element list reproduces single-judge behavior)
    score_one(judge_model) -> verdict    injected per-judge API scorer (pe.judge bound to spec/records)
    provider_of(model) -> provider       pe._provider
    on_judge(judge_model, same_provider) optional progress callback (for printing)
    """
    judge_results = []
    for j in judges:
        same = provider_of(j) == target_provider
        if on_judge:
            on_judge(j, same)
        verdict = score_one(j)
        judge_results.append({
            "judge": j,
            "provider": provider_of(j),
            "same_provider_as_target": same,
            "verdict": verdict,
        })
    return build_panel_verdict(judge_results, dims, target_provider, method)
