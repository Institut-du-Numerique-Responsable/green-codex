# Green Codex

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

## Sources

- [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/)
- [GR491](https://gr491.isit-europe.org/)
- [Opquast](https://checklists.opquast.com/fr/qualite-numerique/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)

Green Codex is a reusable engineering guide, not a replacement for the official referentials or
for a formal compliance audit. Teams should always verify the current versions and document their
evidence.
