## Pattern: strict-output-format
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Lock output to a single parseable format (JSON, single label, CSV row) with no surrounding prose.

---

### Mechanism
Removes optionality at generation time. The model is told there is exactly one valid output shape; preamble, explanation, and markdown are explicitly forbidden.

---

### Template
"Respond with only {format}. No explanation, no preamble, no markdown code fences.

{task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
Classify this email as spam or not spam: "Congratulations! You've been selected for a free cruise. Click here to claim."

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Respond with only one word: either "spam" or "not_spam". No explanation, no preamble.

Classify this email: "Congratulations! You've been selected for a free cruise. Click here to claim."

Output
[placeholder — to be filled after testing]

---

### When to Use
- API integrations and tool-call plumbing.
- Classification pipelines that pipe output directly into code.
- Bulk batch jobs where any prose breaks the parser.
- When the downstream system is brittle and can't tolerate variation.

---

### When NOT to Use
- Tasks where the user benefits from seeing reasoning.
- Exploratory or ambiguous queries.
- Conversational UX.
- Anywhere a wrong classification without explanation would cause silent downstream errors.

---

### Failure Modes
- Prose leakage — model prepends "Sure!" or appends "Let me know if..." despite instructions.
- Markdown fences — model wraps JSON in ```json blocks, breaking naive parsers.
- Invalid format under edge cases — malformed JSON, misquoted strings, trailing commas.
- Silent failure — model returns format but with wrong or fabricated content.

---

### Examples
Example 1: Input: "Respond with only a JSON object matching this schema: {sentiment: 'positive'|'negative'|'neutral', confidence: 0-1}. No preamble. Text: 'The meeting could have been an email.'"

Output: [placeholder — to be filled after testing]

Example 2: Input: "Respond with only one word: the ISO 3166-1 alpha-2 country code. No preamble. Country: 'Sverige'"

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- few-shot-examples (one clean example is the strongest format anchor)
- structured-output-schema
- brevity-directive
- direct-answer
- low-latency-optimization

Conflicts with:
- cognitive-decomposition (no room for steps)
- plan-and-solve
- self-verification (no room for a review pass)
- creative-flow
- empathic-response
- role-persona (often — personas want to talk)

### Notes (Optional)
Always validate parseability, not just presence. A JSON-shaped string can still be malformed. For maximum robustness, use the provider's native structured-output or tool-calling mode instead of prompt-level constraints. If you must use prompting, include one filled example — format compliance jumps meaningfully with a single demo.

Version History
v0.1 – initial version
