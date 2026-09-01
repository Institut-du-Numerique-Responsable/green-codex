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
- evidence-based audits with severity, confidence, and verification steps.

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
- `green-codex/references/rules.md`: complete English rules for frontend, backend, data,
  accessibility, web quality, and responsible AI;
- `green-codex/agents/openai.yaml`: UI metadata for skill discovery.

Run the package smoke test and the Codex skill validator before publishing changes:

```bash
python3 green-codex/scripts/test_skill.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py green-codex
```

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
