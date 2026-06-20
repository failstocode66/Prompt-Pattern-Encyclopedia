# Offline tests for memory_eval.py ([C2]).
# Monkeypatches run_prompt + judge + load_lesson_body so the WITH/WITHOUT A/B runs with
# no API calls. A fake judge scores higher when the lesson is present, simulating a helpful
# lesson, so the delta/outcome/summary logic is exercised end-to-end.  py evals/test_memory_eval.py

import unittest

import PromptEval as pe
import memory_eval as me

_INJECT_MARKER = "note(s) from past work"


def _fake_run_prompt(prompt, model, runs):
    return [{"text": f"answer[{'WITH' if _INJECT_MARKER in prompt else 'WITHOUT'}]",
             "input_tokens": 5, "output_tokens": 10, "seconds": 0.1, "run": i}
            for i in range(1, runs + 1)]


def _fake_judge(judge_model, spec, model, records, similarity):
    # A helpful lesson => the injected (WITH) prompt scores higher.
    base = 5 if _INJECT_MARKER in spec["prompt_text"] else 3
    dims = pe._judged_dims(len(records))
    v = {d: {"score": base, "justification": "j", "evidence": "e"} for d in dims}
    v["summary"] = "s"
    return v


class StripFrontmatter(unittest.TestCase):
    def test_strips_yaml_block(self):
        self.assertEqual(
            me.strip_frontmatter("---\na: 1\nb: 2\n---\nHello body\nmore").strip(),
            "Hello body\nmore")

    def test_no_frontmatter_passthrough(self):
        self.assertEqual(me.strip_frontmatter("Just text").strip(), "Just text")


class Inject(unittest.TestCase):
    def test_includes_lesson_and_task(self):
        out = me.inject(["LESSON BODY"], "THE TASK")
        self.assertIn("LESSON BODY", out)
        self.assertIn("THE TASK", out)
        self.assertIn(_INJECT_MARKER, out)


class EvaluateCase(unittest.TestCase):
    def setUp(self):
        self._rp, self._j, self._ll = pe.run_prompt, pe.judge, me.load_lesson_body
        pe.run_prompt, pe.judge = _fake_run_prompt, _fake_judge
        me.load_lesson_body = lambda slug, d: f"FAKE LESSON BODY for {slug}"

    def tearDown(self):
        pe.run_prompt, pe.judge, me.load_lesson_body = self._rp, self._j, self._ll

    def test_helpful_lesson_is_a_win(self):
        case = {"id": "c1", "task": "do x", "relevant_lessons": ["L"],
                "reference": "ref", "dimensions": ["accuracy", "completeness"]}
        r = me.evaluate_case(case, "claude-sonnet-4-6", ["gpt-5.4-mini", "gemini-2.5-flash"], 1, "dir")
        self.assertEqual(r["without_overall"], 3.0)
        self.assertEqual(r["with_overall"], 5.0)
        self.assertEqual(r["delta"], 2.0)
        self.assertEqual(r["outcome"], "win")
        # the WITH answer actually carried the injected lesson
        self.assertEqual(r["with"]["answer"], "answer[WITH]")
        self.assertEqual(r["without"]["answer"], "answer[WITHOUT]")

    def test_only_target_dims_drive_overall(self):
        case = {"id": "c2", "task": "do y", "relevant_lessons": ["L"],
                "reference": "ref", "dimensions": ["accuracy"]}
        r = me.evaluate_case(case, "claude-sonnet-4-6", ["gpt-5.4-mini"], 1, "dir")
        self.assertEqual(r["target_dims"], ["accuracy"])
        self.assertEqual(r["with_overall"], 5.0)


class Summarize(unittest.TestCase):
    def test_win_rate_and_lift(self):
        s = me.summarize([{"outcome": "win", "delta": 2.0},
                          {"outcome": "win", "delta": 1.0},
                          {"outcome": "tie", "delta": 0.0}])
        self.assertEqual(s["n"], 3)
        self.assertEqual(s["wins"], 2)
        self.assertEqual(s["ties"], 1)
        self.assertEqual(s["win_rate"], 0.67)
        self.assertEqual(s["mean_delta"], 1.0)


if __name__ == "__main__":
    unittest.main()
