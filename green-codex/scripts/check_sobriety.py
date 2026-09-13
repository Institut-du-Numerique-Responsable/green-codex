#!/usr/bin/env python3
"""Small, dependency-free checks for high-confidence sobriety anti-patterns."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SKIP_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__"}
TEXT_SUFFIXES = {
    ".c", ".cc", ".cpp", ".css", ".go", ".h", ".html", ".htm", ".java", ".js", ".jsx",
    ".jl", ".json", ".kt", ".php", ".plsql", ".py", ".rb", ".rs", ".scala", ".scss",
    ".sh", ".sql", ".ts", ".tsx", ".vue", ".xml", ".yaml", ".yml", ".zsh",
}


def finding(rule, path, line, message, severity="important", status="FAIL"):
    return {"rule": rule, "path": str(path), "line": line, "message": message, "severity": severity, "status": status}


def mask_tokens(text, pattern):
    # Preserve positions so findings still point to the original source lines.
    return re.sub(pattern, lambda match: re.sub(r"[^\n]", " ", match.group()), text, flags=re.S)


class MediaParser(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.findings = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"video", "audio"}:
            return
        for name, value in attrs:
            if name == "autoplay":
                dynamic = value is not None and value.startswith("{")
                if dynamic and value.strip() == "{false}":
                    continue
                self.findings.append(finding(
                    "WEB-EFF-004", self.path, self.getpos()[0],
                    "Verify dynamic autoplay." if dynamic else "Do not autoplay audio or video; require user action.",
                    status="REVIEW_REQUIRED" if dynamic else "FAIL",
                ))


def scan_file(path):
    text = path.read_text(encoding="utf-8")
    findings = []
    suffix = path.suffix.lower()
    if suffix in {".sql", ".plsql"}:
        sql = mask_tokens(text, r"'(?:(?:'')|[^'])*'|\"(?:(?:\"\")|[^\"])*\"|--[^\n]*|/\*.*?\*/")
        for match in re.finditer(r"\bselect\s+\*", sql, re.I):
            number = sql.count("\n", 0, match.start()) + 1
            findings.append(finding("DB-EFF-001", path, number, "Use an explicit column projection instead of SELECT *."))
    if suffix in {".html", ".htm", ".vue", ".jsx", ".tsx"}:
        parser = MediaParser(path)
        parser.feed(text)
        findings.extend(parser.findings)
    if suffix in {".js", ".jsx", ".ts", ".tsx", ".vue"}:
        javascript = mask_tokens(text, r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"|`(?:\\.|[^`\\])*`|//[^\n]*|/\*.*?\*/")
        for match in re.finditer(r"\bsetInterval\s*\(", javascript):
            number = javascript.count("\n", 0, match.start()) + 1
            findings.append(finding("WEB-EFF-003", path, number, "Review the polling interval, stop condition and cost.", severity="review", status="REVIEW_REQUIRED"))
    return findings


def files_under(root):
    if not root.exists():
        raise OSError(f"Path does not exist: {root}")
    if root.is_file():
        if root.suffix.lower() not in TEXT_SUFFIXES:
            raise ValueError(f"Unsupported file type: {root}")
        yield root
        return
    if not root.is_dir():
        raise ValueError(f"Not a regular file or directory: {root}")

    def raise_walk_error(error):
        raise error

    for directory, dirs, names in os.walk(root, onerror=raise_walk_error):
        dirs[:] = sorted(name for name in dirs if name not in SKIP_DIRS)
        for name in sorted(names):
            path = Path(directory) / name
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    findings = []
    scanned = 0
    try:
        for path in files_under(args.path):
            findings.extend(scan_file(path))
            scanned += 1
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Scan incomplete: {error}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item['status']} {item['rule']} {item['path']}:{item['line']} - {item['message']}")
        if not findings:
            print(f"No static findings in {scanned} supported files; this is not a compliance assessment.")
    return 1 if any(item["status"] == "FAIL" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
