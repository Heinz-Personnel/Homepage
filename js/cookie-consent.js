/* Heinz Personnel Solutions: Einwilligungsbanner (Cookies und vergleichbare Technologien)
   Stand: Oktober 2026, ausgerichtet an § 25 TDDDG, DSGVO und VG Hannover (Az. 10 A 5385/22).
   Kategorien:
   - Notwendig (immer aktiv): speichert nur die Auswahl selbst im Browser (localStorage,
     Schlüssel "heinz_consent"), § 25 Abs. 2 Nr. 2 TDDDG. Keine Cookies, kein Tracking.
   - Marketing (nur mit Einwilligung): Google Ads Conversion-Tracking (AW-18457911738).
     Google Consent Mode v2 im Basis-Modus: Das Google-Tag lädt erst nach Einwilligung.
   Erste Ebene: "Alle akzeptieren" und "Nur notwendige Cookies" gleich groß und gleich gestaltet.
   Einwilligung gilt 12 Monate, danach wird erneut gefragt. Widerruf jederzeit über
   "Cookie-Einstellungen" (Link unten links und im Footer). */
(function () {
  var GADS_ID = 'AW-18457911738';
  var KEY = 'heinz_consent';
  var VERSION = 2;
  var MAX_AGE_MS = 365 * 24 * 60 * 60 * 1000;
  var lang = document.documentElement.lang === 'en' ? 'en' : 'de';

  var T = {
    de: {
      title: 'Datenschutz-Einstellungen',
      intro: 'Wir nutzen technisch notwendige Speicherfunktionen, damit diese Website funktioniert und Ihre Auswahl gespeichert bleibt. Mit Ihrer Einwilligung setzen wir zusätzlich Google Ads Conversion-Tracking ein. So sehen wir, ob jemand nach dem Klick auf eine unserer Anzeigen Kontakt mit uns aufnimmt. Dabei werden Daten an Google übermittelt, auch in die USA. Ihre Auswahl können Sie jederzeit über „Cookie-Einstellungen“ ändern oder widerrufen.',
      acceptAll: 'Alle akzeptieren',
      necessaryOnly: 'Nur notwendige Cookies',
      settings: 'Einstellungen',
      save: 'Auswahl speichern',
      back: 'Zurück',
      floating: 'Cookie-Einstellungen',
      privacy: 'Datenschutzerklärung', privacyHref: 'datenschutz.html',
      imprint: 'Impressum', imprintHref: 'impressum.html',
      alwaysOn: 'Immer aktiv',
      necTitle: 'Notwendig',
      necText: 'Speichert ausschließlich Ihre Auswahl in diesem Banner im Speicher Ihres Browsers, damit der Hinweis nicht bei jedem Seitenaufruf erscheint. Es werden dafür keine Cookies gesetzt und keine Daten an Dritte übermittelt. Speicherdauer: 12 Monate.',
      mktTitle: 'Marketing: Google Ads Conversion-Tracking',
      mktText: 'Anbieter: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Zweck: messen, ob Besucher:innen nach dem Klick auf eine Google-Anzeige von Heinz Kontakt aufnehmen. Dafür setzt Google Cookies (z. B. „_gcl_au“) mit einer Speicherdauer von bis zu 90 Tagen. Daten wie Ihre IP-Adresse und Informationen zu Ihrem Besuch können an Google LLC in den USA übermittelt werden. Google LLC ist nach dem EU-US Data Privacy Framework zertifiziert. Personalisierte Werbung (Remarketing) nutzen wir nicht. Rechtsgrundlage: Ihre Einwilligung nach § 25 Abs. 1 TDDDG und Art. 6 Abs. 1 lit. a DSGVO.',
      toggleLabel: 'Google Ads Conversion-Tracking erlauben'
    },
    en: {
      title: 'Privacy settings',
      intro: 'We use technically necessary storage so that this website works and your choice is remembered. With your consent, we also use Google Ads conversion tracking. This shows us whether someone contacts us after clicking one of our ads. Data is transferred to Google, including to the USA. You can change or withdraw your choice at any time via “Cookie settings”.',
      acceptAll: 'Accept all',
      necessaryOnly: 'Necessary cookies only',
      settings: 'Settings',
      save: 'Save selection',
      back: 'Back',
      floating: 'Cookie settings',
      privacy: 'Privacy Policy', privacyHref: 'datenschutz-en.html',
      imprint: 'Legal Notice', imprintHref: 'impressum-en.html',
      alwaysOn: 'Always active',
      necTitle: 'Necessary',
      necText: 'Only stores your choice in this banner in your browser\'s storage, so the notice does not appear on every page. No cookies are set for this and no data is passed to third parties. Storage period: 12 months.',
      mktTitle: 'Marketing: Google Ads conversion tracking',
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
  function write(marketing) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ v: VERSION, ts: Date.now(), marketing: !!marketing }));
      localStorage.removeItem('heinz_cookie_consent'); // alte Version
    } catch (e) {}
  }

  /* ---------- Google Ads (Consent Mode v2, Basis-Modus) ---------- */
  function gtag() { window.dataLayer.push(arguments); }
  function loadGoogleAds() {
    if (window.__gadsLoaded) return;
    window.__gadsLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = gtag;
    gtag('consent', 'default', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'denied',
      analytics_storage: 'denied'
    });
    gtag('js', new Date());
    gtag('config', GADS_ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GADS_ID;
    document.head.appendChild(s);
  }
  function revokeGoogleAds() {
    if (window.__gadsLoaded && window.gtag) {
      window.gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' });
    }
    var host = location.hostname.replace(/^www\./, '');
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (/^(_gcl_|_gac_|_gads|_gpi)/.test(name)) {
        ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }

  /* ---------- Darstellung ---------- */
  function styles() {
    if (document.getElementById('cc-styles')) return;
    var css =
      '.cc-banner{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#1B2B99;color:#fff;font-family:var(--body,Inter,sans-serif);box-shadow:0 -6px 28px rgba(0,0,0,.28);max-height:90vh;overflow-y:auto;}' +
      '.cc-banner [hidden]{display:none!important;}' +
      '.cc-inner{max-width:1200px;margin:0 auto;padding:24px;}' +
      '@media(min-width:768px){.cc-inner{padding:28px 48px;}}' +
      '.cc-title{font-family:var(--display,Anton,sans-serif);text-transform:uppercase;font-weight:400;font-size:1.35rem;letter-spacing:.01em;margin:0 0 10px;color:#fff;}' +
      '.cc-text{margin:0;font-size:.92rem;line-height:1.6;color:#fff;max-width:900px;}' +
      '.cc-links{margin:10px 0 0;font-size:.85rem;}' +
      '.cc-links a{color:#fff;font-weight:700;text-underline-offset:3px;margin-right:18px;}' +
      '.cc-actions{display:grid;grid-template-columns:1fr;gap:12px;margin-top:20px;}' +
      '@media(min-width:700px){.cc-actions{grid-template-columns:1fr 1fr 1fr;max-width:900px;}}' +
      '.cc-btn{display:flex;align-items:center;justify-content:center;min-height:52px;padding:12px 18px;font-family:inherit;font-size:.95rem;font-weight:700;cursor:pointer;border:2px solid #fff;transition:background .18s ease,color .18s ease;}' +
      '.cc-btn--main{background:#fff;color:#1B2B99;}' +
      '.cc-btn--main:hover{background:transparent;color:#fff;}' +
      '.cc-btn--ghost{background:transparent;color:#fff;}' +
      '.cc-btn--ghost:hover{background:#fff;color:#1B2B99;}' +
      '.cc-btn:focus-visible,.cc-toggle input:focus-visible+span,.cc-floating:focus-visible{outline:3px solid #FF5A1F;outline-offset:3px;}' +
      '.cc-cats{margin-top:20px;display:grid;grid-template-columns:1fr;gap:12px;max-width:900px;}' +
      '@media(min-width:900px){.cc-cats{grid-template-columns:1fr 1fr;}}' +
      '.cc-cat{border:1px solid rgba(255,255,255,.35);padding:18px 20px;display:flex;flex-direction:column;}' +
      '.cc-cat-head{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:10px;}' +
      '.cc-cat-head strong{font-size:.98rem;color:#fff;}' +
      '.cc-cat p{margin:0;font-size:.84rem;line-height:1.55;color:#fff;}' +
      '.cc-always{font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#fff;white-space:nowrap;}' +
      '.cc-toggle{position:relative;display:inline-flex;align-items:center;cursor:pointer;flex-shrink:0;}' +
      '.cc-toggle input{position:absolute;opacity:0;width:1px;height:1px;}' +
      '.cc-toggle span{width:50px;height:28px;border:2px solid #fff;border-radius:999px;position:relative;transition:background .18s ease;}' +
      '.cc-toggle span::after{content:"";position:absolute;top:3px;left:3px;width:18px;height:18px;border-radius:50%;background:#fff;transition:transform .18s ease;}' +
      '.cc-toggle input:checked+span{background:#FF5A1F;border-color:#FF5A1F;}' +
      '.cc-toggle input:checked+span::after{transform:translateX(22px);}' +
      '.cc-floating{position:fixed;left:16px;bottom:16px;z-index:9998;background:#1B2B99;color:#fff;border:2px solid #fff;font-family:var(--body,Inter,sans-serif);font-size:.78rem;font-weight:700;padding:8px 14px;cursor:pointer;}' +
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

  function decide(el, marketing) {
    var before = read();
    write(marketing);
    if (marketing) {
      loadGoogleAds();
      close(el);
    } else {
      revokeGoogleAds();
      close(el);
      // War Google Ads schon geladen, Seite neu laden, damit nichts mehr aktiv ist.
      if (window.__gadsLoaded || (before && before.marketing)) location.reload();
    }
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
        '<h2 class="cc-title" id="cc-title">' + T.title + '</h2>' +
        '<p class="cc-text">' + T.intro + '</p>' +
        '<p class="cc-links"><a href="' + T.privacyHref + '">' + T.privacy + '</a><a href="' + T.imprintHref + '">' + T.imprint + '</a></p>' +
        '<div class="cc-cats" hidden>' +
          '<div class="cc-cat"><div class="cc-cat-head"><strong>' + T.necTitle + '</strong><span class="cc-always">' + T.alwaysOn + '</span></div><p>' + T.necText + '</p></div>' +
          '<div class="cc-cat"><div class="cc-cat-head"><strong>' + T.mktTitle + '</strong>' +
            '<label class="cc-toggle"><input type="checkbox" id="cc-mkt" aria-label="' + T.toggleLabel + '"' + (cur && cur.marketing ? ' checked' : '') + '><span></span></label>' +
          '</div><p>' + T.mktText + '</p></div>' +
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
      if (on) el.querySelector('#cc-mkt').focus();
    }
    el.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cc]');
      if (!b) return;
      var a = b.getAttribute('data-cc');
      if (a === 'all') decide(el, true);
      else if (a === 'necessary') decide(el, false);
      else if (a === 'save') decide(el, el.querySelector('#cc-mkt').checked);
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
    if (c.marketing) loadGoogleAds();
    floating();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
