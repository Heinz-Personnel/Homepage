#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gen import page

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

# ============================================= FOR EMPLOYERS (EN) ====
einrichtungen_body_en = '''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / For Employers</div>
    <span class="eyebrow">For hospitals &amp; care facilities</span>
    <h1 class="reveal in">Staffing that stays.</h1>
    <p class="lead reveal in">To us, a placement isn't successful once a contract is signed. It's successful when your professional is still on the team years later.</p>
    <div class="hero-proof-strip reveal">
      <div class="hero-proof-stat"><div class="num">92%</div><div class="lbl">stay longer than three years</div></div>
      <div class="hero-proof-stat"><div class="num">400+</div><div class="lbl">professionals successfully placed</div></div>
      <div class="hero-proof-stat"><div class="num">98%</div><div class="lbl">successful professional recognitions</div></div>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="wrap">
    <span class="badge"><img src="logo-ral-guetezeichen.svg" alt="RAL quality mark for fair recruitment in nursing, Germany" style="height:100px"></span>
    <span class="badge"><img src="logo-bvifg.png" alt="Member of the Federal Association for International Skilled Worker Recruitment" style="height:74px"></span>
    <span class="badge"><img src="logo-gapa.png" alt="GAPA quality association for fair recruitment of nursing professionals from abroad" style="height:96px"></span>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="problem reveal">
      <h2>Filling open positions, sustainably.</h2>
      <p>Qualified nursing professionals are in short supply in many places. Demand is growing noticeably faster than the German labour market can cover on its own. For HR decision-makers, that means unfilled shifts, ongoing strain on the team, and the worry that a quick fix won't hold up long term.</p>
      <p>Fair recruitment is the standard today, the RAL quality mark and bvifg membership prove that. What actually matters is something else: whether a professional is still there after years. That's exactly what our process is built for. If it doesn't work out once, we arrange a replacement without hassle and at no extra cost.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Why HPS instead of temp staffing or social media recruiting?</h2></div>
    <div class="split">
      <div class="win-card reveal">
        <h3>Temp staffing</h3>
        <p>Solves acute shortages in the short term, but without lasting attachment to the team. High turnover, recurring effort, no integration into the facility.</p>
      </div>
      <div class="win-card reveal" style="transition-delay:.08s">
        <h3>Social media recruiting</h3>
        <p>Reaches many applicants, but without a structured recognition and integration process. The risk of a mismatch stays with the facility.</p>
      </div>
    </div>
    <div class="win-card featured reveal" style="margin-top:22px;">
      <h3>Our approach</h3>
      <p>Experienced international nursing professionals, supported from first contact to well beyond the first day on the job. The result: 92% of our placed professionals stay longer than three years.</p>
    </div>
  </div>
</section>

<section id="prozess">
  <div class="wrap">
    <div class="section-head reveal"><h2>Our process in detail</h2><p style="font-size:15.5px;margin-top:10px;">A path you can follow: from the first needs assessment to long-term integration.</p></div>
  </div>
  <div class="route-wrap" id="route">
    <svg class="route-svg" id="routeSvg" viewBox="0 0 100 800" preserveAspectRatio="none">
      <path id="routePath" d="M50,0 C20,50 20,90 50,120 C80,150 80,190 50,220 C20,250 20,300 50,330 C80,360 80,400 50,430 C20,460 20,510 50,540 C60,560 60,590 50,620"/>
    </svg>
    <div class="waypoint right reveal">
      <span class="tag">Stage 1</span><h3>Needs assessment</h3>
      <p>We talk with you personally to understand exactly who fits your facility.</p>
      <span class="time">Day 1</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Stage 2</span><h3>Matching from our pool</h3>
      <p>We propose suitable candidates from our existing, already pre-qualified pool. No starting from zero.</p>
      <span class="time">From week 2</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Stage 3</span><h3>Recognition &amp; visa</h3>
      <p>Language training and professional recognition already run in parallel for our pool. That noticeably shortens your wait.</p>
      <span class="time">6 months</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Stage 4</span><h3>Arrival &amp; integration</h3>
      <p>A personal welcome on arrival, and support for as long as it's needed.</p>
      <span class="time">From day 1 on the team</span>
      <div class="stamps">
        <div class="stamp"><img src="logo-ral-guetezeichen.png" alt="RAL quality mark for fair recruitment in nursing, Germany" loading="lazy" decoding="async"><span>RAL-verified</span></div>
        <div class="stamp"><img src="logo-bvifg.png" alt="bvifg member" loading="lazy" decoding="async"><span>bvifg</span></div>
        <div class="stamp"><img src="logo-gapa.png" alt="GAPA quality association" loading="lazy" decoding="async"><span>GAPA</span></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Not luck. A system.</h2>
      <p style="font-size:15.5px;margin-top:10px;max-width:680px;">Our success isn't down to chance, it rests on our own model: the HEINZ Integration Framework. Developed on the basis of academic research, including work with Leuphana University, and sharpened by our own experience since 2018.</p>
    </div>
    <div class="heinz-grid">
      <div class="heinz-letter reveal"><div class="big">H</div><div class="lbl">Handlungssicherheit<br>Orientation &amp; onboarding</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.04s"><div class="big">E</div><div class="lbl">Erwartungen matchen<br>Transparency &amp; placement</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.08s"><div class="big">I</div><div class="lbl">Inklusion &amp; Respekt<br>Employer coaching</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.12s"><div class="big">N</div><div class="lbl">Navigation ermöglichen<br>Language &amp; systems</div></div>
      <div class="heinz-letter reveal" style="transition-delay:.16s"><div class="big">Z</div><div class="lbl">Zukunft &amp; Verwurzelung<br>Settlement &amp; career</div></div>
    </div>
    <p class="heinz-proof reveal">One finding from the research: structured orientation in the first few weeks measurably reduces early drop-off by 36 percent. We're happy to walk you through the HEINZ Integration Framework in a personal conversation.</p>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="clients standalone reveal">
      <p class="lead-sm">These facilities already work with us:</p>
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
    <h2>Curious to learn more?</h2>
    <p>In a free, no-obligation first conversation, we're happy to tell you more and find out whether and how we can work together.</p>
    <a href="kontakt-en.html" class="btn btn-primary">Schedule a call</a>
  </div>
</section>
'''
page("fuer-einrichtungen-en.html", "For Employers — Heinz Personnel Solutions", "fuer-einrichtungen.html", einrichtungen_body_en, description="Reliable staffing with international nursing professionals: RAL quality mark, fallback cover, on average 6 months to the first day on the job.", extra_script=ROUTE_SCRIPT, extra_css=ROUTE_CSS)

# =============================================== FOR PROFESSIONALS (EN) ====
ANKAADIA_URL = "https://app.ankaadia.com/candidate-application/4ffb749b-c604-47f5-b04b-f84bdf96bd8e/4eb15342-1f37-4771-bdec-4f7f94f5687a"

fachkraefte_body_en = f'''
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index-en.html">Home</a> / For Professionals</div>
    <span class="eyebrow">For nursing professionals who want to come to Germany</span>
    <h1 class="reveal in">Your path to Germany. Fair, transparent, no hidden costs.</h1>
    <p class="lead reveal in">We support you personally, from your first enquiry to arriving on the team, and beyond.</p>
    <div class="hero-cta-row reveal" style="margin-top:22px;">
      <a href="{ANKAADIA_URL}" class="btn btn-primary" target="_blank" rel="noopener">Apply now</a>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="wrap">
    <span class="badge"><img src="logo-ral-guetezeichen.svg" alt="RAL quality mark for fair recruitment in nursing, Germany" style="height:100px"></span>
    <span class="badge"><img src="logo-bvifg.png" alt="Member of the Federal Association for International Skilled Worker Recruitment" style="height:74px"></span>
    <span class="badge"><img src="logo-gapa.png" alt="GAPA quality association for fair recruitment of nursing professionals from abroad" style="height:96px"></span>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="win-card reveal" style="max-width:720px;border-color:var(--green);">
      <h3>Our clear promise to you</h3>
      <p>No hidden costs. No repayment schemes. You pay nothing for your placement. That's a fixed part of our RAL-certified process.</p>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Real success stories.</h2><p style="font-size:15.5px;margin-top:10px;">No stock-photo smiles. This is what it really looks like when our professionals arrive in Germany and find a home.</p></div>
    <div class="story-grid">
      <a class="reveal" href="blog-post-5-en.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-willkommen-gruppe.jpg" alt="Arrival at Berlin Brandenburg Airport, a warm welcome" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">Arrived: welcome to Germany</p></a>
      <a class="reveal" style="transition-delay:.08s" href="blog-post-6-en.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-mietwagen-team.jpg" alt="Team welcome at the airport" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">The first day, together with the team</p></a>
      <a class="reveal" style="transition-delay:.16s" href="blog-post-7-en.html"><div class="story-photo" style="height:210px;"><img src="foto-hero-gartenfest.jpg" alt="Summer party with the whole team" loading="lazy" decoding="async"></div><p style="font-size:13.5px;text-align:center;color:var(--ink-soft);">One year later: summer party with the team</p></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>Your path, step by step.</h2><p style="font-size:15.5px;margin-top:10px;max-width:680px;">From your first introduction to arriving on the team: transparent, with clear timeframes. Language training and recognition procedures run in parallel with us, which is why facilities already working with our candidate pool can typically welcome their new professional after about 6 months. If you apply fresh today, plan for roughly 12 to 13 months until entry into Germany.</p></div>
  </div>
  <div class="route-wrap" id="route">
    <svg class="route-svg" id="routeSvg" viewBox="0 0 100 1000" preserveAspectRatio="none">
      <path id="routePath" d="M50,0 C20,50 20,90 50,120 C80,150 80,190 50,220 C20,250 20,300 50,330 C80,360 80,400 50,430 C20,460 20,510 50,540 C80,570 80,610 50,640 C20,670 20,710 50,740"/>
    </svg>
    <div class="waypoint right reveal">
      <span class="tag">Stage 1</span><h3>Getting to know each other &amp; application</h3>
      <p>We get to know each other personally and talk about your experience, your goals, and possible facilities.</p>
      <ul>
        <li>Video or in-person conversation with our team</li>
        <li>Recording your qualification and work experience</li>
        <li>Introduction to suitable facilities, matching begins</li>
      </ul>
      <span class="time">Day 1</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Stage 2</span><h3>Language training A1 to B2</h3>
      <p>German lessons with native-speaking teachers, organised through our partner Lingoda, up to a confident B2 level.</p>
      <ul>
        <li>Placement test and individual study plan</li>
        <li>Weekly online or in-person lessons</li>
        <li>Interim exams at A2 and B1 level</li>
        <li>Typically 6 to 9 months to the final B2 exam</li>
      </ul>
      <span class="time">From month 1</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Stage 3</span><h3>Recognition &amp; labour market clearance</h3>
      <p>We coordinate the deficiency notice, professional recognition and labour market clearance, in parallel with your language course.</p>
      <ul>
        <li>Credential evaluation and deficiency notice from the responsible state authority</li>
        <li>If needed: an adaptation measure or knowledge test</li>
        <li>Application for professional recognition and labour market clearance</li>
        <li>Usually 6 to 12 months depending on the state, runs in parallel with your language course</li>
      </ul>
      <span class="time">From month 9</span>
    </div>
    <div class="waypoint left reveal">
      <span class="tag">Stage 4</span><h3>Visa &amp; entry</h3>
      <p>We support the visa process and organise your travel. On arrival day, we pick you up in person.</p>
      <ul>
        <li>Appointment and documents for the German diplomatic mission</li>
        <li>Organising travel and your first accommodation</li>
        <li>Personal pickup at the airport</li>
      </ul>
      <span class="time">From month 13</span>
    </div>
    <div class="waypoint right reveal">
      <span class="tag">Stage 5</span><h3>Arrival &amp; integration</h3>
      <p>Housing, official registrations, opening a bank account, first weeks on the team, and support for as long as it's needed.</p>
      <ul>
        <li>Registering with the residents' registration office, bank account, health insurance</li>
        <li>Introduction and support on your new team</li>
        <li>Ongoing support from our integration management, well beyond your first day on the job</li>
      </ul>
      <span class="time">Settling in begins</span>
      <div class="stamps">
        <div class="stamp"><img src="logo-ral-guetezeichen.png" alt="RAL quality mark for fair recruitment in nursing, Germany" loading="lazy" decoding="async"><span>RAL-verified</span></div>
        <div class="stamp"><img src="logo-bvifg.png" alt="bvifg member" loading="lazy" decoding="async"><span>bvifg</span></div>
        <div class="stamp"><img src="logo-gapa.png" alt="GAPA quality association" loading="lazy" decoding="async"><span>GAPA</span></div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-soft);">
  <div class="wrap">
    <div class="section-head reveal"><h2>Your points of contact</h2></div>
    <div class="team-grid" style="grid-template-columns:repeat(2,1fr);max-width:560px;">
      <div class="team-card reveal"><div class="avatar"><img src="team-tabeia.jpg" alt="Tabeia Antonio" loading="lazy" decoding="async"></div><h3>Tabeia Antonio</h3><div class="role">Integration Manager</div><p class="bio">Supports you from recruitment to a settled place on the team.</p></div>
      <div class="team-card reveal" style="transition-delay:0.08s"><div class="avatar"><img src="team-tanja.jpg" alt="Tanja Grabow" loading="lazy" decoding="async"></div><h3>Tanja Grabow</h3><div class="role">Professional Support</div><p class="bio">Supports you from finding housing to your first day on the job.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><h2>RAL quality mark "Fair Recruitment in Nursing"</h2></div>
    <div class="win-card reveal" style="max-width:760px;">
      <p style="margin:0 0 12px;">HPS holds the RAL quality mark "Fair Recruitment in Nursing, Germany" and is a member of the Federal Association for International Skilled Worker Recruitment (bvifg). That means independently audited, fair recruitment standards, verifiable by you, with a clear complaints process should something not go as planned.</p>
      <a href="beschwerdeformular-en.html" class="btn btn-ghost btn-sm">Complaints form</a>
    </div>
    <div class="section-head reveal" style="margin-top:44px;margin-bottom:20px;"><h3 style="font-size:19px;">Important links for your planning</h3></div>
    <div class="resource-links reveal">
      <a class="resource-link" href="https://www.faire-anwerbung-pflege-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">RAL Quality Association Fair Recruitment in Nursing</div><div class="rdesc">The official body behind the RAL quality mark, independent audits of fair recruitment.</div></a>
      <a class="resource-link" href="https://fair-recruitment-nurse.com/" target="_blank" rel="noopener"><div class="rtitle">fair-recruitment-nurse.com</div><div class="rdesc">Information on how to recognise certified, fair recruitment agencies.</div></a>
      <a class="resource-link" href="https://www.anerkennung-in-deutschland.de/" target="_blank" rel="noopener"><div class="rtitle">Recognition in Germany</div><div class="rdesc">The German government's official portal for recognising foreign professional qualifications.</div></a>
      <a class="resource-link" href="https://www.make-it-in-germany.com/en/" target="_blank" rel="noopener"><div class="rtitle">Make it in Germany</div><div class="rdesc">The German government's official portal for international professionals.</div></a>
      <a class="resource-link" href="https://www.bvifg.de/" target="_blank" rel="noopener"><div class="rtitle">Federal Association for International Skilled Worker Recruitment</div><div class="rdesc">National association for fair, transparent recruitment of skilled workers.</div></a>
      <a class="resource-link" href="downloads-en.html"><div class="rtitle">Downloads &amp; documents</div><div class="rdesc">Info brochures, terms and conditions, and our commitment declaration to read.</div></a>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap reveal">
    <h2>Interested in a position in Germany?</h2>
    <p>Apply directly or write to us. We'll get back to you personally.</p>
    <div class="hero-cta-row" style="justify-content:center;">
      <a href="{ANKAADIA_URL}" class="btn btn-primary" target="_blank" rel="noopener">Apply now</a>
      <a href="kontakt-en.html" class="btn btn-ghost">Get in touch</a>
    </div>
  </div>
</section>
'''
page("fuer-fachkraefte-en.html", "For Professionals — Heinz Personnel Solutions", "fuer-fachkraefte.html", fachkraefte_body_en, description="Your path as a nursing professional to Germany: fair, transparent, no hidden costs. Language course, recognition, visa and personal support.", extra_script=ROUTE_SCRIPT, extra_css=ROUTE_CSS)

print("einrichtungen-en + fachkraefte-en done")
