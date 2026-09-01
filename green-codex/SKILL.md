---
name: green-codex
description: Apply Green IT and responsible digital practices when designing, coding, reviewing, or auditing software and digital services.
---

# Green Codex

Use this skill when a request concerns eco-design, digital sobriety, accessibility, responsible
AI, sustainable software, or an environmental audit of code or a digital service.

## Working method

1. Identify the technology, lifecycle stage, and user or environmental risk in scope.
2. Inspect the smallest relevant set of files and existing project guidance before proposing changes.
3. Apply the relevant checks in `references/criteria.md`; do not invent a criterion or claim a
   compliance level without evidence.
4. Apply the enforceable sobriety rules in `references/rules.md` (identifiers `CODE-*`, `API-*`,
   `WEB-*`, and `DB-*`) when code, APIs, storage, or databases are in scope. Report `PASS`, `FAIL`,
   or `REVIEW_REQUIRED` for each applicable rule.
5. Prefer measurable, reversible improvements: reduce transferred bytes, requests, CPU and memory
   work, storage, build output, and unnecessary polling. Preserve functionality and accessibility.
6. For accessibility, check semantic HTML, keyboard operation, focus, contrast, names and errors;
   keep official acronyms such as RGAA and RGESN unchanged.
7. For AI features, consider model size, prompt and context volume, caching, rate limits, data
   minimisation, human oversight, and disclosure of AI-generated content.
8. Report findings with file and line references, impact, confidence, and a concrete fix. Separate
   observed facts from recommendations.

## Review output

When auditing, group results by severity (blocking, important, improvement), cite the applicable
reference, and include a short measurement or verification plan. Do not optimise for a score at the
expense of security, correctness, resilience, or user needs.

## Repositories and CI

Before changing generated artefacts, locate the source of truth and its generator. Run the project's
tests, linters, and data validators. Add a regression test for a new rule when practical. Never
commit secrets, build caches, dependency directories, or local reports unless explicitly requested.

Read `references/criteria.md` for the compact mapping of RGESN, GR491, Opquast, and RGAA concerns,
and `references/rules.md` for the complete English rule set.
