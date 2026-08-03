#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# ========================================================= PRESS (EN) ====
presse_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Press</div>
    <span class="eyebrow">Press &amp; Media Contact</span>
    <h1 class="reveal in">Everything you need for your coverage.</h1>
    <p class="lead reveal in">Logos, press photo, key figures and company description of Heinz Personnel Solutions, ready to download.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Company at a glance</h2></div>
    <div class="reveal" style="max-width:760px;display:flex;flex-direction:column;gap:20px;">
      <div class="win-card" style="background:var(--bg);">
        <h3>One line</h3>
        <p>Heinz Personnel Solutions has been placing international nursing professionals with German hospitals and care facilities since 2018, fairly, transparently and sustainably.</p>
      </div>
      <div class="win-card" style="background:var(--bg);">
        <h3>Short version</h3>
        <p>Heinz Personnel Solutions GmbH (HPS) has been placing international nursing professionals, mainly from the Philippines and India, with German hospitals and care facilities since 2018. More than 400 professionals have already been placed successfully, 92% stay longer than three years. HPS holds the RAL quality mark "Faire Anwerbung Pflege Deutschland" (Fair Recruitment in Nursing) and is a member of the Federal Association for International Recruitment of Skilled Workers (bvifg).</p>
      </div>
      <div class="win-card" style="background:var(--bg);">
        <h3>Long version</h3>
        <p>Heinz Personnel Solutions GmbH (HPS), based in Berlin, has been placing international nursing professionals, mainly from the Philippines and India, with German hospitals and care facilities since 2018. The focus is not the individual placement but sustainable integration: 92% of the more than 400 professionals placed so far stay longer than three years at their facility. HPS holds the RAL quality mark "Faire Anwerbung Pflege Deutschland" and is a member of the Federal Association for International Recruitment of Skilled Workers (bvifg). The company works on a triple-win principle: fair terms for the facility, the professional and the recruiter, with no hidden costs and no repayment schemes for the professionals. The managing director is Ivo Straßenburg.</p>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap bento bento-duo">
    <div class="bento-cell big reveal">
      <div class="stat-num" data-count="92" data-suffix="%">0%</div>
      <div class="stat-label">of our placed professionals stay longer than three years</div>
    </div>
    <div class="bento-cell reveal" style="transition-delay:0.1s">
      <div class="stat-num" data-count="400" data-suffix="+">0+</div>
      <div class="stat-label">international nursing professionals successfully placed</div>
    </div>
    <div class="bento-cell quote reveal" style="transition-delay:0.18s;grid-column:span 1;">
      <p>Active since 2018. RAL-certified. bvifg member.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Certifications</h2></div>
    <div class="net-grid">
      <a class="net-item reveal" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-ral-guetezeichen.svg" alt="RAL quality mark" loading="lazy" decoding="async"></div><div><h3>RAL quality mark</h3><p>"Faire Anwerbung Pflege Deutschland", awarded by the GAPA quality association, independently audited.</p></div></a>
      <a class="net-item reveal" style="transition-delay:0.06s" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-bvifg.png" alt="bvifg" loading="lazy" decoding="async"></div><div><h3>bvifg</h3><p>Member of the Federal Association for International Recruitment of Skilled Workers, shared standards for fair labour migration.</p></div></a>
      <a class="net-item reveal" style="transition-delay:0.12s" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-gapa.png" alt="GAPA" loading="lazy" decoding="async"></div><div><h3>GAPA</h3><p>Quality association for the recruitment and placement of nursing professionals from abroad, awards the RAL seal.</p></div></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2 style="font-size:22px;margin-bottom:18px;">Press photo</h2>
      <div class="story-photo" style="height:auto;max-width:280px;">
        <img src="presse-foto-ivo-web.jpg" alt="Ivo Straßenburg, Managing Director Heinz Personnel Solutions" loading="lazy" decoding="async">
      </div>
      <p style="font-size:13px;color:var(--ink-mute);margin-top:10px;max-width:280px;">Ivo Straßenburg, Managing Director, Heinz Personnel Solutions GmbH.</p>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:18px;">Downloads</h2>
      <div class="resource-links" style="grid-template-columns:1fr;">
        <a class="resource-link" href="presse-foto-ivo-hires.jpg" download><div class="rtitle">Press photo, Ivo Straßenburg</div><div class="rdesc">High resolution, JPG, for print and web.</div></a>
        <a class="resource-link" href="logo-hps.svg" download><div class="rtitle">Company logo (SVG)</div><div class="rdesc">Vector format, scales without loss of quality.</div></a>
        <a class="resource-link" href="logo-hps.png" download><div class="rtitle">Company logo (PNG)</div><div class="rdesc">Raster format with transparent background.</div></a>
      </div>
      <p style="font-size:13px;color:var(--ink-mute);margin-top:14px;">More photos of the team and our work are on <a href="ueber-uns-en.html" style="color:var(--green-dark);font-weight:600;">About Us</a>, further resolutions available on request.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap split">
    <div class="reveal">
      <div class="story-photo" style="height:auto;max-width:220px;">
        <img src="blog-carekonkret-clipping.jpg" alt="care konkret, interview with Ivo Straßenburg" loading="lazy" decoding="async">
      </div>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:12px;">Press mention</h2>
      <p style="margin:0 0 6px;font-weight:600;color:var(--ink);">"Damit internationale Pflegekräfte bleiben" ("So international nursing professionals stay")</p>
      <p style="font-size:14px;color:var(--ink-mute);margin:0 0 14px;">care konkret, issue 28/29, 10 July 2026. Interview: Ilgin Seren Evisen, Marketing &amp; Business Development Manager, Ankaadia GmbH.</p>
      <a href="blog-post-4-en.html" class="btn btn-ghost btn-sm">Read the interview</a>
      <a href="blog-carekonkret-clipping.jpg" download class="btn btn-ghost btn-sm" style="margin-left:10px;">Download clipping</a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Press contact</h2>
    <p>Heinz Personnel Solutions GmbH<br>Ivo Straßenburg, Managing Director<br><a href="mailto:presse@hpstalent.de" style="color:var(--green-dark);font-weight:600;">presse@hpstalent.de</a></p>
    <p style="margin-top:16px;font-size:14px;">
      <a href="https://www.linkedin.com/in/ivo-stra%C3%9Fenburg-725069a6" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">Ivo Straßenburg on LinkedIn</a>
      &nbsp;·&nbsp;
      <a href="https://www.linkedin.com/company/heinz-personnel-solutions-gmbh/" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">HPS on LinkedIn</a>
    </p>
  </div>
</section>
'''
page("presse-en.html", "Press & Media Contact — Heinz Personnel Solutions", "index.html", presse_body_en, description="Press kit of Heinz Personnel Solutions: logos, press photo, key figures and company description to download, press contact and press mentions.")

print("presse-en done")
