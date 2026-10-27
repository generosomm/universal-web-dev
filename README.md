<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-dark.svg">
  <img src=".github/assets/banner-light.svg" width="100%" alt="Universal Web Dev: any website your AI builds, planned, distinctive, and checked before it ships.">
</picture>

<br>

[![Checks](https://github.com/generosomm/universal-web-dev/actions/workflows/check.yml/badge.svg)](https://github.com/generosomm/universal-web-dev/actions/workflows/check.yml)
![Skills](https://img.shields.io/badge/skills-29%20pinned-17703f?style=flat-square)
![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex-0d1411?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)
[![License](https://img.shields.io/badge/license-MIT-186B53?style=flat-square)](LICENSE)

**[Install](#install-in-one-message)** · **[What you get](#what-you-get)** · **[How it works](#how-it-works)** · **[How to use it](#how-to-use-it)** · **[See a site it built](#see-a-site-it-built)** · **[Included skills](#included-skills)** · **[FAQ](#faq)**

</div>

---

### Help your AI build websites that look designed and actually work

If you've asked an AI to build a website, you've probably seen the result: a centred headline, three icon cards and a soft gradient. It also tends to skip the boring parts that make a site ready to launch, like colour contrast, phone layouts, broken links and secrets left in the browser.

Universal Web Dev is one skill you add to your coding assistant. For each request, it picks the right expert from 29 community skills and leaves the rest unloaded. You get a design that fits the business, a plan before any code, and a checklist before launch, without paying for every manual on every edit.

**New to skills?** A skill is a folder of instructions your coding assistant reads when a task needs it. Until then, your assistant only sees each skill's short description, so installing many of them costs very little. The [FAQ](#faq) has the numbers.

<br>

## Install in one message

Paste this into Claude Code, Codex or any coding assistant that can run commands:

```text
install or update universal-web-dev and all of its skills from:
https://github.com/generosomm/universal-web-dev
follow INSTALL.md, preserve my customized skills, and report what changed.
```

Your assistant downloads this skill and the 29 skills it uses, each from a reviewed, pinned commit. Then it runs a check and tells you what it installed. Restart or refresh your assistant afterwards so it picks up the new skills.

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

Use `--host codex` for Codex, or `--dest <folder>` for any other skills directory. Profiles: `core` (design and workflow), `lean` (adds Caveman), `backend` (API design, security review), `postgres` (Supabase's Postgres guidance), or `all`.

The installer never runs code from the skills it downloads. It keeps a backup whenever it replaces something, and rolls back if an install fails. Details are in [INSTALL.md](INSTALL.md).

</details>

<br>

## What you get

**A design made for the client.** Each new page gets its own layout, type and palette, based on what makes that business different from its competitors. Common AI patterns are banned and checked in a real browser, and your brand or an existing design always comes first.

**Only the help a task needs.** Fixing a typo loads nothing extra and a bug loads the debugging skill. The big design manuals load for new pages, not for every edit.

**A site that's ready to launch.** You get a plan before code, tests that check real behaviour, and a launch checklist that fits the site. A portfolio won't get a cookie banner or a bot check it doesn't need.

<br>

## How it works

Think of Universal Web Dev as a project lead. It doesn't do every job itself. It reads your request, hands each part to the right specialist skill, and makes sure the work is checked before anyone calls it done.

Here's what happens when you ask for something:

1. You describe the work in plain words, like "fix the contact form" or "build a landing page for my bakery".
2. Your assistant sees that it's web work and opens this skill's routing table in [SKILL.md](SKILL.md). That file is small, about 1,700 tokens.
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

All the routing lives in [SKILL.md](SKILL.md), about 7 KB.

### What gets checked before launch

Each item is marked done, pending, or "doesn't apply" with a reason, so a portfolio isn't put through checks meant for an online shop.

| Trust and safety | Found and shared | Works for everyone |
| --- | --- | --- |
| Privacy policy and terms that match what the site does | Meta titles and descriptions | Contrast checked with a measurement |
| No secrets in browser code | Social preview image and favicon | Keyboard focus and alt text |
| HTTPS and secure sessions | Sitemap and robots.txt | Phone, tablet and desktop layouts |
| Cookie consent only where needed | Heading order and structured data | Custom 404 and no broken links |
| Form validation and spam protection | Hreflang for multilingual sites | Fast pages: images, slow scripts |

See the full checklist in [website readiness](references/website-readiness.md).

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

Every skill installs from a pinned commit listed in [dependencies.lock.json](dependencies.lock.json). Authors and licenses are in [CREDITS.md](CREDITS.md).

| Skill | By | What it does here | Loads when |
| --- | --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Jesse Vincent | Planning, debugging, test-driven development, code review, verification (14 skills; `using-superpowers` and `writing-skills` are loaded by Superpowers itself) | One at a time: a bug, a behaviour change, a written plan, a review, or the final check |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Dietrich Gebert | The smallest change that fully solves the task | Writing or changing code |
| [Humanizer](https://github.com/blader/humanizer) | Siqi Chen | Rewrites website copy that reads AI-written, in your own voice | Copy needs a rewrite |
| [Taste](https://github.com/Leonxlnx/taste-skill) | Leonxlnx | Art direction that avoids generic AI pages | A new marketing page or portfolio |
| [Frontend Design](https://github.com/anthropics/skills) | Anthropic | Direction for app screens and dashboards | A new app screen or dashboard |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Next Level Builder | Searchable UX, accessibility and stack guidance | A focused lookup, not a full read |
| [Emil's skills](https://github.com/emilkowalski/skills) | Emil Kowalski | Interaction polish, Break UI, Mobile Native, Prototype, Pick UI Library | Motion and component states; Break UI and Mobile Native at release; Prototype and Pick UI Library only when you ask |
| [Impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus | Final polish, audit and accessibility review | Once, as the final review |
| [Caveman](https://github.com/JuliusBrussee/caveman) | Julius Brussee | Terse replies when you ask for them *(lean profile)* | You ask for short replies |
| [API Design](https://github.com/wshobson/agents) | Seth Hobson | REST and GraphQL contracts *(backend profile)* | Designing an API |
| [Security Best Practices](https://github.com/openai/skills) | OpenAI | Security review on request *(backend profile)* | You ask for a security review |
| [Postgres Best Practices](https://github.com/supabase/agent-skills) | Supabase | Schemas, queries, RLS *(postgres profile)* | Postgres work |

### Every skill, in plain words

Each name below is the skill's real name, the one you'll see in your assistant and in [SKILL.md](SKILL.md). You never have to call these yourself, except the two marked "only when you ask". Universal Web Dev picks them for you.

A profile is a bundle you choose at install time. `core` is installed for everyone. `lean`, `backend` and `postgres` are extras, and "all of its skills" installs every profile.

**Planning and teamwork** (from Superpowers, `core`)

| Skill | In plain words | Used when |
| --- | --- | --- |
| `brainstorming` | Asks you questions to turn a rough idea into clear requirements | A new project where it's unclear what you want |
| `writing-plans` | Writes a step-by-step build plan you can review | A build big enough for several sprints |
| `executing-plans` | Follows a written plan one step at a time and checks each step | Carrying out a plan |
| `subagent-driven-development` | Gives each plan step to a helper AI and reviews what it hands back | Carrying out a plan, if your assistant can run helpers (subagents) |
| `dispatching-parallel-agents` | Runs several helpers at once on jobs that don't depend on each other | Separate tasks, if your assistant can run helpers |
| `test-driven-development` | Writes a test that fails first, then the code that makes it pass, so you know the feature works | Any change to how the site behaves |
| `systematic-debugging` | Finds what's actually causing a bug before touching code, instead of guessing | A bug or a failing test |
| `verification-before-completion` | Runs the checks and reads the results before claiming "done" | The final check, and every release |
| `requesting-code-review` | Asks a reviewer to look over the changes | Before merging work |
| `receiving-code-review` | Checks that review feedback is correct before acting on it | When feedback comes in |
| `using-git-worktrees` | Makes a separate copy of the project to work in, so your main files stay untouched | Risky or experimental work |
| `finishing-a-development-branch` | Wraps up finished work: tests pass, then merge, open a pull request or keep it | When a branch is done |
| `using-superpowers` | Teaches your assistant how to find and use the skills above | Loaded by Superpowers itself |
| `writing-skills` | A guide to writing and testing new skills | Loaded by Superpowers itself, mainly for skill authors |

**Writing code and copy** (`core`)

| Skill | In plain words | Used when |
| --- | --- | --- |
| `ponytail` | Makes the smallest change that fully solves the task, with no extra files, libraries or features you didn't ask for | Writing or changing code |
| `humanizer` | Rewrites text that sounds like a chatbot so it sounds like you, keeping your facts | Headlines, intros, about text or buttons need a rewrite |

**Design** (`core`)

| Skill | In plain words | Used when |
| --- | --- | --- |
| `design-taste-frontend` (Taste) | Picks a design direction for a public page (layout, fonts, colours, photos) and checks it in a browser against a list of generic AI looks | A new landing page, marketing page or portfolio |
| `frontend-design` | Design direction for app screens, where clarity matters more than flair | A new dashboard, admin area or app screen |
| `ui-ux-pro-max` | A searchable library of UX rules, colour palettes, font pairings and framework tips. Your assistant looks up one answer instead of reading it all | A focused design question |
| `impeccable` | A final design review of spacing, type, colour, accessibility and states like hover and error | Once, at the end of a design task |

**Feel and finishing touches** (from Emil Kowalski, `core`)

| Skill | In plain words | Used when |
| --- | --- | --- |
| `emil-design-eng` | Polishes how things feel to use: animations, hover and press states, gestures | Buttons, menus, transitions or motion |
| `break-ui` | Fills a screen with worst-case content (very long names, empty lists, huge numbers, emoji) and reports what breaks | Before launch, on the main screens |
| `mobile-native` | Fixes the small things that make a site feel wrong on a phone, like inputs that zoom the page or content hidden under the notch | Before launch |
| `prototype` | Builds several different versions of a piece of UI so you can flip between them and keep the best | Only when you ask; it may suggest it when the look is undecided |
| `pick-ui-library` | Recommends a ready-made library for charts, code inputs, drag and drop and similar widgets, so they aren't built from scratch | Only when you ask; it may suggest it before hand-building one |

**Extras** (optional profiles)

| Skill | In plain words | Used when |
| --- | --- | --- |
| `caveman` *(lean)* | Makes your assistant's replies very short while keeping every technical fact | You ask for short replies |
| `api-design-principles` *(backend)* | Rules for designing a clean API, the part of your app that other code talks to: URLs, errors, versions | Designing an API |
| `security-best-practices` *(backend)* | Reviews Python, JavaScript, TypeScript or Go code for security problems and suggests fixes | You ask for a security review |
| `supabase-postgres-best-practices` *(postgres)* | Rules for Postgres databases: tables, queries, indexes, and RLS (row-level security, which controls which rows each user can see) | Any Postgres database work |

Also recommended, but not installed or pinned: components and icons from FeralUI, Motion Primitives, Magic UI, Cult UI, Animata, React Bits, Animate UI, Sonner, Lucide, lucide-animated, itshover, Tabler and Phosphor. Your AI adds them only when a project wants them, restyled to match the site's design. See [component sources](references/component-sources.md) for the rules and [credits](CREDITS.md#referenced-not-installed) for authors and licenses.

Some skills we looked at were left out because they overlap the ones above, touch your browser logins, send your work to other services, or have no license. [More skills](references/more-skills.md) lists them with the reasons, so your AI can suggest a safe one when a project needs it.

<br>

## FAQ

<details>
<summary><strong>Does installing 29 skills make my assistant slower or more expensive?</strong></summary>

<br>

Barely. An installed skill costs only its description until it's used. Here's what we measured on a full install (characters ÷ 4, a rough token estimate):

| What | Tokens | When |
| --- | --- | --- |
| All 30 skill descriptions | about 2,200 | Once per conversation, about one page of text |
| This skill's routing | about 1,700 | Each web task |
| Every skill's full instructions added up | about 90,000 | Never all at once: a task loads only the one to three skills its routing row names |

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

This is a community preview. The installer, the checker and a static reference site are tested on Windows and in CI on Linux and Windows. Trials with business systems (logins, databases, roles) come next. No skill guarantees bug-free output; this one helps you catch problems earlier.

Want to contribute? Follow [AGENTS.md](https://github.com/generosomm/universal-web-dev/blob/main/AGENTS.md), keep changes focused, and include test evidence. Found a problem? [Open an issue](https://github.com/generosomm/universal-web-dev/issues) with your AI tool, your setup and what you expected, and remove any secrets or private project data first.

The [MIT license](LICENSE) covers this wrapper's own files. Each included skill keeps its own license. None of them are bundled here, and nothing here implies their authors endorse this project.

<div align="center">

<br>

Made by **[Merwin M. Generoso](https://generosomm.dev)** · [GitHub](https://github.com/generosomm)

</div>
