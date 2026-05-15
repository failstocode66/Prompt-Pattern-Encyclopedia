## Pattern: audience-calibration

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Tune depth, vocabulary, and assumed knowledge by specifying the audience for the response.

---

### Mechanism
Without an explicit anchor, models default to a generic mid-expertise reader. Specifying the audience pulls generation toward the right register and assumed background — the reader-side counterpart to role-persona's speaker-side framing.

---

### Template
"Write your response for the following audience:
{audience description, including expertise level, what they already know, and what they don't know}.

Task: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Explain why an LLM might hallucinate.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Write your response for the following audience: a non-technical executive who has used ChatGPT a few times, knows it can be "wrong sometimes," but has no background in machine learning. They need to make a decision about whether to deploy an LLM in customer support. They have 90 seconds to read.

Task: Explain why an LLM might hallucinate.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Explanations that span expertise levels (technical → executive, expert → novice)
- Content with a defined reader (investors, customers, junior engineers, regulators)
- Translation across registers (research paper → blog post, internal doc → public announcement)
- Onboarding or pedagogical contexts where mismatched depth fails
- Anytime "explain it like I'm X" or "for an audience of Y" feels relevant

---

### When NOT to Use
- Cases where the audience is irrelevant (pure computation, code that the model produces and runs)
- When the user is the audience and has already supplied their context implicitly
- Generic queries with no obvious reader
- Tasks where the expected register is unambiguous from the task type

---

### Failure Modes
- Audience stereotype — "executive" produces buzzword bingo; "child" produces patronizing analogies
- Over-simplification — strips out content that the actual audience could handle
- Under-simplification — model claims to calibrate but maintains its default depth
- Audience drift — opens at the right level then drifts back to default mid-response
- Mismatched omissions — leaves out information the audience needs and keeps things they don't

---

### Examples

Example 1:
Input: "Audience: a senior backend engineer with no frontend experience who needs to add basic state management to their first React component. Task: Explain useState."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Audience: a board of non-technical investors evaluating whether to fund a generative AI startup. They need to assess defensibility, not implement anything. Task: Explain what a vector database is and why it matters."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- role-persona (speaker frame + audience frame is the canonical pairing)
- few-shot-examples (examples calibrated to the same audience reinforce the level)
- length-budgeting (audience implies a length expectation)
- analogical-reasoning (analogies pull from the audience's domain)

Conflicts with:
- strict-output-format (if the format is technical but the audience is non-technical, tension emerges)
- direct-answer (audience calibration usually requires some scene-setting)

---

### Notes (Optional)
Audience descriptions are most useful when they specify what the reader *already knows* and *doesn't know*, not just an expertise level. "A senior engineer" is vague; "a senior backend engineer who has not touched frontend in 5 years" pins the prior knowledge precisely. Generic audience labels ("layperson," "expert") underperform specific ones. Always check for audience drift in long responses — models calibrate at the opening and slowly regress to defaults.

---

### Version History
v0.1 – initial version
