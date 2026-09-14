# 3U: utile, utilisé, utilisable

Use these three questions for a service, feature or AI pilot when its value or
readiness is in scope. Reuse `SERVICE-EFF-001`, `SERVICE-EFF-006` and, for AI,
`AI-EFF-001`/`AI-EFF-002`. This is a practical decision aid, not a new standard,
certification or requirement to audit every small code change.

## A small, realistic test

Choose one essential task, its intended users and the current alternative. Confirm
why the task matters using user evidence (`SERVICE-EFF-001`); faster execution of
an unnecessary task does not establish utility. Then agree
what benefit matters, acceptable quality and the observation period before
interpreting results. Use existing evidence first. A short worksheet and a few
observed tasks can start an investigation; they do not prove population-wide fit.

| Question | Feasible test | Evidence and decision |
| --- | --- | --- |
| **Utile — does it help?** | Compare a small set of representative tasks with the current process or a simple non-AI option. Include difficult cases. Count correct outcomes, time including review/correction, and material costs. | Record the task, baseline, sample and expected benefit. Faster output with worse quality does not establish utility. Use agreed quality and benefit criteria; without them, report what is observed and what remains unknown. |
| **Utilisé — is it actually used when needed?** | During a voluntary pilot over a relevant business cycle, count people with a real opportunity to use it, those who try it, and those who return when another need occurs. Ask a few users and non-users why. | Keep numerators, denominators, period and voluntary/mandatory context. Downloads, logins, generated calls or mandated use alone do not establish adoption. Before launch, usage is unverified, not failed. Rare but critical services may need infrequent use; do not impose daily activity targets. |
| **Utilisable — can people complete the task?** | Observe a few intended users completing the essential journey without coaching. Include keyboard access, relevant assistive technology, errors/recovery and realistic device/network conditions. | Record independent completion, help needed, blockers and recovery. A reproducible keyboard blocker is a failure for that journey even if most people succeed. Automated tests support the result but cannot replace observation. A small convenience sample does not establish accessibility for everyone. |

Counts such as a handful of participants or a short pilot are starting points,
not universal pass thresholds. Match the sample, period and acceptable risk to
the task; disclose gaps and avoid statistical claims from small samples. For a
one-off task, repeat usage may be irrelevant: record that limit rather than
inventing a retention requirement.
Successful uses do not establish the number of opportunities: two resolved incidents
prove two successful uses, not that only two incidents occurred. Keep that denominator
unknown unless the supplied evidence counts all relevant opportunities.

Use aggregated counts, an existing authorised log or a voluntary tally where
possible. Do not install tracking, collect sensitive task contents, rank workers
or contact users without authorisation. Report missing usage evidence and propose
the smallest collection method instead.

## Return three decisions, not one score

For each U, give `PASS` (evidence meets stated criteria in the assessed scope),
`FAIL` (an observed requirement is violated), or `REVIEW_REQUIRED` (criteria,
evidence or tests are missing). Always distinguish observed use from whether that
level meets the service's purpose. Do not average the three U results or let high
usage compensate for a harmful outcome or an inaccessible journey.

Keep the output short: U, result, dated evidence/sample, limit, next test and
owner if known. Suggest continue, adjust or reconsider based on the evidence;
do not deploy, remove a feature or redefine the user's task without authority.

For example, if a helper is faster but introduces incorrect answers, investigate
quality and total correction time before claiming it useful. If usage counts
exist but no adoption criterion was agreed, report those counts and
`REVIEW_REQUIRED` for adequacy. If a user is blocked at a keyboard step, report
`FAIL` for usability and retest that step and the complete journey after repair.

For an AI service, consult only the sections of
[the responsible AI charter](responsible-ai-charter.md) needed by the task or
observed risk, such as data permissions, truthful sources or consequential human
oversight. A 3U check does not automatically trigger all sixteen commitments.

## What Codex can verify

Codex can inspect supplied evidence, calculate rates with explicit denominators,
run authorised application tests and prepare this small protocol. It cannot
infer real adoption from code, invent participant observations or claim proposed
tests were executed. Repository CI validates this guidance's packaging; an actual
3U verdict requires evidence from the service and the people using it.
