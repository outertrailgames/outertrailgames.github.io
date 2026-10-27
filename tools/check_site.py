"""Optional static checks: python tools/check_site.py (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links = path, set(), []
        self.h1 = self.main = self.title = 0
        self.meta, self.canonical = set(), False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        assert tag != "script", f"{self.path}: unexpected script"
        assert not any(k.startswith("on") for k in a), f"{self.path}: inline handler"
        if "id" in a:
            assert a["id"] not in self.ids, f"{self.path}: duplicate id"
            self.ids.add(a["id"])
        if tag == "h1": self.h1 += 1
        if tag == "main": self.main += 1
        if tag == "title": self.title += 1
        if tag == "meta": self.meta.add(a.get("name", ""))
        if tag == "link" and a.get("rel") == "canonical": self.canonical = True
        if tag == "html": assert a.get("lang") == "en"
        if tag == "img":
            assert all(k in a for k in ("alt", "width", "height")), f"{self.path}: image metadata missing"
        for key in ("href", "src"):
            if key in a: self.links.append(a[key])

pages = {}
for path in ROOT.rglob("*.html"):
    p = Page(path)
    p.feed(path.read_text(encoding="utf-8"))
    assert p.h1 == p.main == p.title == 1, f"{path}: landmarks/title"
    assert {"description", "viewport"} <= p.meta and p.canonical, f"{path}: metadata"
    pages[path.resolve()] = p
count = 0
for path, p in pages.items():
    for link in p.links:
        u = urlsplit(link)
        if u.scheme or u.netloc: continue
        target = (ROOT / unquote(u.path).lstrip("/")) if u.path.startswith("/") else path.parent / unquote(u.path)
        if not u.path: target = path
        if target.is_dir(): target /= "index.html"
        target = target.resolve()
        assert target.is_relative_to(ROOT), f"{path}: link escapes site"
        assert target.is_file(), f"{path}: missing {link}"
        if u.fragment:
            assert target in pages and unquote(u.fragment) in pages[target].ids, f"{path}: missing fragment {link}"
        count += 1
print(f"PASS: {len(pages)} HTML pages, {count} internal references; metadata, landmarks, images, and no-script checks.")
