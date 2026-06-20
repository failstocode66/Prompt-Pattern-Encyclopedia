# Offline wiring tests for PromptEval's panel integration ([A2]).
#
# Monkeypatches run_prompt + judge so evaluate() runs end-to-end (incl. report
# writing) with NO API calls. Verifies (a) single-judge output is unchanged and
# (b) a judge panel aggregates per dimension. Live cross-provider verification is [A4].
#   py evals/test_eval_wiring.py

import tempfile
import unittest

import PromptEval as pe

# Real provider-prefixed names so PromptEval._provider() resolves them.
_SCORES = {"gpt-5.4-mini": 4, "claude-opus-4-8": 5, "gemini-2.5-flash": 4, "claude-haiku-4-5": 3}


def _fake_run_prompt(prompt, model, runs):
    return [{"text": f"out-{model}-{i}", "input_tokens": 10, "output_tokens": 20,
             "seconds": 0.1, "run": i} for i in range(1, runs + 1)]


def _fake_judge(judge_model, spec, model, records, similarity):
    s = _SCORES.get(judge_model, 4)
    dims = pe._judged_dims(len(records))
    v = {d: {"score": s, "justification": f"{judge_model}-{d}", "evidence": "ev"} for d in dims}
    v["summary"] = f"{judge_model}-summary"
    return v


_SPEC = {"pattern": "demo", "prompt_text": "p", "expected": None, "format_spec": None, "tone": None}


class EvalWiring(unittest.TestCase):
    def setUp(self):
        self._rp, self._j = pe.run_prompt, pe.judge
        pe.run_prompt, pe.judge = _fake_run_prompt, _fake_judge
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        pe.run_prompt, pe.judge = self._rp, self._j

    def test_single_judge_is_unchanged(self):
        res = pe.evaluate(_SPEC, ["claude-sonnet-4-6"], 1, ["claude-haiku-4-5"], False, self.tmp)
        self.assertEqual(res["judge"], "claude-haiku-4-5")
        self.assertNotIn("judges", res)            # no panel metadata leaks into single-judge output
        self.assertNotIn("aggregate_method", res)
        m = res["models"][0]
        self.assertEqual(m["dimensions"]["accuracy"]["score"], 3)
        self.assertNotIn("panel", m["dimensions"]["accuracy"])
        self.assertNotIn("panel_meta", m)

    def test_panel_aggregates_per_dimension(self):
        judges = ["gpt-5.4-mini", "claude-opus-4-8", "gemini-2.5-flash"]
        res = pe.evaluate(_SPEC, ["claude-sonnet-4-6"], 1, judges, False, self.tmp, "mean")
        self.assertTrue(res["judge"].startswith("panel["))
        self.assertEqual(res["judges"], judges)
        self.assertEqual(res["aggregate_method"], "mean")
        m = res["models"][0]
        acc = m["dimensions"]["accuracy"]
        self.assertEqual(acc["score"], 4)          # mean(4,5,4)=4.33 -> 4
        self.assertEqual(acc["panel"]["judges"],
                         {"gpt-5.4-mini": 4, "claude-opus-4-8": 5, "gemini-2.5-flash": 4})
        # claude-opus shares the target's provider (anthropic) and scored higher -> flag
        self.assertTrue(acc["panel"]["self_preference"]["flag"])
        self.assertIn("panel_meta", m)
        self.assertEqual(m["panel_meta"]["n_judges"], 3)

    def test_median_panel_is_outlier_robust(self):
        # claude-haiku=3 is the outlier vs gpt/gemini=4; median ignores it
        judges = ["gpt-5.4-mini", "gemini-2.5-flash", "claude-haiku-4-5"]
        res = pe.evaluate(_SPEC, ["claude-sonnet-4-6"], 1, judges, False, self.tmp, "median")
        acc = res["models"][0]["dimensions"]["accuracy"]
        self.assertEqual(acc["score"], 4)          # median(4,4,3)=4
        self.assertEqual(acc["panel"]["method"], "median")

    def test_panel_markdown_renders_breakdown(self):
        judges = ["gpt-5.4-mini", "claude-opus-4-8", "gemini-2.5-flash"]
        res = pe.evaluate(_SPEC, ["claude-sonnet-4-6"], 1, judges, False, self.tmp, "mean")
        md = open(res["_md_path"], encoding="utf-8").read()
        self.assertIn("Judge panel", md)
        self.assertIn("**Judges:**", md)
        self.assertIn("Self-preference delta", md)
        for j in judges:                            # each judge has a breakdown column
            self.assertIn(j, md)
        self.assertIn("⚠", md)                      # claude-opus (same provider) scored higher -> flag

    def test_single_judge_markdown_has_no_panel(self):
        res = pe.evaluate(_SPEC, ["claude-sonnet-4-6"], 1, ["claude-haiku-4-5"], False, self.tmp)
        md = open(res["_md_path"], encoding="utf-8").read()
        self.assertNotIn("Judge panel", md)
        self.assertIn("**Judge:**", md)
        self.assertNotIn("**Judges:**", md)


class BatchResilience(unittest.TestCase):
    """run_batch must skip a failed eval and keep its completed siblings ([B3] hardening)."""

    def setUp(self):
        self._ev, self._wr = pe.evaluate, pe.write_batch_reports

    def tearDown(self):
        pe.evaluate, pe.write_batch_reports = self._ev, self._wr

    def test_failed_eval_is_skipped_not_fatal(self):
        def fake_eval(spec, models, runs, judges, do_review, out_dir, method="mean"):
            if spec["pattern"] == "boom":
                raise RuntimeError("provider 503")
            return {"pattern": spec["pattern"], "models": [{"model": "m", "overall": 4.0}]}

        pe.evaluate = fake_eval
        pe.write_batch_reports = lambda *a, **k: ("x.md", "x.json")
        manifest = {"evals": [{"pattern": "a"}, {"pattern": "boom"}, {"pattern": "c"}]}
        res = pe.run_batch(manifest, ["m"], 1, ["j"], False, "/tmp", "mean")
        self.assertEqual([r["pattern"] for r in res], ["a", "c"])  # boom skipped; a + c survive


if __name__ == "__main__":
    unittest.main()
