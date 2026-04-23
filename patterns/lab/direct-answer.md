## Pattern: direct-answer
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Return the answer alone, with no reasoning, context, or surrounding prose.

---

### Mechanism
Explicit instruction that the answer is the entire output. Removes assistant-register defaults (acknowledgment, setup, caveats) and forces the model to commit.

---

### Template
"Output only the answer. No explanation, no preamble, no punctuation unless required.

{task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Is 127.0.0.1 a valid IPv4 address?

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Output only the answer. No explanation, no preamble.

Is 127.0.0.1 a valid IPv4 address?

Output
[placeholder — to be filled after testing]

---

### When to Use
- Programmatic consumption where the output is a value, not a message.
- Tight UI slots (form autofill, quick lookups, inline widgets).
- Fact-lookup queries with a single correct answer.
- Boolean or enum outputs where the label is the deliverable.

---

### When NOT to Use
- Ambiguous questions where the right response is a clarification.
- Reasoning-dependent tasks — "direct answer" makes wrong answers undetectable.
- Any user-facing context where a bare value feels abrupt.
- Tasks where the model is likely to be wrong and the user has no way to verify.

---

### Failure Modes
- Confident wrong answer with no trace for review.
- Silent ambiguity resolution — model picks one interpretation without surfacing that choice.
- Format mismatch — "yes" vs "Yes" vs "true" when downstream expects one specific form.
- Hallucinated facts presented as bare truth.

---

### Examples
Example 1: Input: "Output only the answer. No explanation. What is the SI unit of electric current?"

Output: [placeholder — to be filled after testing]

Example 2: Input: "Output only the answer, either 'yes' or 'no', no punctuation, no preamble. Does Python's sorted() return a new list?"

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- strict-output-format
- brevity-directive
- low-latency-optimization
- few-shot-examples (one example removes interpretation ambiguity)

Conflicts with:
- cognitive-decomposition
- plan-and-solve
- self-verification
- empathic-response
- role-persona (personas want to talk)

### Notes (Optional)
Direct-answer is a sharp tool. It trades auditability for throughput. Before using it, confirm the model is actually reliable on the task class — direct-answer amplifies the cost of each wrong output. For any task where correctness matters and you're not certain, use direct-answer paired with self-consistency (vote on the final value) rather than direct-answer alone.

Version History
v0.1 – initial version
