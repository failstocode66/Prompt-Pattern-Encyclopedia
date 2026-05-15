## Pattern: cognitive-verifier

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Generate clarifying sub-questions, answer each, then synthesize — improving responses to under-specified questions.

---

### Mechanism
Models silently pattern-match to the obvious reading of a question. Forcing explicit sub-questions surfaces hidden dimensions and missing inputs; each sub-answer then becomes context for the synthesis step.

---

### Template
"When I ask a question, follow this procedure before answering:
1. Generate 3-5 additional sub-questions that, if answered, would let you give a more complete and accurate response.
2. Answer each sub-question briefly using your best reasoning.
3. Synthesize a final answer that integrates the sub-answers.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Should I use Postgres or MongoDB for my app?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
When I ask a question, follow this procedure before answering:
1. Generate 3-5 sub-questions that would let you give a more complete answer.
2. Answer each briefly.
3. Synthesize a final answer.

Question: Should I use Postgres or MongoDB for my app?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Open-ended advisory questions where the right answer depends on unstated context
- Architecture, design, or "should I" decisions
- Research questions that span multiple dimensions (cost, performance, maintainability, team skill)
- Tasks where the user is likely to under-specify but expects a tailored answer

---

### When NOT to Use
- Fully specified factual queries (sub-questions add latency without benefit)
- Tasks with hard latency or token budgets
- Creative tasks where divergent thinking is the point, not convergent specification
- When the user has already supplied complete context — sub-questions become redundant or condescending

---

### Failure Modes
- Sub-question inflation — model generates many shallow sub-questions instead of a few sharp ones
- Self-confirmation — the model answers its own sub-questions in ways that conveniently support a predetermined conclusion
- Lost synthesis — sub-answers are listed but never integrated into a coherent final answer
- Sub-question drift — sub-questions wander away from the user's actual intent and the answer follows them

---

### Examples

Example 1:
Input: "Use the cognitive verifier procedure (sub-questions → sub-answers → synthesis). Question: What's the best way to deploy my Next.js app?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Use the cognitive verifier pattern. Question: Is it worth getting a graduate degree in computer science right now?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-decomposition (sub-questions can each become decomposed tasks)
- self-verification (verify the final synthesis against the sub-answers)
- role-persona (a senior-advisor persona reinforces the questioning discipline)
- few-shot-examples (demonstrate the right granularity of sub-question)

Conflicts with:
- brevity-directive (sub-questions inherently expand output)
- direct-answer (the pattern's whole point is structured detour before answering)
- low-latency-optimization (multi-step procedure increases tokens and latency)

---

### Notes (Optional)
Originates from the prompt patterns catalog (White et al., Vanderbilt 2023). The sub-question count is load-bearing: too few defeats the purpose, too many produces dilution. 3-5 is a reasonable default. Always pair with an explicit synthesis instruction — without it, models commonly list sub-answers without integrating them, leaving the user to do the work.

---

### Version History
v0.1 – initial version
