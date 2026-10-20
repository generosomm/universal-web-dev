# Universal Web Dev

Plan first. Build one usable feature at a time. Verify the actual user flow.

A reusable development skill by [Merwin M. Generoso](https://github.com/generosomm) for planning, building and verifying websites and web-based systems. It coordinates community skills without assuming a framework, database, visual style or industry.

**Community preview:** installer and checker validation includes temporary fixtures and disposable pinned-source installations. A complete reference website is still pending. See the [release checklist](docs/release-checklist.md) for evidence, limits and publication status.

## Install through your AI

After publication, paste the repository link into a local coding assistant and say:

```text
install or update universal-web-dev and its core skills from this repository.
follow INSTALL.md, preserve my customized skills, and report any manual setup.
```

**For the assistant:** follow [INSTALL.md](INSTALL.md). Resolve the host's skills directory, use managed sync, run the checker and report any missing/manual requirements. The assistant needs local tools and permissions; a URL alone is not an installer for every AI platform.

## What it does

- Adapts to static sites, business systems, existing projects and focused fixes.
- Plans empty projects before code using concise root briefs, an MVP sprint ledger and per-sprint test records.
- Delivers one usable vertical feature with relevant permissions, database/API contracts and real-flow verification.
- Loads relevant guidance on demand and preserves accepted project decisions.

Use it for portfolios, landing pages, dashboards, booking platforms, inventory systems and other web applications. Bring your own requirements and preferred stack. The skill guides your coding assistant; it does not provide hosting, databases or paid service accounts.

Start with [SKILL.md](SKILL.md). For example:

```text
use $universal-web-dev to plan a small inventory system with owner and staff roles.
start with the project documentation and MVP sprint plan before application code.
```

For an existing project:

```text
use $universal-web-dev to continue this project's next MVP feature.
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

Requires Python 3.10+ and a local Codex-compatible skills directory. Clone/download this repository, then run commands from its root. Review downloaded skills as instructions; installation never executes their scripts. The default command only prints a plan, with no network or filesystem changes:

```sh
python scripts/install.py --profile core --sync
python scripts/install.py --profile core --sync --apply
python scripts/doctor.py
```

Default destination is $CODEX_HOME/skills, or ~/.codex/skills. Use `--dest <skills-directory>` to choose another root. Other runtimes need their documented skills directory and tool compatibility; installation is not account/cloud/mobile synchronization. New skills may require refreshing the host's catalog.

**Impeccable requires manual setup.** Its pinned distribution uses a separately downloaded runtime binary. The installer prints the limitation and skips it; the checker keeps it unverified. Follow its [credited upstream instructions](CREDITS.md) before claiming all eight capabilities are available. Do not run a downloaded binary merely to clear a check.

Optional modules, selected explicitly:

```sh
python scripts/install.py --profile backend --apply
python scripts/install.py --profile postgres --apply
python scripts/doctor.py --profile all
```

Backend selects API Design and OpenAI Security; Postgres selects Supabase's SQL guidance, not a hosted database or account. With `--sync --apply`, missing skills are installed and unchanged receipt-managed skills update when the selected release changes their pinned source. Matching versions are skipped without downloads. Modified or unmanaged existing skills are preserved and reported. `--update --apply` is the explicit replacement override, with backups and rollback on commit failure. Updates use reviewed pins from the selected wrapper release; they never silently follow upstream HEAD. Review local customizations and the printed plan first. If a running host locks the folder on Windows, release the lock/check normal permissions and retry; the installer stops without forcing deletion. See [installation recovery](INSTALL.md#locked-installation-directories).

## Dependencies and attribution

| Core capability | Main role |
| --- | --- |
| Superpowers | Planning, implementation workflow and verification |
| Ponytail | The smallest complete implementation with controlled scope |
| Caveman | Concise updates in the user's preferred language |
| Frontend Design | Intentional visual direction and interface composition |
| Taste | Distinctive typography, layout and visual choices |
| UI/UX Pro Max | UI/UX guidance and design-system decisions |
| Emil Design Engineering | Component polish, interaction details and purposeful motion |
| Impeccable | Interface critique, accessibility and refinement; manual setup |

The eight capabilities are routed by relevance across the project, without loading every manual for every edit. Superpowers includes its workflow subskills; installed folder count is therefore larger than eight. Each module retains its own scope and license. The pinned upstream versions may differ from locally customized copies.

See [all credits and verified source/license links](CREDITS.md), [pinned dependencies](dependencies.lock.json), and [sharing guidance](references/sharing.md). No third-party skill source or runtime binary is bundled here. Opt-in installation downloads selected pinned source archives and retains license notices. This independent project does not imply upstream sponsorship or endorsement.

## Checks and updates

```sh
python -m unittest discover -s tests -v
python scripts/doctor.py --package-only
```

The doctor checks package integrity and dependency presence, not website security, external-service wiring, full runtime compatibility or exact integrity of existing custom skills. Manual requirements remain visible. Keep skills selective and projects small; better planning and focused tests do not guarantee zero bugs or lower token usage.

Contributors should follow [AGENTS.md](AGENTS.md), keep changes focused and include relevant regression evidence. Maintainer updates should change verified source pins and credits together, test in a disposable skills directory, and review upstream changes before applying them. The project's [MIT license](LICENSE) covers original wrapper files only; upstream licenses remain separate.
