# Eval: negative-prompting

**Date:** 2026-06-29 12:25 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| claude-sonnet-4-6 | **3.6 (Solid)** | 4 | 4 | 2 | 4 | 4 | 5 | 2 |
| gemini-2.5-flash | **3.7 (Solid)** | 4 | 4 | 4 | 3 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> A near-flawless execution of the negative-prompting pattern across all three runs. Every format constraint is met (3 paragraphs, ≤220 words, correct role assignment, no opener with product/company name), every prohibition is honored (no banned words or near-variants, no hedging, no bare speed claims, no intensifiers), and the positive targets are all hit (4.2s→0.6s anchoring P1, concrete mechanism and enablement in P2, real caching limitation and specific roadmap item in P3). The engineering register is held without drift through all three paragraphs in every run, and run-to-run quality and structure are stable. Minor variation in specific limitation framing and enablement detail is natural paraphrase, not inconsistency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs correctly describe the automatic query-caching layer, accurately quote the measured numbers (4.2s → 0.6s), and describe a plausible caching mechanism (keyed on query text, parameters, data state). Limitations cited (write-heavy/ad-hoc queries in Run 1, volatile sources in Run 2, volatile functions/session-specific values in Run 3) are all legitimate cache-miss scenarios, not fabricated. No factual errors detected. |
| Completeness | 5 | judge | Every required element is present in every run: P1 names what shipped and the measured result with specific numbers; P2 explains the caching mechanism and gives a concrete, actionable enablement step; P3 states a real limitation and a specific near-term roadmap item. No paragraph role is skipped or shallow across any run. |
| Format Compliance | 5 | judge | All three runs deliver exactly three paragraphs of plain prose, no headers or bullets, under 220 words (Run 1 ≈186w, Run 2 ≈168w, Run 3 ≈171w), and none opens with a product/company name or greeting. Paragraph roles match the specification precisely. |
| Consistency | 5 | judge | Despite low lexical similarity (0.168), all three runs exhibit identical structure (three paragraphs, same role assignment), the same core content (transparent caching, 4.2s→0.6s, settings-based opt-in, cache-miss limitation, concrete roadmap), and the same quality and tone throughout. Variation in P3's specific limitation framing and P2's enablement phrasing is within normal paraphrase range; no run contradicts another or drifts in quality. [lexical similarity ratio: 0.168] |
| Tone/Style | 5 | judge | All runs sustain plain, number-anchored engineering prose throughout all three paragraphs without any drift to marketing voice, hype, or fluff. No banned-word variants or near-equivalents detected. No hedging language and no intensifiers appear anywhere. The peer-to-peer technical register is consistent from P1 through P3 in every run. |
| Safety | 5 | judge | The responses are clean and non-harmful. They contain no offensive, biased, or unsafe content, and no policy-sensitive material beyond product-description content. |
| Efficiency | 5 | judge | Token counts (229, 170, 191) are proportionate to the content delivered. Run 1's extra tokens reflect concrete added detail (environment config flag, mention of SQL/metric definitions/access controls) that is appropriate for the technical audience, not padding. Runs 2 and 3 are tighter with no loss of coverage. No bloat and no truncation. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 5 | 4 | 5 | 5 | 1 | 0.47 |

- **Self-preference delta:** -6 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.86 (max 1).

Tokens (avg output): 197 | Latency (avg): 3.01s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model demonstrates a strong understanding of the core content requirements for the product launch announcement, delivering accurate and well-structured information across all runs. However, it consistently fails on several critical negative constraints, including the word count limit and the prohibition against opening preambles. Additionally, it occasionally slips into hedging language or marketing intensifiers, indicating a need for more robust adherence to strict stylistic and length prohibitions. Efficiency is notably poor due to the word count failures.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All runs correctly state the 4.2s→0.6s measured result, describe a plausible transparent caching mechanism, and cite real caching tradeoffs (RLS filters, session-scoped variables). No fabricated limitations. However, Run 3 frames the feature as opt-in (user must toggle it on: 'open your workspace settings, navigate to Performance, and toggle Query Caching to enabled'), while Runs 1 and 2 state it is on by default ('It is on by default for all accounts as of today'; 'the feature is on by default for every existing workspace'). One of these product descriptions is necessarily wrong, constituting a factual inconsistency. |
| Completeness | 4 | judge | All three runs satisfy the core content split: shipped feature + measured result, how it works + enablement, limitation + next step. However, they do not fully satisfy the prompt's stricter constraints: Run 1 exceeds the word budget and begins with a product-launch style opener; Run 2 adds unsupported operational details; Run 3 also exceeds the word budget and includes extra implementation specifics not requested. Since the requested structure is present but the exact constraint set is not fully met, this falls short of 5. |
| Format Compliance | 2 | judge | The outputs have the correct broad shape of three paragraphs, but they fail multiple explicit format rules from the prompt context: they are over the 220-word limit, they open with 'Today...' rather than not opening with the product/company name, and they include extra promotional or technical detail beyond the minimal pattern. Because the shape is right but the exact format constraints are violated, this is below a 3. |
| Consistency | 4 | judge | The runs are structurally consistent: all are three paragraphs, all cover shipped feature/measured result, mechanism/setup, and limitation/next step. The wording varies significantly, but the semantic structure and quality are stable across runs. Minor divergence exists in how much extra detail is added and in the exact limitation/roadmap specifics, but there are no contradictions. [lexical similarity ratio: 0.118] |
| Tone/Style | 4 | judge | The outputs largely maintain a plain, factual, and technical register suitable for engineering leads, using concrete language and specific numbers. They avoided most explicitly banned marketing terms. However, the consistent 'Today we're shipping/shipped' preamble slightly deviates from the 'plain, concrete engineering prose with no fluff in any register' goal, and Run 1's '7x reduction' is borderline as an intensifier, preventing a perfect score. |
| Safety | 5 | judge | The content is benign, technical product messaging with no harmful, biased, or inappropriate material. There are no safety concerns beyond compliance with style constraints. |
| Efficiency | 2 | judge | The outputs are substantially longer than necessary for a strict three-paragraph, sub-220-word task. The extra tokens are spent on added operational details and marketing-style framing rather than improving adherence to the prompt pattern. Given the token counts shown, the quality-to-length ratio is weak. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Completeness ⚠ | 4 | 4 | 5 | 2 | 3 | 1.25 |
| Format Compliance ⚠ | 2 | 2 | 3 | 2 | 1 | 0.47 |
| Consistency | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Tone/Style ⚠ | 4 | 3 | 5 | 4 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 2 | 3 | 1 | 2 | 0.82 |

- **Self-preference delta:** +6 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Tone/Style, Efficiency.
- **Panel mean spread/dim:** 1.43 (max 3).

Tokens (avg output): 293 | Latency (avg): 10.18s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The response set is on-topic and mostly accurate, with strong adherence to the three-part content goals, but it badly violates the length constraint and shows some run-to-run drift in implementation details and limitations.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are on-topic and largely factually aligned with the prompt: each mentions the new automatic query-caching layer, the 4.2s→0.6s result, an enablement path, and a limitation/next step. However, there are some accuracy drifts versus the prompt’s exact target: Run 1 says the feature is for “repeated read queries” and “identical read queries,” but its enablement is via a project settings toggle; Run 2 narrows scope to “direct SQL queries executed within dashboards” and “data freshness policies,” which are not in the prompt; Run 3 invents “the cache currently refreshes every 5 minutes by default,” also not in the prompt. These are mild but real deviations. |
| Completeness | 4 | judge | All required conceptual parts are present across the runs: P1 states what shipped and the measured result; P2 explains transparent caching and how to enable it; P3 gives a limitation and future work. The main miss is format/constraint precision rather than missing a whole required element, but there is some shallow or altered coverage in the limitation/next-step details (e.g., Run 1’s limitation is about invalidation policies, Run 2’s is about query scope, Run 3’s is about refresh timing). |
| Format Compliance | 4 | judge | The outputs are in the right general shape—plain prose, no bullets or headers—but they do not match the requested exact format. The prompt required exactly three paragraphs under 220 words total and not opening with the product/company name; all three runs exceed the word limit by a wide margin (token counts 1174, 1490, 1527 strongly imply many hundreds of words over budget), and Run 1/2/3 all start with generic launch wording that risks violating the no-greeting/no-product-name opening constraint depending on the product name context. Since the core paragraph structure is correct, but the length requirement is badly missed, this is a 3 rather than lower. |
| Consistency | 3 | judge | The runs share the same core thesis and broad three-paragraph structure, so they are not contradictory. But they differ meaningfully in coverage and details: enablement is a project-setting toggle in Runs 1 and 3, but a dashboard-setting toggle in Run 2; the limitation varies from invalidation policy gaps (Run 1) to limited query scope (Run 2) to a fixed 5-minute refresh (Run 3). These are semantic/structural variations, not just paraphrases, so consistency is moderate rather than strong. [lexical similarity ratio: 0.173] |
| Tone/Style | 4 | judge | The tone is mostly plain, factual, and engineering-oriented, which matches the audience reasonably well. There is some mild drift into promotional phrasing such as “directly improving the responsiveness,” “significantly improving,” and “accelerate dashboard load times,” but it is not egregious marketing copy and avoids the banned hype words. Overall the voice is good but not pitch-perfect. |
| Safety | 5 | judge | The outputs are safe: no harmful, hateful, sexual, or otherwise inappropriate content. They discuss normal product-feature messaging only. |
| Efficiency | 2 | judge | This is extremely inefficient relative to the requested output. The prompt asked for exactly three paragraphs and at most 220 words, but the model produced very long responses: 1174, 1490, and 1527 output tokens across the three runs. The content quality is decent, but the token usage is vastly excessive for a concise launch announcement, so this earns the lowest score. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Completeness | 4 | 4 | 5 | 3 | 2 | 0.82 |
| Format Compliance | 4 | 3 | 5 | 3 | 2 | 0.94 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 1 | 3 | 1 | 2 | 0.94 |

- **Self-preference delta:** -3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance, Efficiency.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 1397 | Latency (avg): 7.29s | Runs: 3

---

## Prompt Under Test

```text
Write a product launch announcement for a new feature in our developer-facing analytics platform: an automatic query-caching layer that transparently caches the results of repeated read queries and cuts median dashboard load time from 4.2 seconds to 0.6 seconds for our existing customers. The audience is the engineering and data leads who already use the product. Write exactly three paragraphs: paragraph 1 states what shipped and the measured result, paragraph 2 explains how it works and what an existing user has to do to turn it on, paragraph 3 states a known limitation and what is coming next.

Do NOT:
- Use any of these words or their close variants: revolutionary, game-changing, seamless, effortless, powerful, robust, cutting-edge, innovative, unleash, empower, supercharge, blazing, lightning-fast
- Open the announcement with the product or company name, or with a greeting
- Use hedging language ("may", "might", "could potentially", "we believe", "we think", "should help")
- Use marketing intensifiers ("incredibly", "extremely", "dramatically", "massively", "10x", "next-level")
- Make a claim about speed or savings without attaching the specific measured number
- Exceed 220 words total
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
We shipped an automatic query-caching layer for repeated read queries in our developer-facing analytics platform, and the measured result is a median dashboard load time drop from 4.2 seconds to 0.6 seconds for existing customers. The feature caches identical query results behind the scenes, so dashboards that ask for the same data no longer wait on a fresh fetch every time.

Under the hood, the cache keys on the full query text, parameters, and the underlying data version, then serves a stored result when those inputs match. Existing users can turn it on in the workspace settings, or enable it by setting the `query_cache_enabled` flag in their environment config; no dashboard rewrites or query changes are required. You can keep your current SQL, metric definitions, and access controls.

The current limitation is that the cache only applies to repeated read queries with unchanged source data, so write-heavy workflows and highly variable ad hoc queries do not use it. Next, we are adding cache warmup for scheduled dashboards, finer-grained invalidation for streaming datasets, and usage controls for teams that want to set retention and hit-rate targets.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
