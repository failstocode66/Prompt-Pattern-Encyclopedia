## Pattern: reflect-and-revise

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Draft, critique, then revise in a single self-correction pass.

---

### Mechanism
First-pass outputs have predictable shortcomings (incompleteness, weak transitions, unsupported claims). A structured self-critique surfaces them and revision incorporates the fixes — broader than self-verification, which targets only correctness.

---

### Template
"Produce your response in three labeled phases.

Phase 1 — Draft: Write your initial answer.

Phase 2 — Critique: List 3-5 specific weaknesses in your draft. Be concrete. Each critique should name what is wrong and what would improve it. Vague critiques ('could be clearer') are not allowed.

Phase 3 — Revision: Rewrite the answer addressing each weakness from Phase 2.

Task: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Write a one-page README for a CLI tool that converts CSV files to JSON.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Three phases: (1) draft, (2) list 3-5 specific weaknesses in the draft, (3) revise.

Task: Write a one-page README for a CLI tool that converts CSV files to JSON.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Long-form writing where first drafts predictably need editing (essays, READMEs, emails)
- Outputs where coverage matters and gaps are easy to miss
- Tasks with multiple quality dimensions (clarity, completeness, tone, structure)
- High-stakes single-shot deliverables where a second pass is cheap insurance
- Outputs the user will publish or share externally

---

### When NOT to Use
- Short factual answers where revision adds nothing
- Tasks where the first draft is the only target (live conversation, brainstorming)
- Latency-sensitive contexts
- Cases where the critique step will produce diminishing returns relative to its token cost
- Creative tasks where the draft's spontaneity is the point

---

### Failure Modes
- Vague critique — Phase 2 produces "could be more concise" without specifics, so Phase 3 doesn't know what to change
- Cosmetic revision — Phase 3 rewords without addressing the substantive issues identified in Phase 2
- Critique-revision mismatch — revision fixes things that weren't critiqued and ignores things that were
- Self-flattery — model produces only minor critiques to make the draft look strong
- Regression — revision introduces new problems while fixing old ones

---

### Examples

Example 1:
Input: "Draft, critique (3-5 specific weaknesses), revise. Task: Write a customer apology email for a 12-hour service outage."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Three-phase reflect-and-revise. Task: Explain transformer attention to a developer who knows Python but no ML."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- self-verification (verify correctness in Phase 2 alongside quality critique)
- devils-advocate (specialized form of critique focused on opposing arguments)
- negative-prompting (use to seed the critique criteria — "did the draft do these forbidden things?")
- structured-output-schema (lock the three phases into a schema)

Conflicts with:
- direct-answer (multi-phase by design)
- creative-flow (critique step interrupts flow)
- low-latency-optimization (three passes per response)
- brevity-directive (each phase adds length)

---

### Notes (Optional)
The load-bearing instruction is "specific" — without it, Phase 2 produces generic critiques and Phase 3 has nothing concrete to act on. Requiring 3-5 critiques (not just one) prevents the easy single-fix shortcut. For multi-dimensional revision (correctness AND clarity AND length), use staged-refinement instead, which gives each dimension its own pass.

---

### Version History
v0.1 – initial version
