# Audit corrections

**Goal:** Address the six findings from the 2026-09-13 repository audit.

**Constraints:** Keep Python dependency-free. Preserve existing licence edits.
Do not claim that lexical checks establish response quality. Keep CI validation
mandatory before releases. Limit website changes to broken discovery assets.

1. Add failing scanner regressions for invalid paths, unreadable input, SQL
   comments, multiline media and polling requiring review. Fix the scanner,
   preserving line numbers and reporting incomplete scans separately.
2. Add failing evaluation regressions: lexical success alone must remain
   REVIEW_REQUIRED. Accept separately recorded semantic reviews only when tied
   to the exact response, case and run metadata. Document reproducible comparisons.
3. Make release depend on the reusable validation workflow. Make Markdown link
   discovery recursive; remove duplicate checks and the unused pip update job.
4. Fix project-relative website asset URLs, remove unsupported manifest routes,
   and verify local resolution. Remove duplicated skill instructions.
5. Run package, scanner, evaluation, release and static-site checks; review the
   complete diff independently and fix material findings.

Actual model-response collection is separate from synthetic evaluator unit tests.
No benchmark score will be invented or inferred from those tests.
