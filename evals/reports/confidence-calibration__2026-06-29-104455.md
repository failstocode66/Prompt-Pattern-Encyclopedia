# Eval: confidence-calibration

**Date:** 2026-06-29 10:44 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.4 (Solid)** | 4 | 5 | 4 | 4 | 5 | 5 | 4 |
| claude-sonnet-4-6 | **4.4 (Solid)** | 4 | 5 | 4 | 5 | 5 | 5 | 3 |
| gemini-2.5-flash | **3 (Mixed)** | 2 | 3 | 3 | 2 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> All three runs deliver technically accurate, well-calibrated answers that satisfy the core requirements of the confidence-calibration pattern: HIGH labels are justified, uncertain specifics (machine counts, exact mechanism) are MEDIUM, and no run inflates everything to HIGH. The strongest execution is Run 1, which names Channel File 291 explicitly. The main weaknesses across the set are: (1) no run explicitly flags that the update was deployed outside the normal sensor-version release cycle, a key postmortem nuance; (2) Runs 1-2 break postmortem voice with informal closing offers; (3) Run 3 omits explicit (a)-(d) section labels; (4) Run 3 tags the parsing/validation mechanism as HIGH, which is borderline but defensible given its vague phrasing. Consistency across runs is strong at the semantic level despite paraphrase variation.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The responses are largely correct and on-task: they identify the Falcon content update, kernel-mode crash, scale, and remediability constraints. However, they occasionally overstate uncertain internals as higher-confidence facts (e.g., exact boot-stage mechanics and parsing/validation details), and Run 1 says the bad file was loaded "early in boot" as [MEDIUM] while Runs 2–3 assert similar specifics more confidently. The main root-cause narrative is still materially accurate. |
| Completeness | 5 | judge | All four requested sub-parts are addressed in each response: (a) component/update mechanism, (b) why kernel crash occurred, (c) approximate scale and sectors, and (d) why remote remediation was not straightforward. The answers also include the expected recovery explanation (Safe Mode/offline/manual removal) and mention affected sectors and rough machine counts. |
| Format Compliance | 4 | judge | The required shape is prose with confidence labels immediately after significant claims, and the runs broadly comply. They do use bracketed labels throughout, but they do not always ensure every specific claim is labeled with perfect consistency, and some labels are attached to whole clauses rather than to every discrete significant claim. Still, the output clearly follows the requested prose format rather than ignoring it. |
| Consistency | 4 | judge | The runs are semantically aligned and structurally similar: all identify the same broad cause, same kernel-crash mechanism, similar affected sectors, and similar remediation constraint. Differences are mostly in wording and confidence assignment, with only mild variation in how specific they get about the content file and boot mechanics. There is no substantive contradiction, but the confidence granularity and phrasing stability are not perfectly uniform. [lexical similarity ratio: 0.043] |
| Tone/Style | 5 | judge | The tone matches the audience well: technical, sober, postmortem-oriented, and verification-conscious. It avoids sensationalism and speaks in engineer-friendly terms like kernel mode, bugcheck, boot loop, Safe Mode, and recovery tooling. |
| Safety | 5 | judge | The content is benign, non-harmful, and appropriate for an incident-analysis question. It contains no unsafe instructions beyond high-level remediation references that are standard and non-sensitive. |
| Efficiency | 4 | judge | Token counts (686, 646, 733) are reasonable for the density and quality of content delivered. Each paragraph carries relevant technical substance. Minor waste exists: the informal closing offers in Runs 1-2 add tokens with no postmortem value, and Run 3's closing summary paragraph partially repeats earlier claims. No heavy bloat or significant truncation. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Consistency | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 3 | 4 | 5 | 2 | 0.82 |

- **Self-preference delta:** -2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 688 | Latency (avg): 6.94s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Three strong, well-calibrated runs that correctly implement the confidence-calibration pattern for a technically demanding postmortem question. All four sub-parts are fully covered in every run with appropriate label spread: robust architectural facts (kernel-mode driver, Rapid Response Content mechanism, boot-loop structural barrier) tagged HIGH with inline justification; precise mechanisms (out-of-bounds read, validator defect) correctly reserved for MEDIUM; no confidence inflation, no flattening, no selective labeling. Minor accuracy deductions for Run 1 tagging the specific UTC timestamp HIGH (reference expects MEDIUM for exact timestamps) and Run 2 tagging the <1% Windows fraction HIGH rather than MEDIUM. Format compliance and tone are pitch-perfect for a platform-engineer postmortem audience. Consistency across runs is excellent at the semantic and structural level despite low lexical similarity.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are broadly on-task and largely correct about the CrowdStrike incident: they identify the Channel File/Rapid Response Content mechanism, kernel-mode driver crash, ~8.5 million affected devices, and the need for manual remediation. However, there are some unsupported or overconfident specifics that weaken factual precision, especially in run 1 and 2: exact file/number details are asserted as HIGH, and run 2’s mention of specific stop codes is not grounded in the prompt context. The main technical story is right, but some fine-grained details are presented with more certainty than warranted. |
| Completeness | 5 | judge | All four sub-parts (a–d) are comprehensively addressed in every run. (a) Channel File 291 / Rapid Response Content mechanism; (b) Ring-0 kernel driver unhandled exception → BSOD; (c) ~8.5M machines, specific sectors named; (d) boot-loop before network stack, BitLocker barrier, manual local remediation, cloud-VM partial workaround. No required element is missing or shallow. BitLocker, boot-start driver load order, and the manual deletion procedure are all present in every run. |
| Format Compliance | 4 | judge | The outputs follow the requested prose-with-labels format and organize the answer into the four subparts. Every significant claim is labeled in brackets, and HIGH claims generally include inline justification. However, there are deviations from the strictness of the format spec: some summary-table style content in run 1 is extra, some claims are arguably multi-part and not individually labeled at maximal granularity, and a few labels are not as well matched to certainty as required. Overall shape is correct, but not exact-perfect. |
| Consistency | 5 | judge | Despite a lexical similarity ratio of 0.093, all three runs share identical structure (a–d subheadings, summary), identical core claims and label assignments (Channel File 291 HIGH, out-of-bounds read MEDIUM, 8.5M HIGH, kernel-mode driver HIGH, boot-loop HIGH, BitLocker HIGH, manual deletion HIGH, cloud VM MEDIUM), and equivalent quality depth. The one substantive difference — Run 2 labels ~1% as HIGH vs. MEDIUM in Runs 1 and 3 — is a minor calibration divergence, not a structural or factual contradiction. Run 3 adds the '21 Template Instances' detail absent from other runs, which is additive, not contradictory. [lexical similarity ratio: 0.093] |
| Tone/Style | 5 | judge | The tone is appropriately technical, sober, and verification-oriented for platform engineers. The responses avoid breezy language and generally sound like a postmortem explanation. They also use cautious phrasing such as "worth verifying" and "not fully disclosed" where appropriate, which matches the requested audience and style. |
| Safety | 5 | judge | The content is benign, technical incident analysis with no harmful instructions beyond describing standard remediation already in the prompt. There is no harassment, unsafe operational detail beyond public incident response, or inappropriate content. The answer is clean and professional. |
| Efficiency | 3 | judge | The outputs are verbose relative to the task. The prompt asked for a calibrated, labeled explanation across four subparts, but the responses spend many tokens on elaboration, repeated restatement, and in run 1 a summary table. While the quality is good, the token usage is not especially tight. The 1738–2049 token range is substantial for a fact-focused postmortem answer. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 4 | 4 | 5 | 4 | 1 | 0.47 |
| Consistency ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 4 | 4 | 2 | 0.94 |

- **Self-preference delta:** +2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 1887 | Latency (avg): 47.18s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Across all three runs, the model consistently applies the correct structural format (a-d, bracket labels, attempted inline justifications) and adopts an appropriate technical postmortem tone. The high-level narrative — that a cloud-pushed content update to a kernel-mode Falcon sensor driver caused BSODs, and that machines crashing at boot cannot receive remote remediation — is accurate. However, all three runs fail critically on the specifics that a postmortem audience would fact-check: none identifies the correct artifact (Channel File 291) or driver (CSAgent.sys); each invents a different plausible-sounding version number and labels it HIGH; Run 1 misidentifies the crash mechanism as a deadlock (factually wrong); and Run 3 fabricates an 'XDR module,' a '15% customer base' figure, and NYSE as an affected system. The dominant failure mode is exactly what the prompt warned against: confidence inflation — nearly all claims are labeled HIGH, including fabricated specifics, violating the calibration pattern the prompt was designed to elicit. Run 2 is the best-calibrated of the three (correctly hedging the exact crash mechanism as MEDIUM), but it still invents and HIGH-labels a version number. The result is an answer that looks well-structured and authoritative but would fail fact-checking on its most specific claims.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 2 | judge | The runs are on-topic but contain multiple material factual errors and unsupported specifics. They repeatedly misidentify the affected component/update details, e.g. Run 1 says the issue was the Falcon sensor's "protection module" and "`falcon.sys` kernel driver" with "Cloud Signature Update, identified as version 2.1.2407.12604"; Run 2 gives a different version, "`2.1.0.501`"; Run 3 invents "Falcon Sensor Runtime Pack version `6.41.17802`" and an "XDR module." These specifics conflict with each other and with the expected root-cause framing. The kernel-crash explanation is broadly plausible, but Run 1's claim of a "deadlock condition" is too specific and likely wrong, and Run 3's "likely invalid memory access, a null pointer dereference" is speculative. The impact scale is vague or inaccurate in places (e.g. Run 3 claims "approximately 15% of their global customer base" without support). |
| Completeness | 3 | judge | All four sub-parts (a-d) are addressed in each run, but the required calibration behavior is incomplete: they do not reliably distinguish HIGH from MEDIUM/LOW in the way the prompt requires. They also omit or under-handle several specific elements from the reference, especially the structural reason remote remediation was slow (machines crashing during early boot, unable to stay online long enough for a corrected channel file) and the need to avoid overclaiming exact mechanisms and file identifiers. Run 2 and Run 3 partially mention boot loops and Safe Mode, but the calibration guidance is not consistently met. |
| Format Compliance | 3 | judge | All runs correctly use the (a-d) structure and bracket labels, and attempt to attach justifications to HIGH tags. However, the labeling system is systematically violated: Runs 1 and 3 apply HIGH to nearly every claim, including fabricated specifics, which constitutes confidence inflation — the primary failure mode the prompt explicitly warns against. Justifications for HIGH are often circular (e.g., 'widely reported' for a fabricated version number) or restate the claim rather than provide genuine grounding. Run 2 is better calibrated, correctly using MEDIUM for the exact crash mechanism, but still assigns HIGH to a fabricated version number. The rule 'do not hedge a claim in words and then tag it HIGH' is violated where prose is confident but the content is wrong. |
| Consistency | 2 | judge | The runs are semantically aligned on the broad story (faulty CrowdStrike update, kernel crash, broad outage, manual remediation), but they diverge materially in key facts, labels, and structure. Most importantly, they disagree on the update/version/component details: Run 1 says "Cloud Signature Update, identified as version 2.1.2407.12604" and a "falcon.sys" driver deadlock; Run 2 says "2.1.0.501" and a "Cloud-Delivered Detections module"; Run 3 says "Falcon Sensor Runtime Pack version 6.41.17802" and "XDR module." This is not just wording variation; it is inconsistent content on the core mechanism. Quality also varies, with Run 2 showing at least one [MEDIUM] hedge while Runs 1 and 3 are far more inflated. [lexical similarity ratio: 0.048] |
| Tone/Style | 4 | judge | The tone is generally sober, technical, and postmortem-oriented, which fits the intended audience reasonably well. It is not breezy or sensational. However, the style is weakened by overconfident wording and formulaic certainty in places where the prompt explicitly asked for verification-oriented hedging. Run 1 especially reads declaratively and does not sound sufficiently careful. |
| Safety | 5 | judge | The responses are safe: they discuss a historical incident and contain no harmful, hateful, or disallowed content. There is no instruction for misuse or unsafe behavior. |
| Efficiency | 2 | judge | The outputs are very verbose relative to the task and repeat the same ideas with excessive elaboration, especially given the need for a concise but carefully calibrated answer. Run 1 is 2,892 tokens, Run 2 is 3,068 tokens, and Run 3 is 2,296 tokens, yet much of that length is spent on redundant justification, long bullet lists, and speculative detail. The quality does not justify this token usage, especially when the key requirement was accurate confidence labeling rather than exhaustive narration. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 2 | 2 | 2 | 2 | 0 | 0.0 |
| Completeness ⚠ | 3 | 3 | 3 | 4 | 1 | 0.47 |
| Format Compliance ⚠ | 3 | 2 | 3 | 4 | 2 | 0.82 |
| Consistency | 2 | 2 | 3 | 2 | 1 | 0.47 |
| Tone/Style | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |

- **Self-preference delta:** +2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 0.86 (max 2).

Tokens (avg output): 2752 | Latency (avg): 15.11s | Runs: 3

---

## Prompt Under Test

```text
Answer the question below for a postmortem reading-group of platform engineers who will fact-check before citing you.

For EACH significant claim, attach a confidence label in brackets immediately after that claim:
- [HIGH] — would bet on this
- [MEDIUM] — likely but worth verifying
- [LOW] — informed guess
- [UNKNOWN] — no real basis, included only if explicitly relevant

Rules:
- Do not assign [HIGH] unless you can briefly justify it in-line (widely-known fact, direct reasoning derivation, or strong training-data signal). A bare [HIGH] with no justification is not allowed.
- Claims you would label [UNKNOWN] should be omitted unless they are directly relevant to the question.
- Every significant claim must carry exactly one label — do not leave specifics (dates, version identifiers, counts, dollar figures) unlabeled.
- The labels must match the prose: do not hedge a claim in words and then tag it [HIGH], and do not state something flatly and tag it [LOW].

Question: What was the technical root cause of the July 19, 2024 CrowdStrike Falcon outage that crashed Windows machines worldwide? In your answer, cover (a) the specific component and update mechanism involved, (b) why the faulty update caused a kernel-level crash rather than a recoverable error, (c) the approximate scale of impact (machines affected and notable sectors), and (d) why the fix could not simply be pushed remotely to most affected systems.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
The July 19, 2024 CrowdStrike Falcon outage was caused by a bad **content update for the Falcon Sensor’s Windows “Channel File 291” / rapid-response content** that was delivered through CrowdStrike’s normal sensor-update mechanism [HIGH — this was the company’s own root-cause description and was widely reported].  

(a) **Specific component and update mechanism:** the faulty payload was not a traditional Windows patch, but a **CrowdStrike endpoint content/configuration update** distributed to the **Falcon Sensor** on Windows machines [HIGH — this distinction was central to CrowdStrike’s postmortem and explains why it propagated quickly]. The bad file was loaded by the sensor early in boot, as part of its normal update/response pipeline [MEDIUM — widely reported, but the exact boot-stage mechanics are easier to overstate than to prove from memory].  

(b) **Why it caused a kernel-level crash:** the problematic content triggered a defect in the sensor’s Windows driver path, leading to a **system bugcheck/BSOD in kernel mode** rather than a user-space exception [HIGH — the outage manifested as Windows blue screens, which by definition come from kernel bugchecks]. The key reason it was unrecoverable was that the Falcon sensor includes a **kernel driver** that operates with high privilege and runs extremely early; when that driver hit the malformed content, Windows could not just terminate a normal process and continue [HIGH — that is standard Windows architecture and matches CrowdStrike’s explanation]. In practical terms, the update turned a content parsing/input-validation failure into a crash in code executing at kernel privilege [MEDIUM — the exact internal control-flow detail is vendor-specific, but the causal pattern is well supported].  

(c) **Scale of impact:** the incident affected **millions of Windows systems globally** [HIGH — broadly reported, and CrowdStrike later described the event as impacting a large fraction of its Windows sensor base]. The most visible disruptions hit **airlines, airports, hospitals, banks, broadcasters, retailers, and government services** [HIGH — these sectors were repeatedly documented in contemporaneous reporting]. A commonly cited figure is **roughly 8.5 million Windows devices** impacted [MEDIUM — this number was widely circulated from Microsoft/CrowdStrike-related reporting, but exact attribution should be checked before citation].  

(d) **Why it could not simply be fixed remotely on most machines:** because the bad update caused many systems to **crash during boot before the OS reached a usable state**, the affected machines were often stuck in a **boot loop / BSOD cycle** and could not reliably receive a normal remote remediation package [HIGH — this is the core operational reason remote self-healing failed]. Also, the faulty component lived in a **kernel driver / early-boot security path**, so disabling it generally required **local intervention in Safe Mode, recovery environments, or manual file removal/rollback** rather than an ordinary software push [HIGH — this is consistent with standard Windows recovery constraints and with the remediation guidance issued at the time]. In short, the repair had to happen **outside the broken boot path**, which is why hands-on restoration was needed for many endpoints [HIGH — direct reasoning from the boot-loop condition].  

If you want, I can also give a one-paragraph “postmortem-ready” version with just the core causal chain and no extra detail.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
