## Pattern: staged-refinement

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Revise in sequential passes that each target one dimension (correctness → clarity → concision).

---

### Mechanism
Single critique passes weight one dimension and neglect others. Sequential passes with per-pass focus, each constrained against changing other dimensions, produce more thorough refinement without regression.

---

### Template
"Produce your response through these stages. At each stage, only modify the dimension named for that stage.

Stage 1 — Draft: Write the initial response.

Stage 2 — Correctness pass: Revise to fix factual or logical errors. Do not change style.

Stage 3 — Clarity pass: Revise for clarity, structure, and flow. Do not change correctness.

Stage 4 — Concision pass: Tighten by approximately {N}% without dropping substantive content.

Label each stage's output. Final answer is the Stage 4 output.

Task: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Write a technical blog post (~600 words) explaining why a startup might choose Postgres over MongoDB.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Four stages: draft → correctness pass → clarity pass → concision pass (tighten ~25%). Label each stage's output.

Task: Write a technical blog post (~600 words) explaining why a startup might choose Postgres over MongoDB.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Polished long-form writing where multiple quality dimensions matter
- Outputs being prepared for external publication
- Technical documentation that must be correct AND readable AND concise
- Tasks where a single revision pass would force a trade-off but you want all dimensions improved
- Cases where the user wants to inspect intermediate versions, not just the final

---

### When NOT to Use
- Short outputs where multi-pass refinement is overkill
- Latency-sensitive responses
- Tasks where one dimension trivially dominates the others
- Conversational replies
- Creative work where mechanical passes flatten voice

---

### Failure Modes
- Stage bleed — clarity pass silently fixes correctness issues (or vice versa), losing the discipline
- Conservative passes — each stage produces near-identical output, suggesting the model isn't actually refining
- Regression in late stages — concision pass drops content that was just added for completeness
- Stage explosion — model invents extra stages or splits stages further
- Late-stage skipping — model produces stages 1-3 well but coasts on stage 4

---

### Examples

Example 1:
Input: "Four stages: draft, correctness pass, clarity pass, concision pass (tighten 20%). Label each. Task: Write release notes for a v2.1 update that includes 5 bug fixes and 2 minor features."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Staged refinement: draft → correctness → clarity → concision. Task: Draft a 1-page memo recommending a vendor for cloud hosting."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- reflect-and-revise (R&R is the single-pass version; staged-refinement is the multi-pass version)
- self-verification (use as the correctness-pass mechanism)
- length-budgeting (concision pass + explicit length budget reinforces tightening)
- negative-prompting (seed each pass with what NOT to do)

Conflicts with:
- direct-answer (deliberate multi-stage structure)
- low-latency-optimization (multiple sequential passes)
- creative-flow (mechanical passes flatten voice)
- brevity-directive (every stage produces output; net token cost is high)

---

### Notes (Optional)
The per-stage constraint ("do not change X") is what prevents the pattern from collapsing into one giant revision. Stage order matters: correctness before clarity before concision is the safe default — fixing wrong information before polishing it, and polishing before trimming. Reversing the order (concision first) tends to entrench errors and obscure them with tight prose. The number of stages can be tuned; three-stage and four-stage variants are common.

---

### Version History
v0.1 – initial version
