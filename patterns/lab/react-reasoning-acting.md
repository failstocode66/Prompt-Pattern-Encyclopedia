## Pattern: react-reasoning-acting

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Structure tool-using interactions as visible Thought / Action / Observation cycles.

---

### Mechanism
Conflating reasoning with action makes agent behavior opaque. The three-phase loop forces explicit reasoning between actions, making each step auditable and improving tool selection because each call must be justified.

---

### Template
"Use the following loop to complete the task. Each iteration is three phases:

Thought: [Reason about the current state. What do I know? What do I need next? Which tool is best?]
Action: [Tool name and arguments]
Observation: [Result returned by the tool]

Repeat as needed. When the task is complete, output:

Final Answer: [the answer]

Task: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
[With tool access to web search and a calculator] What was the inflation-adjusted box office of the top-grossing 1997 film, in 2024 dollars?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Use Thought / Action / Observation loops. End with "Final Answer:".

[With tool access to web search and a calculator] Task: What was the inflation-adjusted box office of the top-grossing 1997 film, in 2024 dollars?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Multi-step tool-using agents (search → analyze → search → answer)
- Workflows where each tool call depends on prior observations
- Debugging or developing agents — the Thought trace is the debug log
- Tasks needing both retrieval and computation interleaved
- Cases where the user wants to inspect agent reasoning before trusting the output

---

### When NOT to Use
- Single tool calls with no chaining (priming the format is overkill)
- Latency-sensitive agentic tasks where Thought tokens are wasted
- Tools that return so much output that Observation dwarfs everything
- Pure-text tasks with no tools available
- Modern frameworks that handle tool-calling natively without the explicit format (the framework may already provide the structure)

---

### Failure Modes
- Thought theater — model produces Thought blocks that don't actually inform the Action ("Thought: I should search for X. Action: [searches for Y]")
- Observation absorption — model receives a tool output and then proceeds as if it hadn't, ignoring the actual result
- Infinite loop — model never produces "Final Answer," cycling between Thought and Action indefinitely
- Premature final answer — model declares victory after one tool call without checking
- Action without observation — model produces Action blocks but doesn't wait for or process the tool result
- Format drift — Thought/Action/Observation labels drop off after a few iterations

---

### Examples

Example 1:
Input: "Use ReAct (Thought/Action/Observation, then Final Answer). Tools: web_search, calculator. Task: How much would $10,000 invested in NVIDIA stock on January 1 2020 be worth today?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "ReAct loop. Tools: file_read, file_write, bash. Task: Find all TODO comments in the /src directory and produce a summary report."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- tool-affordance-disclosure (declare tools upfront, then ReAct uses them)
- chain-of-thought (the Thought phase IS chain-of-thought, scoped to one decision)
- plan-and-solve (use plan-and-solve to draft the loop structure, then ReAct to execute)
- self-verification (verify Final Answer before returning)

Conflicts with:
- direct-answer (ReAct is by design multi-turn and verbose)
- brevity-directive (Thought tokens are extra by design)
- low-latency-optimization (extra reasoning per step adds latency)

---

### Notes (Optional)
Introduced by Yao et al. (Princeton/Google, 2022) as "ReAct: Synergizing Reasoning and Acting." Foundational pattern for agentic systems. Modern tool-calling APIs (function calling) often subsume the explicit format — the model's API-level tool calls replace explicit Action blocks. The pattern remains useful for human-readable agent traces, custom orchestration, or when you want explicit reasoning surfaced in the output rather than hidden behind a function call. Iteration caps are essential — without a max-iteration limit, ReAct loops can run away. Empty Thought blocks are a strong signal the model is bypassing the pattern.

---

### Version History
v0.1 – initial version
