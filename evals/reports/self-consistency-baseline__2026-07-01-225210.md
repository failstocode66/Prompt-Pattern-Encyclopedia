# Eval: self-consistency-baseline

**Date:** 2026-07-01 22:52 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.1 (Mixed)** | 5 | 1 | 1 | 5 | 3 | 5 | 2 |
| claude-sonnet-4-6 | **3.3 (Mixed)** | 4 | 1 | 1 | 5 | 4 | 5 | 3 |
| gemini-2.5-flash | **3.1 (Mixed)** | 4 | 2 | 1 | 5 | 3 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> The model accurately solves the underlying probability problem, correctly identifying the conditional sample space and the final probability of 1/4. However, it entirely fails to implement the requested self-consistency pattern. It produces only a single derivation per run, instead of five independent attempts, and consequently omits the required vote tally, tiebreaker rule, and specific final 'Result' line. This leads to very low scores for completeness, format compliance, and efficiency (relative to the pattern's expectations). The tone is analytical for the content delivered but lacks the 'self-auditing' quality associated with the pattern. All runs are highly consistent in their structure and content, including their consistent failure to follow the pattern.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs solve the conditional probability correctly and stay on task. They correctly restrict to the four equally likely outcomes with at least two girls and identify only GGG as favorable, yielding 1/4. |
| Completeness | 1 | judge | Every self-consistency-specific requirement is absent: (1) no five independent attempts with distinct methodologies, (2) no 'Attempt k final answer: <value>' labels, (3) no vote tally enumerating distinct answers, (4) no stated tiebreaker rule, (5) no 'Result: <value>' closing line. Only the bare mathematical answer is present. All pattern requirements are ignored. |
| Format Compliance | 1 | judge | The required format was five clearly delimited attempts, each with an exact attempt-final-answer line, followed by a vote tally, tiebreaker, and a standalone Result line. The outputs instead provide a single solution per run with no attempt numbering, no tally, and no final "Result: <value>" line. |
| Consistency | 5 | judge | Across the three runs, the semantic content, structure, and quality are highly stable: each enumerates the 8 outcomes, filters to the same 4 outcomes under "at least two girls," and concludes 1/4. Wording varies slightly, but there is no contradiction or meaningful structural divergence. [lexical similarity ratio: 0.53] |
| Tone/Style | 3 | judge | The tone is clear, analytical, and concise, suitable for a quantitative reasoning problem. It is not quite the careful self-auditing style requested in the evaluation context because it does not show explicit self-checking, but the register is otherwise appropriate. |
| Safety | 5 | judge | The content is benign and free of harmful, biased, or inappropriate material. |
| Efficiency | 2 | judge | For the simple problem asked, the outputs are reasonably concise. But relative to the evaluation context’s stronger reference pattern, the response set is under-generated: only three short runs and none of the required multi-attempt self-consistency machinery. The token usage is low, but the delivered quality against the expected pattern is incomplete, making the efficiency only modest. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 1 | 2 | 1 | 1 | 1 | 0.47 |
| Format Compliance | 1 | 1 | 1 | 1 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style ⚠ | 3 | 4 | 2 | 2 | 2 | 0.94 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 2 | 2 | 1 | 1 | 0.47 |

- **Self-preference delta:** +4 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Tone/Style.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 137 | Latency (avg): 1.74s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model correctly solves the probability problem and demonstrates excellent accuracy, tone, style, and safety. However, it completely failed to implement the 'self-consistency-baseline' pattern under test, producing only a single, verbose derivation per run instead of five distinct attempts, a vote tally, and a tiebreaker. This led to severe penalties in completeness, format compliance, and efficiency. While the individual runs are highly consistent with each other, this consistency highlights a failure to produce the diverse chains expected by the self-consistency pattern itself, which was not graded under the 'consistency' rubric item (which focused on cross-run similarity).

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs are mathematically correct and directly on task: they condition on "at least two girls," identify the 4 relevant outcomes, and compute 1/4 correctly. |
| Completeness | 1 | judge | The self-consistency pattern requires five clearly delimited independent attempts, an explicit vote tally, a stated tiebreaker rule, and a final 'Result:' line. Every one of these requirements is absent across all three runs. Each run provides only a single reasoning chain. The 'discriminating signal' requirement (at least one chain landing on a wrong answer like 1/2 or 1/3) is also entirely missing. |
| Format Compliance | 1 | judge | The outputs do not match the required format specification. They are not five attempts, lack per-attempt lines exactly matching "Attempt k final answer: <value>", omit the required vote tally and tiebreaker statement, and do not end with the exact standalone result line. |
| Consistency | 5 | judge | All three runs are structurally and semantically near-identical: same section headers, same 8-row probability table, same conditional-probability formula, same arithmetic, same boxed answer. The model consistently applies one approach (sample-space enumeration + P(A∩B)/P(B)) and consistently reaches 1/4. The lexical-similarity ratio of 0.285 is explained entirely by paraphrasing, not structural divergence. Quality, structure, and conclusion are stable across runs. [lexical similarity ratio: 0.285] |
| Tone/Style | 4 | judge | The tone is mostly analytical and self-auditing, with clear probability reasoning and minimal filler, which fits the intended audience well. However, it is generic rather than explicitly self-auditing across multiple attempts, since the required ensemble-style justification is absent. |
| Safety | 5 | judge | The content is benign, mathematical, and contains no harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The outputs are reasonably concise for the quality delivered, but they repeat the same full enumeration in each run and use more tokens than necessary for a simple 1/4 derivation. Still, the verbosity is moderate rather than bloated. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 5 | 3 | 5 | 2 | 0.94 |
| Completeness | 1 | 2 | 1 | 1 | 1 | 0.47 |
| Format Compliance | 1 | 1 | 1 | 1 | 0 | 0.0 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 4 | 2 | 2 | 2 | 0.94 |

- **Self-preference delta:** -3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Efficiency.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 351 | Latency (avg): 5.91s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model consistently produced the correct mathematical answer (1/4) for the probability question, demonstrating good accuracy in its calculation and a suitable analytical tone. However, it completely failed to implement the requested self-consistency pattern. Across all three runs, it provided a single, verbose explanation rather than five independent attempts. Consequently, it missed all related formatting and completeness requirements, such as producing 'Attempt k final answer' lines, an explicit vote tally, or a stated tiebreaker rule. This structural failure, despite the mathematical correctness, resulted in very low completeness, format compliance, and efficiency scores. The consistency across runs was high, but this was a consistent failure to adhere to the prompt's core pattern instructions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Each run independently and correctly calculates the conditional probability as 1/4. The identification of the sample space, conditioning event, and calculation steps are accurate. However, the core mechanism of the self-consistency pattern (multiple *independent* attempts that ideally scatter to demonstrate robustness against traps, then vote) is entirely missed. The output does not reflect the 'discriminating signal is that the chains scatter realistically' aspect, instead converging on the correct answer without showing any variability, which is a failure of the *pattern implementation* even if the final result is right. |
| Completeness | 2 | judge | The core math question is answered completely, but the response set does not satisfy the prompt-under-test requirements for five attempts, per-attempt final-answer lines, vote tally, or explicit tiebreaker. Typical behavior is one complete solution per run rather than the required self-consistency-baseline structure. |
| Format Compliance | 1 | judge | The outputs do not follow the specified format at all. The required structure was five clearly delimited attempts, each with an exact final-answer line, followed by a vote tally, tiebreaker, and a standalone Result line. Instead, each run is a conventional explanatory solution with a boxed final answer. |
| Consistency | 5 | judge | All three runs are structurally and semantically identical: list all 8 outcomes, define event A (≥2 girls = 4 outcomes), define event B (GGG = 1 outcome), apply conditional probability formula, confirm via reduced sample space, box 1/4. The failure mode is uniform across runs. [lexical similarity ratio: 0.187] |
| Tone/Style | 3 | judge | The tone is analytical and explanatory, which is broadly appropriate, but it is not the self-auditing, multi-attempt quantitative style requested. It reads like a standard tutorial rather than a careful, structured vote-based evaluation. |
| Safety | 5 | judge | The content is benign, non-sensitive probability reasoning with no harmful, biased, or inappropriate material. |
| Efficiency | 2 | judge | The runs are very verbose for a simple 1/4 conditional-probability problem, especially given the task’s goal of a compact self-consistency baseline. The token counts are high (roughly 2.0k–2.4k each) while delivering only one straightforward solution per run, so the quality-to-token ratio is poor. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 5 | 3 | 4 | 2 | 0.82 |
| Completeness | 2 | 3 | 1 | 1 | 2 | 0.94 |
| Format Compliance | 1 | 1 | 1 | 1 | 0 | 0.0 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 3 | 3 | 3 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 2 | 1 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 2293 | Latency (avg): 11.1s | Runs: 3

---

## Prompt Under Test

```text
Question: A family has three children. You are told that at least two of them are girls. What is the probability that all three children are girls? (Assume each child is independently a boy or a girl with probability 1/2.)
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
There are 8 equally likely gender combinations for 3 children:

- BBB
- BBG
- BGB
- GBB
- BGG
- GBG
- GGB
- GGG

We’re told **at least two are girls**, so we keep only:

- GGB
- GBG
- BGG
- GGG

That gives **4** equally likely outcomes, and only **1** of them is all girls.

So the probability is:

\[
\frac{1}{4}
\]

**Answer: \(\boxed{\tfrac{1}{4}}\)**
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
