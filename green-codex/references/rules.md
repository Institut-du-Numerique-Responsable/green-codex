# Green IT rules

Apply these rules to code that you write, change, or review. Combine the language-specific rules
with the universal rules below. Cite RGESN, GR491, Opquast, or RGAA only when the evidence supports
the reference.

## Universal rules

- Confirm the user need before adding functionality; prefer the smallest viable solution.
- Minimise dependencies and choose a platform-native API when it is sufficient.
- Collect, process, store, and log only what is necessary. Define retention for new data.
- Bound caches, queues, retries, concurrency, and memory. Avoid polling and busy waiting.
- Stream or paginate large collections; avoid `SELECT *`, N+1 queries, and unbounded quadratic work.
- Never hard-code secrets. Keep production logs useful but sparse.
- Preserve security, correctness, resilience, and accessibility when optimising environmental impact.

## Frontend, HTML, CSS, and media

- Keep transferred bytes and request count low; load non-critical scripts with `defer` or `async`.
- Use native HTML elements (`button`, `a`, `details`, `dialog`, `select`) before custom widgets.
- Lazy-load below-the-fold images and embeds. Never autoplay video; use a poster and user action.
- Prefer AVIF/WebP with fallbacks, responsive `srcset`/`sizes`, and explicit media dimensions.
- Prefer SVG or CSS for simple icons. Keep the DOM shallow and remove dead markup.
- Ship only the CSS and fonts used. Prefer system fonts; otherwise use limited WOFF2 families with
  `font-display: swap`.
- Animate only `transform` and `opacity`, honour `prefers-reduced-motion`, and avoid continuous
  animations. Provide a usable print stylesheet.
- Debounce expensive input, scroll, and resize handlers. Cache network responses explicitly.

## Backend, APIs, and data

- Paginate collections and stream large responses. Select only required columns and fields.
- Add and verify indexes for frequent filters and joins; eliminate N+1 access patterns.
- Set timeouts, bounded retries, and circuit breakers for remote calls. Do not retry blindly.
- Prefer asynchronous or event-driven refresh over polling. Measure CPU, memory, storage, and
  network impact where practical.
- Dispose resources deterministically and avoid loading an entire file or dataset into memory.

## Language guidance

Apply the backend rules to JavaScript/TypeScript, Java, C#, Python, PHP, Ruby, Rust, C, C++, SQL,
and other server-side code. Additionally:

- JavaScript/TypeScript: use code splitting and dynamic imports for optional features; avoid layout
  thrashing and repeated framework re-renders.
- Python: use iterators and generators for large data; avoid repeated serialisation and unbounded
  DataFrame copies.
- Java/C#: bound executor pools and caches; dispose streams, database handles, and HTTP clients.
- PHP/Ruby: stream exports and avoid rendering unbounded collections in one response.
- C/C++/Rust: release resources on every path; measure allocations and avoid needless copies.
- SQL: use projections, predicates, pagination, and verified indexes; never use unbounded queries.

## Web quality and accessibility

- Use semantic structure, visible focus, keyboard operation, correct language, labels, error text,
  sufficient contrast, alternative text, zoom/reflow, and media alternatives.
- Test with a keyboard and a screen reader when the change affects user interaction.
- Keep official acronyms **RGESN**, **GR491**, **Opquast**, and **RGAA** unchanged.
- Do not claim RGAA or Opquast conformance from a static inspection alone; state what was tested.

## Responsible AI

- Use the smallest capable model and context. Cache stable prompts and outputs where safe.
- Minimise personal and confidential data sent to a model. Set budgets, rate limits, and timeouts.
- Keep a human review path for consequential outputs. Disclose AI assistance where transparency is
  required and retain a provenance note when it is available.

## Audit format

For each finding, record the file and line, observed evidence, applicable criterion, environmental
or user impact, severity, confidence, and a verification command or measurement. Separate facts,
inferences, and recommendations.
