## Pattern: analogical-reasoning

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Recall a structurally similar known problem and adapt its solution to the current case.

---

### Mechanism
Models solve familiar problems better than unfamiliar ones; many "new" problems share structure with known ones. Explicit retrieval and structural mapping converts unfamiliar problems into familiar ones before solving.

---

### Template
"Before solving the problem below, recall 1-2 problems with similar structure — they can be from any domain. For each:
- State the analogous problem briefly.
- Describe its known solution.
- Identify the structural mapping to the current problem.

Then use the mapping to solve the current problem.

Problem: {problem}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
A startup needs to fairly distribute equity among 4 founders who joined at different times and contributed differently. Suggest a method.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Before solving, recall 1-2 problems with similar structure from any domain. State each analog, its solution, and the mapping. Then solve.

Problem: A startup needs to fairly distribute equity among 4 founders who joined at different times and contributed differently. Suggest a method.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Problems that feel novel but share structure with well-studied domains
- Cross-disciplinary transfer (apply physics to economics, biology to engineering)
- Algorithm design when the user can't name the relevant technique but the structure fits a known one
- Strategy and design questions with established patterns elsewhere

---

### When NOT to Use
- Problems with no useful analog (truly novel research questions, deeply context-specific decisions)
- Tasks where the model would force a bad analog rather than admit none fits
- Cases where the user has already supplied the relevant framework
- Time-sensitive answers where analogical detour wastes tokens

---

### Failure Modes
- Forced analogies — model invents an analog that doesn't actually map, then bends the new problem to fit
- Surface analogy — picks an analog that shares vocabulary but not structure (analogy by keyword, not by relations)
- Mapping break — recalls a real analog but the structural mapping silently fails partway through
- Over-confidence transfer — assumes the analog's solution transfers fully when only parts do

---

### Examples

Example 1:
Input: "Recall 1-2 analogous problems, map their structure, then solve. Problem: How do you onboard a new senior engineer to a 10-year-old undocumented codebase?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Use analogical reasoning. Problem: Design a queueing system for a hospital emergency room that handles both walk-ins and ambulance arrivals."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- stepback-abstraction (both invoke general structure; stepback names the principle, analogy names a sibling instance)
- few-shot-examples (analogs function like worked examples)
- role-persona (a polymath persona reinforces cross-domain transfer)
- chain-of-thought (chain through the analogical mapping)

Conflicts with:
- direct-answer (analogy is a deliberate detour)
- brevity-directive (recalling and mapping adds length)
- strict-output-format (analogical exploration is prose-shaped)

---

### Notes (Optional)
Inspired by Yasunaga et al.'s "Analogical Prompting" (Google DeepMind, 2023), which showed self-generated exemplars rival hand-crafted few-shot examples on reasoning benchmarks. The discipline of explicit *structural mapping* — not just naming an analog — is what makes the pattern work. Without it, the model often produces a vaguely-related anecdote and proceeds unchanged.

---

### Version History
v0.1 – initial version
