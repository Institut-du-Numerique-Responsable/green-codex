# Measurement and decision protocol

Read for resource comparisons, environmental claims or material optimisations. This is project
engineering guidance; it does not certify a service or replace a lifecycle assessment.

## Start with a decision

Record the useful task, current bottleneck, proposed change and acceptance threshold. Reuse project
budgets; otherwise propose a workload-specific baseline and target, clearly labelled provisional.
Do not invent universal page-weight, response-time, energy or carbon limits.

Use the cheapest evidence capable of resolving the decision. A query count can demonstrate the
removal of N+1 calls; it cannot establish carbon savings. Do not install a monitoring stack for a
small edit or rerun expensive benchmarks after a conclusion is already supported.

## Evidence levels

| Evidence | What it supports | What it does not establish |
| --- | --- | --- |
| Static inspection | A located pattern or configured limit | Actual frequency, energy, complete compliance |
| Trace/profile | Requests, bytes, CPU, memory for a tested task | Environmental impact without a model |
| Energy metering | Energy in a stated measurement boundary | Whole-service energy if components are omitted |
| Environmental model | An estimate with factors and assumptions | Direct measurement or universal savings |
| EcoIndex/Lighthouse or similar score | Findings under that tool's method | A lifecycle assessment or RGESN/RGAA compliance |

## Reproducible comparison

- Fix the useful output, input dataset, quality and service level. Record code/build versions,
  device/runtime, network conditions, concurrency and tool versions. Include failure and retry work.
- Compare equivalent baseline and candidate workloads. Separate cold and warm caches/startup;
  include an idle window if background work is affected. Do not compare a cold baseline to a warm
  candidate or a development build to a production build.
- Repeat enough to expose variation; record repetitions, duration and dispersion. Alternate runs
  when practical. If variation masks the result, report it as inconclusive, not a precise gain.
- Capture relevant resource metrics and task completion, plus accessibility and correctness checks
  affected by the change. Stop when the decision is supported; avoid gratuitous measurement.
- Report unit cost and period totals using the same boundary. For example, 20% less energy per
  task with twice as many tasks means 60% more task-related energy, assuming other factors equal.
  State idle and shared overhead separately; do not imply causation from traffic growth alone.
- Include migration, duplicated operation, storage and maintenance costs for architectural changes.
  If a break-even estimate is possible, disclose its horizon and assumptions; otherwise flag the gap.

## Carbon and lifecycle claims

The [SCI specification](https://sci.greensoftware.foundation/) expresses carbon intensity as
`SCI = (O + M) / R`: operational emissions plus allocated embodied emissions per functional unit.
Where applicable, `O = E × I`, with energy in kWh and a carbon intensity in gCO2e/kWh. Keep units,
time period and boundary consistent; disclose allocation, factors, source dates and uncertainty.
Account for significant supporting systems and avoid double-counting facility overhead. Compare
baseline and candidate with the same methodology. Offsets do not reduce SCI.

Unknown energy, hardware allocation or factors must remain explicit gaps, not invented zeros.
Partial operational estimates may still be useful when clearly labelled; do not call them complete
SCI or lifecycle results. Resource, price and token reductions are not direct carbon measurements.

For lifecycle decisions, also examine water, equipment manufacture, material use, lifetime and
end of life. A carbon-only calculation cannot decide every environmental trade-off. Do not infer
a service footprint from a provider's renewable claim or PUE alone.

## Compact evidence record

`Rule/status | task + boundary | baseline → candidate + units | method/environment/date |
repetitions + uncertainty | trade-offs + missing data | decision + next verification`

Use `REVIEW_REQUIRED` where essential evidence is absent. Cite raw results or reproducible commands;
do not fill the record with fabricated measurements. Source consulted: SCI web specification
1.1.0, 2026-09-05; verify the applicable edition before a formal assessment.
