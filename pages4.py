#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# ============================================================== FAQ ====
faq_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / FAQ</div>
    <span class="eyebrow">Häufige Fragen</span>
    <h1 class="reveal in">Fragen und Antworten.</h1>
    <p class="lead reveal in">Die wichtigsten Fragen zu unserem Vermittlungsprozess, für Arbeitgeber und für Fachkräfte.</p>
  </div>
</section>

<section>
  <div class="wrap">

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Für Einrichtungen & Arbeitgeber</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Wie lange dauert eine Vermittlung von der Anfrage bis zum Arbeitsbeginn?</summary>
        <p>Für Fachkräfte aus unserem bestehenden, bereits vorqualifizierten Pool rechnen wir im Schnitt mit rund 6 Monaten von der Bedarfsanalyse bis zum ersten Arbeitstag. Sprachausbildung und Anerkennungsverfahren laufen parallel und sind bei diesen Kandidat:innen schon weit fortgeschritten oder abgeschlossen.</p>
      </details>
      <details class="faq-item">
        <summary>Was ist der Unterschied zwischen einer Vermittlung aus Ihrem Pool und einer komplett neuen Anwerbung?</summary>
        <p>Bei Kandidat:innen aus unserem Pool sind Sprachkurs und Anerkennung bereits angelaufen, deshalb geht es für Einrichtungen schneller. Wird eine Fachkraft komplett neu angeworben, rechnen wir mit rund 12 bis 13 Monaten von der ersten Bewerbung bis zur Einreise, da Sprachausbildung (6 bis 9 Monate) und Anerkennungsverfahren (je nach Bundesland 6 bis 12 Monate) parallel, aber von null an durchlaufen werden.</p>
      </details>
      <details class="faq-item">
        <summary>Mit welchen Einrichtungen arbeiten Sie bereits zusammen?</summary>
        <p>Wir arbeiten unter anderem mit Sana Kliniken AG, Diakonie, Helios, AWO, DRK und den Main-Kinzig-Kliniken zusammen. Auf Anfrage geben wir gern weitere Referenzen.</p>
      </details>
      <details class="faq-item">
        <summary>Aus welchen Ländern kommen die vermittelten Pflegefachkräfte?</summary>
        <p>Der Schwerpunkt liegt auf den Philippinen und Indien. Wir arbeiten seit 2018 aktiv an der Vermittlung internationaler Pflegefachkräfte aus diesen Regionen.</p>
      </details>
      <details class="faq-item">
        <summary>Ist HPS offiziell zertifiziert?</summary>
        <p>Ja. HPS trägt das RAL-Gütezeichen „Faire Anwerbung Pflege Deutschland“ und ist Mitglied im Bundesverband Internationale Fachkräftegewinnung (bvifg).</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Kosten & faire Anwerbung</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Entstehen für die Einrichtung versteckte Kosten?</summary>
        <p>Nein. Unser Modell ist auf Transparenz ausgelegt. Alle Kosten werden vorab klar kommuniziert, ohne versteckte Positionen.</p>
      </details>
      <details class="faq-item">
        <summary>Welche Kosten kommen konkret auf uns als Einrichtung zu?</summary>
        <p>Die genaue Kostenstruktur hängt vom gewählten Leistungsumfang ab. Wir legen sie Ihnen vor Vertragsabschluss vollständig und schriftlich offen. Eine individuelle Übersicht erstellen wir gern im persönlichen Erstgespräch.</p>
      </details>
      <details class="faq-item">
        <summary>Müssen Fachkräfte für ihre Vermittlung bezahlen?</summary>
        <p>Nein. Es gibt keine versteckten Kosten und keine Rückzahlungsmodelle für die vermittelten Fachkräfte. Das ist fester Bestandteil unseres RAL-zertifizierten Prozesses und Grundlage des Employer-Pays-Prinzips.</p>
      </details>
      <details class="faq-item">
        <summary>Was passiert, wenn eine Vermittlung nicht funktioniert oder eine Fachkraft frühzeitig geht?</summary>
        <p>Unser Prozess sieht eine Ausfallabsicherung vor: Passt es einmal nicht, sorgen wir unkompliziert und ohne zusätzliche Kosten für eine neue Fachkraft. Zusätzlich steht Ihnen gemäß RAL-Gütezeichen ein geregeltes <a href="beschwerdeformular.html" style="color:var(--green-dark);font-weight:600;">Beschwerdeverfahren</a> zur Verfügung.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Für Fachkräfte: Sprache, Anerkennung & Visum</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Muss ich bereits Deutsch sprechen, um mich zu bewerben?</summary>
        <p>Nein. Für die Bewerbung sind noch keine Deutschkenntnisse notwendig. Sie erwerben sie im Rahmen unseres Programms gemeinsam mit unserem Partner Lingoda.</p>
      </details>
      <details class="faq-item">
        <summary>Wie lange dauert es, bis ich das erforderliche B2-Niveau erreiche?</summary>
        <p>Je nach Vorkenntnissen dauert der Sprachkurs in der Regel 6 bis 9 Monate, mit muttersprachlichen Lehrkräften und Zwischenprüfungen auf A2- und B1-Niveau.</p>
      </details>
      <details class="faq-item">
        <summary>Wie läuft die Anerkennung meiner ausländischen Qualifikation ab und wie lange dauert sie?</summary>
        <p>Wir koordinieren Zeugnisbewertung, Defizitbescheid und, falls nötig, eine Anpassungsmaßnahme oder Kenntnisprüfung mit der zuständigen Landesbehörde. Je nach Bundesland dauert dieser Schritt meist 6 bis 12 Monate und läuft parallel zu Ihrem Sprachkurs, sodass sich Ihre Gesamtwartezeit dadurch in der Regel nicht verlängert.</p>
      </details>
      <details class="faq-item">
        <summary>Benötige ich ein Visum, um in Deutschland zu arbeiten?</summary>
        <p>Ja, als Nicht-EU-Bürger:in benötigen Sie ein Arbeitsvisum. Wir begleiten Sie bei der Beantragung und koordinieren alle notwendigen Schritte mit den deutschen Behörden und der zuständigen Auslandsvertretung.</p>
      </details>
      <details class="faq-item">
        <summary>Gibt es eine Altersgrenze für Bewerber:innen?</summary>
        <p>Nein, es gibt keine feste Altersgrenze. Entscheidend sind Ihre abgeschlossene Ausbildung als Pflegefachkraft und Ihre Motivation, in Deutschland zu arbeiten.</p>
      </details>
      <details class="faq-item">
        <summary>Kann ich meine Familie nach Deutschland nachholen?</summary>
        <p>Grundsätzlich ist ein Familiennachzug für anerkannte Fachkräfte nach deutschem Recht möglich. Die genauen Voraussetzungen und Fristen hängen vom Einzelfall ab, wir besprechen das gern persönlich mit Ihnen.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Ankommen & Leben in Deutschland</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Wie wird die Integration nach der Ankunft begleitet?</summary>
        <p>Wir unterstützen bei Wohnungssuche, Behördengängen, Kontoeröffnung, Arztbesuchen sowie interkulturellen Schulungen und Mentoring, auch über den ersten Arbeitstag hinaus.</p>
      </details>
      <details class="faq-item">
        <summary>Wie finde ich eine Unterkunft in Deutschland?</summary>
        <p>Wir unterstützen Sie bei der Wohnungssuche und stimmen uns mit Ihrer künftigen Einrichtung ab, ob bereits eine erste Unterkunft bereitgestellt wird.</p>
      </details>
      <details class="faq-item">
        <summary>Was verdiene ich als Pflegefachkraft in Deutschland?</summary>
        <p>Das Gehalt hängt von Einrichtung, Bundesland und Ihrer Berufserfahrung ab. Eine konkrete Einschätzung für Ihre Situation geben wir Ihnen gern im persönlichen Gespräch.</p>
      </details>
      <details class="faq-item">
        <summary>Was passiert, wenn ich mich nicht wohlfühle oder Unterstützung brauche?</summary>
        <p>Unser Integrationsmanagement steht Ihnen dauerhaft als Ansprechpartner zur Verfügung, telefonisch, persönlich oder digital, auch lange nach dem ersten Arbeitstag.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Rechtliches & Kontakt</h2></div>
    <div class="faq-list reveal">
      <details class="faq-item">
        <summary>An wen kann ich mich wenden, wenn ich eine Beschwerde zum Anwerbungsprozess habe?</summary>
        <p>Als Träger des RAL-Gütezeichens bieten wir Fachkräften und Einrichtungen einen geregelten Weg, Beschwerden einzureichen. Nutzen Sie dazu unser <a href="beschwerdeformular.html" style="color:var(--green-dark);font-weight:600;">Beschwerdeformular</a>.</p>
      </details>
      <details class="faq-item">
        <summary>Wie kann ich einen Termin für ein Erstgespräch vereinbaren?</summary>
        <p>Über unsere <a href="kontakt.html" style="color:var(--green-dark);font-weight:600;">Kontaktseite</a> können Sie direkt einen Termin buchen oder uns eine Nachricht schreiben.</p>
      </details>
    </div>

  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Ihre Frage nicht dabei?</h2>
    <p>Schreiben Sie uns direkt. Wir melden uns persönlich zurück.</p>
    <a href="kontakt.html" class="btn btn-primary">Kontakt aufnehmen</a>
  </div>
</section>
'''
page("faq.html", "FAQ — Heinz Personnel Solutions", "faq.html", faq_body, description="Antworten auf die wichtigsten Fragen zu unserem Vermittlungsprozess, für Arbeitgeber und internationale Pflegefachkräfte.")

# =========================================================== KONTAKT ====
kontakt_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Kontakt</div>
    <span class="eyebrow">Kontakt</span>
    <h1 class="reveal in">Lernen wir uns kennen.</h1>
    <p class="lead reveal in">In einem unverbindlichen Erstgespräch klären wir, ob und wie wir zusammenarbeiten können. Wir freuen uns auf Sie.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2 style="font-size:22px;margin-bottom:18px;">Termin direkt buchen</h2>
      <div class="cal-placeholder">
        <div class="icn">📅</div>
        <h3>Termin online buchen</h3>
        <p>Wählen Sie direkt online einen freien Termin für ein unverbindliches Erstgespräch, ganz ohne Wartezeit auf eine Antwort.</p>
        <a href="https://calendar.app.google/zBSR58vMimhxW8pEA" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:18px;">Termin auswählen</a>
      </div>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:18px;">Oder schreiben Sie uns</h2>
      <div class="form-card">
        <form action="https://formspree.io/f/xwvgzjkz" method="POST">
          <div class="form-two">
            <div class="form-row"><label for="f-name">Name</label><input id="f-name" name="name" type="text" placeholder="Ihr Name" required></div>
            <div class="form-row"><label for="f-email">E-Mail</label><input id="f-email" name="email" type="email" placeholder="ihre@email.de" required></div>
          </div>
          <div class="form-row"><label for="f-org">Einrichtung (optional)</label><input id="f-org" name="einrichtung" type="text" placeholder="Klinik / Pflegeeinrichtung"></div>
          <div class="form-row"><label for="f-msg">Nachricht</label><textarea id="f-msg" name="nachricht" placeholder="Wie können wir helfen?" required></textarea></div>
          <input type="text" name="_gotcha" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="consent-row"><input type="checkbox" id="f-consent" name="einwilligung" required><label for="f-consent">Ich habe die <a href="datenschutz.html" style="color:var(--green-dark);font-weight:600;">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Daten zur Bearbeitung meiner Anfrage einverstanden.</label></div>
          <input type="hidden" name="_subject" value="Neue Kontaktanfrage über die Website">
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Nachricht senden</button>
        </form>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap reveal" style="text-align:center;">
    <h2 style="font-size:20px;margin-bottom:10px;">Direkter Kontakt</h2>
    <p style="margin:0;">Heinz Personnel Solutions GmbH<br><a href="mailto:info@hpstalent.de" style="color:var(--green-dark);font-weight:600;">info@hpstalent.de</a></p>
  </div>
</section>
'''
page("kontakt.html", "Kontakt — Heinz Personnel Solutions", "index.html", kontakt_body, description="Nehmen Sie Kontakt zu Heinz Personnel Solutions auf: unverbindliches Erstgespräch zur internationalen Pflegekräftevermittlung.")

# ========================================================= IMPRESSUM ====
impressum_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Impressum</div>
    <h1 class="reveal in">Impressum</h1>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <h2 style="font-size:18px;margin:26px 0 8px;">Angaben gemäß § 5 TMG</h2>
      <p>Heinz Personnel Solutions GmbH<br>Am Eichenhain 32<br>13465 Berlin</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Vertreten durch</h2>
      <p>Geschäftsführer: Ivo Straßenburg</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Kontakt</h2>
      <p>E-Mail: info@hpstalent.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Registereintrag</h2>
      <p>Handelsregister: HRB 274372 B<br>Registergericht: Amtsgericht Berlin Charlottenburg</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Umsatzsteuer-ID</h2>
      <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz: DE320036514</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
      <p>Ivo Straßenburg<br>Am Eichenhain 32<br>13465 Berlin</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">EU-Streitschlichtung</h2>
      <p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">ec.europa.eu/consumers/odr</a>. Unsere E-Mail-Adresse finden Sie oben im Impressum.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Verbraucherstreitbeilegung / Universalschlichtungsstelle</h2>
      <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Haftung für Inhalte</h2>
      <p>Als Diensteanbieter sind wir gemäß § 7 Abs. 1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Haftung für Links</h2>
      <p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Urheberrecht</h2>
      <p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet und Inhalte Dritter entsprechend gekennzeichnet. Sollten Sie dennoch auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis.</p>
    </div>
  </div>
</section>
'''
page("impressum.html", "Impressum — Heinz Personnel Solutions", "index.html", impressum_body, description="Impressum von Heinz Personnel Solutions GmbH gemäß § 5 TMG.")

# ======================================================= DATENSCHUTZ ====
datenschutz_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Datenschutzerklärung</div>
    <h1 class="reveal in">Datenschutzerklärung</h1>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <h2 style="font-size:18px;margin:26px 0 8px;">1. Verantwortlicher</h2>
      <p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:<br>Heinz Personnel Solutions GmbH, Am Eichenhain 32, 13465 Berlin<br>E-Mail: info@hpstalent.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">2. Allgemeines zur Datenverarbeitung</h2>
      <p>Wir verarbeiten personenbezogene Daten unserer Nutzer:innen grundsätzlich nur, soweit dies zur Bereitstellung einer funktionsfähigen Website sowie unserer Inhalte und Leistungen erforderlich ist. Die Verarbeitung erfolgt regelmäßig nur nach Einwilligung der betroffenen Person (Art. 6 Abs. 1 lit. a DSGVO), zur Erfüllung eines Vertrags oder vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. b DSGVO) oder auf Grundlage unseres berechtigten Interesses an einer sicheren, funktionsfähigen und wirtschaftlichen Bereitstellung unseres Angebots (Art. 6 Abs. 1 lit. f DSGVO).</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">3. Server-Logfiles</h2>
      <p>Beim Aufruf unserer Website erfasst unser Hosting-Provider automatisch Informationen in sogenannten Server-Logfiles, die Ihr Browser automatisch übermittelt, etwa Browsertyp, Betriebssystem, Referrer-URL, Uhrzeit der Serveranfrage und gekürzte IP-Adresse. Diese Daten dienen ausschließlich der Sicherstellung eines störungsfreien Betriebs und der Sicherheit unserer Systeme (Art. 6 Abs. 1 lit. f DSGVO) und werden nicht mit anderen Datenquellen zusammengeführt.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">4. Kontaktformular, Beschwerdeformular & Terminbuchung</h2>
      <p>Wenn Sie uns über das Kontaktformular, das Beschwerdeformular oder die Terminbuchung Anfragen zukommen lassen, verarbeiten wir die von Ihnen dort angegebenen Daten (z. B. Name, E-Mail-Adresse, Nachrichtentext) zur Bearbeitung Ihrer Anfrage. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage vertragsbezogen ist, andernfalls unser berechtigtes Interesse an der Bearbeitung eingehender Anfragen (Art. 6 Abs. 1 lit. f DSGVO). Ihre Daten werden gelöscht, sobald sie für die Bearbeitung nicht mehr erforderlich sind, gesetzliche Aufbewahrungspflichten bleiben unberührt.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">5. Bewerbung über Ankaadia</h2>
      <p>Für Bewerbungen von Pflegefachkräften nutzen wir die Plattform unseres Partners Ankaadia GmbH. Wenn Sie sich über den Bewerbungslink auf unserer Website bewerben, verlassen Sie unsere Seite und geben Ihre Daten direkt in das System von Ankaadia ein. Die dortige Verarbeitung richtet sich nach der Datenschutzerklärung von Ankaadia.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">6. Cookies und Einwilligungsmanagement</h2>
      <p>Unsere Website verwendet, sofern technisch umgesetzt, Cookies und vergleichbare Technologien. Notwendige Cookies, die für den Betrieb der Website erforderlich sind, werden auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO gesetzt. Alle Cookies, die nicht zwingend erforderlich sind (z. B. für Analyse oder Marketing), setzen wir nur nach Ihrer ausdrücklichen Einwilligung über ein Cookie-Consent-Tool (Art. 6 Abs. 1 lit. a DSGVO). Sie können Ihre Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">7. Eingesetzte Dienste Dritter</h2>
      <p>Je nach Einwilligung und technischem Ausbaustand kommen auf dieser Website folgende Dienste externer Anbieter zum Einsatz. Eine Übermittlung findet nur insoweit statt, wie es für den jeweiligen Dienst erforderlich ist:</p>
      <p><b>Google (u. a. Google Analytics, Google Maps, Google Fonts):</b> Anbieter ist Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Google kann Daten auf Servern in den USA verarbeiten. Weitere Informationen: <a href="https://policies.google.com/privacy?hl=de" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">policies.google.com/privacy</a>.</p>
      <p><b>Meta / Facebook:</b> Wir betreiben eine Unternehmensseite bei Facebook und binden ggf. Social-Plugins ein. Anbieter ist Meta Platforms Ireland Limited, 4 Grand Canal Square, Dublin 2, Irland. Weitere Informationen: <a href="https://www.facebook.com/privacy/policy/" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">facebook.com/privacy/policy</a>.</p>
      <p><b>HubSpot:</b> Für Marketing- und Kundenkommunikation kann die Plattform der HubSpot Ireland Limited, One Sir John Rogerson's Quay, Dublin 2, Irland, zum Einsatz kommen, etwa für Formulare und Newsletter-Versand.</p>
      <p><b>Vimeo:</b> Zur Einbindung von Videoinhalten kann der Dienst der Vimeo.com, Inc., New York, USA, genutzt werden. Beim Abspielen eines Videos kann eine Verbindung zu Servern von Vimeo hergestellt werden.</p>
      <p><b>KI-gestützte Anwendungen (z. B. Claude von Anthropic):</b> Wir setzen KI-gestützte Werkzeuge zur Unterstützung interner Arbeitsabläufe ein, etwa bei Text- und Inhaltserstellung. Ein direkter Kontakt eines KI-Tools mit personenbezogenen Besucherdaten dieser Website findet aktuell nicht statt.</p>
      <p><b>Ankaadia:</b> siehe Ziffer 5.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">8. Speicherdauer</h2>
      <p>Wir speichern personenbezogene Daten nur so lange, wie es für den jeweiligen Verarbeitungszweck erforderlich ist, oder solange gesetzliche Aufbewahrungspflichten bestehen, etwa aus dem Handelsgesetzbuch oder der Abgabenordnung.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">9. Ihre Rechte als betroffene Person</h2>
      <p>Sie haben jederzeit das Recht auf Auskunft über die bei uns zu Ihrer Person gespeicherten Daten, auf Berichtigung, Löschung oder Einschränkung der Verarbeitung, auf Widerspruch gegen die Verarbeitung sowie auf Datenübertragbarkeit. Eine bereits erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Wenden Sie sich dazu einfach an info@hpstalent.de.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">10. Beschwerderecht bei der Aufsichtsbehörde</h2>
      <p>Sie haben zudem das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Da unser Unternehmenssitz in Berlin liegt, ist die zuständige Behörde:<br>Berliner Beauftragte für Datenschutz und Informationsfreiheit<br>Alt-Moabit 59–61, 10555 Berlin<br>mailbox@datenschutz-berlin.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">11. Aktualität und Änderung dieser Datenschutzerklärung</h2>
      <p>Diese Datenschutzerklärung ist aktuell gültig. Durch die Weiterentwicklung unserer Website und unseres Angebots oder aufgrund geänderter gesetzlicher Vorgaben kann es notwendig werden, diese Datenschutzerklärung anzupassen.</p>
    </div>
  </div>
</section>
'''
page("datenschutz.html", "Datenschutzerklärung — Heinz Personnel Solutions", "index.html", datenschutz_body, description="Datenschutzerklärung von Heinz Personnel Solutions GmbH gemäß DSGVO.")

# ================================================ BESCHWERDEFORMULAR ====
beschwerde_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Beschwerdeverfahren</div>
    <span class="eyebrow">RAL-Gütezeichen „Faire Anwerbung Pflege“</span>
    <h1 class="reveal in">Beschwerdeformular</h1>
    <p class="lead reveal in">Als Träger des RAL-Gütezeichens „Faire Anwerbung Pflege Deutschland“ bieten wir Fachkräften und Arbeitgebern einen geregelten Weg, Beschwerden zu unserem Vermittlungsprozess einzureichen.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="form-card reveal">
      <form action="https://formspree.io/f/xqerjoee" method="POST">
        <div class="form-two">
          <div class="form-row"><label for="b-name">Name</label><input id="b-name" name="name" type="text" placeholder="Ihr Name" required></div>
          <div class="form-row"><label for="b-email">E-Mail</label><input id="b-email" name="email" type="email" placeholder="ihre@email.de" required></div>
        </div>
        <div class="form-row">
          <label for="b-rolle">Ich melde mich als</label>
          <select id="b-rolle" name="rolle">
            <option>Pflegefachkraft</option>
            <option>Einrichtung / Klinik</option>
            <option>Sonstiges</option>
          </select>
        </div>
        <div class="form-row"><label for="b-betreff">Betreff</label><input id="b-betreff" name="betreff" type="text" placeholder="Worum geht es?" required></div>
        <div class="form-row"><label for="b-text">Beschreibung der Beschwerde</label><textarea id="b-text" name="beschwerde" placeholder="Bitte schildern Sie den Sachverhalt möglichst genau." required></textarea></div>
        <input type="text" name="_gotcha" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="consent-row"><input type="checkbox" id="b-consent" name="einwilligung" required><label for="b-consent">Ich habe die <a href="datenschutz.html" style="color:var(--green-dark);font-weight:600;">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Daten zur Bearbeitung meiner Beschwerde einverstanden.</label></div>
        <input type="hidden" name="_subject" value="Neue Beschwerde über das RAL-Beschwerdeformular">
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Beschwerde einreichen</button>
      </form>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <h2 style="font-size:20px;margin-bottom:14px;">Beschwerdeverfahren</h2>
      <p>Wir möchten, dass alle Beteiligten, Pflegefachkräfte, Arbeitgeber und Partner, jederzeit eine Möglichkeit haben, Anliegen, Probleme oder Beschwerden sicher und unkompliziert mitzuteilen. Dafür haben wir ein transparentes und leicht zugängliches Beschwerdeverfahren eingerichtet.</p>
      <p style="margin-top:14px;">Sie können Beschwerden über folgende Wege einreichen:</p>
      <ul style="margin:10px 0 22px;padding-left:20px;">
        <li style="margin-bottom:6px;">Über das Beschwerdeformular auf dieser Seite</li>
        <li>Per E-Mail an <a href="mailto:complaints@hpstalent.de" style="color:var(--green-dark);font-weight:600;">complaints@hpstalent.de</a></li>
      </ul>

      <h3 style="font-size:17px;margin:26px 0 10px;">Ablauf des Beschwerdeverfahrens</h3>
      <ol style="margin:0 0 20px;padding-left:20px;">
        <li style="margin-bottom:10px;"><b>Eingangsbestätigung:</b> Sie erhalten innerhalb von maximal 5 Werktagen eine Rückmeldung, dass Ihre Beschwerde eingegangen ist.</li>
        <li style="margin-bottom:10px;"><b>Prüfung und Klärung:</b> Unsere zuständige Kontaktperson prüft Ihr Anliegen sorgfältig, nimmt bei Bedarf Rücksprache mit Ihnen und leitet alle notwendigen Schritte ein.</li>
        <li style="margin-bottom:10px;"><b>Abhilfe / Maßnahmen:</b> Wir entwickeln geeignete Lösungen und setzen diese in Abstimmung mit allen Beteiligten um.</li>
        <li><b>Abschluss:</b> Sie erhalten eine schriftliche Rückmeldung über das Ergebnis. Die maximale Bearbeitungsdauer beträgt 3 Wochen.</li>
      </ol>

      <h3 style="font-size:17px;margin:26px 0 10px;">Schutz von Hinweisgebenden</h3>
      <p>Alle Beschwerdeführenden sind gemäß Hinweisgeberschutzgesetz vor Benachteiligung geschützt. Beschwerden können jederzeit ohne Nachteile eingereicht werden.</p>
    </div>
  </div>
</section>
'''
page("beschwerdeformular.html", "Beschwerdeformular — Heinz Personnel Solutions", "index.html", beschwerde_body, description="Beschwerdeformular gemäß RAL-Gütezeichen Faire Anwerbung Pflege Deutschland für Fachkräfte und Einrichtungen.")

# =========================================================== DOWNLOADS ====
downloads_body = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Start</a> / Downloads</div>
    <span class="eyebrow">Alles Wichtige auf einen Blick</span>
    <h1 class="reveal in">Downloads &amp; Dokumente</h1>
    <p class="lead reveal in">Infobroschüren, Vertragsunterlagen und Selbstverpflichtungserklärung, für Ihre Planung und zum Nachlesen.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Dokumente zum Download</h2></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/07/2024_Infobroschuere_DE_fl.pdf" target="_blank" rel="noopener"><div class="rtitle">KDA-Infobroschüre (Deutsch)</div><div class="rdesc">Informationen der RAL-Gütegemeinschaft für Kandidat:innen. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/08/2024_Infobroschuere_EN_fl.pdf" target="_blank" rel="noopener"><div class="rtitle">KDA Info Brochure (English)</div><div class="rdesc">Information from the RAL quality association for candidates. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_Selbstverpflichtungserklarung.pdf" target="_blank" rel="noopener"><div class="rtitle">Selbstverpflichtungserklärung</div><div class="rdesc">Unsere Selbstverpflichtung zur fairen Anwerbung. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_Declaration-of-Commitment.pdf" target="_blank" rel="noopener"><div class="rtitle">Declaration of Commitment</div><div class="rdesc">Our commitment to fair recruitment, in English. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_AGB_2.pdf" target="_blank" rel="noopener"><div class="rtitle">Allgemeine Geschäftsbedingungen</div><div class="rdesc">AGB von Heinz Personnel Solutions. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_GTC_2.pdf" target="_blank" rel="noopener"><div class="rtitle">General Terms and Conditions</div><div class="rdesc">Our terms and conditions, in English. PDF</div></a>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Weiterführende Links</h2></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">RAL-Gütegemeinschaft Faire Anwerbung Pflege</div><div class="rdesc">Offizielle Stelle des RAL-Gütezeichens.</div></a>
      <a class="resource-link" href="https://fair-recruitment-nurse.com/" target="_blank" rel="noopener"><div class="rtitle">fair-recruitment-nurse.com</div><div class="rdesc">Wie Sie zertifizierte, faire Vermittlungsagenturen erkennen.</div></a>
      <a class="resource-link" href="https://www.anerkennung-in-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">Anerkennung in Deutschland</div><div class="rdesc">Portal der Bundesregierung zur Berufsanerkennung.</div></a>
      <a class="resource-link" href="https://www.make-it-in-germany.com/de/" target="_blank" rel="noopener"><div class="rtitle">Make it in Germany</div><div class="rdesc">Portal der Bundesregierung für internationale Fachkräfte.</div></a>
      <a class="resource-link" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="rtitle">Bundesverband Internationale Fachkräftegewinnung</div><div class="rdesc">Bundesweiter Verband für faire Fachkräftegewinnung.</div></a>
      <a class="resource-link" href="https://www.lingoda.com/de/" target="_blank" rel="noopener"><div class="rtitle">Lingoda</div><div class="rdesc">Unser Partner für Online-Sprachunterricht.</div></a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Noch Fragen zu einem Dokument?</h2>
    <p>Schreiben Sie uns. Wir helfen gern weiter.</p>
    <a href="kontakt.html" class="btn btn-primary">Kontakt aufnehmen</a>
  </div>
</section>
'''
page("downloads.html", "Downloads & Dokumente — Heinz Personnel Solutions", "index.html", downloads_body, description="Infobroschüren, AGB und Selbstverpflichtungserklärung von Heinz Personnel Solutions zum Nachlesen und Download.")

print("faq + kontakt + legal + downloads done")
