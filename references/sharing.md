# Sharing and dependencies

Resolve skills by catalog name. This package contains the original wrapper, references, installer, checker and tests; upstream skill sources and binaries are not bundled. Install the full package rather than copying SKILL.md alone. For an AI given the repository link, start with [INSTALL.md](../INSTALL.md). See [README](../README.md), [credits](../CREDITS.md) and [dependency lock](../dependencies.lock.json).

## Installation and compatibility

Use Python 3.10+. `python scripts/install.py --profile core` prints a plan without network/writes; add `--apply` to download pinned sources and install. `--host claude` targets ~/.claude/skills; `--host codex` (default) targets ~/.codex/skills; `--dest` selects another directory. `--profile lean`, `--profile backend` and `--profile postgres` are optional. Use `--sync --apply` for missing skills and unchanged receipt-managed updates to the selected release's pins. Preserve modified/unmanaged copies and report them; `--update --apply` is an explicit replacement override with backups and rollback. Review customizations first. No upstream scripts are executed.

Core capabilities are Superpowers, ponytail, frontend-design, design-taste-frontend, ui-ux-pro-max, emil-design-eng and impeccable; SKILL.md routes each task to the few it needs. The optional lean profile adds caveman. Superpowers' workflow siblings are co-installed because its references depend on them. Installation is not language, provider or framework selection. UI/UX script examples must resolve their actual installed skill directory, not a hardcoded host plugin path.

Impeccable installs guidance-only: its critique, audit and polish playbooks work, while live browser mode, the detector and shortcuts need the upstream launcher (its `scripts/` folder is not installed because the launcher downloads an unpinned binary). Don't claim every core skill ran when one is missing or its runtime is unverified. A host may use documented reference fallbacks, but disclose the limited coverage.

Run `python scripts/doctor.py`, using `--skills-dir` for another skill root and `--profile all` to inspect optional modules. It checks package links and dependency names without credentials, database connections or service calls. Presence is not operational verification. `--package-only` checks only this package. Missing/manual modules remain reported. Refresh the host catalog as needed.

## Distribution

The original wrapper is MIT licensed. Preserve that license, all upstream notices and credited publishers. Do not relicense dependencies as MIT, bundle third-party fonts/images/binaries, or imply endorsement. Credits include pinned source/license links; any future vendoring requires separate review of the selected material's terms.

Share no private paths, credentials, personal memory or project source. Verify changes in an isolated skills directory and a real project before making broader compatibility claims. Keep the main guide small, use references only when relevant, and maintain one source for each project decision. Public publishing requires the maintainer's approval; a local Git repository is not a published release.
