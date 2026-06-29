# Eval: flipped-interaction

**Date:** 2026-06-29 11:35 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.4 (Solid)** | 4 | 4 | 5 | 3 | 5 | 5 | 5 |
| claude-sonnet-4-6 | **4.1 (Solid)** | 3 | 3 | 5 | 5 | 4 | 5 | 4 |
| gemini-2.5-flash | **4.6 (Strong)** | 5 | 5 | 5 | 4 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> The model follows the flipped-interaction pattern correctly in structure across all runs — one question per turn, no premature SQL or optimization plan. Runs 1 and 3 select the canonical highest-leverage first question (query + EXPLAIN ANALYZE BUFFERS plan), earning full marks on the diagnostic strategy. Run 2 diverges by substituting a table-name request for the plan, which is a weaker opener that costs both accuracy and consistency. All runs are exceptionally efficient and format-compliant. The main gaps are: Run 2's suboptimal diagnostic choice, the absence of any brief role acknowledgment or signal that further questions will follow, and the resulting consistency penalty from Run 2's meaningful divergence from the other two runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Typical behavior is on-task and mostly aligned with the benchmark: runs 1 and 3 ask the highest-leverage diagnostic question and specifically request the query plus EXPLAIN ANALYZE BUFFERS. However, run 2 is a weaker, downstream question about table names, which the reference explicitly says should cost accuracy because it asks schema/table info before the plan. |
| Completeness | 4 | judge | The response set covers the core requirement of asking one diagnostic question and, in 2 of 3 runs, asks for the ideal artifacts. It misses the bonus nuance of a brief role acknowledgment and why this is the first question, but those are optional. The main incompleteness is run 2 not requesting the plan at all and therefore not matching the strongest expected opener across all runs. |
| Format Compliance | 5 | judge | All three runs produce exactly one prose question with no numbered/bulleted list, no SQL, no optimization plan, and no premature 'I have enough to proceed' signal. The format specification is met precisely in every run. |
| Consistency | 3 | judge | Runs 1 and 3 are semantically and structurally nearly identical, both requesting the query plus EXPLAIN (ANALYZE, BUFFERS). Run 2 is a meaningful semantic divergence: it replaces the plan request with a request for table names, producing a measurably weaker diagnostic question. This is not mere wording variation — it represents a different and inferior diagnostic strategy, affecting quality stability across runs. [lexical similarity ratio: 0.686] |
| Tone/Style | 5 | judge | The tone is professional, concise, and consultative, matching a senior performance consultant intake. It is not chatty or padded, and the wording is clear and actionable. |
| Safety | 5 | judge | The content is benign and work-related, with no harmful, biased, or inappropriate material. It only requests diagnostic information relevant to PostgreSQL performance. |
| Efficiency | 5 | judge | Token counts are extremely low (23–37 tokens) for the task delivered. There is zero padding, no preamble, no redundant explanation. The quality-per-token ratio is high in Runs 1 and 3; Run 2 is even shorter but at the cost of accuracy, not efficiency. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Completeness | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Format Compliance | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 4 | 5 | 5 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.57 (max 1).

Tokens (avg output): 32 | Latency (avg): 1.43s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model performs well on adherence to most negative constraints, format, tone, and safety. It consistently delivers a concise, professional, single-turn response. Its primary weakness lies in 'Accuracy' and 'Completeness' as it consistently fails to ask the most important and leveraged first question, omitting the critical `EXPLAIN (ANALYZE, BUFFERS)` plan which is necessary for meaningful diagnosis. While efficient for the content it provides, its efficiency is slightly hindered by the quality gap. Consistency is strong for core intent and structure, with minor variations in phrasing.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The responses are on-topic and relevant to the task, but they ask for the query text only instead of the highest-leverage diagnostic pair (query + EXPLAIN ANALYZE/BUFFERS). That is a weaker first question than the reference recommends, though still useful. |
| Completeness | 3 | judge | The flipped-interaction pattern requires identifying the single highest-leverage diagnostic question. The prompt instructions and rubric both specify that the canonical opener bundles the query text AND its execution plan. All runs cover only one of the two required components (the SQL text), leaving the plan—equally essential—to a subsequent turn. One substantive requirement is missed. |
| Format Compliance | 5 | judge | Each run is a single conversational question and contains no extra substantive content, lists, SQL, or premature optimization plan. This matches the required single-question format. |
| Consistency | 5 | judge | The three runs are semantically stable and structurally identical: each asks for the slow query’s SQL text as the sole question. Wording varies slightly, but the core intent and single-question format remain constant. [lexical similarity ratio: 0.719] |
| Tone/Style | 4 | judge | The tone is professional, concise, and consultative, which fits the intended audience well. It is slightly plain and lacks the ideal senior-consultant framing or brief role acknowledgment, but it is still appropriate. |
| Safety | 5 | judge | The outputs are benign, non-sensitive, and contain no harmful, biased, or inappropriate content. |
| Efficiency | 4 | judge | The outputs are very short and avoid padding, which is efficient. However, they spend their limited tokens on the wrong first diagnostic object (SQL only) instead of the more informative query+EXPLAIN request, so the efficiency is good but not optimal relative to the quality target. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Completeness ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 4 | 4 | 5 | 4 | 1 | 0.47 |

- **Self-preference delta:** +2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 22 | Latency (avg): 2.2s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Strong, on-task single-question intake across runs. The main slight weakness is that Run 1 omits the explicit query text request, but overall the behavior matches the flipped-interaction pattern very well.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | The model asks the highest-leverage diagnostic first: for the actual query text plus EXPLAIN (ANALYZE, BUFFERS). This is exactly the canonical opener for a slow Postgres query and avoids off-target questions about schema or indexes before seeing the plan. |
| Completeness | 5 | judge | It fully satisfies the turn-1 requirement: exactly one question, specific and actionable, and no SQL or optimization plan. The question asks for the precise artifacts needed to start diagnosis. |
| Format Compliance | 5 | judge | The outputs match the required conversational single-question format. Each run contains exactly one question and nothing else substantive, with no bullets, numbering, or stacked questions. |
| Consistency | 4 | judge | The runs are semantically stable and structurally aligned: all ask for the query plus EXPLAIN (ANALYZE, BUFFERS). There is minor variation in wording and detail, but no contradiction or meaningful divergence. [lexical similarity ratio: 0.601] |
| Tone/Style | 5 | judge | The tone is professional, concise, and consultative, appropriate for a senior PostgreSQL performance consultant. It is warm enough to engage without becoming chatty or padded. |
| Safety | 5 | judge | The content is benign and purely diagnostic. It contains no harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The responses are concise, but one run adds a small amount of explanatory padding. Still, the token counts are modest and the information density is high, so the output is efficient overall. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 4 | 4 | 1 | 3 | 1.41 |

- **Self-preference delta:** -6 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.86 (max 3).

Tokens (avg output): 257 | Latency (avg): 1.93s | Runs: 3

---

## Prompt Under Test

```text
I want you to act as a senior PostgreSQL performance consultant. I have a production query that has gotten slow and I need your help fixing it — but do NOT propose a fix or write any SQL yet.

Instead of answering immediately, ask me questions ONE AT A TIME until you have enough information to recommend a concrete optimization plan. Ask the single most important question first, then adapt each subsequent question based on my previous answer. Ask at most one question per turn. When (and only when) you have enough to act, say exactly "I have enough to proceed" on its own line and then produce the optimization plan.

Goal: Diagnose and produce an optimization plan for one slow production PostgreSQL query.

Begin.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
What is the exact SQL query, and can you share the `EXPLAIN (ANALYZE, BUFFERS)` output for its slow production execution?
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
