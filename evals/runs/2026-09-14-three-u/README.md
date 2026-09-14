# Practical 3U: one paired sample

On 2026-09-14, separate agents answered the exact French `three-u-pilot` prompt
from [the catalogue](../../cases.json), without seeing evaluation checks or the
other answer. Baseline used commit `9beddf8`; candidate used the revised 3U
routing and reference. Responses are preserved unchanged; each `run.json` records
the actual skill/reference hashes, settings and limits.

| Assessment | Baseline | Candidate |
| --- | --- | --- |
| Lexical screening | FAIL: two expected service rule IDs absent | FAIL: same IDs absent |
| Independent semantic review | 3/4 checks pass | 4/4 checks pass |
| Combined evaluator | FAIL | FAIL (lexical requirements) |

Both answers give realistic tests and separate the three U decisions. The reviewer
found a narrow baseline gap: correct usage denominators were reported, but the
answer did not explicitly distinguish adequacy against missing agreed adoption
criteria. The candidate does. This single sample cannot establish a reliable
improvement rate. It also shows that useful advice and literal rule-ID coverage
are different checks; the answers were not edited to make screening pass.

A separate reviewing agent judged both labelled answers and recorded per-check
evidence in `reviews.json`. This was not blinded. Review hashes bind the exact
response, case and run. Exact backend/sampling settings were unavailable; tool
output compression occurred. The candidate's first attempt hit a quota limit and
was resumed before a response was saved.

This is a synthetic evidence-interpretation exercise, not a 3U assessment of a
real product. No application test, interview or usage observation was executed.

Reproduce screening and review binding (expected exit code 1 for both variants):

```bash
python3 green-codex/scripts/run_evals.py \
  --responses evals/runs/2026-09-14-three-u/candidate/responses \
  --run evals/runs/2026-09-14-three-u/candidate/run.json \
  --reviews evals/runs/2026-09-14-three-u/candidate/reviews.json \
  --case three-u-pilot
```

Replace `candidate` with `baseline` for the baseline record. Consult each
`reviews.json` for semantic results separately from lexical screening.
