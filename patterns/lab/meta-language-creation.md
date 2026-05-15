## Pattern: meta-language-creation

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Bind compact tokens to elaborate behaviors so repeated instructions can be invoked through shorthand.

---

### Mechanism
Repeated complex instructions waste tokens and drift when restated. Binding compact tokens to elaborate behaviors up front reduces per-turn length and increases cross-turn consistency.

---

### Template
"For the rest of this conversation, use the following shorthand. Acknowledge the bindings, then wait for my first instruction.

- When I write `{token_1}`, treat it as: {expanded meaning 1}
- When I write `{token_2}`, treat it as: {expanded meaning 2}
- When I write `{token_3}`, treat it as: {expanded meaning 3}

Confirm you understand the bindings."

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
[Across 10 turns the user repeatedly types]: "Refactor this code for readability without changing behavior. Use descriptive names, extract helper functions where appropriate, and add docstrings. Don't change the function signature."

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
For the rest of this conversation:
- When I write `/refactor`, treat it as: refactor the most recent code I sent for readability without changing behavior; use descriptive names, extract helper functions where appropriate, add docstrings, do not change the function signature.
- When I write `/explain`, treat it as: explain what the most recent code does in plain language, line-by-line if non-trivial.
- When I write `/test`, treat it as: produce pytest unit tests covering the happy path and at least 2 edge cases.

Confirm you understand.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Long sessions with repeated patterns of instruction
- Building a personal command vocabulary for an assistant workflow
- Multi-step pipelines where each step has a known invocation pattern
- Reducing typing overhead in conversational coding or writing sessions
- Pair-programming or co-writing flows with stable repeated tasks

---

### When NOT to Use
- One-off interactions where setup cost exceeds savings
- Tasks where each instruction is unique
- Cases where the bindings are too numerous to track (>5-7 bindings degrades reliability)
- New users or new contexts where the bindings need clarification each time
- Interfaces with constrained context windows where the bindings themselves consume budget

---

### Failure Modes
- Binding drift — model interprets `/refactor` slightly differently across turns
- Binding loss — model forgets bindings after long context or compression
- Collision with model conventions — chosen tokens clash with patterns the model already responds to (e.g., `/help`)
- Partial recall — model honors some bindings but not others
- Over-extension — user introduces new tokens mid-session without re-binding, and the model guesses

---

### Examples

Example 1:
Input: "For the rest of this session: `/short` = rewrite the most recent text in half the words. `/long` = expand it by 50% adding concrete examples. `/neutral` = remove emotional or persuasive language. Confirm."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Bindings: `crit` = list 3 weaknesses, `pol` = polish for clarity, `tldr` = produce a 2-sentence summary. Confirm and wait."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- few-shot-examples (demonstrate the expected behavior for each binding)
- structured-output-schema (each binding can have a schema)
- instruction-anchoring (re-anchor the bindings in long sessions)
- response-priming (prime each invocation with the expected output shape)

Conflicts with:
- low-latency-optimization (initial setup adds overhead, though it pays back across turns)
- direct-answer (some commands explicitly want longer multi-step outputs)
- (mostly composes — meta-language sits above other patterns as an interaction layer)

---

### Notes (Optional)
From the Vanderbilt prompt patterns catalog (White et al., 2023) as "Meta Language Creation." Best for sustained sessions; less useful for one-shot prompts. Keep the binding set small (3-6 tokens) for reliable recall — beyond ~7, drift sets in. In long sessions, periodically restate the bindings (or use instruction-anchoring) to prevent loss. Avoid token strings that the model has been trained to handle in fixed ways (e.g., system-style commands).

---

### Version History
v0.1 – initial version
