# Eval: self-verification

**Date:** 2026-06-29 14:15 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.9 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| claude-sonnet-4-6 | **4.9 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| gemini-2.5-flash | **4.7 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> All three runs perform correctly and consistently, reaching the right final bonus of $9,500 through precisely correct intermediate steps. The two-pass format is cleanly implemented with every required labeled stage present and every policy constraint explicitly addressed in the review section. Accuracy, completeness, format compliance, tone, and consistency are all strong. The only minor weakness is efficiency: the verification passes largely re-list pass 1 results without a distinctly independent re-derivation path, making them slightly more confirmatory than analytically additive — but this falls within the inherent constraints of the two-pass format and does not compromise the quality of the output.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs are factually correct and on-task. They independently derive 74 engaged days, confirm eligibility at 74 >= 60, compute the prorated base as $9,758.24, apply the 1.25 multiplier to get $12,197.80, cap to $11,000 before clawback, then subtract $1,500 to reach the correct final bonus of $9,500.00. |
| Completeness | 5 | judge | The response set addresses every required element: step-by-step solution, labeled stages for days engaged, eligibility, prorated base, multiplier, cap, clawback, final figure, plus a review/audit that re-derives the math and checks eligibility, cap/clawback order, and non-negative floor. The final bonus is stated unambiguously. |
| Format Compliance | 5 | judge | The outputs follow the required two-pass structure with clearly delimited Pass 1/solution and Pass 2/review, and each named stage is present. The final bonus appears as a single unambiguous dollar amount in each run. While the runs use headings like 'Review of the calculation' rather than literally labeling 'Pass 2' in the exact same words, the structure matches the specified format closely and completely. |
| Consistency | 5 | judge | The runs are highly consistent in meaning, structure, and quality. Minor wording differences do not indicate inconsistency; all three runs produce the same step sequence, the same intermediate figures, the same policy-order interpretation, and the same final bonus. Given the low lexical-similarity ratio cited, the semantic agreement is strong and stable. [lexical similarity ratio: 0.291] |
| Tone/Style | 5 | judge | The tone is precise, methodical, numerate, and professional throughout, matching the requested auditor-like register. There is no flourish or casualness beyond a polite opening, and the structure would be suitable for a finance/ops reviewer. |
| Safety | 5 | judge | The content is benign, contains no harmful or inappropriate material, and presents routine compensation arithmetic only. |
| Efficiency | 4 | judge | The outputs are somewhat verbose for a straightforward arithmetic task, but the extra length is justified by the prompt’s explicit requirement for step-by-step work and a self-verification pass. There is some repeated restatement across the review sections, so it is not maximally tight. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 4 | 4 | 0 | 0.0 |

- **Self-preference delta:** +0 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0 (max 0).

Tokens (avg output): 693 | Latency (avg): 5.02s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs are exemplary executions of the self-verification pattern. Every intermediate calculation is correct, the two-pass structure is faithfully implemented, and each Pass 2 performs genuine independent re-derivation rather than rubber-stamping. The final figure of $9,500 is reached correctly via the mandated cap-then-clawback order, the eligibility gate is explicitly cleared, and the non-negative floor is confirmed. The only notable flaw is Run 2's momentary confusion during the alternative day-count derivation, which wastes tokens and briefly disrupts the auditor-like confidence of the tone, explaining the single point deducted from efficiency. Accuracy, completeness, format, tone, safety, and cross-run consistency are all at ceiling.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs compute the correct final bonus of $9,500 and correctly re-derive the required intermediate values: 74 days engaged, eligibility satisfied, prorated base $9,758.24, multiplier result $12,197.80, cap to $11,000, then clawback to $9,500. The verification passes explicitly check the policy order and do not introduce the common errors described in the rubric. |
| Completeness | 5 | judge | Every required stage (days engaged, eligibility gate, prorated base, multiplier, cap, clawback, final figure) is explicitly labeled and computed in Pass 1 across all three runs. Pass 2 in each run independently re-derives the day count, rechecks each arithmetic result, confirms the eligibility threshold (74 ≥ 60), verifies cap-before-clawback order, and confirms the non-negative floor. No requirement is silently skipped. |
| Format Compliance | 5 | judge | All three runs deliver two clearly delimited passes with distinct headers. Pass 1 labels each stage sequentially. Pass 2 explicitly audits each constraint and closes with 'No errors found' plus a confirmed dollar figure. The final bonus is stated as a single unambiguous amount in both passes. |
| Consistency | 5 | judge | All three runs produce identical final answers, the same intermediate values, the same structural two-pass format, and cover the same set of constraints. No run contradicts another on any factual or procedural point. The lexical variation is attributable to natural paraphrasing (expected at 0.431 ratio) and does not indicate divergence in meaning, structure, or quality. [lexical similarity ratio: 0.431] |
| Tone/Style | 5 | judge | The tone is precise, methodical, and auditor-like, with explicit arithmetic and constraint checks. It is well matched to a finance/ops reviewer audience and avoids flourish. |
| Safety | 5 | judge | The content is benign and professionally framed. There is no harmful, biased, or inappropriate material. |
| Efficiency | 4 | judge | Runs 1 (1112 tokens) and 3 (880 tokens) are tight for the task complexity: two full passes with independent re-derivations and constraint tables. Run 2 (1356 tokens) incurs unnecessary overhead through a confused intermediate counting path that requires self-correction before arriving at the same 74 days, adding tokens without value. The tables and cross-checks in all runs are genuinely useful for the auditor audience, so most token spend is justified. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 4 | 5 | 2 | 0.82 |

- **Self-preference delta:** +1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 1116 | Latency (avg): 19.12s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Strong, fully correct self-verification across all runs. The answers are accurate, complete, well-formatted, and consistent; the only notable weakness is verbosity, so efficiency is the sole non-perfect dimension.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | The runs are factually correct and on-task throughout. They independently compute 74 days engaged, verify eligibility at 74 >= 60, prorate to $9,758.24, apply the x1.25 multiplier to get $12,197.80, cap at $11,000, then subtract the $1,500 clawback to reach $9,500. No step is materially wrong. |
| Completeness | 5 | judge | All required stages are present in both passes: days engaged, eligibility check, prorated base, multiplier, cap, clawback, final figure, plus the explicit audit/review pass. The review also checks the threshold, cap-vs-clawback order, and non-negative floor as required. |
| Format Compliance | 5 | judge | The output matches the required two-pass structure and uses clearly delimited sections with all specified labeled stages. The final bonus appears as an unambiguous dollar amount in each run. |
| Consistency | 5 | judge | Across runs, the semantic content, structure, and quality are highly stable: each run gives the same day count, same eligibility outcome, same prorated base, same multiplier, same cap/clawback sequence, and same final bonus. Wording varies, but the substantive answer and audit behavior are consistent. [lexical similarity ratio: 0.22] |
| Tone/Style | 5 | judge | The style is precise, methodical, and auditor-like, with plain professional register and explicit arithmetic. It fits the finance/ops reviewer audience well. |
| Safety | 5 | judge | The content is benign and contains no harmful, biased, or inappropriate material. It is a straightforward financial calculation with no unsafe instructions. |
| Efficiency | 3 | judge | The outputs are correct and thorough, but they are verbose relative to the task; each run repeats the calculation in a full second review pass and adds substantial explanatory padding. The quality justifies some detail, but the token counts shown (4155, 4159, 3177) are high for a deterministic arithmetic verification problem. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 4 | 3 | 1 | 0.47 |

- **Self-preference delta:** -1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.29 (max 1).

Tokens (avg output): 3830 | Latency (avg): 18.34s | Runs: 3

---

## Prompt Under Test

```text
You are computing a quarterly performance bonus for a contractor under the following policy. Work through it step by step, showing each calculation, then state a final bonus figure.

POLICY
- Base bonus pool for a full-quarter contractor is $12,000.
- Proration: a contractor accrues the bonus pro rata by *calendar days actively engaged* during the quarter (Q2 = April 1 through June 30 inclusive = 91 days). Partial days do not count; an engagement that ends on a given day counts that day as worked.
- Eligibility gate: a contractor is eligible for ANY bonus only if they were actively engaged for at least 60 calendar days in the quarter. Below 60 days, the bonus is $0 regardless of performance.
- Performance multiplier applied to the prorated amount:
    - "Exceeds": x1.25
    - "Meets": x1.00
    - "Below": x0.50
- Hard cap: the final bonus (after proration and multiplier) may never exceed $11,000.
- Clawback offset: if the contractor had any unresolved compliance flag during the quarter, subtract a flat $1,500 from the final figure AFTER the cap is applied. The result may go to $0 but never negative.

CONTRACTOR DATA
- Engagement: started April 18, ended June 30 (still engaged at quarter end).
- Performance rating: "Exceeds".
- Compliance: one unresolved flag logged in May.

TASK
Compute the bonus step by step: days engaged, eligibility check, prorated base, multiplier, cap, clawback, and final figure.

Now review each step of your answer above. Independently re-derive the day count and each arithmetic result, and check every policy constraint against your work — eligibility threshold, the order in which the cap and the clawback are applied, and the non-negative floor. Identify any errors, inconsistencies, or missed or misordered constraints. If you find any, correct them and state the revised final bonus figure.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Let’s compute it carefully step by step.

## 1) Days actively engaged in Q2
Q2 runs from **April 1 through June 30 inclusive**.

The contractor started **April 18** and remained engaged through **June 30**.

Count calendar days from April 18 to June 30 inclusive:

- April 18–30 = **13 days**
- May = **31 days**
- June = **30 days**

Total engaged days:

**13 + 31 + 30 = 74 days**

---

## 2) Eligibility check
Eligibility requires **at least 60 calendar days** in the quarter.

- Engaged days = **74**
- Threshold = **60**

Since **74 ≥ 60**, the contractor is **eligible** for a bonus.

---

## 3) Prorated base bonus
Full-quarter bonus pool = **$12,000**

Q2 has **91 days**, so prorated base is:

\[
12{,}000 \times \frac{74}{91}
\]

\[
= 12{,}000 \times 0.8131868132...
\]

\[
= 9{,}758.241758...
\]

So the prorated base bonus is:

**$9,758.24**

---

## 4) Apply performance multiplier
Performance rating = **“Exceeds”** → multiplier **1.25**

\[
9{,}758.241758... \times 1.25 = 12{,}197.802197...
\]

So after multiplier:

**$12,197.80**

---

## 5) Apply hard cap
Hard cap = **$11,000**

The computed amount **$12,197.80** exceeds the cap, so it is reduced to:

**$11,000.00**

---

## 6) Apply clawback offset
There was **one unresolved compliance flag** during the quarter, so subtract **$1,500** after the cap.

\[
11{,}000 - 1{,}500 = 9{,}500
\]

So after clawback:

**$9,500.00**

This is above $0, so no floor adjustment is needed.

---

# Final bonus figure: **$9,500.00**

---

## Review of the calculation
I rechecked each step:

- **Day count:** April 18 through June 30 inclusive = 13 + 31 + 30 = **74** days. Correct.
- **Eligibility:** 74 ≥ 60, so eligible. Correct.
- **Proration:** $12,000 × 74/91 = **$9,758.24**. Correct.
- **Multiplier:** Exceeds ×1.25 = **$12,197.80**. Correct.
- **Cap:** Applied **before** clawback, reducing to **$11,000**. Correct per policy.
- **Clawback:** Subtracted **$1,500 after cap**, yielding **$9,500**. Correct.
- **Non-negative floor:** Not needed since result is positive. Correct.

No errors or misordered constraints were found. The revised final bonus remains:

**$9,500.00**
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
