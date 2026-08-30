"""The Bar 3 harness enforces two honesty rules; prove it actually does.

Both rules are anti-criteria in docs/definition-of-done.md, and both describe
things an author does to themselves under mild pressure rather than things an
attacker does. A rule of that kind is worth nothing as prose. These tests check
that the harness refuses, not that it warns.
"""

import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "evals" / "specialist-lift"
HARNESS = SUITE / "tools" / "lift_eval.py"
VALIDATOR = SUITE / "tools" / "validate_lift.py"


def run(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *arguments], cwd=ROOT, capture_output=True, text=True
    )


class LiftHarnessTests(unittest.TestCase):
    """Exercise the harness against a throwaway suite, not the real one."""

    def setUp(self):
        self.cases = SUITE / "cases"
        self.runs = SUITE / "runs"
        self.rubric = SUITE / "rubric.md"
        self.rubric_backup = self.rubric.read_text(encoding="utf-8")
        self.created = []

        # A rubric with no placeholders, so `prepare` will proceed.
        self.rubric.write_text(
            "# rubric\n\n"
            + "".join(
                f"### S{n} — item\n\n- **Question:** q\n- **Satisfied when:** w\n\n"
                for n in range(1, 9)
            ),
            encoding="utf-8",
        )
        for index, negative in ((1, False), (2, True)):
            path = self.cases / f"zz-harness-test-{index}.json"
            path.write_text(
                json.dumps(
                    {
                        "id": f"zz-harness-test-{index}",
                        "question": f"question {index}",
                        "decision_context": "context",
                        "archetype": "Payment-rail exposure",
                        "negative_control": negative,
                    }
                ),
                encoding="utf-8",
            )
            self.created.append(path)
        self.run_dir = self.runs / "zz-harness-test"

    def tearDown(self):
        self.rubric.write_text(self.rubric_backup, encoding="utf-8")
        for path in self.created:
            path.unlink(missing_ok=True)
        shutil.rmtree(self.run_dir, ignore_errors=True)

    def _prepare(self) -> subprocess.CompletedProcess:
        return run(
            str(HARNESS), "prepare", "zz-harness-test",
            "--model", "model-x",
            "--judge-model", "model-y",
            "--horizontal-skill", str(ROOT / "SKILL.md"),
            "--force",
        )

    def _write_scores(self, cases: dict) -> None:
        (self.run_dir / "scores.json").write_text(
            json.dumps({"cases": cases}), encoding="utf-8"
        )

    def test_prepare_writes_three_conditions_and_a_blinding_key(self):
        result = self._prepare()
        self.assertEqual(result.returncode, 0, result.stderr)
        for index in (1, 2):
            for condition in ("A", "B", "C"):
                prompt = self.run_dir / "prompts" / f"zz-harness-test-{index}__condition_{condition}.txt"
                self.assertTrue(prompt.exists(), f"missing {prompt.name}")

        manifest = json.loads((self.run_dir / "manifest.json").read_text())
        # Condition C must carry both methods, B only the horizontal one.
        b = (self.run_dir / "prompts" / "zz-harness-test-1__condition_B.txt").read_text()
        c = (self.run_dir / "prompts" / "zz-harness-test-1__condition_C.txt").read_text()
        a = (self.run_dir / "prompts" / "zz-harness-test-1__condition_A.txt").read_text()
        self.assertLess(len(a), len(b))
        self.assertLess(len(b), len(c))
        self.assertEqual(set(manifest["blinding_key"]["zz-harness-test-1"].values()), {"A", "B", "C"})

    def test_scoring_is_refused_when_the_rubric_changed_after_preparation(self):
        """B3.1 — editing the rubric after reading outputs is the easiest way to manufacture lift."""
        self.assertEqual(self._prepare().returncode, 0)
        self._write_scores(
            {
                "zz-harness-test-1": {"A": 1, "B": 3, "C": 6},
                "zz-harness-test-2": {"A": 1, "B": 4, "C": 4},
            }
        )
        self.rubric.write_text(self.rubric.read_text() + "\n### S9 — added later\n", encoding="utf-8")

        result = run(str(HARNESS), "score", "zz-harness-test")
        self.assertNotEqual(result.returncode, 0, "scoring should refuse a changed rubric")
        self.assertIn("rubric changed", result.stderr)

    def test_scoring_is_refused_when_a_prepared_case_has_no_score(self):
        """B3.5 — publishing only the cases that came out well is undetectable from outside."""
        self.assertEqual(self._prepare().returncode, 0)
        self._write_scores({"zz-harness-test-1": {"A": 1, "B": 3, "C": 6}})

        result = run(str(HARNESS), "score", "zz-harness-test")
        self.assertNotEqual(result.returncode, 0, "scoring should refuse an omitted case")
        self.assertIn("zz-harness-test-2", result.stderr)

    def test_report_records_null_lift_rather_than_hiding_it(self):
        self.assertEqual(self._prepare().returncode, 0)
        self._write_scores(
            {
                # A null result on the measured case: C adds nothing over B.
                "zz-harness-test-1": {"A": 1, "B": 5, "C": 5},
                "zz-harness-test-2": {"A": 1, "B": 4, "C": 4},
            }
        )
        result = run(str(HARNESS), "score", "zz-harness-test")
        self.assertEqual(result.returncode, 0, result.stderr)

        report = json.loads((self.run_dir / "report.json").read_text())
        self.assertEqual(report["mean_lift_c_over_b"], 0)
        self.assertEqual(report["null_or_negative_cases"], 1)
        self.assertEqual(report["negative_controls_holding"], 1)
        self.assertIn("Not a labelled dataset", report["scope"])

    def test_validator_rejects_a_same_family_judge(self):
        """B3.4 — a model scoring its own family is not a blind judge."""
        self.assertEqual(self._prepare().returncode, 0)
        manifest_path = self.run_dir / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["judge_model"] = manifest["model"]
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        result = run(str(VALIDATOR))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("different vendor family", result.stderr)

    def test_validator_requires_a_negative_control_once_the_rubric_is_real(self):
        """B3.6 — without it, added signal is indistinguishable from added words."""
        for path in self.created:
            if path.name.endswith("2.json"):
                path.unlink()
        result = run(str(VALIDATOR))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("negative control", result.stderr)


if __name__ == "__main__":
    unittest.main()
