"""Catch broken install guards and generated Skills navigation regressions."""
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("skills_check", Path(__file__).with_name("check-skills.py"))
skills = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skills)


class SkillsChecksTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        source, site = root / "source", root / "site"
        (source / "content/post").mkdir(parents=True)
        (site / "page/2").mkdir(parents=True)
        entries, cards = [], []
        for order, name in enumerate(skills.NOTES, 1):
            (source / f"content/post/{name}.md").write_text(
                f'---\ntitle: "{name}"\nfeaturedOrder: {order}\ndraft: false\n---\n')
            url = f"/blog/post/{name}/"
            entries.append({"title": name, "url": url})
            cards.append(f'<article class="featured-card"><a href="https://iankingh.github.io{url}">note</a></article>')
            page = site / f"post/{name}/index.html"
            page.parent.mkdir(parents=True)
            page.write_text('<a href="https://github.com/iankingh/agent-skills">repo</a>' + ''.join(
                f'<a href="/blog/post/{other}/">next</a>' for other in skills.NOTES if other != name))
        (site / "search-index.json").write_text(json.dumps(entries))
        (site / "index.html").write_text('<h3 id="pinned-title">Pinned</h3>' + ''.join(cards))
        (site / "page/2/index.html").write_text('<article class="quest-card"><a href="/blog/post/example/">ordinary</a></article>')
        (site / "skills").mkdir()
        (site / "skills/index.html").write_text('<h1>技能圖鑑<span>Skill Codex</span></h1><div class="codex-card"></div>')
        return source, site, cards

    def test_generated_pages_match_sources_and_keep_atlas(self):
        source, site, _ = self.fixture()
        skills.check_site(source, site)

    def test_reordered_homepage_fails(self):
        source, site, cards = self.fixture()
        (site / "index.html").write_text('<h3 id="pinned-title">Pinned</h3>' + ''.join(reversed(cards)))
        with self.assertRaisesRegex(ValueError, "featured order"):
            skills.check_site(source, site)

    def test_second_page_cannot_repeat_pinned_section(self):
        source, site, _ = self.fixture()
        (site / "page/2/index.html").write_text('<h3 id="pinned-title">Pinned</h3>')
        with self.assertRaisesRegex(ValueError, "Second homepage"):
            skills.check_site(source, site)

    def test_missing_mutual_link_and_replaced_atlas_fail(self):
        for problem in ("mutual", "atlas"):
            with self.subTest(problem=problem):
                source, site, _ = self.fixture()
                if problem == "mutual":
                    (site / f"post/{skills.NOTES[0]}/index.html").write_text('<a href="https://github.com/iankingh/agent-skills">repo</a>')
                else:
                    (site / "skills/index.html").write_text('<h1>Skills 收藏</h1>')
                with self.assertRaisesRegex(ValueError, "mutual|atlas"):
                    skills.check_site(source, site)

    def test_duplicate_search_result_fails(self):
        source, site, _ = self.fixture()
        entries = json.loads((site / "search-index.json").read_text())
        (site / "search-index.json").write_text(json.dumps(entries + [entries[0]]))
        with self.assertRaisesRegex(ValueError, "appear once"):
            skills.check_site(source, site)

    def test_install_fixture_detects_missing_broken_symlink_guard(self):
        article = (skills.ROOT / "content/post/ub-mode-guide.md").read_text()
        block = next(block for block in re.findall(r"```sh\n(.*?)\n```", article, re.S)
                     if "cp ub-mode-source/SKILL.md" in block)
        broken = block.replace(' || [ -L "$ub_skill_dir" ]', '')
        self.assertNotEqual(broken, block)
        with self.assertRaisesRegex(ValueError, "broken-symlink"):
            skills.check_copy_snippet(broken)
