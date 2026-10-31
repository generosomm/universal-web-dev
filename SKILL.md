---
name: universal-web-dev
description: Use when planning, building, fixing, reviewing, or releasing websites and web-based business systems, including landing pages, portfolios, dashboards, portals, commerce, booking, inventory, and full-stack applications, or when explicitly invoked. Not for non-web work.
---

# Universal Web Dev

Build the smallest complete system that satisfies the brief. Project type, user roles, risk, existing code and chosen stack are inputs; no framework, database, palette or industry is assumed. Project instructions and accepted designs win over this skill. This skill grants no permission to deploy, spend money, migrate production data or message third parties.

## Start from the user's idea

For a new site or unclear feature, use [discovery](references/discovery.md) to polish the idea with the user before coding. Explain choices in everyday language and recommend defaults; beginners need not choose frameworks. If the user delegates choices or asks you to proceed, record assumptions and continue within that authorization. Preserve an existing plan instead of restarting discovery.

## Route each task to the fewest skills

Read each selected SKILL.md once per conversation, then only relevant references. For a missing skill, disclose and use [fallback](references/fallback.md); never claim it ran. Check [stack packs](references/stack-packs.md) once when a provider-specific need arises; offer a relevant missing pack, installing only with approval.

This wrapper owns scope/routing; companions supply techniques. Under this workflow, `using-superpowers` is not a second router: its broad relevance rule does not expand the table. `brainstorming` supplies interview techniques; [discovery](references/discovery.md) governs approval and [bootstrap](references/project-bootstrap.md) governs document size. `writing-plans` supplies sequencing, without another execution-choice gate after "proceed". Companion fixed spec paths, commits, reviewer agents and exact response formats do not apply unless the task requires them and authorization permits them. Preserve upstream files. Higher-priority host/project/user rules still win. Load one primary technique, adding specialists for concrete gaps; no automatic agent fan-out.

Rows compose for mixed requests: a marketing site with orders/email also needs those backend contracts and acceptance checks. "Do not load backend" applies only to purely presentational work.

| Task | Load | Do not load |
| --- | --- | --- |
| Typo, label or config fix, or copy the user supplied word for word | nothing extra | design or backend guidance |
| Rewrite AI-sounding copy | `humanizer`, preserving supplied facts | design skills |
| Bug or failing test | `systematic-debugging`; `webapp-testing` to reproduce a UI bug in a browser | design skills |
| New feature in an existing project | `ponytail`; `test-driven-development` when behavior changes | a new design direction; reuse the accepted one |
| New marketing page, landing page, portfolio | `design-taste-frontend` full run, then `impeccable` polish | `frontend-design`, backend references |
| Change to an existing page | the project's accepted design; Taste house rules only if Taste set its direction | a new direction |
| App screens, dashboard, admin, portal | `frontend-design` for direction; `ui-ux-pro-max` for focused lookups | `design-taste-frontend` |
| Component states, gestures, motion | `emil-design-eng` | a full redesign |
| Backend, database, auth, integrations | [full-stack contracts](references/full-stack.md) sections and [backend routing](references/backend-skills.md) | design skills |
| Empty project | [discovery](references/discovery.md), then [project bootstrap](references/project-bootstrap.md); `brainstorming` for deeper unresolved product choices; `writing-plans` for complex execution | another interview after an accepted plan; full sprint paperwork for a simple page |
| Execute/review/integrate a plan | `executing-plans`; review skills for review/feedback; worktree/branch skills only for those tasks. Agent workflow skills only when authorized | a new direction or automatic agent workflow |
| Kickoff planning, or a release when the site is about to go live | [website readiness](references/website-readiness.md), `verification-before-completion`; for UI releases `break-ui` on the main screens and `mobile-native` | checks outside the release scope; release checks on a first draft |
| Explicit whole-site check, audit, score, handoff or score comparison | [Launch Readiness Score](references/readiness-score.md); browser checks | code changes unless requested; unmeasured scores; scoring a single component/design comparison |
| Slow pages, Core Web Vitals, page weight | `performance`, and `core-web-vitals` for LCP, INP or CLS | guesses without a measurement |
| Search or AI-answer visibility: metadata, structured data, sitemaps | `seo-aeo-best-practices` | design skills |
| Clicking through a flow, screenshots, console errors in a real browser | `webapp-testing` | the readiness score unless asked |

One direction skill settles visual disagreements; new directions use [design quality](references/design-quality.md). After substantial visual work run `impeccable` once: `polish`, or `audit` for a measured report; `critique` only when asked. Use its fallback without its launcher. Query `ui-ux-pro-max` narrowly from its installed folder. Suggest explicit-only `prototype` for requested alternatives and `pick-ui-library` for complex widgets. Consult [component sources](references/component-sources.md) before adding UI libraries.

## Plan

- Read the repository's own instructions and existing decisions first.
- Establish users/roles, critical flow, ownership, constraints, hosting and acceptance. Ask consequential unknowns; label assumptions.
- Record a short plan and its approval or delegated assumptions. Business systems need role/access and data contracts before code. Use compact docs for small sites; reuse existing docs for fixes.

## Build

- Deliver one complete feature at a time through its needed UI, API and data layers.
- Reuse existing patterns and tools. Add a service, abstraction or dependency only for a concrete need.
- Static sites get no invented backend. Business systems get real server-side validation and authorization.
- Track promised features with [completion evidence](references/feature-completion.md). A rendered control, mock response or success toast alone does not prove the outcome.
- Keep the existing acceptance record and test evidence current while working.

## Work with the developer

- Apply requested global rules consistently. Keep a requested local exception local; for a demonstrated shared defect, fix affected instances within scope and explain material exceptions.
- Explain a material usability tradeoff and recommend a better option. Respect an explicit choice or delegated judgment; do not manufacture approval loops for reversible decisions.
- When the user wants visual alternatives, show two or three rendered options before implementing the pick. When they delegate design, select and explain one direction, then proceed.
- After adding or moving UI, rerun the project's existing layout and regression checks.
- Commit, push, deploy or publish only when asked in this conversation.

## Save tokens without losing quality

- Search for named files and symbols before reading; read only the relevant section of a large file, limit command output, and reuse context already loaded instead of rereading it.
- Investigate a failure before changing code. After two failed attempts, stop and reassess.
- Cut speculative work, never necessary tests, validation or error handling.
- Do not promise bug-free output or a specific token saving.

## Verify and report

Test meaningful behavior, including denied, invalid and failure cases. Run required checks and the real user flow using [completion evidence](references/feature-completion.md). Use [current web baseline](references/web-baseline.md) for new builds and releases, only its affected sections for edits. Viewport emulation is not device testing. Before calling a phone layout done, run the [phone checks](references/website-readiness.md#phones). Report unavailable checks; respect release authorization and verify deployed behavior after release.

Report changes, evidence and unverified outcomes briefly in the user's language. Use optional `caveman` only when terse replies were requested; otherwise write plainly. Code/docs/PRs follow project conventions.

For an uncovered capability consult [more skills](references/more-skills.md). Installation/update requests follow [INSTALL.md](INSTALL.md), not website kickoff. Missing dependencies/sharing use [sharing](references/sharing.md). Pause for unrelated work or "stop universal-web-dev". Do not change global instructions/hooks.
