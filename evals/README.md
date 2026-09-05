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

These automated checks are lexical screening, not proof of correct reasoning. Review each response
against its `review_checks` when present, and check the actual recommendation, arithmetic, evidence
status and respect for scope. A response that merely repeats keywords must not pass semantic review.
The substring-based forbidden-term checks can also reject a correctly negated claim; inspect it.

For comparisons, run the same prompts against the baseline and revised skill with the same model,
tools and settings in fresh contexts. Save actual responses and record the model, date, loaded
references and limitations. Never fabricate responses to satisfy the evaluator. Keep catalogue
validation, lexical results and independent semantic review results separate in any report.

New lifecycle cases cover service necessity, older devices, rebound arithmetic, unsupported
compliance claims, muted autoplay, critical images, total AI task cost and safe retirement.
