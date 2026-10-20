#!/usr/bin/env python3
"""Maintainer tool: compare each pinned dependency with its upstream default branch.

Read-only by default. Reports whether new upstream commits touch the files the installer
actually copies (skill folders, support paths, license files). `--write owner/repo` moves
reviewed pins to the reported upstream commit in the lock and CREDITS.md. Python stdlib only.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location('_universal_installer', Path(__file__).with_name('install.py'))
_installer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_installer)


def fetch(path):
    request = urllib.request.Request('https://api.github.com/' + path, headers={'Accept': 'application/vnd.github+json'})
    if os.environ.get('GITHUB_TOKEN'):
        request.add_header('Authorization', 'Bearer ' + os.environ['GITHUB_TOKEN'])
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def installed_paths(packages):
    """Repo-relative prefixes the installer copies, and the ones it deliberately skips."""
    keep, skip = set(), set()
    for package in packages:
        keep.update(package['license_files'])
        for skill in package['skills']:
            keep.add(skill['path'])
            keep.update(item['source'] for item in skill.get('support', []))
            skip.update(str(PurePosixPath(skill['path'], e)) for e in skill.get('exclude', []))
    return keep, skip


def touches(filename, keep, skip):
    path = PurePosixPath(filename)
    inside = lambda prefixes: any(p == '.' or path == PurePosixPath(p) or path.is_relative_to(p) for p in prefixes)
    return inside(keep) and not inside(skip)


def check(manifest, get=fetch):
    groups = {}
    for package in manifest['packages']:
        groups.setdefault((package['repo'], package['ref']), []).append(package)
    report = []
    for (repo, ref), packages in groups.items():
        head = get('repos/{}/commits/HEAD'.format(repo))['sha']
        entry = {'repo': repo, 'pinned': ref, 'upstream': head, 'installed_changes': [], 'complete': True}
        if head != ref:
            compare = get('repos/{}/compare/{}...{}'.format(repo, ref, head))
            files = compare.get('files')
            # The compare API caps its file list; an uncertain answer must not read as "nothing changed".
            entry['complete'] = files is not None and len(files) < 300
            keep, skip = installed_paths(packages)
            entry['installed_changes'] = [f['filename'] for f in files or [] if touches(f['filename'], keep, skip)]
            entry['commits'] = compare.get('ahead_by')
        report.append(entry)
    return report


def write(repos, report, root=ROOT):
    chosen = {entry['repo']: entry for entry in report if entry['repo'] in repos and entry['upstream'] != entry['pinned']}
    for name in ['dependencies.lock.json', 'CREDITS.md']:
        path = root / name
        text = path.read_text(encoding='utf-8')
        for entry in chosen.values():
            text = text.replace(entry['pinned'], entry['upstream'])
        path.write_text(text, encoding='utf-8')
    return sorted(chosen)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--write', action='append', default=[], metavar='OWNER/REPO',
                        help='Move this reviewed repo to its upstream commit (repeatable)')
    args = parser.parse_args(argv)
    report = check(_installer.load_manifest(ROOT / 'dependencies.lock.json'))
    for entry in report:
        if entry['upstream'] == entry['pinned']:
            state = 'up to date'
        elif not entry['complete']:
            state = 'new commits; file list truncated, review the full diff manually'
        elif entry['installed_changes']:
            state = 'new commits change installed files: review before --write'
        else:
            state = 'new commits, installed files unchanged: safe to --write'
        print('{}: {} ({} -> {})'.format(entry['repo'], state, entry['pinned'][:10], entry['upstream'][:10]))
        for name in entry['installed_changes'][:20]:
            print('    ' + name)
    if args.write:
        print('Updated pins: ' + (', '.join(write(set(args.write), report)) or 'none'))
        print('Then run the tests, a disposable --apply install and doctor.py before committing.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
