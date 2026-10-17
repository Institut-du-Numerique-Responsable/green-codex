#!/usr/bin/env python3
"""Exercise the hook's turn isolation, continuation limit and JSON protocol."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from nr_hook import handle
from install_nr_hook import updated_config

SUMMARY = '''## Bilan NR
Action: CODE-EFF-007 — standard library only.
Intérêt: no extra dependency.
Preuve: imports inspected.
Limites: energy not measured.
'''


class HookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.state = Path(self.temp.name)

    def event(self, event="Stop", **changes):
        return dict(hook_event_name=event, session_id="session", turn_id="turn", **changes)

    def arm(self):
        return handle(self.event("UserPromptSubmit", prompt="$green-codex review"), self.state)

    def test_installation_preserves_other_hooks_and_is_idempotent(self):
        original = {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "existing"}]}]}}
        result = updated_config(original, "python3 /skill/nr_hook.py")
        self.assertEqual(result["hooks"]["Stop"][0], original["hooks"]["Stop"][0])
        self.assertEqual(updated_config(result, "python3 /skill/nr_hook.py"), result)
        self.assertEqual(len(original["hooks"]["Stop"]), 1)

    def test_explicit_invocation_reminds_then_catches_missing_summary(self):
        self.assertIn("hookSpecificOutput", self.arm())
        output = handle(self.event(last_assistant_message="Done."), self.state)
        self.assertEqual(output["decision"], "block")
        self.assertEqual(list(self.state.iterdir()), [])

    def test_unrelated_turn_is_not_blocked(self):
        self.assertEqual(handle(self.event(last_assistant_message="Bonjour"), self.state), {})

    def test_next_prompt_resets_scope(self):
        self.arm()
        handle(self.event("UserPromptSubmit", prompt="merci"), self.state)
        self.assertEqual(handle(self.event(last_assistant_message="De rien"), self.state), {})

    def test_stale_turn_and_other_session_do_not_arm(self):
        self.arm()
        for key in ("turn_id", "session_id"):
            event = self.event(last_assistant_message="Done")
            event[key] = "other"
            self.assertEqual(handle(event, self.state), {})

    def test_existing_id_catches_implicit_use(self):
        out = handle(self.event(last_assistant_message="Applied CODE-EFF-007."), self.state)
        self.assertEqual(out["decision"], "block")

    def test_complete_summary_passes(self):
        self.arm()
        self.assertEqual(handle(self.event(last_assistant_message=SUMMARY), self.state), {})

    def test_english_markdown_summary(self):
        message = "## NR summary\n**Action:** CODE-EFF-007 used.\n**Benefit:** no dependency.\n**Evidence:** imports checked.\n**Limits:** energy unknown."
        self.assertEqual(handle(self.event(last_assistant_message=message), self.state), {})

    def test_empty_fields_are_rejected(self):
        message = "## Bilan NR CODE-EFF-007\nAction:\nBenefit:\nEvidence:\nLimits:"
        out = handle(self.event(last_assistant_message=message), self.state)
        for field in ("action", "benefit", "evidence", "limits"):
            self.assertIn(field, out["reason"])

    def test_missing_proof_is_requested(self):
        out = handle(self.event(last_assistant_message=SUMMARY.replace("Preuve:", "Note:")), self.state)
        self.assertIn("evidence", out["reason"])

    def test_unknown_rule_does_not_validate_summary(self):
        out = handle(self.event(last_assistant_message=SUMMARY.replace("CODE-EFF-007", "MADE-UP-001")), self.state)
        self.assertIn("known rule ID", out["reason"])

    def test_no_action_needs_reason(self):
        for message, blocked in [("## Bilan NR\nNR: non applicable — simple greeting.", False),
                                 ("## Bilan NR\nNR: non applicable", True)]:
            self.assertEqual("decision" in handle(self.event(last_assistant_message=message), self.state), blocked)

    def test_continuation_never_loops(self):
        self.arm()
        self.assertEqual(handle(self.event(stop_hook_active=True, last_assistant_message="Incomplete"), self.state), {})

    def test_cli_errors_are_valid_json_without_prompt_leak(self):
        for raw in ("private malformed input", "[]", "x" * (1024 * 1024 + 1)):
            proc = subprocess.run([sys.executable, str(Path(__file__).with_name("nr_hook.py")),
                                   "--state-dir", str(self.state)], input=raw, text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0)
            self.assertIn("systemMessage", json.loads(proc.stdout))
            self.assertNotIn("private", proc.stdout)


if __name__ == "__main__":
    unittest.main()
