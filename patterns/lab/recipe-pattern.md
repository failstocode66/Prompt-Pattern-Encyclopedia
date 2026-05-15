## Pattern: recipe-pattern

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Produce a complete, ordered procedure including prerequisites and follow-up steps the user didn't ask about.

---

### Mechanism
Users asking "how do I X" often miss prerequisites and follow-ups. Explicit instruction to surface the complete numbered sequence — not just the named middle — produces a portable artifact the user can follow without re-prompting.

---

### Template
"I want to achieve: {goal}.

Provide a complete, ordered recipe of steps to reach this goal:
- Include any prerequisite steps and follow-up steps I may not have thought to ask about.
- Number each step.
- For each step, note required inputs, tools, or commands.
- Flag any step where a wrong choice would be expensive to reverse.

Make it portable — I should be able to follow it without further questions."

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
How do I publish my first Python package to PyPI?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
I want to achieve: publishing my first Python package to PyPI.

Provide a complete recipe including prerequisites and follow-up. Number each step. Note required inputs/tools. Flag any irreversible steps. Make it portable.

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Procedural tasks the user will execute end-to-end
- "How do I do X" requests where missing prerequisites are common
- Tasks the user will perform once but wants documented for future reference
- Onboarding-style content (first deployment, first release, first incident response)
- Documentation drafts where the model produces a starting recipe to refine

---

### When NOT to Use
- Conceptual or explanatory questions ("why does X work?")
- Decision questions where the answer is "it depends" rather than a sequence
- Creative tasks
- Tasks with too much context-dependence to produce a portable recipe
- Cases where one of the steps is genuinely unsafe to follow without supervision

---

### Failure Modes
- Step skipping — model assumes a common prerequisite ("after you have X installed...") without listing it
- Step bloat — every micro-action becomes a numbered step, drowning real decisions in trivia
- Missing reversibility flags — destructive steps appear with no warning
- False completeness — model produces the recipe with confident finality despite gaps
- Environment assumption — recipe works only on the model's default-assumed environment, not the user's

---

### Examples

Example 1:
Input: "Goal: deploy a Next.js app to production with a custom domain and HTTPS. Provide a complete recipe (prereqs, steps, follow-up, irreversible flags)."
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Goal: incorporate a single-shareholder company in British Columbia. Recipe with prereqs and follow-up steps, irreversible steps flagged."
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- output-automator (recipe defines steps; output-automator can codify them as a script)
- plan-and-solve (plan-and-solve produces internal reasoning structure; recipe-pattern produces external deliverable)
- cognitive-decomposition (decomposition is the analytical move; recipe-pattern is the output form)
- assumption-surfacing (surface environment assumptions before producing the recipe)

Conflicts with:
- creative-flow (recipes are structured, divergent thinking is not)
- direct-answer (a direct answer is rarely a recipe)
- brevity-directive (complete recipes are long by nature)

---

### Notes (Optional)
From the Vanderbilt prompt patterns catalog (White et al., 2023) as "Recipe Pattern." The discipline of "complete — including steps you weren't asked about" is what distinguishes recipe-pattern from a regular ordered list. Always pair with assumption-surfacing for environment-dependent recipes; without it, the model produces a recipe that works on its imagined system, not the user's. For destructive or irreversible steps, the explicit "flag irreversible" instruction is load-bearing — without it, model-produced recipes routinely bury `rm -rf` style operations in a numbered list.

---

### Version History
v0.1 – initial version
