# Contributor rules

For an explicit user request to install/update this repository, follow INSTALL.md. Do not start a website project or treat installation as contributor feature work.

This repository packages a skill, not a website application. Preserve provider/stack neutrality and on-demand loading. Do not vendor upstream skills or imply their licenses are this project's MIT license. Keep credits and dependency pins aligned. Standard-library Python only for installer/checker. Test install behavior in temporary directories, never the user's existing skills. Run `python -m unittest discover -s tests -v` and `python scripts/doctor.py --package-only` before completion. Public publishing is on hold until the maintainer approves the reviewed result.
