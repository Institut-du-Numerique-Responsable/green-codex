# Green Codex

[![Version](https://img.shields.io/github/v/release/Institut-du-Numerique-Responsable/green-codex?sort=semver)](https://github.com/Institut-du-Numerique-Responsable/green-codex/releases)
[![CI](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-yellow.svg)](LICENSE)

Green Codex is a Codex skill for applying Green IT and responsible digital practices while
designing, implementing, reviewing, or auditing software and digital services.

It distils guidance from RGESN, GR491, Opquast, and RGAA into a practical workflow for Codex.
The official acronyms are kept unchanged.

## What it covers

- digital and software eco-design;
- energy, data, storage, network, and infrastructure efficiency;
- accessible and resilient user interfaces;
- responsible use of AI, including model size, context, caching, and data minimisation;
- 14 responsible Codex usage practices for context, briefs, durable guidance, verification, and
  proportionate compute;
- evidence-based audits with severity, confidence, and verification steps.

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
   `WEB-*`, `DB-*`, `INFRA-*`, `OPS-*`, `NET-*`, `HW-*`, `AI-*`, and the matching `LANG-*` rules.
   A React project therefore receives both `LANG-JS-*` and `LANG-REACT-*`; SQL and PL/SQL receive
   their respective rule sets.
3. **Turn guidance into action.** For each applicable rule, it proposes a concrete change or
   confirms that the current implementation is adequate. Examples include bounding pagination,
   removing `SELECT *`, preventing N+1 queries, streaming large files, limiting retries, lazy
   loading media, or setting a data-retention period.
4. **Require evidence.** Every rule is reported as `PASS`, `FAIL`, or `REVIEW_REQUIRED` and includes
   the file and line, environmental or user impact, severity, confidence, and a verification
   method such as a test, benchmark, query plan, allocation profile, network trace or SCI estimate.
5. **Preserve responsible trade-offs.** No optimisation may weaken security, correctness,
   accessibility, resilience, privacy or user needs. A language change, cloud move or model
   reduction is recommended only when its benefit is demonstrated for the real workload.

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

Copy the `green-codex` directory into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R green-codex ~/.codex/skills/green-codex
```

The skill is then available when Codex selects it automatically, or explicitly with `$green-codex`.

## Included files

- `green-codex/SKILL.md`: workflow and decision guidance;
- `green-codex/references/criteria.md`: compact criteria map and evidence checklist;
- `green-codex/references/rules.md`: complete rules for frontend, backend, data,
  accessibility, web quality, and responsible AI;
- `green-codex/references/usage-practices.md`: 14 project-authored practices adapted to Codex,
  with official sources for Codex-specific mechanisms;
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

Code and test scripts are MIT licensed. Documentation and rule content are available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE) and
[LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0).

## Sources

- [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/)
- [GR491](https://gr491.isit-europe.org/)
- [Opquast](https://checklists.opquast.com/fr/qualite-numerique/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)

Green Codex is a reusable engineering guide, not a replacement for the official referentials or
for a formal compliance audit. Teams should always verify the current versions and document their
evidence.

## Website and discoverability

The project website is published from [`docs/`](docs/) with a lightweight, accessible landing page,
structured metadata, a sitemap, `robots.txt`, and an `llms.txt` summary for search engines and AI
assistants:

<https://institut-du-numerique-responsable.github.io/green-codex/>
