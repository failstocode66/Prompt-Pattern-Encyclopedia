## Pattern: least-to-most-prompting

Version: 1.0
Status: Core
Last Updated: 2026-07

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

A *measured* head-to-head — and the most honest of the four, because the delta is the smallest. The task is a chained workforce-planning calculation (each quantity feeds the next). Read the caveat in the note: all three modern test models reached the correct answer *with and without* the pattern, so the lift is mostly structure and auditability, not a correctness rescue.

#### Input (WITHOUT pattern)
A support center forecasts 9,600 contacts next week (Mon–Fri 1,600/day, Sat–Sun 800/day), 7.5-minute average handle time. Staff to 120% of raw handle-time hours, then gross up because agents are productive only 80% of paid time. 8-hour shifts, 5 per week; each day splits into two equal shifts; no agent works both shifts in a day. Minimum agents for the week, and is a valid schedule achievable? Show the per-shift-per-day requirement.

#### Output
A correct answer via a plain top-to-bottom walkthrough: 1,200 handle-hours → ×1.2 = 1,440 → ÷0.8 = 1,800 paid hours; 19 agents per weekday shift, 10 per weekend shift; 230 shift-slots → **46 agents, feasible**. It gets there — but reasons in an undifferentiated numbered list and stumbles on the way: it first announces **45** agents from the hours total, then walks it back to 46 after the shift-rounding reconciliation. Format compliance scored **2/5** across all three models.

---

#### Input (WITH pattern)
Solve in two phases. Phase 1 — Decompose: list an ordered sequence of sub-problems, easiest to hardest, each naming which earlier result it consumes, *before solving anything*. Phase 2 — Solve in order, restating the carried-forward numbers at each step. End with the final answer.

Problem: [the same support-center staffing problem as above]

#### Output
**Phase 1** lists six ordered sub-problems first (weekly workload → ×1.2 service target → ÷0.8 gross-up → convert to 8-hour shifts → split to per-shift daily counts → feasibility check), each annotated with the prior result it consumes. **Phase 2** solves them in that order, restating the carried-forward figure at each step (1,200 → 1,440 → 1,800 → …). Same **46 agents, feasible**, but the dependency trail is explicit and auditable end to end.

> *Measured delta: WITH **12.5/15** vs WITHOUT **11.3/15** — **+1.2**, the most modest of the four promoted patterns. Caveat, stated plainly: every test model solved this task correctly with or without the pattern; the gain is format / auditability (format compliance 2/5 → 4/5), not accuracy. On strong 2026 models this problem did not *need* decomposition — reach for least-to-most on genuinely compositional failures, weaker/smaller models, or when an auditable dependency trail is itself the deliverable (see When to Use). Provenance: `evals/reports/least-to-most-prompting__2026-06-29-115540.md` (WITH) and `evals/reports/least-to-most-prompting-baseline__2026-07-01-223403.md` (WITHOUT).*

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

Example 1 — a real dependency chain (where ordering helps)
Input: "Decompose easiest-to-hardest, then solve in order, using prior answers as inputs. Problem: Given a list of meeting times, find the minimum number of conference rooms needed."
Output: The ordered decomposition mirrors the algorithm's true dependency: (1) sort the intervals by start time; (2) sweep through them, using a running set of end times to detect overlaps — this consumes the sorted order from step 1; (3) track the maximum number of simultaneously-active meetings, which consumes the sweep from step 2; that maximum is the answer. Solving out of order fails — you cannot sweep before you sort — so naming the dependency up front is what keeps a weaker model from jumping straight to a wrong count. This is the case least-to-most is genuinely for: an early sub-answer is a hard prerequisite for the next.

Example 2 — the caveat, honestly (a strong model barely needs it)
Input: "Least-to-most: order sub-problems by difficulty, solve in sequence. Problem: A user asks how to migrate their monolith to microservices. Produce a migration plan."
Output: The pattern imposes a sensible dependency order — (1) identify bounded contexts and seams; (2) pick the lowest-coupling context to extract first (consumes the seam map); (3) stand up the extraction infrastructure (API gateway, CI/CD, observability); (4) strangler-fig the first service out; (5) iterate, each extraction consuming the lessons of the last. But a capable 2026 model produces essentially this plan from a plain "give me a migration plan" prompt too — the phased structure is already in its training. Here least-to-most is a thinking *scaffold* that makes the ordering explicit and auditable, not a capability unlock, and the marginal gain on a strong model is small. This is the honest other half of the +1.2 measured delta.

> *Both examples are authored, faithful illustrations (not scored eval runs). Example 1 is a task where dependency ordering is load-bearing; Example 2 deliberately shows the pattern earning little on a strong model — the caveat the V2 baseline pass surfaced.*

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

*Measured caveat (V2 baseline pass, 2026-07-01): on strong 2026 models the improvement over a no-pattern baseline was modest — **+1.2/15**, the smallest of the promoted patterns. All three test models solved the benchmark task correctly with or without the pattern; the gain was mostly structure and auditability. Reach for least-to-most when a model is genuinely failing a compositional task single-shot, on weaker or smaller models, or when an auditable dependency trail is itself the deliverable — not as a default wrapper on capable models.*

---

### Version History
v0.1 – initial version
v1.0 – 2026-07-27 promoted lab → core (encyclopedia-pattern-promotion plan, [V5]). Full Lab→Core validation: score 12.5→13.1/15 (V3 4-judge firmed), measured baseline delta +1.2 (promote-with-caveat — modest, structure/auditability not accuracy; see Notes), ≥2 real-use examples, documented failure modes. Evidence: evals/PROMOTION-AUDIT.md.
