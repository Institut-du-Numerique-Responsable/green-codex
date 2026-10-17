# Rule sources and provenance

Inventory of the sources explicitly documented in the repository, audited 2026-10-17.
This is not proof of the complete historical input used to generate every rule. The initial 183 identified rules/practices comprised 159 in `rules.md`, 14 Codex usage
practices and 10 operational AI charter rules. The INR extension adds 112 identified
instructions (5 NR charter, 18 AIR, 48 stakeholder and 41 RIA31), for 295 project IDs.
The new licensed adaptations are attributed in their respective files. Some are aliases. These are not official criterion numbers.

## Environmental design, quality and inclusion

| Documented source | Role in the skill | Traceability available |
| --- | --- | --- |
| [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/) | Service needs, ecodesign, frontend/backend, infrastructure, lifecycle | `criteria.md` records RGESN 2024 v2, checked 2026-09-05, with selected numbered anchors. No complete rule-by-rule crosswalk. |
| [GR491 — INR/ISIT](https://gr491.isit-europe.org/) | Lifecycle, needs, architecture, UX, software, hosting, governance | Thematic mapping in `criteria.md`; no pinned edition or exact source criterion for each rule. |
| [Opquast](https://checklists.opquast.com/fr/qualite-numerique/) | Web quality, content, navigation, forms, robustness | Complementary source; edition and individual source criteria not recorded. |
| [RGAA](https://accessibilite.numerique.gouv.fr/) | Accessibility safeguards | Complementary source; applicable edition and individual tests must be identified for each audit. |
| [Software Carbon Intensity specification](https://sci.greensoftware.foundation/) | Functional units, operational and embodied emissions, measurement boundaries | `measurement.md` cites the web specification; not a complete lifecycle assessment or automatic carbon calculator. |
| [Charte IA responsable — INR/ISIT](https://charter.isit-europe.org/charte-ia/?lang=fr_FR) | Human, ethical, trustworthy and environmentally responsible AI | `responsible-ai-charter.md` maps 16 commitments to 10 project rules. It records a private template inspection on 2026-09-14, commit `a2d10fe3ff5cdbe25772bbc3cd2857bf618b4acf`, and a public HTTP 403 then. Public reproducibility is limited; no numbered edition recorded. |

These are the links and historical verification statements recorded by the project; this
inventory does not claim all current editions were rechecked on the inventory date.

## Codex usage practices

`usage-practices.md` documents these five primary references:

1. [Codex CLI reference](https://developers.openai.com/codex/cli/reference): commands and execution modes.
2. [Codex AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md): instruction hierarchy and scope.
3. [OpenAI prompting guidance](https://learn.chatgpt.com/docs/prompting): objectives, context, constraints and verification.
4. [OpenAI best practices](https://learn.chatgpt.com/guides/best-practices): task context and proportionate reasoning effort.
5. [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5): evaluation, caching and retained task state. This is a version-dependent model reference, not a universal environmental standard.

The 14 practices adapt an earlier Green Claude checklist, as stated in `usage-practices.md`.
The repository does not pin that predecessor's source/version here, so that historical
lineage cannot be reconstructed completely from these files. They are editorial practices,
not quotations attributable to a named person.

## Editorial rules and missing provenance

The language/framework and architecture recommendations, universal engineering safeguards,
and practical 3U test procedure are project synthesis. No separate primary reference is
recorded for every recommendation. Do not manufacture citations or equate thematic similarity
with derivation. The 3U guide is linked to service rules and the charter, without an independent
bibliographic origin recorded for the method itself.

For stronger traceability, add to each rule when verified: source URL, edition/date, exact
criterion or section, adaptation rationale and evidence method. Until then, keep its origin
labelled project-authored and any official mapping explicitly partial.

## New execution mechanism (not an original rule source)

[Codex hooks](https://developers.openai.com/codex/hooks) was consulted on 2026-10-17 for the
integration notes in `closing-summary.md`. It describes runtime integration, not NR criteria.

## INR extension added on 2026-10-17

| Source | Verified material and adaptation |
| --- | --- |
| [Charte NR](https://charter.isit-europe.org/?lang=fr_FR) | Five public axes; [nr-charter.md](nr-charter.md). Distinct from the AI charter. |
| [BP-AIR](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/tree/f7b0f6b) | 18 fiches at revision `f7b0f6b`; [air-practices.md](air-practices.md), CC BY-SA 4.0. Work-in-progress status retained. |
| [Stakeholder guide](https://github.com/Institut-du-Numerique-Responsable/guide-maturite-parties-prenantes/tree/d28bdfc) | Version 1.2, revision `d28bdfc`, 48 questions across ten families; [stakeholder-maturity.md](stakeholder-maturity.md), CC BY-SA 4.0. |
| [RIA31](https://ref-ia.isit-europe.org/) | 41 questions observed in the live browser, 13 recommendations, five families; [ria31.md](ria31.md). PDF v1.21 (June 2024) still states 31. Licence indications differ; both recorded. |

Each new consigne has a source pointer and an evidence request. The 48 stakeholder questions
and 41 RIA31 questions are covered at question level, not every weighted subcriterion or detailed
assessment procedure. The adaptation does not claim equivalence with their official scores.

[Opquast reuse terms](https://checklists.opquast.com/fr/qualite-numerique/licence/) were checked
on 2026-10-17: CC BY-SA 4.0. See [reuse-rights.md](reuse-rights.md). A thematic reference does
not prove exact derivation, and paraphrasing is not a licence exemption.

The language and natural-language matrix in `nr-charter.md` is a Green Codex editorial
application of the five charter axes, not a set of language requirements issued by INR.
It reuses existing rule IDs and distinguishes Codex checks from human evidence.
