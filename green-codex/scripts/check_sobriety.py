#!/usr/bin/env python3
"""Small, dependency-free checks for high-confidence sobriety anti-patterns."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKIP_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__"}
TEXT_SUFFIXES = {
    ".c", ".cc", ".cpp", ".css", ".go", ".h", ".html", ".htm", ".java", ".js", ".jsx",
    ".jl", ".json", ".kt", ".php", ".plsql", ".py", ".rb", ".rs", ".scala", ".scss",
    ".sh", ".sql", ".ts", ".tsx", ".vue", ".xml", ".yaml", ".yml", ".zsh",
}


def finding(rule, path, line, message, severity="important"):
    return {"rule": rule, "path": str(path), "line": line, "message": message, "severity": severity}


def scan_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    findings = []
    suffix = path.suffix.lower()
    lines = text.splitlines()
    if suffix in {".sql", ".plsql"}:
        for number, line in enumerate(lines, 1):
            if re.search(r"\bselect\s+\*", line, re.I):
                findings.append(finding("DB-EFF-001", path, number, "Use an explicit column projection instead of SELECT *."))
    if suffix in {".html", ".htm", ".vue", ".jsx", ".tsx"}:
        for number, line in enumerate(lines, 1):
            if re.search(r"<(?:video|audio)\b[^>]*\bautoplay\b", line, re.I):
                findings.append(finding("WEB-EFF-004", path, number, "Do not autoplay audio or video; require user action."))
    if suffix in {".js", ".jsx", ".ts", ".tsx", ".vue"}:
        for number, line in enumerate(lines, 1):
            if re.search(r"\bsetInterval\s*\(", line):
                findings.append(finding("WEB-EFF-003", path, number, "Polling requires a documented interval, stop condition and cost."))
    return findings


def files_under(root):
    if root.is_file():
        return [root]
    return [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES and not any(part in SKIP_DIRS for part in p.parts)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    findings = []
    for path in files_under(args.path):
        findings.extend(scan_file(path))
    if args.format == "json":
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item['severity'].upper()} {item['rule']} {item['path']}:{item['line']} - {item['message']}")
        if not findings:
            print("No high-confidence sobriety findings.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
