# Green Codex

[![Version](https://img.shields.io/github/v/release/Institut-du-Numerique-Responsable/green-codex?sort=semver)](https://github.com/Institut-du-Numerique-Responsable/green-codex/releases)
[![CI](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%2B%20CC%20BY%204.0%20%2B%20CC%20BY--SA%204.0-yellow.svg)](LICENSE)
[![INR](https://img.shields.io/badge/INR-Institut%20du%20Num%C3%A9rique%20Responsable-4CAF50?logo=leaf&style=flat)](https://institutnr.org/)

Green Codex is a Codex skill for applying Green IT and responsible digital practices while
designing, implementing, reviewing, or auditing software and digital services.

It distils guidance from RGESN, GR491, Opquast, and RGAA into a practical workflow for Codex.
The official acronyms are kept unchanged. It also includes scoped adaptations of the NR charter,
BP-AIR, the stakeholder maturity guide and RIA31. See the
[source inventory](green-codex/references/sources.md) for provenance and coverage limits.

The approach is presented on the INR website (in French):
[Écoconcevoir avec un assistant de code](https://institutnr.org/ecoconcevoir-avec-un-assistant-de-code).

The current package is version `1.0.0` (see [`VERSION`](VERSION)). Rule identifiers such as
`CODE-EFF-*` and `LANG-*` belong to this project; they are routing and engineering guidance, not
official criterion numbers or a compliance score.

## Expression in Codex and ChatGPT

Green Codex applies [expression and commit-message rules](green-codex/references/expression.md)
in every language. The skill loads this reference for every task. For ChatGPT, provide
the standalone instructions in that file as conversation context. Repository changes
do not update an account's instructions automatically. These are project editorial
conventions, with manual review of actual outputs required.

## What it covers

The [token sobriety rules](green-codex/references/token-sobriety.md) cover NR-TOK-001
through NR-TOK-030 for development agents, including Codex, Claude Code and Mistral Vibe.
They define mandatory safeguards, default recommendations, capability-dependent actions
and a concise session report. Token and cost savings require comparable measurements;
they do not establish environmental savings.

Réduire les tokens et les appels inutiles contribue au Numérique Responsable en
limitant les traitements mobilisés pour un même résultat, tout en préservant la qualité ;
le gain environnemental réel dépend du modèle, de l'infrastructure et de l'usage.

The [Codex application guide](green-codex/references/codex-token-sobriety.md) documents
targeted searches, stale evidence, compaction, cache, agent delegation, acceptance
criteria and measurement boundaries, with official sources and a worked example.

- digital and software eco-design;
- energy, data, storage, network, and infrastructure efficiency;
- accessible and resilient user interfaces;
- responsible use of AI, including model size, context, caching, and data minimisation;
- 14 responsible Codex usage practices for context, briefs, durable guidance, verification, and
  proportionate compute;
- evidence-based audits with severity, confidence, and verification steps;
- service utility, device longevity, inclusive access, retirement and rebound effects;
- reproducible measurement separating resource proxies, energy and modelled environmental impacts.

The catalogue also routes guidance for serverless and edge deployments, mobile and offline-first
services, IoT and embedded systems, distributed systems, NoSQL and data platforms, and the
following languages and frameworks: Java, Kotlin, Scala, Rust, C, C++, Go, Python, JavaScript,
TypeScript, PHP, Ruby, Julia, Nim, Zig, Shell, SQL, PL/SQL, HTML, CSS, React, Vue, Angular,
Svelte, Preact, Astro and Solid. Detection narrows the review; it does not make every rule
applicable to every file.

## How the NR rules are applied

Green Codex does not label a language, framework, cloud provider, or database as inherently
“green”. The Institut du Numérique Responsable (NR) practices are applied to the way a technology
is designed, configured and operated: useful functionality first, then lower CPU and memory work,
fewer requests and bytes, bounded storage, accessibility, security, and a documented lifecycle.

When the skill is used, Codex follows this sequence:

1. **Discover the scope.** It identifies the lifecycle stage, user impact, data flows, workload and
   technologies from source files, manifests, lockfiles and runtime configuration.
2. **Route the rules.** It applies the universal rules and every relevant family in
   [`green-codex/references/rules.md`](green-codex/references/rules.md): `CODE-*`, `API-*`,
   `WEB-*`, `DB-*`, `INFRA-*`, `OPS-*`, `NET-*`, `HW-*`, `AI-*`, `SERVICE-*`, `MEASURE-*`,
   applicable `ARCH-*`, and matching `LANG-*` rules.
   A React project therefore receives both `LANG-JS-*` and `LANG-REACT-*`; SQL and PL/SQL receive
   their respective rule sets.
3. **Turn guidance into action.** For each applicable rule, it proposes a concrete change or
   confirms that the current implementation is adequate. Examples include bounding pagination,
   removing unused returned columns, preventing N+1 queries, streaming large files, limiting retries, lazy
   loading media, or setting a data-retention period.
4. **Require evidence.** Each applicable rule assessed is reported as `PASS`, `FAIL`, or
   `REVIEW_REQUIRED` and includes the file and line (or service evidence), environmental or user
   impact, severity, confidence, and a verification
   method such as a test, benchmark, query plan, allocation profile, network trace or SCI estimate.
5. **Preserve responsible trade-offs.** No optimisation may weaken security, correctness,
   accessibility, resilience, privacy or user needs. A language change, cloud move or model
   reduction is recommended only when its benefit is demonstrated for the real workload.

Targeted changes receive targeted checks; full audits also document coverage and exclusions.
Project rule identifiers are not official criterion numbers. Selected RGESN mappings are recorded
with their edition in the criteria reference; this does not establish formal compliance.

## Responsible use of Codex

### Responsible AI charter

Start daily service assessments with [the 3U guide](green-codex/references/three-u.md):
**utile** (compare useful outcomes and correction effort with the current process),
**utilisé** (observe real use when the need occurs), and **utilisable** (observe
independent task completion, including accessible interaction). A few comparable
tasks, a voluntary usage tally and observed journeys can start this assessment.
Agree criteria for the service; there is no universal adoption target or combined
score. Without usage evidence, actual adoption stays `REVIEW_REQUIRED`.

The full charter remains a reference for relevant issues or an explicit charter
audit, not a mandatory checklist for every AI task.

For AI work, Green Codex also applies the INR/ISIT responsible AI charter through
[a dedicated reference](green-codex/references/responsible-ai-charter.md). It maps
the charter's sixteen commitments across four axes: people, inclusion and ethics,
trust, and environmental responsibility. Ten `AI-CHARTER-*` rules address the
first three axes; existing AI and measurement rules cover frugality and lifecycle.

Daily application is scoped to the task: check data and tool permissions for an
AI agent, source disclosure for a chatbot, human oversight for risky decisions,
or staff participation and training for a workplace rollout. A non-AI helper
does not trigger an organisational audit. Use `$green-codex` with a bounded request,
for example: "Review this AI support agent against the responsible AI charter;
identify affected commitments, evidence gaps and tests without changing anything."

Some product behaviours are testable automatically: tenant isolation, approval
bypass, retrieval failures and resource budgets. Accessibility journeys need
manual checks too; participation, training and purchasing commitments require
human evidence. Findings use `PASS`, `FAIL` or `REVIEW_REQUIRED` for their assessed
scope. Passing tests never certifies an organisation or compliance with the AI Act.
The [evaluation catalogue](evals/README.md) includes seven charter scenarios,
including a control against expanding a small unrelated task into a charter audit.

### Codex usage practices

When the task concerns Codex itself, the skill applies the 14 project-authored practices in
[`green-codex/references/usage-practices.md`](green-codex/references/usage-practices.md). They
cover relevant initial context, forks and task boundaries, deliberate compaction, the maintained
code map, complete briefs, bounded delegation, durable project guidance, proportionate
verification, model and reasoning selection, justified parallel work, and minimal non-interactive
runs. These practices are editorial guidance adapted to Codex, not personal advice attributed to
an individual.

## NR charter and additional guides

Select these references for the task being assessed; they are not a checklist to run in full:

- [NR charter](green-codex/references/nr-charter.md): five axes translated into concrete expectations
  for programming languages and natural-language tasks.
- [BP-AIR](green-codex/references/air-practices.md): architecture decisions adapted from 18 source fiches.
- [Stakeholder maturity](green-codex/references/stakeholder-maturity.md): evidence requests based on
  48 source questions, without reproducing the official scoring method.
- [RIA31](green-codex/references/ria31.md): adaptations of 41 questions observed on the source site;
  the reference explains the difference from the older 31-question document. RIA31 is distinct
  from the EU AI regulation.

An applicable check with missing evidence remains `REVIEW_REQUIRED`. Human decisions and actual
organisational adoption cannot be established by generated documents. For a simple text request,
use a short factual NR summary; no scanner or JSON record is required.

## Measurement and evidence

For comparisons or environmental claims, read the
[`measurement.md`](green-codex/references/measurement.md) protocol. It defines the useful task and
functional unit, equivalent baseline, measurement boundary, workload conditions, uncertainty and
lifecycle trade-offs. Resource proxies, token counts, latency and cost are not direct carbon
measurements. Where the SCI method is applicable, the report records operational and embodied
components, factors, allocation, period and uncertainty; missing evidence remains
`REVIEW_REQUIRED`.

Example finding:

```text
FAIL DB-EFF-001 at src/repository/users.sql:14
SELECT * transfers unused columns for every request.
Action: select the named fields required by the endpoint.
Verification: query test plus an EXPLAIN plan and response-size comparison.
```

Reported energy or carbon gains are never universal promises. A measurement must state its
workload, baseline, environment, method, duration and uncertainty. When hosted CI cannot provide
reliable energy data, the skill reports `REVIEW_REQUIRED` instead of inventing a result.

## Installation

For a first installation on macOS or Linux, with Git and Codex already installed,
clone this repository and open its root folder:

```bash
git clone https://github.com/Institut-du-Numerique-Responsable/green-codex.git
cd green-codex
```

Copy the `green-codex` directory into your personal skills directory. If the destination
already exists, inspect and back up your local changes before updating it; do not run
a first-install copy into an existing installation.

```bash
mkdir -p ~/.agents/skills
cp -R green-codex ~/.agents/skills/green-codex
```

Verify the copy with `ls ~/.agents/skills/green-codex/SKILL.md`. In Codex CLI or the IDE
extension, invoke `$green-codex` in your request. If the skill does not appear, restart
Codex. Personal skill discovery uses `~/.agents/skills` in the
[official documentation](https://learn.chatgpt.com/docs/build-skills).

Watch the [50-second installation walkthrough](https://institut-du-numerique-responsable.github.io/green-codex/#installation-video)
or read its transcript on the same page.

## Included files

- `green-codex/SKILL.md`: workflow and decision guidance;
- `green-codex/references/criteria.md`: compact criteria map and evidence checklist;
- `green-codex/references/measurement.md`: comparison protocol, evidence levels and carbon boundaries;
- `green-codex/references/responsible-ai-charter.md`: charter traceability, daily actions and evidence requirements;
- `green-codex/references/three-u.md`: small practical tests for utility, actual usage and usability;
- `green-codex/references/rules.md`: complete rules for frontend, backend, data,
  accessibility, web quality, responsible AI, modern architectures, operations and
  language/framework-specific guidance;
- `green-codex/references/usage-practices.md`: 14 project-authored practices adapted to Codex,
  with official sources for Codex-specific mechanisms;
- `green-codex/scripts/check_sobriety.py`: conservative static checks for selected high-confidence
  anti-patterns;
- `green-codex/scripts/nr_hook.py`: optional native summary check; install with `scripts/install_nr_hook.py`
  from the installed skill directory, then approve in Codex `/hooks`;
- `green-codex/scripts/nr_summary.py`: validates task records and renders the NR closing summary;
- `green-codex/references/closing-summary.md`: record format, command and integration limits;
- `green-codex/references/sources.md`: source inventory and provenance gaps;
- `green-codex/references/reuse-rights.md`: attribution and reuse conditions;
- `green-codex/scripts/run_evals.py`: separate format checks and hash-bound semantic reviews;
- `evals/cases.json`: realistic behavioral evaluation scenarios;
- `evals/README.md`: procedure for running evaluations against saved Codex responses;
- `green-codex/agents/openai.yaml`: UI metadata for skill discovery.

Run the package smoke test and the Codex skill validator before publishing changes:

```bash
python3 green-codex/scripts/test_skill.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py green-codex
```

### Automated sobriety checks

The repository includes a dependency-free static checker for high-confidence anti-patterns. It
reports SQL `SELECT *`, media autoplay and unbounded JavaScript polling, with file and line
references. It intentionally stays conservative: a clean scan is not a compliance claim, and
performance, energy, accessibility and architecture still require targeted tests or measurements.

```bash
python3 green-codex/scripts/test_sobriety.py
python3 green-codex/scripts/check_sobriety.py --path .
python3 green-codex/scripts/check_sobriety.py --path . --format json
```

The same checks run in the `validate` GitHub Actions workflow. Project-specific thresholds and
additional rules should be added only with a regression test and documented evidence.

### End-of-task NR summary

Every task using the skill now requests a concise explanation of the NR actions taken,
with rule IDs, user benefits, evidence and unresolved checks. For automation, use
`green-codex/scripts/nr_summary.py` with a current task record and explicit scan scope.
It validates the record and reruns the three static checks; it does not certify the other rules.
See [record format, command and hook integration](green-codex/references/closing-summary.md).
An optional native hook checks summary structure and requests at most one correction.
Install it explicitly from the persistent skill directory, then review and trust its two
entries in Codex `/hooks`; copying the skill alone does not enable it. See the linked guide
for detection limits, installation, verification and removal.

## Use and contribution

Use the skill for audits, code reviews, architecture decisions, and implementation work. Findings
must distinguish observed evidence from recommendations and must not trade away security,
correctness, accessibility, or resilience for an environmental score.

Issues and pull requests are welcome in the [GitHub repository](https://github.com/Institut-du-Numerique-Responsable/green-codex).
See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Release process

The version is stored in `VERSION` and must match the release tag (`vX.Y.Z`). Run both validation
commands, update `CHANGELOG.md`, and create a GitHub release from the tag. See the CI workflow for
the checks executed on every pull request.

## License

Code and test scripts are Apache-2.0 licensed. Documentation and rule content are available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), except explicitly marked
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) adaptations. See [LICENSE](LICENSE) and
[LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0).

The token sobriety references inspired and adapted from Caveman are Apache-2.0 licensed.
See [third-party attribution](green-codex/references/third-party-attributions.md)
for Julius Brussee's copyright, INR modifications, independence and provenance limits.

## Team

Green Codex is maintained by a core team at the Institut du Numérique Responsable (INR):

| Name | GitHub | Role |
|------|-------|------|
| Guillaume Gallon | [@gridboy](https://github.com/gridboy) | Maintainer |
| Guillaume Bourgeois | [@bourgeoisguillaume01-glitch](https://github.com/bourgeoisguillaume01-glitch) | Maintainer |
| Vincent Courboulay | [@vincentcourboulay](https://github.com/vincentcourboulay) | Maintainer |

See [AUTHORS.md](AUTHORS.md) for the full contributor list.

## Additional INR references and reuse

The skill includes scoped adaptations of the NR charter (5 axes), BP-AIR (18 fiches),
the stakeholder maturity guide (48 questions) and the live RIA31 (41 visible questions).
Each instruction links to its source and specifies an action and evidence. The new IDs
are accepted by the end-of-task summary command; static scanner coverage remains unchanged.
See [source inventory](green-codex/references/sources.md) and
[reuse rights](green-codex/references/reuse-rights.md). BP-AIR, stakeholder and RIA31
adaptations are explicitly CC BY-SA 4.0; rewriting does not waive source licence terms.

## Sources

See the [complete documented source inventory and provenance gaps](green-codex/references/sources.md).

- [Charte IA responsable — INR/ISIT](https://charter.isit-europe.org/charte-ia/?lang=fr_FR)

- [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/)
- [GR491](https://gr491.isit-europe.org/)
- [Opquast](https://checklists.opquast.com/fr/qualite-numerique/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)
- [SCI specification](https://sci.greensoftware.foundation/)
- [Codex CLI command reference](https://developers.openai.com/codex/cli/reference)
- [Codex guidance for `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md)
- [OpenAI prompting guidance](https://learn.chatgpt.com/docs/prompting)
- [OpenAI best practices](https://learn.chatgpt.com/guides/best-practices)
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5)

Green Codex is a reusable engineering guide, not a replacement for the official referentials or
for a formal compliance audit. The project records checked editions where relevant, but teams
should verify current versions and document their own evidence before making a formal claim.

## Website and discoverability

The project website is published from [`docs/`](docs/) with a lightweight, accessible landing page,
structured metadata, a sitemap, `robots.txt`, and an `llms.txt` summary for search engines and AI
assistants:

<https://institut-du-numerique-responsable.github.io/green-codex/>

## Verification limits and practical scope

The 3U starts with a confirmed need. Technical AI work uses efficiency rules;
charter sections are read for explicit assessments or identified risks. Inspection
can suffice for simple changes; benchmarks resolve material uncertainty. Rule
aliases preserve existing identifiers without requiring duplicate findings.

The scanner excludes direct SQL existence tests from excess-projection findings.
JSX/TSX comments and string examples are masked; template media requires review
because this scanner is not a JavaScript/Vue compiler. A clean scan cannot prove
all runtime behaviour.

Evaluation output separates `FORMAT` from `SEMANTIC`. Keyword matches alone never
validate reasoning; `--strict-format` also requires literal identifiers and terms.
See [evaluation instructions](evals/README.md) and the
[audit and correction record](docs/audit-skill-2026-09-14.md).
