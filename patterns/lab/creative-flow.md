## Pattern: creative-flow
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Elicit voice-driven, rhythm-sensitive creative output by explicitly suppressing analytical overhead.

---

### Mechanism
Instructions to skip planning and explanation free the model from the default assistant-register (structured, hedging, scaffolded) and let it generate at the register appropriate to the creative form. The permission itself is the mechanism.

---

### Template
"Write without overthinking. Don't plan, don't explain, don't caveat. Just write.

{task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Write a six-word memoir about autumn.

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Write without overthinking. Don't plan, don't explain, don't caveat. Just write.

A six-word memoir about autumn.

Output
[placeholder — to be filled after testing]

---

### When to Use
- Poetry, flash fiction, aphorisms, jokes, taglines.
- Short-form creative work where voice matters more than information.
- Brainstorming — generating variation without premature editing.
- Any creative form where structure actively hurts the output.

---

### When NOT to Use
- Anything requiring factual accuracy.
- Reasoning tasks — flow kills correctness.
- Long-form writing with structural requirements (novels, essays with a thesis).
- When the user needs the work to defend a specific claim.

---

### Failure Modes
- Voice over accuracy — output is stylish and factually wrong where it claimed to be informative.
- Shallow stylization — model mimics "creative" register (adjective stacks, em-dashes) without actual craft.
- No guardrails — drifts into cliché or purple prose with nothing to pull it back.
- Registers incorrectly — adopts a literary voice for a task that wanted playful, or vice versa.

---

### Examples
Example 1: Input: "Write without overthinking. Just write. A haiku about a coffee shop at 7am."

Output: [placeholder — to be filled after testing]

Example 2: Input: "Write without overthinking. Just write. A tagline for a bike shop that specializes in repairs for commuters."

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- role-persona (a specific creative voice reinforces flow — "you are a terse noir narrator")

Conflicts with:
- cognitive-decomposition
- plan-and-solve
- structured-output-schema
- self-verification
- few-shot-examples (demos flatten voice toward themselves)
- brevity-directive (sometimes — depends on whether length is part of the form)

### Notes (Optional)
Creative-flow is a permission pattern, not a generation engine. It removes the governor; the output still depends on the task framing. Pair with a specific form (haiku, six-word memoir, tagline) — open-ended "be creative" tends to produce middle-of-the-road output regardless of flow framing. If output feels flat, the fix is usually more specific task framing, not stronger flow language.

Version History
v0.1 – initial version
