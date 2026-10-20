import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('doctor', Path(__file__).parents[1] / 'scripts/doctor.py')
doctor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(doctor)


class DoctorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / 'package'
        self.package.mkdir()
        self.entry = '---\nname: universal-web-dev\ndescription: Test\n---\n# Example\n'
        (self.package / 'SKILL.md').write_text(self.entry, encoding='utf-8')
        self.manifest = {'schema_version': 1, 'packages': [{'id': 'example', 'repo': 'owner/repo', 'ref': 'a' * 40, 'profiles': ['core'], 'license': 'MIT', 'license_files': ['LICENSE'], 'skills': [{'name': 'example', 'path': 'skills/example'}]}]}
        self.save_manifest()

    def save_manifest(self):
        (self.package / 'dependencies.lock.json').write_text(json.dumps(self.manifest), encoding='utf-8')

    def check(self, roots=None, package_only=True):
        return doctor.check(self.package, roots or [], ['core'], package_only)

    def test_package_only_needs_no_installed_dependencies(self):
        self.assertEqual(self.check()['errors'], [])

    def test_missing_entrypoint_is_reported(self):
        (self.package / 'SKILL.md').unlink()
        self.assertTrue(self.check()['errors'])

    def test_broken_reference_is_reported(self):
        (self.package / 'SKILL.md').write_text(self.entry + '[broken](references/missing.md)', encoding='utf-8')
        self.assertTrue(self.check()['errors'])

    def test_reference_cannot_escape_package(self):
        (self.root / 'private.md').write_text('private', encoding='utf-8')
        (self.package / 'SKILL.md').write_text(self.entry + '[outside](../private.md)', encoding='utf-8')
        self.assertTrue(self.check()['errors'])

    def test_missing_dependency_cannot_pass(self):
        result = self.check(package_only=False)
        self.assertEqual(result['dependencies']['example'], 'missing')
        self.assertTrue(result['errors'])

    def test_compatible_skills_in_another_root(self):
        skills = self.root / 'skills'
        for name in ['example', 'universal-web-dev']:
            target = skills / name
            target.mkdir(parents=True)
            (target / 'SKILL.md').write_text('---\nname: ' + name + '\ndescription: Test\n---\n', encoding='utf-8')
        result = self.check([skills], False)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['dependencies']['example'], 'present')

    def test_incomplete_manifest_cannot_pass_package_only(self):
        for value in [None, []]:
            if value is None:
                self.manifest['packages'][0].pop('skills', None)
            else:
                self.manifest['packages'][0]['skills'] = value
            self.save_manifest()
            self.assertTrue(self.check()['errors'])

    def test_canonical_family_cannot_be_split_or_aliased(self):
        self.manifest['packages'][0]['canonical_folders'] = True
        self.save_manifest()
        skills = self.root / 'skills'
        for folder, name in [('old-example', 'example'), ('universal-web-dev', 'universal-web-dev')]:
            path = skills / folder
            path.mkdir(parents=True)
            (path / 'SKILL.md').write_text('---\nname: ' + name + '\n---\n', encoding='utf-8')
        self.assertTrue(self.check([skills], False)['errors'])

    def test_manual_dependency_is_not_verified(self):
        self.manifest['packages'][0]['manual_reason'] = 'Requires supported tool'
        self.save_manifest()
        self.assertTrue(self.check(package_only=False)['errors'])


if __name__ == '__main__':
    unittest.main()
