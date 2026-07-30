# HPS Website – Build-System

Diese Website besteht aus fertigen HTML-Dateien im Hauptverzeichnis (`index.html`,
`fuer-einrichtungen.html`, `index-en.html`, ...) plus den Python-Skripten, die
diese HTML-Dateien erzeugen. **Die HTML-Dateien werden nie von Hand bearbeitet**,
sondern immer über die `.py`-Dateien neu generiert.

## Aufbau

- `gen.py` – gemeinsame Basis: CSS, Header, Footer, SEO-Tags (Deutsch + Englisch)
- `pages.py`, `pages2.py`, `pages3.py`, `pages4.py`, `pages6.py`, `pages7.py` – deutsche Seiten
- `pages_en.py`, `pages2_en.py`, `pages3_en.py`, `pages4_en.py`, `pages6_en.py`, `pages7_en.py` – englische Seiten (Dateiname jeweils mit `-en` Endung)
- `build.py` – **immer dieses Skript nutzen**, um wirklich ALLE Seiten neu zu schreiben
- `validate.py` – prüft danach automatisch auf kaputte Links, kaputtes HTML/CSS/JS

## Änderungen vornehmen (z.B. mit Claude Code)

1. Die passende `.py`-Datei öffnen und den Text/Code darin ändern.
2. `python3 build.py` ausführen (regeneriert alle HTML-Dateien neu).
3. `python3 validate.py` ausführen, muss "ALL OK" ausgeben.
4. Änderungen committen und auf `main` pushen.

## Wichtige Regeln (Markenstimme)

- Sie-Anrede auf Deutsch, professioneller Ton auf Englisch
- Keine Gedankenstriche (—) in normalem Fließtext
- Keine Pfeile in Buttons
- Zahlen/Fakten nicht erfinden, im Zweifel nachfragen

## Zweisprachigkeit

Jede deutsche Seite `X.html` hat ein englisches Gegenstück `X-en.html` im selben
Verzeichnis. Der Sprachumschalter oben rechts im Header verlinkt automatisch
zur jeweils passenden Version, das ist in `gen.py` (Funktion `header()`)
implementiert und muss bei neuen Seiten nicht manuell gepflegt werden.
