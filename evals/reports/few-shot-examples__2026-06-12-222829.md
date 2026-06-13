# Eval: few-shot-examples

**Date:** 2026-06-12 22:28 | **Judge:** claude-opus-4-8 | **Runs/model:** 2 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| claude-sonnet-4-6 | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| gemini-2.5-flash | **4.7 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> The few-shot prompt elicited a flawless terse classifier response. Both runs returned exactly 'NEUTRAL', matching the expected reference for the mixed-signal feedback, in correct format, minimal tokens, and with perfect run-to-run stability. Earns top marks across all dimensions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | Both runs output NEUTRAL, exactly matching the expected reference label for the mixed-signal feedback (confusing interface but resolved quickly by support). |
| Completeness | 5 | judge | The task requires a single classification label; both runs deliver exactly that with no missing component. |
| Format Compliance | 5 | judge | Format spec demanded a single uppercase label from {POSITIVE/NEGATIVE/NEUTRAL} with no other text. Both runs comply exactly. |
| Consistency | 5 | judge | Both runs produce identical content, structure, and correct label; perfectly stable. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | Requested register is terse classifier output with no prose. Both runs are pure label output, pitch-perfect for the stated audience. |
| Safety | 5 | judge | A single sentiment label is wholly benign with no harmful, biased, or inappropriate content. |
| Efficiency | 5 | judge | 6 output tokens per run delivers the exact required answer with zero waste. |

Tokens (avg output): 6 | Latency (avg): 1.33s | Runs: 2

---

## Scorecard: claude-sonnet-4-6

> The few-shot prompt elicited a flawless terse classifier response. Both runs returned 'NEUTRAL', matching the reference expectation for this mixed-signal feedback, in exact format, with minimal tokens (5 each) and perfect run-to-run consistency. This is a textbook example of a well-functioning few-shot classification prompt; all dimensions earn a 5.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | Both runs output NEUTRAL, which exactly matches the reference expectation for this mixed-signal feedback (confusing interface but quickly resolved by support). The classification is correct and on-task. |
| Completeness | 5 | judge | The prompt requested a single classification label and nothing else. Both runs delivered exactly that, fully satisfying the only requirement. |
| Format Compliance | 5 | judge | Format spec required a single uppercase label from POSITIVE/NEGATIVE/NEUTRAL with no other text. Both runs produced exactly 'NEUTRAL' uppercase with no extra prose, punctuation, or labels. |
| Consistency | 5 | judge | Both runs produced identical content, structure, and correct classification. Perfect stability across runs. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | Requested tone was terse classifier output with no prose. Both runs delivered a bare label, perfectly matching the register for a classifier. |
| Safety | 5 | judge | The output is a neutral sentiment label with no harmful, biased, or inappropriate content whatsoever. |
| Efficiency | 5 | judge | Each run used only 5 output tokens to deliver the exact required label with no padding or waste. Maximally tight for the quality delivered. |

Tokens (avg output): 5 | Latency (avg): 1.5s | Runs: 2

---

## Scorecard: gemini-2.5-flash

> The few-shot prompt reliably elicited the correct NEUTRAL classification in both runs, with perfect format, tone, safety, and consistency. The only weakness is efficiency: despite a one-word visible output, the reported 306/318 output tokens suggest considerable hidden reasoning overhead disproportionate to the trivial task, which is the sole reason it falls short of a perfect score on that dimension.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | Both runs output NEUTRAL, which exactly matches the reference expected label for this mixed-signal feedback (confusing interface but quickly resolved by support). |
| Completeness | 5 | judge | The request asked for a single classification label, and both runs delivered exactly that with no omissions. |
| Format Compliance | 5 | judge | Format spec required a single uppercase label from POSITIVE/NEGATIVE/NEUTRAL with no other text. Both runs comply exactly. |
| Consistency | 5 | judge | Both runs produced identical content, structure, and correct quality. No divergence in answer or format. [lexical similarity ratio: 1.0] |
| Tone/Style | 5 | judge | Intended tone is terse classifier output with no prose. Both runs are bare labels, perfectly matching the register. |
| Safety | 5 | judge | A single sentiment label contains no harmful, biased, or inappropriate content. |
| Efficiency | 3 | judge | The visible output is maximally tight (one word), but the reported output token counts (306 and 318) are extremely high for a single-word label, indicating substantial hidden/reasoning token expenditure relative to the trivial deliverable. The quality is fine, but the token-to-value ratio shows notable waste. |

Tokens (avg output): 312 | Latency (avg): 2.65s | Runs: 2

---

## Prompt Under Test

```text
Classify the sentiment of customer feedback as exactly one of: POSITIVE, NEGATIVE, or NEUTRAL.

Examples:
Feedback: "The delivery was late but the product is excellent." -> NEUTRAL
Feedback: "Absolutely love it, works perfectly!" -> POSITIVE
Feedback: "Broke after one day, total waste of money." -> NEGATIVE

Now classify this feedback. Respond with only the single uppercase label and nothing else.
Feedback: "The interface is confusing and I couldn't find the export button, but support sorted it out quickly."
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
NEUTRAL
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by claude-opus-4-8 (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
