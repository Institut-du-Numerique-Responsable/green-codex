#!/usr/bin/env python3
"""Tests for the static sobriety checker."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_sobriety.py"


def run_checker(path, *args):
    return subprocess.run(
        [sys.executable, str(CHECKER), "--path", str(path), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def main():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "query.sql").write_text("SELECT * FROM users;\n", encoding="utf-8")
        (root / "page.html").write_text("<video autoplay src='x.mp4'></video>\n", encoding="utf-8")
        (root / "app.js").write_text("setInterval(refresh, 100);\n", encoding="utf-8")

        result = run_checker(root)
        assert result.returncode == 1, result.stdout + result.stderr
        assert "DB-EFF-001" in result.stdout
        assert "WEB-EFF-004" in result.stdout
        assert "WEB-EFF-003" in result.stdout

        report = run_checker(root, "--format", "json")
        findings = json.loads(report.stdout)
        assert {item["rule"] for item in findings} == {
            "DB-EFF-001",
            "WEB-EFF-003",
            "WEB-EFF-004",
        }

        clean = root / "clean"
        clean.mkdir()
        (clean / "query.sql").write_text("SELECT id, name FROM users LIMIT 100;\n", encoding="utf-8")
        assert run_checker(clean).returncode == 0
    print("Sobriety checker tests passed")


if __name__ == "__main__":
    main()
