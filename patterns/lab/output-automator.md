## Pattern: output-automator

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Produce an executable artifact (script, checklist, config) alongside prose so the answer can be applied without manual translation.

---

### Mechanism
Prose instructions force the user to translate words into actions every time. An artifact compresses that step into a reusable object — high payoff for repeated procedures or multi-step processes.

---

### Template
"Answer the request below. In addition to (or instead of) prose instructions, produce a {script / checklist / config file / template} that executes the steps. The artifact should be usable without further translation — runnable code, copyable config, or a printable checklist.

If a script is appropriate, specify language and any required dependencies inside the artifact itself.

Request: {request}"

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
How do I set up automated nightly database backups on a Linux server?

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
Answer the request below. Produce a script or config alongside any prose. The artifact should be usable as-is.

Request: How do I set up automated nightly database backups on a Linux server?

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Procedures the user will run repeatedly (automatable workflows)
- Multi-step tasks where manual translation is error-prone
- Configuration tasks (CI/CD, Nginx, systemd, Docker)
- Checklists for processes the user will repeat (onboarding, release, incident response)
- Cases where the user explicitly wants a deliverable, not just instructions

---

### When NOT to Use
- One-time decisions where no artifact would be reused
- Tasks where the "right" automation depends on context the model doesn't have
- Cases where a flawed script would do damage if run blindly (destructive operations)
- Conceptual questions where automation isn't the goal
- When prose explanation is the deliverable (teaching, decision support)

---

### Failure Modes
- Untested code — script runs in the model's head but breaks on real systems (missing flags, wrong paths, env assumptions)
- Brittle scripts — assumes a specific environment without flagging assumptions
- Implicit destructive operations — `rm -rf`, force-pushes, unscoped database modifications hidden inside the artifact
- Checklist generalization — checklist items are too vague to be actionable
- Artifact-only response — prose context is omitted, leaving the user with a script they don't understand

---

### Examples

Example 1:
Input: "Produce an executable artifact alongside the answer. Request: How do I rotate API keys across our 12 services without downtime?"
Output: [placeholder — to be filled after testing]

Example 2:
Input: "Produce a checklist artifact. Request: What do I need to do before launching a new SaaS to public availability?"
Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- recipe-pattern (recipe defines the steps; output-automator codifies them as artifacts)
- structured-output-schema (artifact's structure can be schema-enforced)
- strict-output-format (lock the artifact format)
- assumption-surfacing (surface environment assumptions before producing the script)

Conflicts with:
- creative-flow (artifacts are structured, creative writing is not)
- direct-answer (often complementary, but a one-line direct answer rarely needs an artifact)
- brevity-directive (artifacts add length)

---

### Notes (Optional)
Originates from the Vanderbilt prompt patterns catalog (White et al., 2023) as "Output Automator." The pattern's value scales with reuse — a script run once is no better than prose; a script run weekly compounds savings. Always pair with assumption-surfacing for environment-dependent scripts: hidden assumptions about paths, permissions, or installed tools are the primary failure mode in production use. Consider explicitly asking the model to include a dry-run flag or a confirmation prompt before destructive operations.

---

### Version History
v0.1 – initial version
