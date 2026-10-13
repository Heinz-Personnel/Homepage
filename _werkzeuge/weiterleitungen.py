#!/usr/bin/env python3
"""Weiterleitungsseiten für alte WordPress-Adressen (GitHub Pages kann keine echten 301).

1. Zuordnung in _werkzeuge/weiterleitungen.csv eintragen, eine Zeile pro alte Adresse:
       /alte-adresse/;fuer-einrichtungen.html
   (Zeilen mit # werden ignoriert.)
2. Im Repo-Ordner ausführen:  python3 _werkzeuge/weiterleitungen.py          (zeigt nur an)
                              python3 _werkzeuge/weiterleitungen.py --anlegen (legt Dateien an)

Für jede alte Adresse entsteht eine kleine Seite mit meta refresh (0 Sekunden),
canonical auf die neue Adresse, noindex und sichtbarem Link. Bestehende Dateien
werden nie überschrieben. Die Seiten kommen nicht in die Sitemap.
"""
import os, sys, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BASE = 'https://pflegekraftvermittlung.com/'
CSV = os.path.join(ROOT, '_werkzeuge', 'weiterleitungen.csv')

TPL = '''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<title>Umgezogen | Heinz</title>
</head>
<body>
<p>Diese Seite ist umgezogen: <a href="{url}">{label}</a></p>
</body>
</html>
'''


def target_file(old):
    p = old.strip()
    if p.startswith('http'):
        p = '/' + p.split('/', 3)[3] if p.count('/') >= 3 else '/'
    p = p.split('?')[0].split('#')[0].lstrip('/')
    if not p:
        return None
    if p.endswith('.html'):
        return p
    return p.rstrip('/') + '/index.html'


def main():
    create = '--anlegen' in sys.argv
    if not os.path.exists(CSV):
        print('Keine Datei', CSV)
        return
    rows = []
    for line in open(CSV, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        old, new = [x.strip() for x in line.split(';', 1)]
        rows.append((old, new))
    for old, new in rows:
        f = target_file(old)
        url = new if new.startswith('http') else BASE + new.lstrip('/')
        if new.strip('/') in ('', 'index.html'):
            url = BASE
        if not f:
            print('übersprungen (Startseite):', old)
            continue
        path = os.path.join(ROOT, f)
        status = 'existiert schon, bleibt' if os.path.exists(path) else ('angelegt' if create else 'würde angelegt')
        print('%-45s -> %-50s %s' % (old, url, status))
        if create and not os.path.exists(path):
            os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
            open(path, 'w', encoding='utf-8').write(TPL.format(url=html.escape(url), label=html.escape(url)))


if __name__ == '__main__':
    main()
