# Closing NR summary

Every completed task using this skill ends with a short summary in the user's language:
all NR actions actually taken, their rule IDs, why they matter, and observed verification.
Group related actions for readability without dropping IDs. Separate unresolved checks and
proposals from applied actions. If nothing was applied, say so. Never infer energy or carbon
savings from a clean scan, fewer dependencies, tokens, or elapsed time.

For a small task, a few evidence-backed sentences suffice. For natural-language-only tasks
without relevant code to scan, use that textual summary rather than this static-scan command. For repeatable automation or a
larger audit, keep a task record outside version control and use `scripts/nr_summary.py`.
Record assessed rules, not the entire catalogue; identify exclusions and missing evidence
in `limitations`. Update the record after the final edit and verification. A previous task's
record must not be reused as current evidence.

## Evidence before status

Apply the applicability gate in `SKILL.md` before writing the record. Keep out-of-scope rules
out of `rules`; explain material exclusions in `limitations`. An applicable check that could
not run stays `REVIEW_REQUIRED`, with its missing tool, document or human decision identified.

For each assessed point, cite the artifact or command, observed result and assessed scope.
Recheck affected evidence after an edit; do not reuse an earlier passing result for changed
behaviour. A proposed action is not an applied action. If a rule covers more than was checked,
state the checked subpoint in `action` and remaining coverage in `limitations`.
The record contains pointers and findings, never credentials or unnecessary personal data.

## Record and command

Example structure (replace the illustrative evidence with actual observations):

```json
{
  "run_id": "unique-task-id",
  "scope": "Changed Python command and its tests",
  "rules": [
    {
      "id": "CODE-EFF-007",
      "status": "PASS",
      "action": "Used the Python standard library without a new dependency.",
      "benefit": "Avoids an additional installation and maintenance dependency.",
      "evidence": "Inspected the final imports and dependency manifest diff."
    }
  ],
  "limitations": ["Energy and carbon gains were not measured."]
}
```

Run from any working directory, substituting the actual skill and project paths:

```sh
python3 /path/to/green-codex/scripts/nr_summary.py \
  --path /path/to/changed-code \
  --record /path/to/task-record.json \
  --run-id unique-task-id --strict
```

The command prints Markdown to stdout. Include it or a faithful concise rendering in the
final answer. Redirect it to a local report or CI summary when useful. It uses no network,
model call, external package, or automatic repair. Select the smallest relevant scan scope.

Exit codes: `0` means no declared FAIL or static FAIL; `1` means a FAIL, or with `--strict`,
a REVIEW_REQUIRED, an empty action record, or no supported scanned files; `2` means an invalid
record or incomplete scan. A non-strict zero can contain unresolved reviews. Always read the
report. Preserve the status when wrapping or piping the command.

The script checks known IDs, required fields, duplicate entries and the expected run ID,
then reruns the existing three static checks. It does not execute commands contained in
`evidence`, authenticate claims, prove record freshness, detect all applicable rules, or
resolve contradictions between declared PASS and scan findings. Both remain visible; static
FAIL still fails the command. A matching run ID prevents accidental mix-ups, not forged evidence.
Review the final diff and cited results before reporting an action as verified.

## Integration choices

- **Interactive skill:** follow the closing-summary instruction before the final response.
  This is an agent instruction, not a guaranteed runtime interception.
- **CI or execution wrapper:** run this command after the work and tests, publish its stdout,
  and propagate its exit status. `--strict` makes unresolved reviews visible as a failing gate.
  A scan-only CI job does not know which NR actions were performed; it needs the task record.
- **Native Codex hook:** a `Stop` adapter can invoke the command using task-specific paths and
  return the hook's JSON protocol. The command's Markdown is not valid direct `Stop` stdout.
  Keep the adapter scoped to NR tasks and honour `stop_hook_active` to avoid repeated
  continuations. Require a current task record; do not silently read a stale shared report.

[Official Codex hook documentation](https://developers.openai.com/codex/hooks), consulted
2026-10-17, describes `Stop`, JSON output, `stop_hook_active`, project/user configuration,
and trust review. A plain skill installation does not register this command as a hook.
No native hook or global configuration is installed by this package. Test an adapter in the
actual host before enabling it; the portable command is independently usable now.
