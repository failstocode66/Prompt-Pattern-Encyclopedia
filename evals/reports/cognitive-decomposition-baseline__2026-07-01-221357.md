# Eval: cognitive-decomposition-baseline

**Date:** 2026-07-01 22:13 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.7 (Strong)** | 5 | 5 | 5 | 4 | 5 | 5 | 4 |
| claude-sonnet-4-6 | **4.9 (Strong)** | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| gemini-2.5-flash | **4.3 (Solid)** | 4 | 5 | 5 | 3 | 5 | 5 | 3 |

---

## Scorecard: gpt-5.4-mini

> The response set is correct, complete, well-formatted, and consistent across runs. It clearly performs the required dependency-ordered capacity planning and reaches the expected 59-replica, $62,451.50/month result, with only mild verbosity reducing efficiency slightly.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs correctly compute the peak load, CPU and I/O capacities, identify CPU as the binding constraint, apply N+1 to reach 59 replicas, and arrive at the correct monthly cost of $62,451.50. No factual errors or arithmetic mistakes are present in the typical behavior. |
| Completeness | 5 | judge | The responses cover every required element: peak calculation, CPU capacity, I/O capacity, binding constraint, servers before and after N+1, and total monthly cost. The final answers explicitly state all requested outputs. |
| Format Compliance | 5 | judge | The output follows the required sequential, labeled-step format and postpones the final answer until after the derivation. The final answer explicitly lists the binding constraint, replica counts before/after N+1, and monthly cost. |
| Consistency | 4 | judge | Across runs, the semantic content, structure, and quality are stable: each run follows the same decomposition, identifies CPU as the bottleneck, computes 58 then 59 servers, and lands on the same monthly cost. Variation is only superficial wording and ordering of equivalent intermediate math. [lexical similarity ratio: 0.25] |
| Tone/Style | 5 | judge | The tone is precise, technical, quantitative, and explanatory, matching an engineering peer-review audience. It is neutral and avoids chatty language. |
| Safety | 5 | judge | The content is benign, domain-appropriate capacity planning with no harmful, biased, or inappropriate material. |
| Efficiency | 4 | judge | The answers are high quality and fully correct, but somewhat verbose relative to the straightforward arithmetic task. The token counts (646–712) are longer than necessary for the delivered value, though not excessively wasteful. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Consistency ⚠ | 4 | 5 | 5 | 3 | 2 | 0.94 |
| Tone/Style ⚠ | 5 | 5 | 5 | 4 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 4 | 4 | 0 | 0.0 |

- **Self-preference delta:** +2 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Consistency.
- **Panel mean spread/dim:** 0.57 (max 2).

Tokens (avg output): 688 | Latency (avg): 4.99s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Strong, fully correct, and format-compliant response set. All runs solve the capacity-planning problem correctly, with consistent stepwise reasoning and the correct final count and cost. Minor verbosity keeps efficiency below perfect, but all other dimensions are excellent.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 5 | judge | All three runs are mathematically correct and on-task. They correctly compute peak QPS as 57,600, identify CPU as the binding constraint at 1,000 QPS/server, derive 58 servers for peak, add N+1 to reach 59, and compute the monthly cost as $62,451.50. No factual or arithmetic errors appear in the typical behavior across runs. |
| Completeness | 5 | judge | The response set covers every required element: sequential steps, peak load, CPU and I/O capacities, explicit binding constraint, raw server count, N+1 adjustment, and final monthly cost. It also states the final answer only after the steps, as required. |
| Format Compliance | 5 | judge | The outputs follow the specified format closely: sequential numbered steps with numeric intermediate results, then a final summary after the derivation. The final answer is not jumped to prematurely, and the required elements are clearly stated. Minor stylistic differences do not break the requested shape. |
| Consistency | 5 | judge | The runs are highly consistent in semantic and structural content. All three use the same step ordering, same intermediate results, same binding constraint, same raw and final server counts, and same cost. Differences are superficial wording or presentation only, not contradictions or quality shifts. [lexical similarity ratio: 0.375] |
| Tone/Style | 5 | judge | The tone is precise, technical, quantitative, and explanatory, matching an engineer doing capacity planning for peer review. It is neutral and not chatty, with appropriate terminology and clear stepwise reasoning. |
| Safety | 5 | judge | The content is benign and free of harmful, biased, or inappropriate material. It concerns capacity planning and cost estimation only. |
| Efficiency | 4 | judge | The outputs are a bit verbose relative to the straightforward arithmetic task, especially with repeated verification, tables, and restated summaries. That said, the extra tokens support clarity and explicitness, so this is mildly inefficient rather than wasteful. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Consistency | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 4 | 4 | 4 | 5 | 1 | 0.47 |

- **Self-preference delta:** -2.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.43 (max 1).

Tokens (avg output): 1025 | Latency (avg): 19.42s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> Mostly correct and well-formatted step-by-step capacity-planning answers, but Run 2 contains a material cost error, preventing top marks for accuracy and consistency.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are largely correct and on-task, with the right peak sizing, CPU-vs-I/O comparison, N+1 handling, and final replica count/cost in Runs 1 and 3. However, Run 2 has a significant arithmetic error in the cost calculation, giving $62,406.50 instead of the correct $62,451.50, which prevents a 5. |
| Completeness | 5 | judge | All required elements are present across the typical behavior: sequential labeled steps, numeric intermediate results, identification of the binding constraint, pre- and post-N+1 counts, and final monthly cost. The outputs also avoid the listed trap cases. |
| Format Compliance | 5 | judge | The responses follow the required sequential, labeled-step format before the final answer, and each final answer appears only after the steps. They do not jump straight to the answer or use an unstructured single-paragraph solve. |
| Consistency | 3 | judge | The core answer is stable across runs: peak 57,600 QPS, CPU-bound at 1,000 QPS/server, 58 before redundancy, 59 after N+1. However, Run 2 diverges on the final cost, reporting an incorrect monthly cost while the other runs report the correct one, so the runs are not fully consistent in quality and conclusion. [lexical similarity ratio: 0.279] |
| Tone/Style | 5 | judge | The tone is precise, technical, quantitative, and explanatory, matching an engineer doing capacity planning for peer review. It is neutral and not chatty. |
| Safety | 5 | judge | The content is benign and free from harmful, biased, or inappropriate material. |
| Efficiency | 3 | judge | The outputs achieve the correct structure and mostly correct solution, but they are verbose relative to the task, with substantial repetition and explanatory padding. Run 2 is especially long at 4039 tokens, and even the shorter runs use more words than needed for the required concise stepwise derivation. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 4 | 3 | 1 | 0.47 |
| Completeness | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Format Compliance | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Consistency | 3 | 3 | 3 | 3 | 0 | 0.0 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 3 | 3 | 0 | 0.0 |

- **Self-preference delta:** -1 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Panel mean spread/dim:** 0.14 (max 1).

Tokens (avg output): 3166 | Latency (avg): 13.95s | Runs: 3

---

## Prompt Under Test

```text
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
We size for the **daily peak**, then add **N+1 redundancy**.

## 1) Peak read load
Average steady-state QPS = 18,000  
Peak factor = 3.2×

\[
\text{Peak QPS} = 18{,}000 \times 3.2 = 57{,}600
\]

So the fleet must handle **57,600 read QPS** at peak.

---

## 2) Per-server capacity from CPU

Each query needs **12 ms of CPU time on a single core**.

A server has:

- 16 cores
- max usable utilization per core = 75%

Usable CPU time per second per server:

\[
16 \times 0.75 = 12 \text{ core-seconds of usable CPU per second}
\]

Each query consumes:

\[
12 \text{ ms} = 0.012 \text{ core-seconds/query}
\]

So CPU-limited QPS per server is:

\[
\frac{12}{0.012} = 1{,}000 \text{ QPS}
\]

---

## 3) Per-server capacity from I/O

Each query needs **4 logical page reads**.

Per-server I/O ceiling:

\[
40{,}000 \text{ page reads/sec}
\]

So I/O-limited QPS per server is:

\[
\frac{40{,}000}{4} = 10{,}000 \text{ QPS}
\]

---

## 4) Binding constraint at peak
Compare the two:

- CPU limit: **1,000 QPS/server**
- I/O limit: **10,000 QPS/server**

So **CPU is the binding constraint**.

---

## 5) Servers needed for peak load
Without redundancy:

\[
\frac{57{,}600}{1{,}000} = 57.6
\]

Round up:

\[
58 \text{ servers}
\]

---

## 6) Apply N+1 redundancy
You need the fleet to still handle peak load with **one server failed**, so the remaining **N-1** servers must still provide at least 58-server capacity.

Let total servers be \(N\). Then:

\[
N - 1 \ge 58
\]

\[
N \ge 59
\]

So the minimum fleet size is:

## **59 replicas**

---

## 7) Monthly cost
Each server costs:

\[
\$1.45/hour
\]

Monthly hours = 730

Cost per server per month:

\[
1.45 \times 730 = \$1{,}058.50
\]

For 59 servers:

\[
59 \times 1{,}058.50 = \$62{,}451.50
\]

---

# Final Answer
- **Binding constraint:** **CPU**
- **Servers required to handle peak:** 58
- **With N+1 redundancy:** **59 replicas**
- **Monthly fleet cost:** **$62,451.50**
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
