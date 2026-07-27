## Pattern: plan-and-solve
Version: 1.0
Status: Core
Last Updated: 2026-07-27

---

### Intent
Separate planning from execution so framing errors surface before they poison the solution.

---

### Mechanism
Forces the model to commit to an approach in writing before applying it. A bad plan is easier to catch (by the model or a reviewer) than a bad answer that was never framed as a plan. Reduces mid-task drift.

---

### Template
"First, devise a plan — list the steps you will take to solve this without solving it yet. Then carry out the plan step by step. Finally, state the answer.

Task: {task}"

---

### Baseline Comparison (Required)

A *measured* head-to-head from the eval campaign. The task is a constrained scheduling problem with a single correct answer (the earliest ship time), which makes the plan-vs-no-plan difference easy to score.

Input (WITHOUT pattern)
A hotfix must ship in one day across three sequential sub-teams, each working only local 09:00–18:00: Bangalore (UTC+5:30) BUILD 2h → Berlin (UTC+2) INTEGRATE 1h → New York (UTC−4) VALIDATE-AND-SHIP 2h, with a 15-minute synchronous handoff at each boundary. Produce a minute-by-minute UTC schedule that ships as early as possible; say what is forced or impossible.

Output
Freeform prose — it converts the windows, then schedules forward under ad-hoc headings (*Key windows / Earliest schedule / Minute-by-minute summary*). With no separation of plan from execution, the missing frame lets a real error through: one run schedules the Berlin→New-York handoff at **06:45–07:00 UTC**, hours before New York is online, and ships at the wrong **15:00 UTC**. Format compliance scored **1/5 across all three models**; the weakest model's accuracy scored **1/5**.

Input (WITH pattern)
First, devise a plan — list the steps you will take to solve this without solving it yet. Then carry out the plan step by step. Finally, state the answer.

Task: [the same three-timezone hotfix scheduling problem as above]

Output
A **Plan** section first — six steps stated *without* solving (convert windows → note stage durations and the 15-minute overlaps → walk forward respecting local hours and sequential dependency → check for forced gaps → build the schedule → state the ship time). Then an **Execution** section that carries out each step and catches the very handoff-timing trap the baseline shipped — it explicitly rules the pre-07:00 handoff *not usable* — and an **Answer**: the correct **15:15 UTC**, with the forced idle window (07:00→13:00, waiting on New York) named as unavoidable.

> *Measured delta: WITH **12.3/15** vs WITHOUT **9.1/15** — **+3.2**. Committing to an approach in writing before executing restores an auditable structure (format compliance 1/5 → 4–5/5) and catches framing errors the freeform answer ships. Provenance: `evals/reports/plan-and-solve__2026-06-29-130415.md` (WITH) and `evals/reports/plan-and-solve-baseline__2026-07-01-224628.md` (WITHOUT).*

---

### When to Use
- Multi-stage tasks where the right approach matters more than the right computation.
- Problems with non-obvious structure (ambiguous word problems, design tasks).
- Situations where premature commitment to a solution is a known risk.
- As a frame on top of cognitive-decomposition when decomposition alone doesn't catch framing errors.

---

### When NOT to Use
- Trivial tasks where planning doubles the output for no gain.
- Tasks where the "plan" is indistinguishable from the solution (e.g., "define X").
- Latency-critical calls.
- Tasks already well-served by a schema or direct lookup.

---

### Failure Modes
- Plan/execution divergence — model writes a plan, then solves a different problem.
- Plan too abstract to constrain execution ("Step 1: understand the problem").
- Over-planning — plan occupies most of the output and execution is rushed.
- Model treats "state the plan" as permission to skip real thinking during execution.

---

### Examples
Example 1 — constraint scheduling
Input: "First devise a plan, then execute it. Task: Given four attendees' availability windows across three time zones, propose a 60-minute meeting slot (or show none exists)."
Output: Plan (stated first, no solving): (1) convert every window to a common zone (UTC); (2) intersect the four windows; (3) inside the intersection, find a 60-minute slot honoring any hard "no earlier than" constraints; (4) if the intersection is shorter than 60 minutes, report the closest option and who must flex. Execution follows the plan in order and lands a concrete answer — e.g. *"14:00–15:00 UTC works for all four,"* or *"no common 60-minute window exists; the tightest option asks Tokyo to join 30 minutes after hours."* The plan step is what forces the "or show none exists" branch to actually be checked instead of a slot being asserted.

Example 2 — debugging (framing before fixing)
Input: "First devise a plan, then execute it. Task: A Python script is producing the wrong total. Here's the code and expected vs. actual output. Diagnose and fix."
Output: Rather than editing the first suspicious line, the model commits to a diagnosis plan: (1) restate expected vs. actual and the size of the gap; (2) locate where the total is accumulated; (3) enumerate candidate causes (accumulator re-initialized inside the loop, an off-by-one bound, a filter dropping rows, float-versus-integer rounding); (4) trace one hypothesis against the given data; (5) apply the fix and predict the corrected output. Execution then finds, say, that `total = 0` sits *inside* the loop so only the last row is summed — moves the initializer out, and predicts the total now matches. The plan prevents the common failure mode of a "fix" that changes the output without explaining the gap.

> *Both examples are authored, faithful illustrations (not scored eval runs). They render the behavior the eval measured on the scheduling task: a plan stated before any solving, execution mapped onto that plan, and framing errors caught before they reach the answer.*

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition (plan-and-solve is the higher-level frame; decomposition is the execution step)
- self-verification (verify the plan, then verify the execution)
- self-consistency
- role-persona ("You are a careful planner")

Conflicts with:
- direct-answer
- brevity-directive
- low-latency-optimization
- creative-flow

### Notes (Optional)
The plan step is most valuable when it names the assumptions and constraints explicitly. A plan that just restates the task steps in abstract terms adds tokens without adding signal. For repeat task types, consider converting a good plan into a few-shot example instead — it's cheaper.

Version History
v0.1 – initial version
v1.0 – 2026-07-27 promoted lab → core (encyclopedia-pattern-promotion plan, [V5]). Full Lab→Core validation: score 12.3→13.0/15 (V3 4-judge firmed), measured baseline delta +3.2, ≥2 real-use examples, documented failure modes. Evidence: evals/PROMOTION-AUDIT.md.
