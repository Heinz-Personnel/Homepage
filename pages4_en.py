#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

# ============================================================== FAQ (EN) ====
faq_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / FAQ</div>
    <span class="eyebrow">Frequently asked questions</span>
    <h1 class="reveal in">Questions and answers.</h1>
    <p class="lead reveal in">The most important questions about our placement process, for employers and for nursing professionals.</p>
  </div>
</section>

<section>
  <div class="wrap">

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">For facilities &amp; employers</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>How long does a placement take, from enquiry to the first day on the job?</summary>
        <p>For professionals from our existing, already pre-qualified pool, we typically plan around 6 months from the needs assessment to the first day on the job. Language training and recognition procedures run in parallel and are, for these candidates, already well advanced or complete.</p>
      </details>
      <details class="faq-item">
        <summary>What's the difference between a placement from your pool and a completely new recruitment?</summary>
        <p>For candidates from our pool, language training and recognition are already under way, so it goes faster for facilities. If a professional is recruited entirely from scratch, we plan around 12 to 13 months from the first application to entry into Germany, since language training (6 to 9 months) and the recognition procedure (6 to 12 months, depending on the state) run in parallel but start from zero.</p>
      </details>
      <details class="faq-item">
        <summary>Which facilities do you already work with?</summary>
        <p>We work with, among others, Sana Kliniken AG, Diakonie, Helios, AWO, DRK, and the Main-Kinzig-Kliniken. On request, we're happy to provide further references.</p>
      </details>
      <details class="faq-item">
        <summary>Which countries do the placed nursing professionals come from?</summary>
        <p>Our focus is on the Philippines and India. We have been actively placing international nursing professionals from these regions since 2018.</p>
      </details>
      <details class="faq-item">
        <summary>Is HPS officially certified?</summary>
        <p>Yes. HPS holds the RAL quality mark "Fair Recruitment in Nursing, Germany" and is a member of the Federal Association for International Skilled Worker Recruitment (bvifg).</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Costs &amp; fair recruitment</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Are there hidden costs for the facility?</summary>
        <p>No. Our model is built for transparency. All costs are clearly communicated in advance, with no hidden items.</p>
      </details>
      <details class="faq-item">
        <summary>What costs does our facility actually need to plan for?</summary>
        <p>The exact cost structure depends on the scope of services chosen. We disclose it to you fully and in writing before any contract is signed. We're happy to prepare an individual overview during a personal first conversation.</p>
      </details>
      <details class="faq-item">
        <summary>Do nursing professionals have to pay for their placement?</summary>
        <p>No. There are no hidden costs and no repayment schemes for placed professionals. That's a fixed part of our RAL-certified process and the foundation of the employer-pays principle.</p>
      </details>
      <details class="faq-item">
        <summary>What happens if a placement doesn't work out, or a professional leaves early?</summary>
        <p>Our process includes fallback cover: if it doesn't work out once, we arrange a new professional without hassle and at no extra cost. In addition, under the RAL quality mark, you have access to a formal <a href="beschwerdeformular-en.html" style="color:var(--green-dark);font-weight:600;">complaints procedure</a>.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">For professionals: language, recognition &amp; visa</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>Do I need to already speak German to apply?</summary>
        <p>No. No German language skills are required to apply. You'll acquire them as part of our programme, together with our partner Lingoda.</p>
      </details>
      <details class="faq-item">
        <summary>How long does it take to reach the required B2 level?</summary>
        <p>Depending on your prior knowledge, the language course usually takes 6 to 9 months, with native-speaking teachers and interim exams at A2 and B1 level.</p>
      </details>
      <details class="faq-item">
        <summary>How does the recognition of my foreign qualification work, and how long does it take?</summary>
        <p>We coordinate the credential evaluation, the deficiency notice and, if needed, an adaptation measure or knowledge test with the responsible state authority. Depending on the state, this step usually takes 6 to 12 months and runs in parallel with your language course, so your overall waiting time typically doesn't get any longer as a result.</p>
      </details>
      <details class="faq-item">
        <summary>Do I need a visa to work in Germany?</summary>
        <p>Yes, as a non-EU citizen you need a work visa. We support you through the application and coordinate all the necessary steps with the German authorities and the relevant diplomatic mission.</p>
      </details>
      <details class="faq-item">
        <summary>Is there an age limit for applicants?</summary>
        <p>No, there is no fixed age limit. What matters is your completed training as a nursing professional and your motivation to work in Germany.</p>
      </details>
      <details class="faq-item">
        <summary>Can I bring my family to Germany?</summary>
        <p>In principle, family reunification is possible for recognised professionals under German law. The exact requirements and timelines depend on your individual case, we're happy to discuss this with you personally.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Arriving &amp; living in Germany</h2></div>
    <div class="faq-list reveal" style="margin-bottom:44px;">
      <details class="faq-item">
        <summary>How is integration supported after arrival?</summary>
        <p>We support you with finding housing, official registrations, opening a bank account, doctor's visits, as well as intercultural training and mentoring, well beyond your first day on the job.</p>
      </details>
      <details class="faq-item">
        <summary>How do I find accommodation in Germany?</summary>
        <p>We support you in finding housing and coordinate with your future facility on whether initial accommodation is already being provided.</p>
      </details>
      <details class="faq-item">
        <summary>What will I earn as a nursing professional in Germany?</summary>
        <p>Salary depends on the facility, the state, and your professional experience. We're happy to give you a concrete assessment for your situation in a personal conversation.</p>
      </details>
      <details class="faq-item">
        <summary>What happens if I don't feel comfortable or need support?</summary>
        <p>Our integration management is available to you permanently as a point of contact, by phone, in person or digitally, well beyond your first day on the job.</p>
      </details>
    </div>

    <div class="section-head reveal" style="max-width:760px;margin-left:auto;margin-right:auto;"><h2 style="font-size:20px;">Legal &amp; contact</h2></div>
    <div class="faq-list reveal">
      <details class="faq-item">
        <summary>Who can I contact if I have a complaint about the recruitment process?</summary>
        <p>As a holder of the RAL quality mark, we offer both professionals and facilities a formal way to submit complaints. Please use our <a href="beschwerdeformular-en.html" style="color:var(--green-dark);font-weight:600;">complaints form</a>.</p>
      </details>
      <details class="faq-item">
        <summary>How can I schedule a first conversation?</summary>
        <p>Via our <a href="kontakt-en.html" style="color:var(--green-dark);font-weight:600;">contact page</a>, you can book a time slot directly or send us a message.</p>
      </details>
    </div>

  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Didn't find your question?</h2>
    <p>Write to us directly. We'll get back to you personally.</p>
    <a href="kontakt-en.html" class="btn btn-primary">Get in touch</a>
  </div>
</section>
'''
page("faq-en.html", "FAQ — Heinz Personnel Solutions", "faq.html", faq_body_en, description="Answers to the most important questions about our placement process, for employers and international nursing professionals.")

# =========================================================== CONTACT (EN) ====
kontakt_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Contact</div>
    <span class="eyebrow">Contact</span>
    <h1 class="reveal in">Let's get to know each other.</h1>
    <p class="lead reveal in">In a free, no-obligation first conversation, we'll find out whether and how we can work together. We look forward to hearing from you.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2 style="font-size:22px;margin-bottom:18px;">Book a time directly</h2>
      <div class="cal-placeholder">
        <div class="icn">📅</div>
        <h3>Book a time online</h3>
        <p>Pick a free slot directly online for a no-obligation first conversation, no waiting for a reply.</p>
        <a href="https://calendar.app.google/zBSR58vMimhxW8pEA" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:18px;">Choose a time</a>
      </div>
    </div>
    <div class="reveal" style="transition-delay:.08s">
      <h2 style="font-size:22px;margin-bottom:18px;">Or write to us</h2>
      <div class="form-card">
        <form action="https://formspree.io/f/xwvgzjkz" method="POST">
          <div class="form-two">
            <div class="form-row"><label for="f-name">Name</label><input id="f-name" name="name" type="text" placeholder="Your name" required></div>
            <div class="form-row"><label for="f-email">Email</label><input id="f-email" name="email" type="email" placeholder="your@email.com" required></div>
          </div>
          <div class="form-row"><label for="f-org">Facility (optional)</label><input id="f-org" name="einrichtung" type="text" placeholder="Hospital / care facility"></div>
          <div class="form-row"><label for="f-msg">Message</label><textarea id="f-msg" name="nachricht" placeholder="How can we help?" required></textarea></div>
          <input type="text" name="_gotcha" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="consent-row"><input type="checkbox" id="f-consent" name="einwilligung" required><label for="f-consent">I have read the <a href="datenschutz-en.html" style="color:var(--green-dark);font-weight:600;">privacy policy</a> and agree to my data being processed to handle my enquiry.</label></div>
          <input type="hidden" name="_subject" value="New contact enquiry via the website (EN)">
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Send message</button>
        </form>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap reveal" style="text-align:center;">
    <h2 style="font-size:20px;margin-bottom:10px;">Direct contact</h2>
    <p style="margin:0;">Heinz Personnel Solutions GmbH<br><a href="mailto:info@hpstalent.de" style="color:var(--green-dark);font-weight:600;">info@hpstalent.de</a></p>
  </div>
</section>
'''
page("kontakt-en.html", "Contact — Heinz Personnel Solutions", "index.html", kontakt_body_en, description="Get in touch with Heinz Personnel Solutions for a free, no-obligation first conversation about international nursing recruitment.")

# ========================================================= LEGAL NOTICE (EN) ====
impressum_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Legal Notice</div>
    <h1 class="reveal in">Legal Notice (Impressum)</h1>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <p style="font-size:13.5px;color:var(--ink-mute);border-left:3px solid var(--border);padding-left:14px;">This page is a courtesy translation for your convenience. The German-language version of this Legal Notice is legally binding.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Information pursuant to Section 5 TMG</h2>
      <p>Heinz Personnel Solutions GmbH<br>Am Eichenhain 32<br>13465 Berlin, Germany</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Represented by</h2>
      <p>Managing Director: Ivo Straßenburg</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Contact</h2>
      <p>Email: info@hpstalent.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Register entry</h2>
      <p>Commercial register: HRB 274372 B<br>Register court: Amtsgericht Berlin Charlottenburg (Berlin Charlottenburg Local Court)</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">VAT ID</h2>
      <p>VAT identification number pursuant to Section 27a of the German VAT Act: DE320036514</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Responsible for content pursuant to Section 18(2) MStV</h2>
      <p>Ivo Straßenburg<br>Am Eichenhain 32<br>13465 Berlin, Germany</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">EU dispute resolution</h2>
      <p>The European Commission provides a platform for online dispute resolution (ODR): <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">ec.europa.eu/consumers/odr</a>. Our email address is listed above.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Consumer dispute resolution</h2>
      <p>We are not willing or obliged to participate in dispute resolution proceedings before a consumer arbitration board.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Liability for content</h2>
      <p>As a service provider, we are responsible for our own content on these pages in accordance with Section 7(1) TMG under general law. However, under Sections 8 to 10 TMG, we as a service provider are not obliged to monitor transmitted or stored third-party information, or to investigate circumstances that indicate unlawful activity. Obligations to remove or block the use of information under general law remain unaffected. Liability in this regard is only possible from the point in time at which a specific infringement becomes known. Upon becoming aware of any such infringements, we will remove the relevant content immediately.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Liability for links</h2>
      <p>Our website contains links to external third-party websites, over whose content we have no control. We therefore cannot accept any liability for this external content. The respective provider or operator of the linked pages is always responsible for their content. The linked pages were checked for possible legal violations at the time of linking. Permanent monitoring of the linked pages' content is not reasonable without concrete evidence of a violation. Upon becoming aware of any legal violations, we will remove such links immediately.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">Copyright</h2>
      <p>The content and works created by the site operators on these pages are subject to German copyright law. Duplication, editing, distribution and any kind of use outside the limits of copyright law require the written consent of the respective author or creator. Insofar as the content on this page was not created by the operator, the copyrights of third parties are respected and third-party content is marked accordingly. Should you nevertheless become aware of a copyright infringement, please let us know.</p>
    </div>
  </div>
</section>
'''
page("impressum-en.html", "Legal Notice — Heinz Personnel Solutions", "index.html", impressum_body_en, description="Legal notice (Impressum) of Heinz Personnel Solutions GmbH pursuant to Section 5 TMG.")

# ======================================================= PRIVACY POLICY (EN) ====
datenschutz_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Privacy Policy</div>
    <h1 class="reveal in">Privacy Policy</h1>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <p style="font-size:13.5px;color:var(--ink-mute);border-left:3px solid var(--border);padding-left:14px;">This page is a courtesy translation for your convenience. The German-language Datenschutzerklärung is the legally binding version.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">1. Controller</h2>
      <p>The controller responsible for data processing on this website is:<br>Heinz Personnel Solutions GmbH, Am Eichenhain 32, 13465 Berlin, Germany<br>Email: info@hpstalent.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">2. General information on data processing</h2>
      <p>We process personal data of our users only to the extent necessary to provide a functional website along with our content and services. Processing generally takes place only with the data subject's consent (Art. 6(1)(a) GDPR), for the performance of a contract or pre-contractual measures (Art. 6(1)(b) GDPR), or on the basis of our legitimate interest in a secure, functional and economical operation of our services (Art. 6(1)(f) GDPR).</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">3. Server log files</h2>
      <p>When you visit our website, our hosting provider automatically collects information in what are known as server log files, which your browser transmits automatically, such as browser type, operating system, referrer URL, time of the server request, and a truncated IP address. This data is used exclusively to ensure smooth operation and the security of our systems (Art. 6(1)(f) GDPR) and is not combined with other data sources.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">4. Contact form, complaints form &amp; appointment booking</h2>
      <p>If you contact us via the contact form, the complaints form, or the appointment booking tool, we process the data you provide there (e.g. name, email address, message text) to handle your request. The legal basis is Art. 6(1)(b) GDPR where your enquiry relates to a contract, otherwise our legitimate interest in processing incoming enquiries (Art. 6(1)(f) GDPR). Your data will be deleted once it is no longer required for processing, statutory retention obligations remain unaffected.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">5. Application via Ankaadia</h2>
      <p>For applications from nursing professionals, we use the platform of our partner Ankaadia GmbH. If you apply via the application link on our website, you leave our site and enter your data directly into Ankaadia's system. Processing there is governed by Ankaadia's own privacy policy.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">6. Cookies and consent management</h2>
      <p>Where technically implemented, our website uses cookies and comparable technologies. Necessary cookies, required for the operation of the website, are set on the basis of Art. 6(1)(f) GDPR. Any cookies that are not strictly necessary (e.g. for analytics or marketing) are only set with your express consent via a cookie consent tool (Art. 6(1)(a) GDPR). You may withdraw your consent at any time with effect for the future.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">7. Third-party services used</h2>
      <p>Depending on consent given and technical implementation, the following third-party services may be used on this website. Data is only transferred to the extent required for the respective service:</p>
      <p><b>Google (including Google Analytics, Google Maps, Google Fonts):</b> Provider is Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland. Google may process data on servers in the USA. More information: <a href="https://policies.google.com/privacy?hl=en" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">policies.google.com/privacy</a>.</p>
      <p><b>Meta / Facebook:</b> We operate a business page on Facebook and may embed social plugins. Provider is Meta Platforms Ireland Limited, 4 Grand Canal Square, Dublin 2, Ireland. More information: <a href="https://www.facebook.com/privacy/policy/" target="_blank" rel="noopener" style="color:var(--green-dark);font-weight:600;">facebook.com/privacy/policy</a>.</p>
      <p><b>HubSpot:</b> For marketing and customer communication, we may use the platform of HubSpot Ireland Limited, One Sir John Rogerson's Quay, Dublin 2, Ireland, for example for forms and newsletter delivery.</p>
      <p><b>Vimeo:</b> To embed video content, we may use the service of Vimeo.com, Inc., New York, USA. Playing a video may establish a connection to Vimeo's servers.</p>
      <p><b>AI-assisted tools (e.g. Claude by Anthropic):</b> We use AI-assisted tools to support internal workflows, such as content and text creation. There is currently no direct contact between any AI tool and personal visitor data of this website.</p>
      <p><b>Ankaadia:</b> see section 5.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">8. Retention period</h2>
      <p>We store personal data only for as long as necessary for the respective processing purpose, or as long as statutory retention obligations apply, for example under German commercial or tax law.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">9. Your rights as a data subject</h2>
      <p>You have the right at any time to obtain information about the personal data we hold about you, to have it corrected, deleted, or its processing restricted, to object to processing, and to data portability. You may withdraw any consent already given at any time with effect for the future. Simply contact us at info@hpstalent.de.</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">10. Right to lodge a complaint with a supervisory authority</h2>
      <p>You also have the right to lodge a complaint with a data protection supervisory authority. As our company is based in Berlin, the competent authority is:<br>Berlin Commissioner for Data Protection and Freedom of Information (Berliner Beauftragte für Datenschutz und Informationsfreiheit)<br>Alt-Moabit 59–61, 10555 Berlin, Germany<br>mailbox@datenschutz-berlin.de</p>

      <h2 style="font-size:18px;margin:26px 0 8px;">11. Currency and amendment of this privacy policy</h2>
      <p>This privacy policy is currently valid. Due to the ongoing development of our website and our services, or due to changes in legal requirements, it may become necessary to amend this privacy policy.</p>
    </div>
  </div>
</section>
'''
page("datenschutz-en.html", "Privacy Policy — Heinz Personnel Solutions", "index.html", datenschutz_body_en, description="Privacy policy of Heinz Personnel Solutions GmbH pursuant to the GDPR.")

# ================================================ COMPLAINTS FORM (EN) ====
beschwerde_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Complaints Procedure</div>
    <span class="eyebrow">RAL quality mark "Fair Recruitment in Nursing"</span>
    <h1 class="reveal in">Complaints form</h1>
    <p class="lead reveal in">As a holder of the RAL quality mark "Fair Recruitment in Nursing, Germany", we offer nursing professionals and employers a formal way to submit complaints about our placement process.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="form-card reveal">
      <form action="https://formspree.io/f/xqerjoee" method="POST">
        <div class="form-two">
          <div class="form-row"><label for="b-name">Name</label><input id="b-name" name="name" type="text" placeholder="Your name" required></div>
          <div class="form-row"><label for="b-email">Email</label><input id="b-email" name="email" type="email" placeholder="your@email.com" required></div>
        </div>
        <div class="form-row">
          <label for="b-rolle">I am submitting this as</label>
          <select id="b-rolle" name="rolle">
            <option>Nursing professional</option>
            <option>Facility / hospital</option>
            <option>Other</option>
          </select>
        </div>
        <div class="form-row"><label for="b-betreff">Subject</label><input id="b-betreff" name="betreff" type="text" placeholder="What is this about?" required></div>
        <div class="form-row"><label for="b-text">Description of the complaint</label><textarea id="b-text" name="beschwerde" placeholder="Please describe the situation as precisely as possible." required></textarea></div>
        <input type="text" name="_gotcha" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="consent-row"><input type="checkbox" id="b-consent" name="einwilligung" required><label for="b-consent">I have read the <a href="datenschutz-en.html" style="color:var(--green-dark);font-weight:600;">privacy policy</a> and agree to my data being processed to handle my complaint.</label></div>
        <input type="hidden" name="_subject" value="New complaint via the RAL complaints form (EN)">
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Submit complaint</button>
      </form>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap" style="max-width:720px;">
    <div class="reveal">
      <h2 style="font-size:20px;margin-bottom:14px;">Complaints procedure</h2>
      <p>We want everyone involved, nursing professionals, employers and partners, to always have a safe and straightforward way to raise concerns, problems or complaints. That's why we have set up a transparent and easily accessible complaints procedure.</p>
      <p style="margin-top:14px;">You can submit a complaint through the following channels:</p>
      <ul style="margin:10px 0 22px;padding-left:20px;">
        <li style="margin-bottom:6px;">Via the complaints form on this page</li>
        <li>By email to <a href="mailto:complaints@hpstalent.de" style="color:var(--green-dark);font-weight:600;">complaints@hpstalent.de</a></li>
      </ul>

      <h3 style="font-size:17px;margin:26px 0 10px;">How the complaints procedure works</h3>
      <ol style="margin:0 0 20px;padding-left:20px;">
        <li style="margin-bottom:10px;"><b>Acknowledgement of receipt:</b> You will receive confirmation that your complaint has been received within a maximum of 5 working days.</li>
        <li style="margin-bottom:10px;"><b>Review and clarification:</b> Our responsible contact person carefully reviews your concern, consults with you if needed, and initiates any necessary steps.</li>
        <li style="margin-bottom:10px;"><b>Remedy / measures:</b> We develop suitable solutions and implement them in coordination with everyone involved.</li>
        <li><b>Resolution:</b> You will receive written feedback on the outcome. The maximum processing time is 3 weeks.</li>
      </ol>

      <h3 style="font-size:17px;margin:26px 0 10px;">Protection for whistleblowers</h3>
      <p>All complainants are protected against disadvantage under the German Whistleblower Protection Act (Hinweisgeberschutzgesetz). Complaints can be submitted at any time without any negative consequences.</p>
    </div>
  </div>
</section>
'''
page("beschwerdeformular-en.html", "Complaints Form — Heinz Personnel Solutions", "index.html", beschwerde_body_en, description="Complaints form under the RAL quality mark Fair Recruitment in Nursing, Germany, for professionals and facilities.")

# =========================================================== DOWNLOADS (EN) ====
downloads_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / Downloads</div>
    <span class="eyebrow">Everything important at a glance</span>
    <h1 class="reveal in">Downloads &amp; documents</h1>
    <p class="lead reveal in">Info brochures, contract documents and our commitment declaration, for your planning and to read.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Documents to download</h2></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/07/2024_Infobroschuere_DE_fl.pdf" target="_blank" rel="noopener"><div class="rtitle">KDA info brochure (German)</div><div class="rdesc">Information from the RAL quality association for candidates. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/08/2024_Infobroschuere_EN_fl.pdf" target="_blank" rel="noopener"><div class="rtitle">KDA info brochure (English)</div><div class="rdesc">Information from the RAL quality association for candidates. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_Selbstverpflichtungserklarung.pdf" target="_blank" rel="noopener"><div class="rtitle">Commitment declaration (German)</div><div class="rdesc">Our commitment to fair recruitment. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_Declaration-of-Commitment.pdf" target="_blank" rel="noopener"><div class="rtitle">Declaration of Commitment (English)</div><div class="rdesc">Our commitment to fair recruitment, in English. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_AGB_2.pdf" target="_blank" rel="noopener"><div class="rtitle">Terms and conditions (German)</div><div class="rdesc">Terms and conditions of Heinz Personnel Solutions. PDF</div></a>
      <a class="resource-link" href="https://pflegekraftvermittlung.com/wp-content/uploads/2025/11/2511_HPS_GTC_2.pdf" target="_blank" rel="noopener"><div class="rtitle">General Terms and Conditions (English)</div><div class="rdesc">Our terms and conditions, in English. PDF</div></a>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Further links</h2></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">RAL Quality Association Fair Recruitment in Nursing</div><div class="rdesc">The official body behind the RAL quality mark.</div></a>
      <a class="resource-link" href="https://fair-recruitment-nurse.com/" target="_blank" rel="noopener"><div class="rtitle">fair-recruitment-nurse.com</div><div class="rdesc">How to recognise certified, fair recruitment agencies.</div></a>
      <a class="resource-link" href="https://www.anerkennung-in-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">Recognition in Germany</div><div class="rdesc">The German government's portal on professional recognition.</div></a>
      <a class="resource-link" href="https://www.make-it-in-germany.com/en/" target="_blank" rel="noopener"><div class="rtitle">Make it in Germany</div><div class="rdesc">The German government's portal for international professionals.</div></a>
      <a class="resource-link" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="rtitle">Federal Association for International Skilled Worker Recruitment</div><div class="rdesc">National association for fair skilled worker recruitment.</div></a>
      <a class="resource-link" href="https://www.lingoda.com/en/" target="_blank" rel="noopener"><div class="rtitle">Lingoda</div><div class="rdesc">Our partner for online language teaching.</div></a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Questions about a document?</h2>
    <p>Write to us. We're happy to help.</p>
    <a href="kontakt-en.html" class="btn btn-primary">Get in touch</a>
  </div>
</section>
'''
page("downloads-en.html", "Downloads & Documents — Heinz Personnel Solutions", "index.html", downloads_body_en, description="Info brochures, terms and conditions, and the commitment declaration of Heinz Personnel Solutions to read and download.")

print("faq-en + kontakt-en + legal-en + downloads-en done")
