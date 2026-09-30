"""The Bar 3 harness enforces honesty rules; prove it refuses rather than warns.

Every rule here is an anti-criterion in docs/definition-of-done.md, and every one
describes something an author does to themselves under mild pressure rather than
something an attacker does. A rule of that kind is worth nothing as prose.

The tests build a throwaway repository in a temp directory and run the harness
against that. An earlier version mutated the real suite and restored it
afterwards, which broke the moment real cases were added — and, worse, meant a
passing test depended on the suite being empty.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REAL_ROOT = Path(__file__).resolve().parents[1]
REAL_TOOLS = REAL_ROOT / "evals" / "specialist-lift" / "tools"

ARCHETYPES_STUB = """# Archetypes

## 1. Payment-rail exposure

- **Mechanism**: stub.

## 2. Beneficial ownership opacity

- **Mechanism**: stub.

## 3. Caspian corridor disruption

- **Mechanism**: stub.
"""

RUBRIC_STUB = "# rubric\n\n" + "".join(
    f"### S{n} — item\n\n- **Question:** q\n- **Satisfied when:** w\n\n" for n in range(1, 9)
)


class HarnessTestCase(unittest.TestCase):
    """A minimal repository containing only what the harness reads."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)

        (self.tmp / "docs").mkdir()
        (self.tmp / "docs" / "risk-archetypes.md").write_text(ARCHETYPES_STUB, encoding="utf-8")
        for name in ("regional-logic", "source-guide", "currency-watch", "analysis-contract"):
            (self.tmp / "docs" / f"{name}.md").write_text(f"# {name} reference stub\n")
        (self.tmp / "SKILL.md").write_text("# vertical method stub\n", encoding="utf-8")
        self.horizontal = self.tmp / "horizontal.md"
        self.horizontal.write_text("# horizontal method stub\n", encoding="utf-8")

        self.suite = self.tmp / "evals" / "specialist-lift"
        (self.suite / "cases").mkdir(parents=True)
        (self.suite / "runs").mkdir()
        shutil.copytree(REAL_TOOLS, self.suite / "tools")

        self.rubric = self.suite / "rubric.md"
        self.rubric.write_text(RUBRIC_STUB, encoding="utf-8")

        self.harness = self.suite / "tools" / "lift_eval.py"
        self.validator = self.suite / "tools" / "validate_lift.py"
        self.run_dir = self.suite / "runs" / "r1"

    def add_case(self, case_id: str, *, negative_control: bool = False, archetype: str | None = None):
        if archetype is None:
            archetype = "none" if negative_control else "Payment-rail exposure"
        (self.suite / "cases" / f"{case_id}.json").write_text(
            json.dumps(
                {
                    "id": case_id,
                    "question": f"question for {case_id}",
                    "decision_context": "context",
                    "archetype": archetype,
                    "negative_control": negative_control,
                }
            ),
            encoding="utf-8",
        )

    def run_tool(self, tool: Path, *arguments: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(tool), *arguments], cwd=self.tmp, capture_output=True, text=True
        )

    def prepare(self, **overrides) -> subprocess.CompletedProcess:
        options = {"model": "model-x", "judge-model": "model-y"}
        options.update(overrides)
        return self.run_tool(
            self.harness, "prepare", "r1",
            "--model", options["model"],
            "--judge-model", options["judge-model"],
            "--model-family", overrides.get("model-family", "openai"),
            "--judge-family", overrides.get("judge-family", "anthropic"),
            "--horizontal-skill", str(self.horizontal),
            "--force",
        )

    def write_scores(self, cases: dict) -> None:
        manifest = json.loads((self.run_dir / "manifest.json").read_text())
        mapping = json.loads((self.run_dir / "blinding-key.json").read_text())
        (self.run_dir / "outputs").mkdir(exist_ok=True)
        for entry in manifest["cases"]:
            for condition in "ABC":
                (self.run_dir / "outputs" / f"{entry['case_id']}__condition_{condition}.md").write_text("verbatim evidence\n")
        self.assertEqual(self.run_tool(self.harness, "judge", "r1").returncode, 0)
        judged = {case: {anonymous: {f"S{i}": {
            "satisfied": i <= scores[condition], "rationale": "criterion justification",
            "evidence": "verbatim evidence" if i <= scores[condition] else ""
        } for i in range(1, 9)} for anonymous, condition in mapping[case].items()} for case, scores in cases.items()}
        (self.run_dir / "scores.json").write_text(json.dumps({"cases": judged}), encoding="utf-8")


class PrepareTests(HarnessTestCase):
    def test_conditions_differ_only_by_the_method_files_they_carry(self):
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)

        prompts = self.run_dir / "prompts"
        a, b, c = (
            (prompts / f"case-1__condition_{condition}.txt").read_text() for condition in "ABC"
        )
        self.assertNotIn("horizontal method stub", a)
        self.assertIn("horizontal method stub", b)
        self.assertNotIn("vertical method stub", b)
        self.assertIn("horizontal method stub", c)
        self.assertIn("vertical method stub", c)
        # The question text is identical across all three.
        for prompt in (a, b, c):
            self.assertIn("question for case-1", prompt)

    def test_prepare_is_refused_against_a_placeholder_rubric(self):
        """Bar 3 must not be claimable on a rubric that measures nothing."""
        self.add_case("case-1")
        self.rubric.write_text("### S1 — REPLACE-ME\n", encoding="utf-8")
        result = self.prepare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("REPLACE-ME", result.stderr)

    def test_blinding_key_covers_every_condition(self):
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)
        manifest = json.loads((self.run_dir / "manifest.json").read_text())
        self.assertEqual(set(json.loads((self.run_dir / "blinding-key.json").read_text())["case-1"].values()), {"A", "B", "C"})


class RefusalTests(HarnessTestCase):
    def test_scoring_is_refused_when_the_rubric_changed_after_preparation(self):
        """B3.1 — editing the rubric after reading outputs is the easiest way to manufacture lift."""
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)
        self.write_scores({"case-1": {"A": 1, "B": 3, "C": 6}})
        self.rubric.write_text(RUBRIC_STUB + "\n### S9 — added after the fact\n", encoding="utf-8")

        result = self.run_tool(self.harness, "score", "r1")
        self.assertNotEqual(result.returncode, 0, "a changed rubric must be refused")
        self.assertIn("rubric changed", result.stderr)

    def test_scoring_is_refused_when_a_prepared_case_has_no_score(self):
        """B3.5 — publishing only the cases that came out well is undetectable from outside."""
        self.add_case("case-1")
        self.add_case("case-2")
        self.assertEqual(self.prepare().returncode, 0)
        self.write_scores({"case-1": {"A": 1, "B": 3, "C": 6}})

        result = self.run_tool(self.harness, "score", "r1")
        self.assertNotEqual(result.returncode, 0, "an omitted case must be refused")
        self.assertIn("every prepared case", result.stderr)

    def test_report_records_a_null_result_rather_than_hiding_it(self):
        self.add_case("case-1")
        self.add_case("control", negative_control=True)
        self.assertEqual(self.prepare().returncode, 0)
        self.write_scores(
            {
                "case-1": {"A": 1, "B": 5, "C": 5},   # the vertical adds nothing
                "control": {"A": 1, "B": 4, "C": 4},
            }
        )
        result = self.run_tool(self.harness, "score", "r1")
        self.assertEqual(result.returncode, 0, result.stderr)

        report = json.loads((self.run_dir / "report.json").read_text())
        self.assertEqual(report["mean_lift_c_over_b"], 0)
        self.assertEqual(report["null_or_negative_cases"], 1)
        self.assertEqual(report["negative_controls_holding"], 1)
        self.assertIn("Not a labelled dataset", report["scope"])


class ValidatorTests(HarnessTestCase):
    def _cases_for_a_complete_suite(self):
        self.add_case("case-1", archetype="Payment-rail exposure")
        self.add_case("case-2", archetype="Beneficial ownership opacity")
        self.add_case("case-3", archetype="Payment-rail exposure")
        self.add_case("case-4", archetype="Beneficial ownership opacity")
        self.add_case("case-5", archetype="Caspian corridor disruption")
        self.add_case("control", negative_control=True)

    def test_rejects_a_same_family_judge(self):
        """B3.4 — a model scoring its own family is not a blind judge."""
        self._cases_for_a_complete_suite()
        result = self.prepare(**{"judge-model": "model-y", "judge-family": "openai"})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("different vendor family", result.stderr)

    def test_requires_a_negative_control(self):
        """B3.6 — without it, added signal is indistinguishable from added words."""
        self._cases_for_a_complete_suite()
        (self.suite / "cases" / "control.json").unlink()
        result = self.run_tool(self.validator)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("negative control", result.stderr)

    def test_rejects_an_archetype_that_is_not_documented(self):
        self._cases_for_a_complete_suite()
        self.add_case("case-6", archetype="Invented archetype")
        result = self.run_tool(self.validator)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invented archetype", result.stderr)

    def test_only_a_negative_control_may_declare_no_archetype(self):
        self._cases_for_a_complete_suite()
        self.add_case("case-7", negative_control=False, archetype="none")
        result = self.run_tool(self.validator)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("only a negative control", result.stderr)

    def test_accepts_a_complete_suite(self):
        self._cases_for_a_complete_suite()
        result = self.run_tool(self.validator)
        self.assertEqual(result.returncode, 0, result.stderr)


class ReceiptTests(HarnessTestCase):
    def complete_run(self):
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)
        self.write_scores({"case-1": {"A": 1, "B": 3, "C": 5}})

    def test_refuses_scores_without_outputs(self):
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)
        (self.run_dir / "scores.json").write_text(json.dumps({"cases": {"case-1": {"A": 0, "B": 0, "C": 999}}}))
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_numeric_totals_including_999(self):
        self.complete_run()
        mapping = json.loads((self.run_dir / "blinding-key.json").read_text())
        (self.run_dir / "scores.json").write_text(json.dumps({"cases": {"case-1": {key: 999 for key in mapping["case-1"]}}}))
        result = self.run_tool(self.harness, "score", "r1")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("numeric totals", result.stderr)

    def test_refuses_changed_output_after_judge_export(self):
        self.complete_run()
        (self.run_dir / "outputs/case-1__condition_C.md").write_text("edited after judging")
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_changed_prompt(self):
        self.complete_run()
        (self.run_dir / "prompts/case-1__condition_C.txt").write_text("different question")
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_changed_reference(self):
        self.complete_run()
        (self.run_dir / "inputs/vertical/docs/risk-archetypes.md").write_text("edited reference")
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_loads_regional_references_in_C_only(self):
        self.add_case("case-1")
        self.assertEqual(self.prepare().returncode, 0)
        c = (self.run_dir / "prompts/case-1__condition_C.txt").read_text()
        b = (self.run_dir / "prompts/case-1__condition_B.txt").read_text()
        self.assertIn("regional-logic reference stub", c)
        self.assertIn("Payment-rail exposure", c)
        self.assertNotIn("regional-logic reference stub", b)

    def test_judge_packet_does_not_include_identity_or_mapping(self):
        self.complete_run()
        packet = json.loads((self.run_dir / "judge/case-1.json").read_text())
        self.assertEqual(set(packet["outputs"]), {"output_1", "output_2", "output_3"})
        self.assertNotIn("model", packet)
        self.assertNotIn("blinding_key", packet)

    def test_refuses_non_boolean_item_score(self):
        self.complete_run()
        path = self.run_dir / "scores.json"
        data = json.loads(path.read_text())
        data["cases"]["case-1"]["output_1"]["S1"]["satisfied"] = 999
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_untraceable_positive_item(self):
        self.complete_run()
        path = self.run_dir / "scores.json"
        data = json.loads(path.read_text())
        data["cases"]["case-1"]["output_1"]["S1"].update(satisfied=True, evidence="invented quote")
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_inconsistent_applicability(self):
        self.complete_run()
        path = self.run_dir / "scores.json"
        data = json.loads(path.read_text())
        data["cases"]["case-1"]["output_1"]["S8"]["satisfied"] = None
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)

    def test_refuses_overwriting_executed_run(self):
        self.complete_run()
        self.assertNotEqual(self.prepare().returncode, 0)

    def test_refuses_run_path_traversal(self):
        self.assertNotEqual(self.run_tool(self.harness, "score", "../outside").returncode, 0)

    def test_refuses_two_different_claude_ids(self):
        self.add_case("case-1")
        result = self.prepare(model="claude-a", **{"model-family": "anthropic", "judge-model": "claude-b", "judge-family": "anthropic"})
        self.assertNotEqual(result.returncode, 0)

    def test_refuses_misdeclared_known_family(self):
        self.add_case("case-1")
        self.assertNotEqual(self.prepare(model="claude-a").returncode, 0)

    def test_validator_recomputes_report(self):
        self.complete_run()
        self.assertEqual(self.run_tool(self.harness, "score", "r1").returncode, 0)
        path = self.run_dir / "report.json"
        report = json.loads(path.read_text())
        report["cases"][0]["C"] = 999
        path.write_text(json.dumps(report))
        result = self.run_tool(self.validator)
        self.assertIn("differs from recomputed", result.stderr)


if __name__ == "__main__":
    unittest.main()
