# CLAUDE.md – Website Heinz Personnel Solutions

Diese Datei liest Claude (Claude Code und Cowork) bei jeder Arbeit an diesem Repo zuerst.
Sie ist die verbindliche Arbeitsgrundlage. Bei Widersprüchen gilt: Anweisung von Ivo im Chat > diese Datei > alles andere.

## 1. Projekt in Kürze

- Website: https://pflegekraftvermittlung.com (GitHub Pages, Domain über `CNAME`). **Hauptadresse ist OHNE www**:
  www leitet auf die Adresse ohne www weiter. Canonical, hreflang, Sitemap, og:url und JSON-LD daher immer
  `https://pflegekraftvermittlung.com/...`, nie mit www (sonst meldet Google "Seite mit Weiterleitung").
  `wechsel.html` ist bewusst `noindex` und steht deshalb nicht in der Sitemap.
- Inhaber / Ansprechpartner: Ivo Straßenburg (Geschäftsführung), nicht technisch, braucht klare Schritt-für-Schritt-Anleitungen
- Technik: statisches HTML, kein Build-Schritt. Jede Seite ist eine eigenständige Datei mit eigenem `<style>`-Block im `<head>`. Kein externes Stylesheet, kein Framework.
- Alles, was auf `main` gepusht wird, geht automatisch live.

## 2. Arbeitsweise (wer macht was)

1. **Konzept, Texte, Recherche:** Ivo stimmt Änderungen mit Claude in Cowork ab.
2. **Umsetzung:** Cowork bearbeitet die Dateien direkt in diesem lokalen Ordner
   (`~/Documents/GitHub/Homepage`) und führt die Pflicht-Checks aus Abschnitt 6 aus.
3. **Veröffentlichen:** Ivo öffnet GitHub Desktop, prüft die geänderten Dateien, schreibt eine kurze
   Beschreibung, klickt **Commit to main** und dann **Push origin**.
4. **Kleine Änderungen über Claude Code im Browser** sind möglich. Danach muss Ivo in GitHub Desktop
   **Fetch origin / Pull** klicken, bevor Cowork wieder lokal arbeitet. Sonst entstehen Konflikte.

Hinweis für Cowork: Im Sandbox-Container **keine git-Befehle** ausführen (auch nicht `git status`).
Die Sandbox kann `.git/index.lock` anlegen, aber nicht löschen, das blockiert GitHub Desktop.
Für Vergleiche `diff` verwenden. Commit und Push macht immer Ivo.

## 3. Markenregeln (verbindlich, keine Ausnahmen)

- **Keine Gedankenstriche:** weder `—` noch `–`, nirgends. Satz neu bauen (Punkt, Komma, Doppelpunkt),
  Zahlenspannen mit "bis" ("3 bis 6 Monate"), Titel-Trenner `|`.
- **Firmenname im Text immer "Heinz"**, niemals "HPS". Juristisch voll: "Heinz Personnel Solutions GmbH".
- **Sie-Anrede** auf Deutsch. Ton: ehrlich, menschlich, anpackend, direkt, warm. Kein Agentur-Deutsch,
  keine Buzzwords (ganzheitlich, auf Augenhöhe, maßgeschneidert, Synergien), keine Kampf-Rhetorik.
- **Positive Direktaussagen statt Verneinung.** Kontrastformel "Kein X. Nur Y." höchstens 1 bis 2 Mal pro Seite.
- **Beweis statt Behauptung:** Jede Qualitätsaussage braucht Zahl, Siegel oder konkreten Prozessschritt.
  Fehlende Fakten nie erfinden, sondern Ivo fragen.
- **CTA-Texte:** "Rufen Sie durch." (eher Arbeitgeber) und "Kennenlernen." (eher Fachkräfte/allgemein).
  Englisch: "Call us directly." / "Let's talk.". "Sprechen wir." nicht mehr verwenden.
- **"Digital"** nie als alleinstehendes Wort, immer mit Nutzen (Tempo, Transparenz).
- Buttons nie in derselben Farbe wie ihr Hintergrund. Kein Flieder-Ton.
- **Nebeneinanderliegende Blöcke schließen immer bündig ab** (gleiche Höhe, gleiche Ober- und Unterkante).
  Bei Grids `align-items:stretch`, nie `start`. Gleich gemeinte Buttons haben gleiche Größe und Abmaße.
- **Neben breiten CTA-Buttons stehen NIEMALS Textlinks.** Zusätzliche Links (z. B. "Passt die Pflege zu mir?",
  "So läuft es ab") gehören immer in eine eigene Zeile darunter (`.hero-paths`), nie in dieselbe Zeile wie der Button
  (`.hero-actions`, `.cta-actions`, `.cta-row` enthalten nur Buttons).
- **Ruhige Typografie, wenig Wechsel:** Anton in Großbuchstaben nur für Überschriften. Alles andere Inter:
  Fließtext normal, Buttons und Formular-Beschriftungen halbfett, in normaler Schreibweise (keine Großbuchstaben,
  kein Sperrsatz). Über einer Kasten-Überschrift keine zusätzliche kleine Großbuchstaben-Zeile, die dasselbe sagt.
  Links im Text normal unterstrichen, nicht fett.
- **Niemals Schwarz auf Blau**, auch nicht im Hover-Zustand: keine schwarze Schrift, kein schwarzer Rahmen und
  kein schwarzer Button auf blauen Flächen. Auf Blau gilt: weißer Button mit dunkelblauer Schrift, Hover
  transparent mit weißer Schrift und weißem Rahmen (oder umgekehrt). Bei jeder Änderung auch `:hover` prüfen.

## 4. Feste Fakten (nur diese Zahlen verwenden)

- Heinz Personnel Solutions GmbH, Am Eichenhain 32, 13465 Berlin · info@hpstalent.de
- Geschäftsführung: Ivo Straßenburg · Team: Sören Heinz (Key Account & Vertrieb), Tabeia Antonio (Integrationsmanagerin), Tanja Grabow (Fachkräftebetreuung)
- 30 Jahre Erfahrung im Gesundheitswesen, seit 2018 internationale Vermittlung
- 400+ vermittelte Pflegefachkräfte · 92 % bleiben länger als 3 Jahre · 98 % erfolgreiche Berufsanerkennungen
- RAL-Gütezeichen "Faire Anwerbung Pflege" (vergeben durch GAPA) · Mitglied im bvifg
- Garantie: 18 Monate (neue Suche ohne Zusatzkosten bei Eigenkündigung) · Zahlung 50/50 (nach Vermittlung / nach Start)
- Triple-Win, Employer-pays-Prinzip: Fachkräfte und Auszubildende zahlen nichts, keine Rückzahlungsklauseln
- Fachkräfte überwiegend aus den Philippinen und Indien
- **Auszubildende** in vielen Ausbildungsberufen, auf der Seite immer nur als Beispiele genannt: Pflege, Handwerk
  (z. B. Zimmerei), Logistik. Andere Berufe nie ausschließen. aus Asien, Deutsch B2, Wohnungssuche bei Bedarf,
  ca. 3 bis 6 Monate von Auswahl bis Ausbildungsstart, gleiche Garantie und Konditionen.
  Für Bewerber:innen empfiehlt Heinz 12 Jahre Schule (Empfehlung, keine Pflicht; gesetzlich gilt für die Pflege
  10 Jahre Schule nach § 11 PflBG, für duale Ausbildungen entscheidet der Betrieb). Deutschkurs bis B2 organisiert Heinz, kostenfrei.
  Wichtig: Das RAL-Siegel gilt für die Anwerbung von Pflegefachkräften. Für Azubis nur "Dieselben Grundsätze gelten
  bei uns auch für die Vermittlung von Auszubildenden", nie eine RAL-Zertifizierung der Azubi-Vermittlung behaupten.
  Die 92 % gelten für Fachkräfte, nicht auf Azubis übertragen.
- Kunden (Auswahl): Sana Kliniken, Diakonie, Helios, AWO, DRK, Main-Kinzig-Kliniken
- Partner: Lingoda, Ankaadia, Akademie der Gesundheit Berlin/Brandenburg, GAPA

## 5. Aufbau der Website

- **Sprachpaare:** Jede Seite gibt es auf Deutsch (`seite.html`) und Englisch (`seite-en.html`).
  Ausnahmen (nur DE): `wechsel.html`, `pflegefachkraefte-berlin-brandenburg.html`.
  Inhaltliche Änderungen immer in **beiden** Sprachen.
- **Hauptseiten:** `index`, `fuer-einrichtungen` (Für Arbeitgeber), `ausbildung` (Ausbildung für Betriebe),
  `fuer-fachkraefte`, `ueber-uns`, `blog` + `blog-post-1` bis `blog-post-10`, `faq`, `downloads`, `presse`,
  `kontakt`, `impressum`, `datenschutz`, `beschwerdeformular`.
- **Navigation** steht in **jeder** HTML-Datei dreimal: `.nav-links` (Desktop), `.mobile-nav` und im Footer.
  Footer (5 Spalten, gleiche Gliederung wie oben): Logo + Kontakt · Arbeitgeber · Zukunftskräfte (inkl. "Stelle wechseln")
  · Heinz (Über uns, Hintergründe, FAQ, Downloads, Presse) · Rechtliches (inkl. Cookie-Einstellungen).
  Neue Menüpunkte in allen Dateien ergänzen. Aktive Seite bekommt `class="is-active"`.
  Oben genau 4 Punkte: **Arbeitgeber ▾** · **Zukunftskräfte ▾** · Team · Hintergründe (EN: Employers ▾ · Talent ▾ · Team · Insights).
  Beide sind Aufklappmenüs `.nav-drop` mit je "Pflegefachkräfte" und "Auszubildende":
  Arbeitgeber → `fuer-einrichtungen` / `ausbildung`; Zukunftskräfte (`data-nav="talent"`) → `fuer-fachkraefte` /
  `ausbildung-bewerbung` (Bewerberseite für Auszubildende). Aktueller Unterpunkt `class="is-current"`.
  "Zukunftskräfte" ist das eigene Heinz-Wort für Bewerber:innen (statt "Talente"), nur als Oberbegriff, nie als Unterpunkt.
  Mobil: Gruppen `.mobile-group` mit je zwei `.mobile-sub`-Links. Alles bleibt auf pflegekraftvermittlung.com
  (Entscheidung Ivo, Oktober 2026: keine eigene Domain/Seite für Ausbildung).
- **Bilder** liegen in `images/`. Die Bild- und `.py`-Dateien im Hauptordner sind Altbestand: nicht löschen,
  ohne Ivo zu fragen, aber auch nicht für neue Seiten verwenden.
- **Kopf jeder Seite** (Reihenfolge beibehalten):
  1. `<script src="js/cookie-consent.js"></script>` direkt nach `<head>`
  2. Meta charset/viewport, Content-Security-Policy, google-site-verification
  3. title, description, canonical, hreflang (de/en/x-default), Open Graph, Twitter
  4. Google Fonts (Anton, Inter), `<style>`
  5. JSON-LD: EmploymentAgency (`@id …/#organization`), BreadcrumbList, je nach Seite Article / FAQPage / Service
- **Einwilligungsbanner** (`js/cookie-consent.js`): erste Ebene "Alle akzeptieren" und "Nur notwendige Cookies"
  gleich groß und gleich gestaltet, dazu "Einstellungen". Kategorien: Notwendig (nur die Auswahl selbst in localStorage
  `heinz_consent`, 12 Monate), Statistik (Google Analytics 4, Mess-ID G-PB43PKLVEL, ohne Google Signals) und
  Marketing (Google Ads Conversion-Tracking). Checkboxen nie vorausgewählt. Neue Zwecke = `VERSION` erhöhen (erneute Abfrage).
  Google Consent Mode v2 Basis-Modus, `ad_personalization` immer `denied` (kein Remarketing).
  "Cookie-Einstellungen" im Footer jeder Seite (`data-cookie-settings`) und als Button unten links.
  Banner-Text und Datenschutzerklärung Ziffer 6 müssen immer zusammenpassen.
- **Google Ads (AW-18457911738) und Google Analytics (G-PB43PKLVEL)** werden ausschließlich über `js/cookie-consent.js` nach Einwilligung geladen.
  Das Google-Tag nie direkt in eine Seite einbauen. Neue externe Skripte brauchen eine CSP-Anpassung und
  eine Prüfung, ob die Datenschutzerklärung sie abdeckt.
- **Telefon:** Nummer nur auf `fuer-einrichtungen`, `ausbildung`, `pflegefachkraefte-berlin-brandenburg` und `kontakt`
  (jeweils DE/EN), nie in Header, Footer, Fachkräfte-Seiten, Blog, JSON-LD oder `llms.txt`. Sie steht nie im Klartext im Code:
  Baustein `.phone-box` mit Button `data-phone-reveal`, die Nummer liegt verschlüsselt in `js/phone.js` (Liste `D`).
  Auf der Website steht die Telekom-030-Festnetznummer (dauerhaft). Das Umleitungsziel wird bei der Telekom geändert,
  nicht auf der Website. Nummer ändern: nur `js/phone.js` neu verschlüsseln.
  Telefonzeiten auf der Seite: Mo bis Fr, 9 bis 17 Uhr.
- **Formulare:** Formspree. Kontakt `xwvgzjkz`, Beschwerde `xqerjoee`.
- **Bewerbung Fachkräfte:** Ankaadia-Link auf `fuer-fachkraefte.html`.
- **Neue Seite?** Dann zusätzlich: Eintrag in `sitemap.xml` (mit hreflang), Eintrag in `llms.txt`,
  Menü/Footer-Links prüfen, Blogkarte in `blog.html`/`blog-en.html` bei Artikeln.

## 6. Pflicht-Checks vor jedem Push

```bash
# 1. HTML parsebar
python3 -c "import glob,lxml.html as l; [l.fromstring(open(f,encoding='utf-8').read()) for f in glob.glob('*.html')]; print('HTML ok')"
# 2. Sitemap gültig
python3 -c "import lxml.etree as e; e.parse('sitemap.xml'); print('Sitemap ok')"
# 3. Keine Gedankenstriche, kein HPS im sichtbaren Text
grep -l -- "—\|–" *.html llms.txt || echo "Keine Gedankenstriche"
python3 -c "import glob,re; print([f for f in glob.glob('*.html') if re.search(r'\bHPS\b', re.sub(r'<[^>]+>','',open(f,encoding='utf-8').read()))] or 'Kein HPS')"
# 4. Jede DE-Seite hat ihr EN-Gegenstück (außer den DE-only-Seiten)
```

Zusätzlich: geänderte Seiten am Handy und am Desktop ansehen, Umlaute korrekt (ä ö ü ß, nie ae/oe/ue).

## 7. Offene Punkte

- Bewerberseite `ausbildung-bewerbung(-en).html`: "Jetzt bewerben" geht vorläufig per E-Mail an recruiting@hpstalent.de.
  Sobald das Ankaadia-Formular für Auszubildende steht, beide Buttons (Hero und Abschluss, DE/EN) auf den neuen Link umstellen.
  Der Entscheidungskompass (nur Pflege) liegt jetzt dort; auf `fuer-fachkraefte` steht nur noch ein Hinweis mit Link.
- Wert "Lebensunterhalt 1.048 € brutto" (Visum § 16a, Stand Juni 2026) auf `ausbildung(-en).html` jährlich prüfen.
- Wohnraum-Absatz auf `pflegefachkraefte-berlin-brandenburg.html` noch allgemein gehalten.
- Google Fonts werden noch von Google-Servern geladen (ohne Einwilligung, IP-Übermittlung). Empfehlung: Schriften
  Anton und Inter lokal in `fonts/` hosten, dann CSP und Datenschutzerklärung Ziffer 7 anpassen.
- Datenschutzerklärung Ziffer 7 nennt Dienste, die aktuell nicht eingebunden sind (Google Analytics, Maps, HubSpot,
  Vimeo, Social-Plugins). Mit Datenschutzberatung prüfen und bereinigen.
