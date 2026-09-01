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
    require(SKILL, "Language rule routing")
    require(SKILL, "`LANG-*` section")
    for criterion in ("RGESN", "GR491", "Opquast", "RGAA"):
        require(CRITERIA, criterion)
        require(RULES, criterion)
    for section in ("Universal rules", "Enforceable sobriety rules", "Frontend", "Backend", "Responsible AI", "Audit format"):
        require(RULES, section)
    for rule_id in ("CODE-EFF-001", "CODE-EFF-008", "CODE-EFF-012", "API-EFF-001", "API-EFF-003", "WEB-EFF-001", "DB-EFF-001", "DB-EFF-005", "DB-EFF-010", "INFRA-EFF-001", "INFRA-EFF-005", "OPS-EFF-003", "NET-EFF-002", "HW-EFF-001", "AI-EFF-001", "AI-EFF-006", "MEASURE-EFF-001", "ARCH-SERVERLESS-001", "ARCH-EDGE-001", "ARCH-MOBILE-001", "ARCH-IOT-001", "ARCH-EMBEDDED-001", "ARCH-DIST-001", "ARCH-NOSQL-001", "ARCH-DATA-001", "LANG-JAVA-001", "LANG-JAVA-005", "LANG-RUST-001", "LANG-GO-001", "LANG-PYTHON-001", "LANG-JS-001", "LANG-PHP-001", "LANG-C-001", "LANG-CPP-001", "LANG-RUBY-001", "LANG-SCALA-001", "LANG-KOTLIN-001", "LANG-ZIG-001", "LANG-NIM-001", "LANG-JULIA-001", "LANG-SHELL-001", "LANG-SQL-001", "LANG-PLSQL-001", "LANG-HTML-001", "LANG-CSS-001", "LANG-REACT-001", "LANG-VUE-001", "LANG-ANGULAR-001", "LANG-SVELTE-001", "LANG-PREACT-001", "LANG-ASTRO-001", "LANG-SOLID-001"):
        require(RULES, rule_id)
    print("Green Codex skill checks passed")


if __name__ == "__main__":
    main()
