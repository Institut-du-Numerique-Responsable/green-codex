# Behavioral evaluations

The cases in `cases.json` are realistic requests used to check whether Green Codex applies the
right rules, asks for evidence, and avoids universal technology or carbon claims.

For each case, run the prompt with the skill and save the response as
`evals/responses/<case-id>.md`. Then run:

```bash
python3 green-codex/scripts/run_evals.py --responses evals/responses
```

The evaluator checks that every expected rule identifier is cited, that the response contains an
actionable vocabulary and that forbidden overclaims are absent. Missing responses are reported as
`REVIEW_REQUIRED`; they are not silently treated as passing. The case schema itself is checked in
CI with `python3 green-codex/scripts/test_evals.py`.
