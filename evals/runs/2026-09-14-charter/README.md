# Responsible AI charter: two paired samples

On 2026-09-14, four fresh agents answered the workplace rollout and agent
boundaries prompts from [the catalogue](../../cases.json): one baseline and one
candidate response per scenario. The baseline used commit `8ade234`; the candidate
used the revised skill and charter reference, whose hashes are in the run records.
Actual responses are preserved unchanged in each variant's `responses` directory.

| Assessment | Baseline | Candidate |
| --- | --- | --- |
| Lexical screening | Both fail: new charter rule identifiers absent | Both pass |
| Independent semantic review | Both pass all seven checks in total | Both pass all seven checks in total |
| Combined evaluator | Both fail lexical requirements | Both pass with bound reviews |

The baseline already gave sound advice. These samples show explicit rule
traceability, not an improvement in semantic pass rate. They are not a statistical
benchmark and do not establish behaviour on the other five charter scenarios.
No application security, accessibility or organisational evidence was tested.

The reviewer was a separate agent that read all four answers against the same
checks. Reviews were bound to the exact case, response and run metadata afterward.
The reviewer saw variant labels; this was not a blinded assessment. Exact model
backend and sampling settings were unavailable, and automatic tool output
compression occurred. See each `run.json` for reference hashes and limitations.
After generation, the reference's source note was corrected to identify the source
repository as private and remove its inaccessible hyperlink; operational rules
were unchanged. Recorded hashes retain the actual generation-time version.

Reproduce the candidate assessment:

```bash
python3 green-codex/scripts/run_evals.py \
  --responses evals/runs/2026-09-14-charter/candidate/responses \
  --run evals/runs/2026-09-14-charter/candidate/run.json \
  --reviews evals/runs/2026-09-14-charter/candidate/reviews.json \
  --case charter-workplace-rollout --case charter-agent-boundaries
```

Replace `candidate` with `baseline` for the expected lexical failures. Semantic
decisions remain available independently in each `reviews.json`.
