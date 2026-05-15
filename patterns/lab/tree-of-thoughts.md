## Pattern: tree-of-thoughts

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Generate multiple candidate approaches, evaluate each, and commit to the strongest.

---

### Mechanism
Linear reasoning commits to one path early; if wrong, the trace is wasted. Forced branching produces multiple approaches and selects the strongest, trading tokens for solution-space coverage.

---

### Template
"Solve this problem in three phases:
1. Generate 3 distinct candidate approaches. Each should attack the problem from a different angle.
2. For each approach, briefly trace its reasoning and identify its main weakness.
3. Select the strongest approach (or combine elements) and produce the final answer.

If the selected approach fails partway, backtrack and try another.

Problem: {problem}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Design a caching strategy for a read-heavy social media feed that handles 100k requests/second.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Solve this in three phases: (1) generate 3 distinct approaches, (2) evaluate weaknesses of each, (3) select and produce the strongest.

Problem: Design a caching strategy for a read-heavy social media feed that handles 100k requests/second.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Design problems with multiple legitimate solution architectures
- Strategic decisions where the obvious answer is often wrong
- Puzzles and games (chess, Game of 24, planning problems)
- High-stakes problems where exploration cost is justified
- Cases where the user wants to see the trade space, not just one answer

---

### When NOT to Use
- Problems with a single canonical correct answer (arithmetic, lookup)
- Latency- or token-budget-constrained tasks
- Conversational or quick-answer contexts
- When the first approach is obviously correct — branching adds noise

---

### Failure Modes
- Fake diversity — three approaches that are minor variants of the same approach
- Premature commitment — model picks the first approach in phase 3 regardless of evaluation
- Evaluation theater — weaknesses listed are generic and don't actually affect ranking
- No backtracking — when the selected approach fails, model continues forcing it instead of switching
- Combinatorial sprawl — branches multiply without convergence

---

### Examples

Example 1:
Input: "Use tree-of-thoughts (3 candidate approaches, evaluate, select). Problem: Design an algorithm to deduplicate near-identical text snippets at scale."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Three candidate strategies, evaluate each, then commit. Problem: How should a solo founder allocate their first month after incorporation?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- self-consistency (both involve sampling alternatives; ToT evaluates explicitly, SC votes)
- self-verification (verify the selected approach before committing)
- cognitive-decomposition (decompose, then ToT inside each subtask)
- devils-advocate (use to stress-test the selected branch)

Conflicts with:
- direct-answer (ToT is deliberately exploratory)
- brevity-directive (multiple branches inherently expand output)
- low-latency-optimization (branching is expensive)

---

### Notes (Optional)
Originates from Yao et al. (Princeton/Google, 2023). Full ToT in research uses external search over a tree with backtracking via separate model calls; the single-prompt version here captures the spirit cheaply. For high-stakes problems, prefer an agentic loop where each branch is evaluated in its own call and the orchestrator selects. Diversity of branches matters — if the model produces three slight variants, the pattern degrades into chain-of-thought.

---

### Version History
v0.1 – initial version
