# Eval: role-persona+brevity-directive

**Date:** 2026-06-19 22:38 | **Judges:** gpt-5.4-mini, claude-opus-4-8, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 2 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4-6 | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

---

## Scorecard: claude-sonnet-4-6

> A strong response set that nails the role-persona+brevity pattern: exactly three single-sentence bullets, no preamble, accurate technical content matching the reference, and a junior-appropriate mentoring tone. Both runs are tight (~96 tokens) and highly consistent in structure, ordering, and meaning. The third bullet tastefully adds when-to-use guidance without violating the format. Earns 5s across all dimensions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | The responses are factually correct and directly relevant to the container vs VM distinction. They correctly state that VMs include a full OS and use virtualized/emulated hardware managed by a hypervisor, while containers share the host kernel and are lighter/faster. |
| Completeness | 5 | judge | All requirements are covered: the difference is explained, the response is exactly three bullet points in each run, and the explanation is in plain language without preamble. The third bullet adds usage guidance, which is extra but still relevant. |
| Format Compliance | 5 | judge | The outputs match the specified format exactly: three bullet points, one sentence each, with no preamble. The bullets are plain-language sentences rather than multi-sentence paragraphs. |
| Consistency | 5 | judge | Across runs, the answer is structurally stable and semantically consistent: both runs present the same three-bullet structure, the same core explanation, and similar quality. Minor wording changes do not constitute inconsistency. [lexical similarity ratio: 0.791] |
| Tone/Style | 5 | judge | The tone is appropriate for a senior engineer explaining to a junior: clear, helpful, and non-technical enough to be accessible while still technically accurate. It is direct and instructional without sounding patronizing. |
| Safety | 5 | judge | The content is benign, technical, and free of harmful, biased, or inappropriate material. |
| Efficiency | 5 | judge | At 95-97 output tokens for three dense, accurate sentences, the responses are tight with no padding; every clause carries information. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-opus-4-8 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |

- **Self-preference delta:** +0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.14 (max 1).

Tokens (avg output): 96 | Latency (avg): 3.78s | Runs: 2

---

## Prompt Under Test

```text
You are a senior DevOps engineer. A junior teammate asks you to explain the difference between a container and a virtual machine. Respond in exactly three bullet points, each a single plain-language sentence, with no preamble.
```

---

## Sample Output (claude-sonnet-4-6, run 1)

```text
• A virtual machine includes a full operating system and runs on emulated hardware managed by a hypervisor, making it heavyweight and slow to start.
• A container shares the host machine's operating system kernel and isolates only the application and its dependencies, making it lightweight and fast to launch.
• Use a VM when you need strong isolation or a different operating system, and use a container when you want speed, efficiency, and consistency across environments.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-opus-4-8, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
