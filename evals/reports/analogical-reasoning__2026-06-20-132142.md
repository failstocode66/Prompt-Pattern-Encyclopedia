# Eval: analogical-reasoning

**Date:** 2026-06-20 13:21 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.3 (Solid)** | 4 | 4 | 4 | 5 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **4.3 (Solid)** | 4 | 4 | 5 | 4 | 5 | 5 | 3 |
| gemini-2.5-flash | **3.9 (Solid)** | 4 | 4 | 4 | 4 | 4 | 5 | 2 |

---

## Scorecard: gpt-5.4-mini

> Overall strong answers. They satisfy the requested analogy-first structure, use genuinely structural analogs, and derive a plausible centralized fair-share allocator with borrowing, urgency, and non-preemptive reclaim. The main misses are incomplete explicit treatment of graceful degradation as admission/triage and a somewhat verbose, repetitive presentation. Consistency across runs is good.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The responses are largely on-task and use genuinely structural analogs (WFQ/DRR, token-bucket, CPU fair-share) rather than surface keywords. They correctly map shared capacity, bursty demand, borrowing slack, and non-preemptive reclaim-at-completion. Minor accuracy issues remain: some claims overgeneralize the fit of CPU/network analogs to discrete drivers, and the solutions sometimes blur the distinction between driver-slots, driver-minutes, and actual non-preemptive route durations. Run 3 is especially strong; Run 1 and 2 are similarly correct but less explicit about the deadline/admission-control nuance. Evidence: Run 1: "Weighted fair queuing or an approximation such as deficit round robin"; "drivers are mobile resources with nontrivial trip durations". Run 2: "token-bucket + deficit round robin (DRR) / fair-share schedulers"; "we cannot preempt ongoing deliveries". Run 3: "Weighted Fair Queuing (WFQ), Deficit Round Robin (DRR), or ... Dominant Resource Fairness (DRF)"; "driver already mid-route is unavailable". |
| Completeness | 4 | judge | The runs cover the required two-stage structure, give 1-2 analogs, provide mappings, then derive a central allocation scheme with state, assignment, reclaim, and failure modes. They also mention non-preemption and fairness/borrowing. However, none fully nails the explicitly expected graceful-degradation-as-admission/triage detail; they mostly frame overload as fair sharing and waiting, with only partial acknowledgment that refunded orders/triage are needed. The required breakdowns around perishability, route time, deadline pressure, and coarse quanta are present but not always enumerated as directly as the prompt demands. Evidence: Run 1 says "orders expire after 30 minutes, so the system needs deadline-aware dispatch" but then the solution mostly uses queues and fair-share scoring. Run 2 says "the allocator becomes a weighted fair scheduler under scarcity" but does not explicitly develop admission/dropping/triage. Run 3 similarly says "latency-sensitive orders expiring" and "deadline-aware priority" without a concrete triage/drop policy. |
| Format Compliance | 4 | judge | All three runs follow the required prose-shaped, two-stage format with an analog stage preceding the solution stage, and they explicitly separate analogs from solution. They also enumerate mappings rather than only gesturing at them. The main deviation is that the prompt asked for one labeled block per recalled analog with explicit element-by-element mapping and explicit breakdowns; the responses comply mostly, but some mapping sections are less rigorously enumerated than requested, and the solution stage occasionally restates rather than strictly builds from the earlier mapping. Still, the overall shape is clearly correct. Evidence: Run 1 has "## Analog 1..." and "## Analog 2..." followed by "# Using the mapping to build a solution". Run 2 and Run 3 similarly present separate analog sections then a solution section. |
| Consistency | 5 | judge | Across all three runs, the structure (two analog blocks → solution), the choice of analogs (WFQ/network scheduling + CPU fair-share scheduling), the element-by-element mappings, the core mechanism (weighted fair-share allocator with borrowing, non-preemptive reclaim at completion boundaries), and the failure modes are stable. The quality of coverage and depth of treatment are similar across runs. Wording differs substantially (as expected), but meaning, structure, and quality are essentially identical. Minor variation (Run 3 adds DRF; Run 1's second analog is 'cloud cluster' vs. CPU) is semantically equivalent. [lexical similarity ratio: 0.025] |
| Tone/Style | 5 | judge | The tone consistently matches the requested audience: analytical, technically precise, and appropriately cautious about where the analogy transfers and where it breaks. The runs avoid salesy certainty and repeatedly flag partial transfer and non-preemption constraints. This is close to pitch-perfect for a senior systems/operations engineer thinking aloud to a peer. Evidence: Run 1: "Where it breaks down." Run 2: "This is the key adaptation from CPU/network analogs: we cannot preempt ongoing deliveries." Run 3: "We must adapt for the non-preemptive, perishable nature of drivers." |
| Safety | 5 | judge | The content is benign and operational in nature, with no harmful, biased, or inappropriate material. It concerns scheduling/allocation algorithms and stays within safe technical discussion. Evidence across runs shows no safety issues. |
| Efficiency | 3 | judge | All three runs are lengthy (2670–2889 tokens) and deliver substantive content, but there is noticeable padding. Each run ends with a redundant 'final recommended scheme' or 'short version' summary that largely repeats the solution already given. The 'if you want pseudocode' offers are pure waste. Within runs, some principles are restated in the requirements-satisfaction section that were already established in the algorithm section. The token counts are justified only partially by the complexity of the task; a tighter engineer-to-engineer answer covering the same ground could be 30–40% shorter. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Completeness | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Format Compliance | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Consistency | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 3 | 5 | 3 | 1.25 |

- **Self-preference delta:** -3 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Efficiency.
- **Panel mean spread/dim:** 1.43 (max 3).

Tokens (avg output): 2772 | Latency (avg): 19.8s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> Across all three runs the prompt pattern produces technically sound, correctly structured responses that genuinely identify the WFQ/max-min fairness analog, map it relation-by-relation with explicit breakdown flagging, and build the allocation scheme from the mapping rather than appending it as decoration. The format is consistently excellent and the tone is pitch-perfect for the target audience. The primary weaknesses are systematic rather than random: disanalogy #3 (lumpy quanta) is absent from every run; graceful degradation is never framed as an admission/triage problem (shedding orders that cannot make the deadline) but instead as proportional reduction; 'staleness of central state' and 'thrashing from aggressive reassignment' are not named as failure modes. Two of three runs hit the 4096-token ceiling and truncate before finishing, which simultaneously caps completeness and wastes the full token budget. Run 3 is the strongest individual output: it completes within budget, includes the geographic nearest-driver mechanism, and frames the 30-minute cliff as a distinct failure mode with an emergency override — but still shares the analog gaps of the other runs.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly identify WFQ/max-min fairness as the primary structural analog and map it relation-by-relation. Disanalogies #1 (travel/non-preemption) and #2 (deadline) are flagged across all runs. However, disanalogy #3 (lumpy indivisible quanta — driver ≈ several orders over an hour vs near-continuous bandwidth) is never explicitly named in any run. Graceful degradation is framed as proportional reduction and weight rebalancing rather than as an admission/triage problem (shed orders that cannot make the 30-min cutoff; analogous to AQM/deadline-aware dropping). The concrete mechanisms are technically sound and justified by the mappings, with no factual errors in formulas, complexity claims, or algorithm structure. |
| Completeness | 4 | judge | Most required pieces are present across the set: analog stage before solution, element-by-element mapping, algorithm, state, assignment/reclaim mechanics, failure modes, and explicit mention of some breakdowns. However, important requested details are shallow or inconsistently handled. In particular, graceful degradation as an admission/triage problem is only partially addressed; the prompt expected explicit dropping/admission decisions when demand exceeds supply, and only Run 1 comes close with triage language. The mapping stage is also sometimes followed by a solution that is not clearly built from it. The analog stage is visible and precedes the solution in all runs, but the solution does not always fully cover all of (a)-(d) in a way that is tightly derived from the mapping. |
| Format Compliance | 5 | judge | All three runs consistently deliver the two-stage structure the format requires: a clearly separated analog stage with individually labeled blocks (each containing the analogous problem, known solution, and element-by-element structural mapping with explicit breakdown flags), followed by a solution stage that visibly builds from those mappings. Mappings are enumerated in tables (not gestured at). The solution stage names the algorithm, specifies state, describes assignment and reclamation, and lists failure modes. The analogs are not decorative — the solution stages in all three runs explicitly cite the analog they are drawing on and name what they are not transferring. |
| Consistency | 4 | judge | All three runs share the same two-stage format, the same primary analog pair (WFQ/bandwidth + hospital ICU), the same core algorithm design (guaranteed floor + burst credit + priority scoring + degradation protocol), and the same coverage of requirements (a)-(d). The algorithm names differ (DWFA, DWDA, TMBC) but are semantically equivalent constructions. Failure modes vary in selection across runs but address compatible themes. The quality is structurally stable; two runs truncate at the same token limit, which is a consistent budget-management weakness. No run contradicts another on the core mechanics or analog selection. The disanalogy gaps are consistently present across all runs, indicating stable (if incomplete) behavior rather than random variation. [lexical similarity ratio: 0.051] |
| Tone/Style | 5 | judge | All three runs maintain the target register throughout: senior engineer thinking aloud to a peer. The intellectual honesty about partial transfers is consistent ('this is where the WFQ mapping partially breaks down,' 'no driver is recalled mid-route… this is the correct partial transfer'). Technical vocabulary is appropriate — WFQ, DRR, deficit counter, token bucket, max-min fairness, nearest-deadline-first, O(log N) — without either hand-waving or over-explaining basics. The tone is confident but not glib; the runs acknowledge uncertainty in tunable parameters and calibration. |
| Safety | 5 | judge | The content is operational/technical and does not contain harmful, biased, or inappropriate material. It is safe throughout. |
| Efficiency | 3 | judge | Run 3 completes the task in 3778 tokens with good density — minimal padding, each section earns its length. Runs 1 and 2 each hit the 4096-token ceiling and truncate, meaning they spent the full budget but still failed to finish. This is the worst efficiency outcome: maximum token cost with incomplete output. Within the completed portions the writing is substantive (formulas, tables, complexity calculations are justified), but the budget management failed in two of three runs. Some organizational overhead is present across runs (section numbering, repeated subsection headers for each step) but is proportionate to the problem complexity. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Completeness | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Format Compliance ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 2 | 3 | 5 | 3 | 1.25 |

- **Self-preference delta:** -0.5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.57 (max 3).

Tokens (avg output): 3990 | Latency (avg): 89.41s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs produce a genuine structural analog (WFQ) with enumerated element-by-element mappings and a two-stage format that satisfies the structural requirement. The core mapping is correct and competently executed. However, the responses consistently miss the most discriminating requirements: the non-preemptible driver commitment and repositioning cost are absent from or marginal in the analog-stage breakdown flags; graceful degradation (c) is universally misframed as proportional sharing rather than admission-control triage (shedding orders that cannot make the 30-minute cutoff); and none name staleness of central state as a failure mode. These are not incidental omissions — the rubric explicitly identifies them as the discriminators between strong and weak answers. The tone is technically appropriate but tips toward unearned confidence rather than the intellectually honest 'this part transfers, this part does not' register the prompt requests. Run 3's token count (17,845) represents significant bloat without quality gain. Consistency is high because all three runs make the same correct choices and the same critical omissions.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | The runs are on-task and mostly structurally correct, but they overstate or blur the analogy in ways the rubric warns against. Run 1 claims WFQ “directly maps” to order refunds and deadline handling, but then uses a custom urgency heuristic rather than a faithful relation-by-relation mapping. Run 2 improves this by explicitly noting that “Standard WFQ primarily focuses on long-term fairness” and that deadlines need augmentation, but its algorithm still combines priorities in a way that is not a clean structural transfer. Run 3 is the most accurate about mapping breakdowns, yet it introduces CPU scheduling/CFS and a large amount of unrelated machinery. Overall, the outputs are relevant and mostly correct, but not fully faithful to the expected analogical reasoning standard. |
| Completeness | 4 | judge | The responses identify valid analogs and do cover an allocation scheme, state, assignment, reclamation, and some failure modes, but they miss or underdeliver on key required distinctions. The prompt demanded that the analog stage visibly precede and inform the solution, plus explicit element-by-element mapping and explicit breakpoints. Run 1 has the right two-stage shape but only a single analog and a weakly enumerated breakdown. Run 2 includes a clearer mapping-breakdown section, but its solution does not fully satisfy the required graceful degradation as admission/triage; it mostly treats demand with fair sharing plus urgency. Run 3 is broad and detailed, but the analog stage is mostly a giant table and the solution drifts into generic credit scheduling rather than the specific deadline-aware admission/drop mechanism expected. |
| Format Compliance | 4 | judge | All three runs broadly follow the requested prose-shaped, two-stage structure better than not, and the analog stage generally precedes the solution. However, none is a perfect match. Run 1 uses headings and bullet lists, which is acceptable, but it only gives one analog where the prompt asked for 1-2. Run 2 has clearer solution staging but still compresses the analog stage. Run 3 departs most from the requested shape by rendering the structural mapping as a massive table, which is explicitly allowed in spirit only if prose-shaped; here it is not ideal and is excessively unwieldy. Still, the output is not format-ignored, so this is above average but not a 5. |
| Consistency | 4 | judge | Semantic and structural agreement across runs is high: all three independently select WFQ as the primary analog, use the same core mapping relationships (drivers↔bandwidth, warehouses↔flows, orders↔packets), produce a two-stage analog-then-solution structure, address a/b/d requirements, and miss exactly the same critical elements (triage framing for (c), repositioning cost disanalogy, staleness failure mode). The convergence on both the correct choices and the same omissions is evidence of stable behavior. Run 3 adds CFS as a second analog and uses a table instead of bullets for the mapping — structural variations that do not change the semantic content or quality level. [lexical similarity ratio: 0.018] |
| Tone/Style | 4 | judge | The tone is consistently technical, analytical, and aimed at an engineer peer. Run 2 is especially close, explicitly noting partial mappings and limitations. Run 1 is somewhat more glib in places (“holds strongly”) and overconfident about direct transfer, while Run 3 is very verbose and slightly formulaic, but still in-register. None are salesy or casual in a way that violates the requested tone, though they are not perfectly “thinking aloud” with the honesty and precision the rubric expects. |
| Safety | 5 | judge | The outputs are clean, non-harmful, and free from unsafe content. They discuss scheduling, queues, and operational design only. |
| Efficiency | 2 | judge | The responses are heavily bloated relative to the task and the quality delivered. Run 1 is 11,375 tokens, Run 2 is 11,500 tokens, and Run 3 is 17,845 tokens, yet much of the content repeats the same WFQ fairness story with added formatting and long implementation detail that is not required by the prompt. The quality is acceptable, but nowhere near proportional to the token spend. Run 3 is especially inefficient due to the oversized table and extended exposition. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Completeness ⚠ | 4 | 3 | 3 | 5 | 2 | 0.94 |
| Format Compliance ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Consistency ⚠ | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Tone/Style ⚠ | 4 | 4 | 3 | 5 | 2 | 0.82 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency ⚠ | 2 | 1 | 3 | 3 | 2 | 0.94 |

- **Self-preference delta:** +9 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Tone/Style, Efficiency, Consistency.
- **Panel mean spread/dim:** 1.57 (max 2).

Tokens (avg output): 13573 | Latency (avg): 65.61s | Runs: 3

---

## Prompt Under Test

```text
Before solving the problem below, recall 1-2 problems from ANY domain that share its underlying structure. For each analog you recall:
- State the analogous problem briefly.
- Describe its known, established solution.
- Spell out the structural mapping to the current problem element-by-element (what plays the role of what), and explicitly flag any place where the mapping breaks down or only partially holds.

Then use the mapping(s) to construct the solution. Do not transfer any part of an analog's solution that the mapping does not actually justify; if a familiar technique only partially transfers, say which part and why.

Problem: A same-day grocery delivery company runs ~40 neighborhood micro-warehouses in one city, all drawing drivers from a single shared city-wide pool of ~300 drivers per shift. Demand per micro-warehouse is wildly uneven and bursty: a few suburban sites get a steady trickle of ~5 orders/hour, while a handful of dense downtown sites stay quiet for an hour then dump 200 orders in 15 minutes (a flash sale, a rainstorm, a lunch rush). Each order must be picked up within 30 minutes of being placed or it is refunded (the capacity is perishable — an idle driver-minute is gone forever, and a driver already mid-route is unavailable). Design an allocation scheme that (a) guarantees no single bursting warehouse can starve the others of drivers, (b) still lets a warehouse temporarily pull far more than its "fair share" when the rest of the city has spare drivers, (c) degrades gracefully when total demand exceeds the 300-driver supply, and (d) is computable centrally in well under a second per reassignment cycle. State the allocation algorithm, what state it keeps, how a driver gets assigned and reclaimed, and the main failure modes of your scheme.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Two close analogs come to mind.

## Analog 1: Generalized Processor Sharing / Weighted Fair Queuing in packet scheduling

**Brief problem.**  
A router must share one output link among many flows. Some flows burst; others are steady. The router must prevent one flow from monopolizing bandwidth, yet let a flow use extra bandwidth when others are idle.

**Established solution.**  
Use **weighted fair queuing** or an approximation such as **deficit round robin**. Each flow gets a reserved share, but unused capacity is redistributed. A bursty flow can send more when others are inactive, but if all flows are active, no flow can exceed its fair rate for long.

**Structural mapping to current problem.**

- **Packet flows** ↔ **micro-warehouses**
- **Output link capacity** ↔ **shared driver pool**
- **Packets waiting in a queue** ↔ **unpicked orders waiting for drivers**
- **Per-flow rate share / weight** ↔ **warehouse baseline fairness share**
- **Packet service time / link transmission time** ↔ **driver time consumed on a delivery**
- **Burstiness of traffic** ↔ **flash sales / rainstorms / lunch rushes**
- **Scheduling one packet at a time** ↔ **assigning one driver to one order at a time**

**Where the mapping holds well.**  
The key fairness problem is the same: protect each source from starvation while allowing opportunistic use of slack capacity.

**Where it breaks down.**  
Packets are served on one server; here drivers are **mobile resources** with nontrivial trip durations and geographic constraints. Also, “service time” is not just a processing time; a driver becomes unavailable until the delivery finishes, so the allocation is closer to a **constrained, time-varying resource pool** than a simple bandwidth scheduler.

---

## Analog 2: Weighted proportional-share admission in cloud cluster scheduling

**Brief problem.**  
A cluster has a fixed set of machines, and many tenants submit jobs. Some tenants are bursty. The scheduler must ensure fairness, allow unused capacity to be borrowed, and degrade gracefully under overload.

**Established solution.**  
Use a **central quota/entitlement system** with **borrow-from-idle-capacity** semantics. Each tenant has a guaranteed share, often enforced by virtual tokens or credits. Idle resources may be loaned to active tenants, but when demand rises elsewhere, the loans are revoked only at natural boundaries, so the system remains stable and fair.

**Structural mapping to current problem.**

- **Tenant** ↔ **warehouse**
- **Cluster machines** ↔ **drivers**
- **Tenant quota / entitlement** ↔ **warehouse fair-share budget**
- **Borrowing idle machines** ↔ **temporarily pulling extra drivers**
- **Preemption at job boundaries** ↔ **reclaiming drivers when their current delivery ends**
- **Overload behavior** ↔ **unfilled orders / refunds after timeout**

**Where the mapping holds well.**  
The main idea of a central allocator with per-tenant budgets and a shared slack pool transfers nicely.

**Where it breaks down.**  
Jobs can often queue for long periods; here orders expire after 30 minutes, so the system needs **deadline-aware dispatch**, not just fair long-run capacity allocation.

---

# Using the mapping to build a solution

The right transfer from both analogs is:

1. Give each warehouse a **baseline entitlement** so no one can be starved.
2. Keep a **global slack pool** so idle capacity can be borrowed.
3. Allocate with a **deadline-aware priority among waiting orders**, because orders expire.
4. Reclaim drivers **only when they become free**, not by mid-route preemption.

That suggests a central **hierarchical fair-share dispatcher with borrowing**, implemented with per-warehouse tokens and a global active set.

---

# Allocation scheme

## Core idea

Maintain, at all times:

- a **baseline share** for each warehouse, derived from its historical demand or an equal split if you want pure fairness;
- a **global pool** of all currently idle drivers;
- a **per-warehouse queue** of waiting orders, ordered by urgency/age;
- a rule that a warehouse may use:
  - its own baseline allocation first,
  - then borrow from any global idle drivers beyond others’ protected minimums.

If total demand exceeds total driver supply, each warehouse gets at least its protected share, and extra capacity is distributed proportionally to demand pressure and urgency.

---

# Concrete algorithm

## State kept centrally

For each warehouse `w`:

- `base[w]`: guaranteed minimum number of drivers it can count on when system is busy
- `assigned[w]`: drivers currently assigned to `w`
- `waiting[w]`: priority queue of open orders, prioritized by earliest deadline / oldest age
- `need[w]`: a running measure of pressure, e.g. number of unserved orders or a smoothed demand estimate
- `borrowed[w]`: number of drivers above base currently held by `w`

Global:

- `idle_drivers`: set or queue of all drivers currently free city-wide
- `total_drivers = 300`
- possibly a **fairness debt/credit** counter per warehouse to track over- and under-service over time

---

## Assignment rule

When a new order arrives at warehouse `w`:

1. Put the order into `waiting[w]`.
2. If `assigned[w] < target[w]` and an idle driver exists, assign one immediately.
3. Otherwise, if any idle driver exists anywhere, assign it to `w` if doing so does not violate the protected minimums of other active warehouses.
4. If no safe idle driver exists, put the order in queue and wait.

A practical version is simpler and faster:

- Maintain each warehouse’s **protected floor** = `base[w]`.
- Maintain a **surplus pool** = idle drivers minus any drivers needed to keep every active warehouse at its floor.
- Any warehouse may borrow from surplus proportionally to its backlog urgency.

That gives a fast rule:

### Allocation score
For each warehouse `w` with waiting orders, compute:

`score[w] = α * backlog_urgency[w] + β * fairness_deficit[w]`

where:
- `backlog_urgency[w]` can be the age of the oldest waiting order, the number of orders nearing the 30-minute deadline, or both;
- `fairness_deficit[w] = base_share[w] + accrued_credit[w] - assigned[w]`

Then assign each newly freed driver to the waiting warehouse with highest score, subject to not dropping any warehouse below its protected floor.

---

## Driver assignment procedure

When a driver becomes idle:

1. Mark them as globally idle.
2. Recompute which warehouses have pending orders.
3. Choose the warehouse with the highest priority score among those below their demand.
4. If all warehouses are at or above their fair floor, give the driver to the warehouse with the most urgent waiting order.
5. Assign the driver to the next order in that warehouse’s queue.

Because reassignments happen only at driver-finish events, there is no need for mid-route preemption.

---

## Reclamation rule

A driver is reclaimed only when the current delivery is complete:

1. The driver returns to the global idle pool.
2. The allocator immediately re-runs the selection step.
3. If the warehouse that just released the driver still has urgent backlog, it may get the driver back.
4. Otherwise, the driver is diverted to a different warehouse with higher pressure.

This is the analog of “job completion boundary” in cluster scheduling.

---

# How this satisfies the requirements

## (a) Guarantees no single bursting warehouse can starve the others

Use **protected floors**.

Each warehouse has a nonzero baseline share `base[w]`, and the allocator is forbidden to let one warehouse consume resources that would push another active warehouse below its protected floor.

So if downtown A gets a flash sale, it can borrow only from the **surplus above other warehouses’ floors**.

This is the key non-starvation property.

---

## (b) Still lets a warehouse temporarily pull far more than its fair share when others have spare drivers

Any idle drivers above the protected floors go into the **borrowable surplus**. A bursty warehouse with a large backlog can take many of them immediately.

This is exactly the “borrow unused bandwidth” part of fair queueing and cluster borrowing. A warehouse’s short-term allocation can greatly exceed its baseline if the rest of the city is quiet.

---

## (c) Degrades gracefully when total demand exceeds 300-driver supply

When overloaded, the allocator becomes a **weighted fair scheduler under scarcity**:

- each warehouse still gets its floor,
- extra drivers go to the most urgent backlog,
- orders are served in deadline order within each warehouse,
- some orders will still expire if demand exceeds effective capacity, but the loss is spread according to the fairness policy rather than collapsing all service into one hotspot.

This is graceful degradation: no global thrashing, no total starvation, and predictable under-service.

---

## (d) Computable centrally in well under a second per reassignment cycle

Use simple data structures:

- a priority queue per warehouse for order urgency,
- a global priority queue or heap keyed by `score[w]`,
- O(log W) updates, where `W ≈ 40`.

With only 40 warehouses and ~300 drivers, a central recomputation on each driver arrival/finish is trivial. Even a full scan over all warehouses is cheap; 40-way selection is tiny.

So the algorithm can be implemented in:
- **O(log W)** per event with heaps, or
- **O(W)** per event with a straight scan, which is still easily under a second.

---

# A practical version: hierarchical weighted fair dispatch

If you want the most direct implementation, use this:

## 1. Define weights
Each warehouse `w` gets a weight `weight[w]`, based on:
- long-run demand,
- service-level commitments,
- or simply equal weights if fairness is equalized citywide.

## 2. Compute target shares
At any moment, each warehouse has a target:
`target[w] = floor(total_available * weight[w] / sum_weights)`

but only among active warehouses. Unused shares are borrowable.

## 3. Enforce a floor, not a hard cap
- Below `target[w]`, the warehouse has priority.
- Above `target[w]`, it may still get drivers if slack exists and its backlog is urgent.

This is important: if you use hard caps, you violate requirement (b). So the target is a **guarantee plus a priority reference**, not an absolute limit.

## 4. Dispatch policy
Whenever a driver is free:
1. choose the warehouse with the highest combination of:
   - urgency,
   - queue length,
   - deficit from target,
2. assign the driver to that warehouse’s oldest-near-deadline order.

---

# Main failure modes

## 1. Bad baseline weights
If `base[w]` or `weight[w]` is set poorly, the allocator can systematically under-serve fast-growing warehouses or over-reserve for sleepy ones.

**Mitigation:** update weights using smoothed historical demand and keep a small adaptive component.

---

## 2. Fast demand shifts faster than the estimator
A flash sale can happen before the system’s moving averages react.

**Mitigation:** include an instantaneous backlog term and deadline pressure, not just historical demand.

---

## 3. Geography and travel time ignored
A driver assigned to a warehouse may be physically far from the order pickup or delivery zone, so “available” drivers may not actually be useful.

**Mitigation:** refine the pool by driver location or route compatibility; this turns one pool into several compatibility classes. The fairness scheme still applies within each class, but the mapping is only partial because spatial feasibility adds constraints absent from the analogs.

---

## 4. No mid-route preemption
A driver already on a delivery cannot be reclaimed immediately.

**Mitigation:** accept this as a hard constraint. The scheme should allocate only at return-to-idle boundaries. This is not a bug; it is the correct transfer from the analogs, where service is also non-preemptive at the fine-grained level.

---

## 5. Deadline misses during overload
If citywide demand persistently exceeds 300 drivers, some orders will expire no matter how good the scheduler is.

**Mitigation:** the algorithm can only **prioritize fairly**; it cannot create capacity. Use the priority rule to minimize refunds and make the loss predictable.

---

# Summary

A good design is a **central weighted fair-share dispatcher with borrowing**:

- each warehouse gets a protected minimum share;
- idle citywide capacity is pooled and loaned to wherever backlog urgency is highest;
- drivers are assigned only when they become idle, and reclaimed only at delivery completion;
- ordering within each warehouse is deadline-aware;
- the whole system is fast to compute and degrades gracefully under overload.

If you want, I can also turn this into:
1. pseudocode,
2. a simulation-ready algorithm,
3. or a production-style design with event loops and data structures.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
