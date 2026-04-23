## Pattern: brevity-directive
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Constrain output length for UX, scannability, or cost.

---

### Mechanism
An explicit length ceiling shifts the model from generative elaboration toward extractive summary. The constraint also suppresses preamble, caveats, and throat-clearing.

---

### Template
"Answer in {N} {sentences|words|lines} or fewer. No preamble.

{task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
What's the difference between a stack and a queue?

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Answer in 2 sentences or fewer. No preamble.

What's the difference between a stack and a queue?

Output
[placeholder — to be filled after testing]

--- 

### When to Use
- Chat UX and mobile contexts where scroll cost is real.
- Cost-sensitive high-volume calls.
- Summaries for dashboards, notifications, tooltips.
- When the audience only needs the headline.

---

### When NOT to Use
- Reasoning tasks that require a trace.
- Explanations that depend on setup or definitions.
- Creative work where length is part of the form.
- Any task where the model is likely wrong — a wrong short answer is less debuggable than a wrong long one.

---

### Failure Modes
- Information loss — constraint drops a critical caveat or condition.
- Confident compression — model truncates nuance into overconfident claims.
- Constraint violation on complex tasks — model exceeds the ceiling anyway.
- False completeness — a two-sentence answer reads like the whole story when it isn't.

---

### Examples
Example 1: Input: "Answer in 1 sentence. No preamble. What does the ACID acronym mean in databases?"
Output: [placeholder — to be filled after testing]

Example 2: Input: "Answer in 20 words or fewer. No preamble. What's the recommended action for a customer whose card was declined at checkout?"
Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

--- 

### Composition
Works well with:
- direct-answer
- strict-output-format
- low-latency-optimization
- role-persona (terse roles reinforce brevity)

Conflicts with:
- cognitive-decomposition
- plan-and-solve
- self-verification
- creative-flow (length often serves form)

Notes (Optional)
Specify the unit (sentences, words, lines) — "be brief" is interpreted inconsistently. Pair with "no preamble" to kill throat-clearing phrases like "Great question!" For critical outputs, validate length programmatically; models drift over the ceiling on hard inputs.

Version History
v0.1 – initial version
