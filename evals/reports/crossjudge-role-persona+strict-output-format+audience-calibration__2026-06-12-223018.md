# Cross-Judge: role-persona+strict-output-format+audience-calibration

**Date:** 2026-06-12 22:30 | **Target:** claude-sonnet-4-6 | **Runs:** 2 | **Judges:** gpt-5.4-mini, claude-opus-4-8, gemini-2.5-flash

Same composed prompt + same target outputs, scored independently by each judge. Disagreement here is judge variance, not model variance.

---

## Judge agreement (score per dimension, 1–5)

| Dimension | gpt-5.4-mini | claude-opus-4-8 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 5 | 5 | 1 | 0.47 |
| Consistency | 5 | 5 | 5 | 0 | 0.0 |
| **Total** | 33 | 35 | 35 | | |

`*` = same provider as the target model (anthropic).

---

## Disagreement summary

- **Mean per-dimension spread:** 0.29 (max 1)
- **Contested dimensions (spread ≥ 2):** none
- **Self-preference delta:** +1 total-score points (same-provider mean 35 vs cross-provider 34) — same-provider judges scored the target HIGHER.

> Interpretation: low spread + a near-zero self-preference delta means the rubric scores are judge-robust. A consistently positive delta is evidence a judge favors its own provider's outputs — a reason to prefer a cross-provider judge or a multi-judge mean.

---

## Per-judge summaries

**gpt-5.4-mini**: Strong, prompt-compliant responses: accurate, audience-appropriate, and structurally correct, with only slight verbosity beyond the minimal needed.

**claude-opus-4-8** (same provider as target): An exemplary response set that nails all seven dimensions. Both runs accurately and accessibly explain APIs for a 10-year-old, follow the exact three-points-plus-Remember format, maintain a warm teacher tone, explain the only jargon, and stay tight on tokens. The two runs are structurally and semantically consistent, with variation limited to harmless illustrative examples. No meaningful weaknesses identified.

**gemini-2.5-flash**: The `claude-sonnet-4-6` model performed exceptionally well against the rubric. It delivered a highly accurate, complete, and format-compliant explanation of an API, perfectly tailored to a 10-year-old audience with a warm, patient teacher tone. The output was highly efficient and demonstrated strong consistency across both runs, with only minor, acceptable variations in specific examples or analogy elaboration. All rubric dimensions received the highest possible score.

---

## Prompt Under Test

```text
You are a patient elementary school science teacher explaining technology to a curious 10-year-old.

Explain what an API is.

Return your answer as exactly three numbered points, each a single sentence, followed by one final line starting with "Remember:" that gives a one-sentence analogy. Do not use any technical jargon without immediately explaining it in everyday words.
```

## Target Output (claude-sonnet-4-6, run 1)

```text
1. An API (which stands for "Application Programming Interface," but just think of it as a "messenger") is a way for two computer programs to talk to each other and share information.
2. When you use an app on a tablet, that app sends a request through an API to another computer somewhere else, asking for the information it needs, like asking a friend to grab something from another room.
3. The API takes that request, delivers it to the right place, and brings the answer back to your app, all in just a split second.

Remember: An API is like a waiter at a restaurant — you tell the waiter what you want, the waiter carries your order to the kitchen, and then brings your food back to you without you ever needing to go into the kitchen yourself.
```
