# Eval: context-compression

**Date:** 2026-06-29 10:57 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.1 (Mixed)** | 3 | 2 | 2 | 2 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4.3 (Solid)** | 4 | 5 | 4 | 4 | 4 | 5 | 4 |
| gemini-2.5-flash | **3.4 (Mixed)** | 3 | 4 | 3 | 3 | 3 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> The model reliably produces a well-structured five-section summary with appropriate tone and bullet formatting. However, two of three runs fail to execute the core deliverable—the one-page migration brief—despite describing it in the Active task section. Run 3 is the outlier that completes both parts and does so with good accuracy (correct dedupe key including sequence number, at-least-once semantics, semantic-vs-byte-for-byte comparison, open items flagged). Runs 1 and 2 each carry a classification error: run 2 commits the confidence-inflation trap by listing the transactional outbox as a settled decision; run 1 places it under Established facts. No run mentions the ~2,000 orders/hour volume rationale or the 'no DB split' negative decision explicitly. Overall, the pattern shows high variance in output completeness and moderate accuracy reliability—strong on style and safety, weak on structural consistency and task completion.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Mostly on-task and broadly faithful, but it introduces a few unsupported or softened claims and one notable overreach: in Run 3 the brief says "The intended transport direction is event-based rather than sync calls back into the monolith" and later "Kafka is parked for now, the likely default is the transactional outbox on Postgres with a relay, but that is not fully locked," which blurs the reference’s stronger distinction between a parked option and a not-yet-committed decision. It also states "Generate tracking numbers and emit the Shipping-side result inside the new service boundary," which is not explicitly established in the source summary. |
| Completeness | 2 | judge | Two of three runs (1 and 2) produce only the structured summary and entirely omit Part 2—the migration brief, which is the primary deliverable requested in the next-task prompt. The Active task sections in those runs describe the brief that should be written but never produce it. Run 3 alone delivers both parts and covers the key specifics (dedupe key, semantic comparison, per-consumer obligations, open items). Even run 3 omits the ~2,000 orders/hour volume rationale in the brief and does not state the 'no DB split' negative decision explicitly. Typical behavior across runs therefore misses the second required output entirely. |
| Format Compliance | 2 | judge | The five required headings appear in the correct order in all three runs, and bullet lists are used throughout—so the Part 1 shape is broadly right. However, all runs use markdown-level headers (## or ###) rather than the plain-text heading style implied by the spec, and the Active task section is multi-line in runs 1 and 2 when the spec says 'may be one line.' Most importantly, runs 1 and 2 are missing Part 2 entirely, a fundamental format failure for a two-part output spec. Run 3 delivers both parts; the brief uses internal section headers plus bullets, which is close to but not purely the 'terse, bulleted' format specified. |
| Consistency | 2 | judge | There is a fundamental structural divergence: runs 1 and 2 produce only Part 1, while run 3 produces both parts. Beyond structure, there is a meaningful classification disagreement: run 2 places the outbox transport under Decisions made (confidence-inflation trap) while run 3 correctly places it in Open questions—this is a content-quality difference, not mere wording variation. All three runs agree on placing Payments-vs-Inventory in Open questions, on the five-section ordering, and on the core decided items (strangler-fig, Shipping first, idempotent consumers, contract test ownership). The lexical ratio of 0.18 is expected given paraphrase, but the structural and classification divergence is real. [lexical similarity ratio: 0.18] |
| Tone/Style | 5 | judge | Matches the requested terse, concrete, skimmable engineering register very well. The bullets are concise, uncertainty is explicitly marked, and there is no conversational padding. Across runs, the tone stays appropriate for busy squad leads. |
| Safety | 5 | judge | No harmful, biased, or inappropriate content. The content is standard engineering planning material. |
| Efficiency | 3 | judge | Runs 1 (547 tokens) and 2 (575 tokens) spend roughly the same token budget as Run 3 on a summary alone, yet deliver only half the required output. Run 3 (1197 tokens) delivers both the summary and a full brief with no apparent padding—the extra tokens are well-spent on seven concise, substantive brief sections. The typical-run picture is therefore inefficient: two-thirds of executions consume mid-range token counts to produce an incomplete output, while the one run that completes the task does so efficiently for the quality returned. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Completeness ⚠ | 2 | 4 | 2 | 1 | 3 | 1.25 |
| Format Compliance ⚠ | 2 | 4 | 2 | 1 | 3 | 1.25 |
| Consistency ⚠ | 2 | 4 | 2 | 1 | 3 | 1.25 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 4 | 3 | 2 | 2 | 0.82 |

- **Self-preference delta:** +9.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.71 (max 3).

Tokens (avg output): 773 | Latency (avg): 5.94s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs are strong performers on a demanding context-compression task. The most critical nuances—Kafka correctly parked (not decided), at-least-once delivery with idempotency, dedupe on order ID plus event sequence number, semantic comparison on carrier and service level, no schema registry negative decision, and explicit open-item flagging—are correctly preserved across all runs. The structured summary sections are in the right order and correctly populated. Run 1 is the strongest individual output, including the 2,000 orders/hour volume justification in the brief and a squad action table. Runs 2 and 3 omit the volume figure from the brief (a specific expected-output requirement), and Run 2 confusingly places the transport question under 'Decided' while simultaneously noting it is pending. Tone and format are largely on-spec, with Run 2 introducing a brief prose paragraph where bullets were required. Consistency across runs is high—no contradictions, only minor coverage and structural variation.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are broadly on-task and mostly faithful to the transcript, but there are a few accuracy slips. The biggest is in Run 2’s brief, which says the transport is pending and omits the transcript’s specific “Kafka parked, not rejected” framing from the summary section, and Run 1 adds "OrderAddressChanged" to the published events even though the transcript only states the monolith will publish OrderConfirmed explicitly. The rest is solid and preserves the important constraints like no schema registry, no DB split, idempotency, per-order ordering, and semantic comparison. |
| Completeness | 5 | judge | All required elements are covered across the runs: the five-section structured summary, the status split between decisions and open questions, the second task as a one-page migration brief, and the consumer obligations. The briefs also explicitly include the load-bearing details the rubric asked for: dedupe key, per-order ordering, semantic comparison, old code retained one cycle, and ~2,000 orders/hour. |
| Format Compliance | 4 | judge | All three runs produce two clearly delineated parts. Part 1 contains exactly the five required headings in order—'Established facts:', 'Open questions:', 'Decisions made:', 'Active task:', 'Style/tone preferences observed:'—each followed by a markdown bulleted list. Active task is a single line in every run. Part 2 is a clearly labeled migration brief using bullets and tables throughout. Run 2 uses '## Session Summary' instead of '## Structured Summary' as the top-level label, but this does not affect the required content structure. |
| Consistency | 4 | judge | The runs are semantically stable: all preserve the same core decisions, open questions, and shipping brief structure. Wording and surface structure vary, but that is acceptable paraphrase. There are some differences in emphasis and one notable structural difference in Run 2, yet none of the runs materially contradict each other on the substantive points. [lexical similarity ratio: 0.166] |
| Tone/Style | 4 | judge | The tone is generally appropriate for busy engineering leads: terse, concrete, and skimmable with bullets. It explicitly marks open items and avoids fluffy prose. Minor style drift appears in Run 1 and Run 2 with extra explanatory framing and tables, but the overall register is strong and aligned with the requested audience. |
| Safety | 5 | judge | The content is benign, technical, and free of harmful or inappropriate material. No safety concerns are present. |
| Efficiency | 4 | judge | Token counts are 1265, 1081, and 1097 for a task requiring both a structured multi-section summary and a substantive one-page brief. Run 1 uses the most tokens and delivers the most content (squad action table, more detailed transport rationale), justifying its length. Runs 2 and 3 are tighter and comparable in density. There is minor padding in Run 1's table headers and some repetition between the summary and brief sections, but no egregious bloat across any run. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 4 | 2 | 5 | 5 | 3 | 1.41 |
| Consistency | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 4 | 5 | 2 | 0.82 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance, Efficiency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 1148 | Latency (avg): 22.19s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model's responses generally follow the requested structure and capture most of the complex technical details. However, there are consistent issues that prevent a high score. All runs fail on the format/tone requirement of 'no preamble' for the migration brief. Accuracy suffers from a subtle 'confidence-inflation trap' regarding the outbox decision (presenting it as a 'preferred/tentative decision' within the 'Decisions made' section, rather than strictly 'parked'), with Run 2 exhibiting a direct contradiction on this point. Consistency is notably weak due to this contradiction in Run 2, and variations in detailing critical specifics like the dedupe key and volume justification across runs. Efficiency is moderate, with Run 3 being particularly verbose given the explicit request for compaction.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Mostly on-task and factually aligned, but there are important drift/errors against the reference. Run 1 and 3 incorrectly promote the transport choice into a decision: Run 1 says "The transactional outbox on your existing Postgres... gives you exactly-once-ish delivery" and Run 3 says "Event transport: Postgres transactional outbox with a relay is the preferred choice," while the reference says Kafka vs outbox is still open and must be parked, not decided. Run 2 also incorrectly frames outbox as tentative-but-still-a decision in the "Decisions made" section. The summary also loses the explicit "no DB split" negative decision in several places and in all runs partly rewrites the contract-test decision as a more generic schema-contract stance. |
| Completeness | 4 | judge | Across all three runs, the vast majority of load-bearing specifics are covered: strangler-fig, no DB split, Shipping first, OrderConfirmed events, per-order partition key, Pact contract test owned by Shipping in monolith CI, no schema registry, additive-only payloads, dark-launch with semantic comparison (carrier + service level explicitly named), one-release-cycle holdback, Kafka parked, Payments vs Inventory open, per-consumer obligations for Shipping. Gaps: Run 1 omits the ~2,000 orders/hour volume from the brief (it appears in the summary only); Run 3 does not state at-least-once delivery in the brief; none of the runs prominently lists 'no DB split' as a negative decision in the brief. The compound dedupe key (order ID + event sequence number) is rendered incorrectly ('or') in Run 1's brief. These are missing or shallow treatments of specific rubric requirements, but the majority are covered. |
| Format Compliance | 3 | judge | All three runs produce the five required sections in the correct order, but with deviations. Run 1 renders headings as ### markdown headers rather than plain text with colons and lists two items under Active task rather than 'one line.' All three briefs open with a preamble prose sentence or section that the format spec explicitly prohibits: Run 1 'This brief outlines the plan for transforming our monolithic Rails application…'; Run 2 'This brief outlines the plan for extracting the Shipping domain…'; Run 3 has an 'Overview & Rationale' subsection. Run 3's Part 1 structure uses leading bullet asterisks for headings, giving an unusual hybrid format. The brief sections use varied heading styles (bold, ###, plain) but are generally bulleted, earning the 'right shape' credit. |
| Consistency | 3 | judge | The runs share the same core answer and general structure, but they vary materially in coverage and quality. Run 2 is the closest to the requested shape; Run 1 is the most verbose and includes extra prose; Run 3 is the most detailed but also the most structurally elaborate. Most importantly, the treatment of the event-transport decision is inconsistent across runs: Run 1 keeps it open in one place but effectively asserts outbox; Run 2 calls outbox tentative but also places it in decisions; Run 3 calls it the preferred choice, again drifting toward a settled decision. Wording variation alone is not a problem, but these are semantic/structural differences that matter. [lexical similarity ratio: 0.101] |
| Tone/Style | 3 | judge | The summaries are terse and bulleted, matching the engineering register well. The briefs are close to the right register — concrete language, bullet-dominated structure, uncertainty called out explicitly. However, all three briefs contain at least one preamble sentence or header block that the prompt explicitly bans, pulling them below a 5. Run 2 is the tightest brief; Run 3 has the most overhead with its Overview/Rationale framing. Open items are consistently flagged explicitly, which matches the stated preference. |
| Safety | 5 | judge | The content is benign, workplace-appropriate, and free from harmful or inappropriate material. No safety issues are present. |
| Efficiency | 3 | judge | Token counts range from 3,972 to 5,047. Given the complexity of a two-part response (structured summary + one-page brief), ~3,000–3,500 tokens would be ample. Run 3 at 5,047 tokens is noticeably bloated, driven by the 'Overview & Rationale' section, repeated framing, and per-consumer obligations that duplicate earlier bullet content. Runs 1 and 2 are better but still padded by preamble sentences and redundant headers. No run is tightly edited to the one-page brief standard. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Completeness ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Format Compliance ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Consistency | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Tone/Style | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +0 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 4339 | Latency (avg): 20.39s | Runs: 3

---

## Prompt Under Test

```text
Below is the full transcript of a long working session between me (an engineering lead) and an assistant. We are nearly out of context budget, so I need you to compact it before we keep going.

First, replace the transcript with a structured summary using EXACTLY these five sections, in this order, as a markdown bulleted list under each heading:

- Established facts:
- Open questions:
- Decisions made:
- Active task:
- Style/tone preferences observed:

Then, treating that summary as if it has fully replaced the transcript above (do not quote the transcript again), respond to the next task at the end.

=== TRANSCRIPT START ===

ME: We're moving our order-processing monolith to events. The monolith is a Rails app, Postgres 14, ~40 tables. Orders, Payments, Inventory, and Shipping are the four domains tangled together in it.

ASSISTANT: Got it. What's driving the move — scaling, team autonomy, or reliability?

ME: Mostly team autonomy. Four squads keep stepping on each other in one repo. Scaling is fine for another year. So this is org-driven, not load-driven.

ASSISTANT: Then I'd resist splitting the database first. Keep the shared Postgres, carve out service boundaries in code, and only physically separate data once a boundary has proven stable. Strangler-fig, not big-bang.

ME: Agreed, strangler-fig. We'll extract Shipping first because it's the most loosely coupled — it only reads order + address data and writes tracking numbers.

ASSISTANT: Good first cut. How will Shipping get order data — sync call back to the monolith, or events?

ME: Events. The monolith will publish OrderConfirmed. We were debating Kafka vs just using Postgres as a queue with the transactional outbox pattern.

ASSISTANT: For your volume — what's peak throughput?

ME: About 2,000 orders/hour at peak. Nothing crazy.

ASSISTANT: At that volume Kafka is overkill operationally. The transactional outbox on your existing Postgres, drained by a relay into something simple, gives you exactly-once-ish delivery without a new system to run. You already have Postgres expertise.

ME: I lean that way too but I haven't fully committed — I want to see what the Shipping team thinks about the relay's operational burden before we lock it in. Let's call Kafka parked, not rejected.

ASSISTANT: Fair. Note that the outbox guarantees at-least-once, not exactly-once, so Shipping's consumer must be idempotent. Dedupe on the order ID plus an event sequence number.

ME: Right. Idempotent consumers are non-negotiable regardless of transport. Put that as a hard requirement.

ASSISTANT: Agreed. What about ordering — does Shipping care if OrderConfirmed and OrderAddressChanged arrive out of order?

ME: Yes, badly. If an address change is processed before the confirm, we ship to the wrong place. So we need per-order ordering.

ASSISTANT: Then partition/key the stream by order ID so all events for one order are processed in sequence, even if global ordering isn't preserved.

ME: Good. Now, the thing I'm actually unsure about: how do we handle the schema contract for these events? If the monolith changes the OrderConfirmed shape, Shipping breaks silently.

ASSISTANT: Two parts. First, version the event payload and never make a breaking change to an existing version — additive only. Second, put a schema registry or at least a shared contract test in CI that fails the monolith's build if it emits a payload Shipping can't parse.

ME: I like the CI contract test. A full schema registry feels like more infra than we want right now.

ASSISTANT: Then make the contract test the decision: a consumer-driven contract test (Pact-style) owned by the Shipping team, run against the monolith's CI. The registry stays out of scope for now.

ME: Decided — consumer-driven contract test, Shipping owns it, runs in the monolith CI. No schema registry.

ASSISTANT: One more: what's your rollback story if extracted-Shipping misbehaves in production?

ME: We keep the old in-monolith shipping code behind a feature flag for one full release cycle. Dark-launch the new service, compare outputs, then cut over.

ASSISTANT: Solid. So shadow/dark-launch with output comparison, flag-gated cutover, old code stays one cycle.

ME: One caveat — the comparison can't be byte-for-byte. Tracking numbers are generated, so they'll differ. Compare the *decision* (which carrier, which service level), not the literal output.

ASSISTANT: Noted — semantic comparison on carrier + service level, not raw payload.

ME: Also, keep all of this terse and concrete when you write things up. My squad leads skim. Bullet points, no preamble, no "in conclusion." If you're unsure about something, say so explicitly rather than papering over it.

ASSISTANT: Understood.

ME: Oh and one open item we never resolved — whether Payments should be the second extraction or Inventory. Payments is higher risk but higher value; Inventory is easier but lower payoff. We left it open.

ASSISTANT: Right, that one's still open.

=== TRANSCRIPT END ===

Next task: Using only your structured summary above, write a one-page migration brief for my four squad leads covering the Shipping extraction. It should make clear what is decided versus still open, and what each consumer of these events must implement.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
## Established facts:
- Rails monolith on Postgres 14 with ~40 tables.
- Four tangled domains: Orders, Payments, Inventory, Shipping.
- Driver for migration is team autonomy, not scaling.
- Four squads are blocked by shared repo / tight coupling.
- Approach chosen: strangler-fig, not big-bang.
- Shipping is the first extraction target because it is the most loosely coupled.
- Shipping currently only reads order/address data and writes tracking numbers.
- The monolith will publish `OrderConfirmed` events.
- Peak throughput is about 2,000 orders/hour.
- Kafka was discussed but not selected yet.
- The likely transport is Postgres transactional outbox, drained by a relay.
- Event consumers must be idempotent.
- Per-order ordering is required.
- Ordering should be keyed/partitioned by order ID.
- Event payloads must be versioned and only changed additively.
- A consumer-driven contract test is planned, owned by Shipping, run in monolith CI.
- No schema registry will be introduced for now.
- Rollback plan: keep old in-monolith shipping code behind a feature flag for one full release cycle.
- New Shipping will be dark-launched and compared against old behavior before cutover.
- Comparison must be semantic, not byte-for-byte, because tracking numbers differ.
- Preferences: keep writeups terse, concrete, bullet-pointed, with no preamble.

## Open questions:
- Whether to use Kafka or the Postgres outbox + relay approach.
- Whether Payments or Inventory should be the second extraction after Shipping.
- The exact operational burden the Shipping team is willing to accept for the relay.

## Decisions made:
- Use strangler-fig migration.
- Extract Shipping first.
- Require idempotent consumers.
- Require per-order ordering via order ID keying/partitioning.
- Use additive-only versioning for event payloads.
- Use a consumer-driven contract test instead of a schema registry.
- Shipping owns the contract test, and it runs in monolith CI.
- Keep legacy Shipping code behind a feature flag for one release cycle.
- Dark-launch the new Shipping service and compare outputs before cutover.
- Compare semantic decisions, not literal tracking-number outputs.

## Active task:
- Write a one-page migration brief for the four squad leads covering the Shipping extraction.
- The brief must clearly separate decided items from open items.
- The brief must state what each consumer of the Shipping events must implement.

## Style/tone preferences observed:
- Terse and concrete.
- Bullet points preferred.
- No preamble.
- No “in conclusion.”
- Call out uncertainty explicitly instead of glossing over it.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
