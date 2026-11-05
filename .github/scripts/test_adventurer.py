"""Exercise actual Hugo ability relations, compatibility and publication boundaries."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


class AdventurerTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory(prefix="blog-abilities-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        for directory in ("content/post", "content/abilities", "layouts/_partials/rpg", "data"):
            (root / directory).mkdir(parents=True)
        (root / "hugo.toml").write_text('baseURL="https://example.org/blog/"\n[params]\nmainSections=["post"]\n')
        (root / "data/skills.json").write_text(json.dumps([
            {"id":"design", "name":"Design", "tags":["design"]},
            {"id":"legacy", "name":"Legacy", "tags":["legacy"]}]))
        for name in ("abilities-data.html", "skills-data.html", "ability-links.html"):
            shutil.copyfile(ROOT / "layouts/_partials/rpg" / name, root / "layouts/_partials/rpg" / name)
        (root / "layouts/baseof.html").write_text('{{ block "main" . }}{{ end }}')
        (root / "layouts/home.html").write_text('{{ range partialCached "rpg/skills-data.html" .Site .Site.Language.Lang }}<p id="{{ .id }}">{{ .count }}</p>{{ end }}')
        (root / "layouts/page.html").write_text('{{ define "main" }}{{ .Content }}{{ partial "rpg/ability-links.html" . }}{{ end }}')
        self.note(root, "abilities/acceptance.md", {"title":"Acceptance", "ability_id":"acceptance", "skill":"design", "stage":"待練習"})
        return root

    def note(self, root, name, fields):
        # JSON front matter is a native Hugo input and avoids a test-only YAML parser.
        path = root / "content" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(fields) + "\n\nFixture article.\n")

    def build(self, root, *flags):
        return subprocess.run(["hugo", "--source", str(root), "--noBuildLock", *flags],
                              text=True, capture_output=True, timeout=30)

    def test_tag_and_duplicate_ability_associations_count_once_and_old_notes_work(self):
        root = self.fixture()
        self.note(root, "post/mixed.md", {"title":"Mixed", "tags":["design"], "abilities":["acceptance","acceptance"]})
        self.note(root, "post/explicit.md", {"title":"Explicit", "abilities":["acceptance"]})
        self.note(root, "post/old.md", {"title":"Old", "tags":["legacy"]})
        result = self.build(root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        home = (root / "public/index.html").read_text()
        self.assertIn('<p id="design">2</p>', home)
        self.assertIn('<p id="legacy">1</p>', home)
        self.assertEqual((root / "public/post/mixed/index.html").read_text().count('href="/blog/abilities/acceptance/"'), 1)

    def test_unknown_ability_fails_build(self):
        root = self.fixture()
        self.note(root,"post/bad.md",{"title":"Bad","abilities":["missing"]})
        result = self.build(root)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("unknown or draft ability",result.stdout+result.stderr)

    def test_duplicate_ability_id_fails_build(self):
        root=self.fixture()
        self.note(root,"abilities/duplicate.md",{"title":"Duplicate","ability_id":"acceptance","skill":"design"})
        result=self.build(root)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("Duplicate ability_id",result.stdout+result.stderr)

    def test_unproven_stage_fails_build(self):
        root=self.fixture()
        self.note(root,"abilities/acceptance.md",{"title":"Acceptance","ability_id":"acceptance","skill":"design","stage":"獨立完成"})
        result=self.build(root)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("needs public evidence",result.stdout+result.stderr)

    def test_draft_abilities_and_articles_do_not_inflate_public_counts_in_preview(self):
        root=self.fixture()
        self.note(root,"abilities/hidden.md",{"title":"Hidden","ability_id":"hidden","skill":"design","draft":True})
        self.note(root,"post/draft.md",{"title":"Draft","tags":["design"],"abilities":["hidden"],"draft":True})
        self.note(root,"post/public.md",{"title":"Public","abilities":["acceptance"]})
        result=self.build(root,"--buildDrafts")
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn('<p id="design">1</p>',(root/"public/index.html").read_text())
        self.assertNotIn('hidden/',(root/"public/post/public/index.html").read_text())

    def test_public_article_cannot_link_a_draft_ability(self):
        root=self.fixture()
        self.note(root,"abilities/hidden.md",{"title":"Hidden","ability_id":"hidden","skill":"design","draft":True})
        self.note(root,"post/public.md",{"title":"Public","abilities":["hidden"]})
        result=self.build(root,"--buildDrafts")
        self.assertNotEqual(result.returncode,0)
        self.assertIn("unknown or draft ability",result.stdout+result.stderr)

    def test_real_ability_layout_keeps_public_evidence_url_without_doubling_base_path(self):
        root = self.fixture()
        shutil.copyfile(ROOT / "layouts/ability.html", root / "layouts/ability.html")
        self.note(root, "abilities/acceptance.md", {
            "title":"Acceptance", "ability_id":"acceptance", "skill":"design",
            "stage":"獨立完成", "layout":"ability",
            "evidence":[{"title":"Public result", "url":"/blog/post/public/"}]})
        self.note(root,"post/public.md",{"title":"Public","abilities":["acceptance"]})
        result = self.build(root)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        page = (root / "public/abilities/acceptance/index.html").read_text()
        self.assertIn('href="/blog/post/public/"',page)
        self.assertNotIn('/blog/blog/',page)


if __name__ == "__main__":
    unittest.main()
