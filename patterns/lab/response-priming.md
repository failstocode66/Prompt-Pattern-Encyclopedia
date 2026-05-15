## Pattern: response-priming

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Lock output direction or format by prefilling the start of the model's response.

---

### Mechanism
Autoregressive models continue from context. Prefilling forces continuation from the chosen tokens, bypassing preamble and hedging, and locks structured output into the implied format (e.g., `{` for JSON).

---

### Template
"[user message ending with the task]

[assistant response prefilled with]: {chosen prefix}"

Examples of effective prefixes:
- For JSON: `{"`
- For tables: `| Column1 | Column2 |\n|---------|---------|\n|`
- For a confident answer: `The answer is:`
- For a structured analysis: `1. `

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Return the parsed contact info from this string as JSON: "Jane Doe, jane@example.com, 555-0199"

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
User: Return the parsed contact info from this string as JSON: "Jane Doe, jane@example.com, 555-0199"

Assistant (prefilled): {"name":

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Structured output where format must be exact (JSON, XML, CSV, code)
- Skipping preamble in API contexts where downstream code expects clean output
- Anchoring tone or posture for the entire response
- Continuing a partial output (resume from a known prefix)
- Multi-turn agents where each turn must start in a known state

---

### When NOT to Use
- Conversational replies where preamble is appropriate
- Cases where the model legitimately needs to refuse or clarify — priming can over-commit it
- Open-ended creative tasks where forcing a prefix kills variance
- Interfaces that don't support assistant-turn prefill (some chat UIs)

---

### Failure Modes
- Over-commitment — model continues from a prefix that's wrong for the actual task and produces nonsense rather than correcting
- Format break — model continues correctly for a few tokens, then drifts (especially with weak prefixes)
- Refusal bypass concerns — priming has been used to bypass safety; well-aligned models still detect and refuse
- Prefix too long — over-specifying the prefix leaves nothing meaningful for the model to generate
- Bad-prefix cascade — typo or wrong character in prefix can derail the rest of the response

---

### Examples

Example 1:
Input: "User: Classify this review as positive/negative/neutral and give confidence 0-1. Review: '{review}'. Assistant (prefilled): {\"sentiment\": \""
Output: [placeholder — to be filled after testing]

Example 2:
Input: "User: List the top 3 risks of this deployment plan. Assistant (prefilled): 1."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- structured-output-schema (priming the opening of the schema reinforces format adherence)
- strict-output-format (priming locks the format choice the format spec asks for)
- length-budgeting (compact prefix + length budget produces tight outputs)
- delimiter-fencing (prefill the opening delimiter of the output)

Conflicts with:
- creative-flow (priming constrains opening, reducing generative variance)
- empathic-response (priming a structured prefix forecloses warm conversational openings)
- direct-answer (often complementary, but a chatty prefix can re-introduce preamble)

---

### Notes (Optional)
Requires an interface that supports assistant-turn prefill (most chat completion APIs do; some chat UIs do not). The prefix should be the shortest text that reliably locks the desired direction — over-long prefixes leave little room for actual generation. Empirically one of the highest-leverage techniques for structured output, since it converts a "produce JSON" instruction into "continue this partial JSON," which the model handles much more reliably.

---

### Version History
v0.1 – initial version
