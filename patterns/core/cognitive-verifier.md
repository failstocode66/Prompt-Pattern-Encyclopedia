## Pattern: cognitive-verifier

Version: 1.0
Status: Core
Last Updated: 2026-07

---

### Intent
Generate clarifying sub-questions, answer each, then synthesize — improving responses to under-specified questions.

---

### Mechanism
Models silently pattern-match to the obvious reading of a question. Forcing explicit sub-questions surfaces hidden dimensions and missing inputs; each sub-answer then becomes context for the synthesis step.

---

### Template
"When I ask a question, follow this procedure before answering:
1. Generate 3-5 additional sub-questions that, if answered, would let you give a more complete and accurate response.
2. Answer each sub-question briefly using your best reasoning.
3. Synthesize a final answer that integrates the sub-answers.

Question: {question}"

---

### Baseline Comparison (Required)

This is a *measured* head-to-head from the eval campaign, not a hand-picked demo. The task is a real "should we?" architecture decision, and the WITHOUT arm is the same question posed to the same models with no pattern scaffolding.

#### Input (WITHOUT pattern)
We're a six-person startup, eight months from running out of runway, and our product runs on Heroku. Our lead engineer wants us to adopt Kubernetes because "we'll need it to scale and it's what serious companies use." Should we move to Kubernetes now?

#### Output
A single flowing advice essay. It reaches a defensible conclusion — *"No, not right now"* — under headings like *The short answer / Why I'd be cautious / When Kubernetes does make sense / A practical decision rule*. But the decision-critical unknowns stay buried in prose: the model never states which assumption it is making (remaining runway, current scale, in-house K8s experience), and it never names the one factor that should decide the call. The reader is left to do the integration.

> *Panel: format-compliance 1–2/5, completeness 2/5 — the generic-essay shape is exactly what the pattern is designed to prevent.*

---

#### Input (WITH pattern)
When I ask a question, follow this exact procedure before answering: (1) generate 3–5 sub-questions, each targeting a different decision-critical dimension I left unspecified; (2) answer each briefly, stating the assumption you are making where the true answer is unknown; (3) synthesize ONE final recommendation that integrates the sub-answers and names the single factor that most determines the call.

Question: [the same Heroku-vs-Kubernetes question as above]

#### Output
**1 — Sub-questions:** five distinct unknowns — immediate bottleneck (velocity, reliability, cost, or traffic)? in-house Kubernetes operating experience? current architecture complexity? migration effort versus remaining runway? any concrete 6–12-month need Heroku cannot meet? **2 — Answers with assumptions:** each answered against the most-likely case with the assumption made explicit ("Assumption: traffic is not yet at 'Heroku is the problem' levels"). **3 — Synthesis:** *"Do not move to Kubernetes now,"* naming the single decisive factor (runway pressure relative to operational payoff) and the flip condition (move only with in-house K8s expertise **and** a demonstrated Heroku ceiling).

> *Measured delta: WITH **13.4/15** vs WITHOUT **9.7/15** — **+3.7**, the largest of the four promoted patterns (3 target models × 3-judge panel). Same underlying judgment, but the pattern forces a structure that surfaces its own assumptions and commits to a decisive factor. Provenance: `evals/reports/cognitive-verifier__2026-06-29-103412.md` (WITH) and `evals/reports/cognitive-verifier-baseline__2026-07-01-222228.md` (WITHOUT).*

---

### When to Use
- Open-ended advisory questions where the right answer depends on unstated context
- Architecture, design, or "should I" decisions
- Research questions that span multiple dimensions (cost, performance, maintainability, team skill)
- Tasks where the user is likely to under-specify but expects a tailored answer

---

### When NOT to Use
- Fully specified factual queries (sub-questions add latency without benefit)
- Tasks with hard latency or token budgets
- Creative tasks where divergent thinking is the point, not convergent specification
- When the user has already supplied complete context — sub-questions become redundant or condescending

---

### Failure Modes
- Sub-question inflation — model generates many shallow sub-questions instead of a few sharp ones
- Self-confirmation — the model answers its own sub-questions in ways that conveniently support a predetermined conclusion
- Lost synthesis — sub-answers are listed but never integrated into a coherent final answer
- Sub-question drift — sub-questions wander away from the user's actual intent and the answer follows them

---

### Examples

Example 1 — under-specified technical decision
Input: "Use the cognitive verifier procedure (sub-questions → sub-answers → synthesis). Question: What's the best way to deploy my Next.js app?"
Output: Instead of defaulting to "use Vercel," the model first surfaces the unknowns that actually change the answer — (1) does the app use SSR / API routes / ISR, or is it a static export? (2) expected traffic and burst profile? (3) does the team already run its own cloud infra? (4) budget and cost sensitivity? (5) any edge / regional-latency requirement? — then answers each against the most-likely case with its assumption stated. The synthesis names the deciding factor: *the rendering model plus the team's ops appetite.* SSR/ISR app on a small team → a managed platform (Vercel / Netlify); static export → object storage behind a CDN at a fraction of the cost; a flip condition is given for each. The tailored recommendation exists only because the sub-questions forced the context out first.

Example 2 — open-ended career decision
Input: "Use the cognitive verifier pattern. Question: Is it worth getting a graduate degree in computer science right now?"
Output: A raw model answers the *average* case ("it depends, but generally…"). With the pattern it first asks what the answer hinges on: (1) the goal — research / academia, a compensation bump, a career switch, or an immigration credential? (2) years of industry experience and portfolio strength? (3) opportunity cost of 1–2 years out of the workforce plus tuition? (4) does the target role actually price the credential? (5) funded or self-paid? Each is answered with an explicit assumption. The synthesis names the decisive factor — *whether the target path rewards the credential* — and gives a conditional answer: an already-employed engineer chasing an IC role → usually negative ROI; a career-switcher or someone targeting research / ML-scientist roles → the calculus flips positive. The recommendation changes with the sub-answers, which is the entire point.

> *Both examples are authored, faithful illustrations (not scored eval runs), but they mirror the behavior the eval measured on the Heroku/Kubernetes item: 3–5 assumption-tagged sub-questions and one synthesis that names a single decisive factor and a flip condition.*

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-decomposition (sub-questions can each become decomposed tasks)
- self-verification (verify the final synthesis against the sub-answers)
- role-persona (a senior-advisor persona reinforces the questioning discipline)
- few-shot-examples (demonstrate the right granularity of sub-question)

Conflicts with:
- brevity-directive (sub-questions inherently expand output)
- direct-answer (the pattern's whole point is structured detour before answering)
- low-latency-optimization (multi-step procedure increases tokens and latency)

---

### Notes (Optional)
Originates from the prompt patterns catalog (White et al., Vanderbilt 2023). The sub-question count is load-bearing: too few defeats the purpose, too many produces dilution. 3-5 is a reasonable default. Always pair with an explicit synthesis instruction — without it, models commonly list sub-answers without integrating them, leaving the user to do the work.

---

### Version History
v0.1 – initial version
v1.0 – 2026-07-27 promoted lab → core (encyclopedia-pattern-promotion plan, [V5]). Full Lab→Core validation: score 13.4/15, measured baseline delta +3.7 (the largest of the tranche), ≥2 real-use examples, documented failure modes. Evidence: evals/PROMOTION-AUDIT.md.
