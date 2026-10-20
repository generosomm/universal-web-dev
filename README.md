# Universal Web Dev

A reusable development skill by [Merwin M. Generoso](https://github.com/generosomm) for planning, building and verifying websites and web-based systems. It coordinates community skills without assuming a framework, database, visual style or industry.

**Local prerelease draft. Public publishing is on hold.** The installer and checker are tested with temporary fixtures; no completed reference website or bug-free/token-savings claim is implied. Current validation scope is in the [release checklist](docs/release-checklist.md).

## Install through your AI

After publication, paste the repository link into a local coding assistant and say:

```text
install or update universal-web-dev and its core skills from this repository.
```

**For the assistant:** follow [INSTALL.md](INSTALL.md). Resolve the host's skills directory, use managed sync, run the checker and report any missing/manual requirements. The assistant needs local tools and permissions; a URL alone is not an installer for every AI platform.

## What it does

- Adapts to static sites, business systems, existing projects and focused fixes.
- Plans empty projects before code using concise root briefs, an MVP sprint ledger and per-sprint test records.
- Delivers one usable vertical feature with relevant permissions, database/API contracts and real-flow verification.
- Loads relevant guidance on demand and preserves accepted project decisions.

Start with [SKILL.md](SKILL.md). For example:

```text
use $universal-web-dev to plan a small inventory system with owner and staff roles.
start with the project documentation and MVP sprint plan before application code.
```

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

Backend selects API Design and OpenAI Security; Postgres selects Supabase's SQL guidance, not a hosted database or account. With `--sync --apply`, missing skills are installed and unchanged receipt-managed skills update when the selected release changes their pinned source. Matching versions are skipped without downloads. Modified or unmanaged existing skills are preserved and reported. `--update --apply` is the explicit replacement override, with backups and rollback on commit failure. Updates use reviewed pins from the selected wrapper release; they never silently follow upstream HEAD. Review local customizations and the printed plan first.

## Dependencies and attribution

Eight core capabilities: Superpowers, Ponytail, Caveman, Frontend Design, Taste, UI/UX Pro Max, Emil Design Engineering and Impeccable. Superpowers includes its workflow subskills; installed folder count is therefore larger than eight. Each module retains its own scope and license. The pinned upstream versions may differ from locally customized copies.

See [all credits and verified source/license links](CREDITS.md), [pinned dependencies](dependencies.lock.json), and [sharing guidance](references/sharing.md). No third-party skill source or runtime binary is bundled here. Opt-in installation downloads selected pinned source archives and retains license notices. This independent project does not imply upstream sponsorship or endorsement.

## Checks and updates

```sh
python -m unittest discover -s tests -v
python scripts/doctor.py --package-only
```

The doctor checks package integrity and dependency presence, not website security, external-service wiring, full runtime compatibility or exact integrity of existing custom skills. Manual requirements remain visible. Keep skills selective and projects small; better planning and focused tests do not guarantee zero bugs or lower token usage.

Maintainer updates should change verified source pins and credits together, test in a disposable skills directory, and review upstream changes before applying them. The project's [MIT license](LICENSE) covers original wrapper files only; upstream licenses remain separate.
