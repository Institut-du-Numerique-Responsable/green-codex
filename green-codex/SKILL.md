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

1. Establish the requested scope: targeted change, review, or service-wide audit. Reuse known user
   needs and project budgets; do not turn a small edit into a full audit or remove functionality
   without authorisation. Inspect only relevant files and project guidance.
2. For design or a service audit, evaluate necessity, reuse and simpler alternatives first. Then
   assess equipment longevity and likely lifecycle hotspots before micro-optimising code.
3. Select applicable families below and in `references/criteria.md`. Rule IDs are project-authored,
   not official criterion numbers. Read only relevant sections of `references/rules.md` using its
   headings or identifier prefixes; do not load unrelated languages or architectures.
4. Establish a representative baseline and a useful functional unit (e.g. one completed search).
   For resource comparisons, carbon claims or material optimisations, read
   `references/measurement.md`. Missing measurements mean unknown gains, not zero impact.
5. Prioritise observed hotspots by expected total benefit, confidence, implementation cost and
   regression risk. Prefer reversible changes. Preserve accessibility, privacy, security,
   correctness and resilience; measure transfers between client, network and server costs.
6. Verify the affected behaviour and compare the agreed budgets. For each applicable rule assessed,
   report `PASS`, `FAIL`, or `REVIEW_REQUIRED` with evidence. A tool's clean result proves only its
   narrow checks. Run `scripts/check_sobriety.py` relative to this skill directory with an explicit
   `--path` pointing to the project under review when its static checks are relevant.

## Scope rule routing

| Scope | Sections/families in `references/rules.md` |
| --- | --- |
| Service design or full audit | Universal rules, `SERVICE-*`, then relevant rows below |
| Device support, inclusion, engagement or lifecycle review | Relevant `SERVICE-*`; retirement also `DB-EFF-005`, `OPS-EFF-001` |
| Runtime, APIs, data | `CODE-*`, `API-*`, `DB-*`, matching languages |
| User journeys, content, web | `WEB-*`, `NET-*`, Web quality and accessibility, matching languages/frameworks |
| Infrastructure, procurement, operation | `INFRA-*`, `OPS-*`, `HW-*`, `NET-*` |
| AI features or inference | `AI-*`, Responsible AI, `CODE-*`, `MEASURE-*` |
| Resource or environmental comparison | `MEASURE-*`, `CODE-EFF-012`, `references/measurement.md` |
| Serverless, edge, mobile, IoT, embedded, distributed, NoSQL, data platforms | Matching `ARCH-*` sections plus relevant rows above |

In a full audit, list the assessed families, exclusions with reasons, and evidence gaps. Outside
that mode, report affected rules and material findings only; do not enumerate the entire catalogue.

## Responsible use of Codex itself

When the request concerns Codex context, prompts, tasks, agents, models, reasoning effort,
automation, or instruction files, read and apply `references/usage-practices.md`. It contains 14
project-authored practices adapted to Codex. Do not load that reference for an ordinary code audit
unless Codex usage is also in scope.

## Responsible use of Codex itself

When the request concerns Codex context, prompts, tasks, agents, models, reasoning effort,
automation, or instruction files, read and apply `references/usage-practices.md`. It contains 14
project-authored practices adapted to Codex. Do not load that reference for an ordinary code audit
unless Codex usage is also in scope.

## Language rule routing

Detect the languages and frameworks from file extensions, build manifests, lockfiles and runtime
configuration before reviewing code. Read and apply each in-scope matching `LANG-*` section in
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

Detection alone does not make every rule applicable: browser DOM rules do not apply to a Node-only
worker, for example. Include the command, benchmark, profile, query plan, network trace or test
supporting each assessed outcome. For JavaScript/TypeScript frameworks, apply both the relevant
base `LANG-JS-*` rules and framework rules.

## Review output

When auditing, give scope and limitations, then prioritised findings: rule/status, file:line or
service evidence, observation, impact, confidence, action, and verification. Close with remaining
measurement gaps and next actions. Distinguish technical efficiency from environmental impact;
never convert an EcoIndex, Lighthouse score or a clean scan into RGESN/RGAA compliance.

## Source attribution

Treat project-authored guidance as project guidance. A named person's advice, a quotation, or a
claim about a product's authorship requires a verifiable primary source linked to the exact claim.
If no primary source is available, remove the attribution and quotation marks instead of presenting
an editorial recommendation as someone else's words. Verify version-dependent commands and product
behavior in current official documentation.

## Repositories and CI

Before changing generated artefacts, locate the source of truth and its generator. Run the project's
tests, linters, and data validators. Add a regression test for a new rule when practical. Never
commit secrets, build caches, dependency directories, or local reports unless explicitly requested.

Read `references/criteria.md` for the compact mapping of RGESN, GR491, Opquast, and RGAA concerns,
`references/rules.md` for the complete software rule set, and `references/usage-practices.md` when
the responsible use of Codex itself is in scope.
