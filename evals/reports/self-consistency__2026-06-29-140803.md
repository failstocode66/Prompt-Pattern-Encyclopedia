# Eval: self-consistency

**Date:** 2026-06-29 14:08 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.4 (Solid)** | 5 | 4 | 4 | 4 | 5 | 5 | 4 |
| claude-sonnet-4-6 | **4 (Solid)** | 4 | 3 | 4 | 4 | 5 | 5 | 3 |
| gemini-2.5-flash | **4.3 (Solid)** | 5 | 3 | 4 | 5 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> Correct, well-formatted, and safe answer set with the right final probability 1/4. However, for a self-consistency evaluation it is not strongly discriminative because all five attempts in every run agree and are semantically very similar, so consistency is only moderate.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | The response set correctly identifies the conditioned event and derives the correct probability 1/4 in every run. The sample-space restriction is correct, and the conditional-probability computation is also correct. |
| Completeness | 4 | judge | The model addresses most requirements fully: it produces five separate attempts, provides explicit tallies, and correctly notes no tie arose. The reasoning correctly identifies the conditioned sample space and favorable outcome. However, while the attempts are framed differently, some are conceptually quite similar (e.g., Run 1, Attempt 3, 'Reason by complement inside the conditioned event' and Run 3, Attempt 4, 'Use the complement of “all girls” within the conditioned set'). The 'genuinely independent' aspect, particularly the expectation for chains to 'scatter realistically' and 'ideally NOT all reaching the same answer' as per the evaluation context, is not fully met, as all 15 attempts (5x3 runs) arrive at the exact same correct answer without exploring plausible alternative (incorrect) reasoning paths. This suggests the independence is more about presentation than true exploratory self-consistency. |
| Format Compliance | 4 | judge | The outputs follow the specified structure exactly: five clearly delimited attempts, each ending with the mandated line, followed by an explicit tally, a tiebreaker/no-tie statement, and a final standalone result line. Minor heading style variation does not break the required format. |
| Consistency | 4 | judge | All three runs are structurally identical: five attempts labeled 1–5 with the same types of reasoning (enumeration, formula, complement, symmetry/counting, ratio), the same tally format, and the same Result line. The same omission (no tiebreaker statement) appears in all three. All 15 final attempt answers are 1/4. Quality is uniformly high with no run being noticeably weaker or stronger. [lexical similarity ratio: 0.152] |
| Tone/Style | 5 | judge | The tone is analytical, precise, and self-auditing, matching the requested audience. It explains conditioning and counting without hedging filler. |
| Safety | 5 | judge | The content is benign educational probability reasoning with no harmful, biased, or inappropriate material. |
| Efficiency | 4 | judge | Run 1 (875 tokens), Run 2 (896 tokens), Run 3 (1015 tokens) are reasonable for five distinct derivations with full mathematical notation. Each attempt is concise and avoids preamble bloat. Minor inefficiency arises because the five approaches share so much logical structure (all conditioned on the same 4-element set) that they deliver less informational diversity per token than genuinely scattered chains would. No egregious padding, but not maximally tight. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 4 | 5 | 3 | 4 | 2 | 0.82 |
| Format Compliance ⚠ | 4 | 5 | 3 | 5 | 2 | 0.94 |
| Consistency | 4 | 2 | 5 | 5 | 3 | 1.41 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 4 | 4 | 1 | 0.47 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 929 | Latency (avg): 7.59s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Correct and on-task, with a clean final answer and stable structure across runs. Main deductions are for incomplete adherence to the self-consistency prompt’s stronger requirement for genuinely distinct attempts and for somewhat bloated, repetitive presentation.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly identify the conditional probability as 1/4 and use valid probability reasoning. No factual errors or off-task content appear in the substantive solution. |
| Completeness | 3 | judge | Requirements 1, 3, and 5 are fully met (correct conditioning and sample space, explicit tally table, correct 'Result: 1/4'). However, two key requirements are absent: (a) no run produces any chain that falls into an anchoring trap (1/2, 1/3, 1/8), so the self-consistency mechanism's discriminating feature — majority vote overcoming at least one errant chain — is never demonstrated; (b) no run explicitly states a tiebreaker rule, even though the format spec requires it be stated even when not needed. |
| Format Compliance | 4 | judge | The five-attempt structure, per-attempt answer lines, vote tally table, and 'Result:' line are all present. Two minor deviations: (1) answer lines and Result lines are wrapped in bold markdown (**) rather than being plain text exactly as specified; (2) the tiebreaker rule is not explicitly stated — runs merely observe all five agree without declaring what rule would apply to a hypothetical tie. |
| Consistency | 4 | judge | Across runs, the semantic answer, structure, and quality are stable: each run has five attempts, a tally, and the same final result 1/4. There is only minor structural variation in how the attempts are labeled and explained. However, the repeated near-identical reasoning within and across runs shows limited true diversity, so it is not a perfect 5. [lexical similarity ratio: 0.273] |
| Tone/Style | 5 | judge | The tone is analytical, careful, and self-auditing, with clear step-by-step reasoning and no filler. It fits the requested quantitative-reasoner register well. |
| Safety | 5 | judge | The content is benign, mathematical, and free from harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The outputs are correct and reasonably clear, but they are somewhat bloated because each run repeats the same conclusion five times with only superficial variation. Given the token counts shown (1245, 1013, 1279) and the relatively simple problem, the verbosity is more than necessary for the quality delivered, especially since the self-consistency goal asked for genuinely distinct attempts rather than repeated near-duplicates. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 5 | 5 | 2 | 3 | 1.41 |
| Completeness | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Consistency ⚠ | 4 | 4 | 5 | 3 | 2 | 0.82 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 3 | 4 | 3 | 1 | 0.47 |

- **Self-preference delta:** +3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Format Compliance, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 1179 | Latency (avg): 18.41s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs correctly solve the conditioning problem and arrive at 1/4 with valid, well-notated reasoning in five structurally distinct (if not always truly independent) attempts. The format is largely compliant, tone is appropriately analytical, and cross-run consistency is excellent. The principal weaknesses are: (1) the self-consistency mechanism's key feature — trap chains scattering to 1/2 or 1/3 before being outvoted — never appears, so the demonstration of the mechanism's error-correction value is absent; (2) several within-run attempt pairs are near-paraphrases of the same enumeration approach rather than genuinely independent lines of reasoning; (3) no explicit tiebreaker rule is stated; and (4) token usage is high relative to the informational content delivered, especially in Run 3. The correct final answer and full format compliance partially compensate, but the self-consistency pattern is not faithfully demonstrated.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs correctly identify the conditioning event ('at least two girls'), restrict the sample space to exactly {BGG, GBG, GGB, GGG}, identify GGG as the single favorable outcome, and arrive at 1/4 via correct arithmetic throughout. No factual errors appear in any reasoning chain across all five attempts in all three runs. |
| Completeness | 3 | judge | It covers the actual probability problem and includes five attempts plus a tally and final result. But it does not satisfy the expected behavior for this pattern test: the rubric/context explicitly expects genuinely independent attempts and a discriminating vote distribution, ideally with at least one trapped or differing chain. Instead, the model gives five near-certainly correct attempts and a unanimous tally, missing the evaluation target. |
| Format Compliance | 4 | judge | All three runs closely follow the specified format: five delimited attempts each closing with the required 'Attempt k final answer: 1/4' line, an explicit vote tally, a note that no tie occurred, and a final Result line. One deviation: Run 3 uses markdown bold ('**Result:** 1/4') rather than the plain 'Result: 1/4' required by the exact format specification. No run states an explicit tiebreaker rule (e.g., 'if tied, I would re-examine chains'), relying instead on noting unanimity. |
| Consistency | 5 | judge | All three runs produce structurally identical outputs: five attempts using the same set of methods (enumeration, conditional probability formula, binomial, Bayes'/complement, scenario partitioning), all five chains reaching 1/4 in every run, a 5:0 tally in every run, and 'Result: 1/4' in every run. Quality and coverage are stable. The low lexical similarity ratio is explained entirely by paraphrase of the same mathematical content. [lexical similarity ratio: 0.113] |
| Tone/Style | 5 | judge | All three runs are consistently analytical and precise throughout, using proper probability notation (P(A\|B), intersection notation, binomial formulas), showing stepwise work without hedging filler, and maintaining the register of a careful quantitative reasoner self-auditing a computation. No casual or imprecise language appears. |
| Safety | 5 | judge | No harmful, biased, or inappropriate content appears. The content is a standard probability problem solution. |
| Efficiency | 3 | judge | Token counts of 11,563 / 9,359 / 14,281 are substantial for five probability solutions that all reach the same answer via correct but overlapping methods. The full sample space is enumerated in a preamble AND re-enumerated within individual attempts in every run. Since no attempt surfaces a wrong answer to justify the mechanism's computational cost, the output delivers less information per token than the length suggests. Run 3 at 14,281 tokens is particularly inflated. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Format Compliance ⚠ | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 11734 | Latency (avg): 52.54s | Runs: 3

---

## Prompt Under Test

```text
I want a reliable answer to a probability question that I know trips people up, so don't just reason once. Work the problem through FIVE separate times, each as an independent attempt that does not look at or reuse the others — vary how you set it up (e.g. enumerate the sample space, use conditional-probability formulas, reason about symmetry, etc.) so the attempts are genuinely different lines of reasoning, not the same chain reworded.

For each of the five attempts:
- Show the reasoning for that attempt.
- End that attempt with a line in the exact form: "Attempt k final answer: <value>" (as a fraction or decimal).

After all five attempts:
- Tally how many attempts produced each distinct final answer.
- Report the answer that appears most often as the result. If two or more answers tie for the most votes, say so explicitly and apply a stated tiebreaker (e.g. re-examine the tied chains and pick the one whose reasoning survives scrutiny) rather than picking arbitrarily.
- Give the final majority answer on its own last line in the form: "Result: <value>".

The problem: A family has three children. You are told that at least two of them are girls. What is the probability that all three children are girls? (Assume each child is independently a boy or a girl with probability 1/2.)
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Attempt 1: Enumerate the equally likely outcomes for three children, using G = girl and B = boy.

The 8 equally likely birth-order outcomes are:
- BBB
- BBG
- BGB
- GBB
- BGG
- GBG
- GGB
- GGG

We are told at least two are girls, so we condition on:
- BGG
- GBG
- GGB
- GGG

That gives 4 equally likely cases, and only 1 of them is all girls.

So the probability is \(1/4\).

Attempt 1 final answer: 1/4

Attempt 2: Use conditional probability.

Let \(A\) be the event “all three children are girls,” and \(C\) be the event “at least two children are girls.”

Then
\[
P(A \mid C) = \frac{P(A \cap C)}{P(C)}.
\]
Since \(A\subseteq C\), \(P(A\cap C)=P(A)\).

Now
\[
P(A)=\left(\frac12\right)^3=\frac18.
\]

To compute \(P(C)\), count outcomes with at least two girls:
- exactly 2 girls: \(\binom32 = 3\) outcomes, each probability \(1/8\)
- exactly 3 girls: \(1\) outcome, probability \(1/8\)

So
\[
P(C)=\frac{3}{8}+\frac{1}{8}=\frac12.
\]

Therefore
\[
P(A\mid C)=\frac{1/8}{1/2}=\frac14.
\]

Attempt 2 final answer: 1/4

Attempt 3: Reason by complement inside the conditioned event.

We know at least two are girls. Among those possibilities, the only way the answer is not “all girls” is if there are exactly two girls and one boy.

With three children, the arrangements with exactly two girls are:
- GGB
- GBG
- BGG

There are 3 such arrangements, all equally likely. The all-girls arrangement GGG is one more case.

So among the 4 possible outcomes consistent with “at least two girls,” 3 are exactly two girls and 1 is three girls.

Thus the probability of all three being girls is
\[
\frac{1}{4}.
\]

Attempt 3 final answer: 1/4

Attempt 4: Use a counting argument with combinations.

Think of the family as having three independent children, each equally likely to be boy or girl. The number of gender sequences with exactly \(k\) girls is \(\binom{3}{k}\).

Given “at least two girls,” the admissible cases are:
- exactly 2 girls: \(\binom{3}{2}=3\)
- exactly 3 girls: \(\binom{3}{3}=1\)

These 4 cases are equally likely under the conditioning because each corresponds to the same number of underlying birth-order sequences once order is kept distinct.

Therefore,
\[
P(\text{3 girls} \mid \text{at least 2 girls})=\frac{1}{3+1}=\frac14.
\]

Attempt 4 final answer: 1/4

Attempt 5: Use a sequential conditioning view.

Suppose we look at the children in order.

Condition on the event that at least two are girls. Under this condition, the possible ordered sequences with the first two children and the third child are still the four sequences:
- GGG
- GGB
- GBG
- BGG

Each has the same unconditional probability, \(1/8\), and conditioning on the event “at least two girls” makes them equally likely among the allowed cases.

Only one of these four is all girls, so the probability is
\[
\frac14.
\]

Attempt 5 final answer: 1/4

Tally of final answers:
- \(1/4\): 5 attempts

Most frequent answer: \(1/4\)

Result: 1/4
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
