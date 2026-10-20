---
name: universal-web-dev
description: Use when planning, building, fixing, reviewing, or releasing websites and web-based business systems, including dashboards, portals, commerce, booking, inventory, and full-stack applications, or when explicitly invoked.
---

# Universal Web Dev

Build the smallest complete system that satisfies the brief. Treat project type, user roles, risk, existing code and chosen stack as inputs, not fixed defaults. Works across stacks and industries; no game, palette, framework or database is assumed. Use the current project's rules and accepted design. This skill grants no deployment, spending, data-migration or third-party messaging permission.

## Eight core skills

Resolve names from the current skill catalog, not machine-specific paths. If unavailable, name the missing dependency and use available guidance without claiming full coverage. Read applicable entrypoints before applying them, once per conversation unless changed; supplied instructions count. Follow their own references and triggers.

| Skill | Responsibility |
| --- | --- |
| `using-superpowers` | Select the applicable planning, debugging, testing and verification workflow |
| `ponytail` | Smallest complete implementation, default full level |
| `caveman` | Concise updates in the user's preferred language; retain exact technical details |
| `frontend-design` | Product-specific concept and visual structure |
| `design-taste-frontend` | Art direction, typography and composition |
| `ui-ux-pro-max` | Focused UX, accessibility, responsive and stack guidance |
| `emil-design-eng` | Component states, purposeful motion and interaction polish |
| `impeccable` | Hierarchy, consistency and final usability review |

Use applicable capabilities across new-site phases: workflow/scope (Superpowers, Ponytail, Caveman), concept (Frontend Design, Taste), implementation (UI/UX Pro Max, Emil), final usability review (Impeccable). Cover each applicable responsibility once, not eight full audits. Static sites need no invented backend; business systems need real permission/data contracts. Honor host tool APIs and explicit-only triggers over upstream examples. UI/UX scripts use the actual installed skill root, not hardcoded host paths. Existing tasks load only applicable skills. Backend-only work needs no design pass. New visual direction needs a product-specific plan; accepted designs are reused. UI/UX Pro Max uses focused queries for specific concerns, not a fresh design system on every change.

## Empty-project bootstrap

Before application code in an empty project, read [project bootstrap](references/project-bootstrap.md). Create the compact root docs, sprint ledger and first sprint/test records; honor applicable plan/design review gates. Reuse existing structures when continuing a project. Update sprint status and test evidence during implementation, not only at handoff.

## Plan and build

- Read governing repository instructions and relevant existing decisions. For a new system establish the goal, actors/roles, critical workflow, data ownership, constraints, stack/deployment and acceptance examples. Ask only blocking questions; label assumptions.
- Record a compact approved plan in existing project docs. For business systems include permission and data/state contracts before coding. Keep later documentation proportional; small fixes reuse existing docs.
- Deliver one complete vertical feature through the necessary UI, API and database layers. Choose a small representative user flow early. Reuse existing patterns and installed tools; don't introduce services, abstraction layers or dependencies without a concrete need.
- For backend, database, auth or integration work, read the applicable sections of [full-stack contracts](references/full-stack.md) and select modules from [backend skill routing](references/backend-skills.md). Preserve validation, authorization and safe migrations.
- At kickoff/release read [website readiness](references/website-readiness.md); during a feature consult only affected checks. Record verified, pending or not applicable with a reason. A checklist is not authority to add tracking or unrelated features.

## Keep context lean

Load details on demand. Reuse unchanged skill/project context. Search named files/symbols first; bound command output and dataset searches. Keep a short handoff of decisions, current feature, acceptance checks and remaining limits in existing docs. Investigate failures before changing code; stop repeated blind retries. Necessary tests and failure handling stay; speculative work goes. Don't promise bug-free output or a token-saving percentage.

## Verify and deliver

Use the selected testing workflow for meaningful behavior, including relevant denied/invalid/failure cases. Run repository-required checks and exercise the actual user flow. Browser viewport emulation is not physical-device testing; mocks are not live integration proof. Respect review gates and existing release authorization, then verify deployed behavior.

For installation, missing dependencies or community export, read [sharing and dependencies](references/sharing.md).

Report changes, evidence and limits briefly in the user's preferred language. Follow project conventions for code/docs/PR language. Communication skills do not impose a language or persona. Example: `Use $universal-web-dev to plan a PHP/MySQL inventory system with admin and staff roles.` Suspend for unrelated work or stop on "normal mode" / "stop universal-web-dev". Don't change global instructions or hooks.
