# Backend skill routing

Eight core skills cover workflow/design; these domain modules are conditional, not extra mandatory passes. Resolve names through the current catalog and verify availability before use. Read only relevant references as each module instructs. A missing module does not justify inventing that it ran, changing stacks, or installing an unrelated bundle.

| Task | Module and boundary |
| --- | --- |
| REST/GraphQL endpoint design or API contract review | `api-design-principles`, installed from wshobson/agents. Read its details only when the short entrypoint is insufficient. Provider-specific integration mechanics still require official provider docs and the full-stack integration contract. |
| Explicit security guidance, security review or secure-by-default coding help | `security-best-practices`, installed from openai/skills. Preserve its explicit trigger and supported languages: Python, JavaScript/TypeScript and Go. Load matching framework/language references; For PHP or another unsupported language, continue an authorized review using current official language/framework security guidance and applicable OWASP material; disclose the module's coverage limit. Don't start a full security report for every feature. Normal validation/authorization remain baseline regardless of whether this module triggers. |
| Supabase database, Auth, Storage, functions or integrations | Existing catalog skill supabase:supabase; follow its provider workflow. No duplicate installation. |
| Postgres schemas, SQL, migrations, RLS, indexes or query performance | Catalog skill supabase:supabase-postgres-best-practices or standalone supabase-postgres-best-practices from the optional Postgres install profile, maintained by Supabase. Postgres-specific; verify installed reference scope and load applicable sections. No duplicate installation. |
| Schema/data migration in any engine | Existing migration skill when a compatibility-safe transition is needed; engine/version-specific official docs and tests. Don't force Postgres or Supabase onto PHP/MySQL or another chosen stack. |
| Unknown failure, incorrect query or integration regression | Existing systematic-debugging/investigate-first as routed by Superpowers. Evidence first, one hypothesis at a time; no speculative parallel rewrites. |
| New behavior and completion checks | Existing test-driven-development and verification-before-completion as applicable; reuse project tests and the governing workflow. No separate testing package required. |

Start with the actual task. A UI spacing fix loads none of these backend modules. A booking API loads API/data/auth guidance that matches its stack. A webhook loads provider verification/retry/idempotency guidance; it does not require microservices. Add further skills only for a demonstrated gap.

## Sources and installation provenance

The authoritative [dependency lock](../dependencies.lock.json) records pinned revisions; [credits](../CREDITS.md) records publishers and license sources. Installation downloads source only, without executing upstream scripts. Pinning is not a security or runtime-compatibility certification. Review updates separately from feature work; no automatic provider/account provisioning.
