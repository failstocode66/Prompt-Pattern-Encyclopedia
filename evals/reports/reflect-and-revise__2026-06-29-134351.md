# Eval: reflect-and-revise

**Date:** 2026-06-29 13:43 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.1 (Solid)** | 4 | 3 | 5 | 4 | 4 | 5 | 4 |
| claude-sonnet-4-6 | **3.3 (Mixed)** | 3 | 3 | 3 | 3 | 4 | 4 | 3 |
| gemini-2.5-flash | **2.7 (Mixed)** | 3 | 2 | 4 | 2 | 3 | 3 | 2 |

---

## Scorecard: gpt-5.4-mini

> Overall strong, mostly on-task responses with solid handling of the key rollback hazard. The set is consistent and correctly structured, but not perfect: some revisions are a bit generic, and the strongest reference-level requirements like explicit snapshot/pre-rollback safeguards and very crisp code-vs-schema ordering are not uniformly or fully expressed.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are largely on-task and technically sound: each revision addresses the core rollback problem with code revert plus schema handling, and Run 1/2/3 all correctly note the dropped-column risk. However, none is fully perfect because some guidance remains too generic or slightly incomplete for the exact runbook scenario; for example Run 1 says "If it is not, you must restore the dropped column shape before traffic is fully shifted back" but does not state the exact safe order with the clarity of the reference, and Run 2’s "restore it from backups, replica lagged copy, or application logs if available" is not a robustly correct recovery path in all cases. |
| Completeness | 3 | judge | The output set covers most required elements: all three phases are present, Phase 2 has 3-5 items, and Phase 3 is sequential and self-contained. The revisions also include schema compatibility checks, monitoring, and comms. Still, the strong reference expects a few specific substantive elements that are not always fully nailed: explicit backup/snapshot before any destructive DB action is absent or only indirectly implied in some runs, and the safe code-vs-schema ordering is present but not always explicit enough as a standalone decision rule. Run 3 also underdelivers on the requested ~300-450 word constraint in the revision. |
| Format Compliance | 5 | judge | The response set follows the required three labeled phases in order, with Phase 2 as a 3-5 item list and Phase 3 as a numbered/sequential procedure. The labels are distinct and not merged. The final-answer JSON-only wrapper requirement is also followed in this evaluation response context, but judging the model outputs themselves, their structure matches the prompt requirements well. |
| Consistency | 4 | judge | The runs are semantically consistent: all three identify the same core failure mode (schema rollback risk after dropped-column migration) and revise toward app-first rollback with schema compatibility checks and verification. They differ somewhat in emphasis and coverage, but not in contradiction. Because structural quality and exact safeguards vary slightly across runs, this is not a 5. [lexical similarity ratio: 0.037] |
| Tone/Style | 4 | judge | The tone is generally operational, technical, calm, and directive, which fits the on-call runbook audience. Imperatives like "Announce," "Use," "Confirm," and "Pause" are appropriate. It is not a perfect 5 because some lines are a bit explanatory or policy-like rather than pure pressure-ready procedure, and some critique phrasing is somewhat meta rather than candidly self-critical. |
| Safety | 5 | judge | The outputs are safe: they advise against risky blind schema downgrades, recommend pausing changes, and avoid harmful or inappropriate content. The guidance is operationally cautious rather than dangerous. |
| Efficiency | 4 | judge | The outputs deliver decent quality, but they are wordy relative to the task’s roughly 300-450 word target for the revision. Each run’s Phase 3 is around the right scale or a bit over/under, but the full response set includes a long Phase 1 draft and a lengthy Phase 2 critique, which is expected by the prompt yet still somewhat padded. The quality is good, so this is only a moderate efficiency penalty rather than severe bloat. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Completeness ⚠ | 3 | 4 | 2 | 4 | 2 | 0.94 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 3 | 5 | 2 | 0.94 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.29 (max 2).

Tokens (avg output): 1248 | Latency (avg): 9.87s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The three runs demonstrate competent reflect-and-revise execution in structure — three distinct phases, candid self-critique lists, and materially improved Phase 3 revisions — but share a critical blind spot: none of the Phase 2 critiques explicitly names the most important technical defect required by the rubric, namely that the dropped column's DATA is permanently gone and that a naive down-migration is unsafe or impossible. This omission propagates to Phase 3, where all revisions treat re-adding the column as a viable path without sufficiently foregrounding irreversible data loss or the roll-forward alternative. Additional consistent gaps across all runs: no pre-rollback backup/snapshot step, no CI pipeline freeze instruction, and weak treatment of the roll-forward vs rollback decision when the migration is destructive. Run 2 is the strongest overall for safety (transaction wrapper, lock_timeout, explicit data-loss warning in Phase 3, time-boxed escalation), but its Phase 2 still doesn't name data permanence as a critique item. Run 1 is uniquely correct in prescribing schema-fix-before-code-revert, while Runs 2 and 3 recommend the opposite order — a substantive operational inconsistency. Format compliance is high across all three runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | All three runs are broadly technically correct but consistently miss naming the most critical defect in Phase 2: that the dropped column's DATA is permanently gone and a down-migration cannot restore it. Run 2 Phase 1 and Phase 3 do state 'The data is gone,' but Phase 2 never critiques the draft for omitting this warning. Run 1 Phase 2 and Run 3 Phase 2 do not mention data permanence at all. Ordering advice also diverges: Run 1 Phase 3 correctly prescribes schema-fix-before-code-revert, while Runs 2 and 3 Phase 3 revert code first then fix schema—a substantive technical disagreement. Technical content within each step is generally sound. |
| Completeness | 3 | judge | The responses cover several required elements—draft, critique, revision, rollback steps, and some verification—but across runs the critique/revision often miss one or more mandated fixes from the prompt: explicit safe ordering of code-vs-schema, the destructive-column decision path, pre-rollback snapshot, incident comms, pipeline freeze, and a standalone 300-450 word revision. Run 2 is the closest to the requested content, but still lacks the pre-rollback snapshot/pipeline freeze and the revision is more than a concise runbook. Run 3 especially falls short by focusing on schema compatibility detection rather than the required destructive-data handling and operational safeguards. |
| Format Compliance | 3 | judge | The overall three-phase structure is present in all runs, and phases are clearly labeled, but the output does not reliably conform to the exact specification. The prompt demanded Phase 2 be 3 to 5 items with concrete defect-and-fix pairs, and Phase 3 be a standalone numbered/sequential procedure roughly 300-450 words. Run 2 and Run 3 are close, while Run 1’s revision is shorter and less clearly within the intended word budget. Across the set, the phases are separate, but formatting deviations and extra prose/markup are common. |
| Consistency | 3 | judge | The runs are semantically related and all attempt the same pattern, but they diverge materially in structure and quality. Run 1 prioritizes restoring the dropped column before code rollback; Run 2 prioritizes app rollback followed by schema reverse with an explicit transaction; Run 3 adds a branchy path A/path B compatibility approach. These are not merely wording differences—they change the operational plan and the nature of the fix, so the set is only moderately consistent. The core theme remains rollback with schema consideration, which keeps this from being a low score. [lexical similarity ratio: 0.057] |
| Tone/Style | 4 | judge | The tone is generally operational, technical, and directive, which matches the audience reasonably well. Run 2 and Run 3 especially read like incident runbooks with imperative steps and caution blocks. That said, some phrasing is still a bit generic or advisory rather than fully pressure-ready, and some items sound tentative instead of authoritative. No run is obviously the wrong register. |
| Safety | 4 | judge | The content is largely safe and appropriate for an operational rollback procedure, with no harmful instructions beyond normal production DB changes. The main safety concern is that some runs propose risky or oversimplified database actions without sufficient guardrails—e.g., re-adding dropped columns, dropping columns, or wrapping complex DDL in a transaction as though it were universally safe. Still, the outputs do include some cautions and escalation points, so this is not a major safety failure. |
| Efficiency | 3 | judge | Token counts are 1707, 1820, and 1648 across runs. Given the three-phase structure and the technical depth required, baseline verbosity is justified. However, all three Phase 1 drafts contain procedural prose that telegraphs future critique items without resolving them, functioning more as filler than deliverable content. Phase 2 items in all runs include at least one or two lower-stakes entries (kubectl placeholder names in Run 1; vague pipeline UI in Run 2; buried warning placement in Run 3) that consume tokens for weak critique value. Phase 3 revisions are the most token-efficient portion of each run. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 2 | 3 | 4 | 2 | 0.82 |
| Completeness | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Format Compliance ⚠ | 3 | 3 | 4 | 3 | 1 | 0.47 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 1725 | Latency (avg): 36.72s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs exhibit the canonical self-flattery failure mode of the reflect-and-revise pattern. Phase 2 critiques consistently identify only cosmetic defects — placeholder genericity, restart vagueness, word count — while completely ignoring the six technically-critical flaws the evaluation context requires: irreversibility of the dropped column's data loss, unsafe code/schema rollback ordering, old-code backward compatibility with the new schema, absence of a pre-rollback snapshot, pipeline freeze, and roll-forward as the safer path for destructive migrations. Because Phase 2 never surfaces these defects, Phase 3 revisions are cosmetically polished rewrites rather than materially safer runbooks. Run 1 introduces an additional regression: SQL that populates old_col from new_col 'assuming direct data mapping', misleadingly implying the lost data is recoverable. No run advises taking a database backup before any DDL, declares a pipeline freeze, or acknowledges that a destructive migration makes roll-forward preferable to roll-back. The pattern's core purpose — using structured self-critique to close real gaps — is not demonstrated in any run.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The responses are on-task in that they discuss rollback, but the core technical handling of the destructive schema change is materially wrong or unsafe. Across runs, Phase 3 often implies re-adding the dropped column from scratch without acknowledging that the lost data cannot be recovered from the migration alone. In Run 1, the revision even says to "UPDATE <your_table_name> SET old_col = new_col;" and "If old_col was originally NOT NULL, restore this constraint," which presumes safe recoverability. Run 3 explicitly states "The newly added `NOT NULL` column (`new_column`) will be ignored by the old code and does no harm by existing," which is not the key issue when the old column was dropped and data may be lost. The outputs are relevant, but technically incomplete around the hardest part. |
| Completeness | 2 | judge | The format requirements are mostly met, and the outputs include three phases, a critique, and a revision. However, the revision does not fully close the substantive gaps required by the prompt: explicit safe ordering of code-vs-schema steps is only partially addressed, the irrecoverability of the dropped column's data and the resulting decision (prefer roll-forward or restore from backup) is missing, pre-rollback snapshot/backups are absent, and incident comms/pipeline freeze are not consistently included. The revision is therefore not a complete fulfillment of the intended rollback runbook specification. |
| Format Compliance | 4 | judge | All three runs use the required three labeled phases in order, and Phase 2 is a 3-to-5 item list, while Phase 3 is a numbered procedure. Run 1 and Run 3 include the requested phase labels clearly. The main deviations are that Phase 3 in some runs exceeds or drifts from the requested content constraints, and Run 3 adds extra heading clutter before the actual phases, but the overall shape is close to spec rather than broken. |
| Consistency | 2 | judge | The runs share the same broad structure and intent, but they differ materially in how they handle the rollback, especially the database portion. Run 1 attempts to reconstruct the dropped column from the new column with direct SQL; Run 2 treats the DB change as a possible manual re-add and explicitly warns against dropping the new column; Run 3 prescribes creating a temporary migration and emphasizes that the new column can remain. These are not just wording differences; they reflect different operational strategies and quality levels. The core answer is similar, but semantic and procedural consistency is only moderate. [lexical similarity ratio: 0.035] |
| Tone/Style | 3 | judge | The tone is generally operational and technical, but it is not consistently pitch-perfect for an on-call under-pressure runbook. Some phrasing is polished and directive, yet many steps are still generic or explanatory rather than crisp imperatives. In Run 1, the revision uses narrative transitions like "This procedure outlines" and "If the 500-error rates subside to normal levels," which is acceptable but a bit soft. Run 3 is closer with direct commands, but also includes explanatory commentary and awkward phrasing such as "does no harm by existing," which is less than ideal for calm directive runbook prose. |
| Safety | 3 | judge | The outputs are not overtly harmful, but there are some questionable operational instructions. Run 1 proposes directly updating production schema with ad hoc SQL and even reconstructing data from a new column as if that were a generally safe rollback path. Run 3 instructs creating and applying a temporary migration in production, which is operationally plausible but still risky without the missing safeguards. There is no malicious content, but the safety posture is only moderate because the guidance downplays irrecoverable data-loss risk and omits snapshot/restore safeguards. |
| Efficiency | 2 | judge | The outputs are bloated relative to the quality delivered. Run 1 is especially verbose at 6924 tokens, with large amounts of generic explanation and placeholder-heavy SQL that do not improve the core answer. Run 3 is also lengthy and includes duplicated headings and extensive explanatory text. Given the task asked for a roughly 300-450 word revision focused on actionable rollback steps, the token usage is inefficient for the delivered substance. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 2 | 2 | 4 | 2 | 0.94 |
| Completeness ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Format Compliance | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Consistency | 2 | 2 | 4 | 1 | 3 | 1.25 |
| Tone/Style ⚠ | 3 | 3 | 3 | 4 | 1 | 0.47 |
| Safety ⚠ | 3 | 3 | 2 | 3 | 1 | 0.47 |
| Efficiency | 2 | 2 | 2 | 2 | 0 | 0.0 |

- **Self-preference delta:** +1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 5680 | Latency (avg): 28.13s | Runs: 3

---

## Prompt Under Test

```text
Produce your response in three labeled phases. Do not skip or merge phases.

Phase 1 - Draft: Write your initial answer.

Phase 2 - Critique: List 3 to 5 specific weaknesses in your draft. Be concrete. Each item must name exactly what is wrong (quote or point to the part of the draft) and state what would fix it. Vague critiques such as "could be clearer" or "add more detail" are not allowed; a critique that names no concrete defect should not be listed.

Phase 3 - Revision: Rewrite the full answer, addressing every weakness you listed in Phase 2. The revision must stand alone as a complete deliverable (do not write "as above" or reference the draft).

Task: Write the "Rollback Procedure" section of a production runbook for the following situation. A backend team deploys to a single Postgres-backed service roughly daily via a CI pipeline. A deploy that included a forward database schema migration (it added a NOT NULL column with a default, backfilled it, and dropped an old column) has caused elevated 500-error rates in production, and the on-call engineer has decided to roll back. Write the rollback section the on-call engineer will follow under pressure: it should cover both reverting the application code and dealing with the already-applied schema migration. Audience: a competent backend on-call engineer who knows the stack but has never rolled back this particular service before. Keep it to roughly 300-450 words in the final revision.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
**Phase 1 - Draft**

## Rollback Procedure

1. **Declare the rollback**
   - Announce in incident channel that you are rolling back the current production deploy.
   - Capture the current deploy version and migration version before changing anything.

2. **Revert the application**
   - In CI/CD, trigger the rollback to the last known good application release.
   - Prefer the automated “redeploy previous artifact” or “rollback” action over a manual hotfix.
   - Wait for the service to become healthy and confirm the new pods/instances are running the previous code.

3. **Handle the database migration**
   - The migration has already:
     - added a new `NOT NULL` column with a default,
     - backfilled it,
     - dropped the old column.
   - Because the old column is gone, a simple code rollback may fail if the previous app still reads it.
   - Check whether the previous app version is compatible with the new schema. If it is not, you must restore the dropped column shape before traffic is fully shifted back.

4. **Restore the dropped column if needed**
   - Apply the documented reverse migration or a manual compensating migration that:
     - recreates the old column with the expected type and nullability,
     - backfills it from the new column if necessary,
     - restores any index/constraint dependencies the old code requires.
   - Do **not** remove the new column yet; leave it in place until the rollback is verified.

5. **Verify and monitor**
   - Confirm the app is serving the reverted code path without DB errors.
   - Watch 500 rates, DB error logs, and latency for at least one full incident window after rollback.
   - If errors persist, stop and reassess before making additional schema changes.

6. **Post-rollback cleanup**
   - Once stable, document the exact deploy, migration, and rollback actions taken.
   - Create a follow-up task to design a safer reversible migration pattern for future releases.

---

**Phase 2 - Critique**

1. The draft says, **"Check whether the previous app version is compatible with the new schema"**, but it does not tell the on-call engineer how to determine that quickly under pressure. It should specify concrete checks, such as whether the old code still queries the dropped column or whether the rollback artifact expects it.

2. The draft says, **"Apply the documented reverse migration or a manual compensating migration"**, but it is too vague because it does not define what to do if there is no reverse migration already written. It should give an explicit fallback order: use an existing down migration, otherwise run an emergency SQL patch approved by the team.

3. The draft includes **"Do not remove the new column yet"**, but it never explains when it is safe to drop it later or who should do that. It should say to leave it until the service is stable and the team has validated the old code path, then handle cleanup in a follow-up deploy.

4. The draft’s step **"Wait for the service to become healthy and confirm the new pods/instances are running the previous code"** lacks concrete validation. It should specify what health signals to check, such as rollout status, error rate, and a sample request hitting the reverted code path.

5. The final step **"watch 500 rates, DB error logs, and latency for at least one full incident window"** is vague about the duration and threshold. It should define a shorter, operationally useful monitoring period and mention expected improvement criteria, like 5–10 minutes of sustained recovery.

---

**Phase 3 - Revision**

## Rollback Procedure

1. **Announce and freeze changes**
   - Post in the incident channel that rollback is in progress.
   - Stop any further deploys or migration jobs for this service.
   - Record the current application release, commit SHA, and database migration version.

2. **Revert the application code**
   - Use the CI/CD rollback action to redeploy the last known good artifact; do not hand-edit production.
   - Wait for the rollout to complete and confirm the service is serving the previous release:
     - deployment/rollout status is healthy,
     - old pods/instances are replaced,
     - error rate starts to fall.
   - Send one or two representative requests through the affected code path to confirm the reverted app is running.

3. **Assess schema compatibility immediately**
   - The failed deploy included a migration that added a `NOT NULL` column with a default, backfilled it, and dropped an old column.
   - The key rollback question is whether the previous app still references the dropped column or depends on the old table shape.
   - Check the previous release notes, the migration diff, or the app query path if needed. If the old release expects the dropped column, you must restore it before calling the rollback complete.

4. **Restore the old schema shape if required**
   - Prefer a documented down migration if one exists.
   - If there is no safe down migration, run the team-approved emergency SQL patch to recreate the dropped column with the original type/nullability and backfill it from the new column as needed.
   - Restore any index, constraint, or trigger dependencies the old code requires.
   - Keep the new column in place during rollback; do not attempt to “fully undo” the forward migration in the same step unless explicitly approved.

5. **Verify recovery**
   - Confirm 500s and DB errors drop back toward baseline within 5–10 minutes.
   - Check app logs for missing-column, constraint, or type-cast errors.
   - If errors remain elevated after the schema fix and app rollback, pause and escalate; do not make additional unplanned schema changes.

6. **Complete the rollback**
   - Once traffic is stable on the reverted app and schema, document:
     - what was rolled back,
     - whether the schema had to be patched,
     - any remaining cleanup items.
   - Open a follow-up task to add a tested reverse migration or a safer expand/contract pattern for this service.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
