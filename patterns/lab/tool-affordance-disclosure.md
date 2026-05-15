## Pattern: tool-affordance-disclosure

Version: 0.1
Status: Lab
Last Updated: 2026-05

---

### Intent
Declare available tools, parameters, effects, and usage conditions upfront to improve tool selection.

---

### Mechanism
Without rich descriptions, models infer tool capabilities from names alone, producing miscalls and invented tools. Structured declarations (purpose, parameters, side effects, when to use vs not) anchor selection to real affordances.

---

### Template

```
You have access to the following tools. Use only these — do not invent others. For each call, match the documented parameters and respect the documented usage conditions.

<tools>
- name: {tool_name}
  purpose: {one-line summary}
  parameters: {schema with types}
  side_effects: {what changes in the world when this is called}
  when_to_use: {trigger conditions}
  when_NOT_to_use: {anti-patterns and alternatives}

- name: {next tool}
  ...
</tools>

Task: {task}
```

---

### Baseline Comparison (Required)

#### Input (WITHOUT pattern)
You have tools: search, fetch, summarize. Task: Find the current CEO of Anthropic and summarize their last public statement.

#### Output
[placeholder — to be filled after testing]

---

#### Input (WITH pattern)
```
<tools>
- name: search
  purpose: Web search across the public internet.
  parameters: {query: string (1-6 words), max_results: int (default 5)}
  side_effects: None.
  when_to_use: Looking up current information or finding URLs to fetch.
  when_NOT_to_use: Already have the URL — use fetch instead.

- name: fetch
  purpose: Retrieve full text content of a specific URL.
  parameters: {url: string}
  side_effects: None.
  when_to_use: Need full page content; have a URL from search or supplied by user.
  when_NOT_to_use: Don't yet have a URL — search first.

- name: summarize
  purpose: Condense long text into a brief summary.
  parameters: {text: string, max_words: int (default 100)}
  side_effects: None.
  when_to_use: Have long text and need a short summary.
  when_NOT_to_use: Text is already short.
</tools>

Task: Find the current CEO of Anthropic and summarize their last public statement.
```

#### Output
[placeholder — to be filled after testing]

---

### When to Use
- Agentic systems with multiple tools
- Tool sets with overlapping or near-overlapping purposes (search vs fetch, edit vs replace)
- Tools with significant side effects that must be triggered deliberately
- Production agent prompts where misuse is expensive
- Onboarding a new model or agent harness to an existing tool inventory

---

### When NOT to Use
- Single-tool contexts where the affordance is obvious
- Cases where tool calling is handled by the API's native function-calling schema (the schema may already encode affordances)
- Quick experiments where setup overhead isn't justified
- When the tool descriptions would balloon the prompt past useful budgets

---

### Failure Modes
- Invented tools — model calls a tool that doesn't exist because the task suggested it (mitigated, not eliminated, by the disclosure)
- Parameter hallucination — model calls a real tool with invented or wrong-typed parameters
- Tool over-selection — model picks a heavier-weight tool than needed because both fit "when_to_use"
- Side effect ignorance — model triggers destructive tools without acknowledging the consequence
- Disclosure bloat — 20 tools with rich descriptions overwhelm the prompt
- Stale disclosure — declaration drifts from actual tool behavior and the model trusts the declaration

---

### Examples

Example 1:

Input:
```
<tools>
- name: create_file, side_effects: writes to disk
- name: edit_file, side_effects: modifies existing file
- name: delete_file, side_effects: permanently removes — irreversible
</tools>
Task: Fix the typo in /home/user/notes.md.
```

Output: [placeholder — to be filled after testing]

Example 2:

Input:
```
<tools>
- name: send_email, side_effects: externally visible
- name: draft_email, side_effects: none, saves to drafts
</tools>
Task: Reply to the customer's question about pricing.
```

Output: [placeholder — to be filled after testing]

---

### Evaluation (Optional in Lab, Required for Core)

Test Cases:
- input: ...
  expected: ...

---

### Composition

Works well with:
- react-reasoning-acting (declare tools first, then ReAct uses them)
- structured-output-schema (tool call format can be schema-enforced)
- delimiter-fencing (the <tools> block is itself an instance of fencing)
- noise-isolation (when tool outputs are untrusted, isolate them on return)

Conflicts with:
- brevity-directive (rich disclosures add tokens)
- low-latency-optimization (more tokens upfront, though the payoff is fewer wasted tool calls)

---

### Notes (Optional)
Native function-calling APIs (OpenAI, Anthropic, etc.) already supply a structured tool schema — this pattern duplicates and enriches it in prompt form when (a) you need richer descriptions than the API schema supports, (b) you want the tool guidance visible to the model in the prompt itself, or (c) you're working with a framework that doesn't expose native function calling. The "when_NOT_to_use" field is the highest-leverage section: it prevents over-selection of generic tools when more specific ones fit. Keep declarations close to real behavior — drift between disclosure and actual tool behavior is a silent failure mode.

---

### Version History
v0.1 – initial version
