## Pattern: length-budgeting

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Enforce a quantitative cap on output length (words, sentences, paragraphs) to fit downstream constraints.

---

### Mechanism
Models default to verbose, padded outputs. A numeric budget shifts the generation target — the model must pre-select what to include — and is more enforceable than stylistic terseness directives because the constraint is measurable.

---

### Template
"Respond in no more than {N} {units: words / sentences / paragraphs / bullet points}.

If you cannot fit a complete answer within the budget, prioritize the most decision-relevant content and explicitly omit lower-priority context. Do not pad to reach the budget.

Task: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Explain how OAuth 2.0 works.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Respond in no more than 100 words. Prioritize the most decision-relevant content; omit lower-priority context. Do not pad to reach the budget.

Task: Explain how OAuth 2.0 works.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Outputs feeding into downstream systems with hard length limits (SMS, push notifications, summary fields)
- UIs with visible character or word limits
- Cases where the user wants a specific length, not just "short"
- Cost or latency budgets that bound generation
- Forcing decision-relevant content selection when everything cannot fit

---

### When NOT to Use
- Tasks where premature truncation produces wrong or unsafe outputs (medical, legal, safety-critical)
- Open-ended creative writing where length should match content
- Cases where the right answer is genuinely longer than the budget — the model will either pad or omit critical content
- When a stylistic "be terse" directive would suffice without a hard number

---

### Failure Modes
- Budget overshoot — model exceeds the cap by 10-50% and pretends not to notice
- Budget underuse — model produces a fraction of the budget when more content would help
- Padding — model reaches the budget by repeating itself or adding filler
- Critical-content omission — model trims the wrong material to fit
- Unit confusion — "100 words" interpreted as "100 tokens" or "100 characters"

---

### Examples

Example 1:
Input: "Respond in no more than 3 sentences. Prioritize what the reader needs to act on. Task: Should we use Docker or run our service directly on the host?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Respond in exactly 5 bullet points, each ≤15 words. Task: Onboarding tips for a new remote hire's first week."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- brevity-directive (style + quantitative budget reinforce each other)
- strict-output-format (format spec + length cap produces tight, predictable outputs)
- response-priming (priming opens the answer in tight form, budget closes it tight)
- direct-answer (budget enforces the directness)

Conflicts with:
- cognitive-decomposition (decomposition expands output)
- chain-of-thought (reasoning trace consumes budget)
- skeleton-of-thought (outline + expansion exceeds tight budgets)
- cognitive-verifier (sub-questions blow the budget)

---

### Notes (Optional)
Words is the most reliable unit; sentences and paragraphs work but have fuzzier edges; tokens are precise but inscrutable to humans. Models routinely overshoot by ~10-20% — if a hard limit matters, set the budget slightly below the true limit. For very tight budgets, pair with response-priming to lock the opening so the model doesn't burn budget on preamble. When the right answer genuinely won't fit, prefer raising the budget over forcing the model to omit critical content silently.

---

### Version History
v0.1 – initial version
