# Green IT criteria quick reference

This is a routing aid, not a replacement for the official referentials.

All `*-EFF-*` and `LANG-*` identifiers belong to this project. A thematic mapping is not evidence
that an official criterion is satisfied. For formal assessments, record the edition, exact
criterion, applicability, test procedure and evidence; consult the official text before deciding.

## RGESN

Use for the environmental design of digital services: user need and scope, functional sobriety,
content and media, frontend performance, backend and data, infrastructure, and lifecycle. Check
that the recommendation is evidenced by the project rather than inferred from a framework name.

## GR491

Use for software and service design decisions across the lifecycle: needs, architecture, UX,
frontend, backend, data, hosting, and governance. Prefer the most specific recommendation and
record the trade-off when an optimisation affects accessibility or resilience.

## Opquast

Use for web quality and user-facing robustness: understandable content, reliable navigation,
forms and errors, security basics, responsive behaviour, and accessible presentation. Opquast is
complementary to environmental criteria.

## RGAA

Use for accessibility verification. Preserve the acronym RGAA and identify the applicable version.
Check keyboard access, focus visibility, semantic structure, alternative text, contrast, labels,
errors, language, zoom/reflow, and media alternatives. A green IT change is not acceptable if it
removes an accessibility feature.

## Evidence checklist

- transfer size and request count before and after;
- CPU, memory, storage, and energy proxy where measurable;
- cacheability, compression, image and video dimensions;
- lifecycle and data-retention assumptions;
- keyboard and screen-reader behaviour;
- test command and result, with date and environment.

For comparative claims, read [measurement.md](measurement.md): functional unit, equivalent baseline,
measurement boundary, uncertainty, period totals and lifecycle trade-offs.

## Verified RGESN routing anchors

Checked 2026-09-05 against [RGESN 2024, version 2](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/).
These are selected anchors, not an exhaustive crosswalk or a compliance score.

| Official criterion | Project guidance to consult |
| --- | --- |
| 1.1–1.2: utility and actual user needs | `SERVICE-EFF-001` |
| 1.3–1.4: ownership and regular review | `SERVICE-EFF-004` |
| 1.5: environmental objectives | `MEASURE-EFF-003`, `MEASURE-EFF-004` |
| 2.1: user hardware profiles | `SERVICE-EFF-002` |
| 4.1: automatic playback disabled | `WEB-EFF-004` |
| 6.1: screen weight and request limits | `API-EFF-002`, `WEB-EFF-002`, `NET-EFF-001` |

Consult other criteria when relevant rather than inferring full coverage from this table. GR491,
Opquast and RGAA remain complementary sources with their own assessment methods; no equivalence
between their scores or requirements is implied.

Official sources: [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/), [GR491](https://gr491.isit-europe.org/), [Opquast](https://checklists.opquast.com/fr/qualite-numerique/), and [RGAA](https://accessibilite.numerique.gouv.fr/).
