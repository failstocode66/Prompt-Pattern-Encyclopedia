## Pattern: low-latency-optimization
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Minimize time-to-first-token and total tokens for cost- or latency-sensitive contexts.

---

### Mechanism
Suppresses preamble, reasoning trace, and pleasantries at the prompt level; typically combined with smaller model selection and tight max_tokens at the API level. The prompt does the behavioral work; the API settings do the mechanical work.

---

### Template
"Answer directly. No preamble, no reasoning, no caveats. First token is the answer.

{task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
What's the capital of Australia?

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Answer directly. No preamble, no reasoning, no caveats. First token is the answer.

What's the capital of Australia?

Output
[placeholder — to be filled after testing]

---

### When to Use
- Real-time UX (autocomplete, inline suggestions, keystroke-time responses).
- High-volume API calls where per-call cost dominates.
- Batch jobs where aggregate latency is the bottleneck.
- Lookup-style tasks with a single short answer.

---

### When NOT to Use
- Reasoning tasks — cutting the trace cuts the accuracy.
- Quality-critical outputs where the trace is a product of the work.
- Tasks where failure is hard to detect without reasoning visible.
- Anything the user will read and evaluate (vs. consume programmatically).

---

### Failure Modes
- Quality collapse — model sacrifices correctness to match the terseness target.
- Silent wrongness — confident wrong answer with no trace to diagnose.
- Debug impossibility — production failures have no breadcrumbs.
- Model misselection — smallest-model + aggressive prompting produces outputs worse than a larger model with a normal prompt.

---

### Examples
Example 1: Input: "Answer directly, one word. No preamble. Which HTTP status code indicates a successful POST with created resource?"

Output: [placeholder — to be filled after testing]

Example 2: Input: "Answer directly, no preamble, no reasoning. Correct the typo: 'recieve their packaeg tommorow'"

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- direct-answer
- strict-output-format
- brevity-directive
- few-shot-examples (anchors format without adding latency per call)

Conflicts with:
- cognitive-decomposition
- plan-and-solve
- self-consistency (N calls erases per-call latency gains)
- self-verification
- role-persona (persona adds preamble-like tone)

### Notes (Optional)
Latency optimization is a stack, not a prompt pattern alone. The biggest wins come from model selection, streaming, caching, and max_tokens — the prompt is the last 10%. Before investing in prompt-level terseness, confirm the model and infra choices are right. Always measure p50 and p95 latency and tail errors after changes; terseness prompts can regress quality on edge cases without showing up in spot checks.

Version History
v0.1 – initial version
