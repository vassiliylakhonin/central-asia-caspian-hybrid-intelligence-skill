"""Provider-independent receipts for specialist-lift protocol 2.

Hashes detect drift relative to saved receipts, not authorship or factual truth.
Commit preparation before generation and judge receipts before scoring.
"""
import hashlib
import json
import re
from pathlib import Path

PROTOCOL = "specialist-lift@2"
CONDITIONS = "ABC"
REFERENCES = ("SKILL.md", "docs/regional-logic.md", "docs/risk-archetypes.md",
              "docs/source-guide.md", "docs/currency-watch.md", "docs/analysis-contract.md")
SCOPE = ("Small N. Not a labelled dataset. Measures substantive coverage against a "
         "model-drafted rubric derived from repository references; author review remains "
         "required. Not factual accuracy, compliance validation, or practitioner validation. "
         "A null result alone does not establish equivalence or justify retirement.")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def slug(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]*", value):
        raise ValueError(f"invalid identifier: {value!r}")
    return value


def item_ids(text: str) -> list[str]:
    ids = re.findall(r"^###\s+(S\d+)\b", text, re.M)
    if len(ids) < 8 or len(set(ids)) != len(ids) or "REPLACE-ME" in text:
        raise ValueError("rubric needs at least eight unique items and no REPLACE-ME placeholders")
    return ids


def families(manifest: dict) -> None:
    generator = manifest.get("model_family", "").strip().lower()
    judge = manifest.get("judge_family", "").strip().lower()
    if not generator or not judge or generator == judge or manifest["model"] == manifest["judge_model"]:
        raise ValueError("judge must be from a different vendor family, declared explicitly")
    for field, family in (("model", generator), ("judge_model", judge)):
        model = manifest[field].lower()
        expected = next((vendor for prefix, vendor in (("claude", "anthropic"),
                        ("gpt", "openai"), ("gemini", "google")) if model.startswith(prefix)), None)
        if expected and expected != family:
            raise ValueError(f"{field} identifier conflicts with declared vendor family")


def checked_path(run: Path, relative: str) -> Path:
    path = (run / relative).resolve()
    if not path.is_relative_to(run.resolve()) or not path.is_file():
        raise ValueError(f"missing or unsafe receipt file: {relative}")
    return path


def check_prepared(run: Path) -> dict:
    manifest = load(run / "manifest.json")
    if manifest.get("protocol") != PROTOCOL:
        raise ValueError("legacy preparation cannot be scored; prepare a new protocol-2 run")
    families(manifest)
    entries = manifest["cases"]
    ids = [slug(entry["case_id"]) for entry in entries]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("prepared cases must be non-empty and unique")
    for path, expected in manifest["input_sha256"].items():
        if digest(checked_path(run, path)) != expected:
            raise ValueError(f"prepared input changed: {path}")
    rubric = checked_path(run, "inputs/rubric.md")
    if item_ids(rubric.read_text()) != manifest["rubric_items"]:
        raise ValueError("rubric items do not match frozen input")
    if digest(rubric) != manifest["rubric_sha256"]:
        raise ValueError("rubric hash mismatch")
    for entry in entries:
        if set(entry["prompt_sha256"]) != set(CONDITIONS):
            raise ValueError("each case requires three pinned prompts")
        for condition, expected in entry["prompt_sha256"].items():
            path = checked_path(run, f"prompts/{entry['case_id']}__condition_{condition}.txt")
            if digest(path) != expected:
                raise ValueError(f"prompt changed: {path.name}")
    return manifest


def build_report(run: Path) -> dict:
    manifest = check_prepared(run)
    scores = load(run / "scores.json")
    prepared = {entry["case_id"] for entry in manifest["cases"]}
    if set(scores.get("cases", {})) != prepared:
        raise ValueError("every prepared case must have scores, with no extra cases")
    receipts = load(run / "judge-receipt.json")
    if receipts["manifest_sha256"] != digest(run / "manifest.json"):
        raise ValueError("preparation changed after judge export")
    mapping = load(run / "blinding-key.json")
    expected_outputs = {f"outputs/{case}__condition_{condition}.md" for case in prepared for condition in CONDITIONS}
    if set(receipts["output_sha256"]) != expected_outputs:
        raise ValueError("output receipts do not cover every case and condition")
    for path, expected in receipts["output_sha256"].items():
        output = checked_path(run, path)
        if not output.read_text().strip() or digest(output) != expected:
            raise ValueError(f"output missing, empty or changed after judging: {path}")
    if receipts["blinding_sha256"] != digest(run / "blinding-key.json"):
        raise ValueError("blinding key changed after judge export")
    rows = []
    for entry in manifest["cases"]:
        case = entry["case_id"]
        blind = mapping[case]
        if set(blind) != {"output_1", "output_2", "output_3"} or set(blind.values()) != set(CONDITIONS):
            raise ValueError("invalid blinding key")
        judged = scores["cases"][case]
        if set(judged) != set(blind):
            raise ValueError(f"{case}: scores must use anonymous output identifiers")
        row = {"case_id": case, "archetype": entry["archetype"], "negative_control": entry["negative_control"]}
        applicability = []
        for anonymous, condition in blind.items():
            items = judged[anonymous]
            if not isinstance(items, dict) or set(items) != set(manifest["rubric_items"]):
                raise ValueError(f"{case}: score every rubric item; numeric totals are not accepted")
            output = (run / f"outputs/{case}__condition_{condition}.md").read_text()
            for item in items.values():
                if not isinstance(item, dict) or type(item.get("satisfied")) not in (bool, type(None)):
                    raise ValueError("item satisfied must be true, false, or null (not applicable)")
                if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
                    raise ValueError("every item requires a rationale, including not-applicable items")
                if item["satisfied"] is True:
                    quote = item.get("evidence", "")
                    if not isinstance(quote, str) or not quote.strip() or quote not in output:
                        raise ValueError("satisfied item requires a verbatim span from that output")
            applicable = {key for key, item in items.items() if item["satisfied"] is not None}
            applicability.append(applicable)
            row[condition] = sum(item["satisfied"] is True for item in items.values())
        if not applicability[0] or any(items != applicability[0] for items in applicability[1:]):
            raise ValueError("applicable items must be non-empty and identical across the three conditions")
        row["denominator"] = len(applicability[0])
        row["lift_c_over_b"] = row["C"] - row["B"]
        row["normalized_lift_c_over_b"] = row["lift_c_over_b"] / row["denominator"]
        row["discrimination_b_over_a"] = row["B"] - row["A"]
        rows.append(row)
    measured = [row for row in rows if not row["negative_control"]]
    controls = [row for row in rows if row["negative_control"]]
    return {"protocol": PROTOCOL, "run_id": manifest["run_id"], "model": manifest["model"],
            "judge_model": manifest["judge_model"], "rubric_sha256": manifest["rubric_sha256"],
            "manifest_sha256": digest(run / "manifest.json"), "scores_sha256": digest(run / "scores.json"),
            "judge_receipt_sha256": digest(run / "judge-receipt.json"), "cases": rows,
            "mean_lift_c_over_b": sum(row["lift_c_over_b"] for row in measured) / len(measured) if measured else 0,
            "mean_normalized_lift_c_over_b": sum(row["normalized_lift_c_over_b"] for row in measured) / len(measured) if measured else 0,
            "null_or_negative_cases": sum(row["lift_c_over_b"] <= 0 for row in measured),
            "negative_controls_holding": sum(row["lift_c_over_b"] <= 0 for row in controls), "scope": SCOPE}
