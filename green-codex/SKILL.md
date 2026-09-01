---
name: green-codex
description: Apply Green IT and responsible digital practices when designing, coding, reviewing, or auditing software and digital services.
---

# Green Codex

Use this skill when a request concerns eco-design, digital sobriety, accessibility, responsible
AI, sustainable software, or an environmental audit of code or a digital service.

No programming language, framework, database or hosting provider is inherently “green”. Assess the
way it is used: architecture, algorithms, configuration, workload, lifecycle, accessibility and
measured resource impact. A familiar or interpreted technology can be the most responsible choice
when it meets the budget and avoids unnecessary migration; a compiled or lightweight technology can
still be wasteful when poorly designed.

## Working method

1. Identify the technology, lifecycle stage, and user or environmental risk in scope.
2. Inspect the smallest relevant set of files and existing project guidance before proposing changes.
3. Apply the relevant checks in `references/criteria.md`; do not invent a criterion or claim a
   compliance level without evidence.
   For high-confidence static anti-patterns, run `python green-codex/scripts/check_sobriety.py`
   and treat its findings as inputs to the review, not as proof of overall compliance.
4. Apply the enforceable sobriety rules in `references/rules.md` (identifiers `CODE-*`, `API-*`,
   `WEB-*`, `DB-*`, `INFRA-*`, and `OPS-*`) when code, APIs, storage, databases, infrastructure,
   or operations are in scope. Report `PASS`, `FAIL`, or `REVIEW_REQUIRED` for each applicable rule.
5. Prefer measurable, reversible improvements: reduce transferred bytes, requests, CPU and memory
   work, storage, build output, and unnecessary polling. Preserve functionality and accessibility.
6. For accessibility, check semantic HTML, keyboard operation, focus, contrast, names and errors;
   keep official acronyms such as RGAA and RGESN unchanged.
7. For AI features, consider model size, prompt and context volume, caching, rate limits, data
   minimisation, human oversight, and disclosure of AI-generated content.
8. Report findings with file and line references, impact, confidence, and a concrete fix. Separate
   observed facts from recommendations.

## Language rule routing

Detect the languages and frameworks from file extensions, build manifests, lockfiles and runtime
configuration before reviewing code. Read and apply every matching `LANG-*` section in
`references/rules.md`; do not substitute a generic rule when a language-specific rule exists.

| Evidence found | Required rule families |
| --- | --- |
| `.java`, Maven or Gradle | `LANG-JAVA-*` |
| `.kt` | `LANG-KOTLIN-*` |
| `.scala` | `LANG-SCALA-*` |
| `.rs` | `LANG-RUST-*` |
| `.c`, `.h` | `LANG-C-*` |
| `.cc`, `.cpp`, `.cxx`, `.hpp` | `LANG-CPP-*` |
| `.go` | `LANG-GO-*` |
| `.py` | `LANG-PYTHON-*` |
| `.js`, `.jsx`, `.ts`, `.tsx`, Node manifests | `LANG-JS-*` plus detected framework rules |
| `.php` | `LANG-PHP-*` |
| `.rb` | `LANG-RUBY-*` |
| `.nim` | `LANG-NIM-*` |
| `.zig` | `LANG-ZIG-*` |
| `.jl` | `LANG-JULIA-*` |
| `.sql` | `LANG-SQL-*` |
| PL/SQL packages, procedures or `.pls`/`.pkb` | `LANG-PLSQL-*` |
| `.html`, `.htm` | `LANG-HTML-*` |
| `.css`, `.scss`, `.less` | `LANG-CSS-*` |
| React, Vue, Angular, Svelte, Preact, Astro or Solid manifests/source | matching framework family |
| Bash, Zsh, Tcsh or shell scripts | `LANG-SHELL-*` |

For each detected family, report at least one outcome for every applicable rule: `PASS`, `FAIL`,
or `REVIEW_REQUIRED`. Include the command, benchmark, profile, query plan, network trace or test
that supports the outcome. When a framework is layered on JavaScript or TypeScript, apply both the
base `LANG-JS-*` rules and the framework rules.

## Review output

When auditing, group results by severity (blocking, important, improvement), cite the applicable
reference, and include a short measurement or verification plan. Do not optimise for a score at the
expense of security, correctness, resilience, or user needs.

## Repositories and CI

Before changing generated artefacts, locate the source of truth and its generator. Run the project's
tests, linters, and data validators. Add a regression test for a new rule when practical. Never
commit secrets, build caches, dependency directories, or local reports unless explicitly requested.

Read `references/criteria.md` for the compact mapping of RGESN, GR491, Opquast, and RGAA concerns,
and `references/rules.md` for the complete rule set.
