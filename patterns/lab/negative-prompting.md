## Pattern: negative-prompting

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Steer output by explicitly listing what to avoid, blocking unwanted defaults the model would otherwise produce.

---

### Mechanism
Models follow positive instructions but emit unwanted defaults (hedging, preambles, stock phrasings) no one asked for. Explicit prohibitions block these at generation; pairs best with positive instructions — positive defines the target, negative removes contamination.

---

### Template
"Do the following: {task}

Do NOT:
- {prohibited pattern 1}
- {prohibited pattern 2}
- {prohibited pattern 3}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Write a one-paragraph product description for a new wireless mouse.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Write a one-paragraph product description for a new wireless mouse.

Do NOT:
- Use the words "innovative," "revolutionary," "cutting-edge," or "game-changing"
- Open with the product name
- Include hedging phrases ("may," "could potentially")
- Exceed 80 words

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Output where the default contains predictable unwanted patterns (marketing fluff, hedging, preamble)
- Brand or style guides that prohibit specific words or phrasings
- Code generation where certain anti-patterns must be avoided
- Anywhere the model has a strong default that conflicts with your goal
- Pairing with positive instructions to disambiguate intent

---

### When NOT to Use
- Tasks where the model's default behavior is already correct
- Cases where the prohibition list grows so long it becomes the prompt
- Creative tasks where prohibitions over-constrain and flatten output
- When the desired behavior is easier to specify positively than negatively
- Cases where you're using negation to make a request you couldn't make positively — negation alone is rarely sufficient

---

### Failure Modes
- Negation salience — listing a forbidden word can prime the model to think about it and use synonyms that smuggle the same idea
- List inflation — 15 prohibitions produce a prompt the model can't reliably track
- Negative-only prompts — without a positive target, the model has too much freedom in what to produce
- Selective compliance — model honors prohibitions in the opening sentences then drifts later
- Forbidden synonyms — model avoids the literal word but uses a near-equivalent

---

### Examples

Example 1:
Input: "Write a customer email about a delayed order. Do NOT: apologize more than once; use the phrase 'unfortunately'; promise a specific new delivery date; exceed 6 sentences."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Generate a Python function that deduplicates a list. Do NOT: use a for loop; rely on third-party libraries; modify the input list in place."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- strict-output-format (positive format + negative anti-patterns)
- brevity-directive (negation list often pairs with terseness goals)
- role-persona (a role implies a register; negation enforces the boundary)
- reflect-and-revise (use the prohibition list as critique criteria)

Conflicts with:
- creative-flow (prohibitions constrain divergent generation)
- direct-answer (lots of negation can drag a direct answer into prose-shaped output)

---

### Notes (Optional)
Best when paired with positive instruction — pure negation gives the model too much freedom. Watch for *negation salience*: prohibiting a word can make the model salient to its synonyms. If a word must really not appear, sometimes a positive replacement target works better ("use 'fast' instead of 'rapid'") than a prohibition. Keep the negation list short — 3-5 prohibitions is reliable; longer lists degrade compliance.

---

### Version History
v0.1 – initial version
