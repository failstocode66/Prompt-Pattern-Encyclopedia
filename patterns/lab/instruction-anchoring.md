## Pattern: instruction-anchoring

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Repeat critical instructions at both the start and end of long contexts to combat lost-in-the-middle.

---

### Mechanism
Attention concentrates at the start and end of long contexts and degrades in the middle. Anchoring instructions at both ends leverages this bias to improve adherence at minimal token cost.

---

### Template
"CRITICAL INSTRUCTIONS:
{the most important instructions, kept short}

{long context, documents, examples, or conversation history}

REMINDER OF CRITICAL INSTRUCTIONS:
{repeat the same instructions verbatim or near-verbatim}

Now respond to: {task}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
[10,000 tokens of customer support tickets]
Summarize the tickets in three bullet points. Output JSON with keys 'top_issue', 'pattern', 'recommendation'. Do not include any ticket IDs.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
CRITICAL INSTRUCTIONS:
- Summarize in exactly 3 bullet points
- Output JSON with keys 'top_issue', 'pattern', 'recommendation'
- Do not include ticket IDs

[10,000 tokens of customer support tickets]

REMINDER:
- 3 bullets, JSON with the three keys, no ticket IDs.

Now respond.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Long prompts (anything over a few thousand tokens) where instructions matter
- Tasks bundling instructions with substantial reference material (RAG, multi-doc analysis, long histories)
- Format-strict outputs where the format spec must survive the long context
- Cases where the model has been observed to drift mid-response
- Production prompts in long-context applications

---

### When NOT to Use
- Short prompts where anchoring is overkill
- Cases where the "middle" doesn't exist (single instruction with no surrounding context)
- Strict token budgets where the repeat is unaffordable
- Conversational replies

---

### Failure Modes
- Verbatim drift — the two copies of the instruction subtly disagree and the model picks one arbitrarily
- Over-anchoring — repeating 20 instructions twice produces 40 lines of meta and the model gets confused about which to prioritize
- Stale anchor — instructions updated only in one location; model follows the other
- False confidence — anchoring helps but doesn't guarantee adherence; users assume it does
- Anchor saturation — anchoring becomes routine, so it doesn't draw attention any more

---

### Examples

Example 1:
Input: "CRITICAL: Output only valid SQL, no commentary. [long schema dump] REMINDER: Output only valid SQL, no commentary. Now write the query for: 'top 10 customers by revenue last quarter.'"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "CRITICAL: Cite the source line number for each claim. [long document] REMINDER: Every claim must end with [line N]. Now summarize the key risks."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- delimiter-fencing (delimiters separate the anchors from the embedded content)
- noise-isolation (anchor outside the untrusted content block)
- context-compression (compress, then anchor the instructions around the compressed form)
- strict-output-format (anchor the format spec at both ends)

Conflicts with:
- brevity-directive (repetition adds tokens by design)
- low-latency-optimization (adds tokens to processing)

---

### Notes (Optional)
The "lost in the middle" phenomenon was characterized by Liu et al. (Stanford, 2023). Anchoring exploits the same attention bias positively. Keep the anchored instructions *short* — long anchors at both ends become their own noise. The two copies should be near-identical; verbatim is safest. If only one of three instructions is critical, anchor only that one — anchoring everything dilutes signal. Most useful for prompts above ~2-4k tokens; below that, attention spreads more evenly and anchoring earns less.

---

### Version History
v0.1 – initial version
