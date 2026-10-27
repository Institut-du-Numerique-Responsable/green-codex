#!/usr/bin/env python3
"""Check that every imported Green Claude rule is accounted for in Green Codex."""
import re
import unittest
from pathlib import Path

from nr_summary import RULE_FILES, known_rules

REFS = Path(__file__).resolve().parents[1] / "references"
MAPPING = REFS / "green-claude-mapping.md"
STATUSES = {"couverte", "nouvelle", "adaptée", "exclue"}


def parse_mapping(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        # Only table rows whose first cell is a Green Claude identifier count.
        if len(cells) != 4 or not re.fullmatch(r"`[A-Z][A-Z0-9-]+-\d{2,3}`", cells[0]):
            continue
        rows.append({
            "source": cells[0].strip("`"),
            "status": cells[1],
            "targets": cells[2].replace("`", ""),
            "reason": cells[3],
        })
    return rows


class MappingTests(unittest.TestCase):
    def test_mapping_rows_valid(self):
        rows = parse_mapping(MAPPING)
        self.assertTrue(rows)
        self.assertEqual(len({r["source"] for r in rows}), len(rows))
        for r in rows:
            self.assertIn(r["status"], STATUSES, r)
            if r["status"] in {"exclue", "adaptée"}:
                self.assertTrue(r["reason"].strip(), r)
            if r["status"] == "exclue":
                self.assertRegex(r["reason"], r"^X-(HOOK|CMD|PRODUCT)\b", r)

    def test_mapping_targets_exist(self):
        known = known_rules()
        for r in parse_mapping(MAPPING):
            if r["status"] != "exclue":
                targets = set(r["targets"].split(", "))
                self.assertFalse(targets - known, r)

    def test_mapping_not_registered_as_definitions(self):
        text = MAPPING.read_text(encoding="utf-8")
        self.assertNotRegex(text, r"(?:\*\*|### )[A-Z][A-Z0-9-]+-\d{2,3}")

    def test_language_families_routed(self):
        rules = (REFS / "rules.md").read_text(encoding="utf-8")
        charter = (REFS / "nr-charter.md").read_text(encoding="utf-8")
        for family in ("LANG-CSHARP", "LANG-SWIFT"):
            self.assertIn(f"`{family}-*`", rules)
            self.assertRegex(charter, rf"{family}-\d{{3}}")
        self.assertNotIn("inventer une famille `LANG-CSHARP-*`", charter)

    def test_no_claude_specific_wording(self):
        pattern = re.compile(r"\b(CLAUDE\.md|Haiku|Sonnet|Opus|Anthropic)\b")
        for name in RULE_FILES:
            text = (REFS / name).read_text(encoding="utf-8")
            self.assertIsNone(pattern.search(text), name)


if __name__ == "__main__":
    unittest.main()
