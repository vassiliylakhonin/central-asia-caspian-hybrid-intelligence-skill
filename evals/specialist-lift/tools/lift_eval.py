#!/usr/bin/env python3
"""Bar 3 harness: measure whether this vertical changes the substance of an answer.

Three conditions per case:

    A  no skill loaded
    B  the horizontal method only (global-think-tank-analyst)
    C  the horizontal method plus this vertical

B is the comparison that matters. A exists only to show the rubric can
discriminate at all — if A scores near B, the rubric is measuring something
every model already does.

The harness deliberately does not call a model. It has no provider dependency
and runs in CI. `prepare` writes the exact prompt bundles and a manifest;
whatever runs them is the operator's choice. `score` ingests judge scores and
produces the report.

Two honesty rules from docs/definition-of-done.md are enforced mechanically
rather than trusted:

  B3.1  The rubric is hashed at prepare time. Scoring a run whose rubric has
        changed is refused. Editing the rubric after reading outputs is the
        easiest way to manufacture lift, so it is made impossible rather than
        discouraged.

  B3.5  Every prepared case must be scored. A case that is prepared and then
        missing from the scores is refused, with its id named. Publishing only
        the cases that came out well is the other easy way, and it is the one a
        reader cannot detect from the outside.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUITE = HERE.parent
ROOT = SUITE.parents[1]
CASES_DIR = SUITE / "cases"
RUNS_DIR = SUITE / "runs"
RUBRIC = SUITE / "rubric.md"
SKILL = ROOT / "SKILL.md"

CONDITIONS = ("A", "B", "C")
CONDITION_LABELS = {
    "A": "no skill loaded",
    "B": "horizontal method only",
    "C": "horizontal method plus this vertical",
}


def die(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_cases() -> list[dict]:
    paths = sorted(CASES_DIR.glob("*.json"))
    if not paths:
        die(f"no cases in {CASES_DIR.relative_to(ROOT)}")
    cases = []
    for path in paths:
        try:
            case = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            die(f"{path.relative_to(ROOT)}: {exc}")
        case["_path"] = str(path.relative_to(ROOT))
        cases.append(case)
    return cases


def build_prompt(case: dict, condition: str, horizontal: str, vertical: str) -> str:
    """Assemble the exact text sent under one condition.

    Conditions differ only by which method files precede the question. Nothing
    else varies, so a difference in output is attributable to the method rather
    than to phrasing.
    """
    parts: list[str] = []
    if condition in ("B", "C"):
        parts.append(horizontal)
    if condition == "C":
        parts.append(vertical)
    parts.append(f"# Question\n\n{case['question']}\n\n# Decision context\n\n{case['decision_context']}")
    return "\n\n---\n\n".join(parts)


def cmd_prepare(args: argparse.Namespace) -> int:
    if not RUBRIC.exists():
        die(f"{RUBRIC.relative_to(ROOT)} is missing; the rubric is pre-registered, not optional")
    rubric_text = RUBRIC.read_text(encoding="utf-8")
    if "REPLACE-ME" in rubric_text:
        die(
            f"{RUBRIC.relative_to(ROOT)} still contains REPLACE-ME placeholders. "
            "A run against a placeholder rubric measures nothing. Write the items first."
        )

    horizontal_path = Path(args.horizontal_skill)
    if not horizontal_path.exists():
        die(
            f"horizontal method not found at {horizontal_path}. Pass --horizontal-skill "
            "pointing at global-think-tank-analyst/SKILL.md."
        )
    horizontal = horizontal_path.read_text(encoding="utf-8")
    vertical = SKILL.read_text(encoding="utf-8")

    cases = load_cases()
    run_dir = RUNS_DIR / args.run_id
    if run_dir.exists() and not args.force:
        die(f"{run_dir.relative_to(ROOT)} already exists; pass --force to overwrite")
    (run_dir / "prompts").mkdir(parents=True, exist_ok=True)

    # The judge sees outputs in randomised order with condition labels stripped.
    # The key is written separately so unblinding is an explicit step.
    rng = random.Random(args.seed)
    blinding: dict[str, dict[str, str]] = {}
    entries = []

    for case in cases:
        case_id = case["id"]
        shuffled = list(CONDITIONS)
        rng.shuffle(shuffled)
        blinding[case_id] = {
            f"output_{index + 1}": condition for index, condition in enumerate(shuffled)
        }
        for condition in CONDITIONS:
            prompt = build_prompt(case, condition, horizontal, vertical)
            target = run_dir / "prompts" / f"{case_id}__condition_{condition}.txt"
            target.write_text(prompt, encoding="utf-8")
        entries.append(
            {
                "case_id": case_id,
                "case_file": case["_path"],
                "archetype": case["archetype"],
                "negative_control": bool(case.get("negative_control", False)),
                "question_sha256": sha256(case["question"]),
            }
        )

    manifest = {
        "run_id": args.run_id,
        "prepared_on": args.date or date.today().isoformat(),
        "model": args.model,
        "judge_model": args.judge_model,
        "seed": args.seed,
        # Hashes pin exactly what was measured. A later diff on any of these
        # invalidates the run rather than silently changing its meaning.
        "rubric_sha256": sha256(rubric_text),
        "vertical_skill_sha256": sha256(vertical),
        "horizontal_skill_sha256": sha256(horizontal),
        "conditions": CONDITION_LABELS,
        "cases": entries,
        "blinding_key": blinding,
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"prepared {len(entries)} cases x 3 conditions in {run_dir.relative_to(ROOT)}")
    print(f"  model       : {args.model}")
    print(f"  judge model : {args.judge_model}")
    print(f"  rubric      : {manifest['rubric_sha256'][:16]}")
    print("\nNext: run each prompt through the model, save outputs as")
    print(f"  {run_dir.relative_to(ROOT)}/outputs/<case_id>__condition_<A|B|C>.md")
    print("then score them blind and write scores.json (see README).")
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    run_dir = RUNS_DIR / args.run_id
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.exists():
        die(f"{manifest_path.relative_to(ROOT)} not found; run `prepare` first")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    current_rubric = sha256(RUBRIC.read_text(encoding="utf-8"))
    if current_rubric != manifest["rubric_sha256"]:
        die(
            "the rubric changed after this run was prepared "
            f"({manifest['rubric_sha256'][:16]} -> {current_rubric[:16]}). "
            "Scoring against a rubric edited after the outputs were read is the "
            "failure mode B3.1 exists to prevent. Re-register the rubric and "
            "re-run every case."
        )

    scores_path = run_dir / "scores.json"
    if not scores_path.exists():
        die(f"{scores_path.relative_to(ROOT)} not found")
    scores = json.loads(scores_path.read_text(encoding="utf-8"))

    prepared = {entry["case_id"] for entry in manifest["cases"]}
    scored = set(scores.get("cases", {}))
    missing = sorted(prepared - scored)
    if missing:
        die(
            "these cases were prepared but have no score: " + ", ".join(missing) + ". "
            "B3.5 requires every prepared case to be published, including null and "
            "negative results. Dropping a case after seeing it is the failure this "
            "check exists for."
        )
    unexpected = sorted(scored - prepared)
    if unexpected:
        die("scores contain cases that were never prepared: " + ", ".join(unexpected))

    rows = []
    for entry in manifest["cases"]:
        case_scores = scores["cases"][entry["case_id"]]
        a, b, c = (case_scores[condition] for condition in CONDITIONS)
        rows.append(
            {
                "case_id": entry["case_id"],
                "archetype": entry["archetype"],
                "negative_control": entry["negative_control"],
                "A": a,
                "B": b,
                "C": c,
                "lift_c_over_b": c - b,
                "discrimination_b_over_a": b - a,
            }
        )

    measured = [row for row in rows if not row["negative_control"]]
    controls = [row for row in rows if row["negative_control"]]
    mean_lift = sum(row["lift_c_over_b"] for row in measured) / len(measured) if measured else 0.0

    report = {
        "run_id": manifest["run_id"],
        "prepared_on": manifest["prepared_on"],
        "model": manifest["model"],
        "judge_model": manifest["judge_model"],
        "rubric_sha256": manifest["rubric_sha256"],
        "cases": rows,
        "mean_lift_c_over_b": round(mean_lift, 3),
        "null_or_negative_cases": sum(1 for row in measured if row["lift_c_over_b"] <= 0),
        "negative_controls_holding": sum(1 for row in controls if row["lift_c_over_b"] <= 0),
        "scope": (
            "Small N. Not a labelled dataset. Measures substantive coverage against an "
            "author-written rubric, not factual accuracy, not compliance or sanctions "
            "validation, and not practitioner validation."
        ),
    }
    (run_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    width = max(len(row["case_id"]) for row in rows)
    print(f"{'case':<{width}}  {'A':>3} {'B':>3} {'C':>3}  {'C-B':>4}  control")
    for row in rows:
        print(
            f"{row['case_id']:<{width}}  {row['A']:>3} {row['B']:>3} {row['C']:>3}  "
            f"{row['lift_c_over_b']:>+4}  {'yes' if row['negative_control'] else ''}"
        )
    print(f"\nmean C-over-B lift on measured cases: {report['mean_lift_c_over_b']:+}")
    print(f"cases with null or negative lift     : {report['null_or_negative_cases']} of {len(measured)}")
    print(f"negative controls holding            : {report['negative_controls_holding']} of {len(controls)}")
    print("\nA null result clears Bar 3. See docs/definition-of-done.md.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    prepare = sub.add_parser("prepare", help="write prompt bundles and a run manifest")
    prepare.add_argument("run_id")
    prepare.add_argument("--model", required=True, help="exact model id used to generate outputs")
    prepare.add_argument(
        "--judge-model",
        required=True,
        help="judge model id; B3.4 requires a different vendor family than --model",
    )
    prepare.add_argument(
        "--horizontal-skill",
        required=True,
        help="path to global-think-tank-analyst/SKILL.md",
    )
    prepare.add_argument("--seed", type=int, default=0, help="blinding shuffle seed")
    prepare.add_argument("--date", help="override the prepared-on date (ISO)")
    prepare.add_argument("--force", action="store_true")
    prepare.set_defaults(func=cmd_prepare)

    score = sub.add_parser("score", help="turn blind judge scores into a report")
    score.add_argument("run_id")
    score.set_defaults(func=cmd_score)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
