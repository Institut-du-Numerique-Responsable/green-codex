#!/usr/bin/env python3
"""Check NR closing-summary structure through Codex lifecycle hooks, without scanning code."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

from nr_summary import known_rules

MAX_INPUT = 1024 * 1024
HEADING = re.compile(r"(?im)^\s*(?:#{1,6}\s*|\*\*)?(?:bilan NR|NR summary)\b")
FIELDS = {
    "action": r"actions?",
    "benefit": r"intérêt|bénéfices?|benefits?",
    "evidence": r"preuves?|evidence",
    "limits": r"limites?|limits?|limitations?",
}
INSTRUCTION = (
    "Complete the final answer with a short Bilan NR / NR summary in the user's language. "
    "Use labelled fields Action, Benefit/Intérêt, Evidence/Preuve and Limits/Limites, "
    "and the applicable Green Codex rule IDs. Report only actions actually performed and "
    "observed evidence. State missing checks and unmeasured gains. If no NR action applies, "
    "state 'NR: non applicable' with a reason. Do not invent proof or run unrelated checks."
)


def check_summary(message):
    """Return structural omissions, not a verdict on the truth of the evidence."""
    heading = HEADING.search(message)
    if not heading:
        return ["NR summary heading"]
    section = message[heading.end():]
    if re.search(r"(?i)NR:\s*(?:non applicable|not applicable)\s*[-—:]\s*\S.+", section):
        return []
    missing = []
    for name, pattern in FIELDS.items():
        matches = re.finditer(
            rf"(?im)(?:^|[;|])[ \t]*(?:[-*][ \t]+)?(?:\*\*)?(?:{pattern})"
            rf"(?:\*\*)?[ \t]*:(?:\*\*)?[ \t]*([^\n;|]*)", section)
        if not any(match.group(1).strip(" *\t\r") for match in matches):
            missing.append(name)
    if not set(re.findall(r"\b[A-Z][A-Z0-9-]+-\d{2,3}\b", section)) & known_rules():
        missing.append("known rule ID")
    return missing


def handle(payload, state_dir):
    if not isinstance(payload, dict):
        raise ValueError("hook input must be an object")
    event = payload.get("hook_event_name")
    if event not in {"UserPromptSubmit", "Stop"}:
        return {}
    session, turn = payload.get("session_id"), payload.get("turn_id")
    if not isinstance(session, str) or not session or not isinstance(turn, str) or not turn:
        raise ValueError("session_id and turn_id are required")
    path = state_dir / (hashlib.sha256(session.encode()).hexdigest() + ".json")
    if event == "UserPromptSubmit":
        prompt = payload.get("prompt")
        if not isinstance(prompt, str):
            raise ValueError("prompt must be text")
        # An explicit invocation arms only this turn, never future unrelated messages.
        if not re.search(r"\$green-codex\b", prompt):
            path.unlink(missing_ok=True)
            return {}
        state_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(dir=state_dir)
        try:
            with os.fdopen(fd, "w") as stream:
                json.dump({"turn_id": turn}, stream)
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)
        return {"hookSpecificOutput": {"hookEventName": event, "additionalContext": INSTRUCTION}}

    armed = False
    if path.exists():
        with path.open() as stream:
            record = json.loads(stream.read(4096))
        armed = isinstance(record, dict) and record.get("turn_id") == turn
        if armed:
            path.unlink()
    # A continuation is never blocked again, even when its summary remains incomplete.
    if payload.get("stop_hook_active") is True:
        return {}
    message = payload.get("last_assistant_message") or ""
    if not isinstance(message, str):
        raise ValueError("last_assistant_message must be text or null")
    ids = set(re.findall(r"\b[A-Z][A-Z0-9-]+-\d{2,3}\b", message))
    scoped = armed or HEADING.search(message) or bool(ids & known_rules())
    if not scoped:
        return {}
    missing = check_summary(message)
    if missing:
        return {"decision": "block", "reason": INSTRUCTION + " Missing: " + ", ".join(missing) + "."}
    return {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path.home() / ".codex" / "green-codex-hook-state")
    args = parser.parse_args()
    try:
        raw = sys.stdin.buffer.read(MAX_INPUT + 1)
        if len(raw) > MAX_INPUT:
            raise ValueError("hook input exceeds 1 MiB")
        result = handle(json.loads(raw), args.state_dir)
    except (OSError, ValueError, UnicodeError):
        # Do not expose prompts or block user work on malformed input or storage failure.
        result = {"systemMessage": "NR hook unavailable: input or local state could not be read; summary not checked."}
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
