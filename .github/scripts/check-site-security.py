"""Check security and link-affordance invariants on the HTML that will actually be published."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

EXTERNAL_MARK = "↗"
NEW_WINDOW_NOTE = "另開新視窗"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.policy = None
        self.redirect = False
        self.errors = []
        self.anchor = None

    def handle_data(self, data):
        if self.anchor is not None:
            self.anchor["text"].append(data)

    def handle_endtag(self, tag):
        if tag != "a" or self.anchor is None:
            return
        anchor, self.anchor = self.anchor, None
        text = "".join(anchor["text"])
        href = anchor["href"]
        if anchor["target"] == "_blank":
            if "noopener" not in anchor["rel"].split():
                self.errors.append("new-window link without rel=noopener")
            if NEW_WINDOW_NOTE not in (anchor["label"].strip() or text):
                self.errors.append(f"new-window link without notice: {href}")
        elif EXTERNAL_MARK in text and not urlsplit(href).scheme:
            self.errors.append(f"internal link uses external mark: {href}")

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "a":
            self.anchor = {"href": attributes.get("href") or "", "target": attributes.get("target") or "",
                           "rel": (attributes.get("rel") or "").lower(),
                           "label": attributes.get("aria-label") or "", "text": []}
        if tag == "meta":
            kind = attributes.get("http-equiv", "").lower()
            if kind == "content-security-policy":
                self.policy = attributes.get("content", "")
            if kind == "refresh":
                self.redirect = True
        loads_resource = tag in ("script", "img") or (
            tag == "link" and set(attributes.get("rel", "").split())
            & {"stylesheet", "preload", "modulepreload", "icon"}
        )
        if loads_resource and not self.redirect and self.policy is None:
            self.errors.append("CSP must precede resource loading")
        for name, value in attrs:
            if name.startswith("on"):
                self.errors.append(f"inline event handler: {name}")
            if name in ("href", "src", "action") and value:
                if urlsplit(value).scheme.lower() in ("javascript", "vbscript"):
                    self.errors.append("executable URL")
        if tag == "script":
            source = attributes.get("src")
            if not source and attributes.get("type", "").lower() not in (
                "application/json", "application/ld+json"
            ):
                self.errors.append("inline executable script")
        if tag in ("object", "embed"):
            self.errors.append(f"embedded active content: {tag}")

    def check(self):
        if self.redirect:
            return self.errors
        if not self.policy:
            self.errors.append("missing CSP")
            return self.errors
        directives = {}
        for entry in self.policy.split(";"):
            parts = entry.split()
            if parts:
                directives[parts[0]] = parts[1:]
        for directive in ("default-src", "object-src", "base-uri", "form-action"):
            if directives.get(directive) != ["'none'"]:
                self.errors.append(f"{directive} must be 'none'")
        allowed_scripts = {
            "'self'", "https://www.googletagmanager.com",
            "https://*.disqus.com", "https://*.disquscdn.com",
        }
        sources = directives.get("script-src", [])
        if "'self'" not in sources or not set(sources) <= allowed_scripts:
            self.errors.append("script-src must use the reviewed allowlist")
        return self.errors


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check-site-security.py <built-site-directory>")
    root = Path(sys.argv[1])
    files = sorted(root.rglob("*.html"))
    if not files or not (root / "index.html").is_file():
        raise SystemExit("No complete built site found")
    failures = []
    for path in files:
        page = Page()
        source = path.read_text(encoding="utf-8")
        page.feed(source)
        errors = page.check()
        if "busuanzi.ibruce.info" in source:
            errors.append("unused Busuanzi script")
        if errors:
            failures.append(f"{path.relative_to(root)}: {', '.join(sorted(set(errors)))}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Security checks passed for {len(files)} HTML files")


if __name__ == "__main__":
    main()
