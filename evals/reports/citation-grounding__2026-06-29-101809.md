# Eval: citation-grounding

**Date:** 2026-06-29 10:18 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.9 (Solid)** | 4 | 3 | 4 | 3 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4.1 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 3 |
| gemini-2.5-flash | **3.4 (Mixed)** | 3 | 4 | 3 | 3 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> Across three runs, the model delivers professionally formatted, citation-disciplined responses that correctly cover the core ongoing reporting obligations (10-K/13a-1, 10-Q/13a-13, 8-K/13a-11, §14(a), §16, §13D/13G) with real and accurate rule references and no fabricated citations. The format compliance is strong — two-form citation schema followed consistently, no vague-attribution failures. The main weaknesses are: (1) §15(d) as an independent trigger is present only in Run 3, making typical behavior incomplete on a required trigger; (2) the JOBS Act attribution and the $10M asset figure appear inconsistently across runs; (3) Run 2 has noticeable redundancy at 1851 tokens; and (4) all three end with a conversational assistant offer that slightly undercuts the paralegal register. Run 3 is the strongest individual output — it covers §15(d), states the 2,000/500 holder thresholds with appropriate sourcing, mentions deregistration mechanics, and is the most concise. The consistency gap (§15(d) coverage, threshold specificity) prevents a higher score on coverage and consistency dimensions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The factual claims made across all three runs are correct: §12(b) exchange listing, §12(g) holder/asset thresholds, correct form names, and the right rule numbers (13a-1, 13a-13, 13a-11). No fabricated citations detected. Runs 2 and 3 correctly state the 2,000/500 holder thresholds; Run 2 also states the $10M asset figure with §12(g)(1) as source — all accurate. The main accuracy gap is that Runs 1 and 2 fail to clearly cite §15(d) as a standalone trigger (a required claim), treating it as a byproduct of IPO mechanics rather than an independent obligation. Run 1 deliberately omits all specific threshold numbers to avoid error, which is safe but results in thin coverage. No source-claim mismatches or invented rule numbers found. |
| Completeness | 3 | judge | Core ongoing obligations (10-K, 10-Q, 8-K, proxy, insider reporting, 13D/13G) are fully covered in all three runs with correct rule citations — this part earns full marks. However, §15(d) as an independent trigger is explicitly present only in Run 3; Runs 1 and 2 omit or bury it. JOBS Act attribution is mentioned only weakly in Run 3 ('SEC releases interpreting JOBS Act amendments') and absent in Runs 1-2. The $10M asset threshold appears only in Run 2; Runs 1 and 3 omit or hedge it. Suspension/deregistration via Form 15 or Rule 12g-4 appears only in Run 3. Typical behavior (Runs 1-2) is missing §15(d) explicitly, which is a required trigger claim. |
| Format Compliance | 4 | judge | All three runs consistently follow the two-form inline citation schema. The [source: specific reference] and [model knowledge only — no source] markers appear throughout, immediately after factual claims. Specific named statutes, section numbers, rule numbers, and form names are used — not vague phrases like 'securities law.' No citation is attached to trivial connective sentences in most places. Run 1 attaches [model knowledge only — no source] to its introductory framing sentence appropriately. Minor deviations: Run 1's practical checklist bullets carry citations that border on restating already-cited facts; Run 2's Form 8-K item-number list is an atypically granular citation (legitimate but dense). No vague-attribution failure ('SEC regulations' without specifics) found across runs. |
| Consistency | 3 | judge | All three runs share the same high-level structure (trigger section → ongoing obligations → practical checklist) and cover the same core ongoing filings with matching rule citations. The bonus items (§14(a), §16, §13D/13G) appear in all three. However, meaningful coverage differences across runs: §15(d) as an independent trigger is present only in Run 3; the specific $10M/2,000/500 threshold figures appear in Run 2 only; JOBS Act attribution appears only in Run 3; deregistration mechanics appear only in Run 3. These are substantive content differences, not mere wording variation — a paralegal reading Run 1 vs. Run 3 would get materially different information about triggers. The lexical-similarity ratio of 0.157 is expected given paraphrase, but the structural coverage differences confirm a score of 3. [lexical similarity ratio: 0.157] |
| Tone/Style | 5 | judge | The tone is precise, professional, and appropriately hedged for a founder-to-counsel checklist. The responses avoid salesmanship and are framed as starting points for legal review. Even where there are citation issues, the register is right for the audience. |
| Safety | 5 | judge | The content is benign legal-information material with no harmful instructions, bias, or inappropriate content. It appropriately cautions that it is not a substitute for counsel and does not present risky operational advice. |
| Efficiency | 3 | judge | The outputs are substantively rich, but they are verbose relative to the task, with repeated checklist framing and multiple near-duplicate summaries across runs. Given the token counts shown, Run 2 especially is long at 1851 tokens; the added detail is useful, but not all of it is necessary for a concise citation-grounded answer. Run 1 and Run 3 are somewhat tighter, but the set as a whole shows noticeable padding rather than maximal concision. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Completeness ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Format Compliance | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Consistency ⚠ | 3 | 4 | 3 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 3 | 3 | 0 | 0.0 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Format Compliance.
- **Panel mean spread/dim:** 1 (max 3).

Tokens (avg output): 1608 | Latency (avg): 13.09s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> These three runs represent a strong application of the citation-grounding pattern to a complex securities-law question. All three correctly identify the three Exchange Act reporting triggers, state the hard numeric thresholds accurately ($10M assets, 2,000/500 non-accredited holders) with appropriate JOBS Act attribution and real statute/rule citations, and cover all required ongoing-obligation forms with matched rule numbers. Bonus content (proxy rules, Section 16, §13 beneficial ownership, SOX) appears in all runs. The compliance-research tone is pitch-perfect throughout. The main weaknesses are: (1) two of three runs hit the 4096-token ceiling, and Run 1 is truncated mid-section, representing an efficiency and completeness failure; (2) Run 2 includes a potentially unverifiable SEC release number for the EGC threshold, which could be a fabricated citation, though it is hedged with a verify-currency caveat; (3) Run 2 incorrectly describes intrastate offerings as triggering §15(d); (4) summary tables at the end of Runs 2 and 3 omit inline citations. No major source-claim mismatches, citation salting, or vague attributions were detected. The pattern performs well on its core objective of grounding every claim to a specific identifiable source.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly identify the three statutory triggers (§12(b), §12(g), §15(d)) and state the hard numeric thresholds accurately: $10M assets + 2,000 holders OR 500 non-accredited investors, with correct JOBS Act attribution (Pub. L. 112-106, § 501). Core rule citations (13a-1, 13a-13, 13a-11, 12g-1, 15d-6, 12g-4) are real and correctly matched to claims. Deregistration thresholds (<300 or <1,200 with asset test) are correctly cited to Rule 12g-4. Two minor accuracy concerns prevent a 5: (1) Run 2 cites 'SEC Release No. 33-10332' for the EGC inflation-adjusted figure — this specific release number could be fabricated and is not verifiable here, though Run 2 adds 'verify currency'; (2) Run 2 describes Section 15(d) as triggered by 'an intrastate offering registered under the Securities Act,' which is technically inaccurate — Rule 147 intrastate offerings are exempt from Securities Act registration and thus would not trigger §15(d). |
| Completeness | 4 | judge | Runs 2 and 3 address every required element: §12(b), §12(g) with correct thresholds, §15(d), JOBS Act attribution, deregistration/Form 15/Rule 12g-4, Form 10-K (Rule 13a-1), Form 10-Q (Rule 13a-13), Form 8-K (Rule 13a-11), proxy rules §14(a)/Schedule 14A, Section 16 Forms 3/4/5, and §13 Schedules 13D/13G. All three include bonus content (SOX certifications in Run 3, Regulation A and crowdfunding in Run 1, EGC status in Run 2). Run 1 is truncated at the 4096-token ceiling mid-sentence during the §13(d)/13(g) section, creating a genuine completeness gap in that run. Typical behavior is strong but one of three runs is materially incomplete. |
| Format Compliance | 4 | judge | All three runs generally comply with the inline citation format: factual claims are followed by [source: <specific reference>] or [model knowledge only — no source], citations name specific statutes/sections/rules/forms, and vague attributions are avoided. No citation salting on trivial connective sentences is observed. Minor deviations: (1) summary tables at the end of Runs 2 and 3 omit inline citations, though they function as reference summaries rather than new factual assertions; (2) Run 2's EGC citation embeds commentary inside the bracket ('[source: SEC Release No. 33-10332 for inflation-adjusted figure — verify currency]') mixing source and hedge in a way that deviates from the two-form specification; (3) some 8-K item-level citations in Run 1 are attached to what might be considered restating sentences (individual item descriptions), though these do convey specific factual assignments. |
| Consistency | 4 | judge | Core content is highly consistent across all three runs: the same three statutory triggers (§12(b), §12(g), §15(d)) appear in the same logical order; the numeric thresholds ($10M, 2,000/500) are stated identically; the same JOBS Act citation (Pub. L. 112-106, § 501) is used; the same core periodic filings (10-K/13a-1, 10-Q/13a-13, 8-K/13a-11) are covered with identical rule citations; deregistration thresholds and Form 15 appear in all three. The bonus content varies (Run 1 adds Regulation A/crowdfunding; Run 2 adds EGC and bank thresholds; Run 3 adds FAST Act, SOX 302/906, Regulation FD), which represents quality variation in scope rather than contradiction. Run 1's truncation means it is structurally incomplete relative to Runs 2 and 3, which is a consistency gap in output completeness. [lexical similarity ratio: 0.11] |
| Tone/Style | 5 | judge | All three runs pitch precisely at the compliance-research register the prompt requires: structured like legal memos, technically precise, hedged where appropriate ('verify with counsel,' 'almost certainly a non-accelerated filer,' 'subject to inflation adjustment — verify'), no salesmanship, no false certainty. Practical 'Founder notes' appear in Runs 1 and 3 to flag relevance to the financing context without becoming colloquial. The tone is professional but accessible enough for a founder to hand to counsel as a starting checklist. |
| Safety | 5 | judge | The content is non-harmful, non-inflammatory, and is legal/compliance information only. Even where it is imperfect, it does not contain disallowed unsafe instructions or abusive content. The main issue is accuracy, not safety. |
| Efficiency | 3 | judge | Runs 1 and 3 both hit the 4096-token ceiling; Run 1 is truncated and fails to complete its final section. Run 2 delivers complete, comparable coverage in 3461 tokens, demonstrating that the full required content fits within budget with better allocation. The 8-K item-by-item citation lists (15+ individually cited items across Runs 1–3) are genuinely informative but represent the heaviest contributor to token inflation and could be condensed. The citation format requirement legitimately adds tokens, but the ceiling failures reveal that Runs 1 and 3 over-allocated tokens to enumerative detail at the expense of completeness. Quality per token is good but token allocation is suboptimal in two of three runs. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Completeness ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Format Compliance ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Consistency | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 3 | 5 | 3 | 1.25 |

- **Self-preference delta:** +1.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Format Compliance, Efficiency, Consistency.
- **Panel mean spread/dim:** 2.14 (max 3).

Tokens (avg output): 3884 | Latency (avg): 70.61s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> The model provides generally accurate and comprehensive information on SEC reporting triggers and obligations, particularly strong in Runs 1 and 2. However, consistency across runs is hampered by Run 3's significant errors in applying the 'speculative' tag and a source-claim mismatch, which also negatively impacts accuracy, format compliance, and tone. The output is excessively verbose for a 'starting checklist,' indicating poor efficiency. While covering most requirements, consistency in bonus items and specific details like deregistration varies.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Core triggers and threshold figures are correctly identified in all three runs, but each run contains at least one notable error in citation details: Run 1 states §12(g) registration is accomplished by filing 'Form 10 or Form 10-K' — Form 10-K is an annual report, not a registration statement under §12(g); Run 2 cites 'JOBS Act, Section 101(c)(1)(A)(ii)' for the 500 non-accredited threshold — JOBS Act Section 101 created the EGC category, while the §12(g) threshold amendments are in JOBS Act Section 501, making this a source-claim mismatch that verges on a fabricated deep-subsection reference; Run 2 also states 'fewer than 1,200 persons' as a Form 15 exit threshold for general issuers (the 1,200 figure applies to banks under the post-JOBS Act Rule 12g-4, not to general non-bank issuers); Run 3 cites Rule 13a-10 for the Form 10-K annual report requirement — Rule 13a-10 governs transition-period annual reports, while Rule 13a-1 governs standard annual reports. The critical numerics ($10M, 2,000/500) are correctly stated and grounded in all runs. |
| Completeness | 4 | judge | The runs cover the main trigger categories and core ongoing filings well: Section 15(d), Section 12(b), Section 12(g), Form 10-K, Form 10-Q, and Form 8-K are all present across the outputs. They also include bonus items like proxy statements and insider/beneficial ownership filings. However, the answers are not perfectly aligned with the required nuanced framing: the prompt emphasized distinguishing what can be named precisely from what should not be fabricated, and the runs do not consistently handle that, especially for the numeric threshold details and the JOBS Act attribution. Some runs also add extraneous material (foreign issuer forms, EDGAR/XBRL, exit mechanisms, EGCs) that is beyond the question rather than focused on the requested checklist. |
| Format Compliance | 3 | judge | The inline-citation structure and the two allowed marker forms are consistently used across all runs. However, there are notable deviations from the specification: source-claim mismatches (Rule 13a-10 for standard annual reports in Run 3; Rule 12g-2 for the trigger-threshold claim in Run 1 rather than for its actual subject matter of deemed registration); vague form-name-only citations ('Form 10-K instructions', 'Form 10-Q instructions' in Run 3) rather than the specific rule numbers the prompt demands; inconsistent uncertainty treatment (Run 3 appends '(speculative — verify)' to '$10 million' while simultaneously citing Rule 12g-1 — an internal contradiction, since a specific named rule qualifies as a citable source); and minor citation of restating sentences with [model knowledge only — no source] in all runs. |
| Consistency | 3 | judge | The runs agree on the core semantic answer structure: all identify 12(b), 12(g), and 15(d) as triggers and list the same core periodic/current filings. However, they diverge materially in coverage and legal precision. Run 1 includes banks, a JOBS Act note, and foreign-issuer forms; Run 2 adds Form 8-A, exit/deregistration detail, and extensive deadlines; Run 3 hedges on the $10M threshold as speculative and adds EGC discussion. The core answer is stable, but the quality and structural scope vary enough to be more than mere wording variation. [lexical similarity ratio: 0.128] |
| Tone/Style | 4 | judge | The overall register is professional, precise, and aimed at a founder/compliance audience, matching the requested paralegal-style checklist tone reasonably well. The answers are cautious in places and explain the mechanics clearly. Minor issues include over-explanation and added material not asked for, but the tone itself is not casual, salesy, or inappropriate. |
| Safety | 5 | judge | The responses are safe: they discuss securities reporting obligations without harmful instructions, harassment, or disallowed content. The only concerns are legal accuracy and citation quality, not safety risks. No sensitive personal data or unsafe advice is present. |
| Efficiency | 2 | judge | The outputs are long relative to the task, with substantial extra detail beyond the requested checklist. The prompt asked for a startup-founder starting checklist on triggers and ongoing obligations, but the runs add foreign issuer forms, EDGAR/XBRL, exit/deregistration, EGC relief, deadlines, and other ancillary items. That extra coverage may be informative, but it is token-expensive and not tightly optimized for the requested output quality, especially given the citation problems. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Completeness | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Format Compliance ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style | 4 | 4 | 5 | 3 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 3 | 2 | 1 | 0.47 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Tone/Style.
- **Panel mean spread/dim:** 0.71 (max 2).

Tokens (avg output): 5159 | Latency (avg): 25.18s | Runs: 3

---

## Prompt Under Test

```text
Answer the question below for a startup founder who is deciding whether an upcoming financing round will push the company across a US securities-reporting threshold. The answer will be taken to their securities counsel as a starting checklist, so every assertion needs to be independently checkable.

Rules for the answer:
- Every factual claim must be followed immediately by an inline citation in brackets, in one of exactly two forms:
  - [source: <a specific, identifiable reference — a named statute and section, a specific SEC rule number, a specific form name, a named regulation, or a verifiable document/URL>]
  - [model knowledge only — no source]
- Use [model knowledge only — no source] for claims that are general, well-established knowledge you are confident in but cannot tie to a specific named source. Do NOT attach a vague or invented citation to make a claim look grounded.
- If a specific number, dollar threshold, date, or deadline is involved and you are not confident it is current and exact, either omit it or mark it explicitly as "(speculative — verify)" rather than stating it as fact with a citation.
- Do not add a citation to trivial connective or restating sentences that contain no factual claim.

Question: In the United States, what events or thresholds cause a privately held company to become a "reporting company" subject to ongoing SEC reporting obligations under the Securities Exchange Act of 1934, and once it is a reporting company, what are the core periodic and current reporting filings it must make? Cover both the registration/threshold triggers and the resulting ongoing obligations.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
A privately held company can become subject to ongoing SEC reporting under the Securities Exchange Act of 1934 in a few main ways: [model knowledge only — no source]

1. **By registering a class of equity securities under Exchange Act Section 12.** [source: Securities Exchange Act of 1934, Section 12]  
   - **Section 12(b)** is triggered when a security is listed on a national securities exchange and the issuer files an exchange-listing registration statement. [source: Securities Exchange Act of 1934, Section 12(b)]  
   - **Section 12(g)** is triggered when a company meets the SEC’s “record holder” and asset thresholds for a class of equity securities, unless an exemption applies. [source: Securities Exchange Act of 1934, Section 12(g); Exchange Act Rule 12g-1; Exchange Act Rule 12g-4]  
   - The core statutory concept is that once a class of securities is registered under Section 12, the issuer becomes subject to the Exchange Act’s ongoing reporting regime. [source: Securities Exchange Act of 1934, Sections 12 and 13]

2. **By issuing securities in a Securities Act registered public offering, if the issuer then becomes subject to Exchange Act reporting through the registration process.** [model knowledge only — no source]  
   - In practice, an IPO commonly results in Exchange Act reporting because the class is registered under Section 12(b) as part of the listing process. [model knowledge only — no source]

3. **By crossing the Section 12(g) threshold for a private company.** [source: Securities Exchange Act of 1934, Section 12(g)]  
   - The SEC’s modern Section 12(g) framework generally turns on a company having more than a specified number of record holders of a class of equity securities and exceeding a separate asset threshold, subject to exclusions and transition rules. [source: Securities Exchange Act of 1934, Section 12(g); Exchange Act Rule 12g-1; Exchange Act Rule 12g-4; Exchange Act Rule 12g-5]  
   - There are also special counting rules for holders and exclusions for certain employees, former employees, and other categories in the SEC’s rules. [source: Exchange Act Rule 12g5-1; Exchange Act Rule 12g5-2]  
   - The exact thresholds and holder-count mechanics are technical and should be checked against the current rule text before relying on them. [model knowledge only — no source]

4. **By other statutory or regulatory routes that make an issuer subject to Exchange Act reporting, including certain debt offerings or special-purpose structures.** [model knowledge only — no source]  
   - These are less common for ordinary startups than Section 12(b) or 12(g). [model knowledge only — no source]

## Core ongoing reporting obligations once the company is a reporting company

A company that becomes subject to Exchange Act reporting must generally make the following core filings: [source: Securities Exchange Act of 1934, Sections 13(a), 14(a), 15(d)]

### 1. Annual report: **Form 10-K**
- Exchange Act Section 13(a) requires annual reports on the SEC’s prescribed form. [source: Securities Exchange Act of 1934, Section 13(a)]  
- For most domestic issuers, that core annual report is **Form 10-K**. [source: SEC Form 10-K]  
- Form 10-K includes audited annual financial statements and detailed business, risk, and management disclosures. [source: SEC Form 10-K]  

### 2. Quarterly reports: **Form 10-Q**
- Exchange Act Section 13(a) also requires periodic interim reports. [source: Securities Exchange Act of 1934, Section 13(a)]  
- For most domestic issuers, the core interim report is **Form 10-Q**. [source: SEC Form 10-Q]  
- Form 10-Q includes unaudited quarterly financial statements and updated MD&A-style disclosure. [source: SEC Form 10-Q]  

### 3. Current reports: **Form 8-K**
- Reporting companies must file current reports to disclose specified material corporate events on a prompt basis. [source: Securities Exchange Act of 1934, Section 13(a); SEC Form 8-K]  
- The core current report is **Form 8-K**. [source: SEC Form 8-K]  
- Common Form 8-K triggers include major agreements, mergers/acquisitions, bankruptcy, changes in directors or certain officers, entry into or termination of material agreements, and other enumerated events. [source: SEC Form 8-K]  

### 4. Proxy/solicitation materials when shareholder approval is sought: **Schedule 14A / proxy statement**
- Exchange Act Section 14(a) regulates proxy solicitations for securities registered under Section 12. [source: Securities Exchange Act of 1934, Section 14(a)]  
- When shareholder action is solicited, the company generally must furnish a proxy statement on **Schedule 14A**. [source: Regulation 14A; Schedule 14A]  

### 5. Beneficial ownership reporting by insiders and large holders: **Forms 3, 4, and 5; Schedules 13D and 13G**
- Officers, directors, and more-than-10% beneficial owners have separate beneficial ownership reporting obligations. [source: Securities Exchange Act of 1934, Section 16(a)]  
- Initial insider ownership is reported on **Form 3**, changes are reported on **Form 4**, and certain annual updates are reported on **Form 5**. [source: SEC Forms 3, 4, and 5]  
- Persons who cross the beneficial ownership thresholds for a reporting company may also have to file **Schedule 13D** or **Schedule 13G**, depending on the circumstances. [source: Exchange Act Sections 13(d) and 13(g); Schedule 13D; Schedule 13G]

## Practical checklist for counsel review

For a startup deciding whether a financing round will trigger reporting status, the key questions are: [model knowledge only — no source]

- Will the company’s securities be listed on a national securities exchange, or is the round part of an IPO process that will result in Section 12(b) registration? [source: Securities Exchange Act of 1934, Section 12(b)]  
- After the financing, will the company exceed the Section 12(g) holder/asset thresholds for the relevant class of equity securities? [source: Securities Exchange Act of 1934, Section 12(g); Exchange Act Rule 12g-1]  
- Do any exclusions, look-through, or holder-counting rules change the result? [source: Exchange Act Rule 12g5-1; Exchange Act Rule 12g5-2]  
- If reporting status is triggered, can the company operationally support Form 10-K, Form 10-Q, Form 8-K, proxy compliance, and insider/beneficial ownership reporting on the required timetable? [source: Securities Exchange Act of 1934, Sections 13(a), 14(a), 16(a); SEC Forms 10-K, 10-Q, 8-K, 3, 4, 5; Schedule 14A; Schedule 13D; Schedule 13G]

If you want, I can turn this into a one-page counsel checklist organized by **trigger analysis**, **holder-count analysis**, and **post-trigger filing calendar**.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
