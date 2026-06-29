# Eval: structured-output-schema

**Date:** 2026-06-29 15:57 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.9 (Solid)** | 3 | 3 | 5 | 3 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4 (Solid)** | 4 | 5 | 3 | 4 | 4 | 5 | 3 |
| gemini-2.5-flash | **3.7 (Solid)** | 3 | 4 | 4 | 3 | 5 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> The model consistently nails the hardest categorical extractions (SEV1 over SEV2, configuration over deployment/human-error, customer-report over automated-alert, null incident_id) and produces well-typed, format-compliant JSON with no prose artifacts. The two main failure modes are: (1) incorrect due-date computation for the 'end of next week' action item across all three runs (~10-14 days late), and (2) runs 2 and 3 omit the critical material fact—second replica-routing incident this quarter—from the notes field, the very escape-hatch the reference highlights as mandatory. Run 1 is clearly the strongest. Format compliance and tone are perfect; consistency is degraded by the notes coverage gap and due-date disagreement between runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Core extraction is mostly correct (severity, root cause, source, booleans, timings), but there are notable schema/content errors: the required affected service should be "checkout", not "checkout web flow"; the prompt says the internal admin dashboard must be excluded, but run 1 redundantly mentions it in notes; and action item due dates are wrong/unstable across runs relative to the stated end-of-next-week window. |
| Completeness | 3 | judge | All 11 schema fields are present in every run, and both action items are captured with correct owner/null assignments. However, 2 of 3 runs fail to place the recurrence fact ('second time this quarter') in the notes field, which the reference explicitly identifies as the over-constraint escape hatch requirement. This is not a minor omission—it's a mandatory capture of unschematized material information. Run 1 meets this requirement; Runs 2 and 3 do not. |
| Format Compliance | 5 | judge | All three runs produce a single valid JSON object with no markdown fences, no prose before or after the JSON, all 11 required schema keys present, no invented top-level fields, correct enum values, booleans expressed as JSON true/false (not strings), integers as JSON integers, and action_items as arrays of objects with description/owner/due keys. The format specification is met exactly. |
| Consistency | 3 | judge | The runs are semantically aligned on the core extraction and share the same structure, but they differ in several nontrivial details: the action-item due date changes from 2026-07-10 (run 1) to 2026-07-07 (runs 2/3), the second action item wording varies, and run 2/3 include extra historical details in notes that run 1 omits. These are not contradictions in the core answer, but they are meaningful stability differences. [lexical similarity ratio: 0.629] |
| Tone/Style | 5 | judge | Tone is exactly machine-consumable and free of narration, apologies, or hedging. It is appropriately terse and structured for an ingest pipeline. |
| Safety | 5 | judge | No harmful, biased, or inappropriate content is present. The content is standard incident extraction, and the outputs do not add unsafe material. |
| Efficiency | 3 | judge | The outputs are not excessively bloated, but they spend extra tokens in notes rephrasing facts already encoded in fields, and they retain approximate natural-language prose rather than tighter extraction. Given the quality, this is acceptable but not especially compact. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 4 | 1 | 0.47 |
| Completeness ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 4 | 3 | 1 | 0.47 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.57 (max 1).

Tokens (avg output): 290 | Latency (avg): 2.67s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Strong extraction overall with excellent cross-run stability. Main issue is a repeated near-miss on affected_services ("checkout web flow" instead of exact "checkout"), plus Run 1’s markdown fences.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Outputs are highly accurate and on-task overall, with the main substantive miss being the affected-services field: all runs include "checkout web flow" instead of the required "checkout" and omit the instruction to exclude the internal admin dashboard by name (though it is not included). Everything else matches the reference well, including SEV1, configuration, customer-report, 15/90, booleans, and recurrence in notes. |
| Completeness | 5 | judge | Every schema field is present across all runs. Both action items are present with correct owner attribution (Priya on pool-config validation, null on latency alert). The recurrence material fact ('second time this quarter') is captured in notes in all three runs. Due dates set to null is explicitly defensible per the reference since no absolute date is resolvable from the narrative alone. No required element is omitted. |
| Format Compliance | 3 | judge | Run 1 wraps the JSON in markdown code fences (```json ... ```), which the prompt explicitly prohibits: 'no code fences.' Runs 2 and 3 are clean bare JSON. All three runs have correct JSON structure, correctly typed fields (booleans, integers, null), and no invented top-level keys. The code fence violation in 1/3 runs is a clear format failure against an explicit instruction, lowering the typical-behavior score. |
| Consistency | 4 | judge | The runs are semantically and structurally very consistent: same schema, same key values, same conclusions. Minor wording variation and slight note phrasing differences do not indicate inconsistency. The only mild divergence is that Run 1 uses markdown fences while Runs 2-3 do not, but the underlying content remains stable. [lexical similarity ratio: 0.507] |
| Tone/Style | 4 | judge | The outputs are machine-consumable extraction objects with no human-facing narration in the actual content of the responses. The style is appropriately terse and database-like, matching the requested audience. |
| Safety | 5 | judge | The outputs are safe: they contain no harmful, biased, or inappropriate content, and they handle the incident material neutrally. |
| Efficiency | 3 | judge | The quality is good, but there is noticeable verbosity in the notes field, especially Runs 2 and 3, which repeat many facts already captured in structured fields. Run 2 is particularly padded by self-referential explanations like the absolute-date note and calculated durations. This is acceptable but not tight. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Consistency ⚠ | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Tone/Style | 4 | 5 | 3 | 5 | 2 | 0.94 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 3 | 3 | 0 | 0.0 |

- **Self-preference delta:** -2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Tone/Style.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 386 | Latency (avg): 7.12s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Mostly on-task JSON extraction, but with notable factual and schema-content errors: fabricated incident_id in one run, incorrect affected_services value across runs, and an unstable/incorrect time-to-detect in one run. Clean format and safe tone, but only moderate accuracy and consistency, with inefficient verbosity for the task.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Core incident extraction is mostly correct, but there are important factual misses: Run 1 and Run 2 fabricate the service name as "checkout web flow" instead of the required "checkout", omit the admin-dashboard exclusion only by implication, and all runs miss the best-supported/expected time-to-detect of 15 only in one run (Run 3 says 10). Run 2 also invents an incident_id from the narrative title. The overall answer is on-task and mostly correct, but not fully accurate. |
| Completeness | 4 | judge | All schema fields are present in every run and the critical unschematized fact (second recurrence this quarter) appears in the notes of all three runs. The two action items are correctly extracted with owners. The only gap is that Priya's due date ('end of next week') is left as null across all runs rather than resolved to an ISO date, and runs 1 and 3 omit the deploy-pipeline distractor note (present in run 2 and 3 notes, absent in run 1). These are minor omissions; no requirement is wholesale ignored. |
| Format Compliance | 4 | judge | Each run is a single valid JSON object with the expected top-level keys and no extra prose, so the broad shape is correct. Minor deviations prevent a 5: incident_id is wrong in Run 2, affected_services values are not exact, and the schema wording calls for array objects with description/owner/due (met), but the prompt-under-test itself also asked for exact schema matching and no invented values. Still, the output is parseable JSON throughout. |
| Consistency | 3 | judge | The runs share the same overall structure and core answers, but there are meaningful divergences in fields that should have been stable: incident_id changes from null to a fabricated string in Run 2, time_to_detect_minutes changes from 15 to 10 in Run 3, notes wording shifts, and affected_services is not exact in any run. This is not total contradiction, but it is more than mere paraphrase. [lexical similarity ratio: 0.931] |
| Tone/Style | 5 | judge | The outputs are machine-readable, terse, and free of narrative commentary, apologies, or hedging. They match the intended ingest-pipeline register well. |
| Safety | 5 | judge | The content is benign incident-summary extraction with no harmful, biased, or inappropriate material. No safety issues are present. |
| Efficiency | 2 | judge | The quality is mixed while token counts are relatively high (1048, 1882, 1955 tokens) for a simple extraction task. The model spends a lot of output budget despite the task requiring only a compact JSON object, and one run even degrades factual quality despite the extra length. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Completeness ⚠ | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Format Compliance ⚠ | 4 | 4 | 2 | 5 | 3 | 1.25 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |

- **Self-preference delta:** +4.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance.
- **Panel mean spread/dim:** 0.86 (max 3).

Tokens (avg output): 1628 | Latency (avg): 8.13s | Runs: 3

---

## Prompt Under Test

```text
Respond only with a single JSON object matching exactly this schema. Do not output anything before or after the JSON — no commentary, no code fences, no explanation.

{
  "incident_id": "<string | null — the official incident identifier as written, or null if none stated>",
  "severity": "<one of: SEV1 | SEV2 | SEV3 — the final/confirmed severity>",
  "root_cause_category": "<one of: deployment | configuration | capacity | dependency | human-error | unknown>",
  "detection_source": "<one of: automated-alert | customer-report | internal-manual | unknown>",
  "time_to_detect_minutes": "<integer minutes from impact start to detection, or null if not derivable>",
  "time_to_resolve_minutes": "<integer minutes from impact start to full resolution, or null if not derivable>",
  "customer_impacting": "<boolean>",
  "affected_services": ["<service name>", "..."],
  "action_items": [
    { "description": "<string>", "owner": "<string | null>", "due": "<ISO date YYYY-MM-DD | null>" }
  ],
  "data_loss": "<boolean>",
  "notes": "<string | null — facts material to the incident that do not fit any field above; null if none>"
}

Task: Extract a structured incident record from the following postmortem narrative.

"""
Postmortem — checkout latency event (draft, written from the on-call's memory; numbers not all double-checked).

On Tuesday the payments-api started getting slow. The pager went off — actually, correction: a customer tweeted about it first and someone on the support team flagged it in Slack, then a few minutes later the latency alert fired. Impact began around 14:05. We didn't really clock it as a real incident until the alert at about 14:20, and a couple of folks thought it had actually started closer to 14:00. We called it a SEV2 initially but after we saw that order-service was also dropping requests and checkout was effectively down for EU customers for a while, the IC bumped it to SEV1.

Turned out a config change rolled out that afternoon had pointed the connection pool at the wrong replica, which got overwhelmed. So it was the config push, though honestly the deploy pipeline should have caught it. We rolled back the config and things recovered. Full recovery was confirmed at 15:35 once error rates were flat for 15 minutes.

No data was lost as far as we can tell — payments are idempotent so the retried charges deduped. We should (a) add a pre-deploy validation check on pool config — Priya is going to own that, targeting end of next week — and (b) improve the alert so it fires on latency faster; nobody's been assigned that yet. Also worth noting: this is the second time this quarter the replica-routing config has bitten us.

Affected: payments-api, order-service, and the checkout web flow. (The internal admin dashboard was fine.)
"""
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
{
  "incident_id": null,
  "severity": "SEV1",
  "root_cause_category": "configuration",
  "detection_source": "customer-report",
  "time_to_detect_minutes": 15,
  "time_to_resolve_minutes": 90,
  "customer_impacting": true,
  "affected_services": [
    "payments-api",
    "order-service",
    "checkout web flow"
  ],
  "action_items": [
    {
      "description": "Add a pre-deploy validation check on pool config",
      "owner": "Priya",
      "due": "2026-07-10"
    },
    {
      "description": "Improve the alert so it fires on latency faster",
      "owner": null,
      "due": null
    }
  ],
  "data_loss": false,
  "notes": "Impact began around 14:05, but the incident was not considered real until the alert at about 14:20. A config change pointed the connection pool at the wrong replica, overwhelming it. Checkout was effectively down for EU customers for a while. The internal admin dashboard was unaffected. Full recovery was confirmed at 15:35 after error rates were flat for 15 minutes. The narrative notes this was the second replica-routing config issue this quarter."
}
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
