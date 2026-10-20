---
name: universal-web-dev
description: Use when planning, building, fixing, reviewing, or releasing websites and web-based business systems, including landing pages, portfolios, dashboards, portals, commerce, booking, inventory, and full-stack applications, or when explicitly invoked. Not for non-web work.
---

# Universal Web Dev

Build the smallest complete system that satisfies the brief. Project type, user roles, risk, existing code and chosen stack are inputs; no framework, database, palette or industry is assumed. Project instructions and accepted designs win over this skill. This skill grants no permission to deploy, spend money, migrate production data or message third parties.

## Route each task to the fewest skills

Load a skill only when its row applies. Read its SKILL.md once per conversation; open its references only for the specific question. If a skill is missing, say so and continue with the guidance you have. Never claim a skill ran when it did not.

| Task | Load | Do not load |
| --- | --- | --- |
| Typo, copy or config fix | nothing extra | design or backend guidance |
| Bug or failing test | `systematic-debugging` | design skills |
| New feature in an existing project | `ponytail`; `test-driven-development` when behavior changes | a new design direction; reuse the accepted one |
| Marketing page, landing page, portfolio | `design-taste-frontend` for direction, then `impeccable` review | `frontend-design`, backend references |
| App screens, dashboard, admin, portal | `frontend-design` for direction; `ui-ux-pro-max` for focused lookups | `design-taste-frontend` |
| Component states, gestures, motion | `emil-design-eng` | a full redesign |
| Backend, database, auth, integrations | [full-stack contracts](references/full-stack.md) sections and [backend routing](references/backend-skills.md) | design skills |
| Empty project | [project bootstrap](references/project-bootstrap.md), `brainstorming`, `writing-plans` | implementation code before the plan |
| Kickoff or release | [website readiness](references/website-readiness.md), `verification-before-completion` | checks outside the release scope |

Use one design direction skill per project; never run two against each other. Run `impeccable` once as the final usability review, not on every edit. Use `ui-ux-pro-max` with narrow queries, and do not generate a new design system for each change. Its scripts run from the actual installed skill folder, never a hardcoded path.

## Plan

- Read the repository's own instructions and existing decisions first.
- For a new system, establish the goal, users and roles, critical workflow, data ownership, constraints, stack, hosting and acceptance examples. Ask only questions that block progress; label assumptions.
- Record a short approved plan in the project docs. Business systems need permission and data contracts before code. Small fixes reuse existing docs.

## Build

- Implement with `ponytail`: deliver one complete vertical feature at a time through the UI, API and database layers it needs.
- Reuse existing patterns and tools. Add a service, abstraction or dependency only for a concrete need.
- Static sites get no invented backend. Business systems get real server-side validation and authorization.
- Keep the sprint ledger and test evidence current while working, not only at handoff.

## Save tokens without losing quality

- Search for named files and symbols before reading; read only the relevant section of a large file.
- Limit command output and dataset searches.
- Reuse context already loaded in this conversation instead of rereading it.
- Investigate a failure before changing code. After two failed attempts, stop and reassess.
- Cut speculative work, never necessary tests, validation or error handling.
- Do not promise bug-free output or a specific token saving.

## Verify and report

Test meaningful behavior, including denied, invalid and failure cases. Run the repository's required checks and walk through the real user flow. Viewport emulation is not device testing, and mocks are not proof that a live integration works. Respect review gates and release authorization, and verify deployed behavior after release.

Report what changed, the evidence and what remains unverified, in a few lines in the user's language. If the optional `caveman` skill is installed and the user asked for terse replies, use it; otherwise write plain, short sentences. Code, docs and PR language follow the project's conventions.

For a request to install or update this skill from its repository link, follow [INSTALL.md](INSTALL.md) and do not start a website project. For missing dependencies or sharing, read [sharing and dependencies](references/sharing.md). Pause this skill for unrelated work, or stop on "stop universal-web-dev". Do not change global instructions or hooks.
