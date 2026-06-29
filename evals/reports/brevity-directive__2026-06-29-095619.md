# Eval: brevity-directive

**Date:** 2026-06-29 09:56 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.3 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 4 |
| claude-sonnet-4-6 | **3.7 (Solid)** | 3 | 2 | 4 | 4 | 5 | 5 | 3 |
| gemini-2.5-flash | **3.4 (Mixed)** | 4 | 3 | 3 | 3 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> The model reliably delivers the correct No verdict with the key exclusive-lock/rewrite reason and stays within the 30-word ceiling across all three runs — a solid brevity-directive execution. The critical gap is the complete omission of the disk-space trap (VACUUM FULL requires free disk equal to table size, a double hazard on an already-low-disk host). The plain-VACUUM recommendation is partially qualified but not stated cleanly enough to avoid the false-completeness flaw. pg_repack coverage is inconsistent (absent from Run 1). Tone is mostly appropriate with minor hedging ('usually,' 'risk'). Overall: competent but not strong — the word budget left room for the load-bearing fact that was dropped.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs are on-task and factually mostly correct: they say not to run VACUUM FULL during business hours, mention the exclusive/blocking lock, and propose alternatives. The main accuracy miss is recommending plain/regular VACUUM as if it addresses the space problem; it only makes space reusable, not returned to the OS, which the reference calls out as a key distinction. Run 1 also weakens precision by saying "reclaiming disk space to the OS usually requires maintenance or table rewrite" without naming the safe online alternative as clearly as requested. |
| Completeness | 4 | judge | The responses cover the verdict and the load-bearing lock caveat, and they mention at least one safe alternative in each run. However, they do not fully satisfy the reference because they omit the ideal disk-space detail that VACUUM FULL needs free disk roughly equal to table size. They also overuse plain/regular VACUUM as the primary suggestion without clarifying its limited space-reclamation behavior. |
| Format Compliance | 4 | judge | All three runs are within the 30-word ceiling (28, 23, 25 words respectively), lead with the verdict, include no preamble or greeting, and follow verdict-reason-alternative structure. Run 2 uses backtick code formatting, a minor deviation from 'plain prose' but not a structural violation. |
| Consistency | 4 | judge | The runs are semantically stable and structurally similar: each begins with "No," explains that VACUUM FULL takes an exclusive lock / rewrites the table, and recommends VACUUM or pg_repack. There is some variation in coverage and wording, but no contradiction or major divergence in meaning. [lexical similarity ratio: 0.572] |
| Tone/Style | 5 | judge | The tone is appropriately terse, decisive, and ops-oriented for an engineer making a production decision. The answers use a direct verdict first and avoid hedging or conversational filler. |
| Safety | 5 | judge | The outputs are safe and do not contain harmful, biased, or inappropriate content. They also appropriately discourage an outage-prone action during business hours on a production primary. |
| Efficiency | 4 | judge | Token counts (42, 49, 43) are low relative to the 30-word limit. Word budgets are not wasted on preamble or filler. However, some words in Runs 1 and 3 go to the less-informative 'usually requires maintenance' phrase rather than the higher-value disk-space trap or a cleaner pg_repack recommendation. Room existed within the ceiling to add the critical missing fact. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Completeness | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Format Compliance | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Consistency | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 2 | 4 | 5 | 3 | 1.25 |

- **Self-preference delta:** -5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Format Compliance, Efficiency.
- **Panel mean spread/dim:** 1.71 (max 3).

Tokens (avg output): 45 | Latency (avg): 1.38s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model performs very well on format compliance, tone, and safety, strictly adhering to the brevity directive and providing a crucial safety warning about `VACUUM FULL`. However, its accuracy and completeness are significantly compromised by failing to recommend `pg_repack` as the appropriate online solution for reclaiming disk space to the OS. Instead, it suggests `regular VACUUM`, which only reclaims space internally, and this distinction is inconsistently handled across runs, impacting overall quality and efficiency in using the limited token budget for the most effective advice.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Generally relevant and mostly correct, but it misses a key operational nuance: the prompt asked about getting disk space back, and Run 2 is factually misleading with "regular VACUUM first (returns space to PostgreSQL)." The outputs also omit the access-exlusive-table-rewrite/free-disk caveat that the reference considers load-bearing. |
| Completeness | 2 | judge | The responses answer no and mention a safer alternative, but they fail to include the essential reason beyond a generic lock warning, and they do not mention pg_repack or the free-disk requirement. They also miss the precise distinction that plain VACUUM reuses space rather than returning it to the OS, except for Run 2 which states an inaccurate version of it. |
| Format Compliance | 4 | judge | All three runs are within the 30-word hard ceiling (Run 1: ~28 words, Run 2: ~26, Run 3: ~25). None open with preamble, greeting, or throat-clearing. All lead with the direct verdict. No trailing offers to elaborate. Format requirements are fully satisfied. |
| Consistency | 4 | judge | The runs are semantically stable: all say no, all warn of blocking reads/writes, and all recommend either regular VACUUM or a maintenance-window VACUUM FULL. Differences are mainly wording and one mild factual slip in Run 2, not contradictory structure or intent. [lexical similarity ratio: 0.871] |
| Tone/Style | 5 | judge | Register is consistently terse and decisive, exactly matching the senior-DBA / on-call ops audience. No hedging, no filler, no softening language. The imperative constructions ('Run regular VACUUM', 'schedule VACUUM FULL') are appropriate for an engineer needing a fast go/no-go. |
| Safety | 5 | judge | The content is safe: no harmful, biased, or inappropriate material. It offers operational database advice without introducing unsafe general content. |
| Efficiency | 3 | judge | The word counts are admirably tight (25–28 words), but the budget is partly spent on the wrong alternative (plain VACUUM) rather than on pg_repack — the one fact that would actually solve the user's disk problem safely. The scarce word allowance is used efficiently in prose density but directed toward content that partially misses the mark, yielding less value per word than optimal. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Completeness | 2 | 2 | 2 | 2 | 0 | 0.0 |
| Format Compliance ⚠ | 4 | 2 | 5 | 5 | 3 | 1.41 |
| Consistency ⚠ | 4 | 4 | 5 | 3 | 2 | 0.82 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 43 | Latency (avg): 2.29s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Overall, the model is directionally correct and safely advises against VACUUM FULL, but it is incomplete relative to the prompt’s preferred load-bearing caveat-plus-alternative pattern, and it inconsistently includes the safe alternative or disk-space warning across runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Typical answers are on-task and factually mostly correct about VACUUM FULL being disruptive and lock-blocking, but they omit the safe alternative emphasis in the strongest form and one run overstates the lock as "exclusive" rather than specifically ACCESS EXCLUSIVE. Run 2 is strongest: "It takes an `ACCESS EXCLUSIVE` lock, blocking all table operations for an extended time. It also temporarily requires double the disk space". Run 1 adds a recommendation but weakly: "Consider `pg_repack` or off-hours." |
| Completeness | 3 | judge | The core no-go reasoning is present, but the response set misses or underdevelops important parts of the prompt across runs: the plain-VACUUM/autovacuum alternative is not mentioned, and the load-bearing distinction that plain VACUUM does not return space to the OS is absent. Only Run 1 mentions pg_repack, and none mention autovacuum or plain VACUUM reclaim/reuse. Also, the prompt asked for a direct verdict plus reason and alternative within 30 words; Run 2 and 3 omit the alternative entirely. |
| Format Compliance | 3 | judge | The outputs follow plain prose and are direct, but they violate the hard 30-word ceiling in all three runs, which is a major format failure. Run 1 is 24 words, Run 3 is 24 words, but Run 2 is 25 words? Actually the visible text is under 30 words; however it still fails the requested exact brevity objective by adding filler like "for an extended time" and "temporarily" rather than the minimal load-bearing phrasing. Since the prompt's hard ceiling is the main issue, the set only partially complies overall, with Run 1 and 3 closer than Run 2. |
| Consistency | 3 | judge | The core verdict (No + exclusive lock blocks operations) is stable across all runs, which is the minimum expected. However, coverage diverges meaningfully: pg_repack appears only in Run 1, the disk-doubling trap only in Run 2, and Run 3 offers no safe alternative at all. Lock precision also varies (ACCESS EXCLUSIVE in Run 2 vs. generic 'exclusive lock' in Runs 1 and 3). These are not mere wording variations — they represent substantively different information delivered to the user across runs. [lexical similarity ratio: 0.326] |
| Tone/Style | 4 | judge | The tone is appropriately terse, decisive, and operationally oriented for a senior DBA/on-call audience. However, the phrasing is somewhat generic and wordy rather than perfectly sharp, especially in Run 1 and Run 3 with extra evaluative language like "highly disruptive" and "significant production downtime." |
| Safety | 5 | judge | The responses are safe, non-abusive, and operationally focused. They correctly warn against an action that could disrupt production and do not introduce harmful or inappropriate content. |
| Efficiency | 2 | judge | The visible text output is concise (27-29 words), but the token budgets are dramatically inconsistent: 384, 483, and 1115 output tokens for nearly identical text quality. Run 2 spends 1115 tokens — nearly 3x Run 3 — and while it yields the disk-doubling fact, the ratio of tokens to useful output is very poor. The model is spending large internal compute on short answers, and the incremental information gain from Run 2's extra ~730 tokens is a single clause. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Completeness | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Format Compliance | 3 | 2 | 5 | 2 | 3 | 1.41 |
| Consistency | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 3 | 2 | 1 | 2 | 0.82 |

- **Self-preference delta:** -2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance, Efficiency.
- **Panel mean spread/dim:** 1 (max 3).

Tokens (avg output): 661 | Latency (avg): 5.35s | Runs: 3

---

## Prompt Under Test

```text
Answer in 30 words or fewer. No preamble.

We're low on disk on our production Postgres primary. One table has a lot of dead tuples after a big delete. Should we run VACUUM FULL on it during business hours to get the space back?
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
No. VACUUM FULL rewrites and locks the table exclusively, causing downtime risk. Use regular VACUUM now; reclaiming disk space to the OS usually requires maintenance or table rewrite.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
