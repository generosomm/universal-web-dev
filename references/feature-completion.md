# Prove the promised outcome

Use for new features and completion/release checks. Extend the existing acceptance record instead of creating a second tracker. A tiny fix needs only its focused evidence.

For each promised user-visible feature record: **outcome | implementation mode | acceptance/check | evidence/environment | status | remaining dependency**. Modes are real implementation, sandbox, or demo/mock. Statuses are planned, implemented but unverified, verified in the named environment, blocked, or intentionally deferred. "Verified locally" does not mean "verified in production". Keep data/provider boundaries visible.

## Minimum evidence by feature

| Feature | Evidence that matters |
| --- | --- |
| Navigation, CTA, downloads | Actual destination/action, deep-link/reload behavior, correct file and mobile/keyboard access |
| Contact/newsletter/email | Server/provider acceptance, invalid input, failure feedback and duplicate-submit handling; recipient delivery separately checked. An API 200 or toast is not inbox delivery |
| CRUD, settings, cart | Relevant create/read/update/delete flow; persisted values survive reload/new session as required. Browser storage is not a shared database |
| Search, filters, pagination | Known matching/no-match inputs, reset/navigation and representative data; search scope matches the promise |
| Login and roles | Valid/invalid/expired session, logout, recovery if promised; denied direct request and another user's/tenant's object ID. Hiding a button proves nothing |
| Bookings, stock, orders | Server validation and durable persistence; concurrent and duplicate requests preserve the recorded invariant |
| Payments/webhooks | Provider sandbox result and server-verified event, signature/idempotency checks and failure/cancel recovery. A browser success redirect is insufficient |
| Uploads/user content | Allowed type/size/content rules, permissions, unsafe input handling, failed upload and access to the stored result |
| CMS/admin | Owner can perform the promised update and published/user-visible data actually changes |

Select relevant cases rather than running every row. Reuse tests/fixtures and available browser tools. Run required build/lint/tests and the critical user journey. Inspect console and failed network requests where browser access exists. Test relevant loading/empty/error/success/disabled states and retry without duplicate side effects. Use [full-stack contracts](full-stack.md) for backend details.

## Missing tools or provider access

Build and test independent local behavior. Mark mocks explicitly, keep privileged configuration server-side, provide an accurate environment example and concise setup instructions. Never silently substitute a demo for a promised integration. State the specific missing account/tool/credential or owner action and how to finish verification. Do not ask users to paste secrets into chat or commit them.

A feature blocked on email credentials stays blocked for live delivery even if local tests pass. If browser access is unavailable, run available non-browser checks and provide a short manual flow, but leave browser/visual acceptance unverified. Do not silently drop features to get a passing result.

## Handoff

Report what works and where it was verified, required setup and costs, and unresolved features with the smallest next action. For a new site include the actual local run/preview command and how the owner changes content. Distinguish built, verified, deployed and launch-ready. The whole site is not fully working while a promised critical outcome is demo-only, blocked or unverified. A scoped prototype can still be complete as a prototype.
