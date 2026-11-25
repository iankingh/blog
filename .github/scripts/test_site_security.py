"""Ensure published links keep the reviewed new-window and external-mark conventions."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'site_security', Path(__file__).with_name('check-site-security.py'))
security = importlib.util.module_from_spec(spec)
spec.loader.exec_module(security)

CSP = ('<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; object-src \'none\'; '
       'base-uri \'none\'; form-action \'none\'; script-src \'self\'">')


def errors_for(body):
    page = security.Page()
    page.feed(CSP + body)
    return page.check()


class LinkAffordanceTests(unittest.TestCase):
    def test_marked_new_window_link_passes(self):
        self.assertEqual(errors_for(
            '<a href="https://github.com/x" target="_blank" rel="noopener noreferrer">GitHub'
            '<span aria-hidden="true">↗</span><span class="sr-only">（另開新視窗）</span></a>'), [])

    def test_new_window_link_requires_notice_and_noopener(self):
        errors = errors_for('<a href="https://github.com/x" target=_blank>GitHub ↗</a>')
        self.assertIn('new-window link without rel=noopener', errors)
        self.assertTrue(any(e.startswith('new-window link without notice') for e in errors))

    def test_icon_only_new_window_link_may_use_aria_label(self):
        self.assertEqual(errors_for(
            '<a href="https://github.com/x" target="_blank" rel="noopener" '
            'aria-label="查看我的 GitHub（另開新視窗）"><svg aria-hidden="true"></svg></a>'), [])

    def test_internal_link_must_not_use_external_mark(self):
        self.assertEqual(errors_for('<a href="/blog/post/a/">筆記 →</a>'), [])
        self.assertTrue(errors_for('<a href="/blog/post/a/">筆記 ↗</a>'))

    def test_aria_label_overrides_child_new_window_notice(self):
        errors = errors_for(
            '<a href="https://github.com/x" target="_blank" rel="noopener" aria-label="GitHub">'
            'GitHub<span class="sr-only">（另開新視窗）</span></a>')
        self.assertIn('new-window link without notice: https://github.com/x', errors)

    def test_same_window_external_link_may_use_mark(self):
        self.assertEqual(errors_for('<a href="https://disqus.com/x">公開留言板 ↗</a>'), [])


if __name__ == '__main__':
    unittest.main()
