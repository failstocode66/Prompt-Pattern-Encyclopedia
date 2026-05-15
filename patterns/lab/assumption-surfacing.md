## Pattern: assumption-surfacing

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
List interpretive assumptions before answering so wrong premises can be corrected upstream.

---

### Mechanism
Models silently fill ambiguity gaps with plausible defaults; mismatched defaults produce confidently wrong output. Externalizing the assumptions makes the gap-filling auditable and correctable before the answer is built on it.

---

### Template
"Before answering, list the assumptions you are making to interpret this request. Number them. For each, briefly note what your answer would change to if that assumption were false. Then provide your answer.

Request: {request}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
Write me a script to back up my database nightly.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Before answering, list the assumptions you are making to interpret this request. Number them. For each, briefly note what your answer would change to if it were false. Then provide your answer.

Request: Write me a script to back up my database nightly.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Engineering or configuration tasks where the answer depends on environment, stack, or constraints not stated
- High-stakes decisions where a hidden wrong assumption is expensive to discover later
- When the user provides a short prompt but expects tailored output
- Audit, review, or analysis contexts where reasoning transparency matters
- Onboarding scenarios where the model is calibrating to a new user

---

### When NOT to Use
- Fully specified, unambiguous requests
- Casual chat or quick conversational turns
- Tasks where listing assumptions would dwarf the actual answer
- When the user has explicitly asked for brevity or a direct answer
- Repeat requests in a session where assumptions have already been established

---

### Failure Modes
- Assumption inflation — lists obvious or trivial assumptions ("I assume you want this in English") that don't aid correction
- Wrong-default lock-in — surfaces an assumption but still proceeds confidently as if it were verified
- Disconnected list — assumptions are stated but the answer doesn't actually depend on them in the stated way
- Defensive padding — assumption list becomes hedging cover rather than a genuine invitation to correct

---

### Examples

Example 1:
Input: "Before answering, list your assumptions and what would change if each were wrong. Then proceed. Request: Set up a CI/CD pipeline for my project."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Surface your assumptions before answering. Request: How much should I charge for a one-page website?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- cognitive-verifier (assumptions and sub-questions overlap — can run them in sequence)
- flipped-interaction (the assumption list can become the interview agenda)
- role-persona (an analyst or auditor persona reinforces assumption discipline)
- plan-and-solve (assumptions feed directly into the plan as parameters)

Conflicts with:
- direct-answer (explicit pre-answer scaffolding by design)
- brevity-directive (assumption lists add length)
- creative-flow (analytical pre-step kills generative momentum)

---

### Notes (Optional)
Useful as a debugging tool: when an answer is wrong, the surfaced assumptions usually show why. Quality of assumptions matters more than count — 3 load-bearing assumptions beat 10 generic ones. Some users find this pattern friction-heavy for casual requests; use selectively when ambiguity stakes are high. The "what would change if false" clause is what gives the pattern teeth — without it, models often list assumptions without any indication of which ones matter.

---

### Version History
v0.1 – initial version
