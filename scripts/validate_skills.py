#!/usr/bin/env python3
"""Validate repo skill files without external dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "skills/openclaw/SKILL.md",
    ROOT / "skills/codex/SKILL.md",
    ROOT / "skills/claude/SKILL.md",
]

def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)

for path in REQUIRED:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing opening YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path}: missing closing YAML frontmatter")
    frontmatter = text[4:end]
    body = text[end + 4 :]
    if not re.search(r"^name:\s*\S+", frontmatter, re.M):
        fail(f"{path}: missing frontmatter name")
    desc_match = re.search(r"^description:\s*(.+)", frontmatter, re.M | re.S)
    if not desc_match or len(desc_match.group(1).strip()) < 80:
        fail(f"{path}: description is missing or too weak")
    for phrase in [
        "Evidence Discipline",
        "Confidence Footer",
        "Compliance note",
        "Disclaimer",
        "Example Prompt",
    ]:
        if phrase not in body:
            fail(f"{path}: missing required phrase: {phrase}")
    if "guaranteed" in body and "Never say `guaranteed`" not in body:
        fail(f"{path}: unsafe guarantee language")

print("ok: skill files validated")
