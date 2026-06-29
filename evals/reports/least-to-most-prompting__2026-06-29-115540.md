# Eval: least-to-most-prompting

**Date:** 2026-06-29 11:55 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.1 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4.1 (Solid)** | 4 | 4 | 4 | 4 | 5 | 5 | 3 |
| gemini-2.5-flash | **4.3 (Solid)** | 5 | 4 | 4 | 4 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> Solid overall performance: all three runs apply the two critical transformations correctly (×1.2 service multiplier on productive hours, then ÷0.8 for paid-hour gross-up), reach the correct per-shift staffing (19 weekday, 10 weekend), compute 230 total shift-slots, and conclude 46 agents with a feasible schedule. The two-phase format with ordered decomposition and explicit carry-forwards is well-executed in Runs 2 and 3. Run 1 is penalized for an intermediate wrong answer (45 agents based on unrounded 225 shifts) that required awkward self-correction, adding ~200 tokens of waste. Across all runs, the feasibility analysis is shallower than the reference requires—none explicitly proves that the 38-distinct-agent weekday peak is non-binding relative to the 46-agent pool, and none flags the 100% utilization tightness as a scheduling risk. The 'staffing table' appears as bullet text rather than a formatted table in all runs, a minor but consistent format deviation.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The typical answer is largely correct on the core arithmetic and final result, but the runs contain a substantive internal error before self-correcting: Run 1 initially claims 45 agents and only later revises to 46 after reconciling rounded shift counts; Run 2 briefly states 38 agents as a candidate before correcting to 46; Run 3 is clean and correct. Because the outputs ultimately land on the right final staffing and feasibility conclusion, but with visible missteps and some muddled reasoning around the binding headcount check, this is not a 5. |
| Completeness | 4 | judge | All required substantive elements are present in the typical output: ordered decomposition, stepwise solution, per-shift staffing table, and final answer with feasibility. However, Run 1’s Phase 1 does not explicitly list sub-problems in easiest-to-hardest order with clear consumption links as requested; it is acceptable but weaker than the rubric’s ideal, and its initial conclusion is internally inconsistent before correction. Run 2 and Run 3 more cleanly satisfy the structure, but the set as a whole is slightly inconsistent in how fully it addresses the feasibility reconciliation demanded by the reference. |
| Format Compliance | 4 | judge | The outputs follow the requested two-phase structure and include the per-shift staffing information and final answer. The main deviation is that Run 1’s Phase 1 is not presented as a clean, explicitly ordered list before any solving in the same polished way as the prompt asked, and the final response is not a concise audited solution but a long derivation with a self-correction. Still, the overall shape is right across runs, so this is near but not exact. |
| Consistency | 4 | judge | All three runs produce identical final answers (46 agents, yes feasible, 19/19 weekday per shift, 10/10 weekend per shift) and follow the same two-phase structure with the same logical decomposition. The mathematical steps are semantically identical across runs. The main inconsistency is structural quality: Run 1's reasoning path is internally messy with an intermediate wrong answer and self-correction, while Runs 2 and 3 proceed cleanly. This affects the quality and auditability of the reasoning path, though not the final conclusions. [lexical similarity ratio: 0.176] |
| Tone/Style | 5 | judge | All three runs maintain a precise, quantitative, operations-analyst voice throughout. Calculations are shown with LaTeX-formatted equations, every number is labeled and traced, intermediate results are named and carried forward with explicit notation. No hand-waving or hedging. The language is professional and auditable, exactly matching the intended workforce-planning analyst audience. |
| Safety | 5 | judge | The content is benign, domain-appropriate workforce planning arithmetic with no harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The outputs are materially bloated relative to the task. The prompt asked for a two-phase solution with a table and final answer; the model instead emits long, highly verbose derivations and, in Run 1 and Run 2, spends many tokens exploring and correcting intermediate miscounts. This is especially inefficient given the target is a straightforward arithmetic/planning problem and the token counts are high (1986, 1710, 1600 output tokens). |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Completeness | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Format Compliance | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Consistency | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Tone/Style | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 4 | 4 | 2 | 0.94 |

- **Self-preference delta:** -6 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency, Consistency.
- **Panel mean spread/dim:** 1.14 (max 2).

Tokens (avg output): 1765 | Latency (avg): 10.49s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The pattern performs very well in Runs 1 and 2, which fully execute the least-to-most decomposition, chain all numeric results correctly, include the required staffing table, and deliver a rigorous feasibility reconciliation — earning high marks on accuracy, completeness, format, and tone. Run 3 is the weak link: it reproduces all correct intermediate values but hits the token ceiling during an over-ambitious explicit schedule construction, leaving the response incomplete with no final answer. The consistent failure mode across runs is a tendency toward verbose feasibility proofs (Gale-Ryser theorem in Run 1; repeated failed construction attempts in Run 3), which hurts efficiency and caused the truncation in Run 3. Structural and semantic consistency across the two complete runs is excellent; Run 3's truncation introduces a meaningful divergence in completeness and format.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | Core quantitative result is correct in all three runs: 46 agents and the per-shift staffing table (19/19 weekdays, 10/10 weekends) matches the reference. However, the feasibility analysis is handled unevenly and sometimes overexplained or partially incorrect in mechanism. Run 1 and Run 2 claim feasibility via schedule constructions that are not fully demonstrated; Run 3 is truncated before the final construction is completed. The most important numerical chain is right, but the proof of achievability is weaker than the reference’s required reconciliation. |
| Completeness | 4 | judge | Runs 1 and 2 cover every required element: Phase 1 decomposition with consumption annotations, Phase 2 step-by-step solutions with carried-forward numerics, the per-shift-per-day table, the 230-agent-shift total, the 46-agent minimum, and a completed feasibility reconciliation. Run 3 is truncated at 4096 tokens, ending mid-table in the group-construction attempt ('U-Wed') without a final answer block or feasibility conclusion. None of the runs explicitly compute the weekly aggregate of 1,200 agent-hours before decomposing to daily figures, a minor omission. |
| Format Compliance | 4 | judge | Runs 1 and 2 exactly satisfy the format specification: two explicitly labeled phases, Phase 1 as an ordered numbered list with consumption annotations, Phase 2 solving in the same order with explicit restatement of carried-forward numerics at each step, a per-shift-per-day table, and a single clearly labeled final answer with agents + feasibility verdict. Run 3 has the correct structure through SP9 but is truncated, leaving no final answer block — a structural incompletion that violates the format requirement. |
| Consistency | 4 | judge | Runs 1 and 2 are highly consistent: same Phase 1/Phase 2 structure, same numeric answers at every step (200/100→240/120→300/150→150/75→19/10→230→46), same feasibility conclusion (Yes), and same per-shift table. Run 3 agrees on all numeric answers through SP9 and begins the same feasibility argument, but diverges structurally by failing to complete and produce a final answer. The low lexical-similarity ratio (0.131) reflects paraphrase, not semantic divergence in the two successful runs. [lexical similarity ratio: 0.131] |
| Tone/Style | 5 | judge | All three runs sustain a precise, quantitative operations-analyst register throughout: mathematical notation (⌈⌉ ceiling, ÷, ×), labeled formulas, structured tables, and explicit numeric carry-forwards. No hand-waving or informal language. Run 1's invocation of the Gale-Ryser theorem is a slight academic elevation but remains appropriate for an auditable workforce-planning document. |
| Safety | 5 | judge | The content is benign, domain-appropriate workforce planning math with no harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | Run 2 (2581 tokens) is reasonably tight. Run 1 (3120 tokens) adds value with a Gale-Ryser proof and binary matrix analysis, but this extends well beyond what the problem requires and represents mild padding. Run 3 (4096 tokens) is the clearest efficiency failure: it attempts a verbose explicit group-construction, discovers an error mid-way ('14 ✗'), restarts, and still hits the token ceiling without completing the task — wasting tokens and delivering an incomplete output. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 3 | 5 | 5 | 2 | 0.94 |
| Completeness ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Format Compliance | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Consistency ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 3 | 4 | 2 | 0.82 |

- **Self-preference delta:** +2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Format Compliance, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.86 (max 3).

Tokens (avg output): 3266 | Latency (avg): 54.87s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Correct, complete, and format-compliant with strong analytical tone and consistent results across runs. Main weakness is severe inefficiency due to excessive verbosity and repetition.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | The runs are mathematically correct and on-task. They correctly compute 12,000/6,000 minutes, 200/100 hours, apply 1.2, divide by 0.8, split shifts, round up to 19 and 10 agents per shift, sum to 230 weekly shift-slots, and conclude 46 agents. They also correctly treat the no-same-day-both-shifts rule as requiring distinct agents per day and verify feasibility since 46 >= 38 weekday distinct agents. |
| Completeness | 4 | judge | All required elements are present: the ordered two-phase structure, carried-forward inputs in each step, the per-shift-per-day staffing table, the final total agents, and a feasibility yes/no answer. The response also includes the weekday/weekend breakdown and reconciles the daily distinct-agent constraint with the weekly headcount. |
| Format Compliance | 4 | judge | All runs include two explicitly labeled phases, an ordered numbered list in Phase 1 with dependency annotations, explicit carry-forward restating in Phase 2, and a final summary answer. The minor deviation is that the per-shift-per-day 'table' is rendered as bulleted or itemized lists rather than a proper tabular grid, which is close but not an exact table format. |
| Consistency | 4 | judge | All three runs reach identical numeric answers (46 agents, feasible, 19/19 weekday shifts, 10/10 weekend shifts) and apply the same core logic with the same structure. The main variation is in Phase 1 granularity: Run 1 decomposes into 11 sub-problems (splitting minutes and hours conversions separately), Run 3 into 9, and Run 2 into 7. This is a structural difference in Phase 1 but does not affect Phase 2 quality or correctness. [lexical similarity ratio: 0.129] |
| Tone/Style | 5 | judge | The tone is precise, quantitative, and auditable, matching the operations-analyst audience. The reasoning is explicit and numerically grounded, without hand-waving or casual language. |
| Safety | 5 | judge | The content is benign business/operations analysis with no harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The output token counts are consistently very high (8009, 7981, 8441 tokens). While the detailed step-by-step breakdown and restatement of inputs (as requested by the prompt) naturally increase verbosity, the extensive token counts also stem from the model's chosen level of detail. Specifically, the verbose day-by-day listing for the staffing table in Runs 2 and 3 contributed to noticeable padding, when a more concise summary would have sufficed and been more 'tight'. Even Run 1, with its more concise table, produced a large number of tokens, suggesting a general verbosity that could be optimized without sacrificing quality for this type of problem. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Completeness | 4 | 5 | 5 | 3 | 2 | 0.94 |
| Format Compliance | 4 | 5 | 4 | 4 | 1 | 0.47 |
| Consistency | 4 | 5 | 4 | 3 | 2 | 0.82 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 3 | 1 | 4 | 3 | 3 | 1.25 |

- **Self-preference delta:** -4.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Completeness, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.29 (max 3).

Tokens (avg output): 8144 | Latency (avg): 33.32s | Runs: 3

---

## Prompt Under Test

```text
Solve this problem in two phases.

Phase 1 - Decompose: Break the problem into an ordered sequence of sub-problems, from easiest to hardest, where each sub-problem builds on the previous one. List the full ordered sequence FIRST, before solving anything. Each sub-problem in the list must name which earlier sub-problem's result it consumes as input.

Phase 2 - Solve in order: Answer each sub-problem in sequence. For every sub-problem after the first, explicitly restate the numeric result(s) you are carrying forward from the prior sub-problem(s) and show how they enter this step's calculation. End with the final answer.

Problem: A customer-support center is planning next week's staffing for a single skill queue. The forecast is 9,600 contacts over the week, distributed as: Mon-Fri 1,600/day and Sat-Sun 800/day. Each contact takes an average handle time of 7.5 minutes. The service target requires staffing to 120% of the raw handle-time workload to absorb queueing and variability (this multiplier is applied to handle-time hours only). Separately, agents are only productively available 80% of their paid time (the other 20% is breaks, training, and after-call admin), so paid hours must be grossed up accordingly. Agents work 8-hour paid shifts, 5 shifts per week. Within a day, the workload splits into two equal shifts (a morning shift and an evening shift), and you cannot staff a fractional person on any shift. Finally, a hard rule: no single agent may be scheduled for both the morning and the evening shift on the same day. Question: What is the minimum total number of agents that must be hired for the week, and is a valid schedule actually achievable under all the constraints? Show the staffing requirement per shift per day along the way.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
## Phase 1 — Decompose

1. **Compute weekly handle-time workload**  
   - Uses: none  
   - Output: total weekly handle-time hours.

2. **Apply the 120% service-target multiplier to get required productive hours**  
   - Uses: result of Sub-problem 1  
   - Output: required productive hours for the week.

3. **Gross up for 80% productivity to get paid hours required**  
   - Uses: result of Sub-problem 2  
   - Output: total paid hours needed for the week.

4. **Convert weekly paid hours into required 8-hour agent-shifts**  
   - Uses: result of Sub-problem 3  
   - Output: total number of paid 8-hour shifts needed.

5. **Split the requirement into daily and per-shift staffing counts**  
   - Uses: result of Sub-problem 4  
   - Output: minimum staff needed per shift for Mon–Fri and Sat–Sun.

6. **Check whether the daily shift counts can be covered by unique agents under the no-double-shift rule**  
   - Uses: result of Sub-problem 5  
   - Output: minimum total number of agents hired and whether a feasible schedule exists.

---

## Phase 2 — Solve in order

### 1) Weekly handle-time workload

There are:
- Mon–Fri: \(5 \times 1{,}600 = 8{,}000\) contacts
- Sat–Sun: \(2 \times 800 = 1{,}600\) contacts

Total weekly contacts:
\[
8{,}000 + 1{,}600 = 9{,}600
\]

Each contact takes 7.5 minutes, so total handle time:
\[
9{,}600 \times 7.5 = 72{,}000 \text{ minutes}
\]

Convert to hours:
\[
72{,}000 \div 60 = 1{,}200 \text{ hours}
\]

**Result carried forward:** weekly raw handle-time workload = **1,200 hours**

---

### 2) Apply the 120% service-target multiplier

We carry forward **1,200 hours** from Step 1.

Required productive hours:
\[
1{,}200 \times 1.2 = 1{,}440 \text{ hours}
\]

**Result carried forward:** required productive hours = **1,440 hours**

---

### 3) Gross up for 80% productive availability

We carry forward **1,440 productive hours** from Step 2.

Since agents are productive only 80% of paid time:
\[
\text{Paid hours required} = \frac{1{,}440}{0.8} = 1{,}800 \text{ hours}
\]

**Result carried forward:** total paid hours needed = **1,800 hours**

---

### 4) Convert weekly paid hours into 8-hour agent-shifts

We carry forward **1,800 paid hours** from Step 3.

Each shift is 8 paid hours:
\[
1{,}800 \div 8 = 225 \text{ shifts}
\]

So the week requires **225 paid 8-hour shifts** total.

**Result carried forward:** total required shifts = **225 shifts**

---

### 5) Split into daily and per-shift staffing counts

We carry forward **225 shifts** from Step 4.

The workload is split into 7 days with two equal shifts per day, so there are:
\[
7 \times 2 = 14 \text{ shifts per week}
\]

Average required staffing per shift:
\[
225 \div 14 = 16.0714\ldots
\]

Since you cannot staff a fractional person on a shift, each shift must be rounded up to meet demand.  
But the demand is not uniform across the week because Mon–Fri are heavier than Sat–Sun, so we compute by day from contacts.

#### Monday–Friday
Daily contacts = 1,600  
Daily handle time:
\[
1{,}600 \times 7.5 = 12{,}000 \text{ minutes} = 200 \text{ hours}
\]
Apply 120%:
\[
200 \times 1.2 = 240 \text{ productive hours}
\]
Gross up for 80% productivity:
\[
240 \div 0.8 = 300 \text{ paid hours}
\]
Split into 2 shifts:
\[
300 \div 2 = 150 \text{ paid hours per shift}
\]
Convert to 8-hour agents:
\[
150 \div 8 = 18.75 \Rightarrow 19 \text{ agents per shift}
\]

#### Saturday–Sunday
Daily contacts = 800  
Daily handle time:
\[
800 \times 7.5 = 6{,}000 \text{ minutes} = 100 \text{ hours}
\]
Apply 120%:
\[
100 \times 1.2 = 120 \text{ productive hours}
\]
Gross up for 80% productivity:
\[
120 \div 0.8 = 150 \text{ paid hours}
\]
Split into 2 shifts:
\[
150 \div 2 = 75 \text{ paid hours per shift}
\]
Convert to 8-hour agents:
\[
75 \div 8 = 9.375 \Rightarrow 10 \text{ agents per shift}
\]

So the staffing requirement per shift per day is:

- **Mon–Fri:** 19 agents on morning shift, 19 agents on evening shift
- **Sat–Sun:** 10 agents on morning shift, 10 agents on evening shift

---

### 6) Check feasibility and minimum total agents hired

We carry forward the per-shift requirements:
- **Mon–Fri:** 19 + 19 = 38 agent-shifts per day
- **Sat–Sun:** 10 + 10 = 20 agent-shifts per day

Now check the no-double-shift rule: no agent may work both shifts on the same day.

That means each day’s two shifts must be covered by distinct people, but an agent can work one shift per day and can work on multiple days during the week. So the feasibility question is whether enough distinct agents exist to cover the busiest day.

The maximum simultaneous staffing needed on any single day is:
- **38 agents/day** on Mon–Fri

Thus the minimum headcount must be at least **38 agents**, because on a heavy weekday you need 38 distinct people that day and no one can cover both shifts.

Can 38 agents actually cover the whole week?

Check total capacity with 38 agents, each working 5 shifts/week:
\[
38 \times 5 = 190 \text{ shifts}
\]

But the week requires:
\[
225 \text{ shifts}
\]

So 38 agents are **not enough**.

Next try 45 agents:
\[
45 \times 5 = 225 \text{ shifts}
\]

This exactly matches the weekly shift requirement. Also, the daily peak is only 38, and 45 agents can cover the weekday and weekend pattern while ensuring no one works both shifts on the same day. So a valid schedule is achievable.

Therefore:

- **Minimum total number of agents hired = 45**
- **Yes, a valid schedule is achievable**

A simple feasibility check:
- Weekday demand: 38 agents/day for 5 days = 190 shifts
- Weekend demand: 20 agents/day for 2 days = 40 shifts
- Total: 230? Wait — careful: weekday demand is 19 per shift × 2 shifts × 5 days = 190 shifts, weekend demand is 10 × 2 × 2 = 40 shifts, total = 230 shifts.

But earlier we computed 225 shifts from weekly hours. The difference comes from rounding up each shift separately. Let’s reconcile this correctly:

- Mon–Fri daily paid hours = 300, split into 2 shifts = 150 per shift = 18.75 → 19 each shift  
  Weekly weekday shifts = \(5 \times 2 \times 19 = 190\)

- Sat–Sun daily paid hours = 150, split into 2 shifts = 75 per shift = 9.375 → 10 each shift  
  Weekly weekend shifts = \(2 \times 2 \times 10 = 40\)

Total rounded staffing requirement:
\[
190 + 40 = 230 \text{ agent-shifts}
\]

Since each agent can work 5 shifts/week, the headcount needed is:
\[
230 \div 5 = 46
\]

And 46 agents produce:
\[
46 \times 5 = 230 \text{ shifts}
\]

This matches exactly.

So the corrected minimum total number of agents is:

## Final answer

- **Staffing per shift per day:**
  - **Mon–Fri:** 19 agents per shift, 2 shifts/day
  - **Sat–Sun:** 10 agents per shift, 2 shifts/day

- **Minimum total number of agents to hire:** **46**

- **Is a valid schedule achievable?** **Yes.**  
  Since each agent works at most one shift per day and up to 5 shifts per week, 46 agents can cover the required 230 rounded shift assignments exactly.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
