import re, glob, os, subprocess
from html.parser import HTMLParser

void_elements = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in void_elements:
            self.stack.append(tag)
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        if tag in void_elements:
            return
        if not self.stack:
            self.errors.append(f"extra closing tag {tag}")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.errors.append(f"unclosed tag {self.stack.pop()}")
                if self.stack:
                    self.stack.pop()
            else:
                self.errors.append(f"mismatched closing tag {tag}, stack top {self.stack[-1] if self.stack else None}")

all_ok = True
files = sorted(glob.glob("*.html"))
for f in files:
    content = open(f, encoding="utf-8").read()
    c = Checker()
    c.feed(content)
    if c.stack:
        print(f"[{f}] UNCLOSED TAGS AT EOF: {c.stack}")
        all_ok = False
    if c.errors:
        print(f"[{f}] TAG ERRORS: {c.errors}")
        all_ok = False

    # CSS brace balance
    for style_match in re.finditer(r'<style[^>]*>(.*?)</style>', content, re.S):
        css = style_match.group(1)
        if css.count('{') != css.count('}'):
            print(f"[{f}] CSS BRACE MISMATCH: {css.count('{')} open vs {css.count('}')} close")
            all_ok = False

    # JS syntax check (needs Node.js; skipped automatically if not installed)
    for i, script_match in enumerate(re.finditer(r'<script[^>]*>(.*?)</script>', content, re.S)):
        js = script_match.group(1).strip()
        if not js or 'src=' in script_match.group(0)[:30]:
            continue
        path = f"/tmp/check_{f.replace('.html','')}_{i}.js"
        try:
            open(path, "w").write(js)
            r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
            if r.returncode != 0:
                print(f"[{f}] JS SYNTAX ERROR script#{i}: {r.stderr.strip()}")
                all_ok = False
        except FileNotFoundError:
            pass  # node not installed, skip JS syntax check

    # href checks
    for href in re.findall(r'href="([^"]+)"', content):
        if href.startswith(("http","mailto:","#","tel:","data:")):
            continue
        href_clean = href.split("#")[0]
        if href_clean and not os.path.exists(href_clean):
            print(f"[{f}] BROKEN HREF: {href}")
            all_ok = False

    # img src checks
    for src in re.findall(r'src="([^"]+)"', content):
        if src.startswith(("http","data:")):
            continue
        if not os.path.exists(src):
            print(f"[{f}] BROKEN IMG SRC: {src}")
            all_ok = False

print("ALL OK" if all_ok else "FAILURES FOUND")
