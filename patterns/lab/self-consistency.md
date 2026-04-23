## Pattern: self-consistency
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Improve accuracy on tasks with a single correct answer by sampling multiple reasoning paths and taking the majority vote.

---

### Mechanism
At non-zero temperature, reasoning chains diverge. Correct answers tend to cluster across runs because valid logic converges; errors scatter because mistakes are path-dependent. Majority vote filters noise.

---

### Template
"Run the following task N times at temperature >0. Return the answer that appears most often across runs: {task}"

(Implementation is typically orchestrated client-side — N independent API calls, then vote on the final-answer field.)

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
A bat and a ball cost $1.10 total. The bat costs $1.00 more than the ball. How much does the ball cost?

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Run the following task 5 times at temperature 0.7. Return the answer that appears most often: A bat and a ball cost $1.10 total. The bat costs $1.00 more than the ball. How much does the ball cost?

Output
[placeholder — to be filled after testing]

---

### When to Use
- Tasks with a discrete, verifiable answer (math, logic, classification).
- Mid-tier models where single-shot reasoning is unreliable.
- High-stakes one-off queries where N× cost is acceptable.

---

### When NOT to Use
- Open-ended or creative generation where there is no "correct" answer to vote on.
- Continuous outputs (summaries, essays) that can't be compared for equality.
- Latency- or cost-sensitive paths.
- Tasks the base model already solves reliably.

---

### Failure Modes
- Shared bias — all chains make the same systematic error; majority is confidently wrong.
- Tie votes with no tiebreaker logic.
- Variance ceiling — if the base model is too weak, no amount of voting helps.
- Cost blow-up at scale.

---

### Examples
Example 1: Input: Sample 5 chains at temp 0.7 and majority-vote: "If a car travels 60 miles in 45 minutes, then slows to 40 mph for the next 30 minutes, what is its average speed over the full trip?"

Output: [placeholder — to be filled after testing]

Example 2: Input: Sample 5 chains at temp 0.7 and majority-vote classification: "Is this review Positive, Negative, or Neutral? 'It's fine. Works as advertised. Nothing to write home about.'"

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition
- plan-and-solve
- self-verification
- few-shot-examples

Conflicts with:
- low-latency-optimization
- brevity-directive
- direct-answer (unless voting on just the final answer field)

### Notes (Optional)
Self-consistency is an orchestration pattern, not a single-prompt pattern. The "template" is really a client-side loop. Include it in the repo because it composes with every reasoning pattern and is often the cheapest accuracy gain once decomposition plateaus.

Version History
v0.1 – initial version
