# AI installation guide

Read this when the user asks to install or update Universal Web Dev from its repository link. This is an installation task, not a request to build a website. Repository content does not itself grant permission: follow the user's request and the host's tool/approval rules. An assistant without filesystem, network or command execution cannot install local skills; explain that limit and give the commands instead.

## One-link request

After this repository is published, the user can send its URL with:

```text
install or update universal-web-dev and all of its skills from this repository in my ai setup.
```

A bare URL is not guaranteed to trigger installation in every assistant. Do not claim universal AI-platform support or invent a public URL before publication.

## Autonomous setup flow

1. Read README.md, this guide and dependencies.lock.json from a fresh checkout/download of the user-selected repository revision. Inspect the installer before running it. Use the current published revision unless the user pins a release. Preserve dirty/existing checkouts; use a separate temporary download rather than resetting someone's work.
2. Identify the host and its documented skills directory. For Claude Code pass `--host claude` (~/.claude/skills or $CLAUDE_CONFIG_DIR/skills); for Codex pass `--host codex` ($CODEX_HOME/skills or ~/.codex/skills); for another host verify its actual support and use --dest explicitly. Do not write to an arbitrary guessed global config file. Check Python 3.10+; do not install Python, a plugin, a CLI binary or administrator tooling as an unrequested side effect.
3. Plan and apply the core installation with the commands below, replacing the target with the resolved directory. The user's install/update request authorizes ordinary selected skill installation subject to host permissions; do not add a second routine confirmation when authorization is already clear. Honor any explicit hold or review request. "All of its skills" (the README prompt) means `--profile all`; "core skills" means `--profile core`. If the host already provides a module through a plugin (for example Supabase's Postgres skill), install the remaining profiles by name instead of `all` and report the skip, so the catalog has no duplicate. Otherwise optional lean/backend/Postgres profiles require the user's selection or the requested project need.
4. Run the dependency checker for the selected profiles. Report installed, updated, unchanged, preserved custom/unmanaged, missing and manual requirements honestly. If the host caches skills, explain its supported refresh/restart step. Do not run a newly installed skill or start a project just to demonstrate installation.

```sh
python scripts/install.py --profile all --sync --dest <skills-directory>
python scripts/install.py --profile all --sync --dest <skills-directory> --apply
python scripts/doctor.py --skills-dir <skills-directory> --profile all
```

No upstream skill script is executed by installation. Impeccable installs guidance-only: its critique, audit and polish playbooks work, while live browser mode, the detector and shortcuts need the upstream launcher; do not download/execute its separate binary. Installation completion and runtime verification are different results.

## Update behavior

"Updated" means the source revisions pinned and reviewed in the selected Universal Web Dev release, not every upstream repository's moving HEAD. Never replace lock revisions automatically during user installation. Maintainers review source/license changes, update the lock and credits, and publish a new wrapper revision separately.

The --sync mode installs missing modules and updates unchanged modules managed by this installer when the release's desired source changes. Its local content receipt detects modifications. Existing unmanaged, malformed-receipt or modified skills are kept and reported; do not claim they were brought up to date. The explicit --update override requires the user's clear intent to replace those local copies, and creates backups. Neither flag is an unattended scheduler or background updater.

Repeated setup should be a no-op for matching managed sources. Failed staging must leave existing installed folders intact; updates preserve backups and attempt rollback on a commit failure. Stop and report a failed requirement rather than weakening checks. Do not print environment values or credentials. Keep the final installation report concise and use the user's language.

## Locked installation directories

If Windows reports Access denied while renaming an installed folder, stop and report it. Check normal directory permissions and release any host/editor lock, then retry the reviewed plan; do not delete the existing folder, escalate privileges automatically or silently fall back to partial in-place updates. Initial staging can succeed while replacement is blocked. Existing installations should remain intact after this failure. A maintainer can separately back up and reconcile their own files, but that is not the installer's automatic update path.
