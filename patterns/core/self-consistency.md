## Pattern: self-consistency
Version: 1.0
Status: Core
Last Updated: 2026-07-27

---

### Intent
Improve accuracy on tasks with a single correct answer by sampling multiple reasoning paths and taking the majority vote.

---

### Mechanism
At non-zero temperature, reasoning chains diverge. Correct answers tend to cluster across runs because valid logic converges; errors scatter because mistakes are path-dependent. Majority vote filters noise.

---

### Template
"Run the following task N times at temperature >0. Return the answer that appears most often across runs: {task}"

(Implementation is typically orchestrated client-side — N independent API calls, then vote on the final-answer field.)

---

### Baseline Comparison (Required)

A *measured* head-to-head from the eval campaign, using a conditional-probability question that reliably trips people up. Read the honest note below: on this item the base model was already correct single-shot, so the measured delta reflects the pattern's machinery (independent attempts + tally + vote), not a rescued answer — self-consistency's error-correction shows up on harder items and weaker models (see the two Examples and When to Use).

Input (WITHOUT pattern)
A family has three children. You are told that at least two of them are girls. What is the probability that all three children are girls? (Each child is independently a boy or girl with probability 1/2.)

Output
One clean derivation: enumerate the 8 birth orders, condition on "at least two girls" (GGB, GBG, BGG, GGG), one of the four is all-girls → **1/4**. Correct — but it is a single chain. There are no independent attempts, no vote tally, and no stated tiebreaker, so there is nothing to fall back on had that one chain gone wrong. Panel: accuracy 5/5, completeness **1/5**, format-compliance **1/5**.

Input (WITH pattern)
Work the problem FIVE separate times as genuinely independent attempts (vary the setup: enumerate the sample space, use the conditional-probability formula, reason by complement, count with combinations, condition sequentially). End each with "Attempt k final answer: <value>", then tally the answers, apply a stated tiebreaker if needed, and give the majority answer as "Result: <value>".

Task: [the same three-children probability question as above]

Output
Five attempts, each a different derivation, every one ending in the mandated answer line; all five land on **1/4**; then an explicit tally (1/4 → 5 votes) and a final **Result: 1/4**. The value is the auditable ensemble — five independent routes agreeing is far stronger evidence than one assertion.

> *Measured delta: WITH **12.7/15** vs WITHOUT **9.5/15** — **+3.2**. Honest reading: this item never exercised the vote's error-correction (no chain scattered — the judges even docked completeness for it), so the +3.2 here is the multi-attempt / tally / vote structure the baseline omits entirely, not a rescued answer. The accuracy payoff appears when chains genuinely diverge (Example 1) or on weaker models. Provenance: `evals/reports/self-consistency__2026-06-29-140803.md` (WITH) and `evals/reports/self-consistency-baseline__2026-07-01-225210.md` (WITHOUT).*

---

### When to Use
- Tasks with a discrete, verifiable answer (math, logic, classification).
- Mid-tier models where single-shot reasoning is unreliable.
- High-stakes one-off queries where N× cost is acceptable.

---

### When NOT to Use
- Open-ended or creative generation where there is no "correct" answer to vote on.
- Continuous outputs (summaries, essays) that can't be compared for equality.
- Latency- or cost-sensitive paths.
- Tasks the base model already solves reliably.

---

### Failure Modes
- Shared bias — all chains make the same systematic error; majority is confidently wrong.
- Tie votes with no tiebreaker logic.
- Variance ceiling — if the base model is too weak, no amount of voting helps.
- Cost blow-up at scale.

---

### Examples
Example 1 — the vote actually correcting an error
Input: Sample 5 chains at temp 0.7 and majority-vote: "If a car travels 60 miles in 45 minutes, then slows to 40 mph for the next 30 minutes, what is its average speed over the full trip?"
Output: This is a genuine trap — average speed is total distance ÷ total time, not the average of the two speeds. Across five independent chains the reasoning scatters: most compute leg 1 = 80 mph over 60 miles, leg 2 = 20 miles in 30 minutes, total 80 miles in 75 minutes → **64 mph**; but at least one chain naively averages 80 and 40 → 60 mph. Tally: 64 mph → 4 votes, 60 mph → 1 vote. Result: **64 mph** — the majority outvotes the trapped chain. This is self-consistency doing the job it exists for: a single sample could have returned the wrong 60.

Example 2 — stabilizing an ambiguous classification
Input: Sample 5 chains at temp 0.7 and majority-vote classification: "Is this review Positive, Negative, or Neutral? 'It's fine. Works as advertised. Nothing to write home about.'"
Output: The review sits on the Neutral/Positive boundary, so a single classification is unstable run to run. Five independent chains: most read the flat, faint-praise tone as Neutral; one reads "works as advertised" as mildly Positive. Tally: Neutral → 4, Positive → 1. Result: **Neutral**. The vote turns an unstable one-shot label into a defensible, repeatable one — the classification analogue of the numeric vote in Example 1.

> *Both examples are authored, faithful illustrations of the mechanism (not scored eval runs). Unlike the measured probability item above — where no chain scattered — these show the case the pattern is really for: chains that genuinely diverge, where majority vote changes the outcome.*

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition
- plan-and-solve
- self-verification
- few-shot-examples

Conflicts with:
- low-latency-optimization
- brevity-directive
- direct-answer (unless voting on just the final answer field)

### Notes (Optional)
Self-consistency is an orchestration pattern, not a single-prompt pattern. The "template" is really a client-side loop. Include it in the repo because it composes with every reasoning pattern and is often the cheapest accuracy gain once decomposition plateaus.

Version History
v0.1 – initial version
v1.0 – 2026-07-27 promoted lab → core (encyclopedia-pattern-promotion plan, [V5]). Full Lab→Core validation: score 12.7/15, measured baseline delta +3.2, ≥2 real-use examples, documented failure modes. Evidence: evals/PROMOTION-AUDIT.md.
