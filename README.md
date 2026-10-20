<div align="center">

# Universal Web Dev

**Plan first. Build with intent. Verify the real flow.**

A flexible development skill for your AI coding assistant.

[Get started](#install-through-your-ai) · [The core skills](#dependencies-and-attribution) · [Setup guide](INSTALL.md) · [Portfolio](https://generosomm.dev)

![Python 3.10 or newer](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square)
[![MIT license for original files](https://img.shields.io/badge/License-MIT-186B53?style=flat-square)](LICENSE)
![Community preview](https://img.shields.io/badge/Status-Community%20preview-8A5700?style=flat-square)

</div>

---

A reusable development skill by [Merwin M. Generoso](https://generosomm.dev) for planning, building and verifying websites and web-based systems. It coordinates community skills without assuming a framework, database, visual style or industry.

**Community preview:** installer and checker validation includes temporary fixtures and disposable pinned-source installations. A static [reference site](https://github.com/generosomm/universal-web-dev/tree/main/examples/reference-site) was built through the routing, with its findings fed back into SKILL.md; a business-system trial (auth, database, roles) is still pending. See the [release checklist](docs/release-checklist.md) for evidence, limits and publication status.

## Install through your AI

Copy this prompt into a local coding assistant with file, terminal and network access (Claude Code, Codex or similar). Run it once to install everything. Run it again after a new release to bring every skill it installed up to that release's reviewed versions; skills you edited or installed some other way are kept and reported, not replaced:

```text
install or update universal-web-dev and all of its skills from:
https://github.com/generosomm/universal-web-dev
follow INSTALL.md, preserve my customized skills, and report what changed.
```

That one link installs this skill plus every skill it uses, from 11 GitHub repositories: Superpowers, Ponytail, Caveman, Anthropic's Frontend Design, Taste, UI/UX Pro Max, Emil Kowalski's skills, Impeccable, API Design, OpenAI Security and Supabase Postgres. Each comes from a reviewed, pinned commit listed in [credits](CREDITS.md). Your own edited copies are kept, never overwritten. Prefer a smaller setup? Say "core skills" instead of "all of its skills".

**For the assistant:** follow [INSTALL.md](INSTALL.md). The assistant needs local tools and permissions; a URL alone is not an installer for every AI platform.

## What it does

- Adapts to static sites, business systems, existing projects and focused fixes.
- Plans empty projects before code using concise root briefs, an MVP sprint ledger and per-sprint test records.
- Delivers one usable vertical feature with relevant permissions, database/API contracts and real-flow verification.
- Routes each task to the fewest skills it needs: a typo loads nothing extra, a landing page loads one design direction plus one final review, and backend work skips design guidance. That keeps context, and token cost, small without skipping tests or validation.
- Preserves accepted project decisions instead of redesigning on every change.

Use it for portfolios, landing pages, dashboards, booking platforms, inventory systems and other web applications. Bring your own requirements and preferred stack. The skill guides your coding assistant; it does not provide hosting, databases or paid service accounts.

Start with [SKILL.md](SKILL.md). Invoke it with `/universal-web-dev` in Claude Code or `$universal-web-dev` in Codex, or just describe the web task. For example:

```text
use universal-web-dev to plan a small inventory system with owner and staff roles.
start with the project documentation and MVP sprint plan before application code.
```

For an existing project:

```text
use universal-web-dev to continue this project's next MVP feature.
reuse the existing design and architecture, update the sprint status,
and verify the complete user flow before marking it done.
```

## Project workflow

1. Clarify users, scope, constraints and MVP acceptance criteria.
2. Plan before application code in an empty project.
3. Build one usable feature, including relevant permissions, validation and failure states.
4. Run appropriate tests and verify the actual user flow.
5. Update sprint status and evidence before continuing.

The default new-project planning structure is:

```text
README.md
PROJECT.md
PRODUCT.md
DESIGN.md
docs/
  sprint-plan.md
  testing.md
  sprints/S01.md
tests/
  sprints/S01/README.md
```

Existing projects keep their established structure. Tests are added as behavior is implemented; a folder alone is not proof. [Website readiness](references/website-readiness.md) covers relevant release checks, including accessibility, mobile layouts, secrets, forms, privacy and discoverability. Conditional references load only when needed to keep context focused.

## Install

Requires Python 3.10+ and a local skills directory (Claude Code, Codex or another compatible host). Clone/download this repository, then run commands from its root. Review downloaded skills as instructions; installation never executes their scripts. The default command only prints a plan, with no network or filesystem changes:

```sh
python scripts/install.py --host claude --profile core --sync
python scripts/install.py --host claude --profile core --sync --apply
python scripts/doctor.py
```

`--host claude` installs to ~/.claude/skills (or $CLAUDE_CONFIG_DIR/skills). `--host codex`, the default, installs to ~/.codex/skills (or $CODEX_HOME/skills). Use `--dest <skills-directory>` for any other root. Other runtimes need their documented skills directory and tool compatibility; installation is not account/cloud/mobile synchronization. New skills may require refreshing the host's catalog.

**Impeccable installs guidance-only.** Its `scripts/` launcher downloads an unpinned runtime binary, so the installer leaves that folder out. Impeccable's own documented fallback then reads PRODUCT.md and DESIGN.md directly, so critique, audit and polish work. Live browser mode, the detector and shortcuts need the launcher; set it up from the [credited upstream source](CREDITS.md) if you want them. Do not run a downloaded binary merely to clear a check.

Optional modules, selected explicitly:

```sh
python scripts/install.py --host claude --profile lean --apply
python scripts/install.py --host claude --profile backend --apply
python scripts/install.py --host claude --profile postgres --apply
python scripts/doctor.py --profile all
```

Lean adds Caveman for terse replies; Backend selects API Design and OpenAI Security; Postgres selects Supabase's SQL guidance, not a hosted database or account.

<details>
<summary><strong>How updates preserve your existing skills</strong></summary>

With `--sync --apply`, missing skills install and unchanged receipt-managed skills update when the selected release changes their pinned source. Matching versions skip downloads. Modified or unmanaged existing skills are preserved and reported.

Caveman moved from `core` to the optional `lean` profile, Impeccable now installs automatically (guidance-only), and Superpowers' `diagnosing-superpowers` is no longer selected. Sync never removes skills, so existing copies stay in place.

`--update --apply` explicitly replaces existing copies, with backups and rollback on installation failure. Review local customizations and the printed plan first. Updates use reviewed pins from the selected wrapper release; they never silently follow upstream HEAD.

If a running host locks the folder on Windows, release the lock/check normal permissions and retry. See [installation recovery](INSTALL.md#locked-installation-directories).

</details>

## Dependencies and attribution

| Core capability | Main role |
| --- | --- |
| Superpowers | Planning, implementation workflow and verification |
| Ponytail | The smallest complete implementation with controlled scope |
| Caveman (optional `lean` profile) | Terse replies when the user asks for them |
| Frontend Design | Intentional visual direction and interface composition |
| Taste | Distinctive typography, layout and visual choices |
| UI/UX Pro Max | UI/UX guidance and design-system decisions |
| Emil Design Engineering | Component polish, interaction details and purposeful motion |
| Break UI, Mobile Native (Emil) | Release checks: worst-case content and real-phone feel |
| Prototype, Pick UI Library (Emil) | Run only when the developer invokes them: try several looks side by side; choose proven libraries for complex widgets |
| Impeccable | Final interface critique, accessibility and refinement (guidance-only install) |

Capabilities are routed by task, so only one design direction skill runs per project and Impeccable reviews once at the end. Superpowers includes its workflow subskills, so the installed folder count is larger than the table. Each module retains its own scope and license. The pinned upstream versions may differ from locally customized copies.

See [all credits and verified source/license links](CREDITS.md), [pinned dependencies](dependencies.lock.json), and [sharing guidance](references/sharing.md). No third-party skill source or runtime binary is bundled here. Opt-in installation downloads selected pinned source archives and retains license notices. This independent project does not imply upstream sponsorship or endorsement.

## Checks and updates

```sh
python -m unittest discover -s tests -v
python scripts/doctor.py --package-only
```

The doctor checks package integrity and dependency presence, not website security, external-service wiring, full runtime compatibility or exact integrity of existing custom skills. Manual requirements remain visible. Keep skills selective and projects small; better planning and focused tests do not guarantee zero bugs or lower token usage.

Contributors should follow [AGENTS.md](https://github.com/generosomm/universal-web-dev/blob/main/AGENTS.md), keep changes focused and include relevant regression evidence. Maintainers check for upstream updates with `python scripts/check-updates.py`, which reports whether new commits touch installed files. Updates should change verified source pins and credits together, test in a disposable skills directory, and review upstream changes before applying them. The project's [MIT license](LICENSE) covers original wrapper files only; upstream licenses remain separate.

---

Created by **Merwin M. Generoso**. Explore my work at **[generosomm.dev](https://generosomm.dev)** or connect on [GitHub](https://github.com/generosomm).

Trying this on a project? [Share a reproducible issue or suggestion](https://github.com/generosomm/universal-web-dev/issues), including your AI host, setup and expected behavior. Remove secrets and private project data first.
