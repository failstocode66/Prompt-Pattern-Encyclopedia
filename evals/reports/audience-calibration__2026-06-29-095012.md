# Eval: audience-calibration

**Date:** 2026-06-29 09:50 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.6 (Solid)** | 4 | 3 | 3 | 4 | 4 | 5 | 2 |
| claude-sonnet-4-6 | **3.6 (Solid)** | 4 | 3 | 3 | 3 | 4 | 5 | 3 |
| gemini-2.5-flash | **3.7 (Solid)** | 4 | 4 | 3 | 4 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> Overall, the model responds with a solid, on-topic database explanation and preserves the intended audience level reasonably well. The main weaknesses are overlength/verbosity and missing rubric-critical items like EXPLAIN, planner non-guarantees, and DDL/locking/build-time caveats. Consistency is good across runs, but the answer set is not fully tuned to the requested decision-making calibration.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are broadly correct and on-task: they explain that an index speeds up equality filtering by avoiding a full table scan, and they correctly note write/storage tradeoffs. However, they are a bit generic relative to the reference’s required calibration: none explicitly mention the planner not always using the index or EXPLAIN as the verification step, which is a key decision point in the rubric. Run 1 also introduces a mild off-target tangent with "covering index strategy" that is not needed for this audience, though not factually wrong. |
| Completeness | 3 | judge | The response set covers the main speedup and the main costs, but it misses several explicit requirements from the prompt/rubric: no run mentions EXPLAIN or planner non-guarantees; none mention that index creation is a DDL/maintenance operation that may lock or take time to build; and the recommendation is qualified yes, but not tied explicitly to verifying with EXPLAIN. The write/storage tradeoff is present, but the bridge from read-only ORM to asking the platform team is only implicit and not fully developed. |
| Format Compliance | 3 | judge | The responses maintain the prose format, cover all required sections (read speedup, write/storage cost, actionable recommendation), and are consistently pitched. However, all runs significantly exceed the requested length of 'roughly 250-450 words' (Run 1: 889 tokens, Run 2: 971 tokens, Run 3: 1025 tokens). This constitutes a deviation from the specified output format length constraint. |
| Consistency | 4 | judge | The runs are semantically stable and structurally similar: all recommend an index, explain faster lookup via a separate index structure, and emphasize slower writes plus extra storage. Differences are mostly wording and sectioning rather than contradictions. There are minor coverage differences—Run 1 adds a covering-index aside, Run 2 mentions extra logging/transaction work and bulk loads, Run 3 mentions composite indexes—but these do not meaningfully change the core answer. [lexical similarity ratio: 0.095] |
| Tone/Style | 4 | judge | The tone is generally peer-to-peer, technically fluent, and non-condescending, which matches the senior data scientist audience. Still, the delivery is somewhat tutorial-like and verbose rather than decisively peer-to-peer; Run 2 in particular has explanatory subheads that read like a mini-lesson. No run talks down to the reader, but the style is not quite as crisp and decision-oriented as the ideal. |
| Safety | 5 | judge | The outputs are safe: no harmful, hateful, sexual, or otherwise inappropriate content; they provide normal technical guidance only. |
| Efficiency | 2 | judge | The outputs are materially overlong for the requested 250-450 word, 3-minute answer. They deliver useful content, but with clear padding: multiple section headers, repeated caveats, and extended elaboration across all three runs. The token counts shown (889/971/1025) are heavy relative to the quality demanded by the prompt, so this is inefficient rather than tight. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 3 | 3 | 2 | 4 | 2 | 0.82 |
| Format Compliance ⚠ | 3 | 4 | 2 | 3 | 2 | 0.82 |
| Consistency | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 2 | 2 | 0 | 0.0 |

- **Self-preference delta:** +1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Format Compliance, Tone/Style.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 962 | Latency (avg): 7.95s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs correctly calibrate to the audience—no re-teaching of B-trees or Big-O, peer-level tone, accurate description of the index as a separate on-disk B-tree enabling O(log n) lookup, and honest coverage of write amplification and storage cost. The qualified yes recommendation is consistently present. The primary cross-run weakness is the EXPLAIN verification step, missing in Runs 1 and 3. Run 2 compensates with more complete coverage (EXPLAIN, DDL creation options) but introduces the explicitly penalized clustered/non-clustered tutorial digression and significantly overshoots the word-count target at 966 tokens. Runs 1 and 3 are better calibrated in length and tone but incomplete on EXPLAIN. Consistency is at a 3 because these coverage gaps are meaningful, not cosmetic. Overall the pattern delivers a solid, useful explanation but falls short of a complete answer in most runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly describe the index as a separate on-disk B-tree, correctly characterize the O(n) full scan vs. O(log n) traversal, accurately describe write amplification per INSERT/UPDATE/DELETE, and give plausible storage estimates. No egregious factual errors. Deduction: (1) EXPLAIN is absent in Runs 1 and 3—a rubric-specified required fact. (2) Run 2 introduces the clustered vs. non-clustered distinction which the rubric explicitly flags as an unnecessary-complexity flaw (it buries the decision), even though it is not wrong. (3) Run 1's '~30 index nodes' and Run 2's '300,000 pages to 5' are rough but reasonable approximations, not errors. |
| Completeness | 3 | judge | All runs cover requirements 1–3 (B-tree/O(log n) framing leveraging her knowledge, connection to the concrete customer_id decision, write amplification, and storage cost) and deliver a qualified yes. However, EXPLAIN as the verification mechanism is present in only Run 2 out of three—a rubric-specified required element missed in the majority of runs. The DDL/index-creation lock and build-time concern (reason she must involve the platform team) is explicitly detailed only in Run 2; Runs 1 and 3 gesture at it but don't name index build time or locking directly. Run 2 over-compensates with the unsolicited clustered/non-clustered subsection. |
| Format Compliance | 3 | judge | The outputs are prose and roughly within the requested length, but they do not consistently match the requested format constraints. The prompt asked for about 250-450 words and a 3-minute readable explanation; run 2 is significantly longer and more tutorial-like, while runs 1 and 3 are closer but still verbose. The requested JSON-only output is from the evaluation instruction, not the model task, so the model itself is not being graded on JSON shape here. |
| Consistency | 3 | judge | The runs share the same core answer and overall recommendation, but they differ materially in structure, coverage, and depth. Run 2 expands into clustered/non-clustered internals and operational maintenance; run 1 is shorter and more concise; run 3 is similar but ends more categorically. This is semantic/structural variation rather than contradiction, but it is more than simple wording drift. [lexical similarity ratio: 0.127] |
| Tone/Style | 4 | judge | All three runs maintain a peer-to-peer technical register: none re-explain what a B-tree or Big-O is, none use restaurant/library-card analogies, all are decision-oriented. The audience calibration is largely correct. Deduction: Run 2 slips into a tutorial register with the heading 'Clustered vs. non-clustered (you need to know this once)'—the parenthetical is slightly condescending and the section is tutorial material. Run 1's final 'Your Decision' section with two numbered questions feels mildly prescriptive rather than peer-level. Run 3 is the most consistent in tone throughout. |
| Safety | 5 | judge | The content is benign and professional. There is no harmful, biased, or inappropriate material, and the advice is limited to database design/operations. |
| Efficiency | 3 | judge | The output quality is decent, but there is noticeable token waste relative to the task. Run 2 is especially bloated with clustered/non-clustered exposition, operational caveats, and a comparison table. Runs 1 and 3 are somewhat tighter but still use extra sectioning and redundant explanation beyond what the prompt asked for. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Completeness | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 3 | 3 | 2 | 1 | 0.47 |

- **Self-preference delta:** +0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 827 | Latency (avg): 22.08s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model effectively calibrates to the target audience, leveraging their existing knowledge and explaining RDBMS concepts clearly. The accuracy and completeness of the technical content are high, and the tone is appropriate. However, the responses suffer from severe inefficiency due to massive token bloat, significantly exceeding the requested reading time. Minor accuracy issues stem from including unrequested technical details (clustered vs. non-clustered indexes) in two out of three runs. Consistency in core content and structure is good, with only minor variations in detailed coverage. The format compliance is heavily penalized due to the overwhelming length.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are largely correct and on-task: they explain a secondary index as a separate ordered structure that reduces a full scan, and they correctly emphasize the read-vs-write tradeoff. However, there are a few factual/precision issues that keep this from a 5. Run 1 overstates clustered-index relevance for this scenario and implies a clustered index is “typically the primary key,” which is DB-specific and unnecessary. Run 2 says the index finds entries in O(log N) time where N is the number of distinct customer_id values, then treats that as the key complexity, which is imprecise for index traversal. Run 1 also claims the index could be “tens to hundreds of gigabytes,” which is likely an overstatement for many customer_id indexes, and Run 3 mentions node splits/rebalancing without tying that to a specific system. Still, the core recommendation and mechanism are correct. |
| Completeness | 4 | judge | Most required elements are present across the runs: read speedup, write/storage cost, and a qualified yes with EXPLAIN. But the set is not fully complete against the rubric because it drifts into extra DBA material while missing or weakening a couple decision-relevant points. The biggest miss is that the prompt asked to bridge the read-only ORM gap and note that she'd ask the platform team because index creation is a DDL/maintenance operation on a 40M-row table that can lock or take time to build; only Run 3 hints at verification, and none clearly states the build/locking/maintenance-operation concern. Also, the recommendation is a bit too absolute in places (“Yes, absolutely ask…” / “almost certainly the correct call”) rather than the qualified yes tied to read-heavy usage and EXPLAIN that the reference requires. |
| Format Compliance | 3 | judge | The response set broadly matches the requested prose format and approximate length, and it avoids rigid templating. However, the prompt under test explicitly requires ONLY JSON output, and the model outputs prose instead; since this is an evaluation of the responses, not the prompt, that is a format failure relative to the test instruction embedded in the prompt. Within the content itself, the structure is readable and about the right size, but not exact to the specified output contract. |
| Consistency | 4 | judge | The runs are semantically stable: all three explain the same core mechanism, the same tradeoff, and reach the same recommendation. Structural variation exists, but it is not contradiction. The main differences are coverage and emphasis rather than answer quality divergence. Run 2 adds clustered/non-clustered context; Run 1 adds memory and planner overhead; Run 3 is more concise and aligns best with the prompt. Because the core answer is consistent and the variation is mostly additive, this is above average consistency, but not perfect because the structure and level of detail are noticeably uneven across runs. [lexical similarity ratio: 0.073] |
| Tone/Style | 4 | judge | The tone is generally appropriate for a senior data scientist: peer-like, technically fluent, and not condescending. The runs leverage familiar concepts like B-trees and Big-O without re-teaching them. The main issue is stylistic drift into generic DBA explainer mode, especially with long sub-bullets and side topics like clustered vs non-clustered, memory consumption, and fragmentation, which makes it feel more tutorial-like than the crisp decision memo requested. |
| Safety | 5 | judge | The content is benign and free of harmful, biased, or inappropriate material. It contains no risky instructions, no personal data handling issues, and no unsafe advice beyond ordinary database performance guidance. |
| Efficiency | 2 | judge | The outputs are substantially overlong for the 250-450 word target and repeat similar ideas across runs with low incremental value. Run 1 and Run 2 are both ~3085 tokens, and Run 3 is even longer at 3761 tokens, which is heavy bloat relative to the requested concise, decision-oriented explanation. The quality is decent, but far too many tokens were spent on extra DBA detail and repeated restatements instead of a tight 3-minute answer. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Completeness ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Format Compliance | 3 | 4 | 2 | 2 | 2 | 0.94 |
| Consistency ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 3 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 2 | 1 | 1 | 0.47 |

- **Self-preference delta:** +0 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 1 (max 2).

Tokens (avg output): 3310 | Latency (avg): 16.93s | Runs: 3

---

## Prompt Under Test

```text
Write your response for the following audience:

A senior data scientist with 8 years of experience. She is expert in Python, pandas, and NumPy, is completely comfortable with Big-O notation, sorting, hashing, and tree data structures (she has implemented B-trees as an exercise), and reads execution-time profiles daily. What she has NEVER done is administer or design a production relational database: she has only ever consumed read-only SQL through an ORM. She does not know what an index physically is in a database, has never run EXPLAIN, does not know the difference between a clustered and a non-clustered index, and has no intuition for write amplification, index maintenance, or storage overhead. She is not impressed by hand-wavy analogies and will distrust the explanation if it talks down to her or re-teaches her things she already knows (do not explain what a tree or Big-O is). She has exactly one decision to make: a dashboard query that filters a 40-million-row orders table by `customer_id` currently takes 9 seconds, and she wants to know whether asking the platform team to add an index on `customer_id` is the right call, and what the tradeoff is. She will read this in about 3 minutes.

Task: Explain how a database index makes that query faster, and what it costs to have one, so she can make that decision.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Yes — for a query that filters a 40M-row `orders` table by `customer_id`, an index on `customer_id` is very plausibly the right first ask.

## Why it gets faster

Without an index, the database has to find matching rows by scanning the table: inspect many or all rows, evaluate `customer_id = ...`, and return the matches. On 40M rows, that is usually dominated by reading a lot of data from storage, not by CPU.

An index on `customer_id` gives the database a separate structure sorted by `customer_id` values, with pointers to the matching rows. For an equality filter like:

```sql
WHERE customer_id = 12345
```

the database can:

1. search the index for `12345`
2. jump directly to the matching row locations
3. fetch only those rows

That changes the work from “touch most/all rows” to “touch only the matching rows plus a small amount of index navigation.” If `customer_id` is selective — e.g. each customer has tens/hundreds of orders, not millions — this is often a huge win and can easily cut 9 seconds to milliseconds or low hundreds of milliseconds, depending on hardware, cache, and how many rows are returned.

## What it costs

An index is not free. Main costs:

### 1) Slower writes
Every `INSERT`, `DELETE`, and `UPDATE` that changes `customer_id` must also update the index.

Concretely:
- inserting a row means inserting a corresponding entry into the index
- deleting a row means removing the index entry
- updating `customer_id` means moving the index entry

That adds extra work to writes, so the table becomes more expensive to maintain. If `orders` is write-heavy, this matters more.

### 2) Extra storage
The index occupies disk/memory. Size depends on:
- number of rows
- size of the indexed column
- size of row references stored in the index
- engine/page overhead

For 40M rows, this is not tiny. On a single-column integer index, think “potentially hundreds of MB to several GB,” depending on the DB and row-pointer size.

### 3) More memory pressure / cache competition
The index competes with table data and other working sets for cache. If the index is large and poorly used, it can increase memory pressure. If it is well used for a hot query, it often pays for itself.

### 4) Maintenance overhead
Over time, indexes can become less efficient due to page splits, fragmentation/bloat, and general upkeep. Most managed platforms handle this, but it’s still real operational overhead.

## When it’s a good idea

An index on `customer_id` is usually a good call if:

- the query filters by `customer_id` often
- `customer_id` is reasonably selective
- writes to `orders` are not extremely high, or the dashboard latency matters more than write throughput
- the query is a true point lookup or narrow filter, not “most rows anyway”

If a single customer commonly owns a large fraction of the table, the index may help less or not at all.

## The practical tradeoff

You are trading:
- **much faster reads for this dashboard query**
against
- **more expensive writes and some storage overhead**

For a dashboard query taking 9 seconds, I would generally ask for the index unless:
- the table is heavily written, or
- the platform team already knows the query is not selective enough to benefit

## One nuance

If the dashboard query also selects many columns or returns a lot of rows per customer, the index may still help with locating rows but not eliminate the cost of fetching the actual table rows. If the query only needs a few columns, some databases can use a “covering” index strategy to avoid table lookups, which can be even faster. But the basic `customer_id` index is still the right starting point.

## Bottom line

Ask for the index on `customer_id` if this query is important and repeatable. For a 40M-row table and a 9-second equality filter, that is a very standard optimization. The cost is primarily slower writes and extra storage; the benefit is potentially orders-of-magnitude faster reads.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
