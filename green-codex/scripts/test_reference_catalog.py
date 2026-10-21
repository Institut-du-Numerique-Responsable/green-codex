#!/usr/bin/env python3
"""Check reference definitions, source coverage and closing-summary registration."""
import re
import unittest
from pathlib import Path

from nr_summary import RULE_FILES, known_rules

REFS = Path(__file__).resolve().parents[1] / "references"


class ReferenceTests(unittest.TestCase):
    def test_token_rules_complete_and_registered(self):
        text = (REFS / "token-sobriety.md").read_text(encoding="utf-8")
        definitions = re.findall(r"\*\*(NR-TOK-\d{3}) :", text)
        expected = {f"NR-TOK-{number:03d}" for number in range(1, 31)}
        self.assertEqual(set(definitions), expected)
        self.assertEqual(len(definitions), len(expected))
        self.assertTrue(expected <= known_rules())

    def test_definitions_unique_and_registered(self):
        definitions = []
        for name in RULE_FILES:
            text = (REFS / name).read_text(encoding="utf-8")
            definitions.extend(re.findall(r"(?:\*\*|### )([A-Z][A-Z0-9-]+-\d{2,3})", text))
        self.assertEqual(len(definitions), len(set(definitions)))
        self.assertEqual(set(definitions), known_rules())

    def test_new_rule_cross_references_exist(self):
        for name in ("nr-charter.md", "air-practices.md", "stakeholder-maturity.md", "ria31.md"):
            text = (REFS / name).read_text(encoding="utf-8")
            cited = set(re.findall(r"\b(?:AIR|STAKE|RIA|NR-CHARTER|[A-Z]+-EFF|AI-CHARTER-[A-Z]+|LANG-[A-Z]+)-\d{3}\b", text))
            self.assertFalse(cited - known_rules(), (name, cited - known_rules()))

    def test_stakeholder_question_coverage(self):
        text = (REFS / "stakeholder-maturity.md").read_text(encoding="utf-8")
        actual = re.findall(r"Source : \[question (\d+\.\d+)\]", text)
        counts = [5, 2, 7, 3, 4, 11, 6, 1, 4, 5]
        expected = {f"{chapter}.{q}" for chapter, count in enumerate(counts, 1)
                    for q in range(1, count + 1)}
        self.assertEqual(set(actual), expected)
        self.assertEqual(len(actual), len(expected))

    def test_air_fiche_coverage(self):
        text = (REFS / "air-practices.md").read_text(encoding="utf-8")
        actual = re.findall(r"Source : \[([GMCIVD]\d+)\]", text)
        expected = {f"{family}{n}" for family, count in
                    {"G": 4, "M": 2, "C": 5, "I": 3, "V": 2, "D": 2}.items()
                    for n in range(1, count + 1)}
        self.assertEqual(set(actual), expected)
        self.assertEqual(len(actual), len(expected))

    def test_ria_question_count_and_duplicate_disambiguation(self):
        text = (REFS / "ria31.md").read_text(encoding="utf-8")
        actual = re.findall(r"Repère source : `([^`]+)`", text)
        self.assertEqual(len(actual), 41)
        self.assertEqual(len(set(actual)), 41)
        self.assertIn("STR-1_03-1, occurrence 1", actual)
        self.assertIn("STR-1_03-1, occurrence 2", actual)


if __name__ == "__main__":
    unittest.main()
