"""Recheck Skills install snippets and built pages without old snapshots or plugins."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shlex
import subprocess
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
NOTES = ("ai-skills-list", "ub-mode-guide", "pstack-guide")


def require(condition, message):
    if not condition:
        raise ValueError(message)


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links, self.featured = [], []
        self.in_feature = False
        self.has_pinned = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") == "pinned-title":
            self.has_pinned = True
        if tag == "article":
            self.in_feature = "featured-card" in attrs.get("class", "").split()
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if self.in_feature:
                self.featured.append(urlsplit(attrs["href"]).path)
                self.in_feature = False

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_feature = False


def check_copy_snippet(block):
    """Run the article's copy operation against disposable destinations only."""
    scenarios = ("new", "directory", "file", "broken-symlink", "existing-symlink")
    for scenario in scenarios:
        with tempfile.TemporaryDirectory(prefix="blog-skill-copy-") as directory:
            root = Path(directory)
            source = root / "ub-mode-source/SKILL.md"
            source.parent.mkdir()
            source.write_text("fixture skill\n")
            target = root / "含空格 target/ub-mode"
            target.parent.mkdir()
            kept = root / "kept-skill"
            kept.mkdir()
            (kept / "SKILL.md").write_text("keep linked skill\n")
            if scenario == "directory":
                target.mkdir()
                (target / "SKILL.md").write_text("keep original\n")
            elif scenario == "file":
                target.write_text("keep file\n")
            elif scenario.endswith("symlink"):
                target.symlink_to(root / "missing" if scenario == "broken-symlink" else kept)
            script, count = re.subn(r"^ub_skill_dir=.*$", lambda _: "ub_skill_dir=" + shlex.quote(str(target)),
                                    block, count=1, flags=re.M)
            require(count == 1, "Install snippet must assign ub_skill_dir before copying")
            run = subprocess.run(["sh"], input=script, cwd=root, text=True,
                                 capture_output=True, timeout=10)
            require(run.returncode == 0, f"Install {scenario}: {run.stderr.strip()}")
            if scenario == "new":
                require((target / "SKILL.md").read_text() == source.read_text(), "New install did not copy the skill")
            elif scenario == "directory":
                require((target / "SKILL.md").read_text() == "keep original\n", "Existing skill was overwritten")
            elif scenario == "file":
                require(target.read_text() == "keep file\n", "Existing file was overwritten")
            else:
                require(target.is_symlink(), "Existing symlink was replaced")
                require(target.readlink() == (root / "missing" if scenario == "broken-symlink" else kept),
                        "Existing symlink target was changed")
                require((kept / "SKILL.md").read_text() == "keep linked skill\n", "Linked skill was overwritten")
            require(source.read_text() == "fixture skill\n", "Install modified its source")
    return len(scenarios)


def check_source(root):
    article = (root / "content/post/ub-mode-guide.md").read_text()
    blocks = re.findall(r"```sh\n(.*?)\n```", article, re.S)
    require(blocks, "ub-mode article has no shell snippets")
    for number, block in enumerate(blocks, 1):
        run = subprocess.run(["sh", "-n"], input=block, text=True, capture_output=True, timeout=10)
        require(run.returncode == 0, f"Shell snippet {number}: {run.stderr.strip()}")
    copies = [block for block in blocks if "cp ub-mode-source/SKILL.md" in block]
    require(len(copies) == 1, "Expected one install-copy snippet in ub-mode article")
    scenarios = check_copy_snippet(copies[0])
    print(f"PASS Skills: {len(blocks)} actual shell snippets; {scenarios} isolated install destinations")


def expected_featured(root, entries):
    selected = []
    for path in (root / "content/post").rglob("*.md"):
        front = path.read_text().split("---", 2)[1]
        order = re.search(r"^featuredOrder:\s*(\d+)\s*$", front, re.M)
        if not order or re.search(r"^draft:\s*true\s*$", front, re.M):
            continue
        title = re.search(r'^title:\s*(.+?)\s*$', front, re.M)[1]
        title = json.loads(title) if title.startswith('"') else title.strip("'")
        urls = [urlsplit(entry["url"]).path for entry in entries if entry["title"] == title]
        require(len(urls) == 1, f"Featured note must appear once in search: {title}")
        selected.append((int(order[1]), urls[0]))
    require(selected and all(order > 0 for order, _ in selected), "Featured orders must be positive")
    require(len({order for order, _ in selected}) == len(selected), "Featured orders must be unique")
    return [url for _, url in sorted(selected)[:3]]


def check_site(root, site):
    index = json.loads((site / "search-index.json").read_text())
    entries = index if isinstance(index, list) else index["posts"]
    expected = expected_featured(root, entries)
    home = Page((site / "index.html").read_text())
    require(home.has_pinned and home.featured == expected,
            f"Home featured order: expected {expected}, got {home.featured}")
    page2 = Page((site / "page/2/index.html").read_text())
    require(not page2.featured and not page2.has_pinned, "Second homepage repeats pinned notes")
    for name in NOTES:
        page = Page((site / f"post/{name}/index.html").read_text())
        require("https://github.com/iankingh/agent-skills" in page.links, f"{name}: missing project source")
        paths = [urlsplit(link).path for link in page.links]
        require(all(f"/blog/post/{other}/" in paths for other in NOTES if other != name),
                f"{name}: missing mutual article link")
        require(sum(urlsplit(entry["url"]).path == f"/blog/post/{name}/" for entry in entries) == 1,
                f"{name}: search must contain exactly one entry")
    atlas = (site / "skills/index.html").read_text()
    title = re.search(r"<h1\b[^>]*>(.*?)</h1>", atlas, re.S)
    require(title and "技能圖鑑" in re.sub(r"<[^>]+>", "", title[1]) and "codex-card" in atlas,
            "Skills atlas was replaced by the collection page")
    print("PASS Skills pages: configured featured order, page 2, mutual links, search and atlas")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, help="Fresh Hugo output; omit to check article snippets")
    args = parser.parse_args()
    if args.site:
        check_site(ROOT, args.site)
    else:
        check_source(ROOT)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, IndexError, subprocess.SubprocessError) as error:
        raise SystemExit(f"FAIL {error}")
