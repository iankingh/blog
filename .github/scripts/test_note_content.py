"""Ensure new notes cannot bypass manifest coverage or exact pagination checks."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    'note_content', Path(__file__).with_name('check-note-content.py'))
notes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(notes)


class NoteContentTests(unittest.TestCase):
    def test_manifest_requires_exact_unique_coverage(self):
        actual = {'a.md', 'b.md'}
        notes.validate_manifest_paths([{'path': p} for p in sorted(actual)], actual)
        for paths in [[], ['a.md'], ['a.md', 'a.md', 'b.md'], ['a.md', 'c.md']]:
            with self.subTest(paths=paths), self.assertRaises(ValueError):
                notes.validate_manifest_paths([{'path': p} for p in paths], actual)

    def test_exact_and_partial_page_boundaries(self):
        for count, sizes in [(1, [1]), (10, [10]), (11, [10, 1]),
                             (130, [10] * 13), (132, [10] * 13 + [2])]:
            with self.subTest(count=count):
                self.assertEqual(notes.pagination_sizes(count), sizes)

    def test_empty_population_is_not_a_pass(self):
        with self.assertRaises(ValueError):
            notes.pagination_sizes(0)

    def fixture(self, root, count):
        pages = {}
        for section in ('', 'post/'):
            for number, size in enumerate(notes.pagination_sizes(count), 1):
                p = root / section / ('index.html' if number == 1 else f'page/{number}/index.html')
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('<article class="quest-card"></article>' * size)
                pages[p.resolve()] = notes.Page(p.read_text())
        return pages

    def test_partial_last_page_requires_exact_card_count(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages = self.fixture(root, 132)
            notes.check_pagination(root, pages, 132)
            p = root / 'post/page/14/index.html'
            pages[p.resolve()] = notes.Page('<article class="quest-card"></article>' * 10)
            with self.assertRaisesRegex(ValueError, 'expected 2 quest cards'):
                notes.check_pagination(root, pages, 132)

    def test_missing_or_stale_pages_fail(self):
        for mode in ('missing', 'stale'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                pages = self.fixture(root, 132)
                if mode == 'missing':
                    (root / 'page/14/index.html').unlink()
                else:
                    p = root / 'post/page/15/index.html'
                    p.parent.mkdir(parents=True)
                    p.write_text('stale')
                with self.assertRaises(ValueError):
                    notes.check_pagination(root, pages, 132)

    def test_search_requires_exact_count_and_unique_urls(self):
        import json
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for entries in [[{'url': '/a/'}], [{'url': '/a/'}, {'url': '/a/'}]]:
                with self.subTest(entries=entries):
                    (root / 'search-index.json').write_text(json.dumps(entries))
                    with self.assertRaisesRegex(ValueError, '2 unique published notes'):
                        notes.check_site(root, 2)


if __name__ == '__main__':
    unittest.main()
