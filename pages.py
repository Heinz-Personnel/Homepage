#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# ============================================================ INDEX ====
index_body = '''
<main id="top">

  <section class="hero hero-fullbleed">
    <div class="hero-mosaic-bg" aria-hidden="true">
      <div class="mosaic-rows">
          <div class="mosaic-row dir-a" style="height:96px;">
            <div class="mtile mc1" style="width:96px;height:96px;"></div>
            <div class="mtile mc2" style="width:96px;height:96px;"><img src="foto-hero-willkommen-gruppe.jpg" alt=""></div>
            <div class="mtile mc3" style="width:96px;height:96px;"></div>
            <div class="mtile mc4" style="width:96px;height:96px;"><img src="foto-hero-gartenfest.jpg" alt=""></div>
            <div class="mtile mc1" style="width:96px;height:96px;"><img src="foto-event-ankunft-gruppe.jpg" alt=""></div>
            <div class="mtile mc2" style="width:96px;height:96px;"></div>
            <div class="mtile mc3" style="width:96px;height:96px;"><img src="foto-hero-parkpicknick.jpg" alt=""></div>
            <div class="mtile mc4" style="width:96px;height:96px;"></div>
            <div class="mtile mc1" style="width:96px;height:96px;"></div>
            <div class="mtile mc2" style="width:96px;height:96px;"><img src="foto-hero-willkommen-gruppe.jpg" alt=""></div>
            <div class="mtile mc3" style="width:96px;height:96px;"></div>
            <div class="mtile mc4" style="width:96px;height:96px;"><img src="foto-hero-gartenfest.jpg" alt=""></div>
            <div class="mtile mc1" style="width:96px;height:96px;"><img src="foto-event-ankunft-gruppe.jpg" alt=""></div>
            <div class="mtile mc2" style="width:96px;height:96px;"></div>
            <div class="mtile mc3" style="width:96px;height:96px;"><img src="foto-hero-parkpicknick.jpg" alt=""></div>
            <div class="mtile mc4" style="width:96px;height:96px;"></div>
          </div>
          <div class="mosaic-row dir-b" style="height:86px;">
            <div class="mtile mc2" style="width:86px;height:86px;"><img src="foto-hero-willkommen-solo.jpg" alt=""></div>
            <div class="mtile mc4" style="width:86px;height:86px;"></div>
            <div class="mtile mc1" style="width:86px;height:86px;"><img src="foto-hero-flughafen-checkin.jpg" alt=""></div>
            <div class="mtile mc3" style="width:86px;height:86px;"></div>
            <div class="mtile mc2" style="width:86px;height:86px;"><img src="foto-event-sommerfest.jpg" alt=""></div>
            <div class="mtile mc1" style="width:86px;height:86px;"></div>
            <div class="mtile mc4" style="width:86px;height:86px;"><img src="foto-hero-strasse-gruppe.jpg" alt=""></div>
            <div class="mtile mc3" style="width:86px;height:86px;"></div>
            <div class="mtile mc2" style="width:86px;height:86px;"><img src="foto-hero-willkommen-solo.jpg" alt=""></div>
            <div class="mtile mc4" style="width:86px;height:86px;"></div>
            <div class="mtile mc1" style="width:86px;height:86px;"><img src="foto-hero-flughafen-checkin.jpg" alt=""></div>
            <div class="mtile mc3" style="width:86px;height:86px;"></div>
            <div class="mtile mc2" style="width:86px;height:86px;"><img src="foto-event-sommerfest.jpg" alt=""></div>
            <div class="mtile mc1" style="width:86px;height:86px;"></div>
            <div class="mtile mc4" style="width:86px;height:86px;"><img src="foto-hero-strasse-gruppe.jpg" alt=""></div>
            <div class="mtile mc3" style="width:86px;height:86px;"></div>
          </div>
          <div class="mosaic-row dir-a" style="height:114px;">
            <div class="mtile mc3" style="width:114px;height:114px;"></div>
            <div class="mtile mc1" style="width:114px;height:114px;"><img src="foto-hero-mietwagen-team.jpg" alt=""></div>
            <div class="mtile mc4" style="width:114px;height:114px;"></div>
            <div class="mtile mc2" style="width:114px;height:114px;"><img src="foto-hero-strasse-gruppe.jpg" alt=""></div>
            <div class="mtile mc1" style="width:114px;height:114px;"></div>
            <div class="mtile mc3" style="width:114px;height:114px;"><img src="foto-event-flughafen-selfie.jpg" alt=""></div>
            <div class="mtile mc4" style="width:114px;height:114px;"></div>
            <div class="mtile mc2" style="width:114px;height:114px;"><img src="foto-hero-gartenfest.jpg" alt=""></div>
            <div class="mtile mc3" style="width:114px;height:114px;"></div>
            <div class="mtile mc1" style="width:114px;height:114px;"><img src="foto-hero-mietwagen-team.jpg" alt=""></div>
            <div class="mtile mc4" style="width:114px;height:114px;"></div>
            <div class="mtile mc2" style="width:114px;height:114px;"><img src="foto-hero-strasse-gruppe.jpg" alt=""></div>
            <div class="mtile mc1" style="width:114px;height:114px;"></div>
            <div class="mtile mc3" style="width:114px;height:114px;"><img src="foto-event-flughafen-selfie.jpg" alt=""></div>
            <div class="mtile mc4" style="width:114px;height:114px;"></div>
            <div class="mtile mc2" style="width:114px;height:114px;"><img src="foto-hero-gartenfest.jpg" alt=""></div>
          </div>
          <div class="mosaic-row dir-b" style="height:92px;">
            <div class="mtile mc4" style="width:92px;height:92px;"></div>
            <div class="mtile mc2" style="width:92px;height:92px;"><img src="foto-hero-parkpicknick.jpg" alt=""></div>
            <div class="mtile mc1" style="width:92px;height:92px;"></div>
            <div class="mtile mc3" style="width:92px;height:92px;"><img src="foto-hero-willkommen-gruppe.jpg" alt=""></div>
            <div class="mtile mc4" style="width:92px;height:92px;"><img src="foto-event-sommerfest.jpg" alt=""></div>
            <div class="mtile mc2" style="width:92px;height:92px;"></div>
            <div class="mtile mc1" style="width:92px;height:92px;"><img src="foto-hero-mietwagen-team.jpg" alt=""></div>
            <div class="mtile mc3" style="width:92px;height:92px;"></div>
            <div class="mtile mc4" style="width:92px;height:92px;"></div>
            <div class="mtile mc2" style="width:92px;height:92px;"><img src="foto-hero-parkpicknick.jpg" alt=""></div>
            <div class="mtile mc1" style="width:92px;height:92px;"></div>
            <div class="mtile mc3" style="width:92px;height:92px;"><img src="foto-hero-willkommen-gruppe.jpg" alt=""></div>
            <div class="mtile mc4" style="width:92px;height:92px;"><img src="foto-event-sommerfest.jpg" alt=""></div>
            <div class="mtile mc2" style="width:92px;height:92px;"></div>
            <div class="mtile mc1" style="width:92px;height:92px;"><img src="foto-hero-mietwagen-team.jpg" alt=""></div>
            <div class="mtile mc3" style="width:92px;height:92px;"></div>
          </div>
        </div>
      <div class="hero-scrim"></div>
    </div>
    <div class="hero-glow glow-a" aria-hidden="true"></div>
    <div class="hero-glow glow-b" aria-hidden="true"></div>
    <div class="wrap hero-content-wrap">
      <div class="reveal in hero-content">
        <span class="eyebrow">Internationale Fachkräfte für die Pflege</span>
        <h1>Pflegefachkräfte, die bleiben.</h1>
        <p class="lead">Vermittlung seit 2018. Menschliche Begleitung durch Fachleute. Digitale Prozesse. Fair für alle Seiten. Ohne versteckte Kosten.</p>
        <span class="status-chip"><span class="dot"></span>Digital vernetzt · bundesweit im Einsatz</span>
        <div class="hero-cta-row">
          <div class="hero-cta-group">
            <div class="hero-ctas">
              <a href="kontakt.html" class="btn btn-primary">Unverbindliches Gespräch vereinbaren</a>
            </div>
            <div class="hero-paths">
              <a href="fuer-einrichtungen.html" class="btn btn-ghost btn-sm">Für Arbeitgeber</a>
              <a href="fuer-fachkraefte.html" class="btn btn-ghost btn-sm">Für Fachkräfte</a>
            </div>
          </div>
          <div class="hero-proof-badge"><span class="dot"></span>400+ echte Geschichten</div>
        </div>
      </div>
    </div>
  </section>

  <div class="trustbar">
    <div class="wrap">
      <span class="badge"><img src="logo-ral-guetezeichen.svg" alt="RAL-Gütezeichen Faire Anwerbung Pflege Deutschland" style="height:144px"></span>
      <span class="badge"><img src="logo-bvifg.png" alt="Mitglied im Bundesverband Internationale Fachkräftegewinnung" style="height:104px"></span>
      <span class="badge"><img src="logo-gapa.png" alt="GAPA – Gütegemeinschaft zur Anwerbung und Vermittlung von Pflegekräften aus dem Ausland" style="height:140px"></span>
    </div>
  </div>

  <section>
    <div class="wrap">
      <div class="problem reveal">
        <h2>Der Fachkräftemangel bleibt. Internationale Fachkräfte sind die Lösung.</h2>
        <p>390.000 Pflegefachkräfte gehen laut Bundesagentur für Arbeit in den nächsten zehn Jahren in den Ruhestand. Der deutsche Arbeitsmarkt kann diese Lücke allein nicht schließen. Wir schon: mit Fachkräften aus den Philippinen und Indien, passgenau statt in Masse, mit klarem Fokus auf Integration. Damit sich die Investition Ihrer Einrichtung nachhaltig lohnt.</p>
        <p style="margin-top:14px;"><a href="fuer-einrichtungen.html" class="btn btn-ghost btn-sm">Mehr für Arbeitgeber</a></p>
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
        <p>„Wir stehen zu unserer Integrationsarbeit. Passt es einmal nicht, begleiten wir Sie unkompliziert und ohne zusätzliche Kosten zu einer neuen Fachkraft.“</p>
      </div>
    </div>
  </section>

  <section style="background:var(--bg-soft);">
    <div class="wrap">
      <div class="section-head reveal">
        <h2>Ein beschleunigter Prozess, der planbar ist.</h2>
        <p style="font-size:15.5px;margin-top:10px;">Durchschnittlich 6 Monate bis zum ersten Arbeitstag. Wir haben einen Pool aus mehreren hundert geprüften, sprachlich vorbereiteten Kandidat:innen aufgebaut und können dadurch die Prozesszeit für Ihre Einrichtung deutlich verkürzen.</p>
      </div>
      <div class="process-grid">
        <div class="p-card reveal">
          <div class="step-num">01</div>
          <div class="icn"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M9 4h6a1 1 0 0 1 1 1v1H8V5a1 1 0 0 1 1-1Z"/><path d="M8 6H6a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-2"/></svg></div>
          <div class="step-label">Tag 1</div><h3>Bedarfsanalyse</h3>
          <p>Wir stimmen uns persönlich mit Ihnen ab und klären, wer wirklich zu Ihrer Einrichtung passt.</p>
        </div>
        <div class="p-card reveal" style="transition-delay:0.08s">
          <div class="step-num">02</div>
          <div class="icn"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
          <div class="step-label">Ab Woche 2</div><h3>Matching aus dem Pool</h3>
          <p>Wir schlagen passende Kandidat:innen aus unserem bestehenden, bereits vorqualifizierten Pool vor. Kein Start bei null.</p>
        </div>
        <div class="p-card reveal" style="transition-delay:0.16s">
          <div class="step-num">03</div>
          <div class="icn"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-1 .1-1.3.5l-.7.8c-.4.5-.3 1.2.2 1.5L9 12l-2 3H4l-1 2 3 1 1 3 2-1v-3l3-2 3.2 6.5c.3.5 1 .6 1.5.2l.8-.7c.4-.3.6-.8.5-1.3Z"/></svg></div>
          <div class="step-label">6 Monate</div><h3>Anerkennung & Visum</h3>
          <p>Sprachprozess und Anerkennung laufen für unseren Pool bereits parallel. Das verkürzt Ihre Wartezeit spürbar.</p>
        </div>
        <div class="p-card reveal" style="transition-delay:0.24s">
          <div class="step-num">04</div>
          <div class="icn"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 1 0-7.8 7.8l1 1L12 21.2l7.8-7.8 1-1a5.5 5.5 0 0 0 0-7.8Z"/></svg></div>
          <div class="step-label">Ab Tag 1 im Team</div><h3>Integration & Begleitung</h3>
          <p>Empfang vor Ort und Begleitung, so lange sie gebraucht wird.</p>
        </div>
      </div>
      <div class="process-cta"><a href="fuer-einrichtungen.html#prozess" class="btn btn-ghost btn-sm">Unser Prozess im Detail</a></div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head reveal"><h2>Fair für alle Seiten.</h2></div>
      <div class="win-grid">
        <div class="win-card reveal"><h3>Für Arbeitgeber</h3><p>Planbare, langfristige Besetzung statt wiederkehrender Suche. Ein digital begleiteter Prozess mit klarer Struktur und Ausfallversicherung.</p></div>
        <div class="win-card reveal" style="transition-delay:0.08s"><h3>Für Fachkräfte</h3><p>Die Vermittlung kostet Fachkräfte absolut nichts. Keine Gebühren, keine Rückzahlungsmodelle. Wir arbeiten streng nach dem RAL-Gütezeichen für faire Anwerbung.</p></div>
        <div class="win-card reveal" style="transition-delay:0.16s"><h3>Für die Zusammenarbeit</h3><p>Wir arbeiten nach einem wissenschaftlichen Modell, das sich in der Praxis bewährt hat. Dadurch profitieren alle, und zwar dauerhaft.</p></div>
      </div>
    </div>
  </section>

  <section style="background:var(--bg-soft);">
    <div class="wrap">
      <div class="section-head reveal">
        <h2>Wir arbeiten nicht allein.</h2>
        <p style="font-size:15.5px;margin-top:10px;">Wir sind Teil unterschiedlicher Netzwerke und Partnerschaften und profitieren so von neuesten Entwicklungen und Technologien im Markt.</p>
      </div>
      <div class="net-grid">
        <a class="net-item reveal" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-bvifg.png" alt="bvifg" loading="lazy" decoding="async"></div><div><h3>bvifg</h3><p>Als Mitglied im Bundesverband Internationale Fachkräftegewinnung gestalten wir gemeinsame Standards für faire Fachkräftemigration mit.</p></div></a>
        <a class="net-item reveal" style="transition-delay:0.06s" href="https://ankaadia.com/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-ankaadia.png" alt="Ankaadia" loading="lazy" decoding="async"></div><div><h3>Ankaadia</h3><p>Die SaaS-Plattform, über die wir unseren gesamten Vermittlungsprozess digital und nachvollziehbar abwickeln.</p></div></a>
        <a class="net-item reveal" style="transition-delay:0.12s" href="https://www.lingoda.com/de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-lingoda.png" alt="Lingoda" loading="lazy" decoding="async"></div><div><h3>Lingoda</h3><p>Hochwertiger Online-Sprachunterricht und Anerkennungskurse, der unsere Kandidat*innen von muttersprachlichen Lehrkräften auf Deutsch vorbereitet.</p></div></a>
        <a class="net-item reveal" style="transition-delay:0.18s" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="net-badge net-badge-logo"><img src="logo-gapa.png" alt="GAPA" loading="lazy" decoding="async"></div><div><h3>GAPA</h3><p>Die GAPA vergibt das RAL-Gütezeichen „Faire Anwerbung Pflege Deutschland“ und sichert eine faire, ethische und transparente Anwerbung internationaler Pflegekräfte.</p></div></a>
      </div>
      <div class="clients reveal">
        <p class="lead-sm">Kliniken, Pflegeeinrichtungen und Wohlfahrtsverbände, die mit uns international Fachkräfte gewinnen:</p>
        <div class="marquee"><div class="marquee-track">
          <span class="client-logo"><img src="logo-sana.svg" alt="Sana Kliniken AG" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-diakonie.png" alt="Diakonie" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-helios.png" alt="Helios" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-awo.png" alt="AWO" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-drk.png" alt="Deutsches Rotes Kreuz" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-main-kinzig.png" alt="Main-Kinzig-Kliniken" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-sana.svg" alt="Sana Kliniken AG" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-diakonie.png" alt="Diakonie" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-helios.png" alt="Helios" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-awo.png" alt="AWO" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-drk.png" alt="Deutsches Rotes Kreuz" loading="lazy" decoding="async"></span>
          <span class="client-logo"><img src="logo-main-kinzig.png" alt="Main-Kinzig-Kliniken" loading="lazy" decoding="async"></span>
        </div></div>
      </div>
    </div>
  </section>

  <section id="team">
    <div class="wrap">
      <div class="team-note">
        <h2 style="font-size:28px;margin-bottom:10px;">Das Team hinter dem Service</h2>
        <p style="font-size:15.5px;">Wir sind kein Callcenter und haben keine langen Warte- und Abstimmungswege. Sie sprechen direkt mit den Menschen, die die Vermittlung und Integration auch tatsächlich bearbeiten. <a href="ueber-uns.html" style="color:var(--green-dark);font-weight:600;">Lernen Sie das ganze Team und echte Geschichten kennen</a></p>
      </div>
      <div class="team-grid">
        <div class="team-card reveal"><div class="avatar"><img src="team-ivo.jpg" alt="Ivo Straßenburg" loading="lazy" decoding="async"></div><h3>Ivo Straßenburg</h3><div class="role">Geschäftsführung</div><p class="bio">Verantwortet Strategie und Partnerschaften.</p></div>
        <div class="team-card reveal" style="transition-delay:0.06s"><div class="avatar"><img src="team-soeren.jpg" alt="Sören Heinz" loading="lazy" decoding="async"></div><h3>Sören Heinz</h3><div class="role">Key Account & Vertrieb</div><p class="bio">Erster Kontakt für Arbeitgeber.</p></div>
        <div class="team-card reveal" style="transition-delay:0.12s"><div class="avatar"><img src="team-tabeia.jpg" alt="Tabeia Antonio" loading="lazy" decoding="async"></div><h3>Tabeia Antonio</h3><div class="role">Integrationsmanagerin</div><p class="bio">Verantwortet die Integration unserer Fachkräfte, von der Ankunft bis zum festen Platz im Team.</p></div>
        <div class="team-card reveal" style="transition-delay:0.18s"><div class="avatar"><img src="team-tanja.jpg" alt="Tanja Grabow" loading="lazy" decoding="async"></div><h3>Tanja Grabow</h3><div class="role">Fachkräftebetreuung</div><p class="bio">Unterstützt bei der Integration unserer Fachkräfte, von der Ankunft bis zum Alltag im Team.</p></div>
      </div>
      <p class="team-more-note" style="text-align:center;font-size:14.5px;color:var(--ink-mute);margin-top:26px;max-width:560px;margin-left:auto;margin-right:auto;">Neben Ivo, Sören, Tabeia und Tanja arbeiten je nach Projekt weitere Kolleg:innen im Hintergrund für Sie. Lernen Sie das gesamte Team gern in einem persönlichen Gespräch kennen.</p>
    </div>
  </section>

  <section style="background:var(--bg-soft);">
    <div class="wrap">
      <div class="section-head reveal"><h2>Einblicke aus unserer Arbeit.</h2></div>
      <div class="blog-grid">
        <a class="blog-card reveal" href="blog-post-4.html"><span class="blog-tag">Presse</span><h3>Damit internationale Pflegekräfte bleiben: Ivo im Gespräch mit care konkret</h3><div class="meta">Interview</div></a>
        <a class="blog-card reveal" href="blog-post-1.html" style="transition-delay:0.08s"><span class="blog-tag">RAL-Siegel</span><h3>Heinz Personnel Solutions erhält das RAL-Gütezeichen</h3><div class="meta">Ausführlicher Artikel</div></a>
        <a class="blog-card reveal" href="blog-post-3.html" style="transition-delay:0.16s"><span class="blog-tag">Integration</span><h3>Ankommen in Deutschland: Gemeinsam starten, Schritt für Schritt</h3><div class="meta">Ausführlicher Artikel</div></a>
      </div>
      <div class="process-cta"><a href="blog.html" class="btn btn-ghost btn-sm">Alle Artikel</a></div>
    </div>
  </section>

  <section class="closing">
    <div class="wrap reveal">
      <h2>Der nächste Schritt.</h2>
      <p>In einem unverbindlichen Erstgespräch klären wir, ob und wie wir zusammenarbeiten können. Wir freuen uns auf Sie.</p>
      <a href="kontakt.html" class="btn btn-primary">Gespräch vereinbaren</a>
    </div>
  </section>

</main>
'''
page("index.html", "Heinz Personnel Solutions — Pflegefachkräfte, die bleiben.", "index.html", index_body, description="Internationale Pflegefachkräfte für deutsche Kliniken und Pflegeeinrichtungen. RAL-zertifiziert, transparent, ohne versteckte Kosten. 92% bleiben länger als drei Jahre.")

print("index done")
