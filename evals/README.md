# /evals — Test cases and evaluation logic

This directory turns the encyclopedia's promotion criteria into reproducible,
diffable artifacts. A composed prompt built from one or more patterns is run
against several models, scored on a 7-dimension rubric by an LLM judge (with an
optional human override), and written out as a markdown report plus a JSON
sidecar that lives in the repo next to the patterns it validates.

It exists to move `/evals` from empty to populated, and to give the
[Lab → Core promotion](../README.md#promotion-criteria-lab--core) decision real
evidence instead of intuition.

## Contents

```
evals/
  PromptEval.py        rubric harness (single + batch modes)
  CrossJudge.py        judge-disagreement / self-preference experiment
  requirements.txt     pinned deps
  prompts/             composed-prompt fixtures + the batch manifest
  reports/             generated eval artifacts (.md + .json)
```

## The rubric (each 1–5)

| Dimension | Question |
|---|---|
| Accuracy | Is the output factually correct and relevant? |
| Completeness | Does it address all parts of the request? |
| Format Compliance | Does it follow the specified output format? |
| Consistency | How similar are outputs across repeated runs? |
| Tone/Style | Does it match the requested tone and audience? |
| Safety | Free from harmful, biased, or inappropriate content? |
| Efficiency | Tokens used relative to output quality? |

This is the richer superset of the README's 3-axis score (Clarity / Consistency
/ Reusability) — **Consistency** carries over directly; the other six add the
accuracy, format, tone, safety, and cost evidence a promotion needs.

**Consistency is judged, not diffed.** An early version scored it with raw text
similarity and gave 1/5 to semantically identical paraphrases. The judge now
scores meaning/structure/quality agreement across runs; the mechanical
lexical-similarity ratio is recorded only as evidence. (See
[docs/eval-methodology.md](../docs/eval-methodology.md).)

## Running

Keys are 1Password `op://` references in a `.env` (no plaintext keys on disk),
materialized at runtime:

```sh
# Single eval
op run --env-file=.env -- py evals/PromptEval.py prompts/my-prompt.txt \
  --pattern role-persona+strict-output-format \
  --expected "what a correct answer must contain" \
  --format-spec "what format compliance means here" \
  --tone "intended tone and audience" \
  --runs 3 --out-dir evals/reports

# Batch — one matrix over many prompts (default automated; drop --no-review to score by hand)
op run --env-file=.env -- py evals/PromptEval.py \
  --batch prompts/batch-manifest.json --no-review --out-dir evals/reports
```

Default target trio is one equitable mid-tier model per provider:
`gpt-5.4-mini`, `claude-sonnet-4-6`, `gemini-2.5-flash` (override with `--models`).
Default judge is `claude-opus-4-8` (override with `--judge`; any provider works).

### Hybrid scoring

By default the judge proposes scores and you accept or override each dimension
(`Enter` accepts, `1-5 [note]` overrides, `a` accepts the rest). Both the judge
and human scores are recorded. Pass `--no-review` for fully automated batch runs.

### Batch manifest

```json
{
  "models": ["gpt-5.4-mini", "claude-sonnet-4-6", "gemini-2.5-flash"],
  "runs": 2,
  "judge": "claude-opus-4-8",
  "evals": [
    { "pattern": "role-persona", "prompt_file": "role-persona.txt",
      "expected": "...", "format_spec": "...", "tone": "..." }
  ]
}
```

`prompt_file` paths are resolved relative to the manifest. The batch writes one
report per eval plus an aggregate **matrix** (pattern × model) and a
per-dimension means table.

## CrossJudge — is the score judge-robust?

An LLM-as-judge is only trustworthy if its scores don't swing with the judge's
identity. `CrossJudge.py` runs one prompt against one target, then has several
cross-provider judges score the **same** outputs, reporting per-dimension
disagreement and flagging same-provider self-preference:

```sh
op run --env-file=.env -- py evals/CrossJudge.py prompts/role-persona-strict-output.txt \
  --pattern role-persona+strict-output-format+audience-calibration \
  --target claude-sonnet-4-6 \
  --judges gpt-5.4-mini,claude-opus-4-8,gemini-2.5-flash \
  --out-dir evals/reports
```

Findings and how to read the output: [docs/eval-methodology.md](../docs/eval-methodology.md).

## Seed reports

The `reports/` directory is seeded with a first batch (role-persona composition
+ few-shot-examples) and a cross-judge run, generated 2026-06-12, as worked
examples of the artifact format.
