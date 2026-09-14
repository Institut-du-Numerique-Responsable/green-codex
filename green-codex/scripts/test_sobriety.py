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

        assert run_checker(root / "missing").returncode == 2
        unreadable = root / "invalid.sql"
        unreadable.write_bytes(b"\xff")
        assert run_checker(unreadable).returncode == 2

        sql = root / "comments.sql"
        sql.write_text("-- SELECT * is forbidden\n/* SELECT *\n */\nSELECT 'SELECT *', id FROM users;\n")
        assert run_checker(sql).returncode == 0
        sql.write_text("-- comment\nSELECT\n * FROM users;\n")
        report = run_checker(sql, "--format", "json")
        assert report.returncode == 1
        assert json.loads(report.stdout)[0]["line"] == 2

        sql.write_text("SELECT EXISTS (/* existence only */ SELECT * FROM orders WHERE customer_id = $1);\n")
        assert json.loads(run_checker(sql, "--format", "json").stdout) == []
        sql.write_text("SELECT EXISTS ((SELECT * FROM orders));\n")
        assert json.loads(run_checker(sql, "--format", "json").stdout) == []
        sql.write_text("SELECT * FROM orders WHERE EXISTS (SELECT * FROM users);\n")
        findings = json.loads(run_checker(sql, "--format", "json").stdout)
        assert len(findings) == 1 and findings[0]["status"] == "FAIL"

        jsx = root / "example.tsx"
        jsx.write_text('// Example: <video autoPlay />\nconst example = "<video autoPlay />";\nexport const Page = () => <p>No video</p>;\n')
        assert json.loads(run_checker(jsx, "--format", "json").stdout) == []
        jsx.write_text('export const Page = () => <video autoPlay />;\n')
        findings = json.loads(run_checker(jsx, "--format", "json").stdout)
        assert len(findings) == 1 and findings[0]["status"] == "REVIEW_REQUIRED"
        jsx.write_text('export const Page = () => <video src="movie.mp4" autoPlay />;\n')
        findings = json.loads(run_checker(jsx, "--format", "json").stdout)
        assert len(findings) == 1 and findings[0]["status"] == "REVIEW_REQUIRED"

        media = root / "multiline.html"
        media.write_text("<!-- <video autoplay> -->\n<video\n autoplay\n src='x.mp4'></video>\n")
        report = run_checker(media, "--format", "json")
        assert report.returncode == 1
        assert len(json.loads(report.stdout)) == 1
        assert json.loads(report.stdout)[0]["line"] == 2
        media.write_text("<video data-autoplay='yes' title='autoplay'></video>\n")
        assert run_checker(media).returncode == 0

        polling = root / "bounded.js"
        polling.write_text("const timer = setInterval(refresh, 1000);\nsetTimeout(() => clearInterval(timer), 5000);\n")
        report = run_checker(polling, "--format", "json")
        assert report.returncode == 0
        assert json.loads(report.stdout)[0]["status"] == "REVIEW_REQUIRED"
        polling.write_text("// setInterval(refresh, 100);\nconst example = 'setInterval(refresh, 100)';\n")
        assert json.loads(run_checker(polling, "--format", "json").stdout) == []
    print("Sobriety checker tests passed")


if __name__ == "__main__":
    main()
