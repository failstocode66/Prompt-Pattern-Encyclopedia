# Eval: strict-output-format

**Date:** 2026-06-29 15:50 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| claude-sonnet-4-6 | **4.9 (Strong)** | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| gemini-2.5-flash | **3.6 (Solid)** | 4 | 5 | 2 | 3 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> All three runs achieve a near-perfect extraction: correct severity up-mapping (SEV-1→critical), null rather than fabricated 0 for missing response time, faithful backslash and double-quote escaping inside error_message, and clean bare JSON with no prose or fences. The response is maximally efficient, fully consistent across runs, and free of any safety concerns.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | Every field maps correctly: ticket_id is the clean 'A-2291', customer_email preserves the apostrophe and + without over-escaping, severity is correctly up-mapped from SEV-1 to 'critical', product_versions and tags are correct arrays, error_message has proper \" and \\ escaping so it decodes to the literal source text, minutes_to_first_response is null (not fabricated), and resolved is boolean false. |
| Completeness | 5 | judge | All eight required schema keys are present and populated in every run. No field is missing, shallow, or omitted. |
| Format Compliance | 5 | judge | The output matches the required strict format: exactly one JSON object, no surrounding prose, no markdown fences, no trailing text, and all fields are double-quoted and parseable. The field order also matches the schema order. |
| Consistency | 5 | judge | All three runs are semantically and structurally identical, with only trivial repetition across runs. There is no divergence in fields, ordering, or quality. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | The tone is perfectly machine-facing and zero-prose, exactly as requested for parser-destined output. There is no commentary or human-facing explanation. |
| Safety | 5 | judge | The content is benign and free of harmful, biased, or inappropriate material. It simply extracts ticket data. |
| Efficiency | 5 | judge | At 100 output tokens per run, the model is very concise for a fully formed strict JSON object and does not waste tokens on explanation. Quality is high, so the token usage is efficient. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 5 | 5 | 5 | 0 | 0.0 |

- **Self-preference delta:** -2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.29 (max 1).

Tokens (avg output): 100 | Latency (avg): 1.59s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs deliver a perfect, byte-identical JSON output that satisfies every requirement in the rubric. The two hardest discriminating points—correct \" and \\ escaping inside error_message to yield valid JSON that decodes back to the exact source literal, and emitting null rather than fabricating a value for minutes_to_first_response—are both handled flawlessly. Keys appear in schema order, severity is correctly mapped to 'critical', the email apostrophe and + are verbatim, and there is zero prose outside the JSON object. Efficiency is excellent at 100 tokens per run for a fully correct payload. Consistency is perfect across all three runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are mostly correct and on-task, but there is a material content error: the error_message drops the required literal text after the quoted token and does not preserve the full source string verbatim. The source says `parser threw Unexpected token "}" at C:\app\config.json:42 — backslash in path, embedded quotes`, but all runs output only `Unexpected token "}" at C:\app\config.json:42`. Other fields are correct, including `severity":"critical"` and `minutes_to_first_response":null`. |
| Completeness | 5 | judge | All eight required schema keys are present in every run. No field is missing, shallow, or omitted. The two discriminating edge cases—null for the missing response time and correct escaping of the error message—are both handled correctly. |
| Format Compliance | 5 | judge | Each run is a single, parseable JSON object with no surrounding prose or code fences, and the keys are presented in the required order. The output is strict-JSON friendly and uses proper escaping for quotes and backslashes. |
| Consistency | 5 | judge | All three runs are structurally and semantically identical, with no divergence in field selection, formatting, or quality. Wording variation is absent, and the same core answer is repeated exactly. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | The response matches the intended machine-facing, zero-prose extractor style perfectly: no commentary, no explanation, only structured JSON. |
| Safety | 5 | judge | The content is benign and task-focused, with no harmful, biased, or inappropriate material. |
| Efficiency | 5 | judge | At 100 tokens per run, the outputs are compact and consistent with the amount of information delivered. The model does not waste tokens on prose or padding. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 3 | 5 | 5 | 2 | 0.94 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 5 | 5 | 5 | 0 | 0.0 |

- **Self-preference delta:** +1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy.
- **Panel mean spread/dim:** 0.43 (max 2).

Tokens (avg output): 100 | Latency (avg): 2.28s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Mostly correct extraction with one major format issue (fences in Runs 1 and 3) and one semantic error in Run 3’s over-escaped error_message. Best run is Run 2; overall strong on content but not a perfect prompt-pattern match.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The outputs are on-task and mostly correct. Runs 1 and 2 correctly map SEV-1 to "critical", preserve the email, set minutes_to_first_response to null, and return the required arrays/boolean. The main accuracy issue is Run 3 over-escapes the error message content, changing the literal text. Also, in Runs 1/2 the error_message appears to preserve the visible text but the backslash handling is not fully verifiable from the rendered output alone. |
| Completeness | 5 | judge | All eight schema fields are present and populated in every run. Severity synonym (SEV-1/urgent→critical) mapped, product_versions and tags correctly rendered as arrays, null used for the unstated response time, resolved correctly set to false. |
| Format Compliance | 2 | judge | The intended shape is a raw JSON object with no surrounding prose or markdown fences. Run 2 complies best. Runs 1 and 3 violate the format by wrapping the JSON in ```json fences, which is explicitly disallowed. Because format compliance is judged across runs, this is a meaningful deviation from the requested output contract. |
| Consistency | 3 | judge | The core fields (ticket_id, email, severity, versions, null, tags, resolved) are stable across all three runs. However, error_message encoding diverges materially: Runs 1 and 2 use correct single-level escaping while Run 3 uses double-level over-escaping—a content difference, not mere wording variation. Format also splits 2-vs-1 on fences. These are structural and correctness divergences. [lexical similarity ratio: 0.956] |
| Tone/Style | 4 | judge | The JSON field values are purely machine-facing with zero embedded commentary—exactly right for a parser-destined output. Small deduction because the code fences in runs 1 and 3 inject non-parseable formatting markers into what must be pristine machine output, degrading tone compliance for typical behavior. |
| Safety | 5 | judge | No harmful, biased, or inappropriate content is present. The outputs are routine structured-ticket extraction data and contain no safety concerns. |
| Efficiency | 2 | judge | The outputs are very verbose for a simple JSON extraction task, especially Runs 1 and 3 at 848 and 1427 output tokens respectively, likely due to fence wrapping and/or inefficiencies. The quality delivered does not justify that token usage. Run 2 is much tighter, but the typical behavior across runs is wasteful. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 2 | 2 | 2 | 2 | 0 | 0.0 |
| Consistency | 3 | 4 | 3 | 1 | 3 | 1.25 |
| Tone/Style | 4 | 5 | 4 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 3 | 1 | 2 | 0.82 |

- **Self-preference delta:** -5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency, Consistency.
- **Panel mean spread/dim:** 1.14 (max 3).

Tokens (avg output): 1032 | Latency (avg): 5.22s | Runs: 3

---

## Prompt Under Test

```text
Respond with only a single JSON object that conforms exactly to the schema below. No explanation, no preamble, no trailing commentary, no markdown code fences.

Schema (all keys required, in this order):
{
  "ticket_id": string,
  "customer_email": string | null,
  "severity": "low" | "medium" | "high" | "critical",
  "product_versions": array of strings,
  "error_message": string,
  "minutes_to_first_response": number | null,
  "tags": array of strings,
  "resolved": boolean
}

Rules:
- Use null for any field the source does not state. Do not guess or fabricate values.
- product_versions and tags must be arrays even if there is one element or none ([]).
- severity must be exactly one of the four allowed lowercase strings; map any synonym in the source to the closest allowed value.
- Numbers must be JSON numbers, not strings.
- Preserve the error_message text verbatim, including its internal punctuation.

Source ticket (single raw log line):
TICKET#A-2291 | reporter: o'neil+billing@acme.co | sev: SEV-1 (urgent) | affects builds 3.10.0-rc2 and 3.9.4 | symptom: parser threw `Unexpected token "}" at C:\app\config.json:42` — backslash in path, embedded quotes | first agent reply after ~ (still waiting) | labels: parser, regression, windows-only | status: open
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
{"ticket_id":"A-2291","customer_email":"o'neil+billing@acme.co","severity":"critical","product_versions":["3.10.0-rc2","3.9.4"],"error_message":"parser threw `Unexpected token \"}\" at C:\\app\\config.json:42` — backslash in path, embedded quotes","minutes_to_first_response":null,"tags":["parser","regression","windows-only"],"resolved":false}
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
