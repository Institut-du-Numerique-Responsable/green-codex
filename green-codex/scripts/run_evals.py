#!/usr/bin/env python3
"""Evaluate saved Green Codex responses against the behavioral case catalogue."""

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REVIEW_CHECKS = [
    "Recommendations address the prompt and explain their reasoning.",
    "Evidence, uncertainty and verification are appropriate to the claim.",
    "Scope, accessibility, security and correctness are preserved.",
]


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def semantic_review(case, response, review, run):
    if not isinstance(run, dict) or not all(run.get(key) for key in ("model", "date", "skill_sha256", "settings")):
        return "REVIEW_REQUIRED", "run metadata missing"
    if not isinstance(run.get("limitations"), list) or not re.fullmatch(r"[0-9a-f]{64}", str(run["skill_sha256"])):
        return "REVIEW_REQUIRED", "run metadata invalid"
    if not isinstance(review, dict) or not review.get("reviewer"):
        return "REVIEW_REQUIRED", "independent semantic review missing"
    if review.get("run_sha256") != digest(json.dumps(run, sort_keys=True, ensure_ascii=False)):
        return "REVIEW_REQUIRED", "review does not match this run"
    if review.get("response_sha256") != digest(response) or review.get("case_sha256") != digest(json.dumps(case, sort_keys=True, ensure_ascii=False)):
        return "REVIEW_REQUIRED", "review does not match this response and case"
    checks = review.get("checks", {})
    if not isinstance(checks, dict):
        return "REVIEW_REQUIRED", "review checks missing"
    for check in case.get("review_checks", DEFAULT_REVIEW_CHECKS):
        result = checks.get(check)
        if not isinstance(result, dict) or not isinstance(result.get("passed"), bool) or not result.get("evidence"):
            return "REVIEW_REQUIRED", "review needs a decision and evidence for each check"
        if result["passed"] is False:
            return "FAIL", f"semantic review: {check}"
    if review.get("verdict") not in {"PASS", "FAIL"}:
        return "REVIEW_REQUIRED", "semantic verdict missing"
    return review["verdict"], "recorded semantic review bound to response, case and run"


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
    parser.add_argument("--reviews", type=Path, help="Independent semantic reviews bound to response and case hashes")
    parser.add_argument("--run", type=Path, help="Model, date, skill hash, settings and limitations for this run")
    parser.add_argument("--strict-format", action="store_true", help="Also fail the exit status for literal rule/term/status mismatches")
    parser.add_argument("--case", action="append", dest="case_ids", help="Evaluate only this case (repeatable); output reports partial coverage")
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    total = len(cases)
    if args.case_ids:
        unknown = set(args.case_ids) - {case["id"] for case in cases}
        if unknown:
            parser.error(f"Unknown cases: {sorted(unknown)}")
        cases = [case for case in cases if case["id"] in args.case_ids]
    reviews = json.loads(args.reviews.read_text()) if args.reviews else {}
    run = json.loads(args.run.read_text()) if args.run else {}
    if not isinstance(reviews, dict):
        parser.error("Reviews must be a JSON object keyed by case ID")
    print(f"Coverage: {len(cases)}/{total} cases" + (" (partial run)" if len(cases) < total else ""))
    failed = False
    for case in cases:
        response_path = args.responses / f"{case['id']}.md"
        if not response_path.is_file():
            print(f"REVIEW_REQUIRED {case['id']}: response missing")
            failed = True
            continue
        response = response_path.read_text(encoding="utf-8")
        result = evaluate(case, response)
        missing_rules, missing_terms, forbidden, statuses = result
        format_failed = bool(missing_rules or missing_terms or forbidden or statuses == 0)
        print(f"FORMAT {'FAIL' if format_failed else 'PASS'} {case['id']}: rules={missing_rules} terms={missing_terms} flagged_terms={forbidden} statuses={statuses}")
        status, reason = semantic_review(case, response, reviews.get(case["id"]), run)
        print(f"SEMANTIC {status} {case['id']}: {reason}")
        failed = failed or status != "PASS" or (args.strict_format and format_failed)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
