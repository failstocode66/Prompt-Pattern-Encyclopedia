# Exercise 183 + Prompt Pattern Encyclopedia tooling.
#
# PromptEval: a rubric-based evaluation harness for composed prompts from the
# Prompt-Pattern-Encyclopedia. Runs a composed prompt N times against one or
# more models, scores it on a 7-dimension rubric (LLM judge + optional human
# override), and writes a drag-ready markdown eval report plus a JSON sidecar
# for the repo's evals/ directory.
#
# Rubric (each 1-5): Accuracy, Completeness, Format Compliance, Consistency,
# Tone/Style, Safety, Efficiency. All dimensions are scored by the judge model
# and reviewable by you; Consistency (needs >= 2 runs) is judged semantically
# with a mechanical lexical-similarity ratio recorded as supporting evidence,
# and Efficiency is judged with token counts in evidence.
#
# The judge is provider-agnostic: --judge may name an Anthropic, OpenAI, or
# Gemini model (CrossJudge.py uses this to compare judges across providers).
#
# Keys come from .env as 1Password op:// references, so run:
#   op run --env-file=.env -- py PromptEval.py prompt.txt --pattern role-persona
#
# Two modes:
#   Single: py PromptEval.py <prompt-file> --pattern NAME [--expected ...] ...
#   Batch:  py PromptEval.py --batch manifest.json   (one matrix over many prompts)
#
# Typical single-mode flags:
#   --models gpt-5.4-mini,claude-sonnet-4-6,gemini-2.5-flash   (default trio)
#   --runs 3            repeated runs per model (consistency needs >= 2)
#   --expected "..."    what a correct answer should contain (grounds Accuracy)
#   --format-spec "..." what format compliance means for this prompt
#   --tone "..."        intended tone / audience
#   --judge MODEL       any Anthropic/OpenAI/Gemini model (default claude-opus-4-8)
#   --no-review         skip the interactive override step (judge scores stand)
#   --out-dir evals     where the .md/.json artifacts land

import argparse
import difflib
import json
import os
import re
import statistics
import sys
import textwrap
import time
from datetime import datetime
from pathlib import Path

import anthropic
from openai import OpenAI
from google import genai
from google.genai import types
from dotenv import load_dotenv, find_dotenv

import panel  # [A1] shared multi-judge panel aggregator (no API; pure)

_ = load_dotenv(find_dotenv())  # read local .env file

TOOL_VERSION = "1.1"
DEFAULT_MODELS = ["gpt-5.4-mini", "claude-sonnet-4-6", "gemini-2.5-flash"]
DEFAULT_JUDGE = "claude-opus-4-8"
MAX_TOKENS = 4096          # per target-model run (GPT-5 family reasons invisibly)
JUDGE_MAX_TOKENS = 16000   # judges may spend hidden reasoning tokens too
RETRIES = 3                # transient-error retries per API call

# --- the rubric -------------------------------------------------------------
# Anchors keep judge and human calibrated to the same scale.

RUBRIC = {
    "accuracy": {
        "name": "Accuracy",
        "question": "Is the output factually correct and relevant?",
        "anchors": "5=fully correct and on-task; 3=minor errors or mild drift; 1=substantially wrong or off-task",
    },
    "completeness": {
        "name": "Completeness",
        "question": "Does it address all parts of the request?",
        "anchors": "5=every requirement covered; 3=one requirement missed or shallow; 1=most requirements ignored",
    },
    "format_compliance": {
        "name": "Format Compliance",
        "question": "Does it follow the specified output format?",
        "anchors": "5=exact format match; 3=right shape with deviations; 1=format ignored",
    },
    "consistency": {
        "name": "Consistency",
        "question": "How similar are outputs across repeated runs?",
        "anchors": "5=same content, structure, and quality every run (wording may vary); 3=same core answer but runs differ in coverage, format, or quality; 1=runs contradict each other or diverge structurally",
    },
    "tone_style": {
        "name": "Tone/Style",
        "question": "Does it match the requested tone and audience?",
        "anchors": "5=pitch-perfect for the stated audience; 3=generic but inoffensive; 1=clearly wrong register",
    },
    "safety": {
        "name": "Safety",
        "question": "Is the output free from harmful, biased, or inappropriate content?",
        "anchors": "5=clean; 3=questionable phrasing or unexamined bias; 1=harmful or inappropriate",
    },
    "efficiency": {
        "name": "Efficiency",
        "question": "How many tokens were used relative to the output quality?",
        "anchors": "5=tight, no waste for the quality delivered; 3=noticeable padding; 1=heavy bloat or truncated by budget",
    },
}
JUDGED_DIMS = ["accuracy", "completeness", "format_compliance", "tone_style", "safety", "efficiency"]
DIM_ORDER = ["accuracy", "completeness", "format_compliance", "consistency",
             "tone_style", "safety", "efficiency"]


# --- provider plumbing ------------------------------------------------------
# Self-contained (not imported from CompareModels) so this file stays portable
# into the Prompt-Pattern-Encyclopedia repo as a single drop-in tool.

def _require_key(env_var):
    key = os.getenv(env_var)
    if not key or key.startswith("op://"):
        raise RuntimeError(
            f"{env_var} is missing or still an op:// reference -- "
            "run via:  op run --env-file=.env -- py PromptEval.py ..."
        )
    return key


def _provider(model):
    name = model.lower()
    if name.startswith("claude"):
        return "anthropic"
    if name.startswith("gemini"):
        return "gemini"
    if name.startswith(("gpt", "o1", "o3", "o4", "chatgpt")):
        return "openai"
    raise ValueError(f"Don't know which provider serves model '{model}'")


def _with_retry(fn, *args):
    for attempt in range(1, RETRIES + 1):
        try:
            return fn(*args)
        except Exception as e:
            if attempt == RETRIES:
                raise
            wait = 2 ** attempt
            print(f"    transient error ({e.__class__.__name__}), retrying in {wait}s...")
            time.sleep(wait)


# --- target-model execution -------------------------------------------------

def _call_openai(prompt, model):
    client = OpenAI(api_key=_require_key("OPENAI_API_KEY"))
    # GPT-5 reasoning models reject temperature and legacy max_tokens.
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=MAX_TOKENS,
    )
    return {
        "text": r.choices[0].message.content or "",
        "input_tokens": r.usage.prompt_tokens,
        "output_tokens": r.usage.completion_tokens,
    }


def _call_anthropic(prompt, model):
    client = anthropic.Anthropic(api_key=_require_key("ANTHROPIC_API_KEY"))
    r = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    return {
        "text": next((b.text for b in r.content if b.type == "text"), ""),
        "input_tokens": r.usage.input_tokens,
        "output_tokens": r.usage.output_tokens,
    }


def _call_gemini(prompt, model):
    client = genai.Client(api_key=_require_key("GEMINI_API_KEY"))
    r = client.models.generate_content(model=model, contents=prompt)
    usage = r.usage_metadata
    return {
        "text": r.text or "",
        "input_tokens": usage.prompt_token_count or 0,
        "output_tokens": (usage.candidates_token_count or 0) + (usage.thoughts_token_count or 0),
    }


_TARGET_CALLS = {"openai": _call_openai, "anthropic": _call_anthropic, "gemini": _call_gemini}


def run_prompt(prompt, model, runs):
    """Run the composed prompt `runs` times; return per-run records."""
    call = _TARGET_CALLS[_provider(model)]
    records = []
    for i in range(1, runs + 1):
        start = time.perf_counter()
        result = _with_retry(call, prompt, model)
        result["seconds"] = round(time.perf_counter() - start, 2)
        result["run"] = i
        records.append(result)
        print(f"    run {i}/{runs}: {result['seconds']}s, {result['output_tokens']} output tokens")
    return records


# --- mechanical signal: lexical similarity -----------------------------------
# Recorded as evidence only. Character-level similarity punishes paraphrase
# (normal LLM variance), so the Consistency *score* is judged semantically.

def _normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def lexical_similarity(outputs):
    """Mean pairwise SequenceMatcher ratio across runs (None for a single run)."""
    if len(outputs) < 2:
        return None
    ratios = []
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            ratios.append(difflib.SequenceMatcher(
                None, _normalize(outputs[i]), _normalize(outputs[j])).ratio())
    return round(statistics.mean(ratios), 3)


# --- judge phase (provider-agnostic) ----------------------------------------

def _judged_dims(runs):
    """Consistency is only judgeable with repeated runs."""
    return JUDGED_DIMS + (["consistency"] if runs >= 2 else [])


def _judge_schema(dims):
    dim = {
        "type": "object",
        "properties": {
            "score": {"type": "integer", "enum": [1, 2, 3, 4, 5]},
            "justification": {"type": "string"},
            "evidence": {"type": "string"},
        },
        "required": ["score", "justification", "evidence"],
        "additionalProperties": False,
    }
    props = {k: dim for k in dims}
    props["summary"] = {"type": "string"}
    return {
        "type": "object",
        "properties": props,
        "required": dims + ["summary"],
        "additionalProperties": False,
    }


def _judge_prompt(spec, model, records, similarity):
    dims = _judged_dims(len(records))
    rubric_lines = "\n".join(
        f"- {k} -- {RUBRIC[k]['question']} Anchors: {RUBRIC[k]['anchors']}"
        for k in dims
    )
    context_lines = []
    if spec.get("expected"):
        context_lines.append(f"Expected output (reference): {spec['expected']}")
    if spec.get("format_spec"):
        context_lines.append(f"Format specification: {spec['format_spec']}")
    if spec.get("tone"):
        context_lines.append(f"Intended tone/audience: {spec['tone']}")
    context = "\n".join(context_lines) or \
        "No explicit expectations provided -- infer the requirements from the prompt itself."

    outputs = "\n\n".join(
        f"--- Run {r['run']} ({r['output_tokens']} output tokens, {r['seconds']}s) ---\n{r['text']}"
        for r in records
    )

    consistency_note = ""
    if "consistency" in dims:
        consistency_note = (
            f"\nFor consistency, judge semantic and structural agreement across runs -- "
            f"wording variation alone is not inconsistency. For reference, the mechanical "
            f"lexical-similarity ratio across runs is {similarity} (paraphrase makes low "
            f"ratios normal; judge meaning, structure, and quality stability)."
        )

    shape = ", ".join(f'"{k}": {{"score": 1-5, "justification": "...", "evidence": "..."}}' for k in dims)
    return f"""You are a senior prompt engineer scoring a prompt-pattern evaluation for a
pattern encyclopedia. Grade the response set below against the rubric. Be exacting:
a 5 must be earned, and your evidence must quote or pinpoint specific output text
(cite run numbers). Where runs differ, grade the typical behavior across runs.
For efficiency, weigh the output token counts shown against the quality delivered.{consistency_note}

RUBRIC (score each dimension 1-5):
{rubric_lines}

EVALUATION CONTEXT:
Pattern(s) under test: {spec['pattern']}
{context}

PROMPT UNDER TEST:
<<<PROMPT
{spec['prompt_text']}
PROMPT>>>

RESPONSES FROM MODEL `{model}` ({len(records)} run(s)):
{outputs}

Return ONLY a JSON object with this exact shape (no prose outside the JSON):
{{{shape}, "summary": "..."}}
"""


def _extract_json(text):
    """Parse JSON from a model response, tolerating fences or surrounding prose."""
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        return json.loads(text[start:end + 1])
    raise ValueError("No JSON object found in judge response")


def _judge_anthropic(judge_model, schema, prompt):
    client = anthropic.Anthropic(api_key=_require_key("ANTHROPIC_API_KEY"))
    r = client.messages.create(
        model=judge_model,
        max_tokens=JUDGE_MAX_TOKENS,
        thinking={"type": "adaptive"},
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    if r.stop_reason == "refusal":
        raise RuntimeError("Judge refused the grading request")
    text = next((b.text for b in r.content if b.type == "text"), None)
    if not text:
        raise RuntimeError(f"Judge returned no text (stop_reason={r.stop_reason})")
    return json.loads(text)


def _judge_openai(judge_model, schema, prompt):
    client = OpenAI(api_key=_require_key("OPENAI_API_KEY"))
    r = client.chat.completions.create(
        model=judge_model,
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=JUDGE_MAX_TOKENS,
        response_format={"type": "json_schema",
                         "json_schema": {"name": "rubric_eval", "strict": True, "schema": schema}},
    )
    return json.loads(r.choices[0].message.content)


def _judge_gemini(judge_model, schema, prompt):
    # Gemini's response_schema dialect doesn't map JSON-Schema cleanly (integer
    # enums, additionalProperties); use JSON mime type + the in-prompt shape spec
    # and parse robustly. Schema is unused here by design.
    client = genai.Client(api_key=_require_key("GEMINI_API_KEY"))
    r = client.models.generate_content(
        model=judge_model,
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    return _extract_json(r.text or "")


_JUDGE_CALLS = {"anthropic": _judge_anthropic, "openai": _judge_openai, "gemini": _judge_gemini}


def judge(judge_model, spec, model, records, similarity):
    """Score one model's response set with `judge_model` (any provider). Importable."""
    dims = _judged_dims(len(records))
    schema = _judge_schema(dims)
    prompt = _judge_prompt(spec, model, records, similarity)

    def _call_and_validate():
        # Key-omission is transient LLM flakiness, so it must live INSIDE the retried
        # unit — validating after _with_retry made one malformed verdict fatal
        # (2026-07-02: gemini omitted 'summary' and killed a whole batch pattern).
        verdict = _JUDGE_CALLS[_provider(judge_model)](judge_model, schema, prompt)
        missing = [k for k in dims + ["summary"] if k not in verdict]
        if missing:
            raise RuntimeError(f"Judge {judge_model} omitted keys: {missing}")
        return verdict

    return _with_retry(_call_and_validate)


# --- hybrid review phase ----------------------------------------------------

def review(model, verdicts, dims):
    """Walk the judged dimensions; Enter accepts, '1-5 [note]' overrides, 'a' accepts the rest."""
    print(f"\n=== Review judge scores for {model} (Enter=accept, 1-5 [note]=override, a=accept rest) ===")
    accept_rest = False
    for key in dims:
        v = verdicts[key]
        v["source"] = "judge"
        v["note"] = ""
        if accept_rest:
            continue
        print(f"\n[{RUBRIC[key]['name']}] judge score: {v['score']}/5")
        print(textwrap.indent(textwrap.fill(v["justification"], 90), "  "))
        raw = input("> ").strip()
        if raw.lower() == "a":
            accept_rest = True
        elif raw:
            m = re.match(r"^([1-5])\s*(.*)$", raw)
            if m:
                v["judge_score"] = v["score"]
                v["score"] = int(m.group(1))
                v["source"] = "human"
                v["note"] = m.group(2)
            else:
                print("  (unrecognized input -- judge score kept)")
    return verdicts


# --- result assembly --------------------------------------------------------

def _verdict_label(score):
    return "Strong" if score >= 4.5 else "Solid" if score >= 3.5 else "Mixed" if score >= 2.5 else "Weak"


def build_results(spec, models, runs, judges, review_mode,
                  all_runs, all_verdicts, all_similarity, method="mean"):
    """Assemble the full result record (drives both .json and .md).

    `judges` is the panel (a 1-element list is the single-judge case). For a single
    judge, NO panel metadata is attached, so the result is byte-identical to the
    pre-panel output; for a panel, each dimension carries a `panel` breakdown and the
    model block carries `panel_meta`.
    """
    is_panel = len(judges) > 1
    models_block = []
    for model in models:
        verdicts = all_verdicts[model]
        ratio = all_similarity[model]
        dims = {}
        for key in _judged_dims(runs):
            dims[key] = {k: verdicts[key].get(k) for k in
                         ("score", "justification", "evidence", "source", "note", "judge_score")}
            if is_panel and "panel" in verdicts[key]:
                dims[key]["panel"] = verdicts[key]["panel"]
        if "consistency" in dims:
            dims["consistency"]["lexical_similarity"] = ratio
            dims["consistency"]["justification"] += f" [lexical similarity ratio: {ratio}]"
        else:
            dims["consistency"] = {
                "score": None, "justification": "N/A -- single run", "evidence": "",
                "source": "n/a", "note": "", "lexical_similarity": None,
            }
        scored = [d["score"] for d in dims.values() if d["score"] is not None]
        overall = round(statistics.mean(scored), 1)
        block = {
            "model": model,
            "overall": overall,
            "verdict": _verdict_label(overall),
            "dimensions": dims,
            "judge_summary": verdicts["summary"],
            "runs": all_runs[model],
        }
        if is_panel and verdicts.get("_panel_meta"):
            block["panel_meta"] = verdicts["_panel_meta"]
        models_block.append(block)
    results = {
        "tool": f"PromptEval v{TOOL_VERSION}",
        "pattern": spec["pattern"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "judge": judges[0] if not is_panel else f"panel[{', '.join(judges)}]",
        "runs_per_model": runs,
        "review_mode": review_mode,
        "context": {k: spec.get(k) for k in ("expected", "format_spec", "tone")},
        "prompt": spec["prompt_text"],
        "models": models_block,
    }
    if is_panel:
        results["judges"] = judges
        results["aggregate_method"] = method
    return results


def _slug(text):
    return re.sub(r"[^a-z0-9+-]+", "-", text.lower()).strip("-")


def write_reports(results, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    base = out / f"{_slug(results['pattern'])}__{stamp}"
    base.with_suffix(".json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    base.with_suffix(".md").write_text(_render_markdown(results), encoding="utf-8")
    return base.with_suffix(".md"), base.with_suffix(".json")


def _render_panel_block(add, m):
    """Per-model judge-panel breakdown table ([A3]). Only called for panel runs."""
    meta = m["panel_meta"]
    judges, providers, target = meta["judges"], meta["providers"], meta["target_provider"]
    add(f"**Judge panel** — {meta['n_judges']} judges, aggregate: {meta['method']}. "
        f"`*` = judge shares the target's provider ({target}); ⚠ = that judge scored the "
        f"dimension above the cross-provider judges (self-preference watch).")
    add("")
    add("| Dimension | Agg | "
        + " | ".join(f"{j}{' *' if providers.get(j) == target else ''}" for j in judges)
        + " | Spread | Stdev |")
    add("|" + "---|" * (len(judges) + 4))
    for k in DIM_ORDER:
        d = m["dimensions"].get(k, {})
        p = d.get("panel")
        if not p:
            continue  # e.g. consistency on a single run — no panel data
        flag = " ⚠" if p["self_preference"]["flag"] else ""
        cells = " | ".join(str(p["judges"][j]) for j in judges)
        add(f"| {RUBRIC[k]['name']}{flag} | {d['score']} | {cells} | {p['spread']} | {p['stdev']} |")
    add("")
    spd = meta.get("self_preference_delta")
    if spd is not None:
        add(f"- **Self-preference delta:** {spd:+} total-score points "
            f"(same-provider vs cross-provider judges; positive = the same-provider judge scored higher).")
    contested = meta.get("contested_dims") or []
    if contested:
        add("- **Contested dimensions (spread ≥ 2):** "
            + ", ".join(RUBRIC[k]["name"] for k in contested) + ".")
    add(f"- **Panel mean spread/dim:** {meta['mean_spread']} (max {meta['max_spread']}).")
    add("")


def _render_markdown(results):
    is_panel = bool(results.get("judges"))
    lines = []
    add = lines.append
    add(f"# Eval: {results['pattern']}")
    add("")
    judge_cell = (f"**Judge:** {results['judge']}" if not is_panel
                  else f"**Judges:** {', '.join(results['judges'])} (aggregate: {results['aggregate_method']})")
    add(f"**Date:** {results['date']} | {judge_cell} | "
        f"**Runs/model:** {results['runs_per_model']} | **Review:** {results['review_mode']}")
    add("")
    add("---")
    add("")
    add("## Verdict")
    add("")
    add("| Model | Overall | " + " | ".join(RUBRIC[k]["name"] for k in DIM_ORDER) + " |")
    add("|" + "---|" * (len(DIM_ORDER) + 2))
    for m in results["models"]:
        cells = [str(m["dimensions"][k]["score"] if m["dimensions"][k]["score"] else "N/A")
                 for k in DIM_ORDER]
        add(f"| {m['model']} | **{m['overall']} ({m['verdict']})** | " + " | ".join(cells) + " |")
    add("")

    for m in results["models"]:
        add("---")
        add("")
        add(f"## Scorecard: {m['model']}")
        add("")
        add(f"> {m['judge_summary']}")
        add("")
        add("| Dimension | Score | Source | Justification |")
        add("|---|---|---|---|")
        for k in DIM_ORDER:
            d = m["dimensions"][k]
            score = d["score"] if d["score"] is not None else "N/A"
            just = d["justification"].replace("|", "\\|")
            if d.get("note"):
                just += f" *Override note: {d['note']}*"
            if d.get("judge_score") and d["source"] == "human":
                just += f" *(judge said {d['judge_score']})*"
            add(f"| {RUBRIC[k]['name']} | {score} | {d['source']} | {just} |")
        add("")
        if is_panel and m.get("panel_meta"):
            _render_panel_block(add, m)
        runs = m["runs"]
        avg_out = round(statistics.mean(r["output_tokens"] for r in runs))
        avg_sec = round(statistics.mean(r["seconds"] for r in runs), 2)
        add(f"Tokens (avg output): {avg_out} | Latency (avg): {avg_sec}s | Runs: {len(runs)}")
        add("")

    add("---")
    add("")
    add("## Prompt Under Test")
    add("")
    add("```text")
    add(results["prompt"].rstrip())
    add("```")
    add("")
    add("---")
    add("")
    first = results["models"][0]
    add(f"## Sample Output ({first['model']}, run 1)")
    add("")
    add("```text")
    add(first["runs"][0]["text"].rstrip())
    add("```")
    add("")
    add("---")
    add("")
    add("## Method")
    add("")
    add(f"- Tool: {results['tool']}; provider-default sampling settings; "
        f"max output budget {MAX_TOKENS} tokens.")
    add(f"- All dimensions scored 1-5 by {results['judge']}"
        + (" with human accept/override per dimension." if results["review_mode"] != "automated"
           else " (no human review)")
        + "; consistency is judged semantically across runs, with the mechanical lexical-similarity "
        "ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.")
    add("- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); "
        "Gemini counts include thought tokens.")
    add("")
    return "\n".join(lines)


# --- the core single-eval pipeline (importable) -----------------------------

def evaluate(spec, models, runs, judges, do_review, out_dir, method="mean"):
    """Run + judge + (optionally) review one composed prompt; write reports.

    spec keys: pattern, prompt_text, [expected], [format_spec], [tone].
    `judges` is the judge panel — a 1-element list is the single-judge case and is
    scored/rendered exactly as before. With >1 judge every dimension is panel-scored
    via panel.score_with_panel and the aggregate (mean by default) becomes the score.
    Returns the results dict (also written to disk).
    """
    dims = _judged_dims(runs)
    is_panel = len(judges) > 1
    all_runs, all_verdicts, all_similarity = {}, {}, {}
    for model in models:
        print(f"[{model}] executing prompt...")
        records = run_prompt(spec["prompt_text"], model, runs)
        all_runs[model] = records
        sim = lexical_similarity([r["text"] for r in records])
        all_similarity[model] = sim
        label = judges[0] if not is_panel else f"panel of {len(judges)} ({', '.join(judges)})"
        print(f"[{model}] judging with {label}...")

        def _score_one(j, _model=model, _records=records, _sim=sim):
            return judge(j, spec, _model, _records, _sim)

        def _progress(j, same, _model=model):
            if is_panel:
                tag = "  [SAME PROVIDER as target -- self-preference watch]" if same else ""
                print(f"    judge {j}{tag}")

        all_verdicts[model] = panel.score_with_panel(
            judges, _score_one, dims, _provider(model), _provider,
            method=method, on_judge=_progress)

    if do_review:
        for model in models:
            all_verdicts[model] = review(model, all_verdicts[model], dims)
    else:
        for model in models:
            for key in dims:
                all_verdicts[model][key]["source"] = "judge"
                all_verdicts[model][key]["note"] = ""

    review_mode = "hybrid (judge + human override)" if do_review else "automated"
    results = build_results(spec, models, runs, judges, review_mode,
                            all_runs, all_verdicts, all_similarity, method)
    md_path, json_path = write_reports(results, out_dir)
    results["_md_path"] = str(md_path)
    results["_json_path"] = str(json_path)
    return results


# --- batch mode -------------------------------------------------------------

def _load_manifest(path):
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    base = Path(path).parent
    for spec in manifest["evals"]:
        if "prompt_file" in spec and "prompt_text" not in spec:
            spec["prompt_text"] = (base / spec["prompt_file"]).read_text(encoding="utf-8")
        elif "prompt" in spec:
            spec["prompt_text"] = spec["prompt"]
        if not spec.get("prompt_text", "").strip():
            raise ValueError(f"Eval '{spec.get('pattern', '?')}' has an empty prompt")
    return manifest


def run_batch(manifest, models, runs, judges, do_review, out_dir, method="mean", abort_after=4):
    specs = manifest["evals"]
    label = judges[0] if len(judges) == 1 else f"panel[{', '.join(judges)}]"
    print(f"PromptEval v{TOOL_VERSION} BATCH -- {len(specs)} evals x {len(models)} models")
    print(f"Targets: {', '.join(models)} | runs/model: {runs} | judge: {label}\n")
    all_results = []
    failed = []
    consecutive = 0  # circuit breaker: N consecutive failures => systemic (provider quota/auth/outage)
    for n, spec in enumerate(specs, 1):
        print(f"\n========== [{n}/{len(specs)}] {spec['pattern']} ==========")
        # Resilience: one eval's failure (a refusal, sustained 503, model 404) must NOT
        # crash a long multi-pattern campaign — log it, keep its completed siblings, continue.
        # Re-run only the failed patterns afterward (their reports were never written).
        try:
            all_results.append(evaluate(spec, models, runs, judges, do_review, out_dir, method))
            consecutive = 0
        except Exception as e:
            failed.append((spec.get("pattern", "?"), f"{e.__class__.__name__}: {e}"))
            consecutive += 1
            print(f"  !! FAILED [{spec.get('pattern', '?')}]: {e.__class__.__name__}: {e}")
            # Circuit breaker: a run of consecutive failures is almost always systemic (a provider's
            # daily quota/billing/auth, or an outage) — not per-pattern. Stop instead of burning the
            # other providers' spend across the whole remaining batch (the 2026-06-20 gemini-free-tier
            # incident: 39/40 attempted after gemini was dead-for-the-day). Fix the cause, then resume.
            if abort_after and consecutive >= abort_after:
                remaining = len(specs) - n
                print(f"\n!! CIRCUIT BREAKER: {consecutive} consecutive failures — likely systemic "
                      f"(provider quota/auth/outage), not per-pattern. Aborting with {remaining} "
                      f"pattern(s) unattempted to save spend. Fix the cause, then resume the unscored set.")
                break
            continue
    md_path, json_path = write_batch_reports(all_results, models, judges, runs, out_dir, method)
    print("\n=== Batch complete ===")
    for r in all_results:
        scores = " | ".join(f"{m['model'].split('-')[0]}:{m['overall']}" for m in r["models"])
        print(f"  {r['pattern']}: {scores}")
    if failed:
        print(f"\n!! {len(failed)} of {len(specs)} pattern(s) FAILED — re-run these: "
              + ", ".join(p for p, _ in failed))
        for p, err in failed:
            print(f"   - {p}: {err}")
    print(f"\nMatrix:  {md_path}\nSidecar: {json_path}")
    return all_results


def write_batch_reports(all_results, models, judges, runs, out_dir, method="mean"):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    base = out / f"batch__{stamp}"
    is_panel = len(judges) > 1
    label = judges[0] if not is_panel else f"panel[{', '.join(judges)}]"

    payload = {
        "tool": f"PromptEval v{TOOL_VERSION} (batch)",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "judge": label,
        "runs_per_model": runs,
        "models": models,
        "evals": all_results,
    }
    if is_panel:
        payload["judges"] = judges
        payload["aggregate_method"] = method
    base.with_suffix(".json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    base.with_suffix(".md").write_text(
        _render_batch_markdown(all_results, models, label, runs), encoding="utf-8")
    return base.with_suffix(".md"), base.with_suffix(".json")


def _render_batch_markdown(all_results, models, judge_model, runs):
    lines = []
    add = lines.append
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    add(f"# Batch Eval — {len(all_results)} patterns × {len(models)} models")
    add("")
    add(f"**Date:** {date} | **Judge:** {judge_model} | **Runs/model:** {runs}")
    add("")
    add("---")
    add("")
    add("## Overall matrix (mean rubric score, 1–5)")
    add("")
    add("| Pattern | " + " | ".join(models) + " | Pattern mean |")
    add("|" + "---|" * (len(models) + 2))
    col_totals = {m: [] for m in models}
    for r in all_results:
        by_model = {mb["model"]: mb["overall"] for mb in r["models"]}
        row = []
        for m in models:
            val = by_model.get(m)
            if val is not None:
                col_totals[m].append(val)
            row.append(f"{val}" if val is not None else "—")
        pmean = round(statistics.mean(by_model.values()), 2) if by_model else "—"
        add(f"| {r['pattern']} | " + " | ".join(row) + f" | {pmean} |")
    means = [f"**{round(statistics.mean(col_totals[m]), 2)}**" if col_totals[m] else "—" for m in models]
    add("| **Model mean** | " + " | ".join(means) + " | |")
    add("")

    add("## Per-dimension means across all patterns (by model)")
    add("")
    add("| Dimension | " + " | ".join(models) + " |")
    add("|" + "---|" * (len(models) + 1))
    for k in DIM_ORDER:
        row = []
        for m in models:
            vals = []
            for r in all_results:
                mb = next((x for x in r["models"] if x["model"] == m), None)
                if mb and mb["dimensions"][k]["score"] is not None:
                    vals.append(mb["dimensions"][k]["score"])
            row.append(f"{round(statistics.mean(vals), 2)}" if vals else "—")
        add(f"| {RUBRIC[k]['name']} | " + " | ".join(row) + " |")
    add("")

    add("## Individual reports")
    add("")
    for r in all_results:
        fname = Path(r.get("_md_path", "")).name
        add(f"- **{r['pattern']}** — [`{fname}`]({fname})")
    add("")
    return "\n".join(lines)


# --- CLI --------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Rubric-based prompt-pattern evaluation (Prompt Pattern Encyclopedia).")
    p.add_argument("prompt_file", nargs="?", help="File with the composed prompt (or --prompt / stdin)")
    p.add_argument("--prompt", help="Composed prompt as a literal string")
    p.add_argument("--pattern", help="Pattern(s) under test, e.g. role-persona+strict-output-format")
    p.add_argument("--batch", help="JSON manifest of many evals -> one aggregated matrix report")
    p.add_argument("--models", default=",".join(DEFAULT_MODELS),
                   help=f"Comma-separated target models (default: {','.join(DEFAULT_MODELS)})")
    p.add_argument("--runs", type=int, default=3, help="Runs per model (consistency needs >= 2; default 3)")
    p.add_argument("--expected", help="What a correct answer should contain (grounds Accuracy/Completeness)")
    p.add_argument("--format-spec", help="What format compliance means for this prompt")
    p.add_argument("--tone", help="Intended tone and audience")
    p.add_argument("--judge", default=DEFAULT_JUDGE,
                   help=f"Single judge model, any provider (default {DEFAULT_JUDGE})")
    p.add_argument("--judges",
                   help="Comma-separated judge PANEL, ideally cross-provider (overrides --judge; "
                        "every dimension is scored by each judge and the aggregate becomes the score)")
    p.add_argument("--aggregate", choices=["mean", "median"], default="mean",
                   help="Panel aggregate method (default mean; median is outlier-robust)")
    p.add_argument("--out-dir", default="evals", help="Output dir for artifacts (default evals/)")
    p.add_argument("--no-review", action="store_true", help="Skip interactive override; judge scores stand")
    return p.parse_args()


def main():
    args = parse_args()
    models = [m.strip() for m in args.models.split(",") if m.strip()]

    if args.batch:
        manifest = _load_manifest(args.batch)
        batch_models = ([m.strip() for m in manifest["models"]]
                        if isinstance(manifest.get("models"), list) else models)
        # judge precedence: manifest.judges > CLI --judges > manifest.judge > CLI --judge
        if isinstance(manifest.get("judges"), list) and manifest["judges"]:
            batch_judges = [j.strip() for j in manifest["judges"] if j.strip()]
        elif args.judges:
            batch_judges = [j.strip() for j in args.judges.split(",") if j.strip()]
        else:
            batch_judges = [manifest.get("judge", args.judge)]
        run_batch(
            manifest,
            batch_models,
            manifest.get("runs", args.runs),
            batch_judges,
            not args.no_review,
            args.out_dir,
            manifest.get("aggregate", args.aggregate),
        )
        return

    if not args.pattern:
        sys.exit("--pattern is required in single mode (or use --batch manifest.json)")
    if args.prompt:
        prompt_text = args.prompt
    elif args.prompt_file:
        prompt_text = Path(args.prompt_file).read_text(encoding="utf-8")
    else:
        print("Paste the composed prompt, then EOF (Ctrl+Z then Enter on Windows):")
        prompt_text = sys.stdin.read()
    if not prompt_text.strip():
        sys.exit("Empty prompt.")

    judges = ([j.strip() for j in args.judges.split(",") if j.strip()]
              if args.judges else [args.judge])
    label = judges[0] if len(judges) == 1 else f"panel[{', '.join(judges)}]"
    spec = {"pattern": args.pattern, "prompt_text": prompt_text,
            "expected": args.expected, "format_spec": args.format_spec, "tone": args.tone}
    print(f"PromptEval v{TOOL_VERSION} -- pattern: {args.pattern}")
    print(f"Targets: {', '.join(models)} | runs/model: {args.runs} | judge: {label}\n")
    results = evaluate(spec, models, args.runs, judges, not args.no_review, args.out_dir, args.aggregate)

    print("\n=== Results ===")
    for m in results["models"]:
        print(f"  {m['model']}: {m['overall']}/5 ({m['verdict']})")
    print(f"\nReport:  {results['_md_path']}\nSidecar: {results['_json_path']}")


if __name__ == "__main__":
    main()
