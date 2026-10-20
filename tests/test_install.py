import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import stat
import unittest
from unittest.mock import patch
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'install.py'


def archive(files, symlink=None):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w') as out:
        for name, content in files.items():
            out.writestr('repo-sha/' + name, content)
        if symlink:
            info = zipfile.ZipInfo('repo-sha/' + symlink)
            info.create_system = 3
            info.external_attr = 0o120777 << 16
            out.writestr(info, 'elsewhere')
    return stream.getvalue()


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.exists(), 'installer implementation is missing')
        spec = importlib.util.spec_from_file_location('skill_install', SCRIPT)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        (self.source / 'SKILL.md').write_text('---\nname: universal-web-dev\n---\nwrapper')
        (self.source / 'references').mkdir()
        (self.source / 'references' / 'guide.md').write_text('guide')
        self.dest = self.root / 'skills'
        self.manifest = self.root / 'dependencies.json'
        self.data = {'schema_version': 1, 'packages': [{
            'id': 'example', 'profiles': ['core'], 'repo': 'owner/repo',
            'ref': 'a' * 40, 'license': 'MIT', 'license_files': ['LICENSE'],
            'skills': [{'name': 'example', 'path': 'nested/skill',
                        'support': [{'source': 'shared', 'target': 'shared'}]}]}]}
        self.write_manifest()
        self.payload = archive({'nested/skill/SKILL.md': '---\nname: example\n---\nbody',
                                'nested/skill/references/a.md': 'ref',
                                'shared/helper.py': 'unexecuted', 'LICENSE': 'MIT text',
                                'unselected/private.txt': 'omit'})

    def write_manifest(self):
        self.manifest.write_text(json.dumps(self.data))

    def run_install(self, *args, payload=None):
        with patch.object(self.mod, 'SOURCE_ROOT', self.source), \
                patch.object(self.mod, 'download', return_value=payload or self.payload), \
                contextlib.redirect_stdout(io.StringIO()):
            return self.mod.main(['--manifest', str(self.manifest), '--dest', str(self.dest), *args])

    def test_plan_creates_nothing_and_never_downloads(self):
        with patch.object(self.mod, 'download', side_effect=AssertionError('network')):
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.mod.main(['--manifest', str(self.manifest), '--dest', str(self.dest)])
        self.assertFalse(self.dest.exists())
        self.assertIn('example', out.getvalue())

    def test_default_dest_obeys_codex_home(self):
        with patch.dict(os.environ, {'CODEX_HOME': str(self.root)}):
            self.assertEqual(self.mod.default_dest(), self.root / 'skills')
        environment = dict(os.environ)
        environment.pop('CODEX_HOME', None)
        with patch.dict(os.environ, environment, clear=True):
            self.assertEqual(self.mod.default_dest(), Path.home() / '.codex' / 'skills')

    def test_manifest_rejects_unpinned_repo_and_unsafe_paths(self):
        for field, value in [('ref', 'main'), ('repo', 'https://evil/repo'),
                             ('license_files', ['../LICENSE'])]:
            with self.subTest(field=field):
                original = self.data['packages'][0][field]
                self.data['packages'][0][field] = value
                self.write_manifest()
                with self.assertRaises(ValueError):
                    self.mod.load_manifest(self.manifest)
                self.data['packages'][0][field] = original

    def test_apply_copies_selected_skill_support_license_and_wrapper(self):
        self.run_install('--apply')
        target = self.dest / 'example'
        self.assertEqual((target / 'shared/helper.py').read_text(), 'unexecuted')
        self.assertEqual((target / 'references/a.md').read_text(), 'ref')
        self.assertEqual((target / 'upstream-licenses/LICENSE').read_text(), 'MIT text')
        self.assertIn('owner/repo', (target / 'UPSTREAM-NOTICE.txt').read_text())
        self.assertFalse((target / 'unselected').exists())
        self.assertTrue((self.dest / 'universal-web-dev/references/guide.md').exists())

    def test_root_skill_is_supported(self):
        self.data['packages'][0]['skills'] = [{'name': 'example', 'path': '.'}]
        self.write_manifest()
        self.run_install('--apply', payload=archive({'SKILL.md': '---\nname: example\n---', 'LICENSE': 'MIT'}))
        self.assertTrue((self.dest / 'example/SKILL.md').exists())

    def test_invalid_archives_leave_destination_untouched(self):
        cases = [archive({'nested/skill/other': 'missing', 'LICENSE': 'MIT'}),
                 archive({'nested/skill/SKILL.md': '---\nname: wrong\n---', 'LICENSE': 'MIT'}),
                 archive({'../escape': 'bad'}), archive({}, symlink='link')]
        for payload in cases:
            with self.subTest(payload=len(payload)), self.assertRaises(ValueError):
                self.run_install('--apply', payload=payload)
            self.assertFalse(self.dest.exists())

    def test_existing_declared_name_is_reused_and_skipped(self):
        alternate = self.dest / 'old-folder'
        alternate.mkdir(parents=True)
        (alternate / 'SKILL.md').write_text('---\nname: example\n---\nold')
        self.run_install('--apply')
        self.assertIn('old', (alternate / 'SKILL.md').read_text())
        self.assertFalse((self.dest / 'example').exists())

    def test_canonical_package_rejects_existing_alternate_folder_without_mutation(self):
        self.data['packages'][0]['canonical_folders'] = True
        self.write_manifest()
        alternate = self.dest / 'alternate-example'
        alternate.mkdir(parents=True)
        entry = alternate / 'SKILL.md'
        entry.write_text('---\nname: example\n---\nkeep')
        for args in ((), ('--apply',), ('--apply', '--update')):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'canonical folder required'):
                self.run_install(*args)
        self.assertEqual(entry.read_text(), '---\nname: example\n---\nkeep')
        self.assertFalse((self.dest / 'example').exists())
        self.assertFalse((self.dest / 'universal-web-dev').exists())

    def test_canonical_package_accepts_existing_canonical_folder(self):
        self.data['packages'][0]['canonical_folders'] = True
        self.write_manifest()
        target = self.dest / 'example'
        target.mkdir(parents=True)
        entry = target / 'SKILL.md'
        entry.write_text('---\nname: example\n---\nkeep')
        self.run_install('--apply')
        self.assertEqual(entry.read_text(), '---\nname: example\n---\nkeep')

    def test_mismatching_destination_is_never_overwritten(self):
        target = self.dest / 'example'
        target.mkdir(parents=True)
        (target / 'SKILL.md').write_text('---\nname: different\n---')
        with self.assertRaises(ValueError):
            self.run_install('--apply', '--update')
        self.assertIn('different', (target / 'SKILL.md').read_text())

    def test_update_preserves_backup_outside_active_skills(self):
        self.run_install('--apply')
        (self.dest / 'example/old.txt').write_text('preserve me')
        self.run_install('--apply', '--update')
        self.assertFalse((self.dest / 'example/old.txt').exists())
        backups = list((self.root / 'skills-backups').glob('*/example/old.txt'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'preserve me')

    def test_windows_alias_paths_are_rejected(self):
        for filename in ('nested/../escape', 'nested/.. /escape', 'nested/NUL', 'nested/file:stream', '/absolute'):
            with self.subTest(filename=filename), self.assertRaises(ValueError):
                self.mod.safe_path(filename)

    def test_archive_expansion_is_bounded_before_destination_mutation(self):
        with patch.object(self.mod, 'MAX_EXPANDED', 10):
            with self.assertRaises(ValueError):
                self.run_install('--apply')
        self.assertFalse(self.dest.exists())

    def test_profiles_can_be_repeated(self):
        self.data['packages'][0]['profiles'] = ['backend']
        self.write_manifest()
        self.run_install('--apply')
        self.assertFalse((self.dest / 'example').exists())
        self.run_install('--apply', '--profile', 'core', '--profile', 'backend')
        self.assertTrue((self.dest / 'example').exists())

    def test_manual_only_packages_are_reported_without_network(self):
        self.data['packages'][0]['skills'] = []
        self.data['packages'][0]['manual_reason'] = 'Upstream requires manual setup'
        self.write_manifest()
        with patch.object(self.mod, 'SOURCE_ROOT', self.source), \
                patch.object(self.mod, 'download', side_effect=AssertionError('network')), \
                contextlib.redirect_stdout(io.StringIO()):
            self.mod.main(['--manifest', str(self.manifest), '--dest', str(self.dest), '--apply'])
        self.assertTrue((self.dest / 'universal-web-dev/SKILL.md').exists())
        self.assertFalse((self.dest / 'example').exists())

    def test_missing_license_stops_before_any_install(self):
        self.payload = archive({'nested/skill/SKILL.md': '---\nname: example\n---',
                                'shared/helper.py': 'test'})
        with self.assertRaises(ValueError):
            self.run_install('--apply')
        self.assertFalse(self.dest.exists())

    def test_wrapper_excludes_python_cache(self):
        cache = self.source / 'scripts/__pycache__'
        cache.mkdir(parents=True)
        (cache / 'test.pyc').write_bytes(b'cache')
        self.run_install('--apply')
        self.assertFalse((self.dest / 'universal-web-dev/scripts/__pycache__').exists())

    def test_simple_quoted_yaml_names_install_and_existing_aliases_skip(self):
        for quote in ('"', "'"):
            with self.subTest(quote=quote):
                alternate = self.dest / 'alternate'
                alternate.mkdir(parents=True, exist_ok=True)
                entry = alternate / 'SKILL.md'
                entry.write_text('---\nname: ' + quote + 'example' + quote + '\n---\nkeep')
                self.run_install('--apply')
                self.assertIn('keep', entry.read_text())
                self.assertFalse((self.dest / 'example').exists())
        self.assertEqual(self.mod.skill_name(entry), 'example')

    def test_upstream_quoted_name_is_accepted(self):
        self.payload = archive({'nested/skill/SKILL.md': '---\nname: "example"\n---',
                                'shared/helper.py': 'test', 'LICENSE': 'MIT'})
        self.run_install('--apply')
        self.assertTrue((self.dest / 'example/SKILL.md').exists())
        (self.dest / 'example/keep.txt').write_text('existing canonical folder')
        self.run_install('--apply')
        self.assertEqual((self.dest / 'example/keep.txt').read_text(), 'existing canonical folder')

    def test_unrelated_symlinks_are_ignored_during_selected_install(self):
        stream = io.BytesIO(self.payload)
        with zipfile.ZipFile(stream, 'a') as out:
            info = zipfile.ZipInfo('repo-sha/unrelated/link')
            info.create_system = 3
            info.external_attr = 0o120777 << 16
            out.writestr(info, '../elsewhere')
        self.run_install('--apply', payload=stream.getvalue())
        self.assertTrue((self.dest / 'example/shared/helper.py').exists())
        self.assertFalse((self.dest / 'example/unrelated').exists())

    def test_selected_symlink_and_symlink_ancestor_are_rejected(self):
        for link in ('nested/skill/link', 'nested'):
            with self.subTest(link=link), self.assertRaises(ValueError):
                self.mod.unpack(archive({'LICENSE': 'MIT'}, symlink=link), self.root / 'unpack',
                                selected_paths=['nested/skill', 'LICENSE'])
        self.assertFalse((self.root / 'unpack').exists())

    def test_unselected_traversal_and_global_size_are_still_rejected(self):
        with self.assertRaises(ValueError):
            self.mod.unpack(archive({'../escape': 'bad'}), self.root / 'unpack', selected_paths=['nested'])
        with patch.object(self.mod, 'MAX_EXPANDED', 2), self.assertRaises(ValueError):
            self.mod.unpack(archive({'unrelated/large': '123'}), self.root / 'unpack', selected_paths=['nested'])

    def executable_payload(self):
        stream = io.BytesIO(self.payload)
        with zipfile.ZipFile(stream, 'a') as out:
            info = zipfile.ZipInfo('repo-sha/nested/skill/scripts/run.sh')
            info.create_system = 3
            info.external_attr = 0o104755 << 16
            out.writestr(info, '#!/bin/sh\nexit 0\n')
        return stream.getvalue()

    def test_archive_regular_permissions_are_applied_without_special_bits(self):
        with patch.object(self.mod.os, 'chmod') as chmod:
            self.mod.unpack(self.executable_payload(), self.root / 'unpack')
        modes = [call.args[1] for call in chmod.call_args_list]
        self.assertIn(0o755, modes)
        self.assertTrue(all(mode & 0o7000 == 0 for mode in modes))

    @unittest.skipIf(os.name == 'nt', 'POSIX executable permission semantics')
    def test_executable_mode_survives_install_without_setuid(self):
        self.run_install('--apply', payload=self.executable_payload())
        script = self.dest / 'example/scripts/run.sh'
        self.assertEqual(stat.S_IMODE(script.stat().st_mode), 0o755)

    def test_failed_commit_restores_all_existing_folders(self):
        self.run_install('--apply')
        (self.dest / 'example/old.txt').write_text('preserve me')
        real = self.mod.os.replace
        def fail_example(source, target):
            if Path(source).name == 'example' and 'staged' in str(source):
                raise OSError('simulated install failure')
            return real(source, target)
        with patch.object(self.mod.os, 'replace', side_effect=fail_example):
            with self.assertRaises(OSError):
                self.run_install('--apply', '--update')
        self.assertEqual((self.dest / 'example/old.txt').read_text(), 'preserve me')


if __name__ == '__main__':
    unittest.main()
