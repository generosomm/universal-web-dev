"""S01 structure and behavior checks. Standard library only; the tide checks need Node and skip without it."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import unittest

SITE = Path(__file__).resolve().parents[3]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags, self.ids, self.text = [], set(), []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.add(attrs['id'])

    def handle_data(self, data):
        self.text.append(data)

    def find(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]


class SiteStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page(SITE / 'index.html')

    def test_first_screen_says_what_it_is(self):
        self.assertEqual(len(self.page.find('h1')), 1)
        self.assertEqual(self.page.find('html')[0].get('lang'), 'en')
        descriptions = [m for m in self.page.find('meta') if m.get('name') == 'description']
        self.assertTrue(descriptions and len(descriptions[0]['content']) > 50)

    def test_images_have_alt_and_dimensions(self):
        for img in self.page.find('img'):
            with self.subTest(src=img.get('src')):
                self.assertIn('alt', img)
                self.assertTrue(img.get('width') and img.get('height'))

    def test_every_section_is_named_by_a_heading(self):
        for section in self.page.find('section'):
            self.assertIn(section.get('aria-labelledby'), self.page.ids)

    def test_internal_links_and_files_resolve(self):
        for a in self.page.find('a'):
            href = a.get('href', '')
            if href.startswith('#'):
                self.assertIn(href[1:], self.page.ids, href)
        for tag, attr in [('link', 'href'), ('script', 'src')]:
            for item in self.page.find(tag):
                ref = item.get(attr, '')
                if ref and not ref.startswith(('http', 'data:')):
                    self.assertTrue((SITE / ref).is_file(), ref)

    def test_booking_uses_email_not_a_fake_checkout(self):
        mailto = [a for a in self.page.find('a') if a.get('href', '').startswith('mailto:')]
        self.assertGreaterEqual(len(mailto), 5)
        for form in self.page.find('form'):
            self.assertNotIn('action', form)
        self.assertFalse(self.page.find('input') and any(i.get('type') == 'password' for i in self.page.find('input')))

    def test_tide_has_a_no_script_answer_and_a_warning(self):
        text = ' '.join(self.page.text)
        self.assertIn('Tide times are posted by the door', text)
        self.assertIn('not for navigation', text)

    def test_not_found_page_exists_and_is_not_indexed(self):
        page = Page(SITE / '404.html')
        self.assertEqual(len(page.find('h1')), 1)
        self.assertTrue(any(m.get('name') == 'robots' and 'noindex' in m.get('content', '') for m in page.find('meta')))

    def test_script_is_a_classic_script(self):
        # Regression: an `export` in a non-module script stopped every feature from running.
        self.assertNotRegex((SITE / 'site.js').read_text(encoding='utf-8'), r'^\s*export\s')

    def test_no_secrets_or_gradients(self):
        css = (SITE / 'styles.css').read_text(encoding='utf-8')
        self.assertNotRegex(css, r'(linear|radial|conic)-gradient')
        for name in ['index.html', 'site.js', 'styles.css']:
            self.assertNotRegex((SITE / name).read_text(encoding='utf-8'), r'(?i)(api[_-]?key|secret|token)\s*[:=]')


@unittest.skipUnless(shutil.which('node'), 'Node is needed to run the tide model')
class TideModel(unittest.TestCase):
    def describe(self, year, month, day):
        script = ("const vm=require('vm');const fs=require('fs');const ctx={};"
                  "vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8')+';this.describe=describe;',ctx);"
                  "process.stdout.write(JSON.stringify(ctx.describe(new Date(%d,%d,%d))));" % (year, month - 1, day))
        out = subprocess.run(['node', '-e', script, str(SITE / 'site.js')], capture_output=True, text=True,
                             env={**os.environ, 'TZ': 'UTC'}, check=True)
        return json.loads(out.stdout)

    def test_two_low_tides_a_day(self):
        text = self.describe(2026, 3, 5)
        self.assertEqual(len(re.findall(r'\d\d:\d\d', text.split('.')[0])), 2)

    def test_windows_crossing_midnight_stay_on_the_chosen_day(self):
        # Regression: a 00:04 low tide was shown as "between 22:34 and 01:34".
        text = self.describe(2026, 10, 20)
        self.assertIn('until', text)
        self.assertNotIn('22:34', text)


if __name__ == '__main__':
    unittest.main()
