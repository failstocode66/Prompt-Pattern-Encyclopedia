# Eval: least-to-most-prompting-baseline

**Date:** 2026-07-01 22:34 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **3.7 (Solid)** | 3 | 4 | 2 | 4 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **3.6 (Solid)** | 4 | 4 | 2 | 3 | 5 | 5 | 2 |
| gemini-2.5-flash | **4 (Solid)** | 5 | 4 | 2 | 4 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> The model performs very well on the core problem, accurately calculating all required values and arriving at the correct final answer with a professional, quantitative tone. Its consistency across runs is high. However, it struggles significantly with format compliance, missing key explicit labeling and annotation requirements. It also slightly misses the most rigorous aspect of the feasibility explanation and exhibits some redundancy in calculations, impacting efficiency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The runs correctly compute the workload, 120% multiplier, 80% gross-up, and per-shift staffing table, but they mishandle the core headcount conclusion. The reference requires 46 agents after reconciling shift demand and feasibility; Run 1 and Run 2 state 46, but Run 3 states 45 then later contradicts itself. Across the set, the typical answer is unstable on the final minimum headcount and feasibility reasoning, so accuracy is materially below fully correct. |
| Completeness | 4 | judge | Every mandatory element is present across all runs: raw handle-time computation, 120% multiplier, 0.8 gross-up, per-shift-per-day staffing table, 230 total agent-shifts, minimum headcount of 46, and a feasibility yes/no. The one missing element is the rigorous daily-peak feasibility check—the expected answer requires explicitly showing that 38 distinct agents per weekday < 46 total agents, confirming the peak does not become the binding constraint. Without that step the feasibility answer is asserted rather than proven. |
| Format Compliance | 2 | judge | The format specification requires two explicitly labeled phases: Phase 1 is a planning list of ordered sub-problems (annotating which prior sub-problem's result each consumes), and Phase 2 executes them in that same order while restating carried-forward inputs at each step. None of the three runs implements this two-phase least-to-most structure. All runs go directly into calculation, using numbered section headings (## 1, ## 2, …) rather than a decomposition-then-execution structure. The per-shift-per-day table and a clear final answer are present, which saves from a score of 1. |
| Consistency | 4 | judge | The responses are highly consistent in their core content, numerical results (46 agents, achievable, 19/19 weekday, 10/10 weekend), and the logical flow of calculations. The explanation of the 45 vs. 46 agent discrepancy is also consistent. While there is wording variation, the semantic and structural agreement is strong. The main inconsistency is the presentation of the final staffing table (Run 1 a summary table, Run 2 a daily detailed table, Run 3 a bulleted summary), and slight variations in the depth of the feasibility explanation. [lexical similarity ratio: 0.287] |
| Tone/Style | 5 | judge | All three runs are consistently precise, quantitative, and audit-ready—mirroring a workforce-planning analyst's voice. Calculations are shown symbolically and numerically, units are stated at each step, rounding decisions are explicitly flagged, and the distinction between productive hours and paid hours is carefully maintained throughout. |
| Safety | 5 | judge | The output is free from harmful, biased, or inappropriate content. It is a benign workforce-planning calculation with no unsafe or sensitive material beyond ordinary staffing math. |
| Efficiency | 3 | judge | Runs clock in at 1,219, 1,217, and 1,092 tokens respectively. Quality is good, but there is noticeable padding: each run presents 45 as a 'minimum' before walking it back to 46 (requiring extra prose to correct), and Runs 1 and 2 end with an offer to show an example schedule ('If you want, I can also show…') that adds tokens without fulfilling the prompt. The math itself is not bloated, but the two-step 45→46 narrative and the trailing offers represent avoidable overhead. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 2 | 4 | 4 | 2 | 0.94 |
| Completeness | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Format Compliance | 2 | 1 | 2 | 2 | 1 | 0.47 |
| Consistency | 4 | 2 | 5 | 4 | 3 | 1.25 |
| Tone/Style | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** -8.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 1176 | Latency (avg): 7.39s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs correctly compute the full numeric chain and reach the right answer (46 agents, feasible). The key operations — 120% multiplier on handle-time hours and dividing by 0.8 for paid-hour gross-up — are both applied in the correct order in every run, and the ceiling rounding and 230-shift aggregate are accurate throughout. The per-shift-per-day table (19/19 weekday, 10/10 weekend) is present and correct in all runs. The primary failure is format: the required two-phase structure (Phase 1 = enumerated sub-problem list with dependency annotations; Phase 2 = ordered solution with carried-forward input restatement) is completely absent — all runs solve inline. Efficiency is hurt significantly by Run 2 hitting the 4,096-token limit mid-analysis after extensive self-correction loops, and all runs produce collapsing group-assignment illustrations that are retracted. Consistency is moderate: the final answer and table are identical across runs, but the feasibility analysis quality and depth vary considerably.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Typical outputs get the core arithmetic right and land on the correct final answer, but the work is not fully rigorous and one run contains major internal missteps before recovering. Runs 1 and 3 correctly compute 46 agents; Run 2 initially derives 46 too, but then meanders through contradictory group counts and an unfinished/unclean feasibility argument. The main factual issue is not the final number but the shaky feasibility justification and some confused scheduling logic. |
| Completeness | 4 | judge | All required elements are present across every run: the full ordered numeric chain, the per-shift-per-day table (19/19 weekday, 10/10 weekend), the 230 aggregate shift-slot count, the 46-agent lower bound with ceiling logic, and a yes/no feasibility conclusion. Run 1 explicitly checks '38 shift-slots/day (Mon–Fri)…with 46 agents × at most 1 slot/day, we can fill 38 out of 46 agent-days — trivially feasible.' Runs 2 and 3 imply the same but do not state the 38<46 reconciliation as cleanly. No run fully and cleanly constructs a verified explicit schedule; all attempt group-assignment illustrations that break down and are abandoned, leaving the feasibility proof somewhat informal. |
| Format Compliance | 2 | judge | The outputs are structured as markdown analyses, not in the specified two-phase format. They include tables and numbered steps, but not the exact requested shape: Phase 1 ordered sub-problems with explicit dependency annotations, Phase 2 solving them in the same order with carried-forward values restated each time. Because the prompt explicitly demanded that format, compliance is partial at best. |
| Consistency | 3 | judge | The runs agree on the core answer and most numeric intermediate results, so there is no contradiction in the final conclusion. However, they vary materially in structure and quality of justification: Run 1 gives a long but somewhat confused constructive schedule, Run 2 spirals through contradictory groupings and partial corrections before ending with a proof sketch, and Run 3 is more concise but still hand-wavy on feasibility. This is same-core-answer, differing-coverage behavior, not full consistency. [lexical similarity ratio: 0.068] |
| Tone/Style | 5 | judge | All three runs are pitched squarely at a quantitative operations-analyst audience. Language is precise and formal, formulas are written out explicitly with LaTeX-style notation, tables provide auditable trails, and conclusions are stated without hedging. No hand-waving appears in the numeric chain. The register is consistent across all runs. |
| Safety | 5 | judge | The content is benign, workplace-planning arithmetic with no harmful, biased, or inappropriate material. There are no safety issues in any run. |
| Efficiency | 2 | judge | The outputs are verbose relative to the task, especially Run 2, which contains substantial re-derivation, self-correction, and dead-end schedule construction before returning to the same answer. Run 1 is cleaner but still longer than necessary; Run 3 is moderately concise. Given the requested exacting, auditable format, some length is warranted, but the token usage is not especially tight compared with the quality delivered. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Format Compliance | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 2 | 2 | 2 | 3 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 2807 | Latency (avg): 50.02s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs are numerically accurate throughout—correctly applying the 120% multiplier and then dividing by 0.8, rounding up shifts, and reaching 46 agents with a valid feasibility conclusion. The per-shift table and final answer are present in every run. The critical failure is format: the required two-phase least-to-most structure (Phase 1 = annotated sub-problem list with dependency chaining; Phase 2 = ordered solution restating carried-forward inputs) is entirely absent across all runs, which are instead undifferentiated numbered step sequences. Efficiency varies widely—Run 1 is acceptable while Run 2 is heavily padded with a constructive schedule proof that goes well beyond the question's requirements. Consistency is good on substance but marred by the large token-count and depth disparity between runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs correctly apply the 120% multiplier to handle-time hours and then divide (not multiply) by 0.8 to gross up paid hours—the two critical accuracy tests. Every intermediate numeric result matches the reference: 200→240→300 paid hrs/day weekday; 100→120→150 paid hrs/day weekend; 150/75 paid hrs/shift; 19/10 agents per shift after ceiling; 230 total agent-shifts; 46 minimum agents; feasibility YES. No run inverts the 0.8 operation or omits either adjustment. |
| Completeness | 4 | judge | All major requested computations are present: raw workload, multiplier, availability gross-up, per-shift staffing, total weekly agent-shifts, minimum headcount, and an explicit feasibility conclusion. The per-shift-per-day table is included in all runs. The main gap is that the reference demanded an explicitly ordered two-phase least-to-most structure with carried-forward inputs; the runs instead use a generic step-by-step breakdown and do not clearly separate Phase 1 and Phase 2 as requested. |
| Format Compliance | 2 | judge | The output does not follow the specified format. The prompt under test requested a two-phase structure with Phase 1 as an ordered numbered list and Phase 2 solving in the same order, with each later step restating carried-forward inputs. The runs are plain multi-step explanations rather than the required phase-labeled format. They do include a staffing table and a final answer, but the exact format match is not satisfied. |
| Consistency | 4 | judge | Across runs, the core answer is stable: same arithmetic path, same staffing table values, same 46-agent conclusion, same yes-feasible outcome. There is some variation in structure and the depth of feasibility proof, but the semantic result remains consistent. The divergence is mostly in exposition and proof style, not in the final answer. [lexical similarity ratio: 0.171] |
| Tone/Style | 5 | judge | The tone is precise, quantitative, and operations-oriented throughout. The responses are numerically explicit, auditable, and avoid hand-waving, matching the intended workforce-planning audience well. |
| Safety | 5 | judge | The content is benign and workplace-planning related. No harmful, biased, or inappropriate material appears. |
| Efficiency | 3 | judge | Run 1 (4,169 tokens) is reasonably tight. Run 3 (7,645 tokens) adds an unnecessary intermediate daily-agent step before splitting into shifts but stays manageable. Run 2 (13,635 tokens) is heavily bloated: the four-group constructive schedule proof is several hundred tokens beyond what the question requires, and the arithmetic verification of days-off totals (92 = 92) is padding. The average token cost (~8,500) is roughly 2× what should be needed for this problem. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Completeness ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 2 | 2 | 2 | 3 | 1 | 0.47 |
| Consistency | 4 | 4 | 4 | 4 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |

- **Self-preference delta:** +3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.57 (max 1).

Tokens (avg output): 8483 | Latency (avg): 37.26s | Runs: 3

---

## Prompt Under Test

```text
Problem: A customer-support center is planning next week's staffing for a single skill queue. The forecast is 9,600 contacts over the week, distributed as: Mon-Fri 1,600/day and Sat-Sun 800/day. Each contact takes an average handle time of 7.5 minutes. The service target requires staffing to 120% of the raw handle-time workload to absorb queueing and variability (this multiplier is applied to handle-time hours only). Separately, agents are only productively available 80% of their paid time (the other 20% is breaks, training, and after-call admin), so paid hours must be grossed up accordingly. Agents work 8-hour paid shifts, 5 shifts per week. Within a day, the workload splits into two equal shifts (a morning shift and an evening shift), and you cannot staff a fractional person on any shift. Finally, a hard rule: no single agent may be scheduled for both the morning and the evening shift on the same day. Question: What is the minimum total number of agents that must be hired for the week, and is a valid schedule actually achievable under all the constraints? Show the staffing requirement per shift per day along the way.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Let’s work it through step by step.

## 1) Weekly workload in handle-time hours
Forecast contacts:

- Mon–Fri: 1,600/day × 5 = 8,000
- Sat–Sun: 800/day × 2 = 1,600

Total weekly contacts = **9,600**

Average handle time = **7.5 minutes/contact**

Total raw handle time:

- 9,600 × 7.5 = 72,000 minutes
- 72,000 / 60 = **1,200 handle-hours**

---

## 2) Apply the 120% service staffing multiplier
Staffing requirement on handle-time hours only:

- 1,200 × 1.2 = **1,440 productive hours**

---

## 3) Gross up for 80% productive availability
Agents are productively available only 80% of paid time, so required paid hours are:

- 1,440 / 0.8 = **1,800 paid hours**

---

## 4) Convert to number of agent shifts
Each agent works:

- 8 paid hours per shift
- 5 shifts/week

So each agent contributes:

- 8 × 5 = **40 paid hours/week**

Total agents needed by weekly hours:

- 1,800 / 40 = **45 agents**

So the **minimum total number of agents hired is 45**.

---

# 5) Staffing requirement per day and per shift

The workload is split evenly between two shifts each day, so half of each day’s workload goes to morning and half to evening.

We should calculate the paid hours needed per day, then divide by 2 shifts.

## Weekdays (Mon–Fri)
Daily contacts = 1,600

Raw handle time:
- 1,600 × 7.5 = 12,000 minutes
- 12,000 / 60 = **200 handle-hours**

Apply 120% staffing factor:
- 200 × 1.2 = **240 productive hours**

Gross up for 80% productivity:
- 240 / 0.8 = **300 paid hours/day**

Split equally across 2 shifts:
- 300 / 2 = **150 paid hours per shift**

Convert to 8-hour agent shifts:
- 150 / 8 = 18.75 → **19 agents per shift**

So for each weekday:
- **Morning: 19 agents**
- **Evening: 19 agents**

Daily total = **38 agents scheduled across the two shifts**

---

## Weekend (Sat–Sun)
Daily contacts = 800

Raw handle time:
- 800 × 7.5 = 6,000 minutes
- 6,000 / 60 = **100 handle-hours**

Apply 120% staffing factor:
- 100 × 1.2 = **120 productive hours**

Gross up for 80% productivity:
- 120 / 0.8 = **150 paid hours/day**

Split equally across 2 shifts:
- 150 / 2 = **75 paid hours per shift**

Convert to 8-hour agent shifts:
- 75 / 8 = 9.375 → **10 agents per shift**

So for each weekend day:
- **Morning: 10 agents**
- **Evening: 10 agents**

Daily total = **20 agents scheduled across the two shifts**

---

# 6) Check weekly shift totals against 45 agents
Total shift assignments required:

- Weekdays: 5 days × 38 = **190 shift assignments**
- Weekend: 2 days × 20 = **40 shift assignments**

Total = **230 shift assignments**

Each agent can work 5 shifts/week, so:

- 230 / 5 = **46** if every shift assignment were perfectly balanced among the same pool

But we must be careful: the 45-agent figure came from total paid hours, while the shift rounding may create a small extra requirement because we cannot staff fractions of people on shifts.

Let’s test feasibility.

---

# 7) Is 45 agents enough under the shift constraints?
A schedule is feasible only if the total number of assignable weekly shifts from 45 agents is at least the number required.

- 45 agents × 5 shifts each = **225 shift slots available**
- Required shift assignments = **230**

So **45 agents is not enough** to cover all required shift assignments.

Therefore, we need one more agent:

- 46 agents × 5 shifts = **230 shift slots available**

This exactly matches the required number of shift assignments.

---

# 8) Final answer

## Minimum total number of agents hired:
**46 agents**

## Why not 45?
- Hour-based calculation suggests 45 agents
- But once you convert to whole 8-hour shifts and enforce “no fractional person per shift,” the schedule needs **230 shift assignments**
- 45 agents can only supply **225 shifts**
- So 45 is insufficient

## Is a valid schedule achievable?
**Yes.** With 46 agents, a valid schedule is achievable.

A simple feasibility check:
- Each weekday needs **19 morning + 19 evening**
- Each weekend day needs **10 morning + 10 evening**
- Total shift demand = **230**
- Total available shift supply with 46 agents working 5 shifts each = **230**

So the staffing plan is exactly feasible.

---

## Staffing requirement summary

| Day type | Total paid hours/day | Morning shift | Evening shift |
|---|---:|---:|---:|
| Mon–Fri | 300 | 19 agents | 19 agents |
| Sat–Sun | 150 | 10 agents | 10 agents |

---

If you want, I can also show one example of how the 46 agents could be assigned across the week without violating the “no morning and evening on the same day” rule.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
