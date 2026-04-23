## Pattern: self-verification
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Catch errors by asking the model to audit its own output in a second pass before committing to a final answer.

---

### Mechanism
Evaluation is often easier than generation. A fresh pass — especially one explicitly framed as adversarial review — can surface propagated errors, arithmetic slips, and constraint violations that the generation pass missed.

---

### Template
"{original task}

Now review each step of your answer above. Identify any errors, inconsistencies, or missed constraints. If you find any, correct them and state the revised final answer."

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
A store sells notebooks at $3.50 each. A customer buys 7 notebooks and pays with a $50 bill. The cashier also adds 8% sales tax. How much change does the customer receive?

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
A store sells notebooks at $3.50 each. A customer buys 7 notebooks and pays with a $50 bill. The cashier also adds 8% sales tax. How much change does the customer receive?

Now review each step of your answer above. Identify any errors, inconsistencies, or missed constraints. If you find any, correct them and state the revised final answer.

Output
[placeholder — to be filled after testing]

---

### When to Use
- After cognitive-decomposition or plan-and-solve, to catch propagated errors.
- High-stakes reasoning where one error invalidates the output.
- Constraint-heavy problems (scheduling, eligibility rules, legal logic).
- Code generation — review pass often catches off-by-one and edge-case misses.

---

### When NOT to Use
- Single-step tasks where there is nothing to verify.
- When an external verifier (test suite, calculator, schema validator) is available and more reliable.
- Latency- or cost-critical paths.
- Tasks where verification would double the output size for a marginal gain.

---

### Failure Modes
- Rubber-stamp review — model re-reads its work and confirms it without real scrutiny.
- Confirmation bias toward the original answer, especially when the error is subtle.
- Verification introduces new errors by reinterpreting a correctly-solved step.
- Infinite loop risk if "verify again" is chained naively.

---

### Examples
Example 1: Input: A multi-step budget allocation problem followed by: "Now review each step for arithmetic or constraint errors and state the revised final answer."

Output: [placeholder — to be filled after testing]

Example 2: Input: Generated code for a function, followed by: "Now review the function for bugs, edge cases, and spec violations. Output a corrected version if needed."

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- cognitive-decomposition
- plan-and-solve
- structured-output-schema
- self-consistency (use verification as the per-chain filter before voting)
- role-persona ("You are a skeptical auditor")

Conflicts with:
- low-latency-optimization
- brevity-directive
- direct-answer

### Notes (Optional)
The quality of verification tracks the adversarial framing. "Check your work" yields rubber-stamping; "Find the error" yields actual errors being found (sometimes invented). Calibrate the framing to the task's actual error rate. For code, an external test suite beats self-verification every time.

Version History
v0.1 – initial version
