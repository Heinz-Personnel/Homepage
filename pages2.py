#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# Der animierte "Weg" (vormals eigene Unterseite unser-weg.html) — jetzt
# direkt in fuer-einrichtungen.html eingebettet, keine eigene Seite mehr.
ROUTE_CSS = '''
  .route-wrap{position:relative;max-width:1040px;margin:0 auto;padding:20px 24px 20px;}
  .route-svg{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;overflow:visible;}
  .route-svg path{fill:none;stroke:var(--green);stroke-width:1.6;stroke-dasharray:6 7;stroke-linecap:round;}
  .waypoint{position:relative;z-index:1;width:47%;margin-bottom:80px;background:var(--bg);}
  .waypoint.left{margin-right:53%;}
  .waypoint.right{margin-left:53%;}
  .waypoint .tag{display:inline-block;font-family:'Outfit',sans-serif;font-weight:600;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--coral-text);background:var(--coral-tint);padding:5px 12px;border-radius:999px;margin-bottom:14px;}
  .waypoint h3{font-family:'Outfit',sans-serif;font-size:clamp(19px,2.2vw,24px);margin-bottom:12px;color:var(--ink);}
  .waypoint p{font-size:15px;margin:0;}
  .waypoint ul{margin:10px 0 0;padding-left:18px;}
  .waypoint li{font-size:13.5px;color:var(--ink-soft);margin-bottom:4px;}
  .waypoint .time{display:block;font-size:12.5px;color:var(--ink-mute);margin-top:10px;font-weight:500;}
  .waypoint::before{content:'';position:absolute;top:8px;width:12px;height:12px;border-radius:50%;background:var(--coral);border:3px solid var(--bg);box-shadow:0 0 0 2px var(--coral);}
  .route-wrap .waypoint:last-child{margin-bottom:0;}
  .waypoint.left::before{right:-30px;}
  .waypoint.right::before{left:-30px;}
  .stamps{display:flex;gap:18px;flex-wrap:wrap;margin-top:22px;}
  .stamp{display:flex;flex-direction:column;align-items:center;gap:6px;padding:12px 14px;border:2px dashed var(--green-dark);border-radius:10px;background:rgba(255,255,255,.7);opacity:0;transform:scale(0.7) rotate(-14deg);transition:opacity .5s ease, transform .5s cubic-bezier(.34,1.56,.64,1);}
  .stamp.in{opacity:1;}
  .stamp:nth-child(1).in{transform:rotate(-7deg);}
  .stamp:nth-child(2).in{transform:rotate(4deg);}
  .stamp:nth-child(3).in{transform:rotate(-2deg);}
  .stamp img{height:32px;width:auto;}
  .stamp span{font-size:9.5px;font-weight:600;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.04em;}
  @media (max-width:820px){
    .route-svg{left:10px;}
    .route-svg path{stroke-dasharray:5 6;}
    .waypoint,.waypoint.left,.waypoint.right{width:100%;margin-left:36px;margin-right:0;}
    .waypoint::before,.waypoint.left::before,.waypoint.right::before{left:-32px;right:auto;}
  }
'''

ROUTE_SCRIPT = '''
  var stamps = document.querySelectorAll('.stamp');
  if ('IntersectionObserver' in window){
    var sio = new IntersectionObserver(function(entries, obs){
      entries.forEach(function(entry){ if (entry.isIntersecting){ entry.target.classList.add('in'); obs.unobserve(entry.target); } });
    }, { threshold:0.3 });
    stamps.forEach(function(el){ sio.observe(el); });
  }
  var routePath = document.getElementById('routePath');
  var routeWrap = document.getElementById('route');
  var pathLen = 0;
  function setupPath(){ if(!routePath) return; pathLen = routePath.getTotalLength(); routePath.style.strokeDasharray = pathLen; }
  function updatePath(){
    if(!routeWrap || !routePath) return;
    var rect = routeWrap.getBoundingClientRect();
    var vh = window.innerHeight;
    var total = rect.height + vh;
    var progress = (vh - rect.top) / total;
    progress = Math.max(0, Math.min(1, progress));
    routePath.style.strokeDashoffset = pathLen * (1 - progress);
  }
  window.addEventListener('load', function(){ setupPath(); updatePath(); });
  window.addEventListener('resize', function(){ setupPath(); updatePath(); });
  window.addEventListener('scroll', updatePath, { passive:true });
'''

# ================================================= FÜR EINRICHTUNGEN ====
einrichtungen_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Für Arbeitgeber</div>
    <span class="eyebrow">Für Kliniken & Pflegeeinrichtungen</span>
    <h1 class="reveal in">Besetzung, die bleibt.</h1>
    <p class="lead reveal in">Für uns ist eine Vermittlung nicht erfolgreich, wenn ein Vertrag unterschrieben ist. Sie ist erfolgreich, wenn Ihre Fachkraft Jahre später noch im Team ist.</p>
    <div class="hero-proof-strip reveal">
      <div class="hero-proof-stat"><div class="num">92%</div><div class="lbl">bleiben länger als drei Jahre</div></div>
      <div class="hero-proof-stat"><div class="num">400+</div><div class="lbl">erfolgreich vermittelte Fachkräfte</div></div>
      <div class="hero-proof-stat"><div class="num">98%</div><div class="lbl">erfolgreiche Berufsanerkennungen</div></div>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="wrap">
    <span class="badge"><img src="logo-ral-guetezeichen.svg" alt="RAL-Gütezeichen Faire Anwerbung Pflege Deutschland" style="height:100px"></span>
    <span class="badge"><img src="logo-bvifg.png" alt="Mitglied im Bundesverband Internationale Fachkräftegewinnung" style="height:74px"></span>
    <span class="badge"><img src="logo-gapa.png" alt="GAPA – Gütegemeinschaft zur Anwerbung und Vermittlung von Pflegekräften aus dem Ausland" style="height:96px"></span>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="problem reveal">
      <h2>Offene Stellen nachhaltig besetzen.</h2>
      <p>In der Pflege fehlen vielerorts qualifizierte Fachkräfte. Der Bedarf wächst spürbar schneller, als der deutsche Arbeitsmarkt ihn allein decken kann. Für Personalverantwortliche heißt das: unbesetzte Dienste, Dauerbelastung im Team und die Sorge, dass eine schnelle Lösung langfristig nichts bringt.</p>
      <p>Faire Anwerbung ist heute Standard, das RAL-Gütezeichen und die bvifg-Mitgliedschaft zeigen das. Entscheidend ist etwas anderes: ob eine Fachkraft auch nach Jahren noch da ist. Genau darauf richten wir unseren Prozess aus. Passt es einmal nicht, sorgen wir unkompliziert und ohne zusätzliche Kosten für eine neue Fachkraft.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Warum HPS statt Zeitarbeit oder Social-Media-Recruiting?</h2></div>
    <div class="split">
      <div class="win-card reveal">
        <h3>Zeitarbeit</h3>
        <p>Löst akute Engpässe kurzfristig, aber ohne langfristige Bindung ans Team. Hohe Fluktuation, wiederkehrender Aufwand, keine Integration in die Einrichtung.</p>
      </div>
      <div class="win-card reveal" style="transition-delay:.08s">
        <h3>Social-Media-Recruiting</h3>
        <p>Erreicht viele Bewerber:innen, aber ohne strukturierten Anerkennungs- und Integrationsprozess. Das Risiko einer Fehlbesetzung bleibt bei der Einrichtung.</p>
      </div>
    </div>
    <div class="win-card featured reveal" style="margin-top:22px;">
      <h3>Unser Ansatz</h3>
      <p>Erfahrene internationale Pflegefachkräfte, begleitet von der ersten Kontaktaufnahme bis weit über den ersten Arbeitstag hinaus. Das Ergebnis: 92% unserer vermittelten Fachkräfte bleiben länger als drei Jahre.</p>
    </div>
  </div>
</section>

<section id="prozess">
  <div class="wrap">
    <div class="section-head reveal"><h2>Unser Prozess im Detail</h2><p style="font-size:15.5px;margin-top:10px;">Ein Weg, dem man folgen kann: von der ersten Bedarfsanalyse bis zur langfristigen Integration.</p></div>
  </div>
  <div class="route-wrap" id="route">
    <svg class="route-svg" id="routeSvg" viewBox="0 0 100 800" preserveAspectRatio="none">
      <path id="routePath" d="M50,0 C20,50 20,90 50,120 C80,150 80,190 50,220 C20,250 20,300 50,330 C80,360 80,400 50,430 C20,460 20,510 50,540 C60,560 60,590 50,620"/>
    </svg>
    <div class="waypoint right reveal">
      <span class="tag">Station 1</span><h3>Bedarfsanalyse</h3>
      <p>Wir stimmen uns persönlich mit Ihnen ab und klären, wer wirklich zu Ihrer Einrichtung passt.</p>
      <span class="time">Tag 1</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Station 2</span><h3>Matching aus dem Pool</h3>
      <p>Wir schlagen passende Kandidat:innen aus unserem bestehenden, bereits vorqualifizierten Pool vor. Kein Start bei null.</p>
      <span class="time">Ab Woche 2</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Station 3</span><h3>Anerkennung &amp; Visum</h3>
      <p>Sprachprozess und Anerkennung laufen für unseren Pool bereits parallel. Das verkürzt Ihre Wartezeit spürbar.</p>
      <span class="time">6 Monate</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Station 4</span><h3>Einreise &amp; Integration</h3>
      <p>Empfang vor Ort und Begleitung, so lange sie gebraucht wird.</p>
      <span class="time">Ab Tag 1 im Team</span>
      <div class="stamps">
        <div class="stamp"><img src="logo-ral-guetezeichen.png" alt="RAL-Gütezeichen Faire Anwerbung Pflege Deutschland" loading="lazy" decoding="async"><span>RAL-geprüft</span></div>
        <div class="stamp"><img src="logo-bvifg.png" alt="Mitglied im bvifg" loading="lazy" decoding="async"><span>bvifg</span></div>
        <div class="stamp"><img src="logo-gapa.png" alt="GAPA Gütegemeinschaft" loading="lazy" decoding="async"><span>GAPA</span></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Kein Zufall. Ein System.</h2>
      <p style="font-size:15.5px;margin-top:10px;max-width:680px;">Unser Erfolg beruht nicht auf Zufall, sondern auf einem eigenen Modell: dem HEINZ Integrationsmodell. Entwickelt auf Basis wissenschaftlicher Forschung, unter anderem mit der Leuphana Universität, und geschärft durch unsere eigene Erfahrung seit 2018.</p>
    </div>
    <div class="heinz-grid">
      <div class="heinz-letter reveal"><div class="big">H</div><div class="lbl">Handlungssicherheit<br>Orientierung &amp; Onboarding</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.04s"><div class="big">E</div><div class="lbl">Erwartungen matchen<br>Transparenz &amp; Placement</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.08s"><div class="big">I</div><div class="lbl">Inklusion &amp; Respekt<br>Employer-Coaching</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.12s"><div class="big">N</div><div class="lbl">Navigation ermöglichen<br>Sprache &amp; System</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.16s"><div class="big">Z</div><div class="lbl">Zukunft &amp; Verwurzelung<br>Settlement &amp; Karriere</div></div>
    </div>
    <p class="heinz-proof reveal">Ein Beispiel aus der Forschung: Strukturierte Orientierung in den ersten Wochen senkt die Abbruchquote nachweislich um 36 Prozent. Mehr zum HEINZ Integrationsmodell erfahren Sie im persönlichen Gespräch.</p>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="clients standalone reveal">
      <p class="lead-sm">Diese Einrichtungen arbeiten bereits mit uns zusammen:</p>
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

<section class="closing">
  <div class="wrap reveal">
    <h2>Neugierig geworden?</h2>
    <p>In einem unverbindlichen Erstgespräch informieren wir gern weiter und schauen, ob und wie wir zusammenarbeiten können.</p>
    <a href="kontakt.html" class="btn btn-primary">Gespräch vereinbaren</a>
  </div>
</section>
'''
page("fuer-einrichtungen.html", "Für Arbeitgeber — Heinz Personnel Solutions", "fuer-einrichtungen.html", einrichtungen_body, description="Planbare Besetzung mit internationalen Pflegefachkräften: RAL-Gütezeichen, Ausfallabsicherung, im Schnitt 6 Monate bis zum ersten Arbeitstag.", extra_script=ROUTE_SCRIPT, extra_css=ROUTE_CSS)

# =================================================== FÜR FACHKRÄFTE ====
ANKAADIA_URL = "https://app.ankaadia.com/candidate-application/4ffb749b-c604-47f5-b04b-f84bdf96bd8e/4eb15342-1f37-4771-bdec-4f7f94f5687a"

fachkraefte_body = f'''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Für Fachkräfte</div>
    <span class="eyebrow">Für Pflegefachkräfte, die nach Deutschland kommen möchten</span>
    <h1 class="reveal in">Ihr Weg nach Deutschland. Fair, transparent, ohne versteckte Kosten.</h1>
    <p class="lead reveal in">Wir begleiten Sie persönlich von der ersten Anfrage bis zum Ankommen im Team, und darüber hinaus.</p>
    <div class="hero-cta-row reveal" style="margin-top:22px;">
      <a href="{ANKAADIA_URL}" class="btn btn-primary" target="_blank" rel="noopener">Jetzt bewerben</a>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="wrap">
    <span class="badge"><img src="logo-ral-guetezeichen.svg" alt="RAL-Gütezeichen Faire Anwerbung Pflege Deutschland" style="height:100px"></span>
    <span class="badge"><img src="logo-bvifg.png" alt="Mitglied im Bundesverband Internationale Fachkräftegewinnung" style="height:74px"></span>
    <span class="badge"><img src="logo-gapa.png" alt="GAPA – Gütegemeinschaft zur Anwerbung und Vermittlung von Pflegekräften aus dem Ausland" style="height:96px"></span>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="win-card reveal" style="max-width:720px;border-color:var(--green);">
      <h3>Unser klares Versprechen an Sie</h3>
      <p>Keine versteckten Kosten. Keine Rückzahlungsmodelle. Sie zahlen nichts für Ihre Vermittlung. Das ist fester Bestandteil unseres RAL-zertifizierten Prozesses.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Echte Erfolgsgeschichten.</h2><p style="font-size:15.5px;margin-top:10px;">Kein Stockfoto-Lächeln. So sieht es wirklich aus, wenn unsere Fachkräfte in Deutschland ankommen und ein Zuhause finden.</p></div>
    <div class="story-grid">
      <a class="reveal" href="blog-post-5.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-willkommen-gruppe.jpg" alt="Ankunft am Flughafen Berlin Brandenburg, herzlicher Empfang" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">Angekommen: Willkommen in Deutschland</p></a>
      <a class="reveal" style="transition-delay:.08s" href="blog-post-6.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-mietwagen-team.jpg" alt="Team-Empfang am Flughafen" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">Der erste Tag, gemeinsam mit dem Team</p></a>
      <a class="reveal" style="transition-delay:.16s" href="blog-post-7.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-gartenfest.jpg" alt="Sommerfest mit dem gesamten Team" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">Ein Jahr später: Sommerfest mit dem Team</p></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Ihr Weg, Schritt für Schritt.</h2><p style="font-size:15.5px;margin-top:10px;max-width:680px;">Von der ersten Vorstellung bis zum Ankommen im Team: transparent, mit klaren Zeiträumen. Sprachausbildung und Anerkennungsverfahren laufen bei uns parallel, das ist der Grund, warum Einrichtungen, die bereits mit unserem Kandidat:innen-Pool arbeiten, ihre neue Fachkraft im Schnitt schon nach 6 Monaten begrüßen können. Bewerben Sie sich jetzt neu, rechnen Sie mit rund 12 bis 13 Monaten bis zur Einreise.</p></div>
  </div>
  <div class="route-wrap" id="route">
    <svg class="route-svg" id="routeSvg" viewBox="0 0 100 1000" preserveAspectRatio="none">
      <path id="routePath" d="M50,0 C20,50 20,90 50,120 C80,150 80,190 50,220 C20,250 20,300 50,330 C80,360 80,400 50,430 C20,460 20,510 50,540 C80,570 80,610 50,640 C20,670 20,710 50,740"/>
    </svg>
    <div class="waypoint right reveal">
      <span class="tag">Station 1</span><h3>Kennenlernen &amp; Bewerbung</h3>
      <p>Wir lernen uns persönlich kennen und sprechen über Ihre Erfahrung, Ihre Wünsche und mögliche Einrichtungen.</p>
      <ul>
        <li>Video- oder Vor-Ort-Gespräch mit unserem Team</li>
        <li>Aufnahme Ihrer Qualifikation und Berufserfahrung</li>
        <li>Vorstellung passender Einrichtungen, Matching beginnt</li>
      </ul>
      <span class="time">Tag 1</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Station 2</span><h3>Sprachausbildung A1 bis B2</h3>
      <p>Deutschunterricht mit muttersprachlichen Lehrkräften, organisiert über unseren Partner Lingoda, bis zum sicheren B2-Niveau.</p>
      <ul>
        <li>Einstufungstest und individueller Lernplan</li>
        <li>Wöchentlicher Online- oder Präsenzunterricht</li>
        <li>Zwischenprüfungen auf A2- und B1-Niveau</li>
        <li>In der Regel 6 bis 9 Monate bis zur B2-Abschlussprüfung</li>
      </ul>
      <span class="time">Ab Monat 1</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Station 3</span><h3>Anerkennung &amp; Arbeitsmarktzulassung</h3>
      <p>Wir koordinieren Defizitbescheid, Berufsanerkennung und Arbeitsmarktzulassung, parallel zum Sprachkurs.</p>
      <ul>
        <li>Zeugnisbewertung und Defizitbescheid der zuständigen Landesbehörde</li>
        <li>Falls nötig: Anpassungsmaßnahme oder Kenntnisprüfung</li>
        <li>Antrag auf Berufsanerkennung und Arbeitsmarktzulassung</li>
        <li>Dauer je nach Bundesland meist 6 bis 12 Monate, läuft parallel zum Sprachkurs</li>
      </ul>
      <span class="time">Ab Monat 9</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Station 4</span><h3>Visum &amp; Einreise</h3>
      <p>Wir begleiten den Visumsprozess und organisieren die Reise. Am Ankunftstag holen wir Sie persönlich ab.</p>
      <ul>
        <li>Termin und Unterlagen für die deutsche Auslandsvertretung</li>
        <li>Organisation von Reise und erster Unterkunft</li>
        <li>Persönliche Abholung am Flughafen</li>
      </ul>
      <span class="time">Ab Monat 13</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Station 5</span><h3>Ankommen &amp; Integration</h3>
      <p>Wohnung, Behördengänge, Kontoeröffnung, erste Wochen im Team, und Begleitung, so lange sie gebraucht wird.</p>
      <ul>
        <li>Anmeldung beim Einwohnermeldeamt, Bankkonto, Krankenversicherung</li>
        <li>Einführung und Begleitung im neuen Team</li>
        <li>Laufende Betreuung durch unser Integrationsmanagement, auch über den ersten Arbeitstag hinaus</li>
      </ul>
      <span class="time">Start Ankommen</span>
      <div class="stamps">
        <div class="stamp"><img src="logo-ral-guetezeichen.png" alt="RAL-Gütezeichen Faire Anwerbung Pflege Deutschland" loading="lazy" decoding="async"><span>RAL-geprüft</span></div>
        <div class="stamp"><img src="logo-bvifg.png" alt="Mitglied im bvifg" loading="lazy" decoding="async"><span>bvifg</span></div>
        <div class="stamp"><img src="logo-gapa.png" alt="GAPA Gütegemeinschaft" loading="lazy" decoding="async"><span>GAPA</span></div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Ihre Ansprechpartnerinnen</h2></div>
    <div class="team-grid" style="grid-template-columns:repeat(2,1fr);max-width:560px;">
      <div class="team-card reveal"><div class="avatar"><img src="team-tabeia.jpg" alt="Tabeia Antonio" loading="lazy" decoding="async"></div><h3>Tabeia Antonio</h3><div class="role">Integrationsmanagerin</div><p class="bio">Begleitet Sie von der Anwerbung bis zum festen Platz im Team.</p></div>
      <div class="team-card reveal" style="transition-delay:0.08s"><div class="avatar"><img src="team-tanja.jpg" alt="Tanja Grabow" loading="lazy" decoding="async"></div><h3>Tanja Grabow</h3><div class="role">Fachkräftebetreuung</div><p class="bio">Unterstützt Sie von der Wohnungssuche bis zum ersten Arbeitstag.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>RAL-Gütezeichen „Faire Anwerbung Pflege“</h2></div>
    <div class="win-card reveal" style="max-width:760px;">
      <p style="margin:0 0 12px;">HPS trägt das RAL-Gütezeichen „Faire Anwerbung Pflege Deutschland“ und ist Mitglied im Bundesverband Internationale Fachkräftegewinnung (bvifg). Das bedeutet: unabhängig geprüfte, faire Anwerbungsstandards, für Sie überprüfbar und mit einem klaren Beschwerdeweg, falls einmal etwas nicht nach Plan läuft.</p>
      <a href="beschwerdeformular.html" class="btn btn-ghost btn-sm">Beschwerdeformular</a>
    </div>
    <div class="section-head reveal" style="margin-top:44px;margin-bottom:20px;"><h3 style="font-size:19px;">Wichtige Links für Ihre Planung</h3></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">RAL-Gütegemeinschaft Faire Anwerbung Pflege</div><div class="rdesc">Offizielle Stelle des RAL-Gütezeichens, unabhängige Prüfung fairer Anwerbung.</div></a>
      <a class="resource-link" href="https://fair-recruitment-nurse.com/" target="_blank" rel="noopener"><div class="rtitle">fair-recruitment-nurse.com</div><div class="rdesc">Informationen, wie Sie zertifizierte, faire Vermittlungsagenturen erkennen.</div></a>
      <a class="resource-link" href="https://www.anerkennung-in-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">Anerkennung in Deutschland</div><div class="rdesc">Offizielles Portal der Bundesregierung zur Anerkennung ausländischer Berufsqualifikationen.</div></a>
      <a class="resource-link" href="https://www.make-it-in-germany.com/de/" target="_blank" rel="noopener"><div class="rtitle">Make it in Germany</div><div class="rdesc">Offizielles Portal der Bundesregierung für internationale Fachkräfte.</div></a>
      <a class="resource-link" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="rtitle">Bundesverband Internationale Fachkräftegewinnung</div><div class="rdesc">Bundesweiter Verband für faire, transparente Fachkräftegewinnung.</div></a>
      <a class="resource-link" href="downloads.html"><div class="rtitle">Downloads &amp; Dokumente</div><div class="rdesc">Infobroschüren, AGB und Selbstverpflichtungserklärung zum Nachlesen.</div></a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Interesse an einer Stelle in Deutschland?</h2>
    <p>Bewerben Sie sich direkt oder schreiben Sie uns. Wir melden uns persönlich zurück.</p>
    <div class="hero-cta-row" style="justify-content:center;">
      <a href="{ANKAADIA_URL}" class="btn btn-primary" target="_blank" rel="noopener">Jetzt bewerben</a>
      <a href="kontakt.html" class="btn btn-ghost">Kontakt aufnehmen</a>
    </div>
  </div>
</section>
'''
page("fuer-fachkraefte.html", "Für Fachkräfte — Heinz Personnel Solutions", "fuer-fachkraefte.html", fachkraefte_body, description="Ihr Weg als Pflegefachkraft nach Deutschland: fair, transparent, ohne versteckte Kosten. Sprachkurs, Anerkennung, Visum und persönliche Begleitung.", extra_script=ROUTE_SCRIPT, extra_css=ROUTE_CSS)

print("einrichtungen + fachkraefte done")
