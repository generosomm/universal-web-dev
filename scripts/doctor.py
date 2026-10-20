#!/usr/bin/env python3
"""Read-only package/dependency check. Never opens services or prints environment values."""
import argparse
import importlib.util
import json
import os
import re
from pathlib import Path


_spec = importlib.util.spec_from_file_location('_universal_installer', Path(__file__).with_name('install.py'))
_installer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_installer)


def declared_name(path):
    try:
        return _installer.skill_name(path)
    except (OSError, ValueError, UnicodeError):
        return None


def default_roots():
    home = Path.home()
    return [Path(os.environ.get('CODEX_HOME', home / '.codex')) / 'skills', home / '.agents' / 'skills']


def check(package, roots, profiles, package_only=False):
    package = Path(package).resolve()
    errors, dependencies = [], {}
    if declared_name(package / 'SKILL.md') != 'universal-web-dev':
        errors.append('Package has no valid universal-web-dev entrypoint')
    try:
        manifest = _installer.load_manifest(package / 'dependencies.lock.json')
    except (OSError, ValueError, TypeError, AttributeError, KeyError) as exc:
        errors.append('Manifest invalid: ' + str(exc))
        manifest = {'packages': []}
    # These are wrapper-owned Markdown files; upstream dependencies are checked separately.
    files = [package / 'SKILL.md'] + list((package / 'references').glob('*.md'))
    files += [p for p in [package / 'README.md', package / 'CREDITS.md', package / 'INSTALL.md'] if p.exists()]
    for file in files:
        if not file.exists():
            continue
        try:
            text = file.read_text(encoding='utf-8')
        except (OSError, UnicodeError):
            errors.append('Unreadable package document: ' + file.name)
            continue
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if link.startswith(('https:', 'http:', 'mailto:', '#')):
                continue
            target = link.split('#', 1)[0].strip('<>')
            resolved = (file.parent / target).resolve()
            if not resolved.is_relative_to(package) or not resolved.is_file():
                errors.append('Invalid local link in ' + file.name + ': ' + target)
    if not package_only:
        found = set()
        canonical_roots = []
        for root in roots:
            root = Path(root)
            if not root.is_dir():
                continue
            canonical = {}
            for folder in root.iterdir():
                if folder.is_dir():
                    name = declared_name(folder / 'SKILL.md')
                    if name:
                        found.add(name)
                        canonical[folder.name] = name
            canonical_roots.append(canonical)
        dependencies['universal-web-dev'] = 'present' if 'universal-web-dev' in found else 'missing'
        if 'universal-web-dev' not in found:
            errors.append('Wrapper not installed in selected skill roots')
        for entry in manifest['packages']:
            if 'all' not in profiles and not set(entry.get('profiles', [])).intersection(profiles):
                continue
            if entry.get('canonical_folders') and not any(all(locations.get(skill['name']) == skill['name'] for skill in entry['skills']) for locations in canonical_roots):
                errors.append(entry['id'] + ': canonical sibling folders must exist together in one skills root')
            if entry.get('manual_reason'):
                dependencies[entry['id']] = 'manual verification required'
                errors.append(entry['id'] + ': ' + entry['manual_reason'])
            for skill in entry.get('skills', []):
                name = skill['name']
                dependencies[name] = 'present' if name in found else 'missing'
                if name not in found:
                    errors.append('Missing skill: ' + name)
    return {'errors': errors, 'dependencies': dependencies,
            'scope': 'package only' if package_only else 'package and dependency presence',
            'limits': 'Presence is not runtime, upstream-integrity, website-security or integration verification.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-only', action='store_true')
    parser.add_argument('--skills-dir', type=Path, action='append', help='Additional installed skills root (repeatable)')
    parser.add_argument('--profile', action='append', choices=['core', 'backend', 'postgres', 'all'])
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    result = check(Path(__file__).resolve().parents[1], args.skills_dir or default_roots(), args.profile or ['core'], args.package_only)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print('PASS' if not result['errors'] else 'NEEDS ATTENTION')
        for name, state in result['dependencies'].items():
            print(name + ': ' + state)
        for error in result['errors']:
            print('- ' + error)
        print(result['limits'])
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
