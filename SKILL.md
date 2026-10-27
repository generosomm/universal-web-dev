---
name: universal-web-dev
description: Use when planning, building, fixing, reviewing, or releasing websites and web-based business systems, including landing pages, portfolios, dashboards, portals, commerce, booking, inventory, and full-stack applications, or when explicitly invoked. Not for non-web work.
---

# Universal Web Dev

Build the smallest complete system that satisfies the brief. Project type, user roles, risk, existing code and chosen stack are inputs; no framework, database, palette or industry is assumed. Project instructions and accepted designs win over this skill. This skill grants no permission to deploy, spend money, migrate production data or message third parties.

## Route each task to the fewest skills

Load a skill only when its row applies; read its SKILL.md once per conversation and its references only for the question at hand. If a skill is missing, say so, use [the built-in fallback](references/fallback.md) for that row, and continue. Never claim a skill ran when it did not. When a project uses a stack or service with an official skill pack (WordPress, Shopify, Laravel, Svelte, React, Stripe, Sanity, Prisma and others), check [stack packs](references/stack-packs.md) once per project and offer the pack; install only with approval.

| Task | Load | Do not load |
| --- | --- | --- |
| Typo, label or config fix, or copy the user supplied word for word | nothing extra | design or backend guidance |
| Copy that reads AI-written or needs a rewrite: headlines, intros, about text, CTAs | `humanizer`, on the user's own words | design skills |
| Bug or failing test | `systematic-debugging`; `webapp-testing` to reproduce a UI bug in a browser | design skills |
| New feature in an existing project | `ponytail`; `test-driven-development` when behavior changes | a new design direction; reuse the accepted one |
| New marketing page, landing page, portfolio | `design-taste-frontend` full run, then `impeccable` polish | `frontend-design`, backend references |
| Change to an existing page | the project's accepted design; Taste house rules only if Taste set its direction | a new direction |
| App screens, dashboard, admin, portal | `frontend-design` for direction; `ui-ux-pro-max` for focused lookups | `design-taste-frontend` |
| Component states, gestures, motion | `emil-design-eng` | a full redesign |
| Backend, database, auth, integrations | [full-stack contracts](references/full-stack.md) sections and [backend routing](references/backend-skills.md) | design skills |
| Empty project | [project bootstrap](references/project-bootstrap.md); `brainstorming` only if requirements are unclear; `writing-plans` only for multi-sprint builds | implementation code before the plan |
| Carrying out a written plan, code review, or finishing a branch | `executing-plans`, or `subagent-driven-development` and `dispatching-parallel-agents` when the host runs subagents; `requesting-code-review` before merge, `receiving-code-review` for feedback; `using-git-worktrees` for isolated work, `finishing-a-development-branch` to wrap up | a new design direction |
| Kickoff planning, or a release when the site is about to go live | [website readiness](references/website-readiness.md), `verification-before-completion`; for UI releases `break-ui` on the main screens and `mobile-native` | checks outside the release scope; release checks on a first draft |
| An explicit request to check or audit the whole site, score it, write a client handoff report, or compare two scores | [Launch Readiness Score](references/readiness-score.md); `webapp-testing` for browser checks | code changes before the report; a score for anything not checked; checking one component or comparing design options |
| Slow pages, Core Web Vitals, page weight | `performance`, and `core-web-vitals` for LCP, INP or CLS | guesses without a measurement |
| Search or AI-answer visibility: metadata, structured data, sitemaps | `seo-aeo-best-practices` | design skills |
| Clicking through a flow, screenshots, console errors in a real browser | `webapp-testing` | the readiness score unless asked |

Use one design direction skill per project; when skills disagree on a visual rule, it wins. Run `impeccable` once as the final review: its `polish` playbook, or `audit` when release needs a measured report; `critique` (seven times larger) only when asked, never on every edit; without its `scripts/` folder, use its documented fallback. Query `ui-ux-pro-max` narrowly, running its scripts from the installed skill folder, and never generate a new design system per change. Suggest, never auto-run, the explicit-only `prototype` when looks are undecided and `pick-ui-library` before hand-building charts, OTP inputs, drag and drop or similar widgets. Read [component sources](references/component-sources.md) before adding icon or UI component libraries.

## Plan

- Read the repository's own instructions and existing decisions first.
- For a new system, establish the goal, users and roles, critical workflow, data ownership, constraints, stack, hosting and acceptance examples. Ask only questions that block progress; label assumptions.
- Record a short approved plan in the project docs. Business systems need permission and data contracts before code. Small fixes reuse existing docs.

## Build

- Implement with `ponytail`: deliver one complete vertical feature at a time through the UI, API and database layers it needs.
- Reuse existing patterns and tools. Add a service, abstraction or dependency only for a concrete need.
- Static sites get no invented backend. Business systems get real server-side validation and authorization.
- Keep the sprint ledger and test evidence current while working, not only at handoff.

## Work with the developer

- A change the developer asks for or accepts in one section (alignment, spacing, a fix, a style) is a site-wide rule: find every place with the same pattern and apply it in the same change. Skip any place where it would look or work worse, such as a timeline or form whose structure depends on its alignment, and name each skipped place with the reason.
- When you expect a request to look or work worse, your first reply is the reason in one line plus a better option, with no edits; build after the developer chooses.
- When looks are undecided, show two or three real options side by side (rendered mockups, a prototype page or screenshots) and build only the pick.
- After adding or moving UI, rerun the project's existing layout and regression checks.
- Commit, push, deploy or publish only when asked in this conversation.

## Save tokens without losing quality

- Search for named files and symbols before reading; read only the relevant section of a large file, limit command output, and reuse context already loaded instead of rereading it.
- Investigate a failure before changing code. After two failed attempts, stop and reassess.
- Cut speculative work, never necessary tests, validation or error handling.
- Do not promise bug-free output or a specific token saving.

## Verify and report

Test meaningful behavior, including denied, invalid and failure cases. Run the repository's required checks and walk through the real user flow. Viewport emulation is not device testing, and mocks are not proof that a live integration works. Before calling a layout done on phones, run the [phone checks](references/website-readiness.md#phones). If a skill's checking script cannot run, use its documented fallback and report that the check did not run. Respect review gates and release authorization, and verify deployed behavior after release.

Report what changed, the evidence and what remains unverified, in a few lines in the user's language. If the optional `caveman` skill is installed and the user asked for terse replies, use it; otherwise write plain, short sentences. Code, docs and PR language follow the project's conventions.

For a capability no row covers, such as diagrams, web research or finding another skill, read [more skills](references/more-skills.md) before installing anything. For a request to install or update this skill from its repository link, follow [INSTALL.md](INSTALL.md) and do not start a website project. For missing dependencies or sharing, read [sharing and dependencies](references/sharing.md). Pause this skill for unrelated work, or stop on "stop universal-web-dev". Do not change global instructions or hooks.
