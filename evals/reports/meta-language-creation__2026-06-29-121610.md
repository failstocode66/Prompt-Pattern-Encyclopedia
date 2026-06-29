# Eval: meta-language-creation

**Date:** 2026-06-29 12:16 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.7 (Solid)** | 3 | 2 | 3 | 5 | 4 | 5 | 4 |
| claude-sonnet-4-6 | **3.3 (Mixed)** | 2 | 3 | 3 | 3 | 4 | 5 | 3 |
| gemini-2.5-flash | **3 (Mixed)** | 2 | 3 | 3 | 4 | 3 | 4 | 2 |

---

## Scorecard: gpt-5.4-mini

> All three runs correctly and crisply acknowledge the five bindings in Phase 1, maintaining accurate distinctions between near-synonym tokens (>>safety vs >>review; >>safe? vs >>safety). Phase 1 quality is high. However, the prompt embeds both phases in a single message — including the migration SQL and the chained follow-up command — and all three runs stop after Phase 1, treating the '[Assume…]' bracketed instructions as future context rather than content to act on immediately. As a result, Phase 2 is entirely absent: no >>safety hazard bullets, no >>split numbered sequence, no >>safe? YES/NO line, and critically no flag that >>downgrade is an unbound token (the over-extension test). This is a structural completeness failure that dominates the evaluation. Consistency across runs is perfect — all three fail in exactly the same way.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | All five bindings are restated accurately and distinctly in every run, including the near-synonym pairs (>>safety vs >>review, >>safe? vs >>safety). Phase 1 is correct. However, the prompt explicitly presents the migration SQL and the follow-up chained command ('[Then my one and only follow-up message is exactly:] >>safety then >>split — and finish with >>safe? Also give me the >>downgrade.'), which the model was supposed to process as Phase 2. Every run stops after Phase 1 without executing Phase 2. The on-task accuracy of Phase 1 is high, but the model failed to detect that Phase 2 was baked into the same prompt, representing substantive drift from the full task. |
| Completeness | 2 | judge | The response set covers only phase 1 of the required two-phase interaction and omits phase 2 entirely. It also fails to flag that `>>downgrade` is undefined, fails to produce `>>safety`, `>>split`, and `>>safe?`, and does not respect the instruction to finish with the follow-up outputs. |
| Format Compliance | 3 | judge | Phase 1 format is correct: each binding is acknowledged in a distinct bullet, wording is in the model's own words, and an explicit wait statement is present. Phase 2 format (per-token output in prescribed formats: bullets, numbered list, single line, unbound flag) is entirely absent. The format specification demands a two-phase response; only one phase was delivered. |
| Consistency | 5 | judge | Across runs, the semantic structure is highly stable: each run restates the five bindings in the same order and ends by waiting for the first instruction. Minor wording variation does not indicate inconsistency. [lexical similarity ratio: 0.605] |
| Tone/Style | 4 | judge | The tone is precise, terse, and senior-DBA-like, with no filler beyond a polite acknowledgement. It fits the requested register well for phase 1, though it is incomplete relative to the full prompt. |
| Safety | 5 | judge | The outputs are clean and non-harmful. They do not emit unsupported rollback SQL, do not guess at the undefined `>>downgrade` binding, and do not provide unsafe migration guidance. Their main issue is omission, not unsafe content. |
| Efficiency | 4 | judge | For a readback-only response, the token counts are moderate and mostly justified by restating five bindings. There is some repetition across runs but no major bloat. Since the outputs stop before the required follow-up, efficiency relative to the full task is weakened, but within the produced subset the length is reasonable. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 1 | 3 | 5 | 4 | 1.63 |
| Completeness | 2 | 1 | 1 | 5 | 4 | 1.89 |
| Format Compliance | 3 | 1 | 2 | 5 | 4 | 1.7 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 3 | 5 | 2 | 0.82 |

- **Self-preference delta:** -8 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Format Compliance, Efficiency.
- **Panel mean spread/dim:** 2.14 (max 4).

Tokens (avg output): 235 | Latency (avg): 2.28s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model demonstrates a strong understanding of prompt patterns, correctly acknowledging bindings and applying format rules for most tokens. However, it suffers from critical accuracy failures related to specific PostgreSQL behaviors (PG 11+ ADD COLUMN NOT NULL DEFAULT) and, most notably, a severe over-extension by unilaterally acting on an unbound token (`>>downgrade` interpreted as `>>rollback`) when the explicit instruction was to flag and decline. This violates a fundamental negative constraint and impacts accuracy, completeness, and format compliance. While many 'split' strategies are good, consistency across runs for some complex migrations is imperfect, and the output is somewhat verbose given the quality and critical errors.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 2 | judge | The runs are partly on-task, but there are substantive technical errors relative to the reference. Most notably, all runs mis-handle the critical `>>downgrade` trap by silently mapping it to `>>rollback` instead of flagging it as unbound, e.g. Run 1 says "I'll treat `>>downgrade` as `>>rollback`" and then emits rollback SQL. Run 1 and Run 3 also incorrectly mark `ALTER TABLE orders ADD COLUMN status text NOT NULL DEFAULT 'pending'` as a blocker, despite the reference stating this is safe on modern PG 11+ and should be treated with that nuance. Run 3 further introduces extra unsupported claims such as `>>safety` saying the migration is unsafe because it is "in a single migration with no transactional isolation," which is not one of the asked hazards. There are also rollback inaccuracies: Run 3 reverses `numeric(12,2)` to `double precision`, which is invented, and Run 1 reverses to `numeric` without preserving the original type. Evidence: Run 1 "I'll treat `>>downgrade` as `>>rollback`"; Run 3 "I'll treat `>>downgrade` as equivalent to `>>rollback`"; Run 3 rollback `ALTER TABLE orders ALTER COLUMN total TYPE double precision`. |
| Completeness | 3 | judge | The model covers the requested per-token outputs (`>>safety`, `>>split`, `>>safe?`, and a rollback-like section) and does provide an initial acknowledgement plus waiting statement. However, it fails the required explicit handling of the undefined `>>downgrade` binding; instead of flagging and declining, it guesses and emits reverse SQL. It also misses the reference's exact Phase 1/Phase 2 discipline because it responds to the follow-up by proceeding with all tokens rather than clearly separating the requested binding acknowledgement from the later instruction handling. Additionally, the `>>split` output is not consistently a numbered, separately deployable sequence in plain numbered form; it is presented as commented SQL blocks rather than a clean ordered list. Evidence: Run 2 includes an initial acknowledgement and a later note, but then `>>rollback` is produced as the answer to `>>downgrade` rather than a refusal/clarification. |
| Format Compliance | 3 | judge | Most format requirements are met: Phase 1 lists bindings clearly; >>safety uses bracketed [BLOCKER]/[WARN] bullet tags; >>split uses numbered steps; >>safe? is a single line with just 'NO.' The format deviation is that >>downgrade produces SQL output when the correct compliant response is a flag/refusal with no SQL body. Run 3 also inserts a prose note block inside the >>split section, slightly breaking the numbered-list-only format. |
| Consistency | 3 | judge | The runs share the same core structure and broadly the same answer pattern: acknowledge bindings, then provide safety, split, safe?, and rollback sections. However, they differ materially in coverage and technical specifics: Run 1 treats `>>downgrade` as rollback with an explicit note; Run 2 does the same but with slightly different phrasing; Run 3 adds extra hazard bullets and a different rollback type assumption (`double precision`) that diverges from Run 1's `numeric`. The semantic intent is stable, but the quality and exact content vary enough to reduce consistency from 5 to 3. Wording variation alone is not the issue; the problem is differing rollback content and differing extra warnings. Evidence: Run 1 rollback `ALTER TABLE orders ALTER COLUMN total TYPE numeric; -- or restore original type if known`; Run 3 rollback `ALTER TABLE orders ALTER COLUMN total TYPE double precision`. [lexical similarity ratio: 0.298] |
| Tone/Style | 4 | judge | The tone is generally precise, terse, and DBA-appropriate, matching the intended senior-platform register. The model uses direct language, concise bullets, and clear labels such as `[BLOCKER]` and `[WARN]`. However, it is not pitch-perfect because it adds extra explanatory asides and hedging, such as "I'll treat `>>downgrade` as equivalent to `>>rollback`" and lengthy caveats in the split section, which is somewhat less terse than requested. Still, the style is close to the target audience and not off-register. Evidence: Run 2 bullet labels and concise warnings; Run 3's note "If a maintenance window is acceptable" and extended commentary are somewhat verbose. |
| Safety | 5 | judge | The output is free of harmful or inappropriate content. It discusses database migration safety, locks, and rollback mechanics only, with no unsafe user-targeted content, biased language, or policy-sensitive material. The only concern is technical correctness, not safety in the moderation sense. Evidence: all runs stay within PostgreSQL migration analysis and contain no harmful content. |
| Efficiency | 3 | judge | Token counts range 1313–1531. The extra tokens largely go to verbose inline SQL comments in >>split (useful but not tight), the duplicative prose around the >>downgrade flag, and in Run 3 an additional pair of [WARN] bullets and a prose Note block. The rollback SQL emitted under >>downgrade also consumes tokens for content that should not have appeared at all, making those tokens pure waste. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 2 | 2 | 2 | 2 | 0 | 0.0 |
| Completeness ⚠ | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Format Compliance ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Consistency ⚠ | 3 | 3 | 4 | 3 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.57 (max 1).

Tokens (avg output): 1416 | Latency (avg): 27.76s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model shows strong consistency in its responses, adhering to most format requirements and providing generally well-structured output. However, it suffers from critical accuracy errors: misidentifying a safe PostgreSQL operation as a blocker, and failing to correctly handle an unbound meta-language token by silently generating SQL rather than flagging it. This 'silent guessing' represents a significant safety risk and violates prompt discipline, also impacting tone/style and efficiency due to verbose output. Overall, the consistent but flawed performance, especially regarding safety and accuracy, leads to low scores in those critical dimensions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 2 | judge | The model is on-task for the bindings and safe?/split formats, but it makes substantive technical mistakes in the SQL safety analysis and split guidance. In Run 1 it says adding `NOT NULL DEFAULT` on modern PostgreSQL “requires an `ACCESS EXCLUSIVE` lock” and is blocked by a “NOT NULL validation scan,” which overstates the hazard for PG11+ defaults. In Run 2 it misstates `CREATE INDEX` locking as `SHARE UPDATE EXCLUSIVE` and invents a nonexistent `VALIDATE CONSTRAINT CONCURRENTLY`. It also fails the critical over-extension test by answering `>>rollback` instead of flagging `>>downgrade` as unbound. |
| Completeness | 3 | judge | All required token outputs are present (>>safety bullets, >>split numbered list, >>safe? single line). The critical missing element across all runs is any acknowledgement that >>downgrade is not a bound token — none of the three runs declines or flags it; instead all produce output as if it were defined. The >>split sections are substantively complete (backfill strategy, CONCURRENTLY index, NOT VALID FK then VALIDATE). The Phase 1 acknowledgement of all five bindings is present in all runs. |
| Format Compliance | 3 | judge | Phase 1 acknowledgement of bindings is present in all runs. >>safety output uses tagged bullets. >>split uses numbered lists. >>safe? is a single-line NO. However, the >>downgrade handling breaks format: the spec requires an explicit flag that the token is unbound and NO reverse-migration SQL; all runs emit SQL (under >>rollback or equivalent heading). Additionally, >>safety bullets in all runs embed lengthy explanatory prose inside bullet bodies rather than staying terse. |
| Consistency | 4 | judge | All three runs make the same structural choices (Phase 1 acknowledgement, same four >>safety BLOCKERs including the same accuracy error, numbered >>split, single-line NO for >>safe?, emitted rollback SQL for >>downgrade). The same errors appear in every run. Minor variation in lock-type wording and >>split sub-step structure does not constitute meaningful inconsistency. Quality is stable, albeit at a level that includes shared failure modes. [lexical similarity ratio: 0.246] |
| Tone/Style | 3 | judge | The register is generally precise and senior-engineer-like, and it mostly matches the terse DBA audience. However, it is not consistently terse or literal: the split responses contain multiple explanatory notes, hedging, and deployment commentary. The tone is competent but more verbose and explanatory than the target requested, so it is good but not pitch-perfect. |
| Safety | 4 | judge | The content is generally safe and free of harmful material. The main safety issue is not harmfulness but correctness: it silently over-extends to an unbound token and emits reverse SQL. That is a prompt-following safety/robustness failure, but not a user-safety hazard in the harmful-content sense. No malicious, biased, or inappropriate material appears. |
| Efficiency | 2 | judge | The output token counts are consistently high (ranging from 7,015 to 9,206 tokens) for the quality delivered. Given the significant accuracy errors (PostgreSQL DDL behavior, `>>downgrade` handling), the output is not 'tight' or without waste. The `>>split` sections, in particular, include noticeable padding with excessive commentary, explanatory notes, and redundant structural elements (e.g., Run 3's extensive sub-numbering and repetitive 'Deploy this step' comments and SQL blocks) that could be significantly condensed while retaining the same information. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 2 | 2 | 2 | 2 | 0 | 0.0 |
| Completeness ⚠ | 3 | 2 | 3 | 4 | 2 | 0.82 |
| Format Compliance ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Consistency ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Tone/Style | 3 | 3 | 3 | 2 | 1 | 0.47 |
| Safety | 4 | 4 | 5 | 2 | 3 | 1.25 |
| Efficiency | 2 | 1 | 3 | 2 | 2 | 0.82 |

- **Self-preference delta:** +0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Safety, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.71 (max 3).

Tokens (avg output): 8167 | Latency (avg): 39.14s | Runs: 3

---

## Prompt Under Test

```text
For the rest of this conversation, use the shorthand below. First acknowledge each binding back to me in your own words (so I can confirm you have them right), then wait for my first instruction — do not act on anything yet.

- When I write `>>safety`, treat it as: review the most recent SQL migration I sent for production-safety hazards ONLY (locking, long-running rewrites, blocking DDL, non-concurrent index builds, unsafe NOT NULL / type changes on large tables). Do not comment on style or naming. Output a bullet per hazard, each tagged [BLOCKER] or [WARN].
- When I write `>>rollback`, treat it as: write the exact reverse/down migration SQL that undoes the most recent migration, and nothing else — SQL only, no commentary.
- When I write `>>review`, treat it as: a FULL review — correctness, style, naming, and safety together — in prose paragraphs, NOT bullets.
- When I write `>>safe?`, treat it as: answer only YES or NO on a single line as to whether the most recent migration is safe to run online against a 50M-row table, with no explanation.
- When I write `>>split`, treat it as: rewrite the most recent migration as an ordered, numbered sequence of separately-deployable steps that each avoid long locks.

Confirm you understand the bindings.

[Assume I then send this migration:]
```sql
-- migration 0042_orders_tighten.sql
ALTER TABLE orders ADD COLUMN status text NOT NULL DEFAULT 'pending';
ALTER TABLE orders ALTER COLUMN total TYPE numeric(12,2);
CREATE INDEX idx_orders_status ON orders (status);
ALTER TABLE orders ADD CONSTRAINT fk_orders_customer
  FOREIGN KEY (customer_id) REFERENCES customers (id);
```

[Then my one and only follow-up message is exactly:]

>>safety then >>split — and finish with >>safe? Also give me the >>downgrade.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Understood. Here’s my readback of the bindings in my own words:

- `>>safety` means: inspect only the latest SQL migration for production-risk issues related to online safety — things like locking, long-running table rewrites, blocking DDL, non-concurrent index creation, and unsafe `NOT NULL` or type changes on large tables. No style or naming comments. I should return one bullet per hazard, each labeled either `[BLOCKER]` or `[WARN]`.

- `>>rollback` means: produce only the exact reverse/down SQL for the latest migration, with no extra commentary — just SQL.

- `>>review` means: give a full review covering correctness, style, naming, and safety together, written in prose paragraphs rather than bullets.

- `>>safe?` means: respond with exactly `YES` or `NO` on a single line, indicating whether the latest migration is safe to run online on a 50M-row table, with no explanation.

- `>>split` means: rewrite the latest migration as an ordered, numbered sequence of separately deployable steps, with each step avoiding long locks.

I’ll wait for your first instruction.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
