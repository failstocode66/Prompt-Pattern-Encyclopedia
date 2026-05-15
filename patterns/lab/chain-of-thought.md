## Pattern: chain-of-thought

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Externalize the reasoning trace before answering to improve multi-step accuracy.

---

### Mechanism
Single-pass reasoning collapses on multi-step problems. Externalizing the trace allocates tokens to intermediate steps so the model can build on its own prior conclusions, making errors visible and sometimes self-correctable.

---

### Template
"Let's think step by step. Show your reasoning before giving the final answer.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
A bat and ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Let's think step by step. Show your reasoning before giving the final answer.

Question: A bat and ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Multi-step arithmetic, logic, or word problems
- Questions involving constraints that must be tracked across steps
- Tasks where the model is known to produce confident wrong answers in single-pass mode
- Cases where the user needs to inspect or verify the reasoning, not just the answer

---

### When NOT to Use
- Pure retrieval ("what is the capital of Australia") — adds noise
- Latency-sensitive completions where the reasoning trace is wasted tokens
- Tasks where the model has been trained to produce reasoning already (recent reasoning-tuned models may handle this implicitly)
- Conversational chat where step-by-step framing feels mechanical

---

### Failure Modes
- Pseudo-reasoning — model emits plausible-sounding steps that don't actually support the final answer
- Confident wrong chains — a wrong inference early gets locked in and the rest of the chain compounds it
- Trace-answer mismatch — the final answer contradicts the reasoning steps preceding it
- Over-elaboration — simple problems get dragged through unnecessary scaffolding

---

### Examples

Example 1:
Input: "Let's think step by step. If a train leaves Vancouver at 8am going 80 km/h and another leaves Calgary at 9am going 100 km/h on the same track 970 km away, when do they meet?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Think step by step before answering. A user reports their app crashes only when offline AND on iOS AND after 30 seconds of use. What's the most likely cause?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-decomposition (decompose the task, then chain-of-thought through each subtask)
- self-verification (chain-of-thought produces a trace; self-verification checks it)
- stepback-abstraction (state the principle, then chain through its application)
- plan-and-solve (plan structures the chain)

Conflicts with:
- direct-answer (CoT is the opposite — externalize, don't suppress)
- brevity-directive (adds reasoning tokens by design)
- low-latency-optimization (reasoning trace increases latency)

---

### Notes (Optional)
Introduced by Wei et al. (Google, 2022) as the canonical "Chain-of-Thought Prompting." Distinct from cognitive-decomposition: CoT exposes a reasoning trace, cognitive-decomposition restructures the task into subtasks. They compose well. Modern reasoning-tuned models often produce chains implicitly even without prompting; the pattern remains useful for older models, smaller models, or when the trace itself is needed for auditability.

---

### Version History
v0.1 – initial version
