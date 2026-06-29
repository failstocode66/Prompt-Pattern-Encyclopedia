# Encyclopedia Eval Campaign — Lab pattern scores (INDEX)

_Generated 2026-06-29 from 40 per-pattern panel-scored reports in `evals/reports/`. 0 missing._

**Config.** Targets (graded): `gpt-5.4-mini` + `claude-sonnet-4-6` + `gemini-2.5-flash`; 3 runs/model; judges = the same mid-tier trio (cross-provider panel, aggregate = mean). Mid-tier judging was empirically vindicated by the 2026-06-20 `tree-of-thoughts` calibration (all-mid vs opus-seat agreed within 0.33/dim).

## How to read this — promotion mapping

The README's **Lab → Core** bar is **≥ 12/15** on the original 3-axis score (Clarity / Consistency / Reusability). The campaign uses the richer **7-dimension** rubric (each 1–5); **Consistency carries over directly** and the other six add accuracy/format/tone/safety/cost evidence. Mapping used here:

- **Pattern mean Overall** = mean of the 3 target models' `overall` (each the mean of its 7 dims, /5).

- **/15-equivalent** = Overall × 3. So **≥ 12/15 ⟺ Overall ≥ 4.0/5** (the 80% bar).

- **Quality-core** = mean of Accuracy/Completeness/Format/Consistency/Tone only — **excludes Safety (a near-constant 5 ceiling on these benign prompts, which inflates Overall) and Efficiency (a cost proxy)**. Treat Quality-core as the stricter discriminator.

- **Caveat.** Scores measure how well the three target models *execute* a pattern, not the pattern's quality in the abstract. A low pattern mean driven by one provider (often `gemini-2.5-flash` here) is a model-execution signal, not necessarily a weak pattern. Promotion is a **review**, not an automatic unlock — use the flags below before promoting.

## Lab → Core candidates (pattern mean ≥ 12/15)

| # | Pattern | Overall /5 | /15 | Quality-core /5 | gpt | claude | gemini |
|---|---|---|---|---|---|---|---|
| 1 | `chain-of-thought` | **4.87** | 14.6 | 4.93 | 5.00 | 4.90 | 4.70 |
| 2 | `direct-answer` | **4.83** | 14.5 | 4.93 | 5.00 | 4.90 | 4.60 |
| 3 | `self-verification` | **4.83** | 14.5 | 5.00 | 4.90 | 4.90 | 4.70 |
| 4 | `delimiter-fencing` | **4.77** | 14.3 | 4.80 | 5.00 | 5.00 | 4.30 |
| 5 | `response-priming` | **4.77** | 14.3 | 4.87 | 5.00 | 4.70 | 4.60 |
| 6 | `cognitive-decomposition` | **4.73** | 14.2 | 4.73 | 5.00 | 4.90 | 4.30 |
| 7 | `few-shot-examples` | **4.57** | 13.7 | 4.53 | 4.70 | 4.90 | 4.10 |
| 8 | `strict-output-format` | **4.50** | 13.5 | 4.47 | 5.00 | 4.90 | 3.60 |
| 9 | `cognitive-verifier` | **4.47** | 13.4 | 4.53 | 4.40 | 4.90 | 4.10 |
| 10 | `low-latency-optimization` | **4.43** | 13.3 | 4.40 | 4.30 | 5.00 | 4.00 |
| 11 | `noise-isolation` | **4.43** | 13.3 | 4.47 | 4.40 | 4.60 | 4.30 |
| 12 | `flipped-interaction` | **4.37** | 13.1 | 4.33 | 4.40 | 4.10 | 4.60 |
| 13 | `self-consistency` | **4.23** | 12.7 | 4.27 | 4.40 | 4.00 | 4.30 |
| 14 | `analogical-reasoning` | **4.17** | 12.5 | 4.27 | 4.30 | 4.30 | 3.90 |
| 15 | `least-to-most-prompting` | **4.17** | 12.5 | 4.27 | 4.10 | 4.10 | 4.30 |
| 16 | `negative-prompting` | **4.10** | 12.3 | 4.13 | 5.00 | 3.60 | 3.70 |
| 17 | `plan-and-solve` | **4.10** | 12.3 | 4.07 | 4.00 | 4.60 | 3.70 |
| 18 | `instruction-anchoring` | **4.07** | 12.2 | 4.07 | 4.10 | 4.40 | 3.70 |
| 19 | `staged-refinement` | **4.07** | 12.2 | 4.00 | 4.40 | 4.10 | 3.70 |
| 20 | `devils-advocate` | **4.03** | 12.1 | 3.93 | 4.30 | 4.40 | 3.40 |
| 21 | `length-budgeting` | **4.03** | 12.1 | 4.13 | 4.10 | 4.30 | 3.70 |
| 22 | `stepback-abstraction` | **4.00** | 12.0 | 4.00 | 4.30 | 4.00 | 3.70 |

**22 of 40 patterns** clear ≥12/15 on the mean. 12 are near-miss (10.5–<12), 6 below 10.5.

## Near-miss (10.5 – <12/15) — promotable with targeted fixes

| Pattern | Overall /5 | /15 | Quality-core | weakest model |
|---|---|---|---|---|
| `confidence-calibration` | 3.93 | 11.8 | 3.93 | gemini-2.5-flash (3.00) |
| `assumption-surfacing` | 3.90 | 11.7 | 3.80 | gemini-2.5-flash (3.30) |
| `structured-output-schema` | 3.87 | 11.6 | 3.87 | gemini-2.5-flash (3.70) |
| `brevity-directive` | 3.80 | 11.4 | 3.73 | gemini-2.5-flash (3.40) |
| `citation-grounding` | 3.80 | 11.4 | 3.80 | gemini-2.5-flash (3.40) |
| `creative-flow` | 3.77 | 11.3 | 3.60 | gemini-2.5-flash (3.30) |
| `skeleton-of-thought` | 3.70 | 11.1 | 3.53 | gemini-2.5-flash (3.10) |
| `output-automator` | 3.67 | 11.0 | 3.87 | claude-sonnet-4-6 (3.30) |
| `tree-of-thoughts` | 3.67 | 11.0 | 3.53 | claude-sonnet-4-6 (3.40) |
| `audience-calibration` | 3.63 | 10.9 | 3.60 | gpt-5.4-mini (3.60) |
| `context-compression` | 3.60 | 10.8 | 3.40 | gpt-5.4-mini (3.10) |
| `react-reasoning-acting` | 3.50 | 10.5 | 3.33 | gpt-5.4-mini (2.10) |

## Below 10.5/15 — not promotion-ready

| Pattern | Overall /5 | /15 | weakest model |
|---|---|---|---|
| `reflect-and-revise` | 3.37 | 10.1 | gemini-2.5-flash (2.70) |
| `role-persona` | 3.37 | 10.1 | gemini-2.5-flash (3.10) |
| `meta-language-creation` | 3.33 | 10.0 | gemini-2.5-flash (3.00) |
| `tool-affordance-disclosure` | 3.23 | 9.7 | gemini-2.5-flash (2.70) |
| `recipe-pattern` | 3.17 | 9.5 | claude-sonnet-4-6 (2.90) |
| `empathic-response` | 3.13 | 9.4 | gpt-5.4-mini (2.90) |

## Campaign dimension profile (mean score per dimension)

| Model | Acc | Comp | Fmt | Cons | Tone | Safe | Eff |
|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | 3.92 | 3.77 | 4.08 | 3.95 | 4.55 | 4.95 | 3.77 |
| claude-sonnet-4-6 | 3.95 | 4.10 | 4.00 | 4.08 | 4.65 | 4.92 | 3.58 |
| gemini-2.5-flash | 3.62 | 3.80 | 3.73 | 3.52 | 4.25 | 4.88 | 2.48 |
| **all** | 3.83 | 3.89 | 3.93 | 3.85 | 4.48 | 4.92 | 3.27 |

## Bias & robustness checks

### Judge self-preference (is the mid-tier panel biased?)

Per dimension, `delta` = (the same-provider judge's score) − (mean of the two cross-provider judges). A systematically **positive** mean would mean a provider's judge inflates its own model. Aggregated across all 40 patterns:

| Same-provider judge | mean delta/dim | n dims |
|---|---|---|
| openai | -0.16 | 280 |
| anthropic | 0.14 | 280 |
| google | 0.19 | 280 |
| **all** | **0.06** | 840 |

Interpretation: deltas near 0 (within a fraction of a point) = no material systematic self-preference → **mid-tier panel judging holds up**, consistent with the 2026-06-20 calibration. Larger per-pattern swings are noise on individual dims; the worst-|total| target/pattern pairs (sum of the same-provider judge's deltas over its 7 dims):

| Pattern | Target model | total self-pref delta |
|---|---|---|
| `tree-of-thoughts` | gemini-2.5-flash | +10.00 |
| `context-compression` | gpt-5.4-mini | +9.50 |
| `empathic-response` | gemini-2.5-flash | +9.50 |
| `analogical-reasoning` | gemini-2.5-flash | +9.00 |
| `output-automator` | claude-sonnet-4-6 | +9.00 |
| `length-budgeting` | gpt-5.4-mini | +8.50 |
| `recipe-pattern` | gemini-2.5-flash | +8.50 |
| `tool-affordance-disclosure` | gemini-2.5-flash | -8.50 |

### Promotion-boundary softness

With a 3-judge panel, panel means land on x.00 / x.33 / x.67, so **any non-unanimous dim is one-judge-flippable by construction** (431 of 720 non-Safety dim-cells campaign-wide — an artifact of n=3 judges, not a defect). That only changes a decision for patterns sitting right at the 12/15 bar. **Patterns within ±0.5 of the line (/15 ∈ [11.5, 12.5]) — treat the candidate/near-miss split as soft; add a 4th judge or hand-score if the call matters:**

| Pattern | /15 | currently |
|---|---|---|
| `analogical-reasoning` | 12.5 | candidate |
| `least-to-most-prompting` | 12.5 | candidate |
| `negative-prompting` | 12.3 | candidate |
| `plan-and-solve` | 12.3 | candidate |
| `instruction-anchoring` | 12.2 | candidate |
| `staged-refinement` | 12.2 | candidate |
| `devils-advocate` | 12.1 | candidate |
| `length-budgeting` | 12.1 | candidate |
| `stepback-abstraction` | 12.0 | candidate |
| `confidence-calibration` | 11.8 | near-miss |
| `assumption-surfacing` | 11.7 | near-miss |
| `structured-output-schema` | 11.6 | near-miss |

### Contested dimensions (judge spread ≥ 2)

205 dim-cells had a 2-point judge spread, concentrated in: **Eff** ×47, **Acc** ×39, **Comp** ×38, **Fmt** ×36, **Cons** ×26, **Tone** ×19. These are where the rubric is most subjective / the prompt hardest to grade.

## Per-pattern detail (aggregate dimension scores, mean across the 3 models)

| Pattern | Acc | Comp | Fmt | Cons | Tone | Safe | Eff | Overall |
|---|---|---|---|---|---|---|---|---|
| `chain-of-thought` | 5.00 | 5.00 | 4.67 | 5.00 | 5.00 | 5.00 | 4.33 | 4.87 |
| `direct-answer` | 5.00 | 5.00 | 4.67 | 5.00 | 5.00 | 5.00 | 4.00 | 4.83 |
| `self-verification` | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 3.67 | 4.83 |
| `delimiter-fencing` | 5.00 | 5.00 | 4.33 | 4.67 | 5.00 | 5.00 | 4.33 | 4.77 |
| `response-priming` | 4.67 | 4.67 | 5.00 | 5.00 | 5.00 | 5.00 | 4.00 | 4.77 |
| `cognitive-decomposition` | 4.33 | 5.00 | 5.00 | 4.33 | 5.00 | 5.00 | 4.33 | 4.73 |
| `few-shot-examples` | 4.00 | 5.00 | 4.33 | 4.33 | 5.00 | 5.00 | 4.33 | 4.57 |
| `strict-output-format` | 4.33 | 5.00 | 4.00 | 4.33 | 4.67 | 5.00 | 4.00 | 4.50 |
| `cognitive-verifier` | 4.33 | 4.33 | 5.00 | 4.67 | 4.33 | 5.00 | 3.67 | 4.47 |
| `low-latency-optimization` | 4.00 | 5.00 | 4.33 | 4.00 | 4.67 | 5.00 | 4.00 | 4.43 |
| `noise-isolation` | 4.00 | 4.33 | 5.00 | 4.00 | 5.00 | 5.00 | 3.67 | 4.43 |
| `flipped-interaction` | 4.00 | 4.00 | 5.00 | 4.00 | 4.67 | 5.00 | 4.00 | 4.37 |
| `self-consistency` | 4.67 | 3.33 | 4.00 | 4.33 | 5.00 | 5.00 | 3.33 | 4.23 |
| `analogical-reasoning` | 4.00 | 4.00 | 4.33 | 4.33 | 4.67 | 5.00 | 2.67 | 4.17 |
| `least-to-most-prompting` | 4.33 | 4.00 | 4.00 | 4.00 | 5.00 | 5.00 | 3.00 | 4.17 |
| `negative-prompting` | 4.33 | 4.33 | 3.67 | 4.00 | 4.33 | 5.00 | 3.00 | 4.10 |
| `plan-and-solve` | 3.67 | 3.33 | 4.67 | 4.00 | 4.67 | 5.00 | 3.33 | 4.10 |
| `instruction-anchoring` | 3.67 | 4.33 | 3.67 | 3.67 | 5.00 | 4.67 | 3.67 | 4.07 |
| `staged-refinement` | 4.00 | 4.33 | 3.33 | 3.33 | 5.00 | 5.00 | 3.67 | 4.07 |
| `devils-advocate` | 3.33 | 3.67 | 4.67 | 3.67 | 4.33 | 5.00 | 3.67 | 4.03 |
| `length-budgeting` | 4.67 | 4.33 | 3.00 | 4.00 | 4.67 | 5.00 | 2.67 | 4.03 |
| `stepback-abstraction` | 3.00 | 4.00 | 4.67 | 3.67 | 4.67 | 5.00 | 3.00 | 4.00 |
| `confidence-calibration` | 3.33 | 4.33 | 3.67 | 3.67 | 4.67 | 5.00 | 3.00 | 3.93 |
| `assumption-surfacing` | 3.67 | 3.33 | 3.67 | 4.00 | 4.33 | 5.00 | 3.33 | 3.90 |
| `structured-output-schema` | 3.33 | 4.00 | 4.00 | 3.33 | 4.67 | 5.00 | 2.67 | 3.87 |
| `brevity-directive` | 3.67 | 3.00 | 3.67 | 3.67 | 4.67 | 5.00 | 3.00 | 3.80 |
| `citation-grounding` | 3.67 | 3.67 | 3.67 | 3.33 | 4.67 | 5.00 | 2.67 | 3.80 |
| `creative-flow` | 3.33 | 4.00 | 3.67 | 3.67 | 3.33 | 5.00 | 3.33 | 3.77 |
| `skeleton-of-thought` | 3.33 | 3.33 | 3.67 | 3.00 | 4.33 | 5.00 | 3.33 | 3.70 |
| `output-automator` | 3.67 | 4.00 | 4.00 | 3.00 | 4.67 | 4.00 | 2.33 | 3.67 |
| `tree-of-thoughts` | 3.33 | 3.00 | 3.67 | 3.33 | 4.33 | 5.00 | 3.00 | 3.67 |
| `audience-calibration` | 4.00 | 3.33 | 3.00 | 3.67 | 4.00 | 5.00 | 2.33 | 3.63 |
| `context-compression` | 3.33 | 3.67 | 3.00 | 3.00 | 4.00 | 5.00 | 3.33 | 3.60 |
| `react-reasoning-acting` | 3.67 | 3.67 | 2.67 | 3.00 | 3.67 | 5.00 | 3.00 | 3.50 |
| `reflect-and-revise` | 3.33 | 2.67 | 4.00 | 3.00 | 3.67 | 4.00 | 3.00 | 3.37 |
| `role-persona` | 2.33 | 2.00 | 4.00 | 4.00 | 4.00 | 4.67 | 2.67 | 3.37 |
| `meta-language-creation` | 2.33 | 2.67 | 3.00 | 4.00 | 3.67 | 4.67 | 3.00 | 3.33 |
| `tool-affordance-disclosure` | 3.00 | 3.00 | 3.00 | 2.67 | 3.67 | 4.67 | 2.67 | 3.23 |
| `recipe-pattern` | 3.00 | 2.00 | 3.00 | 2.67 | 4.00 | 5.00 | 2.33 | 3.17 |
| `empathic-response` | 3.67 | 3.00 | 1.67 | 3.67 | 3.33 | 5.00 | 1.67 | 3.13 |
