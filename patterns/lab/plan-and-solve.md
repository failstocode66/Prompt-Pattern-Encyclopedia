## Pattern: plan-and-solve
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Separate planning from execution so framing errors surface before they poison the solution.

---

### Mechanism
Forces the model to commit to an approach in writing before applying it. A bad plan is easier to catch (by the model or a reviewer) than a bad answer that was never framed as a plan. Reduces mid-task drift.

---

### Template
"First, devise a plan — list the steps you will take to solve this without solving it yet. Then carry out the plan step by step. Finally, state the answer.

Task: {task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
A small bakery wants to introduce a new pastry. They have a $2,000 budget, 3 staff members with 10 hours each to spare, and 4 weeks. Outline how they should approach it.

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
First, devise a plan — list the steps you will take to solve this without solving it yet. Then carry out the plan step by step. Finally, state the answer.

Task: A small bakery wants to introduce a new pastry. They have a $2,000 budget, 3 staff members with 10 hours each to spare, and 4 weeks. Outline how they should approach it.

Output
[placeholder — to be filled after testing]

---

### When to Use
- Multi-stage tasks where the right approach matters more than the right computation.
- Problems with non-obvious structure (ambiguous word problems, design tasks).
- Situations where premature commitment to a solution is a known risk.
- As a frame on top of cognitive-decomposition when decomposition alone doesn't catch framing errors.

---

### When NOT to Use
- Trivial tasks where planning doubles the output for no gain.
- Tasks where the "plan" is indistinguishable from the solution (e.g., "define X").
- Latency-critical calls.
- Tasks already well-served by a schema or direct lookup.

---

### Failure Modes
- Plan/execution divergence — model writes a plan, then solves a different problem.
- Plan too abstract to constrain execution ("Step 1: understand the problem").
- Over-planning — plan occupies most of the output and execution is rushed.
- Model treats "state the plan" as permission to skip real thinking during execution.

---

### Examples
Example 1: Input: "First devise a plan, then execute it. Task: Given four meeting-time constraints across three time zones, propose a 60-minute meeting slot."

Output: [placeholder — to be filled after testing]

Example 2: Input: "First devise a plan, then execute it. Task: A Python script is producing the wrong total. Here's the code and expected vs. actual output. Diagnose and fix."

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition (plan-and-solve is the higher-level frame; decomposition is the execution step)
- self-verification (verify the plan, then verify the execution)
- self-consistency
- role-persona ("You are a careful planner")

Conflicts with:
- direct-answer
- brevity-directive
- low-latency-optimization
- creative-flow

### Notes (Optional)
The plan step is most valuable when it names the assumptions and constraints explicitly. A plan that just restates the task steps in abstract terms adds tokens without adding signal. For repeat task types, consider converting a good plan into a few-shot example instead — it's cheaper.

Version History
v0.1 – initial version
