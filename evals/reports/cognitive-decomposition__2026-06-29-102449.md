# Eval: cognitive-decomposition

**Date:** 2026-06-29 10:24 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **5 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| claude-sonnet-4-6 | **4.9 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| gemini-2.5-flash | **4.3 (Solid)** | 3 | 5 | 5 | 3 | 5 | 5 | 4 |

---

## Scorecard: gpt-5.4-mini

> All three runs execute the cognitive-decomposition pattern flawlessly: they avoid both headline traps (average-not-peak and I/O-not-CPU binding), produce arithmetically consistent intermediate results, and land on the exact reference answer (59 replicas, $62,451.50/month). Format compliance and consistency are perfect; the only deductions are a slightly informal opening phrase in all runs (tone: −1) and minor restatement padding in each step's result block (efficiency: −1). Overall this is an exemplary performance of structured quantitative decomposition.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs are factually correct and on-task. They correctly compute peak load as 57,600 QPS, identify CPU as the binding constraint at 1,000 QPS/server, size to 58 servers for peak, add N+1 to 59, and calculate the monthly cost as $62,451.50. No arithmetic or conceptual errors are present. |
| Completeness | 5 | judge | The response set covers every required element: sequential decomposition, intermediate numeric steps, the binding constraint, the pre- and post-N+1 replica counts, and the monthly cost. The final answers explicitly include all requested outputs. |
| Format Compliance | 5 | judge | The outputs follow the requested structure: labeled sequential steps with numeric results before the final answer, and no premature final answer. The final answer appears only after all steps and includes the required fields. |
| Consistency | 5 | judge | The runs are semantically and structurally consistent across repetitions. They agree on all key steps, intermediate values, and final results; variation is only in wording and phrasing, not meaning or quality. [lexical similarity ratio: 0.43] |
| Tone/Style | 5 | judge | The tone is precise, technical, and explanatory, matching the engineer-peer-review audience. It is neutral and not chatty. |
| Safety | 5 | judge | The outputs are clean, non-harmful, and free of biased or inappropriate content. They only contain benign capacity-planning calculations. |
| Efficiency | 5 | judge | The token use is appropriate for the required step-by-step decomposition and exact numeric justification. There is little wasted verbiage beyond necessary exposition, and the output quality is high. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Format Compliance ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Consistency ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |

- **Self-preference delta:** +2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.71 (max 1).

Tokens (avg output): 764 | Latency (avg): 6.12s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> All three runs are essentially perfect executions of the cognitive-decomposition pattern against a tricky multi-constraint capacity planning problem. Every reference answer number is hit exactly (57,600 peak QPS; 1,000 QPS/server CPU ceiling; 10,000 QPS/server I/O ceiling; CPU identified as binding; 58 servers pre-N+1; 59 post-N+1; $62,451.50/month). The format specification is satisfied in full — numbered, labeled, input-citing steps precede the final answer table. Tone is pitch-perfect for an engineering peer review. Consistency across the three runs is very high despite low lexical overlap, as all runs share the same structure, numbers, and conclusions. The only minor deduction is in efficiency, where a closing narrative paragraph in each run lightly re-summarizes the already-complete table above it, adding ~80-100 tokens of partial redundancy.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs correctly solve the sizing problem, identify CPU as the binding constraint, compute 57,600 peak QPS, 58 servers before redundancy, 59 with N+1, and $62,451.50/month. No factual or arithmetic errors appear in the final conclusions. |
| Completeness | 5 | judge | The response set covers every required element: sequential decomposition, peak calculation, CPU and I/O capacity, binding constraint, pre- and post-N+1 replica counts, and monthly cost. Each run includes a final answer after the steps, satisfying the full task. |
| Format Compliance | 5 | judge | The outputs follow the requested sequential, labeled-step format with numeric intermediate results before the final answer. The final answer appears only after all steps and explicitly states the binding constraint, replica counts, and cost. The structure is consistent with the prompt’s formatting requirements. |
| Consistency | 5 | judge | Across runs, the semantic content, structure, and quality are stable: all compute the same peak, same per-server CPU/I/O capacities, same binding constraint, same pre/post-N+1 counts, and same monthly cost. Wording varies, but the reasoning chain and outputs are consistent. [lexical similarity ratio: 0.21] |
| Tone/Style | 5 | judge | The tone is precise, technical, and explanatory, matching an engineer doing capacity planning for peer review. It is neutral and not chatty, with clear quantitative reasoning throughout. |
| Safety | 5 | judge | The content is benign, non-sensitive, and free of harmful, biased, or inappropriate material. It is purely a capacity-planning calculation. |
| Efficiency | 4 | judge | The outputs are reasonably efficient for the required depth, but they are somewhat verbose and contain repeated verification and summary text beyond what was strictly necessary. The token counts are moderate-to-high for a straightforward calculation, though still justified by the stepwise decomposition requirement. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 4 | 5 | 1 | 0.47 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.14 (max 1).

Tokens (avg output): 1098 | Latency (avg): 18.72s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs demonstrate correct reasoning: they decompose the problem into well-labeled sequential steps, avoid the average-QPS trap (sizing to 57,600 not 18,000), correctly identify CPU as the binding constraint at 1,000 QPS/server (vs I/O at 10,000), and land on 59 replicas with N+1. Format and tone are excellent across all runs. The critical flaw is arithmetic instability in the final multiplication: only Run 1 computes the correct monthly cost of $62,451.50; Runs 2 and 3 produce $62,400.50 and $62,376.50 respectively, errors that persist despite stating the correct formula. This degrades accuracy to a 3 and reveals meaningful run-to-run inconsistency on a core deliverable.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | The runs correctly identify the peak QPS, CPU as the binding constraint, and the replica count before N+1. However, two runs miscalculate the monthly cost, and one run shows an internal arithmetic error in the CPU-demand derivation even though it later lands on the right throughput. The typical final answer is therefore only partially accurate. |
| Completeness | 5 | judge | Every requirement is addressed in all three runs: peak QPS, per-server CPU throughput, per-server I/O throughput, explicit binding constraint identification, pre-N+1 server count, post-N+1 server count, and total monthly cost. The final answer in each run restates (a) binding constraint, (b) pre/post-N+1 counts, and (c) monthly cost. |
| Format Compliance | 5 | judge | All three runs use clearly numbered, labeled steps; each step cites inputs as either stated facts or prior step results; intermediate numeric results are shown before proceeding; the final answer appears only after all steps and separately states binding constraint, before/after N+1 replica count, and monthly cost. |
| Consistency | 3 | judge | Structure, step count, intermediate results, binding constraint, and server counts (58/59) are stable across all three runs. However, the final cost differs in all three runs ($62,451.50 vs $62,400.50 vs $62,376.50), which is a direct inconsistency in a key deliverable. This represents quality instability beyond mere wording variation. [lexical similarity ratio: 0.313] |
| Tone/Style | 5 | judge | The tone is consistently precise, technical, quantitative, and explanatory, matching an engineer performing capacity planning. It is neutral and non-chatty throughout. |
| Safety | 5 | judge | The outputs are free of harmful, biased, or inappropriate content. They are ordinary quantitative analyses. |
| Efficiency | 4 | judge | Token counts of 3085–3417 are commensurate with the 10–11 required labeled steps and the format specification's explicit demands for citing inputs, showing calculations, and restating results. Some minor structural verbosity (e.g., Run 1 Step 10 is a near-redundant restatement of the binding constraint already captured in Step 7), but no significant padding. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Completeness ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Format Compliance ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |

- **Self-preference delta:** +3.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Efficiency.
- **Panel mean spread/dim:** 0.86 (max 3).

Tokens (avg output): 3276 | Latency (avg): 14.38s | Runs: 3

---

## Prompt Under Test

```text
Break this problem into smaller steps. Solve each step sequentially, showing the numeric result of each step before moving to the next, and only after all steps are solved give the final answer. Each step's inputs must come from the stated facts or from an earlier step's result (state which).

Problem: We are sizing a fleet of identical Postgres read-replica servers for a product launch and need the minimum number of replicas and the resulting monthly compute cost. Use these facts:

- Expected steady-state read traffic at launch: 18,000 read queries per second (QPS), averaged over the day.
- Traffic is bursty: the daily PEAK is 3.2x the daily average, and the fleet must be sized to survive the peak without exceeding any per-server limit.
- Each read query, on average, requires 4 logical I/O page reads and 12 ms of CPU service time on a single core.
- Each server has 16 CPU cores. To leave headroom for replication and GC, you may load each core to at most 75% utilization (i.e. usable CPU = cores x 0.75).
- Each server can sustain at most 40,000 logical page reads per second before its buffer-cache/storage path saturates (this is a hard per-server ceiling, independent of CPU).
- You must keep N+1 redundancy: the fleet must still handle peak load with one server failed.
- Each server costs $1.45 per hour and billing is hourly; assume 730 hours in a month.

Compute the minimum number of replicas required and the total monthly cost of the fleet. Be explicit about which resource (CPU or I/O) is the binding constraint at peak, and how N+1 changes the count.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Below I’ll solve it step by step, using only the stated facts or results from earlier steps.

## Step 1: Compute peak read QPS
**Input from problem:**  
- Average read traffic = 18,000 QPS  
- Peak = 3.2 × average

**Calculation:**  
18,000 × 3.2 = **57,600 QPS**

**Result:**  
- **Peak demand = 57,600 read QPS**

---

## Step 2: Compute per-server CPU capacity
**Input from problem:**  
- 16 CPU cores/server  
- Usable CPU per core = 75%  
- Each read query needs 12 ms of CPU service time on a single core

First compute usable core count:
- 16 × 0.75 = **12 usable cores**

Now compute queries/sec per core:
- 1 second / 12 ms = 1 / 0.012 = **83.333... QPS per core**

So per server:
- 12 × 83.333... = **1,000 QPS per server**

**Result:**  
- **CPU capacity per server = 1,000 QPS**

---

## Step 3: Compute per-server I/O capacity in QPS
**Input from problem:**  
- Each query requires 4 logical I/O page reads  
- Each server can sustain at most 40,000 logical page reads/sec

Convert page-read ceiling into query ceiling:
- 40,000 / 4 = **10,000 QPS per server**

**Result:**  
- **I/O capacity per server = 10,000 QPS**

---

## Step 4: Determine the binding constraint at peak
**Inputs from earlier steps:**  
- Peak demand = 57,600 QPS  
- CPU capacity/server = 1,000 QPS  
- I/O capacity/server = 10,000 QPS

The tighter limit is CPU, because:
- 1,000 QPS < 10,000 QPS

So **CPU is the binding constraint**.

**Result:**  
- **Binding constraint at peak: CPU**

---

## Step 5: Compute number of servers needed to handle peak load without failure
**Input from earlier step:**  
- Peak demand = 57,600 QPS  
- Binding per-server capacity = 1,000 QPS

Servers required with no failure:
- 57,600 / 1,000 = **57.6**, so round up to **58 servers**

**Result:**  
- **58 servers needed to handle peak load normally**

---

## Step 6: Apply N+1 redundancy
**Input from problem and earlier result:**  
- Must still handle peak load with one server failed  
- Need 58 servers to handle peak normally

For N+1, total fleet must have one extra server beyond the minimum needed to survive peak:
- 58 + 1 = **59 servers**

**Result:**  
- **Minimum fleet size with N+1 = 59 replicas**

---

## Step 7: Compute monthly cost
**Input from problem:**  
- Cost per server = $1.45/hour  
- 730 hours/month  
- Fleet size = 59 servers

Cost per server per month:
- 1.45 × 730 = **$1,058.50**

Total fleet cost:
- 59 × 1,058.50 = **$62,451.50**

**Result:**  
- **Monthly fleet cost = $62,451.50**

---

# Final answer
- **Binding constraint at peak:** CPU  
- **Minimum number of replicas required (with N+1 redundancy):** **59**
- **Total monthly compute cost:** **$62,451.50**
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
