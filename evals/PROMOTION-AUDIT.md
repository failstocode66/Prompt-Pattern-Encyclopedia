# Promotion Audit — Lab → Core validation

**Plan:** `encyclopedia-pattern-promotion` · Steps [V1]–[V3] · Last updated 2026-07-26

This file accumulates the promotion evidence the 2026-06-29 eval campaign did **not** establish
(a passing score is only one of the five README Lab→Core criteria). Sections:

- **[V1] Criteria gap matrix** — do the 22 score-qualified candidates meet the non-score
  criteria (#3 ≥2 real-use examples, #4 documented failure modes)? *(read-only, no API)*
- **[V2] Baseline-delta** — does each B1-flagged candidate beat a no-pattern control? *(summary)*
- **[V3] Boundary-soft re-judge** — do the 9 candidates within ±0.5 of the 12/15 line still
  clear once a 4th judge is added? *(this pass, 2026-07-26)*

Promotion itself is [V4] (Tyler's review) — this file is the evidence, not the decision.

---

## [V1] Criteria Gap Matrix (2026-06-29)

The 2026-06-29 eval campaign scored all 40 lab patterns and flagged **22 score-qualified
candidates** (pattern-mean ≥ 12/15 — README criterion #5). But a passing score is only one
of the five Lab→Core promotion criteria. This matrix records the **V1 read-only audit** of
the two non-score criteria the campaign did *not* establish, for each of the 22 candidates:

- **#3 — ≥2 real-use examples:** does the pattern file contain at least two *worked*
  applications (concrete input **and** a real produced output), not just template/input slots?
- **#4 — documented failure modes:** does the file document known failure modes / when-not-to-use?

This was a **read-only audit — no API calls, no model runs, no edits to the pattern files.**
It reads each `patterns/lab/<slug>.md` and records a per-criterion verdict so the missing
content is explicit before any promotion. Criteria #1/#2 (test pass, low-variance consistency)
are covered by the eval campaign's test + Consistency dimension; the baseline-delta principle
and the boundary-soft re-judge are handled by later plan steps (V2, V3).

"Clean pass?" below means **both** #3 and #4 are met. It is *not* a promotion decision — V4
combines this with V2/V3 for the actual promote/hold call.

### Gap matrix

Sorted clean-passes first; within ties, ordered by campaign score (high → low).

| Candidate | ≥2 real-use examples | Documented failure modes | Clean pass? | Gaps |
|---|---|---|---|---|
| chain-of-thought | No (0) | Yes | No | All example outputs are unfilled "[placeholder — to be filled after testing]"; no worked applications exist. |
| direct-answer | No (0) | Yes | No | No worked real-use examples: all example/baseline outputs are "[placeholder — to be filled after testing]" stubs. |
| self-verification | No (0) | Yes | No | No completed real-use examples: all 4 example/baseline outputs are "[placeholder — to be filled after testing]". |
| delimiter-fencing | No (0) | Yes | No | No genuine worked examples — every example/baseline output is "[placeholder — to be filled after testing]" with no real demonstrated result. |
| response-priming | No (0) | Yes | No | No genuine worked examples — every example/baseline output is a "[placeholder — to be filled after testing]" stub, so zero of the 2 required real-use examples are demonstrated. |
| few-shot-examples | No (0) | Yes | No | No completed real-use examples — both Examples entries and all Baseline/eval outputs are "[placeholder — to be filled after testing]". |
| strict-output-format | No (0) | Yes | No | No completed real-use examples: all four example/baseline outputs are unfilled "[placeholder — to be filled after testing]" stubs. |
| cognitive-verifier | No (0) | Yes | No | All example and baseline outputs are unfilled "[placeholder — to be filled after testing]"; zero genuine worked real-use examples. |
| low-latency-optimization | No (0) | Yes | No | No completed real-use examples — every example/baseline output is an unfilled "[placeholder — to be filled after testing]". |
| noise-isolation | No (0) | Yes | No | No worked examples: all example/baseline outputs (and most inputs) are "[placeholder — to be filled after testing]", so zero concrete real-use applications exist. |
| flipped-interaction | No (0) | Yes | No | All four example/baseline outputs are unfilled "[placeholder — to be filled after testing]" — zero worked examples exist. |
| self-consistency | No (0) | Yes | No | No worked examples — both Examples and the Baseline Comparison contain only "[placeholder — to be filled after testing]" outputs. |
| analogical-reasoning | No (0) | Yes | No | No worked real-use examples — every example/baseline output is a "[placeholder — to be filled after testing]" stub. |
| least-to-most-prompting | No (0) | Yes | No | No worked real-use examples — all 4 example/baseline outputs are "[placeholder — to be filled after testing]"; nothing is actually solved. |
| negative-prompting | No (0) | Yes | No | No worked real-use examples — every Output (Baseline + both Examples) is a "[placeholder — to be filled after testing]". |
| plan-and-solve | No (0) | Yes | No | No worked real-use examples: all example/baseline outputs are "[placeholder — to be filled after testing]". |
| instruction-anchoring | No (0) | Yes | No | No completed worked examples — every Output field (baseline WITH/WITHOUT and both Examples) is "[placeholder — to be filled after testing]"; only inputs/templates exist. |
| staged-refinement | No (0) | Yes | No | All worked examples are unfilled placeholders, so there are zero genuine real-use examples. |
| devils-advocate | No (0) | Yes | No | No real-use examples: all four candidate examples (2 baseline comparison, 2 in Examples) are unfilled "[placeholder — to be filled after testing]" outputs. |
| length-budgeting | No (0) | Yes | No | All example/baseline outputs are unfilled "[placeholder — to be filled after testing]" — zero genuine worked examples. |
| stepback-abstraction | No (0) | Yes | No | All four example/baseline outputs are "[placeholder — to be filled after testing]"; no worked applications exist. |
| cognitive-decomposition | No (0) | No | No | No filled-in examples (0 worked applications) and no actual failure-mode/when-not-to-use content — every section is an empty template placeholder. |

### V1 Summary

**22 audited, 0 clean passes**, **22 with gaps** (need examples/failure-modes filled before promotion).

- **Real-use examples (#3): 0/22 met.** Every candidate's example and baseline outputs are
  the literal stub `[placeholder — to be filled after testing]`. The files provide concrete,
  plausible *inputs* and structural example slots, but no candidate has a single worked
  application showing the pattern producing an actual result. This is the dominant blocker.
- **Failure modes (#4): 21/22 met.** The sole exception is **cognitive-decomposition**, an
  unfilled skeleton whose Failure-Modes/When-NOT-to-Use headings contain only placeholder text.
- **Net:** no candidate is promotable on the non-score criteria as-is. The gating work before
  V4/V5 is filling ≥2 real worked outputs per candidate (all 22), plus authoring real
  failure-mode content for cognitive-decomposition. (This became plan step [V4b].)

---

## [V2] Baseline-delta pass (2026-07-01) — summary

WITH-vs-WITHOUT (no-pattern control) over the 6 B1-flagged candidates, WITHOUT arm run
2026-07-01 (WITH scores reused from the 06-29 campaign, same panel/config). Deltas
(sum-of-3-model overalls, /15):

| Candidate | WITH /15 | WITHOUT /15 | Δ | Read |
|---|---|---|---|---|
| cognitive-verifier | 13.4 | 9.7 | **+3.7** | strong, real quality lift |
| self-consistency | 12.7 | 9.5 | **+3.2** | strong |
| plan-and-solve | 12.3 | 9.1 | **+3.2** | strong |
| least-to-most-prompting | 12.5 | 11.3 | +1.2 | positive-with-caveat |
| cognitive-decomposition | 14.2 | 13.9 | +0.3 | near-baseline-equivalent (document as reference) |
| chain-of-thought | 14.6 | 14.6 | **+0.0** | 2026 models CoT by default — value is historical/weak-model |

Artifacts: commit `2f9a10d` on `eval-judge-panel` (`prompts/baseline/*`, baseline manifests,
`reports/baseline-delta__2026-07-01.md`).

---

## [V3] Boundary-soft re-judge (2026-07-26)

### The question

The campaign's 3-judge panel (`gpt-5.4-mini` / `claude-sonnet-4-6` / `gemini-2.5-flash`,
aggregate = mean rounded half-up) lands every non-unanimous dimension on x.00 / x.33 / x.67,
so **any contested dimension is one-judge-flippable by construction**. That only matters for
patterns sitting right on the 12/15 line. **9 candidates fall within ±0.5 of the line
(/15 ∈ [12.0, 12.5])** — re-verified against the real per-pattern scores in `INDEX.md`
(positive control below), the set is exactly:
`analogical-reasoning, least-to-most-prompting, negative-prompting, plan-and-solve,
instruction-anchoring, staged-refinement, devils-advocate, length-budgeting, stepback-abstraction`.
[V3] firms each up so its promote/hold call is not a rounding coin-flip.

### Method (why this is a clean before→after)

Add a **4th judge, `claude-opus-4-8`**, to the panel **on the exact stored campaign
generations** — not a re-generation. Rationale:

1. **Isolates the 4th-judge effect.** Opus grades the same 3 runs × 3 target models the
   original 3 judges scored (read from `reports/<pattern>__*.json`), with the same rubric,
   the same judge-prompt builder, and the same per-judge context (expected / format_spec /
   tone). The only variable that changes is the added judge, so the before→after delta is
   attributable to it alone. Re-generating would confound new outputs with the new judge.
2. **Immune to the provider outage that stalled the first attempt.** The 2026-07-02 attempt
   tried to *re-generate* and re-judge via the batch harness and died twice on a
   `gemini-2.5-flash` outage — gemini is **both** a target model and a panel judge, so an
   outage blocks generation and judging alike. This pass touches no gemini path (opus is an
   Anthropic judge; no target regeneration).
3. **Cheap and resumable.** 9 patterns × 3 target models = 27 judge calls (vs. 81 generation
   calls), cached per (pattern, model) so a crash never re-spends a completed call.

Harness: `evals/rejudge_v3.py` (`--judge` = opus over stored runs; `--combine` = pure
before→after). Aggregation reuses `panel.summarize_scores` (mean, round-half-up per dimension;
per-model overall = mean of the 7 dim scores; pattern mean = mean of the 3 models; /15 = ×3).

**Positive control (mandatory):** `--combine` first recomputes the *3-judge* panel means from
the stored per-judge scores and asserts they equal `INDEX.md` for all 9 candidates before
folding opus in. **Result: PASS for all 9** — the report selection and the panel-math
re-implementation reproduce the campaign exactly, so the "after" numbers are trustworthy.

### Result — every boundary candidate now firmly CLEARS ≥12/15

| Candidate | before /15 | after /15 (4-judge) | margin | Clears ≥12/15? | What firmed it (opus broke the tie on the contested dim) |
|---|---|---|---|---|---|
| least-to-most-prompting | 12.5 | **13.1** | +0.6 | **YES** | accuracy 4→5 on gpt & claude (opus 5); completeness 4→5 gemini; efficiency 3→4 gpt |
| plan-and-solve | 12.3 | **13.0** | +0.7 | **YES** | completeness+format+efficiency ↑ on gpt; completeness 4→5 claude; tone 4→5 gemini |
| instruction-anchoring | 12.2 | **12.9** | +0.7 | **YES** | format 3→4 gpt (opus 5); accuracy 4→5 claude; accuracy+efficiency ↑ gemini |
| staged-refinement | 12.2 | **12.9** | +0.7 | **YES** | accuracy 4→5 gpt; accuracy+completeness+format ↑ claude |
| negative-prompting | 12.3 | **12.8** | +0.5 | **YES** | format+efficiency ↑ claude; consistency 3→4 gemini |
| analogical-reasoning | 12.5 | **12.7** | +0.2 | **YES** | format 4→5 gpt; efficiency 2→3 gemini |
| devils-advocate | 12.1 | **12.5** | +0.4 | **YES** | consistency 4→5 gpt; accuracy+format ↑ gemini |
| length-budgeting | 12.1 | **12.4** | +0.3 | **YES** | efficiency ↑ on both gpt & claude (opus 5 on the budget-adherence dim) |
| stepback-abstraction | 12.0 | **12.3** | +0.3 | **YES** | accuracy 2→3 + efficiency 2→3 on gemini (opus 5 / 4) |

Full machine-readable detail (per-model, per-dimension base scores + opus score + contested-dim
flags): `evals/reports/rejudge-v3__2026-07-26.json`.

### Interpretation (for the [V4] decision)

- **All 9 firm up in the SAME direction — upward — and none flips to "does not clear."** The
  DONE bar for [V3] (a firmed clears/does-not-clear verdict per candidate, not a rounding
  coin-flip) is met: **9/9 clear**, each with a margin of at least +0.3/15 above the line.
- **No candidate needed hand-scoring.** The plan allowed hand-scoring a contested dimension
  where a 4th judge still left a genuine coin-flip; none did — opus produced a decisive verdict
  for every candidate.
- **The lift concentrates on the contested dimensions**, exactly where the 3-judge panel was
  flippable — most often `accuracy`, `completeness`, `format_compliance`, and `efficiency`,
  and most often on the `gemini-2.5-flash` target (the weakest executor, which had dragged the
  3-judge means down). Opus, a stronger judge, more often scores a well-executed contested
  dimension at the high end, which rounds the panel-mean dimension score up.
- **Caveat to weigh in [V4]:** the shift is *systematically* upward, and opus is a second
  Anthropic voice on the panel alongside `claude-sonnet-4-6`. This does not threaten the
  clears/does-not-clear verdict (the smallest post-margin, stepback-abstraction at 12.3, still
  clears), but it means the re-judge should be read as **"these 9 are not fragile near-misses —
  they clear robustly"**, not as a precise new score. Promotion still requires the non-score
  criteria (#3 real-use examples — 0/9 met per V1; #4 failure modes — met for all 9) authored
  in [V4b] before any lab→core move.

### Spend

Opus judging: **296,908 input + 138,025 output tokens across 27 calls ≈ $4.94** (claude-opus-4-8
at $5/$25 per 1M). This is above the ~$1–3 estimate and at the top of the pre-approved ~$5 hard
cap; the driver was opus adaptive-thinking output tokens (~5.1k out/call). No credit or billing
error occurred; the fail-fast smoke (analogical-reasoning) ran first and verified sane output
before the batch. All spending is complete — `--combine` is pure computation.

---

## [V4] PROMOTE-SET DECISION — 2026-07-27 (Tyler, recorded verbatim from the vetting session)

**Rulings:** (1) promote-set = "just the 4 delta-proven"; (2) V2 baseline-delta extension =
later; (3) [V4b] authoring runs hands-off — drafts published to Tyler's screen for one batch
review + approval before any lab→core move.

### The agreed promote-set (4)

| Pattern | Score /15 (V3-firmed where boundary) | Baseline delta (V2) | Missing before promotion |
|---|---|---|---|
| cognitive-verifier | 13.4 | **+3.7** | #3 real-use examples (≥2) |
| plan-and-solve | 12.3 → 13.0 | **+3.2** | #3 real-use examples (≥2) |
| self-consistency | 12.7 | **+3.2** | #3 real-use examples (≥2) |
| least-to-most-prompting | 12.5 → 13.1 | **+1.2** (promote-with-caveat: modest delta, "when to use" must scope it) | #3 real-use examples (≥2) |

All four already document failure modes (#4 met per V1). The evidence chain for each is
complete on every criterion except #3, which [V4b] authors next.

### Held in lab — with reasons (18)

- **Format/control candidates** (delimiter-fencing, strict-output-format, response-priming,
  length-budgeting): high scores; candidate exemption from the delta principle (value is output
  control, not a quality delta) — **held for a later tranche** where that exemption is argued
  per-pattern rather than assumed.
- **Baseline-equivalent pair** (chain-of-thought +0.0, cognitive-decomposition +0.3): candidates
  for reference-reclassification with "modern models do this unprompted" framing — held pending
  that framing decision; NOT promotable as-is (the honest +0.0 is part of the encyclopedia's
  credibility).
- **Score-firm, delta-unmeasured** (direct-answer, self-verification, few-shot-examples,
  cognitive-verifier is promoted above, low-latency-optimization, noise-isolation,
  flipped-interaction, analogical-reasoning, negative-prompting, instruction-anchoring,
  staged-refinement, devils-advocate, stepback-abstraction): clear ≥12/15 (boundary members
  robustly per V3) but carry no baseline-delta evidence; **held pending a later V2 extension**
  (deferred by ruling 2) or per-pattern exemption argument.

**Promotion still gates on [V4b]:** no lab→core move until each promote-set pattern carries ≥2
genuine real-use examples, Tyler-approved in the batch review.
