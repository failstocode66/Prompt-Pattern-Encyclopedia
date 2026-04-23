## Pattern: few-shot-examples
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Anchor output format and behavior by showing the model 1–N input/output pairs before the real task.

---

### Mechanism
In-context pattern matching. The model extends the demonstrated pattern to new inputs, which is usually cheaper and more reliable than describing the pattern in prose.

---

### Template
"Here are examples:

Input: {example_input_1}
Output: {example_output_1}

Input: {example_input_2}
Output: {example_output_2}

Now do the same for:
Input: {task}
Output:"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Extract the company name and funding amount from: "Acme Corp announced a $12M Series A today, led by Sequoia."

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Here are examples:

Input: "Northwind raised $5M seed in 2022."
Output: {"company": "Northwind", "amount": "$5M"}

Input: "Beluga Systems closed a $40M Series B."
Output: {"company": "Beluga Systems", "amount": "$40M"}

Now do the same for:
Input: "Acme Corp announced a $12M Series A today, led by Sequoia."
Output:

Output
[placeholder — to be filled after testing]

---

### When to Use
- Format-sensitive tasks where the output shape is idiosyncratic or hard to describe.
- Consistent batch processing — same shape across many inputs.
- Rare or domain-specific categories a zero-shot model might not recognize.
- When instruction-writing takes longer than example-writing.

---

### When NOT to Use
- Highly novel tasks where examples would anchor the wrong framing.
- Creative or voice-driven work where examples flatten the output toward the demos.
- Single-use queries where the example-writing cost exceeds the benefit.
- When all reasonable examples share a bias the model will inherit.

---

### Failure Modes
- Demonstration bias — model overfits to superficial features of the examples (length, specific words, example-order effects).
- Leakage — model echoes example content into the output.
- Format lock-in — model produces the example format even when the real task needs a different one.
- Label imbalance — if examples cover only a subset of classes, the model underpredicts the missing ones.

---

### Examples
Example 1: Input: Extract receipts into JSON using two prior examples as anchors, then:

Output: [placeholder — to be filled after testing]

Example 2: Input: Translate product descriptions into a fixed marketing tone using two anchor translations, then:

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- structured-output-schema
- role-persona
- strict-output-format
- direct-answer

Conflicts with:
- creative-flow (demos flatten voice)
- plan-and-solve (demos that skip planning teach the model to skip planning)

### Notes (Optional)
Use 2–5 examples in most cases. More than 5 rarely helps and raises cost. Diversify examples to cover the edges of the class space. If accuracy matters, check whether the order of examples affects outputs — recency bias is real.

Version History
v0.1 – initial version
