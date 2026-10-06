"""Check the 130-note review manifest and optional Hugo output (stdlib only).

Usage: python3 .github/scripts/check-note-content.py [--site /tmp/blog-output]
The manifest preserves publication dates and records the actual validation scope.
This checks structure and links, not the accuracy of every technical statement.
"""
import argparse
import json
from pathlib import Path
import re
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin

ROOT = Path(__file__).resolve().parents[2]

def fail(message):
    raise ValueError(message)

def fences(body, label):
    opened = None
    code = []
    prose = []
    for line in body.splitlines():
        if opened:
            if re.fullmatch(r'\s*' + re.escape(opened) + r'\s*', line):
                if not ''.join(code).strip():
                    fail(f'{label}: empty code block')
                opened = None
                code = []
            else:
                code.append(line)
        else:
            match = re.match(r'^(`{3,}|~{3,})(.*)$', line)
            if match:
                if not match[2].strip():
                    fail(f'{label}: missing code language')
                opened = match[1]
            else:
                prose.append(line)
    if opened:
        fail(f'{label}: unclosed code block')
    return '\n'.join(prose)

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.cards = set(), [], []
        self.feed(text)
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag in ('a', 'link') and a.get('href'):
            self.links.append(a['href'])
        if tag in ('img', 'script', 'source') and a.get('src'):
            self.links.append(a['src'])
        if tag == 'article' and 'quest-card' in a.get('class', '').split():
            self.cards.append(a)
        if tag == 'img' and 'alt' not in a:
            fail('Image missing alt attribute')

def check_site(site):
    index = json.loads((site / 'search-index.json').read_text())
    entries = index if isinstance(index, list) else index['posts']
    if len(entries) != 130 or len({x['url'] for x in entries}) != 130:
        fail('Search index must contain 130 unique published notes')
    pages = {p.resolve(): Page(p.read_text()) for p in site.rglob('*.html')}
    broken = []
    for filename, page in pages.items():
        base = 'https://iankingh.github.io/blog/' + str(filename.relative_to(site.resolve())).replace('index.html', '')
        for raw in page.links:
            if raw.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
                continue
            url = urlsplit(urljoin(base, raw))
            if url.netloc != 'iankingh.github.io' or not url.path.startswith('/blog/'):
                continue
            relative = unquote(url.path[len('/blog/'):])
            target = (site / relative).resolve()
            if target.is_dir():
                target = target / 'index.html'
            elif not target.exists() and not target.suffix:
                target = target / 'index.html'
            if not target.exists():
                broken.append((str(filename.relative_to(site.resolve())), raw))
            elif url.fragment and target.suffix == '.html' and target in pages:
                if unquote(url.fragment) not in pages[target].ids:
                    broken.append((str(filename.relative_to(site.resolve())), raw))
    if broken:
        fail('Broken internal links/assets/anchors:\n' + '\n'.join(map(str, sorted(set(broken))[:50])))
    for section in ('', 'post/'):
        for number in range(1, 14):
            p = site / section / ('index.html' if number == 1 else f'page/{number}/index.html')
            if not p.exists() or len(pages[p.resolve()].cards) != 10:
                fail(f'{section or "home"} page {number}: expected 10 quest cards')
        if (site / section / 'page/14/index.html').exists():
            fail('Unexpected page 14')
    print(f'PASS search 130 notes; home/post 13 × 10; links, anchors, images/assets in {len(pages)} HTML pages')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path)
    args = parser.parse_args()
    rows = json.loads((ROOT / 'docs/note-review.json').read_text())
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / 'content/post').rglob('*.md')}
    if len(rows) != 130 or {r['path'] for r in rows} != actual:
        fail('Manifest must cover all 130 notes exactly once')
    for row in rows:
        p = ROOT / row['path']
        text = p.read_text()
        match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', text, re.S)
        if not match:
            fail(f'{p}: invalid front matter boundary')
        front, body = match.groups()
        for key in ('title', 'description', 'date', 'lastmod', 'categories', 'tags'):
            value = re.search(r'^' + key + r':[^\n]*', front, re.M)
            if not value or (key in ('title', 'description') and re.search(r':\s*[\"\']{2}\s*$', value[0])):
                fail(f'{p}: missing {key}')
        date = re.search(r'^date:\s*(.*)$', front, re.M)[1].strip('"\'')
        if date != row['originalDate']:
            fail(f'{p}: original publication date changed')
        if row['title'] not in front:
            fail(f'{p}: manifest title does not match the article')
        for source in row.get('originalReferences', []):
            if source not in body:
                fail(f'{p}: original reference removed: {source}')
        prose = fences(body, row['path'])
        if re.search(r'^(?:<<<<<<<|=======|>>>>>>>|#+\s*(?:TODO|TBD|待補|未完成)\s*$)', prose, re.M):
            fail(f'{p}: conflict/template marker')
        if '適用' not in prose or not row['context'] or not row['sources'] or not row['verification']:
            fail(f'{p}: missing context/source/validation scope')
        for reference in re.findall(r'{{< ref "([^"]+)" >}}', prose):
            if not (ROOT / 'content' / reference.lstrip('/')).exists():
                fail(f'{p}: unresolved ref {reference}')
        if not row['published'] or row['status'] != 'complete' or not re.search(r'^draft:\s*false\s*$', front, re.M):
            fail(f'{p}: review or publication incomplete')
    print('PASS 130 manifest entries: dates retained, summaries/context/sources, code fences and refs')
    if args.site:
        check_site(args.site.resolve())

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(f'FAIL {error}')
