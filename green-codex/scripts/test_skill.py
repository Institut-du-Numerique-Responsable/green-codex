#!/usr/bin/env python3
"""Deterministic smoke tests for the Green Codex skill package."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CRITERIA = ROOT / "references" / "criteria.md"
RULES = ROOT / "references" / "rules.md"
METADATA = ROOT / "agents" / "openai.yaml"


def require(path, text):
    contents = path.read_text(encoding="utf-8")
    if text not in contents:
        raise AssertionError(f"{path}: missing {text!r}")


def main():
    for path in (SKILL, CRITERIA, RULES, METADATA):
        if not path.is_file():
            raise AssertionError(f"missing required file: {path}")
    require(SKILL, "name: green-codex")
    require(SKILL, "references/rules.md")
    for criterion in ("RGESN", "GR491", "Opquast", "RGAA"):
        require(CRITERIA, criterion)
        require(RULES, criterion)
    for section in ("Universal rules", "Enforceable sobriety rules", "Frontend", "Backend", "Responsible AI", "Audit format"):
        require(RULES, section)
    for rule_id in ("CODE-EFF-001", "CODE-EFF-006", "API-EFF-001", "WEB-EFF-001", "DB-EFF-001", "DB-EFF-005"):
        require(RULES, rule_id)
    print("Green Codex skill checks passed")


if __name__ == "__main__":
    main()
