# Eval: cognitive-verifier-baseline

**Date:** 2026-07-01 22:22 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.3 (Mixed)** | 3 | 2 | 2 | 4 | 4 | 5 | 3 |
| claude-sonnet-4-6 | **3.3 (Mixed)** | 4 | 3 | 1 | 4 | 4 | 5 | 2 |
| gemini-2.5-flash | **3.1 (Mixed)** | 4 | 2 | 1 | 4 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> The model consistently provides accurate and well-toned advice against immediate Kubernetes adoption for a startup, effectively challenging the lead engineer's rationale and offering pragmatic alternatives. However, its performance is severely hampered by a complete disregard for the specified output format, which required explicit sub-questions, answers with stated assumptions, and a more integrated synthesis. This fundamental format failure also leads to a loss of completeness regarding specific decision-critical dimensions and the precise naming of the dominating factor, despite the overall quality of the general advice.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The runs are broadly on-task and mostly correct in advising against an immediate Kubernetes move, but they miss several decision-critical elements from the reference. None of the runs explicitly address the real driver behind the request as a possible hiring/resume/cargo-cult motive, and none name runway/opportunity-cost as the single dominating factor in the synthesis. Run 1 says "Kubernetes is usually a cost center" and Run 3 says it is "a distraction and a risk," which is directionally right, but the reference expects a more conditional boundary and a stronger distinction between real scaling need vs. speculative need. Evidence: Run 1: "Probably not right now." / "Kubernetes is usually a cost center"; Run 3: "Probably no, not right now." / "moving ... is usually a distraction and a risk." |
| Completeness | 2 | judge | The required cognitive-verifier elements are almost entirely absent. No 3-5 sharp sub-questions are posed as a first section. No paired answers with explicit stated assumptions appear. No single named decisive factor is identified. No clear flip condition is articulated. The expected dimensions (current scale/load vs. Heroku capacity, team K8s ops expertise, real driver behind the request, opportunity cost in engineer-weeks, intermediate managed alternatives) exist scattered in prose but are never assembled into the required diagnostic structure. The managed middle path is mentioned but not foregrounded. The weak 'serious companies' rationale is acknowledged but not candidly interrogated. |
| Format Compliance | 2 | judge | The responses mostly follow the broad shape of list + explanation + recommendation, but they do not comply exactly with the specified format. The reference requires three clearly delineated sections in order: (1) 3-5 sub-questions, (2) a brief answer to each sub-question with an explicit assumption where unknown, and (3) exactly one synthesized final recommendation. The model outputs instead use headings and prose, do not consistently present paired sub-answers with assumptions, and include extra framing such as multi-paragraph rationale and optional offers. Run 1 in particular has multiple sections but not the exact required section structure; Run 2 and 3 similarly add material outside the required three-section pattern. Evidence: Run 1 has "### The short answer" and "### Why I’d be cautious" rather than a strict 3-part structure; Run 2 has "## The key question" and "## What to tell your lead engineer"; Run 3 has "### A good default rule" and "### A better question to ask". |
| Consistency | 4 | judge | Across runs, the semantic answer is highly stable: all three recommend against moving to Kubernetes now, cite runway and operational overhead, and suggest staying on Heroku unless there is a concrete problem. Structural variation is modest, with all runs having a similar list-and-recommendation pattern, though they differ in headings and emphasis. There are no contradictions or major divergences. The low lexical-similarity ratio is consistent with paraphrase rather than inconsistency. Evidence: Run 1 "Probably not right now." Run 2 "For most early-stage startups, the answer is no." Run 3 "Probably no, not right now." [lexical similarity ratio: 0.05] |
| Tone/Style | 4 | judge | The tone is generally strong for a pragmatic senior advisor: direct, candid, and respectful. It avoids hype and mostly challenges the "serious companies use it" rationale appropriately. However, it is somewhat generic and occasionally softens into broad advice rather than the sharper staff-to-founder diagnostic style requested. The lead engineer’s rationale is quoted and rebutted in a respectful way, but the synthesis could be more decisively boundary-setting. Evidence: Run 2 says "Not 'Will we eventually need Kubernetes?' But: 'Does Kubernetes create enough near-term business value...'" and "Something like: Kubernetes may be a good option later..." which is decent but still somewhat templated. |
| Safety | 5 | judge | The content is benign, professional, and free of harmful, biased, or inappropriate material. It is standard technical decision advice with no safety issues. |
| Efficiency | 3 | judge | The answers are reasonably concise for the quality delivered, but they use somewhat more tokens than needed, especially given repeated restatements of the same conclusion across multiple sections and lists. The outputs spend many tokens on generic K8s drawbacks and duplicate the recommendation instead of tightly surfacing the decision boundary and flip conditions. Run lengths of 479-558 tokens are acceptable but not especially efficient for a 3-part pattern answer that could have been materially shorter and more targeted. Evidence: Run 1 repeats the conclusion in "Probably not right now," "If not, don’t do it yet," and "No, not now." Run 2 repeats across "The key question," "Useful rule," and "Practical recommendation." |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Completeness ⚠ | 2 | 3 | 2 | 2 | 1 | 0.47 |
| Format Compliance ⚠ | 2 | 3 | 1 | 1 | 2 | 0.94 |
| Consistency | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 3 | 2 | 3 | 1 | 0.47 |

- **Self-preference delta:** +3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 513 | Latency (avg): 4.36s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Strong, on-task advisory across runs, but it misses the required cognitive-verifier format and explicit assumption-bearing sub-questions, with some over-specific claims and verbose treatment relative to the prompt.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are on-task and mostly correct: they answer that migrating now is premature, ground it in runway/opportunity cost, and mention Heroku and Kubernetes tradeoffs. However, they sometimes overstate specifics not present in the prompt, such as concrete migration timelines and thresholds (e.g., Run 2: 'typically 3-6 months' and '18+ months of runway'; Run 1: '2-4 months of engineering time' and '25-50% of your remaining runway'). These are plausible but not fully supported by the prompt, so this is not a 5. |
| Completeness | 3 | judge | The responses capture the broad recommendation and some tradeoff discussion, but they do not satisfy the prompt's stricter structural/content requirements. They do not provide 3-5 sharp sub-questions with explicit assumptions for each, and they fail to cover all decision-critical dimensions in the reference with the required shape: current/near-term scale vs. Heroku capacity, team Kubernetes/ops expertise and on-call ownership, the true driver behind the request, opportunity cost versus the 8-month runway, and cheaper intermediate options. Some runs mention a subset of these, but not as the required enumerated cognitive-verifier structure. |
| Format Compliance | 1 | judge | The format specification requires three clearly delineated sections: (1) a numbered or bulleted list of 3-5 sub-questions, (2) a brief answer to each sub-question paired with an explicitly stated assumption, and (3) exactly one synthesized final recommendation naming the single most decisive factor and the flip condition. All three runs instead produce multi-section analysis essays with headers, tables, and bulleted lists of advice — none of which map to the required three-section structure. Sub-question count is zero across all runs (format requires 3-5). Explicit assumption statements are absent. The format specification is effectively ignored. |
| Consistency | 4 | judge | Across runs, the semantic conclusion is stable: do not move to Kubernetes now; focus on runway/product; revisit later if real scaling needs emerge. The structure varies more than ideal, but the core answer, tradeoff framing, and recommendation boundary are consistent. Since wording variation is expected and the core logic stays aligned, this is better than a 3, though not a 5 because coverage/structure varies notably and some runs are much more expansive than others. [lexical similarity ratio: 0.053] |
| Tone/Style | 4 | judge | The tone is largely strong and appropriate for a pragmatic senior-advisor voice: direct, candid, and respectful of the lead engineer. It challenges the rationale without being insulting. It is not perfect because some phrasing becomes slightly editorial or generic ('premature optimization dressed up as technical maturity') and occasionally drifts into motivational rhetoric, but overall it fits the audience well. |
| Safety | 5 | judge | The content is safe: no harmful instructions, no harassment, no disallowed content, and no privacy issues. The critique of the lead engineer remains professional and non-abusive. |
| Efficiency | 2 | judge | Run 1 uses 940 tokens, Run 2 uses 753, Run 3 uses 1391. Even Run 2, the most concise, contains padding (repeated tables, multi-header structure for points that could be integrated). Run 3 at 1391 tokens includes a flowchart, a checkbox list, a 'how to have this conversation' script, and a 'better use of energy' section that largely repeat earlier points. Crucially, the responses fail to deliver the required format — so the tokens are spent on the wrong output shape entirely. The cognitive-verifier format (5 sub-questions + answers with assumptions + one synthesis) would be tighter and more useful than any of these essays. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 3 | 2 | 2 | 4 | 2 | 0.94 |
| Format Compliance | 1 | 2 | 1 | 1 | 1 | 0.47 |
| Consistency | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 3 | 2 | 2 | 1 | 0.47 |

- **Self-preference delta:** -3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 1028 | Latency (avg): 25.35s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model is directionally correct and consistently says 'no now,' but it fails the pattern test on structure and specificity: no 3-5 explicit sub-questions, no assumption-tagged answers, no single integrated synthesis with a named decisive factor and flip condition. Strong on basic strategic advice, weak on rubric/format adherence.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are broadly on-task and mostly correct in recommending against immediate Kubernetes adoption, but they repeatedly overstate or speculate beyond the prompt. For example, Run 1 claims Heroku can handle "hundreds or thousands of dynos" and is "very unlikely" to hit limits in 8-24 months, and Run 3 asserts K8s migration could take "2-4 months or more"—these are plausible but not grounded in the prompt and are presented too confidently. The core decision guidance is right, but the answers are not fully fact-safe or tightly calibrated. |
| Completeness | 2 | judge | The responses address the main yes/no question, runway, and general complexity/opportunity-cost arguments, but they miss several required elements from the pattern spec. They do not provide 3-5 sharp sub-questions, do not pair each sub-answer with an explicit assumption, do not give exactly one integrated synthesis grounded in the sub-answers, and do not clearly state the flip condition with the required specificity. They also drift by adding generic future-proofing and alternative platforms without structuring them as decision-critical sub-questions. |
| Format Compliance | 1 | judge | The format is materially non-compliant with the requested pattern format. The rubric requires three clearly delineated sections in order: (1) 3-5 numbered/bulleted sub-questions, (2) a brief answer to each with an explicit assumption, and (3) exactly one synthesized final recommendation referencing the sub-answers and naming the decisive factor and flip condition. Instead, the runs use freeform advice with headings like "Why Not Now?" and "Conclusion," and none present the required question-answer structure. |
| Consistency | 4 | judge | The runs are semantically stable: all three recommend not moving to Kubernetes now, cite runway/opportunity cost, and note Heroku suffices for the current stage. Structural variation exists (different headings, different subpoints, differing amounts of detail), but the core answer and quality are consistent rather than contradictory. Given the low lexical similarity noted in the prompt, the semantic stability is strong. [lexical similarity ratio: 0.033] |
| Tone/Style | 4 | judge | The tone is generally pragmatic, direct, and audience-appropriate, with candid tradeoff language and a senior-advisor voice. However, it is somewhat overbearing and occasionally rhetorically loaded (e.g., "critical mistake," "at worst," "Formula 1 car") rather than the more measured staff-engineer-to-founder style requested. Still, the overall register is close to the target. |
| Safety | 5 | judge | The outputs are safe: no harmful instructions, hate, harassment, or disallowed content. The only potentially sensitive aspect is strongly opinionated strategic advice, which is benign in this context. |
| Efficiency | 2 | judge | The responses are verbose relative to the task and the expected pattern. The prompt under test calls for a compact, structured cognitive-verifier answer, but each run produces roughly 2.6k-3.0k tokens of repeated reasoning, examples, and restatement. That is a lot of token spend for a simple decision with a tightly specified format, so the efficiency is poor despite generally useful substance. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Completeness ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Format Compliance | 1 | 1 | 1 | 1 | 0 | 0.0 |
| Consistency ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 2 | 2 | 0 | 0.0 |

- **Self-preference delta:** +5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Tone/Style.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 2744 | Latency (avg): 14.73s | Runs: 3

---

## Prompt Under Test

```text
Question: We're a six-person startup, eight months from running out of runway, and our product currently runs on Heroku. Our lead engineer wants us to adopt Kubernetes because "we'll need it to scale and it's what serious companies use." Should we move to Kubernetes now?
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Probably not **right now**.

For a 6-person startup with 8 months of runway, Kubernetes is usually a **cost center, not a growth lever**, unless you have a very specific scaling or operational need it solves today.

### The short answer
Don’t adopt Kubernetes because:
- “serious companies use it”
- “we’ll need it eventually”
- “it scales better” in the abstract

Adopt it only if you have a **current, concrete problem** that Kubernetes is the best solution for.

### Why I’d be cautious
Kubernetes adds:
- significant setup and maintenance overhead
- more operational complexity
- more cognitive load for a small team
- more time spent on infrastructure instead of product

For a startup with limited runway, that can hurt:
- shipping speed
- hiring/boarding simplicity
- focus on customer value
- cash burn

### When Kubernetes *does* make sense
Consider it if you already have one or more of these:
- very high traffic or rapid scaling needs
- complex multi-service deployment patterns
- strong need for autoscaling, service discovery, or workload isolation
- compliance/security requirements that benefit from its controls
- a team with real Kubernetes experience and time to maintain it
- evidence Heroku is becoming a bottleneck, not just “less cool”

### Better default path
If you’re on Heroku and things are working, the better move is usually:
- stay on Heroku for now
- optimize app architecture and delivery
- measure actual pain points
- revisit infrastructure when you have a clear trigger

If Heroku cost or limitations are becoming real issues, you can also look at simpler alternatives before Kubernetes:
- managed container platforms
- a single VM or small set of VMs with Docker
- platform services like Render/Fly.io/Railway, depending on your needs

### A practical decision rule
Move to Kubernetes **only if** you can answer “yes” to most of these:
1. Do we have a current operational problem Kubernetes solves?
2. Is that problem more important than product velocity?
3. Can we afford the time to learn and run it?
4. Do we have someone who can own it?
5. Is Heroku actually blocking us, not just annoying us?

If not, don’t do it yet.

### Recommendation
**No, not now.**  
Keep Heroku unless you have a strong, evidence-based reason to move. In a startup this early, focus on building product and preserving runway, not on adopting infrastructure that makes you feel “legit.”

If you want, I can also help you create a **decision framework** for when to leave Heroku and what the lowest-risk migration path would be.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
