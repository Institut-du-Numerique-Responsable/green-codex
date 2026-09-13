# First recorded real response

One of fourteen cases was run in a fresh agent context with the skill and routed
references. The generator did not receive the expected answers, case rubric or
tests. The response is preserved unchanged. Exact backend settings were not
available; see `run.json` for the limitations and hashes of the reference files.

The separate semantic review passes: arithmetic, scope and uncertainty are correct.
Lexical screening fails because the response omits the expected rule identifiers
and explicit finding status. The overall evaluator therefore exits with code 1.
This is recorded evidence of a limitation, not a successful benchmark suite.

Reproduce the recorded evaluation from the repository root:

```bash
python3 green-codex/scripts/run_evals.py \
  --case rebound-total-impact \
  --responses evals/runs/2026-09-13-rebound/responses \
  --run evals/runs/2026-09-13-rebound/run.json \
  --reviews evals/runs/2026-09-13-rebound/reviews.json
```

`skill_sha256` hashes the canonical JSON mapping of reference paths to SHA-256
hashes stored in `reference_sha256`. Canonical JSON here means Python
`json.dumps(value, sort_keys=True, ensure_ascii=False)` encoded as UTF-8.
