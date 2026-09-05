# Code map

- `green-codex/SKILL.md` — entrypoint and workflow for applying the skill.
- `green-codex/references/criteria.md` — compact mapping to RGESN, GR491, Opquast and RGAA.
- `green-codex/references/measurement.md` — evidence levels, reproducible comparisons and SCI boundaries.
- `green-codex/references/usage-practices.md` — conditional guidance on responsible Codex usage.
- `green-codex/references/rules.md` — English rules, including enforceable sobriety checks.
- `green-codex/scripts/test_skill.py` — deterministic package smoke tests.
- `green-codex/scripts/check_sobriety.py` — static anti-pattern scanner; `test_sobriety.py` tests it.
- `green-codex/scripts/run_evals.py` — lexical screening of responses; `test_evals.py` validates cases.
- `evals/cases.json` — behavioral scenarios, expected rules and semantic review checks.
- `evals/README.md` — evaluation procedure and limits.
- `green-codex/agents/openai.yaml` — Codex UI metadata and invocation information.
- `.github/workflows/validate.yml` — CI validation and release checks.
- `scripts/verify-version-release.sh` — VERSION/tag consistency check.
- `docs/index.html` — public documentation landing page.
