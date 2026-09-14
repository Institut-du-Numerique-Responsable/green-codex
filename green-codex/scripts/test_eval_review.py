"""Regression checks for evaluation evidence; samples here are synthetic fixtures."""

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("run_evals.py")


def main():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        case = {"id": "fixture", "prompt": "Review a query", "expected_rules": ["DB-EFF-001"],
                "required_terms": ["query"], "review_checks": ["Explains the query risk."]}
        (root / "cases.json").write_text(json.dumps([case]))
        response = "FAIL DB-EFF-001: The query transfers unused columns. Select only required fields."
        (root / "fixture.md").write_text(response)
        command = [sys.executable, str(SCRIPT), "--cases", str(root / "cases.json"), "--responses", str(root)]
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 1 and "REVIEW_REQUIRED" in result.stdout, result.stdout
        digest = lambda text: hashlib.sha256(text.encode()).hexdigest()
        review = {"fixture": {"response_sha256": digest(response),
                  "case_sha256": digest(json.dumps(case, sort_keys=True, ensure_ascii=False)),
                  "reviewer": "synthetic unit-test fixture", "verdict": "PASS",
                  "checks": {"Explains the query risk.": {"passed": True, "evidence": "transfers unused columns"}}}}
        (root / "reviews.json").write_text(json.dumps(review))
        run = {"model": "synthetic fixture", "date": "2026-09-13", "skill_sha256": "a" * 64,
               "settings": {"context": "synthetic"}, "limitations": ["Not a model benchmark."]}
        review["fixture"]["run_sha256"] = digest(json.dumps(run, sort_keys=True, ensure_ascii=False))
        (root / "reviews.json").write_text(json.dumps(review))
        (root / "run.json").write_text(json.dumps(run))
        command += ["--reviews", str(root / "reviews.json"), "--run", str(root / "run.json")]
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 0, result.stdout + result.stderr
        # A correct reviewed answer must remain visible even without literal rule IDs.
        concise = "The query transfers unused columns. Select only required fields."
        (root / "fixture.md").write_text(concise)
        review["fixture"]["response_sha256"] = digest(concise)
        (root / "reviews.json").write_text(json.dumps(review))
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 0 and "FORMAT FAIL" in result.stdout and "SEMANTIC PASS" in result.stdout, result.stdout
        strict = subprocess.run(command + ["--strict-format"], capture_output=True, text=True)
        assert strict.returncode == 1 and "SEMANTIC PASS" in strict.stdout, strict.stdout
        (root / "fixture.md").write_text(response)
        review["fixture"]["response_sha256"] = digest(response)
        (root / "reviews.json").write_text(json.dumps(review))
        for key, value in {"model": "different model", "skill_sha256": "b" * 64,
                           "settings": {"context": "different"}}.items():
            (root / "run.json").write_text(json.dumps({**run, key: value}))
            result = subprocess.run(command, capture_output=True, text=True)
            assert result.returncode == 1 and "REVIEW_REQUIRED" in result.stdout, result.stdout
        (root / "run.json").write_text(json.dumps(run))
        (root / "fixture.md").write_text(response + " Edited after review.")
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 1 and "REVIEW_REQUIRED" in result.stdout, result.stdout
        (root / "fixture.md").write_text(response)
        case["prompt"] = "Changed prompt"
        (root / "cases.json").write_text(json.dumps([case]))
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 1, result.stdout
    print("Evaluation review regression checks passed")


if __name__ == "__main__":
    main()
