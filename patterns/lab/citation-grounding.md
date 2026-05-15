## Pattern: citation-grounding

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Require inline source citations for factual claims to reduce hallucination.

---

### Mechanism
Models produce plausible facts even when ungrounded. Requiring inline citations (or an explicit "no source" marker) changes the generation target — unsupported claims become harder to produce. Strongest when paired with retrieval.

---

### Template
"Answer the question below. Every factual claim must be followed by an inline citation in brackets:
- [source: {URL, title, or other identifiable reference}]
- [model knowledge only — no source]

If you cannot cite a source for a claim AND the claim is not basic model knowledge, either omit the claim or mark it as speculative.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
What are the main regulatory requirements for a Canadian company collecting biometric data from customers?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Every factual claim must have an inline citation: [source: ...] or [model knowledge only — no source]. Omit unsupported claims or mark them speculative.

Question: What are the main regulatory requirements for a Canadian company collecting biometric data from customers?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Research questions where the user will rely on the answer for decisions
- Legal, medical, financial, or regulatory contexts where source matters
- Pipelines with retrieval — citations should reference retrieved documents
- Journalism, due diligence, or any context where assertion-without-source is a problem
- Cases where the user will fact-check the output and needs entry points to do so

---

### When NOT to Use
- Conversational chat where citations feel clinical
- Creative writing
- Tasks where the model has no access to sources and citations would be invented (worse than no citations)
- Outputs where the structure would be unreadable with inline citations
- Computational or reasoning tasks where the "claim" is a derived result, not a fact

---

### Failure Modes
- Fabricated citations — model invents plausible-looking URLs or titles that don't exist
- Vague attribution — "[source: a 2021 study]" with no identifiable reference
- Citation salting — every sentence gets a citation, including trivial restatements that don't need one
- Selective citation — model cites the easy claims and skips the hard ones
- Source-claim mismatch — cited source doesn't actually support the claim it's attached to

---

### Examples

Example 1:
Input: "Every factual claim must have an inline citation or be marked as model-only knowledge. Question: How is GDPR enforcement structured across EU member states?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Citations required per claim. Question: What were the main empirical findings of the original Transformer paper (Vaswani et al., 2017)?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- confidence-calibration (cited claims earn HIGH; uncited claims are LOW by default)
- noise-isolation (cite from quarantined external content; explicit source attribution prevents over-trust)
- self-verification (verify each cited source-claim pair)
- assumption-surfacing (surface assumptions when no source exists)

Conflicts with:
- creative-flow (citations break narrative)
- brevity-directive (citations add tokens to every claim)
- direct-answer (citations transform the response into something more structured than a direct answer)

---

### Notes (Optional)
Without retrieval, citation-grounding is partial — the model cannot cite sources it hasn't been given, and may fabricate citations. With retrieval (RAG, search), the pattern's value increases sharply. For high-stakes contexts, instruct the model to use a specific citation format that downstream code can validate (e.g., a numbered reference list). Watch for citation fabrication: even strong models invent plausible-looking but nonexistent URLs. When in doubt, instruct the model to prefer "[model knowledge only — no source]" over an unverifiable citation.

---

### Version History
v0.1 – initial version
