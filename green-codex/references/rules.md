# Green IT rules

Apply these rules to code that you write, change, or review. Combine the language-specific rules
with the universal rules below. Cite RGESN, GR491, Opquast, or RGAA only when the evidence supports
the reference.

## How to apply a rule

Every applicable rule has an identifier and must produce one of three outcomes: `PASS` (evidence
is present), `FAIL` (a concrete violation is found), or `REVIEW_REQUIRED` (the rule cannot be
verified automatically). A finding must cite the identifier, file and line, impact, severity,
and a verification command or measurement. Do not mark a rule `PASS` from a declaration alone.

## Universal rules

- Confirm the user need before adding functionality; prefer the smallest viable solution.
- Minimise dependencies and choose a platform-native API when it is sufficient.
- Collect, process, store, and log only what is necessary. Define retention for new data.
- Bound caches, queues, retries, concurrency, and memory. Avoid polling and busy waiting.
- Stream or paginate large collections; avoid `SELECT *`, N+1 queries, and unbounded quadratic work.
- Never hard-code secrets. Keep production logs useful but sparse.
- Preserve security, correctness, resilience, and accessibility when optimising environmental impact.

## Enforceable sobriety rules

These rules are deliberately technology-neutral. Apply the relevant ones and record exceptions.

### Code and runtime

- **CODE-EFF-001 — Bound work:** every loop, recursion, batch, retry policy, queue, cache and
  concurrency pool must have a documented upper bound or an explicit termination condition.
  Verify with a test covering the bound and a worst-case input.
- **CODE-EFF-002 — Bound remote calls:** do not perform network or service calls inside an
  unbounded loop. Set a timeout and a maximum retry count; verify with a mocked call counter.
- **CODE-EFF-003 — Avoid repeated work:** cache or memoise stable results when the cache cost is
  lower than recomputation. Document the invalidation and maximum size; test hit, miss and expiry.
- **CODE-EFF-004 — Stream large data:** do not load an unbounded file, response or collection into
  memory. Use streaming, iterators or pagination and test with data larger than the normal case.
- **CODE-EFF-005 — Resource lifetime:** files, sockets, database handles, workers and temporary
  storage must be released on success and failure paths. Verify with a repeated-run or leak test.
- **CODE-EFF-006 — Resource budget:** define a measurable budget for at least two of CPU time,
  peak memory, transferred bytes, requests or artifact size for performance-sensitive changes.
  Compare before and after on a representative scenario.
- **CODE-EFF-007 — Dependencies:** every new runtime dependency must have a documented purpose,
  measured cost and maintenance status. Reject duplicate functionality or an oversized dependency.
- **CODE-EFF-008 — Complexity:** for a hot path or growing dataset, document the expected
  complexity and avoid an avoidable quadratic algorithm. Prefer `O(n log n)` or better when it
  preserves correctness; prove the change with a benchmark on representative and worst-case data.
- **CODE-EFF-009 — Allocations and structures:** avoid temporary allocations and copies in a hot
  path. Choose a data structure for the access pattern and memory footprint, supported by a
  benchmark or allocation profile. Do not prescribe one language or collection universally.
- **CODE-EFF-010 — Production logging:** logs must be level-controlled, sampled where appropriate,
  and exclude duplicate or high-cardinality payloads. Verify that normal traffic does not create
  unnecessary CPU, memory or disk I/O.
- **CODE-EFF-011 — Language fit:** choose a runtime using measured CPU, memory, energy, latency,
  portability and maintenance constraints. Rust, Go, Java/GraalVM or another compiled alternative
  may suit sustained CPU-intensive work; replacing an interpreted language is not automatic.
- **CODE-EFF-012 — Energy measurement:** for material performance changes, record the workload,
  duration, hardware or cloud context, method and uncertainty. Use SCI-compatible tooling such as
  GreenFrame, Scaphandre or PowerAPI when available; never present an estimate as a fact.
- **CODE-EFF-013 — Leak detection:** run memory/resource leak checks for long-lived or native
  components when supported by the stack (for example Valgrind or a JVM profiler). Document any
  justified exception.

### APIs and frontend

- **API-EFF-001 — Bounded collections:** collection endpoints must define a default and maximum page
  size, use cursor or bounded pagination, and return only required fields. Test the maximum size.
- **API-EFF-002 — Response budget:** document a target response size and request count for the main
  user journey; fail the check when the budget regresses without an approved exception.
- **WEB-EFF-001 — Deferred payloads:** non-critical scripts, images and embeds must be lazy or
  deferred. Verify with a production build and a network trace.
- **WEB-EFF-002 — Media budget:** provide responsive dimensions and modern formats with a fallback;
  no media asset may exceed the repository's documented size limit without justification.
- **WEB-EFF-003 — Idle work:** do not use frequent polling or continuous animation for a state that
  can be event-driven. If polling is unavoidable, document its interval, stop condition and cost.

### Databases and storage

- **DB-EFF-001 — Explicit projection:** production queries must select named columns; `SELECT *`
  is prohibited except in documented schema-inspection tooling. Add a query test or static check.
- **DB-EFF-002 — Bounded reads:** every user- or service-facing list query must have a limit,
  cursor, date window or other proven bound. Verify that an omitted bound fails safely.
- **DB-EFF-003 — No N+1:** a collection read must not issue one query per item. Verify with a query
  counter or an integration test using multiple records.
- **DB-EFF-004 — Verified indexes:** indexes must correspond to measured filters, joins or ordering;
  include the query plan (for example `EXPLAIN`) and remove unused indexes when evidence supports it.
- **DB-EFF-005 — Retention:** each stored data class must have an owner, purpose, retention period,
  deletion or anonymisation procedure, and a test or scheduled job proving enforcement.
- **DB-EFF-006 — Storage growth:** monitor table, object and backup growth; define an alert threshold
  and an archival policy before introducing a high-volume data source.
- **DB-EFF-007 — Duplicate storage:** do not persist the same derived or binary data in multiple
  places unless the performance trade-off is measured and documented.
- **DB-EFF-008 — Compression:** compress large or repetitive payloads when CPU cost and latency are
  lower than storage and network savings. Benchmark the selected codec (for example Zstandard)
  instead of assuming one codec is always best.
- **DB-EFF-009 — Data modelling:** avoid unnecessary duplication and define a consistency boundary.
  Normalise when it reduces storage and update anomalies; allow measured denormalisation when it
  materially reduces repeated reads or compute, with an explicit refresh strategy.

### Infrastructure and operations

- **INFRA-EFF-001 — Workload placement:** choose a region, provider and architecture using energy
  intensity, availability, latency, data residency, accessibility and cost evidence. Renewable-
  energy claims must cite a current provider source; never assume a region is fully renewable.
- **INFRA-EFF-002 — Load shifting:** move deferrable, non-critical work to lower-carbon or lower-
  demand periods when deadlines, data residency and reliability permit. Record the schedule and a
  safe fallback; do not delay interactive or safety-critical work.
- **INFRA-EFF-003 — Elasticity:** scale idle, stateless capacity down or to zero when safe,
  including non-production environments. Define warm-up, state, queue and recovery limits first.
- **INFRA-EFF-004 — Compute model:** select serverless, containers or VMs from measured idle time,
  startup cost, utilisation, workload duration, portability and operational overhead. No model is
  inherently more sustainable for every workload.
- **OPS-EFF-001 — Retention and observability:** set retention by data class and purpose; delete or
  archive logs and traces on schedule (for example with Elasticsearch ILM). Alert on growth and on
  a configurable deviation from a representative baseline, not an unexplained universal percentage.
- **OPS-EFF-002 — Facility evidence:** for owned or procured infrastructure, track PUE or an
  equivalent facility metric and set a context-appropriate target. Consider liquid cooling or heat
  reuse only for suitable high-density deployments, backed by lifecycle and safety assessment.
- **OPS-EFF-003 — Hardware lifecycle:** specify service life, repairability, reuse and end-of-life
  channels in procurement. Prefer refurbished equipment when security, support and performance
  requirements are met; verify labels such as TCO Certified, Energy Star or Blauer Engel.

### Networks and digital services

- **NET-EFF-001 — Avoidable transfer:** identify and remove non-essential requests and duplicate
  downloads in the main user journeys. Verify with a production network trace and request budget.
- **NET-EFF-002 — Caching:** cache immutable or safely cacheable responses at the browser, edge or
  service layer with an explicit TTL and invalidation strategy. Do not cache personal or rapidly
  changing data without a privacy and correctness review.
- **NET-EFF-003 — Protocol choice:** select HTTP/2, HTTP/3 or another protocol based on measured
  latency, reliability, compatibility and energy impact. A newer protocol is not automatically more
  sustainable; record the tested network conditions.
- **NET-EFF-004 — Critical path:** preload or prefetch only resources proven critical to the next
  interaction. Lazy-load everything else and verify the decision with a trace.

### Hardware and facilities

- **HW-EFF-001 — Service life:** define a target service life and repair or upgrade path for
  devices and servers. A five-year target is a useful default, not a guarantee when security or
  support constraints require replacement.
- **HW-EFF-002 — Circular procurement:** compare new, refurbished, modular and repairable equipment
  using lifecycle, warranty, security and performance evidence. Verify environmental labels rather
  than treating one label as sufficient proof.
- **HW-EFF-003 — End of life:** document secure data erasure, reuse, take-back and recycling routes
  before purchasing equipment; retain evidence of the channel used.

### AI workloads

- **AI-EFF-001 — Necessity:** confirm that automation or an AI model is needed; prefer a deterministic
  rule or conventional algorithm for a simple task when it meets the requirement.
- **AI-EFF-002 — Model fit:** select the smallest model meeting quality, safety and latency needs.
  Compare model size, context, tokens, memory, energy and error rates on a representative test set.
- **AI-EFF-003 — Dataset efficiency:** remove duplicates and stale data, minimise context and cache
  stable results where safe. Document quality and privacy checks after reduction.
- **AI-EFF-004 — Hardware fit:** choose accelerator and deployment mode from measured utilisation,
  latency, memory and energy. A low-power GPU is not automatically preferable if it increases
  runtime or failures.
- **AI-EFF-005 — AI budget:** define a per-request or per-job token, time, cost or energy budget,
  enforce it at runtime, and test refusal or fallback when the budget is exceeded.

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
