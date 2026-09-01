#!/usr/bin/env python3
"""Evaluate saved Green Codex responses against the behavioral case catalogue."""

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def evaluate(case, response):
    lowered = response.lower()
    missing_rules = [rule for rule in case["expected_rules"] if rule.lower() not in lowered]
    missing_terms = [term for term in case["required_terms"] if term.lower() not in lowered]
    forbidden = [term for term in case.get("forbidden_terms", []) if term.lower() in lowered]
    statuses = len(re.findall(r"\b(?:PASS|FAIL|REVIEW_REQUIRED)\b", response))
    return missing_rules, missing_terms, forbidden, statuses


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, default=ROOT / "evals" / "cases.json")
    parser.add_argument("--responses", type=Path, required=True)
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    failed = False
    for case in cases:
        response_path = args.responses / f"{case['id']}.md"
        if not response_path.is_file():
            print(f"REVIEW_REQUIRED {case['id']}: response missing")
            failed = True
            continue
        result = evaluate(case, response_path.read_text(encoding="utf-8"))
        missing_rules, missing_terms, forbidden, statuses = result
        if missing_rules or missing_terms or forbidden or statuses == 0:
            print(f"FAIL {case['id']}: rules={missing_rules} terms={missing_terms} forbidden={forbidden} statuses={statuses}")
            failed = True
        else:
            print(f"PASS {case['id']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
