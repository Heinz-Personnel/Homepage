#!/usr/bin/env python3
"""Website-Audit Heinz (nur lesen).
Aufruf im Repo-Ordner:  python3 _werkzeuge/audit.py
Schreibt _werkzeuge/audit-report.md. Ändert keine Website-Dateien.
Der Ordner _werkzeuge wird von GitHub Pages (Jekyll) nicht veröffentlicht."""
import os, re, json, glob, collections
from urllib.parse import urlparse, unquote
import lxml.html as LH
import lxml.etree as LE

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(ROOT)
DOMAIN = 'pflegekraftvermittlung.com'
BASE = 'https://' + DOMAIN + '/'
SKIP_DIRS = {'.git', '_werkzeuge', 'node_modules'}
DE_ONLY = {'wechsel.html', 'pflegefachkraefte-berlin-brandenburg.html'}


def all_html():
    out = []
    for d, dirs, files in os.walk('.'):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith('.')]
        for f in files:
            if f.endswith('.html'):
                out.append(os.path.normpath(os.path.join(d, f)))
    return sorted(out)


def text_of(tree, drop):
    t = LH.fromstring(LH.tostring(tree))
    for b in t.xpath(drop):
        b.drop_tree()
    body = t.find('body')
    return ' '.join((body if body is not None else t).text_content().split())


DROP_VIS = '//script|//style|//noscript|//template'
DROP_MAIN = DROP_VIS + '|//header|//nav|//footer|//*[contains(@class,"mobile-nav")]'


def url_to_file(url):
    path = unquote(urlparse(url).path).lstrip('/')
    return path or 'index.html'


def sitemap():
    try:
        x = LE.parse('sitemap.xml')
    except Exception as e:
        return set(), str(e)
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    return {u.find('s:loc', ns).text.strip() for u in x.getroot().findall('s:url', ns)}, None


# ---------- Seiten einlesen ----------
pages = {}
for f in all_html():
    raw = open(f, encoding='utf-8', errors='replace').read()
    try:
        tree = LH.fromstring(raw)
    except Exception as e:
        pages[f] = {'error': str(e)}
        continue
    meta = lambda n: (tree.xpath('//meta[@name="%s"]/@content' % n) or [None])[0]
    prop = lambda n: (tree.xpath('//meta[@property="%s"]/@content' % n) or [None])[0]
    ld = []
    ld_raw = []
    for s in tree.xpath('//script[@type="application/ld+json"]'):
        try:
            d = json.loads(s.text or '')
            ld_raw.append(d)
            items = d if isinstance(d, list) else (d.get('@graph', [d]) if isinstance(d, dict) else [])
            for it in items:
                tp = it.get('@type') if isinstance(it, dict) else None
                ld.append(('ok', tp if isinstance(tp, str) else ','.join(tp or [])))
        except Exception as e:
            ld.append(('FEHLER', str(e)[:80]))
    pages[f] = dict(
        raw=raw, tree=tree,
        ids=set(tree.xpath('//@id')) | set(tree.xpath('//a/@name')),
        title=(tree.findtext('.//title') or '').strip(),
        desc=meta('description'),
        canonical=(tree.xpath('//link[@rel="canonical"]/@href') or [None])[0],
        hreflang={l.get('hreflang'): l.get('href') for l in tree.xpath('//link[@rel="alternate"][@hreflang]')},
        noindex='noindex' in (meta('robots') or '').lower(),
        refresh=bool(tree.xpath('//meta[translate(@http-equiv,"REFSH","refsh")="refresh"]')),
        og_title=prop('og:title'), og_desc=prop('og:description'), og_image=prop('og:image'),
        tw_title=meta('twitter:title'),
        ld=ld, ld_raw=ld_raw,
        vis=text_of(tree, DROP_VIS), main=text_of(tree, DROP_MAIN),
    )

root_pages = sorted(f for f in pages if os.sep not in f and 'error' not in pages[f])
sub_pages = sorted(f for f in pages if os.sep in f)
locs, sm_err = sitemap()
sm_files = {url_to_file(u) for u in locs}
content_pages = [f for f in root_pages if not pages[f]['refresh']]
indexable = [f for f in content_pages if not pages[f]['noindex']]

R = []
def h(t): R.append('\n## ' + t + '\n')
def li(t): R.append('- ' + t)

R.append('# Audit-Bericht Website Heinz\n')
R.append('Erzeugt von `_werkzeuge/audit.py` (nur lesen). %d HTML-Dateien im Hauptordner '
         '(%d indexierbar, %d noindex, %d Weiterleitungsseiten), %d in Unterordnern.'
         % (len(root_pages), len(indexable), len(content_pages) - len(indexable),
            len(root_pages) - len(content_pages), len(sub_pages)))
for f in pages:
    if 'error' in pages[f]:
        li('**Nicht lesbar:** %s (%s)' % (f, pages[f]['error']))

# ---------- Hosting ----------
h('Hosting')
for name in ['CNAME', 'netlify.toml', '_redirects', '_headers', 'vercel.json', '404.html', '.nojekyll', '_config.yml']:
    if os.path.exists(name):
        extra = ' (' + open(name).read().strip() + ')' if name == 'CNAME' else ''
        li('%s: vorhanden%s' % (name, extra))
    else:
        li('%s: fehlt' % name)
wf = glob.glob('.github/workflows/*')
li('.github/workflows: %s' % (', '.join(wf) if wf else 'fehlt'))
if os.path.exists('CNAME') and not any(os.path.exists(x) for x in ['netlify.toml', '_redirects', 'vercel.json']):
    li('**Ergebnis: GitHub Pages.** Echte 301-Weiterleitungen sind dort nicht möglich (nur meta refresh).')
if not os.path.exists('404.html'):
    li('Keine eigene 404-Seite: Besucher alter Adressen sehen die GitHub-Standardseite.')

# ---------- Indexierbarkeit ----------
h('Indexierbarkeit und Sitemap')
if sm_err:
    li('**Sitemap fehlerhaft:** ' + sm_err)
li('Sitemap-URLs: %d · indexierbare Seiten im Hauptordner: %d' % (len(locs), len(indexable)))
if any('://www.' in u for u in locs):
    li('**URLs mit www in der Sitemap**')
for u in sorted(locs):
    if not os.path.exists(url_to_file(u)):
        li('**Sitemap-URL ohne Datei:** ' + u)
for f in root_pages:
    p = pages[f]
    if p['noindex'] and f in sm_files:
        li('**noindex, steht aber in der Sitemap:** ' + f)
    if f in indexable and f not in sm_files:
        li('**Indexierbar, aber nicht in der Sitemap:** ' + f)
    if p['refresh']:
        li('Weiterleitungsseite: %s (noindex: %s, canonical: %s)' % (f, 'ja' if p['noindex'] else '**nein**', p['canonical']))
    if p['noindex'] and not p['refresh']:
        li('noindex: ' + f)
for d, n in collections.Counter(os.path.dirname(f) for f in sub_pages).items():
    ni = sum(1 for f in sub_pages if os.path.dirname(f) == d and pages[f].get('noindex'))
    li('**Unterordner `%s/`: %d HTML-Dateien, davon %d mit noindex.** Wird öffentlich ausgeliefert '
       '(doppelte Inhalte möglich).' % (d, n, ni))

# ---------- Title ----------
h('Title')
for f in content_pages:
    t = pages[f]['title']
    if not t:
        li('**fehlt:** ' + f)
    elif len(t) > 60:
        li('zu lang (%d): %s: "%s"' % (len(t), f, t))
for t, n in collections.Counter(pages[f]['title'] for f in content_pages).items():
    if n > 1 and t:
        li('**Duplikat (%dx):** "%s": %s' % (n, t, ', '.join(f for f in content_pages if pages[f]['title'] == t)))
suf = [f for f in content_pages if 'Heinz Personnel Solutions' in pages[f]['title']]
li('Titel mit "Heinz Personnel Solutions": %d%s' % (len(suf), (' (' + ', '.join(suf) + ')') if suf else ''))

# ---------- Description ----------
h('Meta description')
for f in content_pages:
    d = pages[f]['desc']
    if not d:
        li('**fehlt:** ' + f)
    elif len(d) < 70:
        li('zu kurz (%d): %s' % (len(d), f))
    elif len(d) > 160:
        li('zu lang (%d): %s' % (len(d), f))
for d, n in collections.Counter(pages[f]['desc'] for f in content_pages if pages[f]['desc']).items():
    if n > 1:
        li('**Duplikat (%dx):** %s' % (n, ', '.join(f for f in content_pages if pages[f]['desc'] == d)))

# ---------- Open Graph ----------
h('Open Graph und Twitter')
for f in content_pages:
    p = pages[f]
    miss = [k for k in ('og_title', 'og_desc', 'og_image', 'tw_title') if not p[k]]
    if miss:
        li('%s: fehlt %s' % (f, ', '.join(miss)))
    if p['og_image']:
        img = url_to_file(p['og_image']) if p['og_image'].startswith('http') else p['og_image']
        if not os.path.exists(img):
            li('**og:image-Datei fehlt:** %s (%s)' % (f, p['og_image']))
    if p['og_title'] and p['og_title'].strip() != p['title']:
        li('og:title ≠ title: %s ("%s" / "%s")' % (f, p['og_title'], p['title']))
    if p['og_desc'] and p['desc'] and p['og_desc'].strip() != p['desc'].strip():
        li('og:description ≠ description: %s' % f)

# ---------- Canonical ----------
h('Canonical')
ok = True
for f in content_pages:
    c = pages[f]['canonical']
    expect = [BASE + f] + ([BASE] if f == 'index.html' else [])
    if not c:
        li('**fehlt:** ' + f); ok = False
    elif c not in expect:
        li('weicht ab: %s → %s' % (f, c)); ok = False
if ok:
    li('Alle Canonicals passen zum Dateinamen.')

# ---------- Wortzahl ----------
h('Wortzahl')
R.append('Gezählt: ganzer sichtbarer Text / nur Inhalt ohne Kopf, Navigation und Footer. Aufgeführt sind Seiten unter 300 Wörtern Inhalt.\n')
for f in content_pages:
    nv, nm = len(pages[f]['vis'].split()), len(pages[f]['main'].split())
    if nm < 300:
        li('%s: %d / %d' % (f, nv, nm))
for f in ('index.html', 'ausbildung.html', 'ausbildung-bewerbung.html'):
    if f in pages:
        li('Zur Info %s: %d / %d' % (f, len(pages[f]['vis'].split()), len(pages[f]['main'].split())))

# ---------- Links ----------
h('Interne Links (href, src)')
broken = collections.defaultdict(set)
for f in sorted(pages):
    p = pages[f]
    if 'error' in p:
        continue
    base_dir = os.path.dirname(f)
    refs = [(e, 'href') for e in p['tree'].xpath('//*[@href]')] + [(e, 'src') for e in p['tree'].xpath('//*[@src]')]
    for el, attr in refs:
        if el.tag == 'link' and el.get('rel') in ('preconnect', 'dns-prefetch'):
            continue
        v = (el.get(attr) or '').strip()
        if not v or v.startswith(('mailto:', 'tel:', 'javascript:', 'data:', '//')):
            continue
        if v.startswith('http'):
            u = urlparse(v)
            if u.netloc not in (DOMAIN, 'www.' + DOMAIN):
                continue
            path, frag = url_to_file(v), u.fragment
        else:
            path, _, frag = v.partition('#')
            path = path.split('?')[0]
            if path.startswith('/'):
                path = unquote(path).lstrip('/') or 'index.html'
            else:
                path = os.path.normpath(os.path.join(base_dir, unquote(path))) if path else f
        if path.endswith('/'):
            path += 'index.html'
        if not os.path.exists(path):
            broken[f].add('%s (Datei fehlt)' % v)
            continue
        if frag and path.endswith('.html'):
            tgt = pages.get(os.path.normpath(path))
            if tgt and 'error' not in tgt and frag not in tgt['ids']:
                broken[f].add('%s (Anker fehlt)' % v)
if not broken:
    li('Keine defekten internen Links.')
for f in sorted(broken):
    li('%s: %s' % (f, '; '.join(sorted(broken[f]))))
wl = [f for f in indexable if re.search(r'href="(?:https://pflegekraftvermittlung\.com/)?wechsel\.html', pages[f]['raw'])]
li('Indexierte Seiten mit Link auf wechsel.html (noindex): %d%s' % (len(wl), (' (z. B. ' + ', '.join(wl[:4]) + ')') if wl else ''))

# ---------- Bilder ----------
h('Bilder')
for f in content_pages:
    noalt, emptyalt, nosize, eager = [], [], [], []
    for i, im in enumerate(pages[f]['tree'].xpath('//body//img')):
        src = im.get('src', '')
        alt = im.get('alt')
        if alt is None:
            noalt.append(src)
        elif not alt.strip():
            hidden = im.get('role') == 'presentation' or any(
                a.get('aria-hidden') == 'true' for a in [im] + list(im.iterancestors()))
            if not hidden:
                emptyalt.append(src)
        if not (im.get('width') and im.get('height')):
            nosize.append(src)
        if i > 0 and im.get('loading') != 'lazy':
            eager.append(src)
    if noalt:
        li('**ohne alt:** %s: %s' % (f, ', '.join(noalt)))
    if emptyalt:
        li('leeres alt ohne aria-hidden: %s: %s' % (f, ', '.join(emptyalt)))
    if nosize:
        li('ohne width/height: %s (%d)' % (f, len(nosize)))
    if eager:
        li('ohne loading="lazy" (ab 2. Bild): %s (%d)' % (f, len(eager)))
big = sorted(((os.path.getsize(x), x) for x in glob.glob('images/*') + glob.glob('*.jpg') + glob.glob('*.png')
              if x.lower().endswith(('.jpg', '.jpeg', '.png'))), reverse=True)[:8]
li('Größte Bilddateien: ' + ', '.join('%s (%d KB)' % (x, s // 1024) for s, x in big))
li('WebP-Dateien: %d' % len(glob.glob('images/*.webp')))

# ---------- hreflang ----------
h('hreflang')
ok = True
for f in indexable:
    hl = pages[f]['hreflang']
    if not hl:
        li('**fehlt:** ' + f); ok = False
        continue
    for lang, url in hl.items():
        tf = url_to_file(url)
        if tf not in pages:
            li('%s: hreflang %s zeigt auf fehlende Datei %s' % (f, lang, url)); ok = False
            continue
        if tf == f:
            continue
        back = set(pages[tf].get('hreflang', {}).values())
        if BASE + f not in back and not (f == 'index.html' and BASE in back):
            li('**nicht gegenseitig:** %s → %s (%s)' % (f, tf, lang)); ok = False
    if 'x-default' not in hl:
        li('x-default fehlt: ' + f); ok = False
    if any('://www.' in u for u in hl.values()):
        li('**www in hreflang:** ' + f); ok = False
for f in indexable:
    if not f.endswith('-en.html') and f not in DE_ONLY and not os.path.exists(f[:-5] + '-en.html'):
        li('EN-Gegenstück fehlt: ' + f); ok = False
if ok:
    li('Alle hreflang-Angaben vollständig und gegenseitig.')

# ---------- JSON-LD ----------
h('JSON-LD')
for f in content_pages:
    p = pages[f]
    bad = [x[1] for x in p['ld'] if x[0] != 'ok']
    types = sorted({x[1] for x in p['ld'] if x[0] == 'ok'})
    flag = []
    if 'EmploymentAgency' not in types:
        flag.append('ohne EmploymentAgency')
    if f.startswith('index') and 'WebSite' not in types:
        flag.append('ohne WebSite')
    if bad:
        flag.append('**ungültiges JSON:** ' + '; '.join(bad))
    li('%s: %s%s' % (f, ', '.join(types) or 'kein JSON-LD', (' | ' + ', '.join(flag)) if flag else ''))
    for d in p['ld_raw']:
        if isinstance(d, dict) and d.get('@type') == 'FAQPage':
            vis = {}
            for det in p['tree'].xpath('//details'):
                sm = det.xpath('./summary')
                if sm:
                    ans = ' '.join(' '.join(x.text_content().split()) for x in det.xpath('./*[not(self::summary)]'))
                    vis[' '.join(sm[0].text_content().split())] = ans
            for q in d.get('mainEntity', []):
                n = ' '.join(q.get('name', '').split())
                a = ' '.join(q.get('acceptedAnswer', {}).get('text', '').split())
                if n not in vis:
                    if n in p['vis'] and a in p['vis']:
                        continue  # sichtbar als Absatz statt <details>
                    li('  **FAQ-Schema-Frage nicht wortgleich sichtbar:** "%s"' % n)
                elif vis[n] != a:
                    li('  **FAQ-Antwort weicht ab:** "%s"' % n)
    if f.startswith('ausbildung') and 'hasCredential' in p['raw']:
        li('  **hasCredential im Azubi-Kontext**')

# ---------- Marke ----------
h('HPS und Gedankenstriche (sichtbarer Text, title, description)')
hit = False
for f in sorted(pages):
    p = pages[f]
    if 'error' in p:
        continue
    v = ' '.join([p['vis'], p['title'], p['desc'] or ''])
    probs = []
    if re.search(r'\bHPS\b', v):
        probs.append('HPS')
    for ch, nm in (('—', '—'), ('–', '–')):
        if ch in v:
            probs.append('%s %dx' % (nm, v.count(ch)))
    if probs:
        hit = True
        li('%s: %s' % (f, ', '.join(probs)))
if not hit:
    li('Nichts gefunden.')

# ---------- Gütezeichen ----------
h('Gütezeichen und 92 % im Azubi-Kontext')
AZUBI = [x for x in content_pages if x.startswith(('ausbildung', 'blog-post-11', 'blog-post-12'))]
R.append('Geprüft werden Azubi-Seiten und Azubi-Artikel (Inhalt ohne Kopf und Footer).\n')
for f in AZUBI:
    p = pages[f]
    probs = [w for w in ('RAL', 'Gütezeichen', 'GAPA', '92 %', '92%', 'quality seal', 'quality mark') if w in p['main']]
    probs += [s for s in p['tree'].xpath('//img/@src') if re.search('ral|gapa|guetezeichen', s, re.I)]
    li('%s: %s' % (f, ('**' + ', '.join(probs) + '**') if probs else 'sauber (nur Footer-Link "Beschwerdeverfahren (RAL)")'))
short = [f for f in content_pages if re.search(r'Faire Anwerbung Pflege(?! Deutschland)', pages[f]['raw'])]
if os.path.exists('llms.txt') and re.search(r'Faire Anwerbung Pflege(?! Deutschland)', open('llms.txt', encoding='utf-8').read()):
    short.append('llms.txt')
li('Kurzform "Faire Anwerbung Pflege" ohne "Deutschland": ' + (', '.join(short) if short else 'keine'))
tr = [f for f in content_pages if re.search(r'Fair Recruitment of Nurses|Fair Recruitment Care', pages[f]['raw'])]
li('Übersetzter Siegelname ("Fair Recruitment ..."): ' + (', '.join(tr) if tr else 'keine'))

open('_werkzeuge/audit-report.md', 'w', encoding='utf-8').write('\n'.join(R) + '\n')
print('Bericht: _werkzeuge/audit-report.md')
