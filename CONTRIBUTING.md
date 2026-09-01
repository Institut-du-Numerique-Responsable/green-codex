# Contributing to Green Codex

Thank you for helping improve Green Codex. Contributions should make the guidance clearer,
more evidence-based, and easier to apply across projects.

## Workflow

1. Open an issue for a new rule, a correction, or a change with a broad impact.
2. Create a focused branch from `main`.
3. Edit the source skill and its references. Keep generated or local artefacts out of commits.
4. Run the checks locally:

   ```bash
   python3 green-codex/scripts/test_skill.py
   python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py green-codex
   ```

5. Open a Pull Request with the scope, evidence, and any trade-offs for accessibility or
   performance.

## Rule changes

Every new rule should identify its intended audience, avoid unverifiable claims, and cite the
official source when it refers to RGESN, GR491, Opquast, or RGAA. Keep official acronyms unchanged.

## Pull Requests

One coherent change per PR is preferred. CI must pass and at least one CODEOWNER review is required
before merging. Do not include secrets, generated caches, personal data, or unrelated formatting.

## Licensing

By contributing, you agree that your contributions are distributed under the project licences:
MIT for executable code and CC BY 4.0 for documentation and rule content, unless a file states
otherwise.
