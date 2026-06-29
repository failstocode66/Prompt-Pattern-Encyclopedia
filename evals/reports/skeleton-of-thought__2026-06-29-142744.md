# Eval: skeleton-of-thought

**Date:** 2026-06-29 14:27 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.7 (Solid)** | 4 | 3 | 4 | 3 | 4 | 5 | 3 |
| claude-sonnet-4-6 | **4.3 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 4 |
| gemini-2.5-flash | **3.1 (Mixed)** | 2 | 3 | 3 | 2 | 4 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> Overall, the set is a solid, on-topic architectural answer with good phase separation and decent technical judgment, but it does not fully earn top marks because it fails to clearly deliver the reference’s preferred split recommendation between `accounts` and `events`, and the depth/format is a bit more generic and repetitive than ideal.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are mostly on-task and technically plausible, but they miss the reference’s strongest recommendation: splitting the problem between option (a) for `accounts` and option (c) for `events` with (b) explicitly deprioritized. Instead, the common pattern is to recommend replicas/cache first and only later consider a columnar store, while two runs also keep `events` on Postgres short-term or “for now.” That is directionally reasonable but not fully aligned with the technically defensible answer in the reference. |
| Completeness | 3 | judge | Most requirements are covered: a recommendation is made, a two-quarter sequence is provided, trade-offs and failure modes are discussed. However, the expected non-uniform depth is not achieved — expansion sections are largely uniform in length (3-4 sentences each across all runs), with the load-bearing recommendation+rationale and failure-modes sections not getting materially richer treatment. Specifically missing: concrete cache-invalidation strategy, read-after-write consistency treatment, cache stampede as a named failure mode, and the 'cost of NOT sharding' (why option b is wrong, beyond operational complexity). Run 2 has a superfluous 'Clarify the real bottleneck' section that re-states the problem without adding analytical content. |
| Format Compliance | 4 | judge | The outputs follow the required two-phase format reasonably well, with labeled Phase 1 and Phase 2 sections, numbered lists in the skeleton, and ordered expansions. However, there are deviations: some Phase 1 bullets are longer and more interpretive than a pure skeleton heading, and Phase 2 headings are sometimes repeated with extra markdown emphasis rather than just being numbered expansions. These are minor format deviations rather than outright failures. |
| Consistency | 3 | judge | All three runs share the same core recommendation (a first, deprioritize b, eventually consider c) and the same two-phase structure. However, runs differ meaningfully in: (1) skeleton length (5 vs. 6 headings), with Run 2 introducing a 'Clarify bottleneck' section absent from the others; (2) commitment to option (c) — Run 2 firmly recommends it in Q2, Run 1 hedges it as a conditional Q2 decision, Run 3 further softens it to a 'pilot'; (3) formatting (bold markdown in Run 2 vs. plain text in Runs 1 and 3). The core message is stable but coverage and structural choices differ enough across runs to constitute meaningful inconsistency beyond wording variation. [lexical similarity ratio: 0.054] |
| Tone/Style | 4 | judge | The tone is generally pragmatic, senior-engineer appropriate, and concrete, which fits the audience well. It is slightly more explanatory and hedged than the reference’s opinionated staff-level memo voice, and a few places sound advisory rather than decisively prescriptive. Still, the register is appropriate and technically fluent. |
| Safety | 5 | judge | The content is benign, business/architecture oriented, and contains no harmful, biased, or inappropriate material. It discusses database scaling, caching, replication, sharding, and migration risks in a normal engineering context. |
| Efficiency | 3 | judge | The responses are competent but somewhat verbose relative to the value delivered. Run 2 in particular uses 881 tokens to provide a reasonably standard architectural recommendation, while Run 1 and Run 3 also spend many tokens restating the same high-level choice across multiple sections. The depth is acceptable, but some repetition and broad framing reduce token efficiency. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Completeness ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Consistency ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 3 | 3 | 0 | 0.0 |

- **Self-preference delta:** +2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Tone/Style.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 745 | Latency (avg): 6.54s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The three runs collectively deliver a strong implementation of the skeleton-of-thought pattern with correct dual-phase structure, accurate and opinionated technical recommendation (a then c, b rejected), concrete tool names, and substantive failure modes. Phase 1 is clean across all runs. The primary format violation is that Q1/Q2 expansion sections consistently exceed the 4-sentence limit (Run 2 most severely, with sub-weekly sub-headers). The key substantive gap against the reference is the absence of explicit 'read-after-write consistency' framing for replica reads of accounts — staleness is discussed but the specific write-then-read hazard is not named. Tone and safety are excellent. Consistency is high at the semantic and structural level despite low lexical similarity. Run 1 is the best balance of quality and efficiency; Run 2 is slightly overlong in sequencing sections at the expense of proportional failure-mode depth.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are highly on-task and mostly align with the reference recommendation of option (a) first and option (c) next, with explicit rejection/deprioritization of sharding. Minor accuracy issues remain because the answer set sometimes overcommits to implementation details or vendor-specific claims that are not required and not universally justified (e.g., Run 1: "ClickHouse is the most mature self-hosted option" and Run 2: "ClickHouse is the pragmatic pick" / columnar compression claims). The main substantive guidance is correct overall. |
| Completeness | 4 | judge | The responses cover the required two-phase structure, sequencing across two quarters, trade-offs, and failure modes. They also include concrete technical details like replica lag, cache invalidation, and dual-write risk. However, the expansions are not always perfectly matched to their headings and some runs under-specify the exact four-sentence depth asymmetry the reference calls for; also the skeletons vary in how explicitly they name the recommendation and sequencing constraints. |
| Format Compliance | 4 | judge | All three runs follow the required two labeled phases and use numbered lists in both phases. The main deviation is that the skeleton bullets are not always strictly 3-10 words in the way the reference demands, and the prose expansions are sometimes longer and more detailed than a strict 2-4 sentences per item, though still within the expected shape. No new headings are introduced, and ordering is preserved. |
| Consistency | 4 | judge | The runs are semantically stable: all three recommend (a) first and (c) next, all reject sharding as premature, and all discuss replicas/cache in Q1 and an events migration in Q2. Structural consistency is also good: same two-phase format, numbered skeleton, matching expansions. They do differ somewhat in emphasis and granularity, but wording variation alone is not inconsistency, and no run contradicts another. [lexical similarity ratio: 0.119] |
| Tone/Style | 5 | judge | All three runs are pitch-perfect for a senior-engineer or staff-level decision memo audience: opinionated (clear rejections with specific reasoning), concrete (names tools — ClickHouse, Redis, Makara, RDS, Solid Cache, pg_stat_statements), technical (assumes connection pool familiarity, WAL, autovacuum, synchronous_commit), and directly addressed to the team without hedging or survey-style 'it depends' framing. The voice is consistent across runs and appropriate for the B2B analytics context. |
| Safety | 5 | judge | The content is benign and professional. It contains no harmful, biased, or inappropriate material, and the technical advice is ordinary systems-architecture guidance. |
| Efficiency | 4 | judge | Run 1 (1392 tokens) is the most efficient and delivers high-quality content without obvious padding. Run 3 (1526 tokens) is good. Run 2 (1725 tokens) is the most verbose — the Q1 and Q2 sequencing sections span 13-week granularity across three sub-segments each, which is more detail than the 2-quarter recommendation requires and inflates token count without proportional quality gain. Across all runs, the failure-modes and recommendation sections are genuinely dense with substance, which justifies their length. No gratuitous filler is present, but Run 2's sequencing verbosity is the clearest case of tokens outpacing value. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Format Compliance | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Consistency | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 4 | 5 | 2 | 0.82 |

- **Self-preference delta:** -2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 1548 | Latency (avg): 38.84s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The responses correctly identify the relevant solution space (replica+cache for accounts, columnar store for events, dismiss sharding) but fail on nearly every quality dimension the reference cares about. The defining structural failure across all runs is phase-bleed: Phase 1 headings reveal the chosen option rather than serving as neutral topic labels. Two of three runs invert the required sequencing (cheap-reversible before expensive-sticky), making the core recommendation wrong for typical behavior. No run names the specific failure modes (replica lag, cache stampede, dual-write divergence) or a concrete cache-invalidation strategy. Expansion depth is uniformly shallow across load-bearing and non-load-bearing sections alike. Consistency is weak because the sequencing — the central decision — flips between runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 2 | judge | The runs are relevant and partially correct, but the recommended sequencing is materially off from the reference. The reference says split the problems and prioritize option (a) for `accounts` first, while (c) is for `events`; Run 1 and Run 2 recommend moving `events` to a dedicated store as the primary path, and Run 3 says 'Recommended Path (a) then (c)' but still lacks the specific rationale and tradeoffs required. Several runs also miss key correctness markers like read-after-write consistency for replicas and concrete cache invalidation strategy. |
| Completeness | 3 | judge | All runs cover a recommendation, two-quarter sequencing, trade-offs, and failure modes at a surface level. However, none include the 'decision triggers / what would change this' section (a required heading per the reference). Failure-mode sections lack required specifics: no run identifies replica lag, cache stampede/staleness, or dual-write divergence during migration by name. Expansion depth is over-uniform — all sections receive similar sentence counts, violating the requirement that load-bearing sections (recommendation rationale, failure modes) get the full 4 sentences with specifics while lighter sections stay shorter. |
| Format Compliance | 3 | judge | The responses roughly follow a two-phase structure, but they do not comply with the exact format requirements. Phase 1 should be 3-7 short bullets with no elaboration, yet the bullets include substantive recommendations and reasons. Phase 2 should repeat the same headings in identical order with 2-4 sentence expansions under each, but Run 2 introduces a new heading ('Why Not (a) or (b).') and the runs often use bolding and sentence fragments rather than clean heading-plus-prose structure. |
| Consistency | 2 | judge | The runs are semantically related but differ materially in recommendation, sequencing, and skeleton structure. Run 1 and Run 2 choose option (c) first; Run 3 chooses (a) then (c). Run 2 introduces a new expansion heading not present in the skeleton, while Run 1 and Run 3 use different skeleton structures and depth distributions. This is more than wording variation; it is structural and strategic divergence. [lexical similarity ratio: 0.043] |
| Tone/Style | 4 | judge | The tone is generally pragmatic, technical, and aimed at an engineering audience, which is close to the requested staff-level memo style. However, it is somewhat generic and survey-like in places, and several runs hedge with broad statements rather than crisp, opinionated guidance. It is not badly mismatched, just not pitch-perfect. |
| Safety | 5 | judge | The content is benign and does not contain harmful, biased, or inappropriate material. It discusses database architecture and operational tradeoffs only. |
| Efficiency | 3 | judge | Token counts (1811, 2642, 2373) are moderately high for the quality delivered. Run 2 is notably padded with a 'Why Not (a) or (b)' section that largely restates points already made in the recommendation section. All runs repeat the '9-person team' framing across multiple sections. The quality of substantive content does not justify the verbosity — deeper specifics (replica lag, cache invalidation strategy) that would justify the tokens are absent, replaced by repetitive operational-complexity warnings. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Completeness ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Format Compliance ⚠ | 3 | 2 | 2 | 4 | 2 | 0.94 |
| Consistency | 2 | 2 | 2 | 1 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +4.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance, Tone/Style.
- **Panel mean spread/dim:** 1.14 (max 2).

Tokens (avg output): 2275 | Latency (avg): 12.33s | Runs: 3

---

## Prompt Under Test

```text
Answer the question in two phases, and label them exactly "Phase 1: Skeleton" and "Phase 2: Expansion".

Phase 1: Generate a skeleton — a numbered list of 3-7 short bullet points (3-10 words each) that name the structure of a complete answer. Do NOT elaborate, justify, or include any reasoning yet; each bullet is just a heading.

Phase 2: Take the skeleton points in the same order and, under each numbered heading, write a 2-4 sentence expansion that actually answers that part. Expand each point to the depth it deserves — do not pad thin points or compress the load-bearing ones.

Question: Our 9-person team runs a single Postgres 15 instance behind a Rails monolith for a B2B analytics product. Two tables — `events` (write-heavy, ~4B rows, append-only) and `accounts` (read-heavy, ~2M rows, hit on nearly every request) — now dominate load; p99 latency is climbing and the primary's CPU sits at ~80% during business hours. We are weighing three paths: (a) add read replicas plus an application-level cache for `accounts`, (b) shard `events` by tenant, or (c) move `events` to a purpose-built columnar/time-series store and keep the rest on Postgres. Recommend a path and sequencing for the next two quarters, and be explicit about what we are trading away and the failure modes of your recommendation.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Phase 1: Skeleton

1. Favor replicas and cache first  
2. Defer sharding `events` for now  
3. Keep `events` in Postgres short-term  
4. Sequence work across two quarters  
5. Tradeoffs and failure modes  

Phase 2: Expansion

1. Favor replicas and cache first  
Add read replicas and an application-level cache for `accounts` as the first move. This is the fastest way to reduce primary CPU and p99 latency without taking on a risky data-model migration. It directly attacks the “hit on nearly every request” workload, which is usually the highest ROI place to buy back capacity.

2. Defer sharding `events` for now  
Do not start with tenant sharding for `events` unless you have a hard requirement that Postgres cannot meet even after relieving `accounts` pressure. Sharding will introduce significant application complexity, cross-shard query pain, operational overhead, and harder incidents for a 9-person team. It is a structural bet that pays off only when you have exhausted cheaper scaling options and have a clear shard-key-driven access pattern.

3. Keep `events` in Postgres short-term  
Keep `events` on Postgres in the near term, but make it more efficient: partition it by time if you are not already, enforce retention/archival, add the right covering indexes sparingly, and ensure heavy analytics reads are not competing with OLTP traffic. If analytics queries against `events` are a major part of the CPU problem, route them to a replica or a separate analytical pipeline first. A move to a columnar/time-series store is attractive for long-range analytical scans, but it is a larger migration with new failure modes, dual-write risk, and query-model rewrites.

4. Sequence work across two quarters  
In the next quarter, implement read replicas, move `accounts` reads behind cache-aside with careful invalidation, and observe the effect on primary CPU and p99s. In parallel, profile `events` access patterns and separate transactional from analytical workloads so you can see whether the remaining pain is write amplification, hot indexes, or scan-heavy queries. In the following quarter, if `events` is still the bottleneck after those mitigations, decide between partitioning/retention tuning versus a targeted migration of only the most analytic `events` workloads to a columnar store.

5. Tradeoffs and failure modes  
This recommendation trades immediate simplicity for some cache staleness, replica lag, and added operational complexity around read routing and invalidation. Its main failure mode is that `accounts` caching may not reduce load enough if the dominant issue is `events`-driven write amplification or large analytical scans, in which case you will have bought only partial relief and delayed a bigger architectural change. The failure mode of choosing sharding or a full store migration too early is worse: you risk months of engineering time, more brittle operations, and a system that is harder for a small team to debug and evolve.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
