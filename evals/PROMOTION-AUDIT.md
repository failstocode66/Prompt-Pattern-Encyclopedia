# Promotion Audit — V1 Criteria Gap Matrix

**Plan:** `encyclopedia-pattern-promotion` · Step [V1] · Last updated 2026-06-29

## What this is

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
and the boundary-soft re-judge are handled by later plan steps (V2, V3) and are out of scope here.

"Clean pass?" below means **both** #3 and #4 are met. It is *not* a promotion decision — V4
combines this with V2/V3 for the actual promote/hold call.

## Gap matrix

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

## Summary

**22 audited, 0 clean passes** (ready for V3 re-judge / V5 promote pending V2),
**22 with gaps** (need examples/failure-modes filled before promotion).

- **Real-use examples (#3): 0/22 met.** Every candidate's example and baseline outputs are
  the literal stub `[placeholder — to be filled after testing]`. The files provide concrete,
  plausible *inputs* and structural example slots, but no candidate has a single worked
  application showing the pattern producing an actual result. This is consistent with the
  files' `Status: Lab` / `v0.1` (untested drafts) and is the dominant blocker across the set.
- **Failure modes (#4): 21/22 met.** 21 candidates have substantive, dedicated "Failure Modes"
  and "When NOT to Use" sections. The sole exception is **cognitive-decomposition**, an
  unfilled skeleton whose Failure-Modes/When-NOT-to-Use headings exist but contain only
  instructional placeholder text — so it fails both non-score criteria.
- **Net:** no candidate is promotable on the non-score criteria as-is. The gating work before
  V4/V5 is filling ≥2 real worked outputs per candidate (all 22), plus authoring real
  failure-mode content for cognitive-decomposition.
