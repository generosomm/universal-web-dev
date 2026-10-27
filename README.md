<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-dark.svg">
  <img src=".github/assets/banner-light.svg" width="100%" alt="Universal Web Dev: any website your AI builds, planned, distinctive, and checked before it ships.">
</picture>

<br>

[![Checks](https://github.com/generosomm/universal-web-dev/actions/workflows/check.yml/badge.svg)](https://github.com/generosomm/universal-web-dev/actions/workflows/check.yml)
![Price](https://img.shields.io/badge/price-free-17703f?style=flat-square)
![Skills](https://img.shields.io/badge/skills-33%20pinned-17703f?style=flat-square)
![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex-0d1411?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)
[![License](https://img.shields.io/badge/license-MIT-186B53?style=flat-square)](LICENSE)

**[Install](#install-in-one-message)** · **[What you get](#what-you-get)** · **[Launch score](#launch-readiness-score)** · **[How it works](#how-it-works)** · **[How to use it](#how-to-use-it)** · **[Included skills](#included-skills)** · **[Your stack](#works-with-your-stack)** · **[FAQ](#faq)**

</div>

---

### A free skill that helps your AI build websites you can actually launch

If you've asked an AI to build a website, you've probably seen the result: a centred headline, three icon cards and a soft gradient. It also tends to skip the boring parts that make a site ready to launch, like colour contrast, phone layouts, broken links and secrets left in the browser.

Universal Web Dev is one free skill you add to your coding assistant. For each request, it picks the right expert from 33 community skills and leaves the rest unloaded. You get a design that fits the business, a plan before any code, tests that prove it works, and a **Launch Readiness Score** that shows exactly what's left before you go live.

It works for any kind of site (portfolio, landing page, shop, booking system, dashboard, full-stack app) in any stack, and it never picks a framework for you.

**New to skills?** A skill is a folder of instructions your coding assistant reads when a task needs it. Until then, your assistant only sees each skill's short description, so installing many of them costs very little. The [FAQ](#faq) has the numbers.

<br>

## Install in one message

Paste this into Claude Code, Codex or any coding assistant that can run commands:

```text
install or update universal-web-dev and all of its skills from:
https://github.com/generosomm/universal-web-dev
follow INSTALL.md, preserve my customized skills, and report what changed.
```

Your assistant downloads this skill and the 33 skills it uses, each from a reviewed, pinned commit. Then it runs a check and tells you what it installed. Restart or refresh your assistant afterwards so it picks up the new skills.

- Updating later? Send the same message. Skills you edited or installed another way are kept and listed in the report, and never overwritten.
- Want a smaller setup? Say "core skills" instead of "all of its skills".

<details>
<summary><strong>Install it yourself instead</strong></summary>

<br>

You need Python 3.10 or newer. From a clone of this repository:

```sh
python scripts/install.py --host claude --profile all --sync           # preview, changes nothing
python scripts/install.py --host claude --profile all --sync --apply   # install
python scripts/doctor.py --profile all                                 # check
```

Use `--host codex` for Codex, or `--dest <folder>` for any other skills directory. Profiles: `core` (design, workflow, testing, speed and search), `lean` (adds Caveman), `backend` (API design, security review), `postgres` (Supabase's Postgres guidance), or `all`.

The installer never runs code from the skills it downloads. It keeps a backup whenever it replaces something, and rolls back if an install fails. Details are in [INSTALL.md](INSTALL.md).

</details>

<br>

## What you get

**A design made for the client.** Each new page gets its own layout, type and palette, based on what makes that business different from its competitors. Common AI patterns are banned and checked in a real browser, and your brand or an existing design always comes first.

**Only the help a task needs.** Fixing a typo loads nothing extra and a bug loads the debugging skill. The big design manuals load for new pages, not for every edit.

**A site that's ready to launch.** You get a plan before code, tests that check real behaviour, and a launch checklist that fits the site. A portfolio won't get a cookie banner or a bot check it doesn't need.

**A score you can show.** Say "check" or "audit" and you get a Launch Readiness Score from 0 to 100, with the evidence behind every point and the fixes that matter most. Freelancers can turn it into a plain-language handoff report for a client.

**The official expert for your stack.** It recognizes WordPress, Shopify, Laravel, Svelte, React, Stripe, Sanity, Prisma and more, and offers the official skill from that tool's maker, where one exists. See [works with your stack](#works-with-your-stack).

**Useful from the first minute.** If a companion skill isn't installed yet, it says so and uses a short built-in version of the essentials, so it still works on its own.

### Why it's different

Most skills are one specialist: a design manual, a debugging method, a token saver. Universal Web Dev is the project lead that coordinates them.

- It decides what *not* to load. Each routing row names the skills to skip, and settles conflicts (one design direction per project, one final review).
- Every skill is pinned to a reviewed commit with its license checked. The installer never runs downloaded code, keeps your edits, and rolls back if something fails.
- Its scores come only from checks that actually ran. Items it couldn't check are listed with how to run them, never guessed.

<br>

## Launch Readiness Score

Ask your assistant to `check` a site for a quick scan, or to `audit` it for every route and every applicable item. Each item is marked pass, partial or fail with the evidence. Items that don't apply are left out instead of lowering the score, and anything it couldn't check lowers the coverage figure shown next to the score.

Here is a real `check` of the reference site in this repository, unedited apart from shortening:

```text
Launch Readiness Score: 70/100, Needs work   Coverage: 21/25 (84%)
Mode: check   Site: examples/reference-site, served locally   Date: 2026-10-27

Category             Score  Weight  Status
Works as intended      88     20    Tide planner works, all 8 in-page links resolve, no console errors
Works for everyone     79     25    Every measured text passes contrast; one small tap target
Trust and safety       75     25    No secrets; third-party font and image requests without a privacy note
Speed                  67     15    No blocking scripts, images sized and lazy; font CSS blocks rendering
Found and shared       30     15    No canonical, share image, structured data or sitemap

Blockers: none
Top fixes: 1. Add LodgingBusiness structured data (S)   2. Add sitemap.xml and robots.txt (S)
           3. Add canonical URL and share image (S)     4. Self-host font and photos, or add a privacy note (M)
Not run: HTTPS (not deployed), worst-case content, Core Web Vitals field data
```

The full report, with evidence, impact and a fix for each finding, is in [readiness-check.md](https://github.com/generosomm/universal-web-dev/blob/main/examples/reference-site/docs/readiness-check.md). The scoring rules are in [readiness score](references/readiness-score.md).

| Say | You get |
| --- | --- |
| `check` | A quick scan of the home page and main flow: score, coverage, blockers, top five fixes |
| `audit` | Every public route and flow, measured where possible, with the full report |
| `handoff` | The latest results in plain words for a client, with who owns each open item |
| `compare` | Two real runs side by side, to show what your fixes changed |

<br>

## How it works

Think of Universal Web Dev as a project lead. It doesn't do every job itself. It reads your request, hands each part to the right specialist skill, and makes sure the work is checked before anyone calls it done.

Here's what happens when you ask for something:

1. You describe the work in plain words, like "fix the contact form" or "build a landing page for my bakery".
2. Your assistant sees that it's web work and opens this skill's routing table in [SKILL.md](SKILL.md). That file is small, about 2,000 tokens.
3. The table matches your request to one row. The row names the skills to load (usually one to three) and the ones to leave alone.
4. Your assistant reads only those skills and does the work. A new project gets a short plan first, then one working feature at a time with tests.
5. Before saying "done", it runs the project's checks and walks through the real user flow. When the site is about to go live, it also goes through the launch checklist below.
6. It tells you what changed, how it was checked, and anything it couldn't check.

A token is a small piece of text, roughly four characters, and it's what AI tools count when they bill you or fill their memory. Loading only the skills a task needs keeps that count low.

### How it picks skills

| You ask for | It loads | It skips |
| --- | --- | --- |
| A typo or copy fix | nothing extra | all design and backend guidance |
| Copy that sounds AI-written | Humanizer, working from your own words | design skills |
| A bug fix | systematic debugging | design skills |
| A new landing page or portfolio | Taste for direction, Impeccable for the final polish | backend guidance, a second design system |
| A dashboard or admin screen | Frontend Design, UI/UX Pro Max lookups | marketing-page art direction |
| A login, database or API | full-stack contracts, API and security guidance | design skills |
| A release | readiness checklist, Break UI, Mobile Native | anything outside the release |
| "Check my site" or "audit my site" | the Launch Readiness Score, Webapp Testing for the browser | code changes before the report |
| Slow pages | Performance, Core Web Vitals | guesses without a measurement |
| Search or AI-answer visibility | SEO and AEO best practices | design skills |
| A WordPress, Shopify or Laravel project | an offer to add that platform's official skill pack | packs for stacks you don't use |

All the routing lives in [SKILL.md](SKILL.md), about 8 KB.

### What gets checked before launch

Each item is marked done, pending, or "doesn't apply" with a reason, so a portfolio isn't put through checks meant for an online shop.

| Trust and safety | Found and shared | Works for everyone |
| --- | --- | --- |
| Privacy policy and terms that match what the site does | Meta titles and descriptions | Contrast checked with a measurement |
| No secrets in browser code | Social preview image and favicon | Keyboard focus and alt text |
| HTTPS and secure sessions | Sitemap and robots.txt | Phone, tablet and desktop layouts |
| Cookie consent only where needed | Heading order and structured data | Custom 404 and no broken links |
| Form validation and spam protection | Hreflang for multilingual sites | Fast pages: images, slow scripts |

See the full checklist in [website readiness](references/website-readiness.md). The [Launch Readiness Score](#launch-readiness-score) turns it into a number.

<br>

## See a site it built

Here's a one-page site for a fictional seaside guesthouse. It was built by following the skill from start to finish: planning documents, a dealt design direction, tests, browser checks and a final polish pass.

<table>
<tr>
<td width="62%"><img src=".github/assets/reference-desktop.jpg" alt="Saltrum reference site: a bottle-green page with the name in large gold letters and the sections stacked as tabbed file folders"></td>
<td width="38%" rowspan="2" valign="top"><img src=".github/assets/reference-phone.jpg" alt="The same page on a phone, with the folder tabs staggered across the width"></td>
</tr>
<tr>
<td><img src=".github/assets/reference-rooms.jpg" alt="The four rooms as green cards that fold into narrow spines as you scroll, with the active room open and its price and booking link"></td>
</tr>
</table>

The checks caught five real bugs before it was finished, including a script error that disabled every feature and a colour that failed contrast. The [code, tests and build record](https://github.com/generosomm/universal-web-dev/tree/main/examples/reference-site) are in `examples/`. The business and its content are made up.

<br>

## How to use it

After installing, there are two ways to start:

- Just describe web work. The skill turns on by itself when your request is about a website or a web app.
- Call it by name: type `/universal-web-dev` in Claude Code or `$universal-web-dev` in Codex, followed by what you want.

Then talk to it the way you'd brief a developer. For example:

```text
use universal-web-dev to plan a booking site for a small dental clinic with staff and admin roles.
```

```text
use universal-web-dev to continue this project's next feature, reuse the existing design,
and verify the whole flow before marking it done.
```

A few more things you might say, and what they lead to:

| You say | What happens |
| --- | --- |
| "The signup button doesn't work" | It finds the cause first with `systematic-debugging`, then fixes it |
| "Make this headline sound less like AI" | `humanizer` rewrites it from your own words |
| "Show me a few options for the hero" | It suggests `prototype` so you can flip between versions and pick one |
| "We launch on Friday, is it ready?" | It runs the launch checklist, `break-ui` and `mobile-native` |
| "Audit my site" | A Launch Readiness Score with evidence and the top fixes |
| "Why is the homepage so slow on my phone?" | `performance` measures first, then fixes the biggest cost |
| "Click through checkout and tell me what breaks" | `webapp-testing` drives a real browser and reads the console |
| "Write a handoff report for my client" | The latest score and open items, in plain words |
| "Do a security review" | `security-best-practices` reviews the code *(backend profile)* |
| "Keep your replies short" | `caveman` trims its answers *(lean profile)* |

For a new project, it writes short planning documents and a sprint plan before any code, then builds one working feature at a time. A sprint is one small, finished piece of the site, such as "visitors can book a room".

Some habits it follows while working with you:

- Your brand, your stack and your existing design come first. It won't swap your framework or restyle a page you already approved.
- When you approve a change in one place, it applies the same change to matching places across the site and tells you which ones it skipped and why.
- If it expects a request to look or work worse, it says so in a line and suggests something better before changing anything.
- It commits, pushes or publishes only when you ask in the conversation.
- To pause it for unrelated work, say "stop universal-web-dev".

<details>
<summary><strong>Project files it creates for a new site</strong></summary>

<br>

```text
README.md        what exists and how to run it
PROJECT.md       stack, structure, conventions
PRODUCT.md       users, critical flow, what "done" means
DESIGN.md        the visual direction and tokens
docs/
  sprint-plan.md   one status table for the whole build
  testing.md       real test commands
  sprints/S01.md   goal, acceptance, evidence
tests/
  sprints/S01/     tests mapped to acceptance
```

Existing projects keep their own structure. See [project bootstrap](references/project-bootstrap.md).

</details>

<br>

## Included skills

All 33 skills are listed below by their real names, the ones you'll see in your assistant and in [SKILL.md](SKILL.md). You don't have to call them yourself. Universal Web Dev picks the right ones for each task, except the two marked "only when you ask".

They come from 14 projects. Most projects add one skill, while [Superpowers](https://github.com/obra/superpowers) adds 14, [Emil's skills](https://github.com/emilkowalski/skills) adds 5 and [Web Quality Skills](https://github.com/addyosmani/web-quality-skills) adds 2. Every skill installs from a pinned commit listed in [dependencies.lock.json](dependencies.lock.json), and authors and licenses are in [CREDITS.md](CREDITS.md).

A profile is a bundle you choose at install time. `core` is installed for everyone. `lean`, `backend` and `postgres` are optional extras, and asking for "all of its skills" installs every profile.

### Planning and teamwork

From [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent. Profile: `core`.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 1 | `brainstorming` | Asks you questions, one at a time, to turn a rough idea into clear requirements. It suggests a couple of approaches and gets your OK before anything is built. | A new project where it's unclear what you want |
| 2 | `writing-plans` | Breaks a big build into small steps, each with the files to touch and how to test it, so you can review the plan before any code is written. | A build big enough to need several sprints |
| 3 | `executing-plans` | Works through a written plan one step at a time, runs the checks for each step, and stops to ask when something doesn't match the plan. | Carrying out a plan in the same conversation |
| 4 | `subagent-driven-development` | Gives each step of a plan to a fresh helper AI (a subagent), then reviews what it hands back before moving on. Each helper starts clean, so mistakes don't pile up. | Carrying out a plan, if your assistant can run helpers |
| 5 | `dispatching-parallel-agents` | Sends several helpers to work at the same time on jobs that don't depend on each other, like fixing three unrelated bugs. | Separate tasks, if your assistant can run helpers |
| 6 | `test-driven-development` | Writes a test that fails first, then writes just enough code to make it pass. You end up with proof that the feature works, and a test that catches it if it breaks later. | Any change to how the site behaves |
| 7 | `systematic-debugging` | Finds what is actually causing a bug before touching code: reproduce it, trace it, test one idea at a time. No guessing and no piling fixes on top of each other. | A bug or a failing test |
| 8 | `verification-before-completion` | Runs the real checks and reads the results before saying "done", "fixed" or "passing". If something wasn't checked, it says so. | The final check, and every release |
| 9 | `requesting-code-review` | Asks a reviewer (often a helper AI) to look over the changes against the plan and flag problems before they're merged. | Before merging work |
| 10 | `receiving-code-review` | Checks that each piece of review feedback is correct before acting on it, and pushes back on suggestions that would make things worse. | When review feedback comes in |
| 11 | `using-git-worktrees` | Makes a separate working copy of the project on its own branch, so experiments never touch your main files. | Risky or experimental work |
| 12 | `finishing-a-development-branch` | Wraps up finished work: confirms the tests pass, then offers to merge it, open a pull request, keep it, or throw it away. | When a piece of work is done |
| 13 | `using-superpowers` | Teaches your assistant how to find the skills above and when to use them. | Loaded by Superpowers itself |
| 14 | `writing-skills` | A guide to writing new skills and testing that they work. | Loaded by Superpowers itself, mainly for people who write skills |

### Writing code and copy

Profile: `core`.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 15 | `ponytail` | Makes the smallest change that fully solves the task. No extra files, libraries, settings or features you didn't ask for, and a short explanation you can read in one go. From [Ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert. | Writing or changing code |
| 16 | `humanizer` | Rewrites text that sounds like a chatbot so it sounds like a person. It removes stock phrases, filler and overblown claims, and keeps your facts. From [Humanizer](https://github.com/blader/humanizer) by Siqi Chen. | Headlines, intros, about text or button labels need a rewrite |

### Design

Profile: `core`.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 17 | `design-taste-frontend` | Also called Taste. Picks a design direction for a public page (layout, fonts, colours, photos) from a library of researched styles, then checks the page in a real browser against a list of generic AI looks and fixes what it finds. From [Taste](https://github.com/Leonxlnx/taste-skill) by Leonxlnx. | A new landing page, marketing page or portfolio |
| 18 | `frontend-design` | Sets a clear visual direction for app screens, where being easy to use matters more than flair: type, spacing, colour and layout that don't look like a template. From [Frontend Design](https://github.com/anthropics/skills) by Anthropic. | A new dashboard, admin area or app screen |
| 19 | `ui-ux-pro-max` | A searchable library of UX rules, colour palettes, font pairings, chart types and tips for each framework. Your assistant looks up just the answer it needs instead of reading the whole thing. From [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) by Next Level Builder. | A focused design question |
| 20 | `impeccable` | A final design review. It checks spacing, type, colour, contrast, accessibility and states like hover, loading and error, then polishes what needs it. From [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus. | Once, at the end of a design task |

### Feel and finishing touches

From [Emil's skills](https://github.com/emilkowalski/skills) by Emil Kowalski. Profile: `core`.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 21 | `emil-design-eng` | Polishes how things feel to use: animation timing, hover and press states, gestures, and the small details people notice without knowing why. | Buttons, menus, transitions or motion |
| 22 | `break-ui` | Fills a screen with worst-case content (very long names, empty lists, huge numbers, emoji, other languages) and reports everything that breaks, with a fix for each. | Before launch, on the main screens |
| 23 | `mobile-native` | Fixes the small things that make a website feel wrong on a phone, like inputs that zoom the page, sticky hover effects, or content hidden under the notch. | Before launch |
| 24 | `prototype` | Builds several genuinely different versions of a piece of UI and lets you flip between them, so you can keep the one that feels right. | Only when you ask; it may suggest it when the look is undecided |
| 25 | `pick-ui-library` | Recommends a proven, ready-made library for things like charts, code inputs, toasts or drag and drop, so they aren't built from scratch. | Only when you ask; it may suggest it before building one of these by hand |

### Testing, speed and search

Profile: `core`.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 26 | `webapp-testing` | Opens your site in a real browser with Playwright, clicks through flows, takes screenshots and reads console errors. Needs Python Playwright; without it, it reports that the browser check didn't run. From [Anthropic's skills](https://github.com/anthropics/skills). | Checking a flow, an audit, or before saying "done" |
| 27 | `performance` | Makes pages load faster: measures first, then fixes the biggest cost, such as a heavy image, blocking script or slow font. From [Web Quality Skills](https://github.com/addyosmani/web-quality-skills) by Addy Osmani. | A page feels slow, or an audit measures it as slow |
| 28 | `core-web-vitals` | Fixes Google's three page-experience scores: how fast the main content appears (LCP), how fast the page reacts (INP) and how much it jumps around (CLS). From the same project. | A Core Web Vitals score is poor |
| 29 | `seo-aeo-best-practices` | Gets pages found by search engines and quoted by AI answers: titles, structured data, sitemaps, and content written to be cited. From [Sanity's agent toolkit](https://github.com/sanity-io/agent-toolkit). | Search visibility, structured data, or the "Found and shared" part of an audit |

### Extras

Optional profiles, installed only if you choose them.

| # | Skill | What it does, in plain words | Used when |
| --- | --- | --- | --- |
| 30 | `caveman` | Makes your assistant's replies very short while keeping every technical fact. Profile: `lean`. From [Caveman](https://github.com/JuliusBrussee/caveman) by Julius Brussee. | You ask for short replies |
| 31 | `api-design-principles` | Rules for designing a clean REST or GraphQL API, the part of your app that other code talks to: naming, errors, paging and versions. Profile: `backend`. From [API Design](https://github.com/wshobson/agents) by Seth Hobson. | Designing an API |
| 32 | `security-best-practices` | Reviews Python, JavaScript, TypeScript or Go code for security problems and suggests safer defaults. Profile: `backend`. From [Security Best Practices](https://github.com/openai/skills) by OpenAI. | You ask for a security review |
| 33 | `supabase-postgres-best-practices` | Rules for Postgres databases: tables, migrations, queries, indexes, and RLS (row-level security, which controls which rows each user is allowed to see). Profile: `postgres`. From [Postgres Best Practices](https://github.com/supabase/agent-skills) by Supabase. | Any Postgres database work |

Also recommended, but not installed or pinned: components and icons from FeralUI, Motion Primitives, Magic UI, Cult UI, Animata, React Bits, Animate UI, Sonner, Lucide, lucide-animated, itshover, Tabler and Phosphor. Your AI adds them only when a project wants them, restyled to match the site's design. See [component sources](references/component-sources.md) for the rules and [credits](CREDITS.md#referenced-not-installed) for authors and licenses.

Some skills we looked at were left out because they overlap the ones above, touch your browser logins, send your work to other services, or have no license. [More skills](references/more-skills.md) lists them with the reasons, so your AI can suggest a safe one when a project needs it.

<br>

## Works with your stack

Many tools now publish official skills for their own products. Universal Web Dev doesn't install all of them, because a Shopify skill is no use on a WordPress site and every installed skill costs tokens. It recognizes your project's stack from its files and offers the matching official pack once, with its publisher and license. Nothing is installed without your OK.

| Stack | Official pack from |
| --- | --- |
| WordPress | WordPress contributors (GPL-2.0-or-later) |
| Shopify | Shopify (MIT) |
| Laravel | Laravel, through Laravel Boost (MIT) |
| Svelte and SvelteKit | the Svelte team (MIT) |
| React and Next.js | Vercel (MIT declared in the skill) |
| Stripe payments | Stripe (MIT) |
| Email | Resend (MIT), useful with any email provider |
| Sanity CMS | Sanity (MIT) |
| Prisma, Neon, Supabase | Prisma (MIT), Neon (Apache-2.0), Supabase (MIT, already the `postgres` profile) |
| Convex | Convex (Apache-2.0), offered only if you already use Convex |
| Clerk, Better Auth | linked only: neither repository has a license file |

The full list, with how each stack is detected, is in [stack packs](references/stack-packs.md). No official pack existed yet for Tailwind CSS, Nuxt, Astro, Drizzle or Django when this was checked.

<br>

## FAQ

<details>
<summary><strong>Is it really free?</strong></summary>

<br>

Yes. Universal Web Dev is MIT licensed and free to use, share and change, including for client work. The skills it installs are open source under their own licenses, and none of them need an account or a paid service.

</details>

<details>
<summary><strong>Does installing 33 skills make my assistant slower or more expensive?</strong></summary>

<br>

Barely. An installed skill costs only its description until it's used. Here's what we measured on a full install (characters ÷ 4, a rough token estimate):

| What | Tokens | When |
| --- | --- | --- |
| All 34 skill descriptions | about 2,600 | Once per conversation, about one page of text |
| This skill's routing | about 2,000 | Each web task |
| Every skill's full instructions added up | about 91,000 | Never all at once: a request loads only the one to three skills its routing row names |

A typo loads nothing extra. A new landing page loads Taste and, at the end, Impeccable. Backend and Postgres guidance stay unloaded on a static site. `Prototype` and `Pick UI Library` load only when you invoke them yourself, in assistants that honour that setting, such as Claude Code.

</details>

<details>
<summary><strong>Will it overwrite skills I already have or have edited?</strong></summary>

<br>

No. Sync installs missing skills and updates only the copies it installed itself that you haven't changed. Everything else stays as it is and is listed in the report.

</details>

<details>
<summary><strong>Which AI tools does it work with?</strong></summary>

<br>

Claude Code and Codex have built-in install paths (`--host claude`, `--host codex`). Other assistants that support agent skills work with `--dest <their skills folder>`. A chat-only AI without file and terminal access can't install skills, but it can give you the commands to run.

</details>

<details>
<summary><strong>Does it pick a framework, database or style for me?</strong></summary>

<br>

No. Your stack, brand and existing design come first. Static sites don't get an invented backend, and business systems get real permission and data rules.

</details>

<details>
<summary><strong>Is Impeccable fully installed?</strong></summary>

<br>

Its design guidance is. Its optional launcher downloads a separate program that isn't pinned, so the installer leaves the launcher out and Impeccable uses its documented fallback. If you want live browser mode and its automatic detector, set up the launcher from [the upstream project](https://github.com/pbakaus/impeccable).

</details>

<details>
<summary><strong>How do the pinned versions stay current?</strong></summary>

<br>

Maintainers run `python scripts/check-updates.py`, review any changes to installed files, and release new pins. Your install updates when you send the install message again. The [release checklist](docs/release-checklist.md) records what has been verified.

</details>

<br>

## Status and limits

This is a community preview. The installer, the checker and a static reference site are tested on Windows and in CI on Linux and Windows. Trials with business systems (logins, databases, roles) come next. The routing is tuned for medium-effort models such as Opus 5.5 and GPT 6.1 Sol, and works with higher settings too. No skill guarantees bug-free output; this one helps you catch problems earlier.

Want to contribute? Follow [AGENTS.md](https://github.com/generosomm/universal-web-dev/blob/main/AGENTS.md), keep changes focused, and include test evidence. Found a problem? [Open an issue](https://github.com/generosomm/universal-web-dev/issues) with your AI tool, your setup and what you expected, and remove any secrets or private project data first.

The [MIT license](LICENSE) covers this wrapper's own files. Each included skill keeps its own license. None of them are bundled here, and nothing here implies their authors endorse this project.

<div align="center">

<br>

Made by **[Merwin M. Generoso](https://generosomm.dev)** · [GitHub](https://github.com/generosomm)

</div>
