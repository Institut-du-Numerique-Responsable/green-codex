#!/usr/bin/env python3
"""Validate the behavioral evaluation case schema."""

import json
from pathlib import Path
import sys
import re


ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "evals" / "cases.json"
RULES = ROOT / "green-codex" / "references" / "rules.md"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_evals import evaluate


def main():
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    rules = RULES.read_text(encoding="utf-8")
    charter = (RULES.parent / "responsible-ai-charter.md").read_text(encoding="utf-8")
    rules += "\n" + charter
    charter_ids = re.findall(r"\*\*(AI-CHARTER-[A-Z]+-\d{3})\b", charter)
    assert charter_ids and len(charter_ids) == len(set(charter_ids)), "Duplicate or missing charter rule definitions"
    assert len(cases) >= 8
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))
    for case in cases:
        assert case["prompt"].strip()
        assert case["expected_rules"] or case.get("scope_control") is True
        assert case["required_terms"]
        for rule in case["expected_rules"]:
            assert f"**{rule}" in rules, f"unknown rule: {rule}"
        for term in case.get("forbidden_terms", []):
            assert term.strip()
        assert case.get("review_checks"), f"Missing semantic review criteria: {case['id']}"
    exercised = {rule for case in cases for rule in case["expected_rules"]}
    assert set(charter_ids) <= exercised, "A charter rule has no evaluation scenario"
    sample = cases[0]
    response = "DB-EFF-003 API-EFF-001 LANG-PYTHON-001 query pagination verification FAIL"
    missing_rules, missing_terms, forbidden, statuses = evaluate(sample, response)
    assert not missing_rules and not missing_terms and not forbidden and statuses == 1
    print(f"Evaluation schema checks passed ({len(cases)} cases)")


if __name__ == "__main__":
    main()
