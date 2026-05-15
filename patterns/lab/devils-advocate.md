## Pattern: devils-advocate

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Construct the strongest case against the initial answer before finalizing it.

---

### Mechanism
Reasoning after an initial answer tends to be confirmatory, not critical. An adversarial role-switch forces counterarguments the model would otherwise suppress, so the revised answer addresses valid objections.

---

### Template
"Answer in three phases:

Phase 1 — Initial answer: Provide your best answer to the question.

Phase 2 — Devil's advocate: Now switch roles. As a skeptical reviewer, construct the strongest possible case AGAINST your initial answer. List at least 3 specific objections, failure cases, or overlooked considerations. Be adversarial, not balanced.

Phase 3 — Revised answer: For each objection, either revise the answer to address it or explain concisely why the objection doesn't apply. Produce the final answer.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Should our team adopt feature flags for all new code paths?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Three phases: (1) initial answer, (2) strongest case against it (at least 3 objections), (3) revised answer addressing each.

Question: Should our team adopt feature flags for all new code paths?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Decision questions where a wrong answer is expensive
- Recommendations where overlooked failure modes would matter
- Strategic or architectural choices with reasonable counter-positions
- Personal review of an answer before committing to action
- Adversarial design — security, legal, contract review

---

### When NOT to Use
- Factual lookups with no real opposing view
- Creative tasks where critique disrupts generative flow
- When the user wants confident direction, not a debate
- Latency-sensitive interactions
- Cases where there genuinely isn't a strong counter-position — the model will invent weak ones

---

### Failure Modes
- Weak objections — model generates straw critiques it can easily dismiss in Phase 3
- Symmetric hedging — initial answer and revised answer end up identical with caveats
- False balance — model treats every objection as valid and waters down a correct answer
- Position flipping — model abandons a correct initial answer because adversarial framing felt persuasive
- Theater — adversarial phase is performed but doesn't actually change the answer in any meaningful way

---

### Examples

Example 1:
Input: "Three phases: answer, strongest case against, revised answer. Question: Should I refactor this 800-line file into smaller modules before adding the new feature?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Devils advocate procedure. Question: Is hiring a junior engineer the right move for a 3-person startup right now?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- self-verification (verification checks correctness; devils-advocate stress-tests robustness)
- assumption-surfacing (surface assumptions, then attack them)
- reflect-and-revise (devils-advocate is one specific critique style; reflect-and-revise is broader)
- tree-of-thoughts (use to stress-test the selected branch)

Conflicts with:
- creative-flow (adversarial framing kills generative momentum)
- direct-answer (the pattern is by design a multi-phase detour)
- low-latency-optimization (three phases per question)
- empathic-response (adversarial tone clashes with warmth)

---

### Notes (Optional)
The discipline that makes this work is the explicit role-switch — "be adversarial, not balanced." Without it, the critique phase produces mild caveats rather than real challenges. Require a minimum number of objections (3+) to force the model past the easy first one. Watch for position flipping: a correct initial answer should usually survive Phase 3 with refinements, not get abandoned.

---

### Version History
v0.1 – initial version
