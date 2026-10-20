# Full-stack contracts

Read the sections relevant to the current feature, not this whole playbook for a typo. Use the existing stack and official provider/framework documentation; verify changing API behavior against current docs. The goal is an explicit small contract and a verified vertical slice, not enterprise architecture by default.

## Business workflow and authorization

Before a new business-system feature, identify actors, roles, organizations/branches and who can read/create/update/delete each resource. Record important state changes and invariants, for example "staff can update stock only in their branch" or "one appointment occupies one capacity slot." Distinguish authentication from permission checks. Enforce ownership/tenant boundaries on every relevant server request or database policy, including IDs supplied by the browser. Hidden buttons are not authorization. Don't assume an admin identity or choose a provider without evidence.

Reuse maintained authentication/session libraries and provider primitives. Support expiry, logout, recovery and denied/error states as applicable; don't invent auth protocols. Browser public/publishable configuration is not automatically a secret; privileged credentials remain server-side. Never use an elevated key to bypass a broken user-authorization design.

## Database and persistence

Choose the engine from the actual requirements and existing system, not from the skill list. Postgres guidance must not be copied blindly into MySQL, SQLite or document databases. Define essential entities, types, relationships, unique/foreign-key/check constraints, and access patterns. Enforce critical integrity in the database where supported, not only the UI.

Use versioned migrations. Preserve compatibility with deployed callers and plan rollback or forward recovery. Verify on isolated/disposable data before authorized production changes; protect existing data and establish backups/recovery appropriate to the change. A destructive reset is not a normal migration shortcut. Don't assume approval to create paid infrastructure or mutate production data.

For stock, bookings, invoices and similar shared state, define the transaction boundary and use an appropriate atomic operation/constraint/locking strategy. Check concurrent and duplicate requests; read-then-write client logic is not enough. Avoid floating-point money calculations; use an explicit currency/precision convention appropriate to the engine. Index observed lookup/join/sort paths and paginate unbounded lists. Diagnose actual slow queries before speculative indexing/caching. EXPLAIN ANALYZE executes the statement; use a safe environment for side effects.

## API contracts and external integrations

For an endpoint, define input/output schemas, validation, authentication/authorization, errors/statuses, pagination and relevant limits. Reuse the existing API style; REST and GraphQL are choices, not two required implementations. Make breaking changes explicit and keep clients compatible.

For an external provider, confirm the correct API version, authentication scope, sandbox/live environments, quotas and supported SDK. Keep secrets server-side; validate upstream responses before using them. Set finite timeouts and a bounded retry policy with backoff appropriate to provider rules. Retry safe reads when justified; don't blindly retry a write. A timeout may have succeeded remotely: use supported idempotency keys and result lookup/reconciliation before another side effect. Handle 401/403/429, malformed replies, partial failure and unavailable service with useful recovery. User-supplied fetch targets need appropriate URL/redirect/SSRF controls.

For webhooks, follow the provider's signature verification contract, including raw body and timestamps where specified. Validate event type/schema, bind it to the correct account, durably deduplicate event IDs and make handlers idempotent. Account for duplicate/out-of-order delivery and retries. Acknowledge only after the event is safely recorded or processed according to the contract; use a durable queue only when the workload needs one. Never trust a browser redirect alone as proof of payment or another external result.

## Evidence and operations

Choose tests from the actual risk: happy path, invalid input, unauthorized/foreign-tenant access, transaction conflicts, duplicate submission, rollback/recovery and relevant provider failures. Add focused webhook replay/signature tests when webhooks exist. Use contract tests/fakes for deterministic failures, then an authorized sandbox smoke test for wiring. Clearly label any untested provider interaction; don't perform chargeable or consequential live operations merely to demonstrate a feature.

Reuse a single service/client boundary where it prevents inconsistent auth/retry/error behavior. Keep safe structured logs for failures and correlation without tokens or private payloads. Show loading/empty/error/retry states; don't fabricate successful saves. Maintain a minimal environment/setup example and distinguish frontend build variables from server secrets. Record actual checks and unresolved limitations. After a change is proven, stop expanding scope.
