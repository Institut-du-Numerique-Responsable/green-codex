---
name: green-codex
description: Apply Green IT and responsible digital practices when designing, coding, reviewing, or auditing software and digital services, or answering natural-language requests about responsible digital practices.
---

# Green Codex

Use this skill when a request concerns eco-design, digital sobriety, accessibility, responsible
AI, sustainable software, or an environmental audit of code or a digital service.

Assess actual usage and evidence; no technology is inherently “green”. Preserve accessibility,
privacy, security and correctness. Do not infer environmental savings from a tool score.

## Working method

1. Establish the requested scope: targeted change, review, or service-wide audit. Reuse known user
   needs and project budgets; do not turn a small edit into a full audit or remove functionality
   without authorisation. Inspect only relevant files and project guidance.
2. For design or a service audit, start with the 3U: useful, actually used, and usable
   (`references/three-u.md`). Reuse evidence and choose small realistic tests against the
   current or simpler alternative. Then assess longevity and likely lifecycle hotspots.
3. Select applicable families below and in `references/criteria.md`. Rule IDs are project-authored,
   not official criterion numbers. Read only relevant sections of `references/rules.md` using its
   headings or identifier prefixes; do not load unrelated languages or architectures.
4. For resource comparisons, carbon claims or material optimisations, establish a representative
   baseline and functional unit using `references/measurement.md`. A simple edit or explanation
   needs no benchmark. Missing measurements mean unknown gains, not zero impact.
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
| Service design, value, adoption, usability or 3U assessment | `references/three-u.md`, `SERVICE-EFF-001`, `SERVICE-EFF-006`, then affected rules |
| Device support, inclusion, engagement or lifecycle review | Relevant `SERVICE-*`; retirement also `DB-EFF-005`, `OPS-EFF-001` |
| Runtime, APIs, data | `CODE-*`, `API-*`, `DB-*`, matching languages |
| User journeys, content, web | `WEB-*`, `NET-*`, Web quality and accessibility, matching languages/frameworks |
| NR charter, practical code/language expectations, natural-language tasks or organisational responsibility | `references/nr-charter.md`; use its applicability matrix and select affected axes only |
| Architecture programme or BP-AIR assessment | `references/air-practices.md`; source fiche IDs route to `AIR-*` |
| Supplier/partner maturity or procurement preparation | `references/stakeholder-maturity.md`; `STAKE-*`, not a contract or certification |
| Explicit RIA31 review or affected AI lifecycle risk | `references/ria31.md`; `RIA-*` operational adaptations, select affected stages |
| Infrastructure, procurement, operation | `INFRA-*`, `OPS-*`, `HW-*`, `NET-*` |
| Technical AI inference or resource optimisation | Relevant `AI-EFF-*`, `CODE-*`, `MEASURE-*`; no automatic organisational audit |
| Explicit charter assessment or identified AI rights, data, source or oversight risk | Affected sections of `references/responsible-ai-charter.md` |
| Resource or environmental comparison | `MEASURE-*`, `CODE-EFF-012`, `references/measurement.md` |
| Serverless, edge, mobile, IoT, embedded, distributed, NoSQL, data platforms | Matching `ARCH-*` sections plus relevant rows above |

In a full audit, list the assessed families, exclusions with reasons, and evidence gaps. Outside
that mode, report affected rules and material findings only; do not enumerate the entire catalogue.

## Applicability gate

Before applying a rule, identify its trigger in the current task and the evidence available:

- **Outside scope:** omit it from execution; explain exclusions in a full audit. Never count it as PASS.
- **Applicable and verifiable:** perform the authorised check; report the result and its exact scope.
- **Applicable but inaccessible:** report REVIEW_REQUIRED and the missing evidence; do not exclude
  a relevant rule merely because its tools, environment or documents are unavailable.
- **Human decision:** prepare the analysis when requested. Do not claim signature, certification,
  purchasing decisions, actual training or organisational adoption from generated documents.

For charter application and natural-language tasks, select the matching rows in
`references/nr-charter.md`. For Codex prompts, context, models, agents or automation, use
`references/usage-practices.md` only for capabilities available in the actual host.
A simple answer needs no static scan, JSON record or organisational audit. Required research
and accuracy checks still apply. A rule's missing proof is not evidence of a violation.

## Language rule routing

Detect the languages and frameworks from file extensions, build manifests, lockfiles and runtime
configuration before reviewing code. Read and apply each in-scope matching `LANG-*` section in
`references/rules.md`; do not substitute a generic rule when a language-specific rule exists.

Use the language/framework matrix in `references/nr-charter.md` when concrete expectations
are needed. For a language without a dedicated family, use applicable generic rules and
state that limitation; never invent a `LANG-*` identifier.

Detection alone does not make every rule applicable: browser DOM rules do not apply to a Node-only
worker, for example. Include the command, benchmark, profile, query plan, network trace or test
supporting each assessed outcome. For JavaScript/TypeScript frameworks, apply both the relevant
base `LANG-JS-*` rules and framework rules.

## Review output

When auditing, give scope and limitations, then prioritised findings: rule/status, file:line or
service evidence, observation, impact, confidence, action, and verification. Close with remaining
measurement gaps and next actions. Distinguish technical efficiency from environmental impact;
never convert an EcoIndex, Lighthouse score or a clean scan into RGESN/RGAA compliance.

## Closing summary for every task

Before the final response, summarise all NR actions actually performed during this task:
rule IDs, concrete action, user benefit, and verification evidence. Distinguish applied actions,
remaining FAIL/REVIEW_REQUIRED items and unmeasured gains. If no NR action was applicable,
say so briefly. Use the user's language and keep the detail proportional to the task.
For a repeatable end-of-run check or audit record, follow `references/closing-summary.md`
and run `scripts/nr_summary.py` with the current task record and explicit scan scope.
A successful static scan alone never means all rules were applied.
When the optional NR hook is configured, label the summary `Bilan NR` or `NR summary`
and use `Action:`, `Intérêt:`/`Benefit:`, `Preuve:`/`Evidence:` and `Limites:`/`Limits:`
with the applicable IDs. If none applies, use `NR: non applicable — reason` under that heading.
This structure lets the hook detect missing fields; it does not authenticate evidence.

## Source attribution

Treat project-authored guidance as project guidance. A named person's advice, a quotation, or a
claim about a product's authorship requires a verifiable primary source linked to the exact claim.
If no primary source is available, remove the attribution and quotation marks instead of presenting
an editorial recommendation as someone else's words. Verify version-dependent commands and product
behavior in current official documentation.

## Sources and reuse

Use `references/sources.md` for provenance and its documented gaps, and
`references/reuse-rights.md` before adapting external material. Paraphrasing does not remove
licence duties. BP-AIR, stakeholder and RIA31 adaptations are CC BY-SA 4.0.
`RIA31` is distinct from the EU AI regulation. Project IDs are not legal obligations.
