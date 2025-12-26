# agent.md — Sage Intacct XML API SDK Agent Instructions

## Mission
Build a production-quality SDK for the Sage Intacct XML API with:
- 100% endpoint coverage (every operation we choose to support is implemented, documented, and tested)
- 100% test coverage for implemented code paths (unit + integration)
- Continuous verification via executed tests and (when allowed) real network calls to Intacct

If something cannot be verified by executed tests, it is not “done”.

## Non-Negotiables
1. **No “paper implementations.”** Every new endpoint must ship with tests that run in CI.
2. **Network calls must be exercised** whenever credentials + outbound access are available.
3. **Deterministic tests.** Integration tests must be replayable without hitting the network by default.
4. **Strict typing and linting** (language-appropriate) and a consistent public API.
5. **Backwards compatibility** once a public method is released (semver rules).

## Constraints & Reality Check (Read Carefully)
You asked for the agent to “operate entirely independently” and “execute network calls” while it develops. That is only possible if:
- The environment running the agent has outbound network access
- You provide Intacct credentials (and a sandbox/company ID)
- The agent is allowed to read those credentials from environment variables or a secrets store

If any of those are missing, the agent must:
- Use recorded HTTP fixtures (VCR-style) captured from a credentialed run, OR
- Use a local stub server that faithfully simulates Intacct responses

**Default mode:** tests run with fixtures (no network).  
**Optional mode:** `INTEGRATION=1` runs real calls and can refresh fixtures.

## Repo Expectations
Use a conventional layout:
- `src/` SDK source
- `tests/` unit + integration tests
- `examples/` runnable examples
- `docs/` reference docs
- `scripts/` dev scripts
- `fixtures/` recorded request/response pairs (sanitized)

## Target Coverage Definition
“100% endpoint coverage” means:
- A tracked catalog of endpoints/operations exists (see **Endpoint Catalog**).
- Every catalog entry has:
  - A public SDK method
  - XML request builder + validation
  - XML response parsing into typed objects
  - Unit tests for serialization/parsing and error cases
  - Integration tests (fixture-based; real network optional)

If the XML API is too large to implement in one pass, implement in phases:
1. **Core platform**: auth/session, request envelope, error handling, retries, logging
2. **Foundation objects**: read/query/list operations
3. **CRUD** for major modules (GL, AP, AR, etc.)
4. **Edge cases**: attachments, custom fields, batching, pagination nuances

## Endpoint Catalog (Single Source of Truth)
Maintain `docs/endpoints.md` as a checklist. It must include:
- Intacct operation name(s) (e.g., `readByQuery`, `create`, `update`, `delete`, `getAPISession`, etc.)
- Module/object (e.g., `GLACCOUNT`, `VENDOR`, etc.)
- SDK method name
- Status: `todo | wip | done`
- Tests: `unit | integration | fixture | live`

The agent must always:
- Add new entries before implementing
- Keep it updated as work progresses
- Use it to prove “coverage”

## API Design Requirements
- Provide a single client entrypoint, e.g. `IntacctClient`
- Support:
  - Session-based auth (preferred) and sender/password flows if needed
  - Request control IDs and idempotency strategy
  - Pagination helpers for query/readByQuery
  - Consistent error model with rich context:
    - HTTP status (if applicable), Intacct error number, description, correction, request controlId
  - Configurable timeouts, retry/backoff for transient errors
  - Logging hooks (request IDs, timings) without logging secrets or PII

Public surface must be stable and minimal:
- `client.<module>.<object>.<operation>(...)` OR `client.<object>.<operation>(...)`
- Avoid exposing raw XML except behind a debug flag.

## XML Handling Requirements
- Generate XML via a builder (no string concatenation).
- Normalize:
  - element order where required
  - escaping and encoding (UTF-8)
  - empty vs missing elements semantics
- Parsing:
  - tolerate optional/missing fields
  - preserve unknown fields in a `raw` map for forward compatibility (optional)

## Testing Strategy
### Unit Tests (always run)
- XML generation snapshots/approvals for each operation
- Response parsing tests for:
  - success responses
  - error responses
  - partial/optional fields
  - pagination
- Property-based tests for escaping and validation (if language supports)

### Integration Tests (fixture-first)
- Use a VCR mechanism to record and replay:
  - request body (sanitized)
  - response body (sanitized)
- Default: replay fixtures only (no network).
- Optional: live mode to refresh fixtures.

### Live Mode (real Intacct calls)
Enabled only when:
- `INTEGRATION=1`
- all required env vars are set (see below)

Live runs must:
- Create unique records (use deterministic prefixes)
- Clean up created records when feasible
- Never run destructive operations on production-like accounts

## Required Environment Variables (Live Mode)
- `INTACCT_SENDER_ID`
- `INTACCT_SENDER_PASSWORD`
- `INTACCT_COMPANY_ID`
- `INTACCT_USER_ID`
- `INTACCT_USER_PASSWORD`
- `INTACCT_ENDPOINT_URL` (e.g., the XML gateway URL)
Optional:
- `INTACCT_LOCATION_ID` (if required)
- `INTACCT_DEBUG_XML=1` (logs sanitized XML)
- `INTACCT_FIXTURE_RECORD=1` (record/refresh fixtures)

The agent must never print secrets. Mask them in logs.

## CI Requirements
CI must run:
- formatting
- lint
- typecheck
- unit tests
- fixture-based integration tests

Live integration tests must be gated and never required for PR success unless you explicitly configure secrets for them.

## Implementation Workflow (How the Agent Works)
For each endpoint/catalog item:
1. Add the endpoint to `docs/endpoints.md`
2. Implement request builder + response parser
3. Add unit tests (XML snapshot + parsing + errors)
4. Add integration test using fixtures
5. Run full test suite locally
6. If live mode is enabled, run integration tests against Intacct and refresh fixtures
7. Mark endpoint as `done` only when:
   - unit + integration tests pass
   - coverage for the new code is effectively 100%
   - docs updated

## Definition of Done (Strict)
An endpoint is “done” only if:
- public method exists and is documented
- request + response types exist (typed models)
- errors handled and tested
- unit tests cover success + failure paths
- integration test exists and passes in fixture mode
- if live mode is available: live test passes at least once and fixtures updated

## Code Quality Rules
- No dead code, no TODOs, no commented-out blocks.
- Keep functions small; prefer composition.
- Prefer explicit, typed models over unstructured dict/maps.
- Follow semantic versioning.
- Add changelog entries for user-facing changes.

## Security & Data Handling
- Never commit credentials.
- Sanitize fixtures:
  - redact sender/user/passwords
  - redact session IDs
  - redact any personal/vendor banking details
- Provide a sanitizer that runs automatically when recording fixtures.

## Deliverables
The agent must maintain and update:
- `docs/endpoints.md` (coverage checklist)
- `docs/usage.md` (how to use the SDK)
- `examples/` for common flows (auth, query, create/update)
- `CHANGELOG.md`

## Stop Conditions
If the agent encounters:
- unclear API behavior
- inconsistent responses
- undocumented fields
It must:
- create a minimal reproduction test
- capture the raw XML (sanitized)
- document assumptions in `docs/notes.md`
- proceed with a conservative implementation that preserves raw data

## Strong Default Opinions (Follow These)
- Fixture-first integration tests; live mode is optional and gated.
- Treat “100% endpoint coverage” as a tracked checklist, not a vibe.
- Never accept a PR that adds endpoints without tests.
- Prefer a small, consistent public API over mirroring every XML nuance.
