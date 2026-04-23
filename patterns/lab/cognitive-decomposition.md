## Pattern: Cognitive-Decomposition
Version: 0.1
Status: Lab
Last Updated: 04-23-2026

---

### Intent
Improve performance on complex or multi-step problems by explicitly forcing stepwise breakdown before solving

---

### Mechanism
Encourages the model to externalize intermediate reasoning rather than attempting a direct answer, reducing errors in complex tasks

---

### Template
"Break this problem into smaller steps. Solve each step sequentially before giving the final answer: {task}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
same task without pattern

Output
model output

Input (WITH pattern)
same task using the pattern

Output
model output

---

### When to Use
List specific scenarios where this pattern is effective

---

### When NOT to Use
List cases where this pattern is unnecessary or harmful

---

### Failure Modes
Describe how or why this pattern can fail
Examples
Provide at least 2 real-use examples.

---

### Example 1: 
Input:
Output:

### Example 2: 
Input:
Output:

---

### Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... 
expected: ...

---

### Composition
Works well with:
pattern-name

Conflicts with:
pattern-name

---

### Notes (Optional)
Additional observations, edge cases, or insights.

Version History
v0.1 – initial version
