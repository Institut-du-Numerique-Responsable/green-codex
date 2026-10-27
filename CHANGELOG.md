# Changelog

## Unreleased

### Green Claude alignment

- Map all 277 Green Claude 1.5.0 rules to Green Codex in `green-claude-mapping.md`: covered,
  rewritten or adapted to Codex. No rule had to be excluded.
- Add 63 rewritten rules and practices, including the new `LANG-CSHARP-*` and `LANG-SWIFT-*`
  families, `CODE-EFF-017` for event-driven waiting and `USAGE-CODEX-BRIEF-03`.
- Widen the skill trigger to file formats, network requests, assets, loops, caching,
  pagination, dependencies and framework or model choices, and add default sobriety reflexes.
- Add `test_green_claude_mapping.py` to CI.

### Installation walkthrough

- Add a silent, locally generated 50-second installation video with native playback
  controls, no autoplay or preloading, and an accessible command transcript.
- Align first-install instructions with the documented personal skills location
  `~/.agents/skills`, include prerequisites and distinguish the Codex prompt from shell commands.


### Site Green Codex

- Rework the landing page around the INR identity, with a local INR logo, blue and
  teal palette, French content and direct access to installation, rules and evidence.
- Keep the page static with no JavaScript or remote fonts; add responsive layouts,
  a skip link and visible keyboard focus. Include token sobriety and licence updates.

### Third-party attribution

- Credit Julius Brussee and Caveman for inspiration and adapted token sobriety rules.
  Preserve the copyright, Apache-2.0 terms, INR modification notice and independence
  statement in the packaged references, NOTICE and license scopes. Document the
  consulted upstream revision and the remaining source-version provenance gap.

### Token sobriety

- Clarify evidence freshness, safe compression, targeted edits, dependency ordering,
  required checks and stopping conditions. Document Codex-specific application with
  verified CLI capabilities, source links and complete-task measurement boundaries.

- Add NR-TOK-001 through NR-TOK-030 for development agents, with mandatory rules,
  default recommendations and capability-dependent model, cache and measurement actions.
- Connect the skill and closing summary to the shared reference, preserve existing
  Codex practice identifiers and avoid counting overlapping savings twice.
- Register NR-TOK identifiers in the summary validator and verify catalogue coverage
  and CLI acceptance. Token and cost metrics remain externally supplied evidence.

### Expression and commit messages

- Add shared editorial instructions for Codex and ChatGPT in every language, with
  direct wording, prohibited rhetorical constructions and no Unicode U+2014 character.
- Require commit messages to explain the change and its reason, record actual
  verification, and match the committed diff, including merge and squash messages.
- Route the skill and repository guidance to the shared reference and document manual
  reuse in ChatGPT. Model adherence still requires review of actual responses.

### NR rules, reporting and hooks

- Add the five NR charter axes, 18 BP-AIR practices, 48 stakeholder maturity questions
  and 41 questions observed on the RIA31 site. Document source versions, coverage limits
  and the difference between RIA31 and the EU AI regulation.
- Record attribution and reuse terms, including CC BY-SA 4.0 for the three adapted guides.
  Clarify that paraphrasing does not remove licence duties.
- Translate charter expectations into actions for programming languages and natural-language
  tasks. Separate verifiable checks, missing evidence, human decisions and exclusions.
- Consolidate overlapping rules without breaking existing identifiers or counting findings twice.
- Add the portable NR summary command, with task records, evidence pointers and fresh static findings.
- Add optional UserPromptSubmit and Stop hooks to check summary structure and request at most
  one correction. Provide an installer with configuration backup and require Codex trust review.
  The hook does not authenticate evidence; implicit use without recognised signals is not detected.
- Expand the evaluation catalogue from 25 to 33 scenarios and add tests for reference coverage,
  summary records and hook behaviour. Catalogue validation does not prove model performance.
- Update the README, public site and assistant summary; remove unsupported percentage savings.
- Complete contribution and evaluation instructions, with diagrams explaining verification boundaries.

### Earlier changes pending release

- Fix SQL existence-test and JSX example false positives; template media requires review.
- Separate evaluation format checks from bound semantic verdicts, with optional strict mode.
- Make verification proportional, consolidate three aliases and clarify 3U/charter routing.
- Add counterexamples and specific semantic criteria to all evaluation scenarios.

- Start service assessments with realistic 3U tests (utile, utilisé, utilisable);
  keep the full AI charter as an on-demand reference rather than a daily checklist.

- Map the INR/ISIT responsible AI charter to scoped daily actions, ten human,
  ethical and trust rules, and existing environmental rules.
- Add seven behavioural scenarios for charter application and evidence limits,
  including a control against unnecessary organisational audits.

- Require primary sources for named attributions and quotations in skill guidance.
- Add 14 responsible-use practices adapted to Codex, without unsupported personal attribution.

## 1.0.0 - 2026-09-01

- Initial Green Codex skill package.
- Green IT rules covering RGESN, GR491, Opquast, and RGAA.
- Deterministic package smoke tests and GitHub Actions validation.
- Contribution, security, and code of conduct documentation.
