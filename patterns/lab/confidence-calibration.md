## Pattern: confidence-calibration

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Attach explicit uncertainty labels to each significant claim so the user can triage verification.

---

### Mechanism
Models sound equally confident regardless of underlying epistemic state. Per-claim uncertainty labels externalize confidence, flag shaky claims, and the forced labeling tends to make the model more conservative.

---

### Template
"Answer the following. For each significant claim, attach a confidence label after the claim in brackets:
- [HIGH] — would bet on this
- [MEDIUM] — likely but worth verifying
- [LOW] — informed guess
- [UNKNOWN] — no real basis, included for completeness

Do not assign HIGH unless you can briefly justify it (training data, reasoning derivation, or widely-known fact). Claims you would have labeled UNKNOWN should usually be omitted unless explicitly relevant.

Question: {question}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
What's the population of Whitehorse, Yukon, and how has it changed over the past decade?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Answer the following. For each significant claim, attach [HIGH], [MEDIUM], [LOW], or [UNKNOWN] in brackets. Omit UNKNOWN unless relevant.

Question: What's the population of Whitehorse, Yukon, and how has it changed over the past decade?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Research and analysis where users need to triage verification
- Forecasting or estimation tasks where calibration matters
- Medical, legal, or financial advisory contexts (with appropriate disclaimers)
- Cases where the user has limited time to fact-check everything
- Anywhere hallucination risk is non-trivial and confidence varies across claims

---

### When NOT to Use
- Conversational chat where labels feel clinical
- Creative writing or fiction
- Tasks where every claim is verifiable by the user anyway
- Outputs going to systems that can't parse the labels
- Cases where the labels themselves would consume more attention than they save

---

### Failure Modes
- Confidence inflation — model labels everything HIGH because that feels like the strongest answer
- Confidence flattening — everything gets MEDIUM as a safe middle
- Label-content mismatch — claim is hedged in prose but tagged HIGH (or vice versa)
- Selective labeling — only some claims get tags; the unlabeled ones are unclear
- Performative humility — model adds LOW labels to make itself seem cautious without actually being uncertain

---

### Examples

Example 1:
Input: "Confidence labels (HIGH/MEDIUM/LOW/UNKNOWN). Question: What were the leading causes of the 2008 financial crisis?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Attach confidence labels per claim. Question: For a solo founder in BC, which tax-planning steps in the first year of incorporation typically have the highest payoff?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- citation-grounding (citations + confidence labels are mutually reinforcing — cited claims earn HIGH more credibly)
- assumption-surfacing (surface assumptions, then label confidence in each)
- self-verification (verify, then re-label confidence based on verification result)
- devils-advocate (use to identify which claims should be downgraded)

Conflicts with:
- brevity-directive (labels add tokens to every claim)
- creative-flow (labels break narrative rhythm)
- direct-answer (labels add structure to what should be direct prose)

---

### Notes (Optional)
True calibration is hard to achieve from prompting alone — models are imperfect at knowing what they know. The pattern's value is partly in the *labels themselves* (useful triage) and partly in the *behavior it induces* (model becomes more conservative when forced to justify HIGH). For high-stakes contexts, pair with citation-grounding so HIGH labels must be backed by sources. Watch for confidence inflation: if every claim is HIGH, the labels are noise. A 3-tier or 4-tier scheme outperforms continuous percentages, which models calibrate poorly.

---

### Version History
v0.1 – initial version
