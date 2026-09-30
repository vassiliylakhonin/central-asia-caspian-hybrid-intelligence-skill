"""Check active routing and evidence-mode rules, without claiming factual checks."""
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def errors(root: Path) -> list[str]:
    problems = []
    skill = (root / "SKILL.md").read_text()
    for reference in ("regional-logic", "risk-archetypes", "source-guide", "analysis-contract"):
        if f"docs/{reference}.md" not in skill:
            problems.append(f"SKILL.md must load docs/{reference}.md")
    for relative in ("SKILL.md", "docs/source-guide.md", "docs/currency-watch.md"):
        text = (root / relative).read_text()
        if re.search(r"(?:prioritize|where to verify|sanctions:|^-).*OFSI consolidated list", text, re.I | re.M):
            problems.append(f"{relative}: current routing must use UK Sanctions List")
        if re.search(r"downgrade[^\n]*`mixed`", text, re.I):
            problems.append(f"{relative}: mixed is not a memo evidence mode")
    interview = (root / "docs/cold-start-interview.md").read_text()
    if "DEPRECATED" in interview:
        problems.append("cold-start interview is still required by the root contract")
    watch = (root / "docs/currency-watch.md").read_text()
    match = re.search(r"\*\*Topic catalogue reviewed:\*\* (\d{4}-\d{2}-\d{2})", watch)
    if not match:
        problems.append("currency watch must distinguish catalogue review from factual verification")
    else:
        try:
            reviewed = date.fromisoformat(match[1])
            if reviewed > date.today():
                problems.append("catalogue review date cannot be in the future")
        except ValueError:
            problems.append("invalid catalogue review date")
    if "**Primary-source status:**" not in watch:
        problems.append("currency watch must disclose primary-source verification status")
    return problems


def main() -> int:
    problems = errors(ROOT)
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if problems:
        return 1
    watch = (ROOT / "docs/currency-watch.md").read_text()
    reviewed = date.fromisoformat(re.search(r"Topic catalogue reviewed:\*\* (\S+)", watch)[1])
    if (date.today() - reviewed).days > 90:
        print("warning: topic catalogue review exceeds 90 days; re-check relevant sources")
    print("ok: runtime documentation contract; topic claims are not factually verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
