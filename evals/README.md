# Behavioral evaluations

A first real response and its separate semantic review are recorded in
[the September 13 run](runs/2026-09-13-rebound/README.md). It covers one case,
with an honest lexical failure; it is not a full benchmark.

The cases in `cases.json` are realistic requests used to check whether Green Codex applies the
right rules, asks for evidence, and avoids universal technology or carbon claims.

For each case, run the prompt with the skill and save the response as
`evals/responses/<case-id>.md`. Then run:

```bash
python3 green-codex/scripts/run_evals.py --responses evals/responses
```

The evaluator first performs lexical screening, then requires an independent semantic review bound
to the exact case, response and run hashes. Supply `--reviews reviews.json --run run.json` for a
review-backed result; without those files every lexical match remains `REVIEW_REQUIRED`. Missing
responses are reported as `REVIEW_REQUIRED`; they are not silently treated as passing. The case
schema and review binding are checked in CI with `test_evals.py` and `test_eval_review.py`.

Each review is keyed by case ID and contains `reviewer`, `verdict`, `checks`,
`response_sha256`, `case_sha256` and `run_sha256`. Hash the UTF-8 response text
unchanged. Hash the case and run objects after serializing with Python
`json.dumps(value, sort_keys=True, ensure_ascii=False)`. Changing the model,
settings, date, limitations or skill hash invalidates the recorded review.

The run records `model`, `date`, `skill_sha256`, non-empty `settings` and a
`limitations` list. Each applicable review check records a boolean `passed`
and an `evidence` explanation. Reviews are attestations by the named reviewer;
hashes detect changed inputs, not whether a reviewer's judgment is correct.

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
