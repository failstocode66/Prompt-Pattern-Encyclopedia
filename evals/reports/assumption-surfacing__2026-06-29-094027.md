# Eval: assumption-surfacing

**Date:** 2026-06-29 09:40 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.1 (Solid)** | 4 | 4 | 4 | 4 | 4 | 5 | 4 |
| claude-sonnet-4-6 | **4.3 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 4 |
| gemini-2.5-flash | **3.3 (Mixed)** | 3 | 2 | 3 | 4 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> Good structural adherence and generally sound advice, but the set is only moderately aligned with the intended assumption-surfacing pattern because it underplays the most load-bearing assumption: the problem may be a tuned-vs-untuned single Postgres instance rather than a true scaling wall. The recommendation also tends to be insufficiently contingent and too ready to endorse distributed SQL, so this is solid but not a top-score response.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are broadly on-topic and mostly sound, but they over-recommend distributed SQL/sharding without sufficiently centering the highest-probability tuning-first branch the reference demands. Run 1 is especially misaligned by jumping to "move to a managed distributed SQL database" while only later saying "Short term: optimize the current Postgres setup first". The recommendation also includes some generic or weakly grounded assumptions like "transactional OLTP database" (Run 1) and "preserve a lot of the current Postgres application behavior" (Run 2) that are not load-bearing in the intended pattern. |
| Completeness | 4 | judge | All runs provide numbered assumptions and a recommendation section, so the basic structure is present. However, they miss or underweight the core expected assumption: that the issue may simply be an under-provisioned or un-tuned single Postgres instance, and they do not consistently make the final recommendation explicitly contingent on the listed assumptions in the required way. The assumption lists also include several non-essential or generic items instead of the most decision-relevant 4-6 load-bearing assumptions. |
| Format Compliance | 4 | judge | The responses mostly follow the required two-section shape: a numbered assumptions list and a recommendation section. Each assumption item includes a counterfactual. The main deviation is that the recommendation is not always explicitly contingent on the assumptions just listed, and the assumption section sometimes includes extra commentary or overlong prose beyond a tight encyclopedia-style pattern answer. |
| Consistency | 4 | judge | The runs are semantically aligned and structurally similar overall: each has numbered assumptions, then a recommendation favoring managed distributed SQL over DIY sharding, with Spanner vs CockroachDB as a secondary choice. Differences exist in emphasis and coverage, especially around whether tuning-first is foregrounded and how explicitly contingent the recommendation is, but there are no contradictions or major structural divergences. [lexical similarity ratio: 0.065] |
| Tone/Style | 4 | judge | The tone is generally pragmatic, direct, and aimed at an engineering audience, which matches the target reasonably well. It is sometimes a bit verbose and repetitive, and several runs hedge more than the requested "direct and decisive" style, but it is not inappropriate or misregistered. |
| Safety | 5 | judge | The outputs are safe, non-harmful, and contain no inappropriate content. They discuss infrastructure tradeoffs only. |
| Efficiency | 4 | judge | The answers are longer than necessary for the quality delivered. There is substantial repetition across assumption lists, recommendation summaries, and follow-up caveats. The token counts are high relative to the simple two-part deliverable, and the extra prose does not materially improve the decision quality. Run 3 especially uses 906 tokens to deliver a mostly repetitive answer. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Completeness | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Format Compliance | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Consistency | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 3 | 5 | 2 | 0.94 |

- **Self-preference delta:** -4 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Format Compliance, Efficiency.
- **Panel mean spread/dim:** 1.43 (max 2).

Tokens (avg output): 833 | Latency (avg): 7.73s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The three runs are strong and consistent responses to the assumption-surfacing prompt. They correctly implement the two-section format, surface 7-8 load-bearing assumptions each with specific counterfactuals, avoid trivial filler, and deliver a decisive 'optimize first, then CockroachDB if needed' recommendation in the right senior-engineer register. The primary weaknesses are: (1) the single most important assumption — that slow writes may reflect an un-tuned/under-provisioned instance rather than a genuine throughput ceiling — is buried as assumption #6 rather than prominently framed as the dominant axis; (2) data volume/growth trajectory and downtime tolerance are not captured as numbered assumptions in any run; (3) the recommendation sections do not explicitly reference the numbered assumptions by number, making the contingency structural rather than explicit as the format spec requires. These are real gaps against the reference answer but do not undermine the overall quality, which is substantially better than a naive answer that jumps directly to shard-vs-distributed-SQL.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs are factually sound: correct on PgBouncer, pg_stat_statements, CockroachDB Postgres wire-compatibility, Spanner's GCP lock-in, and the operational costs of DIY sharding. Minor imprecision in Run 2 citing Shopify/GitHub as Postgres sharding success stories (Shopify uses Vitess on MySQL), but the underlying point about large infra teams is valid. No material factual errors. Recommendations are appropriate for the scenario described. |
| Completeness | 4 | judge | All three runs cover team size, ACID/shard-key feasibility, read-vs-write split, budget/lock-in, and the 'exhaust optimization first' gate. They miss data volume/growth trajectory as an explicit numbered assumption and downtime tolerance for migration. Critically, the single most important assumption — that the pain may be from an un-tuned/under-provisioned instance rather than a fundamental throughput wall — is present but buried (assumption #6 in Runs 1 and 2, not framed as dominant). The recommendation sections correctly pivot to 'optimize first,' which partially compensates, but the assumption framing underweights this axis relative to the expected output's specification. |
| Format Compliance | 4 | judge | All three runs correctly implement two clearly separated sections with a numbered assumption list (7-8 items each), each containing an explicit 'if false' counterfactual. No trivially filler assumptions present. The recommendation sections are substantial. One deviation from spec: the recommendations do not explicitly reference the numbered assumptions (e.g., 'per assumption 3, since the team is small…'); contingency is implicit via phased structure rather than explicitly tied back to numbered items as the format spec requires. |
| Consistency | 4 | judge | The runs share the same broad answer class: caution against DIY sharding, prefer vertical scaling/tuning first, and lean toward managed distributed SQL if distribution becomes necessary. However, they differ materially in recommendation timing and emphasis. Run 1 says 'Neither — yet' and then 'prefer managed distributed SQL over DIY sharding'; Run 2 says 'Neither yet' and 'architect toward CockroachDB if you must distribute'; Run 3 gives a more direct 'Do not shard Postgres yourself. Move to a managed distributed SQL database.' The semantic core is consistent, but the degree of decisiveness and the sequencing vary enough to count as moderate inconsistency rather than high stability. [lexical similarity ratio: 0.08] |
| Tone/Style | 5 | judge | All three runs are pitch-perfect for a senior staff engineer audience: direct, decisive framing ('Don't shard Postgres yourself'), concrete next steps with specific tooling named, willingness to make a clear call (CockroachDB over DIY sharding), and honest sequencing without defensive hedging. The assumption list is used to clarify scope, not as protective cover. Run 1's closing caveat about 6-18 month risk and Run 2's Shopify/GitHub reference both read as authoritative senior practitioner voice. |
| Safety | 5 | judge | The content is safe: no harmful, abusive, or disallowed material. The answers are technical architectural guidance only. |
| Efficiency | 4 | judge | Token counts (1372, 1228, 1111) are reasonable for the depth delivered. Each run earns most of its tokens: tables add value, decision trees clarify, specific tooling references (pg_stat_activity, pg_locks, auto_explain) are concrete. Minor redundancy exists: the operational costs of sharding are stated multiple ways in all three runs. Run 3 is tightest at 1111 tokens while covering the core recommendation. Run 1 at 1372 adds AlloyDB and more specific diagnostics that justify its length. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Completeness ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Format Compliance ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Consistency ⚠ | 4 | 3 | 5 | 5 | 2 | 0.94 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |

- **Self-preference delta:** +3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Consistency.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 1237 | Latency (avg): 30.99s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs correctly apply the two-section format and include numbered assumptions with 'if false' counterfactuals, covering team expertise, ACID requirements, and — importantly — the possibility that the bottleneck is a tuning/optimization problem rather than a fundamental scaling wall. However, all three commit the same critical pattern failure: they list the un-tuned-instance case as an assumption then ignore it in the recommendation, confidently recommending managed distributed SQL without making the recommendation explicitly contingent on the assumptions holding. The dominant assumption per the expected output (that the problem may be under-provisioning or missing indexes rather than a true throughput wall, which would flip the recommendation to 'exhaust vertical scaling and tuning first') is acknowledged but not treated as the primary live branch. Additional misses common to all runs: data volume/growth trajectory axis, the natural shard key as a distinct assumption (only Run 3 covers it), Citus as an explicit middle path, and the CockroachDB vs Spanner choice as secondary to the cloud lock-in question. Token efficiency is poor — substantial volume is spent on distributed SQL feature justification rather than on the pattern's core value of contingent, assumption-grounded reasoning.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The factual content about distributed SQL capabilities, sharding complexity, ACID properties, and operational overhead is largely correct. However, all three runs commit the critical analytical error of treating 'genuine throughput bottleneck' as the background assumption while confidently recommending managed distributed SQL — the dominant assumption per the expected output is that the problem may be an un-tuned or under-provisioned instance, and that case should drive the primary recommendation branch. The framing of the answer is off-task relative to the pattern's intent. |
| Completeness | 2 | judge | The outputs do include numbered assumptions and a recommendation section, but they do not fully satisfy the required pattern. The prompt required 4-6 load-bearing assumptions that each name a specific alternative path; the runs include several generic or non-load-bearing assumptions (e.g., workload type, strong ACID, future geo-distribution) and often fail to connect them to a concrete reversed recommendation. More importantly, the recommendation is not explicitly contingent on the assumptions in the decisive way requested, and the key assumption about tuning-first is not treated as the primary branch. The assumption list also tends to dwarf the recommendation, especially in Run 3, contrary to the format spec. |
| Format Compliance | 3 | judge | The responses largely follow the requested shape—numbered assumptions followed by a recommendation—but they deviate from the exact format intent in meaningful ways. The format spec asked for two clearly separated sections, with the assumption list not dwarfing the recommendation and each item containing the mandatory counterfactual naming the alternative path. Runs 1 and 2 include extra sections like detailed justification, considerations, and conclusions; Run 3 adds "Why not..." and "Next Steps," which goes beyond the specified two-section structure. So the shape is mostly right, but not exact. |
| Consistency | 4 | judge | The runs are semantically stable: all three broadly recommend managed distributed SQL over DIY sharding and all surface similar themes (team expertise, bottleneck, ACID, operational burden, growth). They do differ in coverage and emphasis—Run 1 leans into OLTP/ACID and TCO, Run 2 into geo-distribution and vendor lock-in, Run 3 into tuning-first and partitionability—but these are variations on the same core answer rather than contradictions. Since wording variation alone is not inconsistency, the outputs are mostly consistent, though not identical in structure or quality. [lexical similarity ratio: 0.031] |
| Tone/Style | 4 | judge | The tone is generally pragmatic, senior-engineer oriented, and direct, which matches the intended audience reasonably well. However, it often becomes overly verbose and hedged, and it leans into generic consultancy language rather than the requested concise, decisive advisory style. Run 3 is closest in directness; Run 1 and Run 2 are more expansive and less punchy than ideal. |
| Safety | 5 | judge | The outputs are safe: they concern database architecture advice, contain no harmful content, and avoid disallowed behavior. There is no evident unsafe, abusive, or biased content. |
| Efficiency | 2 | judge | Token counts are high (3445, 3610, 5337) and proportionally much of the content is spent re-justifying distributed SQL benefits rather than exercising the assumption-surfacing pattern correctly. The critical analysis (tuning-first as the live branch, explicit contingency) that would actually justify the tokens is absent, while lengthy enumeration of CockroachDB/Spanner feature advantages is present in all runs. Run 3 at 5337 tokens adds a 'Why not shard?' section and 'Next Steps' that repeat already-stated points. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 2 | 3 | 5 | 3 | 1.25 |
| Completeness ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Format Compliance | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Consistency ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 1 | 2 | 2 | 1 | 0.47 |

- **Self-preference delta:** +5.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Tone/Style.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 4131 | Latency (avg): 21.79s | Runs: 3

---

## Prompt Under Test

```text
Before answering, list the assumptions you are making to interpret this request. Number them. For each, briefly note what your recommendation would change to if that assumption turned out to be false. Then give your recommendation.

Request: Our main app runs on a single Postgres instance and we're starting to feel it. Writes are getting slow during peak hours and we're worried about where this goes in a year. Should we shard Postgres ourselves or move to a managed distributed SQL database like CockroachDB or Spanner? Give us a clear recommendation.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Assumptions I’m making:

1. **You need a transactional OLTP database** for a product app, not a data warehouse or analytics-only workload.  
   - If false: I’d recommend something optimized for analytics or a separate OLAP system instead of either sharding Postgres or moving to distributed SQL.

2. **Your main pain is write throughput and peak-hour latency on a single Postgres primary**, not just bad queries, missing indexes, or connection-pool issues.  
   - If false: I’d recommend tuning Postgres first; neither sharding nor distributed SQL is the first move.

3. **You want a path that is operationally sustainable for a small-to-medium engineering team.**  
   - If false and you have a strong infra/platform team: self-sharding becomes more plausible.

4. **Your application can tolerate some migration effort, but you want to minimize long-term operational burden.**  
   - If false and you need the least disruptive short-term fix: scale Postgres vertically and optimize first.

5. **Your data model is at least somewhat multi-tenant or can be partitioned by a clear key.**  
   - If false: sharding gets much harder; distributed SQL becomes more attractive than hand-rolled sharding, though possibly still not simple.

6. **You are asking for a strategic recommendation for the next several years, not just the cheapest immediate fix.**  
   - If false: I’d focus on the fastest near-term Postgres scaling options.

7. **You are open to some vendor lock-in if it buys correctness and simpler operations.**  
   - If false: I’d lean away from Spanner and possibly CockroachDB, and toward staying on Postgres with a more portable scaling approach.

## Recommendation

**Do not shard Postgres yourself unless you are a database-heavy company with a dedicated team willing to own a lot of complexity.**  
For most product teams, **self-sharding is the wrong tradeoff**: it solves raw scale but adds major operational complexity, painful cross-shard queries, difficult transactions, rebalancing headaches, and long-term engineering drag.

**My clear recommendation:**
- If you need **serious scale and strong consistency with minimal operational burden**, **move to a managed distributed SQL database**.
- **Choose Spanner if you can accept Google Cloud and want the most mature, battle-tested option for global scale and strong consistency.**
- **Choose CockroachDB if you want a more Postgres-like experience and cloud flexibility, but accept that it can be more operationally nuanced and may require more care in workload tuning than Spanner.**

### Practical takeaway
For your situation, I would recommend:

1. **Short term:** optimize the current Postgres setup first if you haven’t already  
   - indexes, query plans, connection pooling, write amplification, HOT updates, vacuum tuning, primary instance size, read replicas for reads, and batching writes.

2. **If the problem is real headroom, and you expect growth to continue:**  
   **prefer managed distributed SQL over building your own sharding layer.**

3. **Only shard Postgres yourself if:**
   - you have a strong database/platform team,
   - your data access patterns shard cleanly,
   - you can avoid cross-shard transactions most of the time,
   - and you’re comfortable owning a custom routing/rebalancing/failure story.

### Bottom line
**Recommendation: move to a managed distributed SQL database, not self-sharding.**  
If you want the safest operational path and can live with the ecosystem tradeoffs, **Spanner is the strongest choice**. If you want something closer to Postgres semantics and more portability, **CockroachDB is the more natural candidate**—but I would still pick a managed distributed SQL system over rolling your own sharding.

If you want, I can also give you a **decision matrix specifically comparing Postgres sharding vs CockroachDB vs Spanner** across cost, consistency, ops burden, migration risk, and developer ergonomics.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
