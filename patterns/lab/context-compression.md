## Pattern: context-compression

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Replace earlier raw content with a structured summary to recover context budget in long sessions.

---

### Mechanism
Long contexts cost more and dilute attention. A structured summary (facts, questions, decisions, active task) preserves what the model needs to continue at a fraction of the budget, acting as session maintenance or sub-task handoff.

---

### Template
"Before continuing, produce a structured summary of the conversation (or document) so far using this format:

- Established facts: {bullets}
- Open questions: {bullets}
- Decisions made: {bullets}
- Active task: {one line}
- Style/tone preferences observed: {one line if any}

Then continue from this summary as if it replaced the prior context, and respond to: {next task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
[After 30 turns of architectural discussion] "Okay, now help me draft the migration plan."

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Before drafting, produce a structured summary of our discussion so far (facts established, open questions, decisions made, active task, style preferences). Then continue from that summary and draft the migration plan.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Long-running conversations approaching the context limit
- Handoffs between sub-tasks within one session
- Multi-document analysis where the raw documents won't all fit
- Agentic workflows that need to compress prior tool outputs
- Switching topics mid-session — compression captures what's still relevant from the prior topic

---

### When NOT to Use
- Short conversations with plenty of budget remaining
- Tasks where exact prior wording matters (legal review, citation, line-by-line code review)
- Cases where the compression itself would cost more than it saves
- When the user has already supplied a tight context — compression is redundant

---

### Failure Modes
- Lossy summary — model drops a detail that becomes relevant later
- Confidence inflation — model summarizes "we discussed X" without noting that no decision was reached
- Tone loss — facts preserved, but the style/voice established earlier vanishes
- Decision rewriting — summary subtly changes what was actually decided
- Compression of compression — repeated compression cycles degrade fidelity rapidly

---

### Examples

Example 1:
Input: "Compress our discussion into the structured summary format. Then proceed to: draft the executive memo summarizing our decisions."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Summarize the last 5 long search results into established facts, open questions, and which sources contradict each other. Then answer: which source should I trust most?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- instruction-anchoring (after compression, re-anchor critical instructions)
- noise-isolation (compress untrusted content into trusted summary form)
- skeleton-of-thought (compression naturally produces a skeleton of what's known)
- structured-output-schema (lock the summary format)

Conflicts with:
- creative-flow (mechanical summary breaks generative momentum)
- (otherwise composes broadly — context-compression is largely a maintenance pattern)

---

### Notes (Optional)
In agentic loops or long sessions, run compression *before* the context becomes critical, not after — once attention degrades, compression itself becomes unreliable. The structured format (facts / questions / decisions / active task) is load-bearing: free-form summaries lose more information per token. After compression, treat the summary as if it replaces — not supplements — the original context, otherwise both occupy budget. Watch for fidelity drift across multiple compression cycles.

---

### Version History
v0.1 – initial version
