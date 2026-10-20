# Prerelease review

Status: local draft, public upload on hold.

## Acceptance

- [x] Flexible across stacks/project types; no forced game, palette, database or response language.
- [x] Empty-project docs-first bootstrap, sprint status and test manifests.
- [x] Eight core sources and conditional modules credited with pinned revisions and license links.
- [x] Original wrapper licensed MIT; upstream material not vendored or relicensed.
- [x] Installer plan default; explicit writes, backups and rollback coverage.
- [x] Package/dependency doctor with clear missing/manual status.
- [x] Independent code review completed and findings resolved.
- [x] Real-source disposable install and update smoke checks completed.
- [ ] Maintainer reviews the local result and authorizes public upload.

## Evidence and limits

Previous bootstrap forward-check created eight planning Markdown files for a branch-booking proposal, with three MVP slices and planned test coverage. This proved documentation generation, not a working booking website.

Installer/checker tests use temporary directories and in-memory archives. Record final command results below after review. CI is configured for Linux/Windows and Python 3.10/3.12 but has not run remotely because this repository has not been published.

Impeccable remains manual due its binary-dependent launcher. Other upstream runtime tools, a physical device and a full new reference website have not been verified by package tests. A real website should be evaluated before claiming broad production reliability.

## Local final checks, 2026-10-20

- Python 3.14 on Windows: `python -m unittest discover -s tests -v`, 34 tests run, 33 passed and one POSIX filesystem-permission test skipped. A platform-independent permission-mask regression passed; actual POSIX behavior awaits configured CI.
- `python scripts/doctor.py --package-only`: passed. Skills with quoted names, unsafe archive entries, unrelated symlinks, rollback, complete manifests and Superpowers canonical sibling paths have regression coverage.
- Installed all automatic pinned-source profiles into a disposable directory: 25 skill folders including the wrapper, 24 upstream license notices. Repeated with --update; backups retained. No upstream scripts or Impeccable binaries executed.
- The installed wrapper's package check passed. Its backend/Postgres dependency check passed. The core check deliberately reports Impeccable manual runtime setup as unverified.
- No public repository or remote CI run exists yet. A new real reference website remains future validation.
