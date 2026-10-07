/* Heinz Personnel Solutions: Telefonnummer erst nach Klick anzeigen.
   Die Nummer steht absichtlich nicht im Klartext im Code, damit Programme,
   die Websites nach Telefonnummern durchsuchen, sie nicht einsammeln.
   Nummer aendern: Claude bitten, die Liste D neu zu verschluesseln. */
(function () {
  var D = [58, 59, 60, 55, 63, 62, 64, 62, 55, 58, 64, 59];
  function decode() {
    var s = '';
    for (var i = D.length - 1; i >= 0; i--) s += String.fromCharCode(D[i] - 7);
    return s;
  }
  function pretty(d) {
    // Format: +LL NN NNNN NNNN (Berliner Festnetz)
    return '+' + d.slice(0, 2) + ' ' + d.slice(2, 4) + ' ' + d.slice(4, 8) + ' ' + d.slice(8);
  }
  function reveal(btn) {
    var d = decode();
    var a = document.createElement('a');
    a.href = 'tel:+' + d;
    a.className = btn.className + ' is-revealed';
    a.textContent = pretty(d);
    btn.parentNode.replaceChild(a, btn);
    a.focus();
  }
  function init() {
    var btns = document.querySelectorAll('[data-phone-reveal]');
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener('click', function () { reveal(this); });
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
