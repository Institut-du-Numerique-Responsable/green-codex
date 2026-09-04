# Responsible Codex usage practices

These 14 project-authored practices adapt the useful substance of the earlier Green Claude usage
checklist to Codex. They are not quotations or personal advice attributed to an individual. Codex
commands and behavior are tied to the official documentation listed below.

Use this checklist when auditing or improving the use of Codex itself. Do not load it for every
ordinary code audit. Token counts, latency, and monetary cost are useful operating indicators, but
none is a direct measurement of energy use or environmental impact.

## Manage context

### USAGE-CODEX-CTX-01 — Keep initial context relevant

State the objective, constraints, acceptance criteria, and where Codex can retrieve evidence.
Avoid pasting whole files or exhaustive tool descriptions when Codex can inspect the relevant
material on demand. Compare input volume, latency, cost, and result quality before standardising a
prompt pattern.

### USAGE-CODEX-CTX-02 — Fork before a risky exploration

Before trying a materially different approach that may be discarded, use `/fork` in the
interactive CLI to clone the current chat, or `codex fork` to clone a saved session. This preserves
the original transcript while the alternative is explored separately. A fork does not rewind to
an earlier turn, so it should not be presented as an undo mechanism.

### USAGE-CODEX-CTX-03 — Start a new task for unrelated work

Use `/new` or `/clear` when the next objective does not need the current history. Both start a new
chat; `/clear` also clears the terminal view. For related work, continue from the smallest useful
state or use `/compact` when the retained conversation still matters.

### USAGE-CODEX-CTX-04 — Compact deliberately

After a long exchange, `/compact` replaces earlier turns with a summary. At stable checkpoints,
make the state easy to preserve: record the objective, accepted decisions, completed and verified
actions, important tool results, open blockers, and the next goal. There is no universal
context-size threshold; watch quality, latency, and input volume, and remember that compaction can
discard useful detail.

### USAGE-CODEX-CTX-05 — Reuse a maintained code map

For a large or repeatedly visited repository, maintain a concise index of key modules, purposes,
and entry points. Read it before broad exploration and update it when the structure changes. Keep
the map small enough that its recurring context cost remains lower than the rediscovery it avoids.

### USAGE-CODEX-CTX-06 — Match response length to the need

Prefer dense, actionable answers. Avoid repeating the prompt, narrating obvious tool activity, or
restating a diff when that adds no decision-relevant information. Retain explanations that prevent
errors or make verification possible.

## Prepare the task

### USAGE-CODEX-BRIEF-01 — Give a complete brief

Provide the intended outcome, relevant constraints, files or systems in scope, exclusions, and
observable acceptance criteria. A good brief reduces avoidable clarification and rework without
front-loading unrelated material.

### USAGE-CODEX-BRIEF-02 — Delegate bounded work

For a well-scoped task, give Codex enough authority and verification criteria to complete it without
step-by-step prompting. Intervene when a material choice, permission, missing input, or correction
is required. Measure whether this reduces turns and rework for the actual workflow.

## Preserve durable guidance

### USAGE-CODEX-MEM-01 — Record recurring project conventions

When the same correction reveals a durable convention, propose a concise rule in `AGENTS.md` at the
narrowest applicable directory. Review and remove stale rules: instructions loaded repeatedly have
a context and maintenance cost of their own.

### USAGE-CODEX-MEM-02 — Package genuinely repeated workflows

Turn a stable, repeated procedure into a versioned Codex skill when reuse justifies its authoring,
maintenance, and loading costs. Keep the skill narrowly triggered and move detailed material into
references that are read only when needed.

## Verify to avoid rework

### USAGE-CODEX-VERIFY-01 — Provide a proportionate verification loop

Give Codex a test, command, browser check, benchmark, or observable criterion that can confirm the
requested outcome. Run the smallest verification that covers the risk, and broaden it when the
change or evidence warrants it. Report what was actually observed rather than declaring success
from inspection alone.

## Proportion compute

### USAGE-CODEX-COMPUTE-01 — Tune model and reasoning effort

Use `/model` to select a model and reasoning effort appropriate to the task. Start from the
configured recommendation, then raise or lower effort based on evaluations of quality, latency,
token volume, and cost. A weaker setting that causes rework is not automatically preferable.

### USAGE-CODEX-COMPUTE-02 — Use multiple agents only when justified

Parallel agents add calls and context. Reserve them for independent work where a credible gain in
elapsed time, coverage, or quality justifies that overhead. Define bounded subtasks, avoid duplicate
exploration, and compare the result with a simpler workflow when the decision is recurring.

### USAGE-CODEX-COMPUTE-03 — Keep non-interactive runs minimal

Use `codex exec` for isolated automation and provide only the required prompt, files, tools, and
configuration. Do not copy options from another product into Codex. Validate quality and resource
indicators over repeated runs before adopting the automation broadly.

## Official Codex sources

- [Codex CLI command reference](https://developers.openai.com/codex/cli/reference) for interactive
  commands, `codex fork`, and `codex exec`.
- [Codex guidance for `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md) for the
  instruction-file hierarchy and scope.
- [Codex prompting guidance](https://learn.chatgpt.com/docs/prompting) for stating expected
  behavior, relevant context, constraints, and verification.
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices) for task context and
  choosing reasoning effort proportionately.
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5)
  for evaluation, prompt caching, and the task state to preserve during compaction. This source is
  general model guidance rather than a Codex command reference.

Recheck these sources when Codex versions or interfaces change. The operational recommendations
above remain Green Codex editorial guidance unless an individual claim links to a primary source.
