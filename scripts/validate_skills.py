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

REQUIRED_ROOT_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "STATUS.md",
]

REQUIRED_SECTIONS = [
    "Core Contract",
    "Use When",
    "Intake",
    "Regional Logic",
    "Mode Selection",
    "Evidence Discipline",
    "Source Handling",
    "Risk / Compliance Mode",
    "Strategic Mode",
    "Hybrid Mode",
    "Confidence Footer",
    "Safety Notes",
    "Installation",
    "Example Prompt",
]

REQUIRED_BODY_PHRASES = [
    "Primary driver is:",
    "Compliance note",
    "Disclaimer",
    "Author: Vassiliy Lakhonin",
    "official sanctions lists",
    "Do not use for formal legal/compliance determinations",
]

FORBIDDEN_CLAIMS = [
    "fully compliant",
    "no sanctions risk",
    "guaranteed compliant",
    "this is a legal determination",
    "constitutes legal advice",
]

README_FORBIDDEN_CLAIMS = [
    "guarantees compliance",
    "guarantees accuracy",
    "detects sanctions evasion",
    "fully autonomous",
    "trusted by",
    "used by",
]

def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def split_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing opening YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path}: missing closing YAML frontmatter")

    frontmatter_text = text[4:end]
    body = text[end + 5 :]
    frontmatter: dict[str, str] = {}

    for line in frontmatter_text.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path}: invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            fail(f"{path}: frontmatter key/value cannot be empty: {line}")
        frontmatter[key] = value

    return frontmatter, body


def section_titles(body: str) -> set[str]:
    return set(re.findall(r"^##\s+(.+?)\s*$", body, re.M))


def validate_root_docs() -> None:
    for path in REQUIRED_ROOT_FILES:
        if not path.exists():
            fail(f"{path}: required root file missing")

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8").lower()

    for claim in README_FORBIDDEN_CLAIMS:
        if claim in readme:
            fail(f"README.md: unsupported claim: {claim}")

    if "no production-usage, adoption or benchmark numbers are claimed" not in readme:
        fail("README.md: must disclose that no production-usage, adoption or benchmark numbers are claimed")

    required_links = [
        "github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill",
        "github.com/vassiliylakhonin/global-think-tank-analyst",
        "github.com/vassiliylakhonin/agenda-intelligence-md",
    ]
    for link in required_links:
        if link not in readme:
            fail(f"README.md: missing companion repo link: {link}")

    if "**bar 2 — not cleared.**" not in status:
        fail("STATUS.md: must explicitly state: **Bar 2 — not cleared.**")


validate_root_docs()

for path in REQUIRED:
    frontmatter, body = split_frontmatter(path)

    name = frontmatter.get("name", "")
    if not name:
        fail(f"{path}: missing frontmatter name")
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{2,80}", name):
        fail(f"{path}: frontmatter name must be lowercase slug")

    description = frontmatter.get("description", "")
    if len(description) < 120:
        fail(f"{path}: description is missing or too weak")

    missing_sections = sorted(set(REQUIRED_SECTIONS) - section_titles(body))
    if missing_sections:
        fail(f"{path}: missing required sections: {', '.join(missing_sections)}")

    for phrase in REQUIRED_BODY_PHRASES:
        if phrase not in body:
            fail(f"{path}: missing required phrase: {phrase}")

    body_without_safety_rule = body.replace("Never say `guaranteed`, `no risk`, or `fully compliant`.", "")
    lower_body = body_without_safety_rule.lower()
    for claim in FORBIDDEN_CLAIMS:
        if claim in lower_body:
            fail(f"{path}: unsafe determinative language: {claim}")

    if len(re.findall(r"^```", body, re.M)) % 2:
        fail(f"{path}: unbalanced fenced code block")

print("ok: skill files validated")
