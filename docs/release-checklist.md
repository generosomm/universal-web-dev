# Prerelease review

Status: initial public community preview authorized by the maintainer on 2026-10-20. Validation limits below still apply.

## Acceptance

- [x] Flexible across stacks/project types; no forced game, palette, database or response language.
- [x] Empty-project docs-first bootstrap, sprint status and test manifests.
- [x] Core sources and optional modules credited with pinned revisions and license links.
- [x] Original wrapper licensed MIT; upstream material not vendored or relicensed.
- [x] Installer plan default; explicit writes, backups and rollback coverage.
- [x] Package/dependency doctor with clear missing/manual status.
- [x] Independent code review completed and findings resolved.
- [x] Real-source disposable install and update smoke checks completed.
- [x] Maintainer reviews the local result and authorizes public upload (2026-10-20).

## Evidence and limits

Previous bootstrap forward-check created eight planning Markdown files for a branch-booking proposal, with three MVP slices and planned test coverage. This proved documentation generation, not a working booking website.

Installer/checker tests use temporary directories and in-memory archives. Local command results are recorded below. CI is configured for Linux/Windows and Python 3.10/3.12; see the repository's Actions tab for current remote results.

Impeccable installs guidance-only; its binary-dependent launcher is excluded. Other upstream runtime tools, a physical device and a full new reference website have not been verified by package tests. A real website should be evaluated before claiming broad production reliability.

## Local final checks, 2026-10-20

- Python 3.14 on Windows: `python -m unittest discover -s tests -v`, 34 tests run, 33 passed and one POSIX filesystem-permission test skipped. A platform-independent permission-mask regression passed; actual POSIX behavior awaits configured CI.
- `python scripts/doctor.py --package-only`: passed. Skills with quoted names, unsafe archive entries, unrelated symlinks, rollback, complete manifests and Superpowers canonical sibling paths have regression coverage.
- Installed all automatic pinned-source profiles into a disposable directory: 25 skill folders including the wrapper, 24 upstream license notices. Repeated with --update; backups retained. No upstream scripts or Impeccable binaries executed.
- The installed wrapper's package check passed. Its backend/Postgres dependency check passed. The core check deliberately reports Impeccable manual runtime setup as unverified.
- At the time of these prerelease checks, no public repository or remote CI run existed. A new real reference website remains future validation.

## Repository-link installation follow-up

An explicit user install/update request routes the assistant to INSTALL.md. A local tool-enabled assistant resolves its actual skills directory, runs core --sync planning/apply and the dependency checker, and reports exceptions. A bare link or assistant without local tools is not promised automatic installation.

Managed receipts bind the installed source identity and content digest. Sync should perform no network for unchanged sources, update changed reviewed pins only for intact managed folders, preserve unmanaged/modified folders, and retain existing backup/rollback behavior. Older installs without receipts require an explicit replacement choice before managed updates apply. Upstream HEAD is never selected during ordinary installation.

Follow-up evidence: 43 local tests run, 42 passed and one POSIX-only check skipped on Windows. A cached pinned-source smoke installed 25 skill folders with managed receipts; repeat sync made no downloads, and a subsequent local customization was preserved and reported. The installed wrapper package check passed. Independent review found malformed wrapper receipt edge cases; both were reproduced with failing regressions, fixed, and re-reviewed with no remaining actionable findings. No AI platform without local tools or public-link installation has been claimed tested.

Windows live-host limit: updating the maintainer's currently loaded global wrapper returned Access denied on directory rename; its existing folder was preserved. Automatic update while a host holds that folder is not claimed supported. Recovery is documented in INSTALL.md; the maintainer's own installed copy was separately backed up and reconciled file-by-file. Disposable-directory install/update tests passed.

## Routing refinement and reference-site trial, 2026-10-20

- SKILL.md routes each task to the fewest skills and names what not to load. Caveman moved to the optional `lean` profile; `--host claude` installs to ~/.claude/skills.
- Impeccable now installs guidance-only: `scripts/` is excluded at extraction and recorded in `UPSTREAM-NOTICE.txt`. A real pinned-source core install into a disposable folder produced 21 skill folders; the doctor passed with every core skill present; a repeat `--sync` reported every skill `skip (unchanged)`. `diagnosing-superpowers` is no longer selected (no sibling references it).
- A static reference site (`examples/reference-site`) was built by following the routing: bootstrap docs, Taste direction, Impeccable polish in fallback mode. Its record lists the bugs the checks caught, what ran, what could not run (Taste's inspector, physical devices, screen reader, performance scores) and the routing changes it caused.
- Not yet exercised by a trial: the bug, existing-feature, app-screen and backend rows. A business-system trial is the next validation.
- Added four skills from the already pinned emilkowalski/skills commit: `break-ui` and `mobile-native` run only at UI release; `prototype` and `pick-ui-library` are explicit-only upstream (`disable-model-invocation`), so on hosts that honor that flag they cost no context until the developer invokes them; SKILL.md only suggests them. SKILL.md stays at 5,665 bytes (original 5,666).
