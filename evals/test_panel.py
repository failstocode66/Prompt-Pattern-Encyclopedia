# Unit tests for panel.py — the shared multi-judge panel aggregator ([A1]).
#
# Pure aggregation, no API calls, so this runs offline:  py evals/test_panel.py
# (or  py -m unittest evals.test_panel).

import unittest

import panel


class SummarizeScores(unittest.TestCase):
    def test_single_score_is_degenerate(self):
        s = panel.summarize_scores([4])
        self.assertEqual(s["score"], 4)
        self.assertEqual(s["mean"], 4.0)
        self.assertEqual(s["median"], 4)
        self.assertEqual(s["spread"], 0)
        self.assertEqual(s["stdev"], 0.0)
        self.assertEqual(s["scores"], [4])

    def test_mean_rounded_half_up(self):
        self.assertEqual(panel.summarize_scores([4, 5])["score"], 5)      # 4.5 -> 5
        self.assertEqual(panel.summarize_scores([2, 3])["score"], 3)      # 2.5 -> 3
        self.assertEqual(panel.summarize_scores([3, 4, 5])["score"], 4)   # 4.0 -> 4
        self.assertEqual(panel.summarize_scores([1, 1, 2])["score"], 1)   # 1.33 -> 1

    def test_spread_min_max_stdev(self):
        s = panel.summarize_scores([3, 4, 5])
        self.assertEqual(s["spread"], 2)
        self.assertEqual(s["min"], 3)
        self.assertEqual(s["max"], 5)
        self.assertGreater(s["stdev"], 0)

    def test_median_method_is_outlier_robust(self):
        # one judge wildly disagrees: median ignores it, mean is dragged
        self.assertEqual(panel.summarize_scores([1, 1, 5], method="median")["score"], 1)
        self.assertEqual(panel.summarize_scores([1, 1, 5], method="mean")["score"], 2)  # 2.33 -> 2

    def test_rejects_unknown_method_and_empty(self):
        with self.assertRaises(ValueError):
            panel.summarize_scores([4], method="mode")
        with self.assertRaises(ValueError):
            panel.summarize_scores([])


class SelfPreference(unittest.TestCase):
    def test_flag_when_same_provider_scores_higher(self):
        rows = [
            {"same_provider_as_target": True,  "scores": {"accuracy": 5}},
            {"same_provider_as_target": False, "scores": {"accuracy": 4}},
            {"same_provider_as_target": False, "scores": {"accuracy": 4}},
        ]
        sp = panel.self_preference(rows, "accuracy")
        self.assertTrue(sp["flag"])
        self.assertEqual(sp["delta"], 1.0)

    def test_no_flag_when_same_provider_scores_lower_or_equal(self):
        rows = [
            {"same_provider_as_target": True,  "scores": {"accuracy": 4}},
            {"same_provider_as_target": False, "scores": {"accuracy": 4}},
        ]
        self.assertFalse(panel.self_preference(rows, "accuracy")["flag"])

    def test_no_flag_without_both_groups(self):
        rows = [{"same_provider_as_target": True, "scores": {"accuracy": 5}}]
        sp = panel.self_preference(rows, "accuracy")
        self.assertFalse(sp["flag"])
        self.assertIsNone(sp["delta"])


def _verdict(scores, summary="ok"):
    """Build a pe.judge-shaped verdict from a {dim: score} map."""
    v = {d: {"score": s, "justification": f"just-{d}-{s}", "evidence": f"ev-{d}-{s}"}
         for d, s in scores.items()}
    v["summary"] = summary
    return v


class BuildPanelVerdict(unittest.TestCase):
    DIMS = ["accuracy", "completeness"]

    def test_single_judge_no_behavior_change(self):
        jr = [{"judge": "claude-opus-4-8", "provider": "anthropic",
               "same_provider_as_target": True,
               "verdict": _verdict({"accuracy": 4, "completeness": 3}, "single")}]
        pv = panel.build_panel_verdict(jr, self.DIMS, "anthropic")
        # per-dim score/justification/evidence identical to the lone judge's verdict
        self.assertEqual(pv["accuracy"]["score"], 4)
        self.assertEqual(pv["accuracy"]["justification"], "just-accuracy-4")
        self.assertEqual(pv["accuracy"]["evidence"], "ev-accuracy-4")
        self.assertEqual(pv["completeness"]["score"], 3)
        self.assertEqual(pv["summary"], "single")
        # degenerate panel metadata
        self.assertEqual(pv["accuracy"]["panel"]["spread"], 0)
        self.assertEqual(pv["accuracy"]["panel"]["stdev"], 0.0)
        self.assertEqual(pv["accuracy"]["panel"]["judges"], {"claude-opus-4-8": 4})
        self.assertFalse(pv["accuracy"]["panel"]["self_preference"]["flag"])
        self.assertEqual(pv["_panel_meta"]["n_judges"], 1)

    def test_three_judge_aggregate_and_self_preference(self):
        jr = [
            {"judge": "gpt-5.4-mini", "provider": "openai", "same_provider_as_target": False,
             "verdict": _verdict({"accuracy": 4, "completeness": 4}, "gpt-sum")},
            {"judge": "claude-opus-4-8", "provider": "anthropic", "same_provider_as_target": True,
             "verdict": _verdict({"accuracy": 5, "completeness": 4}, "claude-sum")},
            {"judge": "gemini-2.5-flash", "provider": "gemini", "same_provider_as_target": False,
             "verdict": _verdict({"accuracy": 4, "completeness": 3}, "gemini-sum")},
        ]
        pv = panel.build_panel_verdict(jr, self.DIMS, "anthropic")
        # accuracy [4,5,4] -> mean 4.33 -> 4; spread 1
        self.assertEqual(pv["accuracy"]["score"], 4)
        self.assertEqual(pv["accuracy"]["panel"]["spread"], 1)
        self.assertEqual(pv["accuracy"]["panel"]["judges"],
                         {"gpt-5.4-mini": 4, "claude-opus-4-8": 5, "gemini-2.5-flash": 4})
        # same-provider (anthropic) judge gave 5 vs cross mean 4 -> self-preference flag
        self.assertTrue(pv["accuracy"]["panel"]["self_preference"]["flag"])
        self.assertEqual(pv["accuracy"]["panel"]["self_preference"]["delta"], 1.0)
        # representative justification comes from a judge AT the aggregate score (4, first listed)
        self.assertEqual(pv["accuracy"]["justification"], "just-accuracy-4")
        # overall meta
        self.assertEqual(pv["_panel_meta"]["judges"],
                         ["gpt-5.4-mini", "claude-opus-4-8", "gemini-2.5-flash"])
        self.assertEqual(pv["_panel_meta"]["method"], "mean")
        self.assertEqual(pv["_panel_meta"]["n_judges"], 3)
        # representative summary = the judge with the MEDIAN total (gpt: 8, claude: 9, gemini: 7) -> gpt
        self.assertEqual(pv["summary"], "gpt-sum")

    def test_median_method_threads_through(self):
        jr = [
            {"judge": "j1", "provider": "openai", "same_provider_as_target": False,
             "verdict": _verdict({"accuracy": 1})},
            {"judge": "j2", "provider": "openai", "same_provider_as_target": False,
             "verdict": _verdict({"accuracy": 1})},
            {"judge": "j3", "provider": "openai", "same_provider_as_target": False,
             "verdict": _verdict({"accuracy": 5})},
        ]
        pv = panel.build_panel_verdict(jr, ["accuracy"], "anthropic", method="median")
        self.assertEqual(pv["accuracy"]["score"], 1)  # median ignores the outlier 5
        self.assertEqual(pv["accuracy"]["panel"]["method"], "median")


class ScoreWithPanel(unittest.TestCase):
    def test_injected_scorer_called_once_per_judge(self):
        calls = []

        def score_one(j):
            calls.append(j)
            return _verdict({"accuracy": 4})

        prov = lambda m: {"a": "anthropic"}.get(m, "openai")
        pv = panel.score_with_panel(["a", "g"], score_one, ["accuracy"], "anthropic", prov)
        self.assertEqual(calls, ["a", "g"])
        self.assertEqual(pv["accuracy"]["panel"]["judges"], {"a": 4, "g": 4})
        # 'a' shares the target provider (anthropic); 'g' does not
        self.assertEqual(pv["_panel_meta"]["providers"], {"a": "anthropic", "g": "openai"})

    def test_single_judge_list_reproduces_single_mode(self):
        pv = panel.score_with_panel(
            ["claude-opus-4-8"],
            lambda j: _verdict({"accuracy": 5, "completeness": 4}, "solo"),
            ["accuracy", "completeness"], "anthropic", lambda m: "anthropic")
        self.assertEqual(pv["accuracy"]["score"], 5)
        self.assertEqual(pv["completeness"]["score"], 4)
        self.assertEqual(pv["summary"], "solo")
        self.assertEqual(pv["_panel_meta"]["n_judges"], 1)


if __name__ == "__main__":
    unittest.main()
