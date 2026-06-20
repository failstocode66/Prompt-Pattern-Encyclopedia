# Evaluation Methodology

How patterns in this encyclopedia are scored, and why the scoring can be
trusted. The tooling lives in [/evals](../evals/README.md); this document covers
the *methodology* — the design decisions that make a 1–5 rubric score mean
something.

---

## 1. Why an LLM judge, and where it fails

Scoring a prompt pattern's output by hand doesn't scale across patterns ×
models × runs, and a single human's scores aren't reproducible. An LLM judge is
reproducible and fast — but it introduces two failure modes that the
methodology has to defend against:

1. **Self-preference bias** — a judge may score outputs from its own model
   family higher than a neutral observer would.
2. **Metric-instrument mismatch** — using the wrong instrument for a dimension
   (e.g. measuring "consistency" with text-diff) produces confident, wrong
   numbers.

The two design decisions below address these directly.

---

## 2. Consistency is judged semantically, not measured lexically

**The trap.** The first implementation scored Consistency mechanically: the mean
pairwise [`difflib.SequenceMatcher`](https://docs.python.org/3/library/difflib.html)
ratio across repeated runs, mapped onto 1–5. It produced **1/5 for outputs that
were semantically identical** — three models each gave the same correct answer
in different words, and the character-level ratios were 0.06–0.32. The metric
was punishing paraphrase, which is normal, healthy LLM variance, not
inconsistency.

**The fix.** The judge scores Consistency on *meaning, structure, and quality
agreement* across runs. The lexical-similarity ratio is still computed and
passed to the judge — but as **evidence**, not as the score. The judge is told
explicitly that low lexical similarity from paraphrase is not inconsistency.

**Evidence it works.** After the fix, on the role-persona composition the judge
gave Claude Sonnet a **4/5** with a precise reason — run 1's third point
described the API carrying the answer back, while run 2 introduced a different
concept (code reuse) — while giving paraphrase-only variance a 5/5. The
mechanical ratio for both was near-identical and uninformative. The general
principle: **reserve mechanical metrics for what they actually measure, and
route judgment calls to a judge.**

---

## 3. Cross-judging: is the score judge-robust?

A rubric score is only meaningful if it doesn't change when you change the
judge. [`CrossJudge.py`](../evals/CrossJudge.py) tests this: it runs one prompt
against one **target** model, then has several judges — deliberately spanning
providers — score the **same** target outputs. Any disagreement is judge
variance, not model variance.

When a judge shares the target's provider (e.g. an Anthropic judge scoring a
Claude target), it's flagged, and the tool reports a **self-preference delta**:
the same-provider judges' mean total score minus the cross-provider judges' mean.
A consistently positive delta is evidence of self-preference.

### Findings (2026-06-12)

Target `claude-sonnet-4-6`, judged by `gpt-5.4-mini`, `claude-opus-4-8`
(same provider), and `gemini-2.5-flash`, on the role-persona composition, two
runs each:

| Signal | Result |
|---|---|
| Mean per-dimension spread | 0.14–0.29 (out of a 4-point range) |
| Contested dimensions (spread ≥ 2) | none |
| Where judges disagreed | Efficiency and Completeness only, by 1 point |
| Self-preference delta | **+0.5 to +1.0** total points — the Claude judge gave the Claude target a perfect 35/35; the cross-provider mean was 34–34.5 |

**Reading it.** Judges agree strongly — the rubric is robust, not a coin flip.
But the self-preference delta was *small and consistently positive*: the
same-provider judge never scored the target lower than the cross-provider
judges, and gave it top marks both times. The gap is within normal noise for a
single comparison, but its *direction* is the point — it's exactly the signal
self-preference would produce.

### What this implies for scoring patterns

- **Don't judge a model's output with its own family** when you can avoid it.
  For pattern evals where the target is a Claude model, prefer a non-Claude
  judge, or —
- **Use a cross-provider judge panel** (now built in — see §3a). Averaging across
  providers cancels per-provider bias and surfaces the genuinely contested
  dimensions (here, Efficiency).
- **The single default judge** (`claude-opus-4-8`) is fine for cross-model
  batches where no single provider is the subject; **switch to a panel when
  scoring a single provider's pattern output in isolation.**

---

## 3a. Panel mode — the multi-judge mean, built into PromptEval (2026-06-19)

The multi-judge mean is no longer a separate experiment. `PromptEval.py` takes
`--judges j1,j2,j3` (a cross-provider panel) alongside the single `--judge`.
Every dimension is scored by each judge; the aggregate — **mean by default**, or
`--aggregate median` for outlier-robustness — becomes the score, and each report
carries a per-judge breakdown with the spread, stdev, and a ⚠ self-preference
flag on any dimension where a same-provider judge scored above the cross-provider
judges. The shared aggregator lives in [`panel.py`](../evals/panel.py) (imported
by both PromptEval and CrossJudge); a single `--judge` is the degenerate N=1 case
and is scored and rendered exactly as before.

**Recommended default for single-provider grading.** When the target is one
provider's model — the Phase-B campaign case, where a Claude target in the trio
is graded in isolation — grade with a cross-provider panel rather than one
same-family judge, so the score is bias-resistant and defensible as Lab→Core
promotion evidence:

```sh
op run --env-file=.env -- py evals/PromptEval.py prompt.txt \
  --pattern role-persona --models claude-sonnet-4-6 \
  --judges gpt-5.4-mini,claude-opus-4-8,gemini-2.5-flash --runs 2 --no-review
```

**Live confirmation (2026-06-19).** On a role-persona+brevity composition
(`claude-sonnet-4-6` target, the three-judge panel above), the judges agreed on
6 of 7 dimensions (5/5) and split only on **Efficiency** — `gpt-5.4-mini` gave 4,
the other two gave 5 (spread 1). The same-provider `claude-opus-4-8` judge sat on
the higher side, so the report flagged Efficiency ⚠ with a self-preference delta
of **+0.5** total points: a small, correctly-surfaced instance of the exact bias
the panel exists to catch — on an otherwise unanimous result.

---

## 4. Equitable-tier comparison

Cross-model numbers only mean something if the models are the same tier. The
default target trio is one mid-tier workhorse per provider —
`gpt-5.4-mini`, `claude-sonnet-4-6`, `gemini-2.5-flash` — not a flagship against
a mini. (An early run that pitted a flagship against a mid-tier model produced a
meaningless "comparison.") Pick model availability against the live model list
per key rather than assuming a name exists.

### A token-counting caveat the rubric exposes

The **Efficiency** dimension reads each provider's reported output-token count,
and those counts are not directly comparable: reasoning/thinking models spend
hidden tokens. In testing, `gemini-2.5-flash` reported ~750–1,400 output tokens
for a ~100-word answer (thought tokens included), while `gpt-5.4-mini` and
`claude-sonnet-4-6` reported ~100–180 for equivalent visible text. The judge is
shown the raw counts and weighs them against visible quality — which is why
Gemini's Efficiency lands at 3/5 on short-answer patterns despite tidy output.
The reports state explicitly that counts include hidden reasoning/thought
tokens so the number is read correctly.

---

## 5. Summary of safeguards

| Risk | Safeguard |
|---|---|
| Judge favors its own family | Built-in `--judges` cross-provider panel (mean/median aggregate, per-dimension ⚠ self-preference flag); CrossJudge for a standalone disagreement probe |
| Wrong instrument for a dimension | Consistency judged semantically; lexical ratio is evidence only |
| Unfair model comparison | Equitable mid-tier default trio |
| Hidden-token miscount | Token counts summed and labeled; judge weighs against visible quality |
| Single-judge opacity | Every score carries a written justification + quoted evidence; hybrid human override available |

Generated reports live in [/evals/reports](../evals/reports/).
