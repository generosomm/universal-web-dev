# Sharing and dependencies

Resolve skills by catalog name. This package contains the original wrapper, references, installer, checker and tests; upstream skill sources and binaries are not bundled. Install the full package rather than copying SKILL.md alone. See [README](../README.md), [credits](../CREDITS.md) and [dependency lock](../dependencies.lock.json).

## Installation and compatibility

Use Python 3.10+. `python scripts/install.py --profile core` prints a plan without network/writes; add `--apply` to download pinned sources and install. The default is $CODEX_HOME/skills or ~/.codex/skills; `--dest` selects another directory. `--profile backend` and `--profile postgres` are optional. Existing compatible skills are skipped; `--update --apply` stages and verifies replacements, retains backups and attempts rollback on installation failure. Review customizations first. No upstream scripts are executed.

Eight core capabilities are using-superpowers, ponytail, caveman, frontend-design, design-taste-frontend, ui-ux-pro-max, emil-design-eng and impeccable. Superpowers' workflow siblings are co-installed because its references depend on them. Installation is not language, provider or framework selection. UI/UX script examples must resolve their actual installed skill directory, not a hardcoded host plugin path.

Impeccable is manual-only in this lock: its launcher downloads a runtime binary outside the pinned source tree. Review and configure the credited upstream distribution separately. Don't claim all eight ran when one is missing or its runtime is unverified. A host may use documented reference fallbacks, but disclose the limited coverage.

Run `python scripts/doctor.py`, using `--skills-dir` for another skill root and `--profile all` to inspect optional modules. It checks package links and dependency names without credentials, database connections or service calls. Presence is not operational verification. `--package-only` checks only this package. Missing/manual modules remain reported. Refresh the host catalog as needed.

## Distribution

The original wrapper is MIT licensed. Preserve that license, all upstream notices and credited publishers. Do not relicense dependencies as MIT, bundle third-party fonts/images/binaries, or imply endorsement. Credits include pinned source/license links; any future vendoring requires separate review of the selected material's terms.

Share no private paths, credentials, personal memory or project source. Verify changes in an isolated skills directory and a real project before making broader compatibility claims. Keep the main guide small, use references only when relevant, and maintain one source for each project decision. Public publishing requires the maintainer's approval; a local Git repository is not a published release.
