#!/usr/bin/env python3
"""Structural checks for the Bar 3 specialist-lift suite.

Runs on every commit. It does not require the suite to be complete — Bar 3 is
recorded as not attempted, and an empty suite is an honest state. It requires
that whatever *is* there is internally consistent, so the suite cannot drift
into looking finished while measuring nothing.

The checks map to criteria in docs/definition-of-done.md and are deliberately
mechanical: each one blocks a specific way Bar 3 could be claimed without being
earned.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUITE = HERE.parent
ROOT = SUITE.parents[1]
CASES_DIR = SUITE / "cases"
RUNS_DIR = SUITE / "runs"
RUBRIC = SUITE / "rubric.md"
ARCHETYPES = ROOT / "docs" / "risk-archetypes.md"

REQUIRED_CASE_FIELDS = ("id", "question", "decision_context", "archetype")
MINIMUM_RUBRIC_ITEMS = 8
MINIMUM_CASES = 5
MINIMUM_ARCHETYPES = 3

errors: list[str] = []
notes: list[str] = []


def known_archetypes() -> set[str]:
    text = ARCHETYPES.read_text(encoding="utf-8")
    return {match.group(1).strip() for match in re.finditer(r"^##\s+\d+\.\s+(.+?)\s*$", text, re.M)}


def check_rubric(rubric_ready: bool) -> None:
    if not RUBRIC.exists():
        errors.append(f"{RUBRIC.relative_to(ROOT)} is missing")
        return
    text = RUBRIC.read_text(encoding="utf-8")
    items = re.findall(r"^###\s+S\d", text, re.M)
    if rubric_ready and len(items) < MINIMUM_RUBRIC_ITEMS:
        errors.append(
            f"B3.1: rubric has {len(items)} items, needs at least {MINIMUM_RUBRIC_ITEMS}"
        )
    if not rubric_ready:
        notes.append("rubric is still a template (B3.1 not met) — expected while Bar 3 is unattempted")


def check_cases(archetypes: set[str], suite_ready: bool) -> list[dict]:
    cases = []
    for path in sorted(CASES_DIR.glob("*.json")):
        try:
            case = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        missing = [field for field in REQUIRED_CASE_FIELDS if not case.get(field)]
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
            continue
        # A negative control is a case where no regional archetype should apply.
        # Forcing one on it would defeat its purpose, so "none" is allowed there
        # and only there.
        if case.get("negative_control") and case["archetype"] == "none":
            pass
        elif case["archetype"] not in archetypes:
            errors.append(
                f"{path.relative_to(ROOT)}: archetype {case['archetype']!r} is not one of the "
                f"archetypes in docs/risk-archetypes.md"
                + (" (only a negative control may use \"none\")" if case["archetype"] == "none" else "")
            )
        cases.append(case)

    ids = [case["id"] for case in cases]
    duplicates = {case_id for case_id in ids if ids.count(case_id) > 1}
    if duplicates:
        errors.append(f"duplicate case ids: {', '.join(sorted(duplicates))}")

    if suite_ready:
        if len(cases) < MINIMUM_CASES:
            errors.append(f"B3.3: {len(cases)} cases, needs at least {MINIMUM_CASES}")
        covered = {case["archetype"] for case in cases if case["archetype"] != "none"}
        if len(covered) < MINIMUM_ARCHETYPES:
            errors.append(
                f"B3.3: cases span {len(covered)} archetypes, needs at least {MINIMUM_ARCHETYPES}"
            )
        if not any(case.get("negative_control") for case in cases):
            errors.append(
                "B3.6: no negative control. Without a case where the region should not "
                "change the substance, the measurement cannot tell added signal from added words."
            )
    elif cases:
        notes.append(f"{len(cases)} case(s) defined; suite not yet complete")
    return cases


def check_runs() -> None:
    """A published run must be internally honest, whatever it found."""
    for run_dir in sorted(path for path in RUNS_DIR.glob("*") if path.is_dir()):
        manifest_path = run_dir / "manifest.json"
        if not manifest_path.exists():
            errors.append(f"{run_dir.relative_to(ROOT)}: no manifest.json")
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        if manifest.get("model") and manifest.get("judge_model") == manifest.get("model"):
            errors.append(
                f"{run_dir.relative_to(ROOT)}: B3.4 requires a judge from a different vendor "
                f"family than the generating model; both are {manifest['model']!r}"
            )

        report_path = run_dir / "report.json"
        if not report_path.exists():
            notes.append(f"{run_dir.relative_to(ROOT)}: prepared, not yet scored")
            continue
        report = json.loads(report_path.read_text(encoding="utf-8"))

        prepared = {entry["case_id"] for entry in manifest["cases"]}
        reported = {row["case_id"] for row in report["cases"]}
        if prepared != reported:
            errors.append(
                f"{run_dir.relative_to(ROOT)}: B3.5 — report omits "
                f"{', '.join(sorted(prepared - reported)) or 'nothing'} and adds "
                f"{', '.join(sorted(reported - prepared)) or 'nothing'}. Every prepared case "
                "must be published, including null and negative results."
            )
        if report.get("rubric_sha256") != manifest.get("rubric_sha256"):
            errors.append(
                f"{run_dir.relative_to(ROOT)}: report was scored against a different rubric "
                "than the run was prepared with (B3.1)"
            )
        if not report.get("scope"):
            errors.append(f"{run_dir.relative_to(ROOT)}: B3.8 — report carries no scope statement")


def main() -> int:
    if not ARCHETYPES.exists():
        print(f"ERROR: {ARCHETYPES.relative_to(ROOT)} is missing", file=sys.stderr)
        return 1

    rubric_ready = RUBRIC.exists() and "REPLACE-ME" not in RUBRIC.read_text(encoding="utf-8")
    # The suite is only held to the full Bar 3 shape once the rubric is real.
    # Before that, Bar 3 is unattempted and an incomplete suite is accurate.
    check_rubric(rubric_ready)
    check_cases(known_archetypes(), suite_ready=rubric_ready)
    check_runs()

    for note in notes:
        print(f"note: {note}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("ok: specialist-lift suite is internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
