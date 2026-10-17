#!/usr/bin/env python3
"""Validate a task's NR action record and print its evidence-based closing summary."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from check_sobriety import files_under, scan_file

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"PASS", "FAIL", "REVIEW_REQUIRED"}
RULE_FILES = ("rules.md", "usage-practices.md", "responsible-ai-charter.md",
              "nr-charter.md", "air-practices.md", "stakeholder-maturity.md", "ria31.md")


def known_rules():
    ids = set()
    for name in RULE_FILES:
        text = (ROOT / "references" / name).read_text(encoding="utf-8")
        ids.update(re.findall(r"(?:\*\*|### )([A-Z][A-Z0-9-]+-\d{2,3})", text))
    return ids


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(record, run_id):
    if not isinstance(record, dict) or record.get("run_id") != run_id:
        raise ValueError("record run_id must match this execution")
    if not nonempty(record.get("scope")):
        raise ValueError("record requires a scope")
    if not isinstance(record.get("rules"), list):
        raise ValueError("record requires a rules array")
    if not isinstance(record.get("limitations"), list) or not all(
        nonempty(value) for value in record["limitations"]
    ):
        raise ValueError("limitations must be an array of nonempty strings")
    ids, seen = known_rules(), set()
    for item in record["rules"]:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError("each rule requires an id")
        if item["id"] not in ids or item["id"] in seen:
            raise ValueError(f"unknown or duplicate rule: {item['id']}")
        seen.add(item["id"])
        if not isinstance(item.get("status"), str) or item["status"] not in STATUSES:
            raise ValueError(f"invalid status: {item['id']}")
        for field in ("action", "benefit", "evidence"):
            if not nonempty(item.get(field)):
                raise ValueError(f"{item['id']} requires {field}")
    return record


def one_line(value):
    return " ".join(value.split())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, type=Path, help="Explicit static scan scope")
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--run-id", required=True, help="Unique ID also written in the task record")
    parser.add_argument("--strict", action="store_true", help="Return 1 for unresolved reviews too")
    args = parser.parse_args(argv)
    try:
        record = validate(json.loads(args.record.read_text(encoding="utf-8")), args.run_id)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"NR summary incomplete: {error}", file=sys.stderr)
        return 2

    print(f"## Bilan NR — {one_line(args.run_id)}\n")
    print(f"Périmètre déclaré : {one_line(record['scope'])}\n")
    print("Actions consignées (preuves à examiner ; le script ne les certifie pas) :\n")
    for item in record["rules"]:
        print(f"- {item['status']} `{item['id']}` — {one_line(item['action'])} "
              f"Intérêt NR : {one_line(item['benefit'])} "
              f"Preuve / manque : {one_line(item['evidence'])}")
    if not record["rules"]:
        print("- REVIEW_REQUIRED : aucune action NR consignée.")

    print(f"\nContrôles statiques relancés sur : {args.path}\n")
    findings, scanned = [], 0
    try:
        for path in files_under(args.path):
            findings.extend(scan_file(path))
            scanned += 1
    except (OSError, UnicodeError, ValueError) as error:
        print(f"REVIEW_REQUIRED : scan incomplet : {error}")
        return 2
    for item in findings:
        print(f"- {item['status']} `{item['rule']}` — {item['path']}:{item['line']} : {item['message']}")
    if not findings:
        print(f"- Aucun signal détecté dans {scanned} fichier(s) ; cela ne valide pas les règles.")
    print("\nLimites : contrôle de trois motifs seulement (projection SQL, autoplay, polling). "
          "Les autres règles nécessitent leurs propres preuves. Aucun gain environnemental "
          "ni conformité déduit du scan.")
    for limitation in record["limitations"]:
        print(f"- {one_line(limitation)}")
    statuses = [item["status"] for item in record["rules"] + findings]
    if not scanned or not record["rules"]:
        statuses.append("REVIEW_REQUIRED")
        if not scanned:
            print("- REVIEW_REQUIRED : aucun fichier pris en charge dans le périmètre statique.")
    return int("FAIL" in statuses or (args.strict and "REVIEW_REQUIRED" in statuses))


if __name__ == "__main__":
    raise SystemExit(main())
