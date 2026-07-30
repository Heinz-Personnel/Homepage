#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master build script fuer die HPS-Website.

Regeneriert ALLE HTML-Seiten (Deutsch + Englisch) aus den Python-Quellmodulen
in diesem Ordner. Immer dieses Skript ausfuehren, nicht die einzelnen
pagesN.py-Dateien einzeln, damit garantiert alle Seiten den aktuellen
gen.py-Stand (Header, Footer, CSS, SEO-Tags) verwenden.

Aufruf:
    python3 build.py

Danach zur Sicherheit:
    python3 validate.py
"""
import importlib
import sys

MODULES = [
    "pages",       # index.html
    "pages2",      # fuer-einrichtungen.html, fuer-fachkraefte.html
    "pages3",      # ueber-uns.html, blog.html, blog-post-1.html
    "pages4",      # faq, kontakt, impressum, datenschutz, beschwerdeformular, downloads
    "pages6",      # blog-post-2/3/4.html
    "pages7",      # blog-post-5/6/7.html
    "pages_en",    # index-en.html
    "pages2_en",   # fuer-einrichtungen-en.html, fuer-fachkraefte-en.html
    "pages3_en",   # ueber-uns-en.html, blog-en.html, blog-post-1-en.html
    "pages4_en",   # faq-en, kontakt-en, impressum-en, datenschutz-en, beschwerdeformular-en, downloads-en
    "pages6_en",   # blog-post-2/3/4-en.html
    "pages7_en",   # blog-post-5/6/7-en.html
]

def main():
    failed = []
    for name in MODULES:
        try:
            if name in sys.modules:
                importlib.reload(sys.modules[name])
            else:
                importlib.import_module(name)
        except Exception as e:
            print(f"FEHLER in {name}.py: {e}")
            failed.append(name)
    print()
    if failed:
        print(f"Build mit Fehlern abgeschlossen. Fehlgeschlagen: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("Build erfolgreich abgeschlossen. Alle Seiten wurden neu geschrieben.")

if __name__ == "__main__":
    main()
