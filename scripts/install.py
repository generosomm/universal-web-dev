#!/usr/bin/env python3
"""Plan by default; install pinned skills only with --apply. Python stdlib only."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
import urllib.request
import uuid
import zipfile

SOURCE_ROOT = Path(__file__).resolve().parents[1]
PROFILES = {'core', 'backend', 'postgres'}
MAX_DOWNLOAD = 64 * 1024 * 1024
MAX_EXPANDED = 256 * 1024 * 1024
MAX_FILES = 20000
RECEIPT = '.universal-web-dev-install.json'
WRAPPER_FILES = ('SKILL.md', 'agents', 'references', 'LICENSE', 'CREDITS.md', 'README.md',
                 'INSTALL.md', 'dependencies.lock.json', 'scripts', 'docs', 'tests')


def content_digest(root, selected=None):
    """Hash paths and bytes without following links or including generated caches."""
    digest = hashlib.sha256()

    def visit(path):
        if path.name in {RECEIPT, '__pycache__'} or path.suffix == '.pyc':
            return
        if path.is_symlink():
            raise ValueError('Refusing content symlink: ' + str(path))
        relative = path.relative_to(root).as_posix().encode('utf-8')
        if path.is_dir():
            digest.update(b'd' + len(relative).to_bytes(8, 'big') + relative)
            for child in sorted(path.iterdir(), key=lambda p: p.name):
                visit(child)
        elif path.is_file():
            content = path.read_bytes()
            digest.update(b'f' + len(relative).to_bytes(8, 'big') + relative)
            digest.update(len(content).to_bytes(8, 'big') + content)
        else:
            raise ValueError('Unsafe content: ' + str(path))

    paths = [root / name for name in selected] if selected is not None else list(root.iterdir())
    for path in sorted(paths, key=lambda p: p.name):
        if path.exists() or path.is_symlink():
            visit(path)
    return digest.hexdigest()


def desired_identity(name, package, skill):
    if package is None:
        return {'kind': 'wrapper', 'name': name, 'content': content_digest(SOURCE_ROOT, WRAPPER_FILES)}
    return {'kind': 'dependency', 'name': name, 'repo': package['repo'], 'ref': package['ref'],
            'package': package['id'], 'path': skill['path'], 'support': skill.get('support', []),
            'license': package['license'], 'license_files': package['license_files']}


def managed_status(target, desired):
    """A receipt authorizes only this module's unchanged installed content."""
    try:
        path = target / RECEIPT
        if path.is_symlink():
            return 'unmanaged'
        receipt = json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(receipt, dict) or type(receipt.get('version')) is not int or receipt['version'] != 1:
            return 'unmanaged'
        identity = receipt.get('identity')
        if not isinstance(identity, dict) or set(identity) != set(desired):
            return 'unmanaged'
        stable = ('kind', 'name', 'repo', 'package', 'path') if desired['kind'] == 'dependency' else ('kind', 'name')
        if any(identity.get(key) != desired.get(key) for key in stable):
            return 'unmanaged'
        hex_digest = lambda value: isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value)
        if desired['kind'] == 'dependency':
            if not isinstance(identity['ref'], str) or not re.fullmatch(r'[0-9a-fA-F]{40}', identity['ref']):
                return 'unmanaged'
            if not isinstance(identity['license'], str) or not identity['license'].strip():
                return 'unmanaged'
            licenses, support = identity['license_files'], identity['support']
            if not isinstance(licenses, list) or not licenses or not isinstance(support, list):
                return 'unmanaged'
            for item in licenses:
                safe_path(item)
            for item in support:
                if not isinstance(item, dict) or set(item) != {'source', 'target'}:
                    return 'unmanaged'
                safe_path(item['source'], root_ok=True)
                safe_path(item['target'])
            # Attribution must agree with the receipt's claimed installed pin.
            notice_path = target / 'UPSTREAM-NOTICE.txt'
            if notice_path.is_symlink():
                return 'unmanaged'
            notice = notice_path.read_text(encoding='utf-8')
            if not notice.startswith('{}\nCommit: {}\n'.format(identity['repo'], identity['ref'])):
                return 'unmanaged'
        elif not hex_digest(identity['content']) or identity['content'] != receipt.get('digest'):
            return 'unmanaged'
        if not hex_digest(receipt.get('digest')):
            return 'unmanaged'
        if content_digest(target) != receipt['digest']:
            return 'modified'
        return 'unchanged' if identity == desired else 'update'
    except (ValueError, OSError, UnicodeError):
        return 'unmanaged'


def safe_path(value, root_ok=False):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('Unsafe relative path: ' + repr(value))
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or (value == '.' and not root_ok):
        raise ValueError('Unsafe relative path: ' + value)
    for part in path.parts:
        if (part.endswith(('.', ' ')) or re.search(r'[<>"|?*\x00-\x1f]', part)
                or re.fullmatch(r'(?i:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?', part)):
            raise ValueError('Unsafe Windows path: ' + value)
    return path


def skill_name(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError('Missing or unsafe SKILL.md: ' + str(path))
    text = path.read_text(encoding='utf-8-sig')
    match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|\s*\Z)', text, re.S)
    name = re.search(r'''^name:[ \t]*(["']?)([\w-]+)\1[ \t]*$''', match[1], re.M) if match else None
    if not name:
        raise ValueError('Missing simple frontmatter name: ' + str(path))
    return name[2]


def load_manifest(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('schema_version') != 1 or not isinstance(data.get('packages'), list):
        raise ValueError('Unsupported dependency manifest')
    ids, names = set(), {'universal-web-dev'}
    for package in data['packages']:
        ident = package.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', ident) or ident in ids:
            raise ValueError('Invalid or duplicate package id')
        ids.add(ident)
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', package.get('repo', '')):
            raise ValueError('Expected GitHub owner/repo')
        if not re.fullmatch(r'[0-9a-fA-F]{40}', package.get('ref', '')):
            raise ValueError('Dependency must be pinned to a full commit SHA')
        profiles = package.get('profiles')
        if not isinstance(profiles, list) or not profiles or not set(profiles) <= PROFILES:
            raise ValueError('Invalid dependency profiles')
        if not isinstance(package.get('license'), str) or not package['license'].strip():
            raise ValueError('Missing license label')
        licenses = package.get('license_files')
        if not isinstance(licenses, list) or not licenses:
            raise ValueError('Missing license files')
        for item in licenses:
            safe_path(item)
        if not isinstance(package.get('skills'), list):
            raise ValueError('Missing skills list')
        for skill in package['skills']:
            name = skill.get('name', '')
            if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', name) or name in names:
                raise ValueError('Invalid or duplicate skill name')
            names.add(name)
            safe_path(skill.get('path'), root_ok=True)
            support = skill.get('support', [])
            if not isinstance(support, list):
                raise ValueError('Invalid support list')
            for item in support:
                safe_path(item.get('source'), root_ok=True)
                target = safe_path(item.get('target'))
                if target.parts[0] in {'SKILL.md', 'UPSTREAM-NOTICE.txt', 'upstream-licenses'}:
                    raise ValueError('Support must not replace entrypoint or attribution')
        if not package['skills'] and not package.get('manual_reason'):
            raise ValueError('Empty package requires manual_reason')
    return data


def default_dest():
    return Path(os.environ['CODEX_HOME']) / 'skills' if os.environ.get('CODEX_HOME') else Path.home() / '.codex' / 'skills'


def download(package):
    url = 'https://codeload.github.com/{}/zip/{}'.format(package['repo'], package['ref'])
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD:
        raise ValueError('Archive exceeds download limit')
    return data


def unpack(data, target, selected_paths=None):
    if len(data) > MAX_DOWNLOAD:
        raise ValueError('Archive exceeds download limit')
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        items = archive.infolist()
        if len(items) > MAX_FILES or sum(item.file_size for item in items) > MAX_EXPANDED:
            raise ValueError('Archive exceeds extraction limits')
        roots, seen, selected_items = set(), set(), []
        selections = [safe_path(p, root_ok=True) for p in selected_paths] if selected_paths is not None else None
        for item in items:
            path = safe_path(item.filename.rstrip('/'))
            mode = item.external_attr >> 16
            folded = str(path).casefold()
            if folded in seen:
                raise ValueError('Duplicate archive path')
            seen.add(folded)
            roots.add(path.parts[0])
            relative = PurePosixPath(*path.parts[1:])
            selected = selections is None or any(relative.is_relative_to(p) or p.is_relative_to(relative) for p in selections)
            if selected:
                if stat.S_ISLNK(mode) or (stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR)):
                    raise ValueError('Selected archive path is a symlink or special file: ' + str(relative))
                selected_items.append(item)
        if len(roots) != 1:
            raise ValueError('Expected one archive root')
        for item in selected_items:
            path = target.joinpath(*PurePosixPath(item.filename).parts)
            if item.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(item) as source, path.open('xb') as output:
                    shutil.copyfileobj(source, output, length=65536)
                permissions = (item.external_attr >> 16) & 0o777
                if permissions:
                    os.chmod(path, permissions)
        return target / roots.pop()


def copy_safe(source, target):
    if source.is_symlink():
        raise ValueError('Refusing source symlink: ' + str(source))
    if source.is_dir():
        target.mkdir(parents=True, exist_ok=True)
        for child in source.iterdir():
            if child.name == '__pycache__' or child.suffix == '.pyc':
                continue
            copy_safe(child, target / child.name)
    elif source.is_file():
        if target.exists():
            raise ValueError('Copy collision: ' + str(target))
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        os.chmod(target, stat.S_IMODE(source.stat().st_mode) & 0o777)
    else:
        raise ValueError('Missing source: ' + str(source))


def locate_existing(dest, name):
    preferred = dest / name
    if preferred.is_symlink():
        raise ValueError('Refusing destination symlink: ' + str(preferred))
    matches = []
    if dest.exists():
        for folder in dest.iterdir():
            if folder.is_symlink() or not folder.is_dir():
                continue
            try:
                declared = skill_name(folder / 'SKILL.md')
            except (ValueError, UnicodeError):
                continue
            if declared == name:
                matches.append(folder)
    if preferred.exists() and preferred not in matches:
        raise ValueError('Destination has unrelated content: ' + str(preferred))
    if len(matches) > 1:
        raise ValueError('Multiple installed folders declare name: ' + name)
    return matches[0] if matches else preferred


def commit(staged, destinations, dest):
    # All writes and renames stay under these resolved, verified roots.
    dest = dest.resolve()
    backup_root = dest.parent / (dest.name + '-backups')
    if backup_root.is_symlink():
        raise ValueError('Refusing backup symlink')
    backup = backup_root / uuid.uuid4().hex
    changes = []
    dest.mkdir(parents=True, exist_ok=True)
    try:
        for name, target in destinations.items():
            if target.parent.resolve() != dest:
                raise ValueError('Destination escaped skills directory')
            old = None
            if target.exists():
                backup.mkdir(parents=True, exist_ok=True)
                old = backup / target.name
                os.replace(target, old)
            changes.append((target, old, False))
            os.replace(staged / name, target)
            changes[-1] = (target, old, True)
    except BaseException:
        for target, old, installed in reversed(changes):
            if installed:
                # Move our installed folder back to owned staging; never delete user folders.
                os.replace(target, staged / target.name)
            if old:
                os.replace(old, target)
        raise
    if backup.exists():
        print('Backups: ' + str(backup))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', action='append', choices=sorted(PROFILES | {'all'}))
    parser.add_argument('--dest', type=Path, default=default_dest())
    parser.add_argument('--manifest', type=Path, default=SOURCE_ROOT / 'dependencies.lock.json')
    parser.add_argument('--apply', action='store_true')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--update', action='store_true', help='Explicitly replace existing skills, retaining backups')
    mode.add_argument('--sync', action='store_true', help='Update unchanged receipt-managed skills to the lock pins')
    args = parser.parse_args(argv)
    manifest = load_manifest(args.manifest)
    profiles = set(args.profile or ['core'])
    selected = [p for p in manifest['packages'] if 'all' in profiles or profiles.intersection(p['profiles'])]
    dest = args.dest.expanduser().absolute()
    if dest.is_symlink():
        raise ValueError('Refusing destination symlink')
    dest = dest.resolve()
    entries = [('universal-web-dev', None, None)]
    for package in selected:
        if package.get('manual_reason'):
            print('Manual: {}: {}'.format(package['id'], package['manual_reason']))
        entries.extend((s['name'], package, s) for s in package['skills'])
    pending = []
    for name, package, skill in entries:
        target = locate_existing(dest, name)
        if package and package.get('canonical_folders') and target.name != name:
            raise ValueError('canonical folder required for {}: found {}; review and manually relocate it to {} before retrying, because this package uses sibling references'.format(name, target, dest / name))
        action = 'install'
        if target.exists():
            if args.update:
                action = 'update'
            elif args.sync:
                status = managed_status(target, desired_identity(name, package, skill))
                action = 'update' if status == 'update' else 'skip (' + status + ')'
            else:
                action = 'skip'
        print('{} {} -> {}'.format(action, name, target))
        if action in {'install', 'update'}:
            pending.append((name, package, skill, target))
    if not args.apply or not pending:
        return 0
    # Stage on the destination filesystem; installation starts only after all checks pass.
    ancestor = dest.parent
    while not ancestor.exists():
        ancestor = ancestor.parent
    with tempfile.TemporaryDirectory(prefix='skill-install-', dir=ancestor) as scratch:
        scratch = Path(scratch)
        staged = scratch / 'staged'
        staged.mkdir()
        repositories = {}
        for name, package, skill, target in pending:
            output = staged / name
            if package is None:
                output.mkdir()
                for item in WRAPPER_FILES:
                    source = SOURCE_ROOT / item
                    if source.exists():
                        copy_safe(source, output / item)
            else:
                key = (package['repo'], package['ref'])
                if key not in repositories:
                    paths = set()
                    for _, candidate, candidate_skill, _ in pending:
                        if candidate and (candidate['repo'], candidate['ref']) == key:
                            paths.add(candidate_skill['path'])
                            paths.update(s['source'] for s in candidate_skill.get('support', []))
                            paths.update(candidate['license_files'])
                    print('Source: {} @ {}'.format(*key), flush=True)
                    repositories[key] = unpack(download(package), scratch / ('archive-' + str(len(repositories))),
                                               selected_paths=sorted(paths))
                repository = repositories[key]
                copy_safe(repository.joinpath(*safe_path(skill['path'], True).parts), output)
                for support in skill.get('support', []):
                    copy_safe(repository.joinpath(*safe_path(support['source'], True).parts), output.joinpath(*safe_path(support['target']).parts))
                for license_file in package['license_files']:
                    copy_safe(repository.joinpath(*safe_path(license_file).parts), output / 'upstream-licenses' / license_file)
                (output / 'UPSTREAM-NOTICE.txt').write_text('{}\nCommit: {}\nLicense: {}\nUpstream content retains its original license.\n'.format(package['repo'], package['ref'], package['license']), encoding='utf-8')
            if skill_name(output / 'SKILL.md') != name:
                raise ValueError('SKILL.md name does not match manifest: ' + name)
            if (output / RECEIPT).exists():
                raise ValueError('Source contains reserved install receipt: ' + name)
            receipt = {'version': 1, 'identity': desired_identity(name, package, skill),
                       'digest': content_digest(output)}
            (output / RECEIPT).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
        commit(staged, {name: target for name, _, _, target in pending}, dest)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        raise SystemExit('Install failed: ' + str(error))
