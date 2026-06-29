# Eval: cognitive-verifier

**Date:** 2026-06-29 10:34 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.4 (Solid)** | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| claude-sonnet-4-6 | **4.9 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| gemini-2.5-flash | **4.1 (Solid)** | 4 | 4 | 5 | 4 | 4 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> Strong overall prompt-pattern adherence with minor misses on fully surfacing the weak ‘serious companies’ rationale and enumerating the intermediate managed-platform alternatives. Best fit is 4/5 on accuracy and completeness, 5/5 on format, safety, and consistency, and 4/5 on tone and efficiency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs are on-task and mostly align with the expected cognitive-verifier pattern: they ask 5 decision-critical sub-questions, give brief assumed answers, and recommend staying on Heroku rather than moving to Kubernetes now. However, they miss or underemphasize some expected decision-critical dimensions, especially the explicit weak rationale critique (“serious companies use it”) and the cheaper intermediate options list, and they sometimes soften the conditional boundary instead of making it tightly integrated around runway/opportunity cost. |
| Completeness | 4 | judge | The response set covers the required three-section structure and keeps sub-questions within the 3–5 limit, with all runs using 5 sub-questions. It also includes assumptions in the answer section and one synthesized recommendation. Missing or shallow elements prevent a 5: the sub-question set does not explicitly include the lead engineer’s rationale as a critique target, and only Run 1 gestures at intermediate options while none fully names the managed middle path (ECS/Fargate/Cloud Run/EKS/GKE) as requested by the reference. The synthesis also does not explicitly say “almost certainly NOT now” in the strongest conditional way for the most likely case, though the intent is clearly there. |
| Format Compliance | 5 | judge | The outputs follow the required shape very closely: three clearly delineated sections in order, 3–5 sub-questions, brief answers with assumptions, and exactly one final recommendation. No run violates the sub-question count, and the recommendation is singular rather than multiple competing conclusions. |
| Consistency | 5 | judge | The three runs are highly consistent in meaning, structure, and quality. All ask five sub-questions about runway/time, K8s expertise, scaling needs, current Heroku fit, and business priority; all answer toward the same conclusion; all name the dominant factor as runway/opportunity cost or immediate operational need. Wording varies substantially, but that variation is semantically stable and not contradictory. [lexical similarity ratio: 0.074] |
| Tone/Style | 4 | judge | The tone is generally strong for a staff-engineer-to-founder advisory voice: direct, decision-oriented, and respectful rather than hypey. It is candid about tradeoffs and repeatedly centers runway. It falls slightly short of a 5 because the critique of the lead engineer’s “serious companies” rationale is only lightly implied, not explicitly challenged in a crisp, founder-facing way, and some language is generic rather than incisive. |
| Safety | 5 | judge | The content is safe, professional, and free of harmful or inappropriate material. It gives technical advice without risky instructions and does not include bias, harassment, or disallowed content. |
| Efficiency | 4 | judge | The output is somewhat verbose for the task, especially given that the expected pattern values 3–5 sharp sub-questions and brief answers. That said, the extra detail is mostly relevant and improves clarity rather than padding aimlessly, so it is not wasteful enough to merit a lower score. The token counts are moderate-to-high (645, 795, 753) but deliver usable structure and decision guidance. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 4 | 5 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 731 | Latency (avg): 6.81s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs are exemplary executions of the cognitive-verifier pattern applied to a nuanced startup infrastructure decision. They surface five decision-critical sub-questions covering every dimension required by the reference (scale, K8s expertise, bottleneck authenticity, runway opportunity cost, intermediate alternatives), each paired with explicit assumptions. The synthesized recommendations are conditional, integrated, name opportunity cost as the single dominating factor, specify flip conditions, challenge the 'serious companies' rationale directly, and offer a managed middle path. Format compliance is exact across all runs. Tone is pitch-perfect for the staff-engineer-to-founder audience. Cross-run consistency is high despite natural paraphrase variation — the same recommendation, reasoning chain, and key insights appear in every run. The only imperfection is minor redundancy in Runs 2 and 3 that could have been trimmed without quality loss, warranting a slight efficiency deduction.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs are factually correct throughout. Claims about Heroku capacity (millions of requests/day), K8s migration cost (4–12 weeks), and the nature of managed alternatives are accurate. The identification of 'serious companies use it' as an identity/prestige argument rather than an engineering argument is analytically correct and on-task. No material factual errors found across any run. |
| Completeness | 5 | judge | All three runs cover every required dimension: (a) actual scale vs. Heroku ceiling, (b) K8s expertise and operational ownership, (c) real driver (cargo-cult vs. bottleneck), (d) runway/opportunity cost, (e) managed intermediate alternatives. Synthesis in each run is conditional, names a single dominating factor, specifies flip conditions, surfaces the 'serious companies' weakness, and offers a pragmatic middle path. No required element is missing or shallow. |
| Format Compliance | 5 | judge | All three runs deliver exactly three clearly delineated sections in order: numbered sub-questions (5 each, within the 3–5 range), sub-answers each paired with an explicit assumption statement, and exactly one synthesized final recommendation naming the single decisive factor and the flip condition. No format violations detected. |
| Consistency | 5 | judge | All three runs converge on the same recommendation (do not adopt K8s now), the same single decisive factor (opportunity cost relative to runway), the same flip conditions (concrete demonstrated scale problem + K8s expertise), the same alternative paths (Render/Railway/Fly.io/ECS), and the same analytical critique of 'serious companies use it.' Sub-question coverage overlaps highly across runs (scale, expertise, bottleneck authenticity, opportunity cost, alternatives/cost). Structural format is identical. Quality is uniformly high. Wording varies naturally as expected with paraphrase. [lexical similarity ratio: 0.079] |
| Tone/Style | 5 | judge | All three runs nail the requested staff-engineer-to-founder register: direct, candid, decision-oriented, no hedging into non-answers, respectful of the lead engineer while clearly challenging the weak rationale. Closing lines in each run are memorable and on-brand for the intended voice. |
| Safety | 5 | judge | The outputs are clean, non-abusive, non-discriminatory, and do not contain harmful instructions or unsafe content. The content is business/technical advisory only. |
| Efficiency | 4 | judge | Runs are appropriately sized for the complexity of the task (1088–1243 tokens). Run 1 is the tightest at 1088 tokens. Runs 2 and 3 have minor redundancy — the 8-month runway constraint is restated multiple times within each run, and some 'what to do instead' bullets partially repeat the sub-answer content. Tables in Runs 1 and 3 add genuine value. No heavy bloat, but a tighter edit could trim 10–15% without loss. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |

- **Self-preference delta:** +3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 1.14 (max 3).

Tokens (avg output): 1174 | Latency (avg): 29.39s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Across three runs, the model correctly applies the cognitive-verifier pattern: it generates four sub-questions (within the 3–5 limit), pairs each answer with an explicit assumption, and synthesizes a single conditional recommendation that names opportunity cost as the decisive factor and states a flip condition. Format compliance is fully met. The recommendation is correct and the tone is mostly appropriate for a senior technical advisor. The primary weaknesses are consistent across runs: the 'real driver' dimension—explicitly probing whether the lead engineer's rationale is cargo-culting or resume-padding—never becomes a dedicated sub-question; managed intermediate platforms (ECS/Fargate/Cloud Run) as an actionable middle path appear only in Run 3; and flip conditions are stated but not fully specified (none name the conjunction of demonstrated scaling pressure + dedicated ops capacity + extended runway). Run 1 is notably verbose in its synthesis without proportional quality gain. Structural and semantic consistency is strong, making this a solid but not exceptional execution of the pattern.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are on-task and mostly match the expected decision boundary: all three conclude not to move to Kubernetes now, cite runway/opportunity cost, and mention limited team expertise and lack of immediate scaling pressure. However, they introduce unsupported specifics as if known (e.g., Run 1 says there are "no critical, immediate scaling or performance issues" and Run 3 assumes 50-70% of lead-engineer time for 3-5 months), and they miss the prompt’s stronger requirement to explicitly frame the flip condition with the most likely baseline and the weak "serious companies use it" rationale more directly.","evidence":"Run 1: 'There are no critical, immediate scaling or performance issues with Heroku...' and 'You should not move to Kubernetes now.' Run 3: 'I will assume...' 'at least 50-70% of your lead engineer's time for 3-5 months' and 'Do NOT move to Kubernetes now.'"},"completeness":{"score":4,"justification":"The response set covers the main requested dimensions and includes 3-4 sub-questions plus a synthesis in each run, with assumptions stated. But it is not fully complete against the reference: the sub-questions miss or underemphasize the explicit 'real driver behind the request' (hiring/resume/cargo-cult 'serious companies') and the intermediate managed middle path is only lightly touched in some runs. Also, Run 1 includes only four sub-questions, which is acceptable, but the set as a whole does not consistently hit all decision-critical dimensions the rubric highlights.","evidence":"Run 2 asks about scaling limits, team expertise, product priorities, and cost analysis; Run 3 asks about market adoption, expertise, Heroku limitations, and alternatives. None explicitly asks 'what is the real driver behind the request' as a sub-question, though Run 3 does quote 'serious companies use Kubernetes' in the final paragraph."},"format_compliance":{"score":4,"justification":"Structurally, each run follows the required three-part pattern: sub-questions, brief answers with assumptions, and one synthesized recommendation. The main deviation is that the model did not produce the exact required JSON-only output; instead it wrapped the evaluation text in prose and then the JSON schema requirement was imposed by the user instruction here. Within the response content itself, the format is close but not exact because headings vary and there is extra framing text like 'Here's the procedure followed.'","evidence":"Run 1 uses '### Sub-Questions', '### Answers to Sub-Questions', and '### Final Recommendation'; Run 2 uses '### 1. Additional Sub-Questions', '### 2. Sub-Question Answers & Assumptions', '### 3. Synthesized Recommendation'; Run 3 uses similar three-section organization, but none are exact JSON-only. "},"tone_style":{"score":4,"justification":"The tone is pragmatic, direct, and aimed at a technical founder audience. It challenges the K8s instinct without hype and emphasizes tradeoffs. Still, it is somewhat generic and occasionally overconfident in assumptions, and it does not always directly and respectfully interrogate the 'serious companies use it' rationale as clearly as the reference expects.","evidence":"Run 2: 'Do NOT move to Kubernetes now.' Run 3: 'your lead engineer is correct that "serious companies use Kubernetes" and it can be essential for extreme scale, your sub-answers collectively indicate...'"},"safety":{"score":5,"justification":"The outputs are benign, business/technical advice only, with no harmful, biased, or inappropriate content.","evidence":"All runs discuss infrastructure choice, runway, and tradeoffs; no unsafe instructions or harmful content appear."},"efficiency":{"score":2,"justification":"The outputs are verbose relative to the task. The user wanted a concise cognitive-verifier pattern with 3-5 sharp sub-questions and brief answers, but each run spends substantial token budget on repetitive caveats, speculative assumptions, and long final recommendations. Run 1 at 3179 tokens and Run 3 at 2686 tokens are especially bloated for a simple advisory answer.","evidence":"Run 1: '3179 output tokens' with long paragraphs under each answer and recommendation; Run 3: '2686 output tokens' with extended assumptions like '50-70% of your lead engineer's time for 3-5 months.'"},"consistency":{"score":4,"justification":"Across runs, the semantic core is stable: 3-4 sub-questions, assumptions, and a 'do not move now' recommendation grounded in runway/opportunity cost. Differences are mostly in wording and emphasis, not contradiction. There are some structural and coverage variations—Run 1 asks about monthly Heroku spend, Run 2 about detailed cost analysis, Run 3 about product-market fit and alternatives—but these remain within the same decision frame rather than diverging meaningfully.","evidence":"Run 1 final: 'You should not move to Kubernetes now.' Run 2 final: 'Do NOT move to Kubernetes now.' Run 3 final: 'Do NOT move to Kubernetes now.' All cite opportunity cost/runway as decisive, with varying sub-question sets."},"summary":"Overall strong on the decision direction and format skeleton, but not a 5 because the prompts are somewhat bloated, slightly over-assumptive, and do not fully and explicitly surface the lead engineer's weak justification or the exact flip condition with the crispness the reference calls for."}]}ুলো.**】}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**】]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}]}**}}}}}】{ |
| Completeness | 4 | judge | The response set covers the main requested dimensions and includes 3-4 sub-questions plus a synthesis in each run, with assumptions stated. But it is not fully complete against the reference: the sub-questions miss or underemphasize the explicit 'real driver behind the request' (hiring/resume/cargo-cult 'serious companies') and the intermediate managed middle path is only lightly touched in some runs. Also, Run 1 includes only four sub-questions, which is acceptable, but the set as a whole does not consistently hit all decision-critical dimensions the rubric highlights. |
| Format Compliance | 5 | judge | All three runs produce exactly three clearly delineated sections in the correct order: (1) numbered/bulleted sub-questions, (2) answers paired with explicit assumptions, (3) one synthesized final recommendation. All runs maintain exactly 4 sub-questions, within the 3–5 range. All sub-answers explicitly state assumptions. No run produces a second final recommendation or omits a section. |
| Consistency | 4 | judge | Across runs, the semantic core is stable: 3-4 sub-questions, assumptions, and a 'do not move now' recommendation grounded in runway/opportunity cost. Differences are mostly in wording and emphasis, not contradiction. There are some structural and coverage variations—Run 1 asks about monthly Heroku spend, Run 2 about detailed cost analysis, Run 3 about product-market fit and alternatives—but these remain within the same decision frame rather than diverging meaningfully. [lexical similarity ratio: 0.078] |
| Tone/Style | 4 | judge | The tone is pragmatic, direct, and aimed at a technical founder audience. It challenges the K8s instinct without hype and emphasizes tradeoffs. Still, it is somewhat generic and occasionally overconfident in assumptions, and it does not always directly and respectfully interrogate the 'serious companies use it' rationale as clearly as the reference expects. |
| Safety | 5 | judge | The outputs are benign, business/technical advice only, with no harmful, biased, or inappropriate content. |
| Efficiency | 3 | judge | Run 1 at 3179 tokens is noticeably bloated: the synthesis section contains multiple advisory paragraphs well beyond what the format requires (one recommendation + decisive factor + flip condition). Runs 2 (2548) and 3 (2686) are leaner and more appropriate for the complexity of the task. Typical behavior across the three runs averages ~2804 tokens. Given that completeness only scores 3 (missing key dimensions), the token expenditure is disproportionate to quality delivered. Run 1's verbosity does not add proportional value. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 4 | 4 | 4.5 | 0.5 | 0.24 |
| Completeness ⚠ | 4 | 4 | 3 | 4.5 | 1.5 | 0.62 |
| Format Compliance ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3.5 | 1.5 | 0.62 |

- **Self-preference delta:** +5.0 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.93 (max 1.5).

Tokens (avg output): 2804 | Latency (avg): 15.17s | Runs: 3

---

## Prompt Under Test

```text
When I ask a question, follow this exact procedure before answering:

1. Generate 3 to 5 additional sub-questions that, if I answered them, would let you give a substantially more complete and accurate response. Each sub-question must target a different decision-critical dimension that I left unspecified — not a restatement of what I already gave you.
2. Answer each sub-question briefly using your best reasoning about the most likely situation, and state the assumption you are making where the true answer is unknown.
3. Synthesize ONE final recommendation that explicitly integrates the sub-answers — your recommendation must change depending on how the key sub-questions resolve, and you must name the single factor that most determines the call.

Question: We're a six-person startup, eight months from running out of runway, and our product currently runs on Heroku. Our lead engineer wants us to adopt Kubernetes because "we'll need it to scale and it's what serious companies use." Should we move to Kubernetes now?
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
1. **Sub-questions that materially change the answer**
   1. **What is your immediate bottleneck: engineering velocity, reliability, cloud cost, or expected traffic growth?**  
   2. **Do you have someone on the team who has operated Kubernetes in production before, or would this be a first-time adoption?**  
   3. **How complex is your current app architecture: one or two services, or many services/background jobs/queues/custom infra needs?**  
   4. **How much runway pressure do you have relative to the migration effort, and would a 2–4 month platform project threaten core product work?**  
   5. **Are there concrete scaling/reliability needs in the next 6–12 months that Heroku cannot reasonably handle?**

2. **Best-guess answers with assumptions**
   1. **Immediate bottleneck:** Most likely **engineering velocity and runway**, not raw scale.  
      **Assumption:** You’re a typical early-stage startup where traffic is not yet at “Heroku is the problem” levels.
   2. **Kubernetes experience:** Likely **no deep in-house Kubernetes operator**.  
      **Assumption:** The team is product-focused, and K8s would be a new operational burden.
   3. **App complexity:** Probably **modest**, with a small number of services.  
      **Assumption:** If you were already running a large service mesh, many microservices, and bespoke infra, you wouldn’t be asking this in such a general way.
   4. **Runway pressure vs migration effort:** A Kubernetes migration would likely consume **too much attention for a six-person team with eight months of runway**.  
      **Assumption:** The migration is not a weekend project; it would introduce real platform and debugging overhead.
   5. **Concrete need:** There is probably **no near-term must-have requirement** that only Kubernetes can satisfy.  
      **Assumption:** If you had strict compliance, multi-region orchestration, or heavy workload isolation needs, that would already be front and center.

3. **Final recommendation**
   **Do not move to Kubernetes now.**  
   With the most likely answers above, Kubernetes is a **distraction risk** rather than a growth unlock. The **single factor that most determines the call is runway pressure relative to expected operational benefit**: if the migration won’t clearly pay back *before* you run out of runway, it’s the wrong move.

   **What to do instead:**  
   - Keep Heroku for now.  
   - Optimize for shipping, customer learning, and raising/expanding runway.  
   - Only revisit Kubernetes if you hit a clear pain point that Heroku can’t solve: sustained cost issues, deployment constraints, reliability limits, or architecture that truly needs orchestration.

   **When the answer would change:**  
   - **Move sooner** if you already have K8s expertise in-house and are blocked by Heroku limitations today.  
   - **Stay put** if your main challenge is building the product and conserving founder time.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
