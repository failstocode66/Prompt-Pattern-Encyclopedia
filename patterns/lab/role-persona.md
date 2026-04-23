## Pattern: role-persona
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Steer tone, depth, vocabulary, and assumed expertise by assigning the model a specific role.

---

### Mechanism
Conditions the model on the distribution of outputs typical for that role. "Patient tutor" pulls toward slow analogies; "skeptical editor" pulls toward critique; "senior engineer" pulls toward tradeoff language.

---

### Template
"You are a {role}. {task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Explain how a database index works.

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
You are a patient CS professor explaining concepts to a first-year student. Explain how a database index works.

Output
[placeholder — to be filled after testing]

---

### When to Use
- Tone shaping (formal, warm, terse, authoritative).
- Depth calibration (ELI5 vs. expert briefing).
- Domain-specific vocabulary where the role implies the lexicon.
- Critique or review tasks where an adversarial frame helps.

---

### When NOT to Use
- Pure computation or retrieval — role adds noise without benefit.
- When the role's stereotype contradicts the task ("you are a pirate" for medical advice).
- When the role invokes persona theater at the expense of substance.
- When a concrete style guide or schema would work better.

---

### Failure Modes
- Stereotype drift — model leans on cliché role behavior instead of content quality.
- Persona theater — catchphrases and mannerisms crowd out the actual answer.
- Role-safety tension — personas framed as "unrestricted expert" can push the model toward refusal or degraded output.
- Over-specification — layering too many role attributes muddies the signal.

---

### Examples
Example 1: Input: "You are a senior code reviewer focused on maintainability. Review this function: {code}"

Output: [placeholder — to be filled after testing]

Example 2: Input: "You are a clinical nurse educator. Explain blood pressure numbers to a newly diagnosed patient."

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition
- self-verification
- empathic-response
- creative-flow
- few-shot-examples

Conflicts with:
- strict-output-format (often — persona produces prose that breaks schemas)
- direct-answer (persona wants to explain; direct-answer wants silence)

### Notes (Optional)
Roles are multipliers on other patterns, not standalone engines. A role without a task still produces something; a role with a clear task and constraint produces something aligned. Prefer specific roles ("emergency-room triage nurse") over generic ones ("expert"). Validate that the role didn't silently change the answer, only the presentation.

Version History
v0.1 – initial version
