## Pattern: structured-output-schema
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Force outputs into a labeled, typed structure so downstream code can parse them and the model has fewer degrees of freedom to hand-wave.

---

### Mechanism
An explicit schema replaces free-form narration with slot-filling. The model generates values for named fields instead of composing prose, which reduces format drift and makes missing reasoning visible.

---

### Template
"Respond only in this JSON schema:
{
  "field_1": "<type/description>",
  "field_2": "<type/description>",
  ...
}

Task: {task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Summarize this support ticket: "Customer reports app crashes on launch after updating to version 4.2 on iPhone 14, iOS 18.2. Happens every time. Tried reinstalling — no change."

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Respond only in this JSON schema:
{
  "issue": "<one-sentence description>",
  "affected_version": "<app version>",
  "platform": "<device and OS>",
  "reproducibility": "<always | intermittent | once>",
  "user_actions_taken": ["<step>", ...]
}

Task: Summarize this support ticket: "Customer reports app crashes on launch after updating to version 4.2 on iPhone 14, iOS 18.2. Happens every time. Tried reinstalling — no change."

Output
[placeholder — to be filled after testing]

---

### When to Use
- Programmatic downstream consumption (pipelines, APIs, tools).
- Extraction tasks where fields map cleanly to schema slots.
- Multi-field reasoning where each field is a discrete sub-conclusion.
- Batch processing that requires consistent output shape.

---

### When NOT to Use
- Free-form prose, explanations, or creative work.
- Conversational replies.
- Tasks where the right answer doesn't fit the schema and forcing it loses information.
- Single-value outputs (use direct-answer instead).

---

### Failure Modes
- Over-constraint — schema omits a field the task actually needs, and the model either invents a field or silently drops the info.
- Empty slots — model fills every field even when evidence is missing, fabricating values.
- Schema drift — model adds commentary outside the JSON, breaking parsers.
- Type violations — model returns strings where numbers were expected, or vice versa.

---

### Examples
Example 1: Input: Extract product info into a fixed schema: {name, price, in_stock, category} from: "Blue ceramic mug, 12oz, $14.99, currently out of stock. Kitchenware."

Output: [placeholder — to be filled after testing]

Example 2: Input: Classify a support ticket into {category, priority, requires_human_review, suggested_response} given the ticket text.

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- few-shot-examples (one filled example removes most ambiguity)
- cognitive-decomposition (each step maps to a field)
- self-verification (verify field-by-field)
- strict-output-format (JSON-only pairs cleanly)

Conflicts with:
- creative-flow
- empathic-response
- role-persona (persona wants prose)

### Notes (Optional)
Prefer strict schemas with enum values for categorical fields. Include a "notes" or "uncertainty" field when evidence is often incomplete — it gives the model a legitimate slot for hedging instead of fabricating. Validate outputs with a schema checker, not with trust.

Version History
v0.1 – initial version
