# Cross-Judge: tree-of-thoughts

**Date:** 2026-06-20 12:03 | **Target:** gpt-5.4-mini | **Runs:** 2 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash, claude-opus-4-8

Same composed prompt + same target outputs, scored independently by each judge. Disagreement here is judge variance, not model variance.

---

## Judge agreement (score per dimension, 1–5)

| Dimension | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | claude-opus-4-8 | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 4 | 5 | 5 | 1 | 0.5 |
| Completeness | 4 | 5 | 5 | 4 | 1 | 0.5 |
| Format Compliance | 4 | 5 | 5 | 5 | 1 | 0.43 |
| Tone/Style | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 5 | 4 | 2 | 0.83 |
| Consistency | 4 | 5 | 5 | 5 | 1 | 0.43 |
| **Total** | 29 | 32 | 35 | 33 | | |

`*` = same provider as the target model (openai).

---

## Disagreement summary

- **Mean per-dimension spread:** 0.86 (max 2)
- **Contested dimensions (spread ≥ 2):** Efficiency
- **Self-preference delta:** -4.33 total-score points (same-provider mean 29 vs cross-provider 33.33) — same-provider judges scored the target LOWER.

> Interpretation: low spread + a near-zero self-preference delta means the rubric scores are judge-robust. A consistently positive delta is evidence a judge favors its own provider's outputs — a reason to prefer a cross-provider judge or a multi-judge mean.

---

## Per-judge summaries

**gpt-5.4-mini** (same provider as target): Strong, senior-level distributed-systems answer with solid architecture and failure-mode coverage. Main deductions: the three candidate approaches are not genuinely distinct enough, and the final selection is not as sharply driven by the rubric’s required tradeoff analysis as it should be.

**claude-sonnet-4-6**: Both runs deliver a technically sound, well-structured Tree-of-Thoughts response that genuinely addresses all four problem requirements. The three candidate approaches are meaningfully distinct (distributed-sync token bucket, WFQ/DRR scheduling, local-first token bucket with async control plane), the weaknesses are specific and tied to the stated requirements, and the final selection is driven by those weaknesses rather than being evaluation theater. The main accuracy gap is that two of three approaches are token-bucket variants — the orthogonality the reference expected (e.g., sliding-window counters in a shared store as a third angle) is missing. Format compliance is exact, tone is calibrated for a senior distributed-systems audience, and consistency across runs is very high in both structure and semantic content. The primary weakness is efficiency: at 3000+ tokens per run, there is noticeable padding from restated principles, redundant summary sections, and offers to provide additional content, costing roughly 30–50% extra tokens without proportional quality gain.

**gemini-2.5-flash**: The model provided an exceptionally strong performance across all dimensions. It fully met the problem's requirements with highly accurate, comprehensive, and well-structured responses. The tone was perfectly aligned with the senior distributed-systems engineer audience. Consistency across runs was outstanding, showcasing stable reasoning and solution generation despite wording variations. The output demonstrated a deep understanding of the problem and the 'tree-of-thoughts' pattern.

**claude-opus-4-8**: A strong, well-structured tree-of-thoughts response. Both runs faithfully follow the three-phase format, deliver a senior-engineer-grade final design that addresses all four requirements with an O(1) local hot path plus lease-based borrowing, and remain highly consistent across runs. The main weakness is partial fake diversity: two of the three candidate approaches are token-bucket variants and the distinct shared-store/approximate-counter paradigm is missing, slightly undercutting completeness. The selection is nonetheless genuinely driven by the evaluated weaknesses (eliminating WFQ for latency, preferring distributed leasing over naive shared buckets), avoiding evaluation theater. Verbosity is reasonable but includes some recap padding and closing upsell offers.

---

## Prompt Under Test

```text
Solve this problem in three phases:
1. Generate 3 distinct candidate approaches. Each should attack the problem from a different angle.
2. For each approach, briefly trace its reasoning and identify its main weakness.
3. Select the strongest approach (or combine elements) and produce the final answer.

If the selected approach fails partway, backtrack and try another.

Problem: Design a rate limiter for a multi-tenant API gateway. Tenants have wildly different and bursty traffic profiles (some send 10 req/s steady, others burst to 50k req/s for a few seconds then idle). You must (a) prevent any single tenant from starving the others' throughput, (b) still let a tenant burst into spare capacity when the system is underutilized, and (c) keep per-request overhead in the low microseconds at 100k+ aggregate req/s. Specify the algorithm(s), the data structures, where the limiter state lives in a horizontally-scaled gateway fleet, and the key failure modes.
```

## Target Output (gpt-5.4-mini, run 1)

```text
Below are three candidate designs, each from a different angle, followed by a comparison and a final recommended architecture.

---

## 1) Three candidate approaches

### Approach A — **Hierarchical token buckets with distributed refill**
**Idea:**  
Give every tenant a guaranteed bucket, plus a shared “overflow” bucket for unused capacity. Each request consumes from the tenant bucket first; if empty, it can consume from overflow if available.

**How it works**
- Each tenant has:
  - **Committed rate** `r_i` and burst `b_i`
  - A local token bucket on each gateway node
- There is also a **cluster-wide excess pool** representing unused capacity.
- Refill happens periodically or via distributed accounting.

**Pros**
- Simple mental model.
- Naturally supports burst above baseline when spare capacity exists.
- Strong per-tenant isolation if the committed bucket is strictly enforced.

**Main weakness**
- Hard to make the shared overflow bucket both **accurate and low-latency** across a horizontally scaled fleet.
- Distributed refill/accounting can become expensive or inconsistent at 100k+ req/s.
- Hot tenants may cause synchronization contention.

---

### Approach B — **Weighted fair queuing / deficit round robin at admission**
**Idea:**  
Instead of hard per-tenant buckets, place requests into per-tenant queues and schedule them fairly using weights. Spare capacity is naturally borrowed by active tenants.

**How it works**
- Each tenant has a queue.
- Scheduler runs weighted round robin / DRR:
  - Each tenant gets quanta proportional to its fair share.
  - Unused quanta from idle tenants are redistributed implicitly.
- Requests are admitted when a tenant is scheduled.

**Pros**
- Strong fairness guarantees.
- Idle tenants don’t waste capacity.
- Good for preventing starvation.

**Main weakness**
- Adds queueing and scheduling overhead.
- Bad fit for “per-request overhead in low microseconds” at 100k+ req/s unless heavily optimized.
- Queuing requests at the gateway can increase tail latency and memory pressure.
- Bursty traffic can explode queue sizes.

---

### Approach C — **Local token buckets per gateway + distributed elastic fairness controller**
**Idea:**  
Use a fast local limiter on each node for the hot path, while a slower control plane assigns each tenant a dynamic share of cluster capacity based on recent demand and usage.

**How it works**
- Each gateway node maintains:
  - A **local per-tenant token bucket** for fast admission.
  - A **local borrowed-capacity budget**.
- A distributed controller periodically computes:
  - Guaranteed minimum rate for each tenant.
  - Opportunistic extra capacity based on unused global headroom.
- Nodes receive updated tenant budgets periodically, not per request.
- Requests are admitted locally with a few atomic ops and timestamp math.

**Pros**
- Fast hot path.
- Good scalability across many gateways.
- Can preserve fairness while allowing burst borrowing.
- Better fit for low-microsecond overhead.

**Main weakness**
- Needs careful design to avoid over-allocation when many nodes borrow simultaneously.
- Fairness is approximate between control-plane updates.
- Requires robust handling of stale configuration and node skew.

---

## 2) Reasoning trace and weakness of each

### Approach A reasoning
- A token bucket is ideal for burst tolerance.
- If every tenant has a committed bucket, no tenant can exceed its guaranteed share indefinitely.
- A shared overflow bucket lets active tenants use spare capacity.

**Weakness:**  
The overflow bucket becomes the hard part. In a fleet of gateways, keeping a single shared pool accurate without introducing contention, coordination overhead, or oversubscription is difficult. This is exactly where low-microsecond latency tends to break down.

---

### Approach B reasoning
- Fair queueing solves starvation by construction.
- If a tenant is active, it gets service proportional to weight.
- Idle tenants don’t consume service; others can use the slack.

**Weakness:**  
A gateway rate limiter is usually on the critical path before request execution. Queueing every request, even briefly, is expensive and complicates backpressure. It also makes burst handling awkward, especially for 50k req/s spikes. It’s more of a scheduler than a pure limiter.

---

### Approach C reasoning
- The hot path must be local and tiny: hash lookup, token refill math, atomic decrement.
- The control plane can tolerate slower, approximate decisions.
- A tenant’s guaranteed floor prevents starvation; dynamic extra budget lets tenants burst into unused capacity.
- Because the limiter state is local, the gateway fleet scales horizontally.

**Weakness:**  
The main risk is temporary unfairness due to stale budget distribution and uneven tenant placement across nodes. But this is manageable with conservative borrowing rules and periodic reconciliation.

---

## 3) Selected approach and final design

## Recommended design: **Hybrid hierarchical token buckets with local enforcement and distributed budget allocation**
This is essentially Approach C, strengthened with the useful parts of Approach A.

---

# Final architecture

## Goals mapped to mechanisms

### (a) Prevent any single tenant from starving others
Use **per-tenant guaranteed rate limits** enforced independently on every gateway node.

- Each tenant has a **reserved minimum rate** `min_rate`
- Requests beyond the tenant’s local reservation are either:
  - denied, or
  - allowed only if there is borrowed shared capacity available

This ensures one tenant cannot consume everyone else’s guaranteed share.

---

### (b) Let tenants burst into spare capacity when underutilized
Use a **shared elastic pool** of uncommitted capacity.

- Every tenant has:
  1. **Guaranteed bucket**: always available up to reservation
  2. **Borrow bucket**: allows temporary use of unused cluster-wide capacity
- Under low load, borrow tokens are plentiful.
- Under heavy load, borrowing is throttled so the system preserves fairness.

A tenant can burst well above its floor, but not in a way that permanently steals from others.

---

### (c) Keep per-request overhead in low microseconds at 100k+ req/s
Use a **single-node fast path** only:

- Per request:
  - lookup tenant state in a cache-friendly map
  - compute token refill using monotonic time
  - atomic decrement / compare-and-swap
- No per-request distributed calls
- No per-request queueing
- No per-request cross-node coordination

This is the key performance requirement.

---

# Algorithm details

## 1. Per-tenant local limiter: token bucket
For each tenant `t` on each gateway node:

- `tokens_guaranteed`
- `tokens_borrowed`
- `last_refill_ts`

Refill function:
- `tokens_guaranteed += min_rate_t * elapsed`
- `tokens_borrowed += borrow_rate_t * elapsed` up to a cap
- clamp both to their bursts

Admission rule:
1. If `tokens_guaranteed > 0`, consume from guaranteed bucket
2. Else if `tokens_borrowed > 0`, consume from borrowed bucket
3. Else reject with 429 / retry-after

This gives:
- strict baseline protection
- burstability
- simple O(1) request path

---

## 2. Cluster-wide capacity model
The control plane periodically computes:

- Total gateway capacity estimate `C`
- Sum of reserved tenant minima `Σ min_rate_t`
- Slack capacity `S = C - Σ min_rate_t`
- Per-tenant burst/borrow allowance based on:
  - recent usage
  - configured priority/weight
  - tenant plan limits
  - observed fairness

There are two practical ways to distribute this:

### Option 1: Fixed periodic budget push
Every few hundred milliseconds or second:
- control plane pushes each node a budget for each tenant
- node uses that budget locally until next update

### Option 2: Leasing / replenishment
Each node receives short-lived leases of borrow tokens for tenants it serves.
- leases are renewed periodically
- if a node is isolated, it degrades safely to guaranteed-only mode

For low overhead, I’d prefer **periodic push with local counters**.

---

## 3. Optional fairness enforcement with “soft caps”
To avoid one tenant consuming all spare capacity indefinitely:

- Give each tenant:
  - **Guaranteed floor**
  - **Soft cap** on borrow rate
- Soft cap can be exceeded only if global utilization is low enough

This means:
- When system is idle, tenants can burst aggressively
- When system is busy, spare capacity is shared in proportion to weights or recent demand

A practical policy:
- allocate unused capacity by **weighted fair share**
- redistribute unused share every control interval

---

# State placement in a horizontally scaled gateway fleet

## Hot-path state: **local memory on each gateway node**
Each gateway keeps a local in-memory map:

- key: tenant_id
- value:
  - token counters
  - last refill time
  - current borrow lease
  - small metadata like weight, min_rate, burst cap

This state should be:
- sharded by tenant_id within the node
- stored in a cache-friendly structure
- protected with atomics or striped locks

### Recommended data structures
- **Tenant state table**
  - concurrent hash map or sharded hash map
- **Per-shard arrays**
  - if tenant IDs are dense or can be remapped, a flat array is even better
- **Atomic counters**
  - for token counts and timestamps
- **LRU / TTL eviction**
  - for inactive tenants to control memory

---

## Control-plane state: **centralized or consensus-backed config**
Store in a durable config store:
- tenant plans
- min_rate
- burst limit
- weight / priority
- tenant status / suspension / overrides

This is not on the request path.

The control plane also tracks:
- global utilization
- per-node load
- lease allocations / reconciliation

---

# Request path pseudocode

```text
on_request(tenant_id):
    state = local_table.get_or_create(tenant_id)

    now = monotonic_time()
    elapsed = now - state.last_refill_ts
    state.last_refill_ts = now

    state.guaranteed_tokens = min(
        state.guaranteed_tokens + min_rate[tenant_id] * elapsed,
        guaranteed_burst_cap[tenant_id]
    )

    state.borrowed_tokens = min(
        state.borrowed_tokens + borrow_rate[state] * elapsed,
        borrowed_burst_cap[tenant_id]
    )

    if state.guaranteed_tokens >= 1:
        state.guaranteed_tokens -= 1
        allow()
    else if state.borrowed_tokens >= 1:
        state.borrowed_tokens -= 1
        allow()
    else:
        reject_429()
```

This can be optimized further by:
- replenishing lazily only when a request arrives
- using fixed-point arithmetic
- caching computed refill rates
- avoiding division on the hot path

---

# How to keep it fair across gateways

A local-only limiter can overspend borrowed capacity if every node independently thinks it has slack. So add one of these safeguards:

## Safeguard A: Conservative borrow budgets
Each node gets only a fraction of the estimated global slack:
- `node_borrow_budget = slack / number_of_active_nodes * safety_factor`
- safety factor < 1 to prevent oversubscription

This is simplest and robust.

## Safeguard B: Lease-based borrowing
Nodes must spend from a lease token budget that is periodically renewed.
- if a node runs out, it falls back to guaranteed-only

This is stricter and safer under skew.

## Safeguard C: Global feedback loop
Control plane adjusts borrow budgets based on observed utilization and rejection rates.

Best in practice: **A + C**, optionally **B** for stricter environments.

---

# Key failure modes

## 1) Oversubscription of shared capacity
**Symptom:** many nodes simultaneously borrow too aggressively.  
**Impact:** overload, latency spikes, unfairness.  
**Mitigation:**
- conservative per-node slack allocation
- short lease intervals
- safety margins
- global reconciliation

---

## 2) Hot tenant on one node
**Symptom:** a tenant hashes heavily to one gateway and exhausts local tokens there while other nodes are idle.  
**Impact:** local 429s despite global slack.  
**Mitigation:**
- consistent hashing / better load balancing
- optional cross-node tenant stickiness balancing
- larger local burst caps with conservative global budgeting

---

## 3) Clock skew / time drift
**Symptom:** refill calculations diverge across nodes.  
**Impact:** inconsistent admission.  
**Mitigation:**
- use monotonic clocks only
- avoid wall-clock dependence
- keep refill intervals short
- prefer fixed-point math

---

## 4) Stale control-plane config
**Symptom:** node uses old min rates or borrow budgets.  
**Impact:** unfairness, over-admission, or unnecessary throttling.  
**Mitigation:**
- versioned config
- TTL on budgets
- fail closed to guaranteed-only mode when stale

---

## 5) Tenant churn / memory blowup
**Symptom:** many short-lived tenants or spoofed tenant IDs create state explosion.  
**Impact:** memory pressure, eviction churn.  
**Mitigation:**
- authenticated tenant identity
- TTL eviction
- bounded per-node state
- admission controls for unknown tenants

---

## 6) Retry storms
**Symptom:** rejected clients immediately retry and amplify load.  
**Impact:** worsening congestion.  
**Mitigation:**
- return `429` with `Retry-After`
- optionally add jittered backoff hints
- coordinate with upstream client libraries

---

# Practical implementation notes

## Fast path optimizations
- fixed-point arithmetic instead of floating point
- shard tenant state to reduce lock contention
- batch refill if tenant is very hot
- use approximate prechecks before heavier atomic updates
- keep metadata in a compact struct for cache locality

## Policy knobs
- per-tenant guaranteed rate
- per-tenant burst size
- borrow weight
- soft cap
- global safety factor
- control-plane update interval

---

# Recommended summary

If I had to implement this for a real multi-tenant gateway, I would use:

1. **Local per-tenant token buckets on each gateway node**
2. **Guaranteed floor + borrowed burst capacity**
3. **Periodic distributed allocation of shared slack**
4. **Conservative borrowing with safety margins**
5. **Monotonic-clock, lock-light hot path**
6. **Config/state split: local runtime state, centralized policy state**

This design:
- prevents starvation,
- allows burst into unused capacity,
- scales horizontally,
- and keeps request overhead extremely low.

If you want, I can also provide:
- a concrete pseudocode implementation,
- a diagram of the data flow,
- or a comparison with pure Redis-backed rate limiting and why it won’t meet the microsecond target.
```
