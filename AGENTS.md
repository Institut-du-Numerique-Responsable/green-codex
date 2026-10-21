# Project conventions

## Documentation & communication

- Code comments must be simple and comprehensible. Explain why the code exists, not what it does. Avoid jargon unless it is necessary.
- Commit messages must have a precise subject and explain the reason and resulting behaviour without requiring the reader to open the diff. Add a body when the subject is insufficient. Record actual verification and important limits, and compare the final message with the staged diff before committing.
- Pull request descriptions must state what changed and why, in plain language. A non-expert reviewer must be able to understand it.
- Merge commit messages must stay readable. Keep the default squash message (title plus PR body). Do not leave vague or auto-generated text.

- Apply [expression rules](green-codex/references/expression.md) to every authored response, document, code comment, commit message and PR description, in every language. Review the final squash message against those rules.
