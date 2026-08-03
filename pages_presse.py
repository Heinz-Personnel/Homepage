#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# ============================================================ PRESSE ====
presse_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Presse</div>
    <span class="eyebrow">Presse &amp; Medienkontakt</span>
    <h1 class="reveal in">Alles, was Sie für Ihre Berichterstattung brauchen.</h1>
    <p class="lead reveal in">Logos, Pressefoto, Kernzahlen und Unternehmensbeschreibung von Heinz Personnel Solutions, zum direkten Download.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Unternehmen in Kürze</h2></div>
    <div class="reveal" style="max-width:760px;display:flex;flex-direction:column;gap:20px;">
      <div class="win-card" style="background:var(--bg);">
        <h3>Ein Satz</h3>
        <p>Heinz Personnel Solutions vermittelt seit 2018 internationale Pflegefachkräfte fair, transparent und nachhaltig an deutsche Kliniken und Pflegeeinrichtungen.</p>
      </div>
      <div class="win-card" style="background:var(--bg);">
        <h3>Kurzfassung</h3>
        <p>Heinz Personnel Solutions GmbH (HPS) vermittelt seit 2018 internationale Pflegefachkräfte, vor allem aus den Philippinen und Indien, an deutsche Kliniken und Pflegeeinrichtungen. Über 400 Fachkräfte wurden bereits erfolgreich vermittelt, 92 % bleiben länger als drei Jahre. HPS trägt das RAL-Gütezeichen „Faire Anwerbung Pflege Deutschland“ und ist Mitglied im Bundesverband Internationale Fachkräftegewinnung (bvifg).</p>
      </div>
      <div class="win-card" style="background:var(--bg);">
        <h3>Ausführlich</h3>
        <p>Heinz Personnel Solutions GmbH (HPS) mit Sitz in Berlin vermittelt seit 2018 internationale Pflegefachkräfte, vor allem aus den Philippinen und Indien, an deutsche Kliniken und Pflegeeinrichtungen. Im Mittelpunkt steht nicht die einzelne Vermittlung, sondern die nachhaltige Integration: 92 % der über 400 bislang vermittelten Fachkräfte bleiben länger als drei Jahre in ihrer Einrichtung. HPS trägt das RAL-Gütezeichen „Faire Anwerbung Pflege Deutschland“ und ist Mitglied im Bundesverband Internationale Fachkräftegewinnung (bvifg). Das Unternehmen arbeitet nach dem Prinzip des Triple-Win: faire Konditionen für Einrichtung, Fachkraft und Vermittler, ohne versteckte Kosten und ohne Rückzahlungsmodelle für die Fachkräfte. Geschäftsführer ist Ivo Straßenburg.</p>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap bento bento-duo">
    <div class="bento-cell big reveal">
      <div class="stat-num" data-count="92" data-suffix="%">0%</div>
      <div class="stat-label">unserer vermittelten Fachkräfte bleiben länger als drei Jahre</div>
    </div>
    <div class="bento-cell reveal" style="transition-delay:0.1s">
      <div class="stat-num" data-count="400" data-suffix="+">0+</div>
      <div class="stat-label">internationale Pflegefachkräfte erfolgreich vermittelt</div>
    </div>
    <div class="bento-cell quote reveal" style="transition-delay:0.18s;grid-column:span 1;">
      <p>Aktiv seit 2018. RAL-zertifiziert. Mitglied im bvifg.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Zertifizierungen</h2></div>
    <div class="net-grid">
      <a class="net-item reveal" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-ral-guetezeichen.svg" alt="RAL-Gütezeichen" loading="lazy" decoding="async"></div><div><h3>RAL-Gütezeichen</h3><p>„Faire Anwerbung Pflege Deutschland“, vergeben von der GAPA-Gütegemeinschaft, unabhängig geprüft.</p></div></a>
      <a class="net-item reveal" style="transition-delay:0.06s" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-bvifg.png" alt="bvifg" loading="lazy" decoding="async"></div><div><h3>bvifg</h3><p>Mitglied im Bundesverband Internationale Fachkräftegewinnung, gemeinsame Standards für faire Fachkräftemigration.</p></div></a>
      <a class="net-item reveal" style="transition-delay:0.12s" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-gapa.png" alt="GAPA" loading="lazy" decoding="async"></div><div><h3>GAPA</h3><p>Gütegemeinschaft zur Anwerbung und Vermittlung von Pflegekräften aus dem Ausland, vergibt das RAL-Siegel.</p></div></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2 style="font-size:22px;margin-bottom:18px;">Pressefoto</h2>
      <div class="story-photo" style="height:auto;max-width:280px;">
        <img src="presse-foto-ivo-web.jpg" alt="Ivo Straßenburg, Geschäftsführer Heinz Personnel Solutions" loading="lazy" decoding="async">
      </div>
      <p style="font-size:13px;color:var(--ink-mute);margin-top:10px;max-width:280px;">Ivo Straßenburg, Geschäftsführer Heinz Personnel Solutions GmbH.</p>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:18px;">Downloads</h2>
      <div class="resource-links" style="grid-template-columns:1fr;">
        <a class="resource-link" href="presse-foto-ivo-hires.jpg" download><div class="rtitle">Pressefoto Ivo Straßenburg</div><div class="rdesc">Hochauflösend, JPG, für Druck und Web.</div></a>
        <a class="resource-link" href="logo-hps.svg" download><div class="rtitle">Firmenlogo (SVG)</div><div class="rdesc">Vektorformat, verlustfrei skalierbar.</div></a>
        <a class="resource-link" href="logo-hps.png" download><div class="rtitle">Firmenlogo (PNG)</div><div class="rdesc">Rasterformat mit transparentem Hintergrund.</div></a>
      </div>
      <p style="font-size:13px;color:var(--ink-mute);margin-top:14px;">Weitere Fotos vom Team und aus unserer Arbeit finden Sie auf <a href="ueber-uns.html" style="color:var(--green-dark);font-weight:600;">Über uns</a>, weitere Auflösungen auf Anfrage.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap split">
    <div class="reveal">
      <div class="story-photo" style="height:auto;max-width:220px;">
        <img src="blog-carekonkret-clipping.jpg" alt="care konkret, Interview mit Ivo Straßenburg" loading="lazy" decoding="async">
      </div>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:12px;">Presseerwähnung</h2>
      <p style="margin:0 0 6px;font-weight:600;color:var(--ink);">„Damit internationale Pflegekräfte bleiben“</p>
      <p style="font-size:14px;color:var(--ink-mute);margin:0 0 14px;">care konkret, Ausgabe 28/29, 10. Juli 2026. Interview: Ilgin Seren Evisen, Marketing &amp; Business Development Manager, Ankaadia GmbH.</p>
      <a href="blog-post-4.html" class="btn btn-ghost btn-sm">Interview lesen</a>
      <a href="blog-carekonkret-clipping.jpg" download class="btn btn-ghost btn-sm" style="margin-left:10px;">Ausschnitt herunterladen</a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Pressekontakt</h2>
    <p>Heinz Personnel Solutions GmbH<br>Ivo Straßenburg, Geschäftsführung<br><a href="mailto:presse@hpstalent.de" style="color:var(--green-dark);font-weight:600;">presse@hpstalent.de</a></p>
    <p style="margin-top:16px;font-size:14px;">
      <a href="https://www.linkedin.com/in/ivo-stra%C3%9Fenburg-725069a6" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">Ivo Straßenburg auf LinkedIn</a>
      &nbsp;·&nbsp;
      <a href="https://www.linkedin.com/company/heinz-personnel-solutions-gmbh/" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">HPS auf LinkedIn</a>
    </p>
  </div>
</section>
'''
page("presse.html", "Presse & Medienkontakt — Heinz Personnel Solutions", "index.html", presse_body, description="Presse-Kit von Heinz Personnel Solutions: Logos, Pressefoto, Kernzahlen und Unternehmensbeschreibung zum Download, Pressekontakt und Presseerwähnungen.")

print("presse done")
