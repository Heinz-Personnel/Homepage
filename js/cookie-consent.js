/* Heinz Personnel Solutions: Einwilligungsbanner (Cookies und vergleichbare Technologien)
   Stand: Oktober 2026, ausgerichtet an § 25 TDDDG, DSGVO und VG Hannover (Az. 10 A 5385/22).
   Kategorien:
   - Notwendig (immer aktiv): speichert nur die Auswahl selbst im Browser (localStorage,
     Schlüssel "heinz_consent"), § 25 Abs. 2 Nr. 2 TDDDG. Keine Cookies, kein Tracking.
   - Statistik (nur mit Einwilligung): Google Analytics 4 (G-PB43PKLVEL), ohne Google Signals.
   - Marketing (nur mit Einwilligung): Google Ads Conversion-Tracking (AW-18457911738), kein Remarketing.
     Google Consent Mode v2 im Basis-Modus: Das Google-Tag lädt erst nach Einwilligung.
   Erste Ebene: "Alle akzeptieren" und "Nur notwendige Cookies" gleich groß und gleich gestaltet.
   Einwilligung gilt 12 Monate, danach wird erneut gefragt. Widerruf jederzeit über
   "Cookie-Einstellungen" (Link unten links und im Footer). */
(function () {
  var GADS_ID = 'AW-18457911738';
  var GA4_ID = 'G-PB43PKLVEL';
  var KEY = 'heinz_consent';
  var VERSION = 3; // 3: Statistik (Google Analytics) neu, daher erneute Abfrage
  var MAX_AGE_MS = 365 * 24 * 60 * 60 * 1000;
  var lang = document.documentElement.lang === 'en' ? 'en' : 'de';

  var T = {
    de: {
      title: 'Cookies',
      intro: 'Wir nutzen Cookies für Statistik (Google Analytics) und zur Erfolgsmessung unserer Anzeigen (Google Ads). Dabei können Daten in die USA übermittelt werden. Sie entscheiden selbst und können Ihre Auswahl jederzeit über „Cookie-Einstellungen“ ändern.',
      acceptAll: 'Alle akzeptieren',
      necessaryOnly: 'Nur notwendige Cookies',
      settings: 'Einstellungen',
      save: 'Auswahl speichern',
      back: 'Zurück',
      floating: 'Cookie-Einstellungen',
      privacy: 'Datenschutzerklärung', privacyHref: 'datenschutz.html',
      imprint: 'Impressum', imprintHref: 'impressum.html',
      alwaysOn: 'Immer aktiv',
      more: 'Details',
      necShort: 'Speichert nur Ihre Auswahl. Keine Cookies, keine Weitergabe.',
      staShort: 'Zeigt uns, wie die Website genutzt wird.',
      mktShort: 'Misst, ob Anzeigen zu Kontaktanfragen führen.',
      necTitle: 'Notwendig',
      necText: 'Speichert ausschließlich Ihre Auswahl in diesem Banner im Speicher Ihres Browsers, damit der Hinweis nicht bei jedem Seitenaufruf erscheint. Es werden dafür keine Cookies gesetzt und keine Daten an Dritte übermittelt. Speicherdauer: 12 Monate.',
      staTitle: 'Statistik',
      staText: 'Anbieter: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Zweck: verstehen, wie unsere Website genutzt wird, etwa welche Seiten besucht werden und woher Besucher:innen kommen, um sie zu verbessern. Dafür setzt Google Cookies (z. B. „_ga“) mit einer Speicherdauer von bis zu 2 Jahren. Google Analytics 4 speichert keine IP-Adressen. Daten können an Google LLC in den USA übermittelt werden, die nach dem EU-US Data Privacy Framework zertifiziert ist. Rechtsgrundlage: Ihre Einwilligung nach § 25 Abs. 1 TDDDG und Art. 6 Abs. 1 lit. a DSGVO.',
      staToggle: 'Google Analytics erlauben',
      mktTitle: 'Marketing',
      mktText: 'Anbieter: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Zweck: messen, ob Besucher:innen nach dem Klick auf eine Google-Anzeige von Heinz Kontakt aufnehmen. Dafür setzt Google Cookies (z. B. „_gcl_au“) mit einer Speicherdauer von bis zu 90 Tagen. Daten wie Ihre IP-Adresse und Informationen zu Ihrem Besuch können an Google LLC in den USA übermittelt werden. Google LLC ist nach dem EU-US Data Privacy Framework zertifiziert. Personalisierte Werbung (Remarketing) nutzen wir nicht. Rechtsgrundlage: Ihre Einwilligung nach § 25 Abs. 1 TDDDG und Art. 6 Abs. 1 lit. a DSGVO.',
      toggleLabel: 'Google Ads Conversion-Tracking erlauben'
    },
    en: {
      title: 'Cookies',
      intro: 'We use cookies for statistics (Google Analytics) and to measure the success of our ads (Google Ads). Data may be transferred to the USA. You decide, and you can change your choice at any time via “Cookie settings”.',
      acceptAll: 'Accept all',
      necessaryOnly: 'Necessary cookies only',
      settings: 'Settings',
      save: 'Save selection',
      back: 'Back',
      floating: 'Cookie settings',
      privacy: 'Privacy Policy', privacyHref: 'datenschutz-en.html',
      imprint: 'Legal Notice', imprintHref: 'impressum-en.html',
      alwaysOn: 'Always active',
      more: 'Details',
      necShort: 'Only stores your choice. No cookies, nothing shared.',
      staShort: 'Shows us how the website is used.',
      mktShort: 'Measures whether ads lead to contact requests.',
      necTitle: 'Necessary',
      necText: 'Only stores your choice in this banner in your browser\'s storage, so the notice does not appear on every page. No cookies are set for this and no data is passed to third parties. Storage period: 12 months.',
      staTitle: 'Statistics',
      staText: 'Provider: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland. Purpose: understanding how our website is used, for example which pages are visited and where visitors come from, in order to improve it. For this, Google sets cookies (e.g. “_ga”) stored for up to 2 years. Google Analytics 4 does not store IP addresses. Data may be transferred to Google LLC in the USA, which is certified under the EU-US Data Privacy Framework. Legal basis: your consent under Section 25(1) TDDDG and Art. 6(1)(a) GDPR.',
      staToggle: 'Allow Google Analytics',
      mktTitle: 'Marketing',
      mktText: 'Provider: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland. Purpose: measuring whether visitors contact Heinz after clicking a Google ad. For this, Google sets cookies (e.g. “_gcl_au”) stored for up to 90 days. Data such as your IP address and information about your visit may be transferred to Google LLC in the USA. Google LLC is certified under the EU-US Data Privacy Framework. We do not use personalised advertising (remarketing). Legal basis: your consent under Section 25(1) TDDDG and Art. 6(1)(a) GDPR.',
      toggleLabel: 'Allow Google Ads conversion tracking'
    }
  }[lang];

  /* ---------- Speicher ---------- */
  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (!v || v.v !== VERSION || (Date.now() - v.ts) > MAX_AGE_MS) return null;
      return v;
    } catch (e) { return null; }
  }
  function write(stats, marketing) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ v: VERSION, ts: Date.now(), stats: !!stats, marketing: !!marketing }));
      localStorage.removeItem('heinz_cookie_consent'); // alte Version
    } catch (e) {}
  }

  /* ---------- Google-Tag (Consent Mode v2, Basis-Modus) ---------- */
  function gtag() { window.dataLayer.push(arguments); }
  function loadGoogle(stats, marketing) {
    if (window.__gtagLoaded || (!stats && !marketing)) return;
    window.__gtagLoaded = { stats: !!stats, marketing: !!marketing };
    window.dataLayer = window.dataLayer || [];
    window.gtag = gtag;
    gtag('consent', 'default', {
      analytics_storage: stats ? 'granted' : 'denied',
      ad_storage: marketing ? 'granted' : 'denied',
      ad_user_data: marketing ? 'granted' : 'denied',
      ad_personalization: 'denied'
    });
    gtag('js', new Date());
    if (stats) gtag('config', GA4_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
    if (marketing) gtag('config', GADS_ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + (stats ? GA4_ID : GADS_ID);
    document.head.appendChild(s);
  }
  function deleteCookies(re) {
    var host = location.hostname.replace(/^www\./, '');
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (re.test(name)) {
        ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }
  function revoke(stats, marketing) {
    if (window.__gtagLoaded && window.gtag) {
      window.gtag('consent', 'update', {
        analytics_storage: stats ? 'granted' : 'denied',
        ad_storage: marketing ? 'granted' : 'denied',
        ad_user_data: marketing ? 'granted' : 'denied',
        ad_personalization: 'denied'
      });
    }
    if (!stats) deleteCookies(/^(_ga|_gid|_gat)/);
    if (!marketing) deleteCookies(/^(_gcl_|_gac_|_gads|_gpi)/);
  }

  /* ---------- Darstellung ---------- */
  function styles() {
    if (document.getElementById('cc-styles')) return;
    var css =
      '.cc-banner{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#1B2B99;color:#fff;font-family:var(--body,Inter,sans-serif);box-shadow:0 -4px 20px rgba(0,0,0,.25);max-height:80vh;overflow-y:auto;}' +
      '.cc-banner [hidden]{display:none!important;}' +
      '.cc-inner{max-width:1200px;margin:0 auto;padding:16px 20px;display:grid;grid-template-columns:1fr;gap:12px;align-items:center;}' +
      '@media(min-width:900px){.cc-inner{padding:16px 48px;grid-template-columns:1fr auto;gap:12px 32px;}}' +
      '.cc-title{font-family:var(--body,Inter,sans-serif);font-weight:700;font-size:.95rem;margin:0 0 4px;color:#fff;}' +
      '.cc-text{margin:0;font-size:.82rem;line-height:1.5;color:#fff;max-width:70ch;}' +
      '.cc-links{margin:6px 0 0;font-size:.78rem;}' +
      '.cc-links a{color:#fff;font-weight:700;text-underline-offset:3px;margin-right:16px;}' +
      '.cc-actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;}' +
      '.cc-actions .cc-btn:last-child{grid-column:1/-1;}' +
      '.cc-actions--settings{grid-column:1/-1;}' +
      '@media(min-width:900px){.cc-actions{grid-template-columns:repeat(3,190px);}.cc-actions .cc-btn:last-child{grid-column:auto;}.cc-actions--settings{justify-content:end;}}' +
      '.cc-btn{display:flex;align-items:center;justify-content:center;min-height:42px;padding:8px 12px;font-family:inherit;font-size:.85rem;font-weight:700;cursor:pointer;border:2px solid #fff;transition:background .18s ease,color .18s ease;}' +
      '.cc-btn--main{background:#fff;color:#1B2B99;}' +
      '.cc-btn--main:hover{background:transparent;color:#fff;}' +
      '.cc-btn--ghost{background:transparent;color:#fff;}' +
      '.cc-btn--ghost:hover{background:#fff;color:#1B2B99;}' +
      '.cc-btn:focus-visible,.cc-toggle input:focus-visible+span,.cc-floating:focus-visible,.cc-cat summary:focus-visible{outline:3px solid #FF5A1F;outline-offset:3px;}' +
      '.cc-cats{grid-column:1/-1;display:grid;grid-template-columns:1fr;gap:8px;}' +
      '@media(min-width:900px){.cc-cats{grid-template-columns:repeat(3,1fr);}}' +
      '.cc-cat{border:1px solid rgba(255,255,255,.35);padding:10px 14px;}' +
      '.cc-cat-head{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:4px;}' +
      '.cc-cat-head strong{font-size:.88rem;color:#fff;}' +
      '.cc-cat p{margin:0;font-size:.78rem;line-height:1.5;color:#fff;}' +
      '.cc-cat details{margin-top:4px;}' +
      '.cc-cat summary{cursor:pointer;font-size:.75rem;font-weight:700;color:#fff;text-decoration:underline;text-underline-offset:3px;}' +
      '.cc-cat details p{margin-top:6px;opacity:.9;}' +
      '.cc-always{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#fff;white-space:nowrap;}' +
      '.cc-toggle{position:relative;display:inline-flex;align-items:center;cursor:pointer;flex-shrink:0;}' +
      '.cc-toggle input{position:absolute;opacity:0;width:1px;height:1px;}' +
      '.cc-toggle span{width:42px;height:24px;border:2px solid #fff;border-radius:999px;position:relative;transition:background .18s ease;}' +
      '.cc-toggle span::after{content:"";position:absolute;top:3px;left:3px;width:14px;height:14px;border-radius:50%;background:#fff;transition:transform .18s ease;}' +
      '.cc-toggle input:checked+span{background:#FF5A1F;border-color:#FF5A1F;}' +
      '.cc-toggle input:checked+span::after{transform:translateX(18px);}' +
      '.cc-floating{position:fixed;left:16px;bottom:16px;z-index:9998;background:#1B2B99;color:#fff;border:2px solid #fff;font-family:var(--body,Inter,sans-serif);font-size:.75rem;font-weight:700;padding:6px 12px;cursor:pointer;}' +
      '.cc-floating:hover{background:#fff;color:#1B2B99;}';
    var st = document.createElement('style');
    st.id = 'cc-styles';
    st.textContent = css;
    document.head.appendChild(st);
  }

  function floating() {
    if (document.getElementById('cc-floating')) return;
    var b = document.createElement('button');
    b.type = 'button';
    b.id = 'cc-floating';
    b.className = 'cc-floating';
    b.textContent = T.floating;
    b.addEventListener('click', function () { open(true); });
    document.body.appendChild(b);
  }

  function close(el) {
    el.remove();
    floating();
  }

  function decide(el, stats, marketing) {
    var loaded = window.__gtagLoaded;
    write(stats, marketing);
    revoke(stats, marketing);
    close(el);
    // Wurde Google schon mit anderer Auswahl geladen, Seite neu laden, damit genau die neue Auswahl gilt.
    if (loaded && (loaded.stats !== !!stats || loaded.marketing !== !!marketing)) { location.reload(); return; }
    loadGoogle(stats, marketing);
  }

  function open(showSettings) {
    styles();
    var old = document.getElementById('cc-banner');
    if (old) old.remove();
    var f = document.getElementById('cc-floating');
    if (f) f.remove();
    var cur = read();

    var el = document.createElement('div');
    el.id = 'cc-banner';
    el.className = 'cc-banner';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-labelledby', 'cc-title');
    el.innerHTML =
      '<div class="cc-inner">' +
        '<div class="cc-copy"><h2 class="cc-title" id="cc-title">' + T.title + '</h2>' +
        '<p class="cc-text">' + T.intro + '</p>' +
        '<p class="cc-links"><a href="' + T.privacyHref + '">' + T.privacy + '</a><a href="' + T.imprintHref + '">' + T.imprint + '</a></p></div>' +
        '<div class="cc-cats" hidden>' +
          '<div class="cc-cat"><div class="cc-cat-head"><strong>' + T.necTitle + '</strong><span class="cc-always">' + T.alwaysOn + '</span></div><p>' + T.necShort + '</p><details><summary>' + T.more + '</summary><p>' + T.necText + '</p></details></div>' +
          '<div class="cc-cat"><div class="cc-cat-head"><strong>' + T.staTitle + '</strong>' +
            '<label class="cc-toggle"><input type="checkbox" id="cc-sta" aria-label="' + T.staToggle + '"' + (cur && cur.stats ? ' checked' : '') + '><span></span></label>' +
          '</div><p>' + T.staShort + '</p><details><summary>' + T.more + '</summary><p>' + T.staText + '</p></details></div>' +
          '<div class="cc-cat"><div class="cc-cat-head"><strong>' + T.mktTitle + '</strong>' +
            '<label class="cc-toggle"><input type="checkbox" id="cc-mkt" aria-label="' + T.toggleLabel + '"' + (cur && cur.marketing ? ' checked' : '') + '><span></span></label>' +
          '</div><p>' + T.mktShort + '</p><details><summary>' + T.more + '</summary><p>' + T.mktText + '</p></details></div>' +
        '</div>' +
        '<div class="cc-actions cc-actions--main">' +
          '<button type="button" class="cc-btn cc-btn--main" data-cc="all">' + T.acceptAll + '</button>' +
          '<button type="button" class="cc-btn cc-btn--main" data-cc="necessary">' + T.necessaryOnly + '</button>' +
          '<button type="button" class="cc-btn cc-btn--ghost" data-cc="settings">' + T.settings + '</button>' +
        '</div>' +
        '<div class="cc-actions cc-actions--settings" hidden>' +
          '<button type="button" class="cc-btn cc-btn--main" data-cc="save">' + T.save + '</button>' +
          '<button type="button" class="cc-btn cc-btn--main" data-cc="necessary">' + T.necessaryOnly + '</button>' +
          '<button type="button" class="cc-btn cc-btn--ghost" data-cc="back">' + T.back + '</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(el);

    var cats = el.querySelector('.cc-cats');
    var mainActs = el.querySelector('.cc-actions--main');
    var setActs = el.querySelector('.cc-actions--settings');
    function settingsView(on) {
      cats.hidden = !on;
      mainActs.hidden = on;
      setActs.hidden = !on;
      if (on) el.querySelector('#cc-sta').focus();
    }
    el.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cc]');
      if (!b) return;
      var a = b.getAttribute('data-cc');
      if (a === 'all') decide(el, true, true);
      else if (a === 'necessary') decide(el, false, false);
      else if (a === 'save') decide(el, el.querySelector('#cc-sta').checked, el.querySelector('#cc-mkt').checked);
      else if (a === 'settings') settingsView(true);
      else if (a === 'back') settingsView(false);
    });
    if (showSettings) settingsView(true);
  }

  /* Öffnen über beliebige Links mit data-cookie-settings (z. B. im Footer) */
  document.addEventListener('click', function (e) {
    var l = e.target.closest && e.target.closest('[data-cookie-settings]');
    if (l) { e.preventDefault(); open(true); }
  });

  function init() {
    var c = read();
    if (!c) { open(false); return; }
    loadGoogle(c.stats, c.marketing);
    floating();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
