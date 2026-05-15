## Pattern: stepback-abstraction

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
State the broader principle first, then derive the specific answer from it.

---

### Mechanism
Models tangle in surface particulars before finding the right principle. Retrieving the general rule first makes the specific answer a derivation, reducing surface-feature pattern-matching errors.

---

### Template
"Before answering the specific question below, first identify the broader concept, principle, or general question that this is an instance of. State that broader concept clearly in 1-3 sentences. Then use it to derive your answer.

Specific question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
If a gas at constant temperature is compressed from 4L to 1L, what happens to its pressure?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Before answering the specific question below, first identify the broader principle that this is an instance of. State it clearly. Then use it to derive your answer.

Specific question: If a gas at constant temperature is compressed from 4L to 1L, what happens to its pressure?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Physics, chemistry, or math problems that apply a known principle or law
- Legal or policy questions that hinge on a doctrine, statute, or precedent
- Decision questions that map cleanly to a well-known framework (e.g., expected value, marginal cost)
- Cases where the model tends to overfit surface features and miss the underlying rule

---

### When NOT to Use
- Tasks with no applicable abstraction (free-form creative writing, casual chat)
- Highly novel problems where no clean higher-level principle exists
- Latency-sensitive completions
- Cases where the abstraction is obvious and would only pad the output

---

### Failure Modes
- Wrong abstraction — the model picks a related but incorrect general principle and confidently derives a wrong specific answer
- Abstraction theater — states a principle but doesn't actually use it; the specific answer is reached independently
- Over-abstraction — retreats so far up the ladder that the stated principle is too vague to constrain the answer
- Vacuous principles — "this is a question about physics" — true but useless

---

### Examples

Example 1:
Input: "Before answering, identify the broader principle and state it. Then use it to derive your answer. Specific question: A California landlord refused to return a tenant's security deposit because the tenant left a small nail hole in the wall. Is this lawful?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "First state the general concept this question is an instance of, then derive the answer. Specific question: Why does a heavier ball not fall faster than a lighter one in a vacuum?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-decomposition (after stepping back, decompose the specific application)
- self-verification (verify the specific answer is consistent with the stated principle)
- role-persona (a domain-expert persona helps name the right abstraction)
- few-shot-examples (demonstrate good stepback granularity)

Conflicts with:
- direct-answer (stepback is a deliberate detour before answering)
- brevity-directive (adds an explicit pre-answer block)
- low-latency-optimization (extra reasoning tokens)

---

### Notes (Optional)
Introduced by Zheng et al. (Google DeepMind, 2023) as "Step-Back Prompting." Empirically improves accuracy on benchmarks like MMLU and TimeQA, particularly where models would otherwise pattern-match on surface features. Quality of the stepback matters more than the act of stepping back — a wrong abstraction can mislead the specific answer in confidently wrong directions. Pair with self-verification when the cost of a wrong derivation is high.

---

### Version History
v0.1 – initial version
