#!/usr/bin/env python3
"""Exercise the closing command, including incomplete and contradictory evidence."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("nr_summary.py")


class SummaryTests(unittest.TestCase):
    def run_summary(self, source="const answer = 42;", status="PASS", strict=False,
                    overrides=None, run_id="test-run", suffix=".js", scan_kind="file", rule_id="CODE-EFF-007"):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / ("app" + suffix)
            target.write_text(source, encoding="utf-8")
            record = {"run_id": "test-run", "scope": "test fixture", "limitations": [],
                      "rules": [{"id": rule_id, "status": status,
                                 "action": "No new dependency", "benefit": "Avoid installation",
                                 "evidence": "Manifest diff inspected"}]}
            record.update(overrides or {})
            if scan_kind == "missing":
                target = root / "missing"
            elif scan_kind == "empty":
                target = root / "empty"
                target.mkdir()
            ledger = root / "record.json"
            ledger.write_text(json.dumps(record), encoding="utf-8")
            command = [sys.executable, str(SCRIPT), "--path", str(target),
                       "--record", str(ledger), "--run-id", run_id]
            if strict:
                command.append("--strict")
            return subprocess.run(command, capture_output=True, text=True)

    def test_summary_explains_actions_and_limits(self):
        result = self.run_summary()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No new dependency", result.stdout)
        self.assertIn("Avoid installation", result.stdout)
        self.assertIn("ne valide pas les règles", result.stdout)

    def test_static_review_is_visible_and_strict_blocks(self):
        result = self.run_summary("setInterval(tick, 1000)", strict=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("WEB-EFF-003", result.stdout)

    def test_declared_failure_fails_even_without_static_findings(self):
        self.assertEqual(self.run_summary(status="FAIL").returncode, 1)

    def test_declared_review_strictness(self):
        self.assertEqual(self.run_summary(status="REVIEW_REQUIRED").returncode, 0)
        self.assertEqual(self.run_summary(status="REVIEW_REQUIRED", strict=True).returncode, 1)

    def test_static_failure_overrides_declared_pass(self):
        result = self.run_summary("SELECT * FROM users", suffix=".sql")
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL `DB-EFF-001`", result.stdout)

    def test_incomplete_scan_and_empty_directory(self):
        for options in ({"scan_kind": "missing"}, {"suffix": ".unknown"}):
            result = self.run_summary(**options)
            self.assertEqual(result.returncode, 2)
            self.assertIn("scan incomplet", result.stdout)
        self.assertEqual(self.run_summary(scan_kind="empty", strict=True).returncode, 1)

    def test_duplicate_rule_rejected(self):
        item = {"id": "CODE-EFF-007", "status": "PASS", "action": "a",
                "benefit": "b", "evidence": "e"}
        self.assertEqual(self.run_summary(overrides={"rules": [item, item]}).returncode, 2)

    def test_new_reference_rules_participate_in_summary(self):
        for rule_id in ("NR-CHARTER-005", "AIR-018", "STAKE-048", "RIA-041",
                        "NR-TOK-007", "NR-TOK-030"):
            with self.subTest(rule=rule_id):
                result = self.run_summary(rule_id=rule_id)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(rule_id, result.stdout)
                self.assertEqual(self.run_summary(rule_id=rule_id, status="FAIL").returncode, 1)

    def test_wrong_run_is_rejected(self):
        self.assertEqual(self.run_summary(run_id="other-run").returncode, 2)

    def test_unknown_rule_or_missing_evidence_rejected(self):
        for item in ({"id": "FAKE-001"}, {"id": "CODE-EFF-007", "status": "PASS"}):
            self.assertEqual(self.run_summary(overrides={"rules": [item]}).returncode, 2)

    def test_empty_record_is_not_success_in_strict_mode(self):
        result = self.run_summary(overrides={"rules": []}, strict=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("aucune action NR", result.stdout)

    def test_malformed_records_are_reported_without_traceback(self):
        for overrides in ({"rules": [None]}, {"limitations": "none"},
                          {"scope": ""}, {"rules": [{"id": []}]}):
            result = self.run_summary(overrides=overrides)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
