# Eval: low-latency-optimization

**Date:** 2026-06-29 12:06 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.3 (Solid)** | 4 | 5 | 3 | 4 | 4 | 5 | 5 |
| claude-sonnet-4-6 | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| gemini-2.5-flash | **4 (Solid)** | 3 | 5 | 5 | 3 | 5 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> Strong mostly-correct 8-line terse answers with one mild format deviation in run 3. Overall high quality, but not perfect due to the extra text on item 2 and minor casing drift.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All runs are on-task and nearly all factual answers are correct. The main issue is run 3 adds an unnecessary explanation on item 2 (“422 Unprocessable Entity”), which is still correct but not the exact bare answer expected for the pattern. No trap-item factual errors appear. |
| Completeness | 5 | judge | All 8 numbered items are answered in every run with no omissions or shallow handling. |
| Format Compliance | 3 | judge | The shape is correct in all runs: exactly 8 numbered lines, in order, with no preamble or closing text. But exact format compliance is not perfect because run 3 violates the bare-answer requirement by appending explanation text on line 2, and run 3 also changes casing on line 6. |
| Consistency | 4 | judge | The runs are highly consistent in content and structure, with identical answers across runs 1 and 2 and only minor wording/casing drift in run 3. There is no contradiction or structural divergence, just a small elaboration on item 2 and capitalization variation on item 6. [lexical similarity ratio: 0.927] |
| Tone/Style | 4 | judge | Runs 1 and 2 are pitch-perfect machine-terse output. Run 3's extra label on line 2 edges toward explanatory rather than programmatic, though still very close to correct. Minor but real deviation from the instruction 'bare value'. |
| Safety | 5 | judge | The content is benign technical information only, with no harmful, abusive, or policy-sensitive material. |
| Efficiency | 5 | judge | Runs 1 and 2 at 46 tokens are essentially the theoretical minimum for 8 terse answers. Run 3 at 49 tokens adds only 3 tokens for the extra label — negligible overhead. No padding, preamble, or explanation anywhere. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 5 | 4 | 1 | 0.47 |
| Completeness | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 3 | 3 | 4 | 3 | 1 | 0.47 |
| Consistency ⚠ | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 5 | 4 | 3 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 4 | 5 | 5 | 1 | 0.47 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Tone/Style.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 47 | Latency (avg): 1.44s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> A near-perfect response set. All three runs are identical, each producing exactly 8 bare-value lines in the required format with zero preamble or caveats, and every one of the 8 facts is correct — including all five trap answers (422, O(n), False, READ COMMITTED, 16). Token efficiency is essentially optimal. This is the gold-standard result for the low-latency-optimization pattern: terse format and correct answers achieved simultaneously with full consistency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All 8 answers are correct for the prompt, including the trap items. The response gives 422 (not 400), O(n) (not O(1)), False, READ COMMITTED, 16, and 0, matching the reference exactly. |
| Completeness | 5 | judge | The response addresses every item in the 8-item list and provides exactly one answer per line with no missing components. |
| Format Compliance | 5 | judge | It matches the required format exactly: 8 numbered lines, each in the form `N. <answer>`, with no preamble or extra commentary. |
| Consistency | 5 | judge | Across all three runs, the model produces the same content, structure, and quality with no semantic differences. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | The output is maximally terse, programmatic, and devoid of hedging or conversational framing, which fits the stated machine-consumed audience. |
| Safety | 5 | judge | The content is benign and contains no harmful, biased, or inappropriate material. |
| Efficiency | 5 | judge | The outputs are extremely concise and deliver perfect quality with no wasted tokens; 49 output tokens for 8 exact answers is tight for this task. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 5 | 5 | 5 | 0 | 0.0 |

- **Self-preference delta:** +0 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0 (max 0).

Tokens (avg output): 49 | Latency (avg): 2.38s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Overall, the model is highly format-stable and concise in structure, but it fails a critical trap item on HTTP status code in 2 of 3 runs, which materially lowers accuracy. Consistency is strong except for that semantic disagreement on line 2.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Runs 1 and 2 both give '400' for item 2, falling into exactly the trap the rubric identifies as the primary silent-wrongness failure mode. Run 3 correctly answers '422'. The remaining 7 items (5432, O(n), False, git reset --hard HEAD, Read Committed, 16, 0) are correct in all three runs. Because the typical/majority behavior (2 of 3 runs) gets the most critical trap item wrong, accuracy cannot exceed 3. |
| Completeness | 5 | judge | All 8 requested items are answered in every run, with no missing lines and no extra commentary. The output covers each prompt item in order. |
| Format Compliance | 5 | judge | The outputs follow the required 8-line numbered format exactly, with one `N. <answer>` per line and no preamble or trailing text. Minor capitalization differences do not violate the specified format. |
| Consistency | 3 | judge | Runs 1 and 2 are structurally and semantically identical. Run 3 diverges on item 2 (422 vs 400), which is a meaningful factual disagreement on the hardest item, not just a wording variation. Format and structure are stable across all three runs, but the factual divergence on item 2 prevents a higher score. [lexical similarity ratio: 0.984] |
| Tone/Style | 5 | judge | The responses are terse, programmatic, and non-conversational, matching the intended machine-consumed style. There is no hedging, explanation, or politeness. |
| Safety | 5 | judge | The content is benign and task-focused. There is no harmful, biased, or inappropriate material. |
| Efficiency | 2 | judge | The outputs are concise in absolute terms, but the token counts are relatively high for a task that required only eight short lines. Run 3 in particular used 777 tokens for a brief answer set, suggesting notable inefficiency relative to quality delivered, especially since one important answer was wrong in runs 1 and 2 and the model still produced substantial overhead. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 3 | 1 | 2 | 0.82 |

- **Self-preference delta:** -1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.57 (max 2).

Tokens (avg output): 525 | Latency (avg): 3.09s | Runs: 3

---

## Prompt Under Test

```text
Answer directly. No preamble, no reasoning, no caveats, no restating the question. First token is the answer.

You are the backend for an inline developer-tools autocomplete: each query gets one short answer, consumed programmatically. Output exactly 8 lines, formatted `N. <answer>`, in order, nothing before line 1 or after line 8.

1. Default port for PostgreSQL.
2. HTTP status code for a request that is syntactically valid but semantically wrong (fails validation).
3. Time complexity of retrieving an element by key from a hash map, worst case.
4. In Python 3, what does `0.1 + 0.2 == 0.3` evaluate to?
5. Git command to discard all uncommitted changes in the working tree and staged area, restoring to HEAD.
6. Default isolation level of a PostgreSQL transaction.
7. Number of bytes in a UUID (the value itself, not its hex-string representation).
8. Bash exit status indicating success.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
1. 5432
2. 422
3. O(n)
4. False
5. git reset --hard HEAD
6. READ COMMITTED
7. 16
8. 0
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
