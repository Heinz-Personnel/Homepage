/* Heinz Personnel Solutions – Cookie-Consent (Google Ads Conversion-Tracking)
   Lädt das Google-Tag (AW-18457911738) erst nach ausdrücklicher Einwilligung. */
(function () {
  var GADS_ID = 'AW-18457911738';
  var CONSENT_KEY = 'heinz_cookie_consent';
  var lang = document.documentElement.lang === 'en' ? 'en' : 'de';

  var texts = {
    de: {
      message: 'Wir verwenden Cookies für das Google Ads Conversion-Tracking, um zu sehen, welche Anzeigen zu einer Kontaktaufnahme führen. Diese Cookies setzen wir nur mit Ihrer Einwilligung.',
      accept: 'Akzeptieren',
      decline: 'Ablehnen',
      settings: 'Cookie-Einstellungen',
      privacy: 'Datenschutzerklärung',
      privacyHref: 'datenschutz.html'
    },
    en: {
      message: 'We use cookies for Google Ads conversion tracking, to see which ads lead to a contact request. We only set these cookies with your consent.',
      accept: 'Accept',
      decline: 'Decline',
      settings: 'Cookie settings',
      privacy: 'Privacy Policy',
      privacyHref: 'datenschutz-en.html'
    }
  };
  var t = texts[lang];

  function getConsent() {
    try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
  }
  function setConsent(v) {
    try { localStorage.setItem(CONSENT_KEY, v); } catch (e) {}
  }

  function loadGoogleAds() {
    if (window.__gadsLoaded) return;
    window.__gadsLoaded = true;
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GADS_ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GADS_ID;
    document.head.appendChild(s);
  }

  function injectStyles() {
    if (document.getElementById('cc-styles')) return;
    var css =
      '.cc-banner{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:var(--hbo-dunkel,#1B2B99);color:#fff;padding:20px 24px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;font-family:var(--body,Inter,sans-serif);box-shadow:0 -4px 24px rgba(0,0,0,.25);}' +
      '.cc-banner p{margin:0;flex:1 1 320px;font-size:14px;line-height:1.6;}' +
      '.cc-banner a{color:#fff;text-decoration:underline;}' +
      '.cc-actions{display:flex;gap:10px;flex-wrap:wrap;}' +
      '.cc-btn{border:1px solid #fff;background:transparent;color:#fff;padding:11px 22px;border-radius:4px;font-size:14px;cursor:pointer;font-family:inherit;}' +
      '.cc-btn--accept{background:#FF5A1F;border-color:#FF5A1F;color:#0B0B0B;font-weight:600;}' +
      '.cc-settings-link{position:fixed;left:16px;bottom:16px;z-index:9998;background:rgba(11,11,11,.72);color:#fff;font-size:12px;padding:6px 12px;border-radius:4px;text-decoration:none;font-family:var(--body,Inter,sans-serif);}' +
      '@media (max-width:640px){.cc-banner{padding:16px;}.cc-actions{width:100%;}.cc-btn{flex:1;}}';
    var style = document.createElement('style');
    style.id = 'cc-styles';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function showSettingsLink() {
    if (document.getElementById('cc-settings-link')) return;
    var a = document.createElement('a');
    a.id = 'cc-settings-link';
    a.href = '#';
    a.className = 'cc-settings-link';
    a.textContent = t.settings;
    a.addEventListener('click', function (e) {
      e.preventDefault();
      showBanner();
    });
    document.body.appendChild(a);
  }

  function showBanner() {
    injectStyles();
    var existing = document.getElementById('cc-banner');
    if (existing) existing.remove();
    var el = document.createElement('div');
    el.id = 'cc-banner';
    el.className = 'cc-banner';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Cookie-Hinweis');
    el.innerHTML =
      '<p>' + t.message + ' <a href="' + t.privacyHref + '">' + t.privacy + '</a></p>' +
      '<div class="cc-actions">' +
      '<button type="button" class="cc-btn cc-btn--decline">' + t.decline + '</button>' +
      '<button type="button" class="cc-btn cc-btn--accept">' + t.accept + '</button>' +
      '</div>';
    document.body.appendChild(el);
    el.querySelector('.cc-btn--accept').addEventListener('click', function () {
      setConsent('accepted');
      loadGoogleAds();
      el.remove();
      showSettingsLink();
    });
    el.querySelector('.cc-btn--decline').addEventListener('click', function () {
      setConsent('declined');
      el.remove();
      showSettingsLink();
    });
  }

  function init() {
    var consent = getConsent();
    if (consent === 'accepted') {
      loadGoogleAds();
      showSettingsLink();
    } else if (consent === 'declined') {
      showSettingsLink();
    } else {
      showBanner();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
