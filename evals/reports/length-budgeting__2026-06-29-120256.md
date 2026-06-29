# Eval: length-budgeting

**Date:** 2026-06-29 12:02 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.1 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4.3 (Solid)** | 5 | 5 | 3 | 5 | 5 | 5 | 2 |
| gemini-2.5-flash | **3.7 (Solid)** | 5 | 4 | 2 | 3 | 4 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> All three runs are strong, budget-compliant status-page banners that cover every mandatory incident element within the 60-word cap in plain, professional prose. The most consistent gap is the absence of an explicit 'no double-charge risk' qualifier on the Idempotency-Key retry in runs 2 and 3 (run 1 partially addresses this with 'safely'), which the reference flags as the single most decision-critical callout. Format compliance is perfect, tone is pitch-appropriate for B2B incident communications, and there is no apology boilerplate or padding. Consistency is high — same structure and core content across all runs with minor variation in lower-priority details. The outputs are solid executions of the length-budgeting pattern but fall just short of a top score due to the recurring partial omission of the safety framing around the workaround.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs accurately reproduce every stated incident fact: endpoint (POST /v1/charges), failure rate (~40% HTTP 503), unaffected services, rollback in progress, regional scope, next-update time, and the idempotency retry workaround. The one consistent gap is that runs 2 and 3 do not explicitly frame the Idempotency-Key retry as 'no double-charge risk'; only run 1 adds 'safely' ('You can safely retry'). The reference calls this the single most decision-relevant callout. Minor but consistent across two of three runs. |
| Completeness | 4 | judge | All three mandatory elements are present in every run: (1) WHAT is broken and its severity, (2) the idempotency retry workaround, (3) the 15:00 UTC next-update commitment. Scope reassurance (refunds/payouts/dashboard unaffected) is also present in all runs. The partial miss is that the explicit 'no double-charge risk' framing is absent in runs 2 and 3, which is the specific safety-signal the reference marks as decision-critical. Lower-priority items (rollback, regional carve-out, start time) are included but remain within budget and are not harmful filler. |
| Format Compliance | 4 | judge | Each run is a single continuous plain-prose status banner with no headers, bullets, or meta-commentary, and each stays within the 60-word cap. |
| Consistency | 4 | judge | All three runs share the same structural sequence (problem statement → severity → scope reassurance → root cause/rollback → retry instruction → next update) and cover the same core facts. No run contradicts another. Minor coverage variation: Run 3 uniquely includes 'successful charges are processing normally' and root-cause detail ('a bad deploy to charge authorization'); runs differ in whether 'safely' qualifies the retry instruction. Meaning and structure are stable; wording variation is expected paraphrase. [lexical similarity ratio: 0.682] |
| Tone/Style | 5 | judge | The tone is calm, professional, and action-oriented, appropriate for a B2B payments status page. It avoids apology boilerplate and hype while still being reassuring and clear. |
| Safety | 5 | judge | The outputs are operational incident updates only, with no unsafe, biased, or inappropriate content. The workaround is presented as safe and non-abusive, consistent with the prompt facts. |
| Efficiency | 3 | judge | All three runs stay well inside the 60-word budget (53, 50, 60 words) and avoid padding or filler. Token counts of 86–96 are reasonable for the prose length. Run 3 uses its budget more fully by adding 'successful charges are processing normally' and root-cause specifics, extracting additional informational value for the same budget spend. No run wastes tokens on boilerplate. Minor inefficiency: including lower-priority details (exact start time, 'rollback in progress', eu-central-1 carve-out) in all runs could have freed budget for the missing explicit double-charge safety callout. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 5 | 4 | 4 | 1 | 0.47 |
| Completeness ⚠ | 4 | 5 | 4 | 3 | 2 | 0.82 |
| Format Compliance ⚠ | 4 | 5 | 5 | 1 | 4 | 1.89 |
| Consistency ⚠ | 4 | 5 | 4 | 3 | 2 | 0.82 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 5 | 4 | 1 | 4 | 1.7 |

- **Self-preference delta:** +8.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.86 (max 4).

Tokens (avg output): 90 | Latency (avg): 1.75s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model provided an exceptionally accurate and complete response, delivering all critical information with a pitch-perfect professional and action-oriented tone. Consistency across runs was also excellent. However, it critically failed the explicit length-budgeting constraint by consistently producing 61 words (1 word over the 60-word limit) and did not adhere to the 'single continuous status-banner message' format, opting instead for a multi-line, header-like structure. These format and efficiency deviations prevent a top score despite the high quality of the content itself.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All incident facts are faithfully reproduced without distortion across all three runs. The ~40% failure rate, 503 codes, POST /v1/charges, idempotency-key workaround and its no-double-charge guarantee, 15:00 UTC next-update, eu-central-1 carve-out, and scope reassurance (refunds/payouts/dashboard unaffected) are all correctly stated. |
| Completeness | 5 | judge | Every required element is present in all runs: (1) what is broken and the failure rate, (2) the idempotency-key workaround with the explicit no-double-charge safety call-out (the single most decision-relevant fact), (3) next-update time. Scope reassurance and rollback status are also included, none of the mandated critical-content items are dropped. |
| Format Compliance | 3 | judge | The format specification is explicit: 'a single continuous status-banner message,' 'Plain prose suitable for a status-page banner — no headers.' All three runs violate both constraints. The first line functions unmistakably as a display header, and 'Action:' functions as a section label. Markdown bold and backtick formatting further departs from plain prose. The word count (~48–52 words, depending on counting convention) is within the 60-word cap but sits below the 55–60 sweet spot cited in the reference. |
| Consistency | 5 | judge | The runs are semantically and structurally stable: each delivers the same core incident banner with the same key facts in the same order—degraded charges, region carve-out, unaffected products, idempotent retry, rollback, next update. Minor wording and formatting differences do not amount to inconsistency. [lexical similarity ratio: 0.897] |
| Tone/Style | 5 | judge | The tone is calm, professional, and action-oriented, appropriate for a B2B payments status banner. It avoids apology boilerplate and hype while clearly instructing the customer what to do. |
| Safety | 5 | judge | The content is benign and operational, with no harmful, biased, or inappropriate material. It safely communicates incident status and a documented retry workaround. |
| Efficiency | 2 | judge | The outputs are functionally good but inefficient relative to the 55-60 word target because they run at 116-117 output tokens and include formatting overhead like markdown emphasis and inline code, which is likely token-expensive for a concise status banner. They do not bloat with apology text, but they are still substantially longer than necessary for the level of content delivered. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 3 | 5 | 2 | 2 | 3 | 1.41 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 2 | 3 | 2 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 1 (max 3).

Tokens (avg output): 116 | Latency (avg): 3.61s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Strong factual alignment and good incident-communications tone. The main weakness is likely length-budget discipline/format tightness: the responses are structurally close but use extra markdown/framing and may exceed the intended 60-word banner constraint, reducing format compliance and efficiency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs are factually aligned with the incident facts: they identify intermittent POST /v1/charges failures, the ~40%/503 behavior, the eu-central-1 exception, unaffected surfaces, and the next update time. No hallucinated or contradictory facts appear. |
| Completeness | 4 | judge | The core required facts are present across runs, especially the decisive workaround and next update time. However, the responses are a bit thinner than the ideal because they omit or compress some lower-priority context like explicitly stating that successful charges are processing normally and that this is a degradation rather than a full outage (though Run 1 includes "Degradation" and Run 3 includes "Ongoing incident"). |
| Format Compliance | 2 | judge | The prompt specifies 'plain prose — no headers.' All three runs use markdown bold formatting as headers or section labels, violating this requirement. Run 1 opens with a bolded title header and a bolded 'Action:' label; runs 2 and 3 use a bolded 'Workaround:' label; run 3 has a bolded 'Ongoing incident' opener. Word counts are within the 60-word cap, there are no bullet lists, and no meta-commentary, so the shape is correct, but the repeated formatting violation is significant. |
| Consistency | 3 | judge | The core factual content (POST /v1/charges failing, ~40% 503s, idempotency-key workaround, 15:00 UTC update, eu-central-1 exclusion, refunds/payouts/dashboard unaffected) is present across all runs. However, structural and coverage differences are meaningful: Run 2 omits start time and rollback status, making it noticeably thinner than Runs 1 and 3; header labeling varies (bold title in Run 1 vs. inline header in Run 3 vs. no header in Run 2); 'safely' modifier appears in Runs 1 and 3 but not Run 2. Same core answer, but coverage and structure differ across runs. [lexical similarity ratio: 0.525] |
| Tone/Style | 4 | judge | The tone is calm, professional, and action-oriented, appropriate for a B2B status-page banner. Minor stylistic issues keep it short of perfect: the use of markdown headings and the investigative framing in Run 2 are a bit less polished than a direct status banner, but the register is broadly correct and reassuring without apology boilerplate. |
| Safety | 5 | judge | The outputs are safe and non-harmful. They avoid sensitive content, biased language, or inappropriate claims, and they provide the intended operational guidance without encouraging unsafe actions. |
| Efficiency | 3 | judge | The actual banner text across all runs is concise and within the 60-word cap with no padding — that is efficient at the output level. However, the output token counts are very high relative to the text produced: Run 2 delivers ~35 words of usable output at 1255 tokens; Run 3 delivers ~40 words at 819 tokens; Run 1 delivers ~50 words at 583 tokens. This strongly suggests heavy thinking-token expenditure. For a constrained prose task of this simplicity, the per-word token cost is expensive. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Format Compliance | 2 | 3 | 2 | 2 | 1 | 0.47 |
| Consistency | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 886 | Latency (avg): 5.02s | Runs: 3

---

## Prompt Under Test

```text
Respond in no more than 60 words.

If you cannot fit a complete answer within the budget, prioritize the most decision-relevant content for an affected customer and explicitly omit lower-priority context. Do not pad to reach the budget.

Task: Write the public status-page banner for an ongoing incident, addressed to our customers (businesses who integrate our payments API). Use the facts below. The banner must let an affected integrator decide what to do right now.

Incident facts:
- Started 14:05 UTC; still ongoing.
- Card charge creation (POST /v1/charges) is failing intermittently — roughly 40% of attempts return HTTP 503.
- Refunds, payouts, and the dashboard are fully unaffected.
- Root cause identified: a bad deploy to the charge-authorization service; rollback in progress.
- Workaround: charge requests are safely idempotent, so customers can retry failed charges with the same Idempotency-Key without risk of double-charging.
- Next update will be posted by 15:00 UTC.
- Affects all regions except eu-central-1.
- This is a degradation, not a full outage; successful charges are processing normally.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
We’re seeing intermittent failures on card charge creation (POST /v1/charges) since 14:05 UTC, affecting all regions except eu-central-1. About 40% of requests return HTTP 503. Refunds, payouts, and the dashboard are unaffected. Root cause identified; rollback in progress. You can safely retry failed charges with the same Idempotency-Key. Next update by 15:00 UTC.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
