#!/usr/bin/env python3
"""Dependency-free checks for the static Too Many Bones Solo Academy site."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "index.html", "getting-started.html", "rules.html", "gearlocs.html",
    "tyrants.html", "expansions.html", "solo-strategy.html", "research.html",
    "assets/style.css", "assets/site.js",
]

class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.has_nav = False
        self.has_footer = False
        self.has_css = False
        self.has_js = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "nav":
            self.has_nav = True
        if tag == "footer":
            self.has_footer = True
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value:
                self.links.append(value)
                if attr == "href" and value.endswith("assets/style.css"):
                    self.has_css = True
                if attr == "src" and value.endswith("assets/site.js"):
                    self.has_js = True

errors = []
for item in REQUIRED:
    path = ROOT / item
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"Missing or empty required file: {item}")

pages = sorted(ROOT.glob("*.html"))
if not pages:
    errors.append("No HTML pages found.")

for page in pages:
    source = page.read_text(encoding="utf-8")
    audit = PageAudit()
    audit.feed(source)
    if not audit.has_nav:
        errors.append(f"{page.name}: missing navigation")
    if not audit.has_footer:
        errors.append(f"{page.name}: missing footer")
    if not audit.has_css:
        errors.append(f"{page.name}: missing local stylesheet reference")
    if not audit.has_js:
        errors.append(f"{page.name}: missing local navigation script reference")

    for raw in audit.links:
        parts = urlsplit(raw)
        if parts.scheme or parts.netloc or raw.startswith("#"):
            continue
        target_text = unquote(parts.path)
        if not target_text:
            continue
        target = (page.parent / target_text).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{page.name}: local link escapes site root: {raw}")
            continue
        if not target.is_file():
            errors.append(f"{page.name}: broken local link: {raw}")
            continue
        if parts.fragment and target.suffix.lower() in {".html", ".htm"}:
            target_source = target.read_text(encoding="utf-8")
            if not re.search(r'\\b(?:id|name)=[\\"\\']' + re.escape(parts.fragment) + r'[\\"\\']', target_source):
                errors.append(f"{page.name}: missing anchor in {target.relative_to(ROOT)}: #{parts.fragment}")

if errors:
    print("Site validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(f"Site validation passed: {len(pages)} HTML pages, required assets present, local links valid.")
