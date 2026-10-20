import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('check_updates', Path(__file__).parents[1] / 'scripts/check-updates.py')
updates = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(updates)

OLD, NEW = 'a' * 40, 'b' * 40


def manifest(exclude=()):
    skill = {'name': 'example', 'path': 'skills/example'}
    if exclude:
        skill['exclude'] = list(exclude)
    return {'packages': [{'id': 'example', 'repo': 'owner/repo', 'ref': OLD, 'license_files': ['LICENSE'], 'skills': [skill]}]}


def fake(head, files):
    def get(path):
        if path.endswith('commits/HEAD'):
            return {'sha': head}
        return {'ahead_by': 2, 'files': [{'filename': f} for f in files]}
    return get


class CheckUpdatesTests(unittest.TestCase):
    def test_up_to_date_makes_no_compare_call(self):
        def get(path):
            self.assertTrue(path.endswith('commits/HEAD'), path)
            return {'sha': OLD}
        self.assertEqual(updates.check(manifest(), get)[0]['installed_changes'], [])

    def test_only_installed_files_are_reported(self):
        report = updates.check(manifest(), fake(NEW, ['README.md', 'skills/example/SKILL.md', 'LICENSE', 'skills/other/x.md']))
        self.assertEqual(report[0]['installed_changes'], ['skills/example/SKILL.md', 'LICENSE'])

    def test_excluded_paths_do_not_count(self):
        report = updates.check(manifest(['scripts']), fake(NEW, ['skills/example/scripts/run']))
        self.assertEqual(report[0]['installed_changes'], [])

    def test_truncated_compare_is_not_treated_as_clean(self):
        report = updates.check(manifest(), fake(NEW, ['x/%d' % i for i in range(300)]))
        self.assertFalse(report[0]['complete'])

    def test_write_moves_only_chosen_repos(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'dependencies.lock.json').write_text(OLD + ' ' + 'c' * 40, encoding='utf-8')
            (root / 'CREDITS.md').write_text('tree/' + OLD, encoding='utf-8')
            report = [{'repo': 'owner/repo', 'pinned': OLD, 'upstream': NEW},
                      {'repo': 'other/repo', 'pinned': 'c' * 40, 'upstream': 'd' * 40}]
            self.assertEqual(updates.write({'owner/repo'}, report, root), ['owner/repo'])
            self.assertEqual((root / 'dependencies.lock.json').read_text(encoding='utf-8'), NEW + ' ' + 'c' * 40)
            self.assertEqual((root / 'CREDITS.md').read_text(encoding='utf-8'), 'tree/' + NEW)


if __name__ == '__main__':
    unittest.main()
