## Pattern: least-to-most-prompting

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Decompose a problem into an ordered easy-to-hard sequence where prior answers feed later sub-problems.

---

### Mechanism
Hard problems often compose from easier ones whose answers are prerequisites. Solving in dependency order ensures each step has its inputs ready, with prior answers carried forward as scaffolding.

---

### Template
"Solve this problem in two phases.

Phase 1 — Decompose: Break the problem into an ordered sequence of sub-problems, from easiest to hardest, where each sub-problem builds on the previous. List the sequence first.

Phase 2 — Solve in order: Answer each sub-problem in sequence. For each one, explicitly reference the answers from prior sub-problems as inputs.

Problem: {problem}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
A company has 3 warehouses (A, B, C) and 4 stores. Warehouse A can supply 100 units/day, B can supply 150, C can supply 200. Stores need 80, 120, 100, 150 units/day respectively. Shipping cost per unit from each warehouse to each store varies. What's the minimum-cost shipping plan?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Solve in two phases. Phase 1: decompose into a sequence of sub-problems ordered easiest to hardest. Phase 2: solve each in order, using prior answers.

Problem: A company has 3 warehouses (A, B, C) and 4 stores. Warehouse A can supply 100 units/day, B can supply 150, C can supply 200. Stores need 80, 120, 100, 150 units/day. Shipping cost per unit from each warehouse to each store varies. What's the minimum-cost shipping plan?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Problems where sub-answers feed into later sub-problems (math word problems with chained quantities, logistics, planning)
- Tasks the model fails on directly but solves correctly when given hints toward the easier sub-cases
- Compositional reasoning where complexity scales with the number of dependent steps
- Curriculum-style learning where intermediate steps are pedagogically useful

---

### When NOT to Use
- Problems where the sub-problems are independent (use cognitive-decomposition instead)
- Tasks with no natural difficulty gradient
- Simple single-step problems
- Latency-sensitive contexts

---

### Failure Modes
- Wrong ordering — model treats the hardest sub-problem first, defeating the scaffolding
- Missing dependencies — sub-problems are listed but answers aren't carried forward to later steps
- Over-decomposition — easy problem split into 8 trivial sub-problems
- Sub-problem hallucination — model invents sub-problems that aren't actually part of the main problem

---

### Examples

Example 1:
Input: "Decompose easiest-to-hardest, then solve in order, using prior answers as inputs. Problem: Given a list of meeting times, find the minimum number of conference rooms needed."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Least-to-most: order sub-problems by difficulty, solve in sequence. Problem: A user asks how to migrate their monolith to microservices. Produce a migration plan."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-decomposition (LtM is a specialized form — adds ordering and dependency)
- chain-of-thought (each sub-problem gets a CoT)
- plan-and-solve (plan-and-solve produces a plan; LtM produces an ordered dependency chain)
- self-verification (verify each sub-answer before using it in the next)

Conflicts with:
- direct-answer (deliberate multi-step structure)
- brevity-directive (sequential decomposition is verbose)
- low-latency-optimization (multiple sequential steps)

---

### Notes (Optional)
Introduced by Zhou et al. (Google, 2022). Empirically improves performance on compositional generalization benchmarks where pure chain-of-thought plateaus. The key discipline is *dependency ordering* — without it, this is just decomposition. When sub-problems are truly independent, use cognitive-decomposition instead; when they cascade, LtM is the better fit.

---

### Version History
v0.1 – initial version
