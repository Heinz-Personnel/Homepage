/* Heinz Personnel Solutions: Google Ads Conversion-Tracking (nur mit Einwilligung).
   Stand: Oktober 2026.
   Meldet zwei Conversions an Google Ads, aber nur, wenn die Besucherin oder der Besucher
   im Einwilligungsbanner "Marketing" erlaubt hat (siehe js/cookie-consent.js):
   - "Kontaktformular gesendet": nach erfolgreichem Absenden des Kontaktformulars (Formspree).
   - "Terminbuchung geklickt": Klick auf den Link zur Online-Terminbuchung (Google Kalender).
   Ohne Einwilligung wird nichts gemessen; das Formular funktioniert trotzdem ganz normal.
   Das Kontaktformular wird im Hintergrund an Formspree geschickt, damit die Besucherin oder
   der Besucher auf unserer Seite bleibt und eine Bestätigung sieht. Klappt das nicht,
   wird das Formular wie bisher klassisch abgeschickt. */
(function () {
  var SEND_TO = {
    lead: 'AW-18457911738/usTaCLPe1JYdELrDteFE',    // Kontaktformular gesendet
    booking: 'AW-18457911738/EH2oCLbe1JYdELrDteFE'  // Terminbuchung geklickt
  };
  var lang = document.documentElement.lang === 'en' ? 'en' : 'de';
  var TXT = {
    de: {
      title: 'Danke für Ihre Nachricht',
      text: 'Ihre Nachricht ist bei uns angekommen. Wir melden uns persönlich bei Ihnen.',
      sending: 'Wird gesendet …'
    },
    en: {
      title: 'Thank you for your message',
      text: 'Your message has reached us. We will get back to you personally.',
      sending: 'Sending …'
    }
  }[lang];

  function marketingAllowed() {
    return !!(window.__gtagLoaded && window.__gtagLoaded.marketing && typeof window.gtag === 'function');
  }

  /* Conversion senden. cb wird immer aufgerufen (spätestens nach 1 Sekunde). */
  function fire(key, cb) {
    var called = false;
    function done() { if (!called) { called = true; if (cb) cb(); } }
    if (!marketingAllowed()) { done(); return; }
    try {
      window.gtag('event', 'conversion', {
        send_to: SEND_TO[key],
        transport_type: 'beacon',
        event_callback: done
      });
      if (key === 'lead' && window.__gtagLoaded.stats) window.gtag('event', 'generate_lead');
    } catch (e) {}
    setTimeout(done, 1000);
  }
  window.heinzConversion = fire;

  /* Klick auf Online-Terminbuchung */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="calendar.app.google"]');
    if (a) fire('booking');
  });

  /* Kontaktformular: im Hintergrund senden, Bestätigung anzeigen, Conversion melden */
  function success(form) {
    var box = document.createElement('div');
    box.className = 'form-card form-success';
    box.setAttribute('role', 'status');
    box.setAttribute('tabindex', '-1');
    var h = document.createElement('h3');
    h.textContent = TXT.title;
    var p = document.createElement('p');
    p.textContent = TXT.text;
    box.appendChild(h);
    box.appendChild(p);
    form.parentNode.replaceChild(box, form);
    box.focus();
  }

  function init() {
    if (!window.fetch || !window.FormData) return;
    var forms = document.querySelectorAll('form[data-conversion="lead"]');
    Array.prototype.forEach.call(forms, function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var btn = form.querySelector('[type="submit"]');
        var label = btn ? btn.textContent : '';
        if (btn) { btn.disabled = true; btn.textContent = TXT.sending; }
        fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' }
        }).then(function (r) {
          if (!r.ok) throw new Error('status ' + r.status);
          fire('lead');
          success(form);
        }).catch(function () {
          // Rückfall: klassisch absenden (ohne Messung), damit keine Anfrage verloren geht.
          if (btn) { btn.disabled = false; btn.textContent = label; }
          HTMLFormElement.prototype.submit.call(form);
        });
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
