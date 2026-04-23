## Pattern: empathic-response
Version: 0.1
Status: Lab
Last Updated: 2026-04-23

---

### Intent
Produce a warm, attuned reply that prioritizes emotional register over information delivery.

---

### Mechanism
Frames the response as witnessing first, problem-solving second (or not at all). The explicit instruction to acknowledge feelings before acting overrides the default assistant tendency to jump to solutions.

---

### Template
"Respond with warmth and attunement. Acknowledge what the person is feeling before offering anything else. Don't jump to solutions unless they ask.

{message}"

---

### Baseline Comparison (Required)
Input (WITHOUT pattern)
My dog died yesterday. I don't know what to do with his bed and his toys.

Output
[placeholder — to be filled after testing]

Input (WITH pattern)
Respond with warmth and attunement. Acknowledge what the person is feeling before offering anything else. Don't jump to solutions unless they ask.

My dog died yesterday. I don't know what to do with his bed and his toys.

Output
[placeholder — to be filled after testing]

---

### When to Use
- Messages involving grief, anxiety, frustration, shame, vulnerability.
- Pastoral or supportive contexts.
- Customer-facing replies where the person is upset and information won't land until they feel heard.
- Peer-review style feedback where tone affects whether the content is absorbed.

---

### When NOT to Use
- Technical questions where warmth reads as patronizing.
- Automated alerts, transactional confirmations, API responses.
- Situations where the person explicitly wants a direct answer.
- Safety-critical messages where information must lead.

---

### Failure Modes
- Performative empathy — the response sounds like a script ("I hear you. That sounds hard.") without substance.
- Validation in place of help — the person wanted a next step; the reply only witnessed.
- Reflective-listening loops that amplify distress instead of supporting.
- Patronizing register — warmth calibrated for grief applied to mild annoyance.
- Avoidance enablement — reply validates feelings about a decision the person needs to act on.

---

### Examples
Example 1: Input: (with pattern) "I just found out I didn't get the promotion. I've been working toward this for two years."

Output: [placeholder — to be filled after testing]

Example 2: Input: (with pattern) "A customer has written: 'This is the third time I've had to call. I'm done. Cancel everything.'"

Output: [placeholder — to be filled after testing]

Evaluation (Optional in Lab, Required for Core)
Test Cases:

input: ... expected: ...

---

### Composition
Works well with:
- role-persona ("You are a calm, experienced counselor")
- brevity-directive (short empathic replies often land better than long ones)

Conflicts with:
- cognitive-decomposition
- structured-output-schema
- direct-answer
- strict-output-format
- self-verification (stepwise review clinicalizes the output)

### Notes (Optional)
The line between empathy and performance is thin. Concrete language ("losing him is a real loss") beats abstract affirmation ("your feelings are valid"). When the person is asking for help with a concrete decision, empathy should precede the help, not replace it. For professional contexts (customer support, clinical), pair with a role that carries domain competence — empathy without competence reads as dismissal.

Version History
v0.1 – initial version
