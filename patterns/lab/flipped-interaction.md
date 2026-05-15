## Pattern: flipped-interaction

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Shift the model into interview mode, eliciting information from the user before producing the answer.

---

### Mechanism
Default behavior is to answer immediately with plausibly-defaulted parameters. Inverting the turn structure forces the model to ask before answering, trading latency for output relevance and reducing wasted generation on wrong assumptions.

---

### Template
"I want you to act as {role/task owner}. Instead of answering immediately, ask me questions one at a time until you have enough information to {desired output}. Ask the most important question first and adapt subsequent questions based on my answers. When you have enough, say 'I have enough to proceed' and produce the output.

Goal: {goal}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Help me plan a birthday party for my partner.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
I want you to act as a party planner. Instead of answering immediately, ask me one question at a time until you have enough to plan the event. Ask the most important question first and adapt based on my answers. When you have enough, say "I have enough to proceed" and produce the plan.

Goal: Plan a birthday party for my partner.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Tasks where the model can't give a useful answer without more context (planning, custom-fit recommendation, personalized advice)
- User-facing applications where elicitation is part of the UX (intake, onboarding, configuration)
- Coaching, tutoring, or therapeutic dialogues that benefit from guided discovery
- When the user explicitly wants a conversational experience rather than a one-shot answer

---

### When NOT to Use
- One-shot completion tasks (translation, summarization of supplied content, code formatting)
- API-style requests where the caller expects a single response, not a dialogue
- When latency or turn count is constrained
- When the user has already supplied complete context — additional questions feel like busywork

---

### Failure Modes
- Question stacking — asks 5 questions at once despite "one at a time" instruction
- Endless interrogation — keeps asking when it already has enough to act
- Premature exit — declares "I have enough" after one question and produces a generic answer
- Off-target questions — asks for information that doesn't affect the output
- Question fatigue — user disengages before the interview completes

---

### Examples

Example 1:
Input: "Act as a technical interviewer. Ask me questions one at a time until you've assessed my Python skill level, then give me a score from 1-10 with justification. Ask the most important question first."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Act as a travel planner. Ask me one question at a time until you can recommend a 7-day itinerary that fits my budget, interests, and constraints. Say 'I have enough to proceed' when ready."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- role-persona (a defined role shapes which questions get asked)
- cognitive-verifier (similar elicitation impulse, but verifier answers its own questions — flipped asks the user)
- empathic-response (warm tone keeps the user engaged through the interview)
- structured-output-schema (apply to the final output once enough info is gathered)

Conflicts with:
- direct-answer (opposite turn structure)
- low-latency-optimization (multi-turn elicitation increases total latency)
- strict-output-format (until elicitation completes, output is conversational, not formatted)

---

### Notes (Optional)
From the Vanderbilt prompt patterns catalog (White et al., 2023). The "one question at a time" constraint is load-bearing — without it, models tend to dump a questionnaire. Adding an explicit exit signal ("I have enough to proceed") helps the model know when to stop asking and start producing. Works particularly well when paired with a budget hint ("ask at most 5 questions") to prevent over-elicitation.

---

### Version History
v0.1 – initial version
