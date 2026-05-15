## Pattern: skeleton-of-thought

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Generate an outline first, then expand each point — improving structural coverage in long outputs.

---

### Mechanism
Long sequential generation loses coherence and omits points. A skeleton commits to structure up front so the expansion phase fills predictable slots; in agentic settings, points can be expanded in parallel for latency gains.

---

### Template
"Answer the question in two phases.

Phase 1: Generate a skeleton — a numbered list of 3-7 short bullet points (3-10 words each) covering the structure of a complete answer. Do not elaborate yet.

Phase 2: For each skeleton point, in order, write a 2-4 sentence expansion.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Explain the key considerations when choosing between SQL and NoSQL databases.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Answer the question in two phases.
Phase 1: Generate a skeleton — a numbered list of 3-7 short bullet points covering the structure of a complete answer. Do not elaborate yet.
Phase 2: For each skeleton point, write a 2-4 sentence expansion.

Question: Explain the key considerations when choosing between SQL and NoSQL databases.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Long-form explanations where structural coverage matters (essays, documentation, comparison writeups)
- Outputs that will be edited or reorganized downstream (a skeleton is easy to rearrange)
- Agentic or batched settings where skeleton points can be expanded in parallel
- Tasks where the model tends to ramble or front-load and lose later content

---

### When NOT to Use
- Short factual answers
- Creative writing where structure shouldn't be preordained
- Conversational responses
- Tasks where the natural answer is a single continuous argument rather than enumerable points

---

### Failure Modes
- Skeleton-as-answer — skeleton points are too detailed and the expansion is redundant
- Expansion mismatch — expansions drift from the skeleton point they're supposed to elaborate
- Listicle bias — forces enumerable structure onto answers that don't naturally enumerate
- Over-uniform expansion — all points get equal weight even when some deserve more depth
- Phase bleed — model starts expanding inside the skeleton phase, defeating the structural commitment

---

### Examples

Example 1:
Input: "Use skeleton-of-thought (phase 1 skeleton, phase 2 expand). Question: What should a junior engineer focus on in their first year?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Skeleton first, then expand each point in 2-4 sentences. Question: Compare React, Vue, and Svelte for a small SaaS startup."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- structured-output-schema (skeleton becomes the schema, expansion fills it)
- plan-and-solve (skeleton is a structural plan; the two patterns share spirit but skeleton-of-thought emphasizes output structure over execution sequencing)
- strict-output-format (skeleton naturally produces formattable structure)
- few-shot-examples (demonstrate good skeleton granularity)

Conflicts with:
- creative-flow (locks in structure before flow can happen)
- direct-answer (deliberate two-phase output)
- brevity-directive (skeleton + expansion is inherently longer than a single concise answer)

---

### Notes (Optional)
Introduced by Ning et al. (2023) as "Skeleton-of-Thought," with explicit parallelization as a key benefit — points can be expanded by parallel model calls and reassembled. Even without parallelization, the structural commitment improves coverage. Skeleton granularity matters: too coarse (2 points) provides no real structure; too fine (15 points) makes the skeleton itself the answer. 3-7 points is a defensible default for most explanatory tasks.

---

### Version History
v0.1 – initial version
