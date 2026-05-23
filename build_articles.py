#!/usr/bin/env python3
"""Generate the three article pages with shared chrome."""
from pathlib import Path

OUT = Path("/home/user/workspace/anti-defection-book/blog")
AMAZON = "https://www.amazon.in/Anti-Defection-Law-Parliamentary-Privileges-vols/dp/8195609961"
EBC = "https://www.ebcwebstore.com/product/anti-defection-law-and-parliamentary-privileges-by-subhash-c-kashyap-4th-edition?products_id=99106869"
PRS = "https://prsindia.org/theprsblog/the-anti-defection-law-explained?page=269&amp;per-page=1"
WEEK = "https://www.theweek.in/theweek/cover/2024/09/28/lok-sabha-former-secretary-general-subhash-c-kashyap-interview.html"
GR = "https://www.goodreads.com/book/show/1990302.Anti_Defection_Law_And_Parliamentary_Privileges"
OL = "https://openlibrary.org/works/OL1075206W/Anti-defection_law_and_Parliamentary_privileges"


def page(title, description, meta_line, headline, body_html, og_image="../images/book-volumes.png"):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Kashyap Chambers</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="Anti-Defection Law, Tenth Schedule, parliamentary privileges, Shaunak Kashyap, Shaunak Kashyap Advocate, Kashyap Chambers, constitutional law India, election law India" />
  <meta name="author" content="Shaunak Kashyap, Advocate — Kashyap Chambers" />
  <link rel="canonical" href="./" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:site_name" content="Kashyap Chambers — Constitutional Law Resources" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />

  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/styles.css" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{description}",
    "author": {{ "@type": "Person", "name": "Shaunak Kashyap", "jobTitle": "Advocate", "affiliation": {{ "@type": "Organization", "name": "Kashyap Chambers" }} }},
    "publisher": {{ "@type": "Organization", "name": "Kashyap Chambers" }},
    "about": ["Anti-Defection Law", "Tenth Schedule", "Parliamentary Privileges", "Constitutional Law of India"],
    "mainEntityOfPage": "Anti-Defection Law and Parliamentary Privileges — Kashyap Chambers"
  }}
  </script>
</head>
<body>

<header class="site-header">
  <div class="container site-header__inner">
    <a href="../index.html" class="brand" aria-label="Kashyap Chambers home">
      <svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true">
        <g stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="square">
          <line x1="6" y1="9" x2="26" y2="9"/><line x1="6" y1="11" x2="26" y2="11"/>
          <line x1="11" y1="11" x2="11" y2="23"/><line x1="21" y1="11" x2="21" y2="23"/>
          <line x1="6" y1="23" x2="26" y2="23"/><line x1="6" y1="25" x2="26" y2="25"/>
        </g>
      </svg>
      <span class="brand__text">Kashyap Chambers<span>Constitutional Law Resources</span></span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="../index.html#the-book">The Book</a>
      <a href="../index.html#why-it-matters">Why It Matters</a>
      <a href="../index.html#curator">Curator</a>
      <a href="../index.html#resources">Resources</a>
      <a href="./index.html" class="is-active">Essays</a>
    </nav>
  </div>
</header>

<main>
  <article class="article">
    <div class="container">
      <header class="article__header">
        <p class="article__meta">{meta_line}</p>
        <h1 style="font-size:var(--text-2xl);max-width:24ch">{headline}</h1>
      </header>
      <div class="article__body">
        {body_html}
      </div>
      <div class="article__cta">
        <h3>Read the full reference</h3>
        <p>The two-volume set <em>Anti-Defection Law and Parliamentary Privileges</em> (Eastern Book Company, 4th edition, 2023) treats these doctrines at length, with case law and parliamentary practice in one place.</p>
        <div style="display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap">
          <a class="btn btn--primary" href="{AMAZON}" rel="noopener" target="_blank">Buy on Amazon <span class="arrow" aria-hidden="true">→</span></a>
          <a class="btn btn--ghost" href="{EBC}" rel="noopener" target="_blank">View on EBC</a>
        </div>
      </div>

      <div class="container container--narrow" style="margin-top:var(--sp-16);padding-top:var(--sp-8);border-top:1px solid var(--rule)">
        <p class="eyebrow eyebrow--ink">More essays</p>
        <ul style="list-style:none;padding:0;margin:0;display:grid;gap:var(--sp-3);font-family:var(--font-sans)">
          <li><a href="./anti-defection-law-india.html" style="border-bottom:1px solid var(--rule);padding-bottom:2px">→ What is the Anti-Defection Law in India?</a></li>
          <li><a href="./parliamentary-privileges-legislative-independence.html" style="border-bottom:1px solid var(--rule);padding-bottom:2px">→ Parliamentary Privileges and Legislative Independence</a></li>
          <li><a href="./why-this-matters-to-advocates.html" style="border-bottom:1px solid var(--rule);padding-bottom:2px">→ Why this subject matters to advocates and researchers</a></li>
        </ul>
      </div>
    </div>
  </article>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="../index.html" class="brand" style="color:var(--parchment);margin-bottom:var(--sp-4)">
          <svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true" style="color:var(--gold-soft)">
            <g stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="square">
              <line x1="6" y1="9" x2="26" y2="9"/><line x1="6" y1="11" x2="26" y2="11"/>
              <line x1="11" y1="11" x2="11" y2="23"/><line x1="21" y1="11" x2="21" y2="23"/>
              <line x1="6" y1="23" x2="26" y2="23"/><line x1="6" y1="25" x2="26" y2="25"/>
            </g>
          </svg>
          <span class="brand__text" style="color:var(--parchment)">Kashyap Chambers<span style="color:var(--text-on-ink-mute)">Constitutional Law Resources</span></span>
        </a>
      </div>
      <div>
        <h4>Buy the Book</h4>
        <ul>
          <li><a href="{AMAZON}" rel="noopener" target="_blank">Amazon.in</a></li>
          <li><a href="{EBC}" rel="noopener" target="_blank">EBC Webstore</a></li>
        </ul>
      </div>
      <div>
        <h4>Listings</h4>
        <ul>
          <li><a href="{GR}" rel="noopener" target="_blank">Goodreads</a></li>
          <li><a href="{OL}" rel="noopener" target="_blank">Open Library</a></li>
        </ul>
      </div>
      <div>
        <h4>Context</h4>
        <ul>
          <li><a href="{PRS}" rel="noopener" target="_blank">PRS Explainer</a></li>
          <li><a href="{WEEK}" rel="noopener" target="_blank">The Week — Interview</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      <div>© <span id="year">2025</span> Kashyap Chambers. Curated page; not affiliated with the publisher.</div>
      <div>Shaunak Kashyap, Advocate · Kashyap Chambers</div>
    </div>
  </div>
</footer>

<script>document.getElementById('year').textContent = new Date().getFullYear();</script>

</body>
</html>
"""


# -------- Essay 1 --------
e1_body = f"""
<p class="lede">India's anti-defection law lives in the Tenth Schedule of the Constitution. It is a short text doing very heavy work: deciding when a sitting legislator forfeits their seat because of how they have voted, or which side of the aisle they have walked to.</p>

<h2>1. Origin: the 52nd Amendment, 1985</h2>
<p>The Tenth Schedule was inserted into the Constitution by the Constitution (Fifty-second Amendment) Act, 1985. The political context is familiar: through the 1960s and 1970s, governments at the Centre and in the States were repeatedly destabilised by floor-crossings, often coordinated and openly transactional. Parliament chose to constitutionalise a response.</p>
<p>The Schedule applies to members of both Houses of Parliament and the State Legislatures. Its central question is straightforward: when does a legislator's conduct amount to defection, and what follows?</p>

<h2>2. The grounds for disqualification</h2>
<p>Read functionally, the Schedule identifies two principal grounds on which a member of a House may be disqualified:</p>
<ul>
  <li><strong>Voluntarily giving up membership</strong> of the political party on whose ticket the member was elected. The phrase has been read broadly by the Supreme Court to include conduct, not just formal resignation.</li>
  <li><strong>Voting or abstaining contrary to a direction (a "whip")</strong> issued by the party, without prior permission and without subsequent condonation within fifteen days.</li>
</ul>
<p>Independents who join a political party after election, and nominated members who join one after the relevant six-month window, are likewise within the Schedule's reach.</p>

<blockquote>The Tenth Schedule asks one constitutional question of every legislator: did you remain, in substance, the person the electorate sent to the House?</blockquote>

<h2>3. The Speaker's role — and its limits</h2>
<p>Disqualification questions under the Tenth Schedule are decided not by a court at first instance but by the presiding officer of the House — the Speaker of the Lok Sabha or a State Assembly, or the Chairman of the Rajya Sabha or a State Council. That choice of forum has been the most contested feature of the law.</p>
<p>In <em>Kihoto Hollohan v. Zachillhu</em> (1992), the Supreme Court upheld the constitutional validity of the Schedule but read down the finality clause: the Speaker's order is subject to judicial review on limited grounds, including <em>mala fides</em>, perversity, and violation of natural justice. Later decisions, including <em>Keisham Meghachandra Singh</em> (2020), have pressed the Speakers to decide references within a reasonable time, treating prolonged delay as itself reviewable.</p>

<h2>4. The split and the merger</h2>
<p>The original Schedule recognised a "split" — a defence available when a significant block of legislators in a party left together. The Ninety-first Amendment (2003) deleted that defence. What survives is the narrower "merger" route in paragraph 4: a member is protected from disqualification only where two-thirds of the legislative party agree to merge with another political party.</p>

<h2>5. What the law leaves open</h2>
<p>Several questions continue to invite litigation and academic comment:</p>
<ul>
  <li>What counts as "voluntarily giving up" party membership when the act is one of speech or association rather than a formal resignation?</li>
  <li>How long may a presiding officer take to decide a disqualification petition, and what is the remedy when delay distorts the political consequence?</li>
  <li>Should the adjudicatory function be moved away from the Speaker — to a tribunal or to the Election Commission — to address concerns about partisanship?</li>
</ul>

<h2>6. Where the volumes go further</h2>
<p>The two-volume reference treats each of these threads with the case law and parliamentary practice that any practitioner needs in front of them. For a public-facing overview, <a href="{PRS}" rel="noopener" target="_blank">PRS Legislative Research</a> maintains a useful explainer; for the deeper apparatus, the book is the natural next step.</p>
"""

# -------- Essay 2 --------
e2_body = f"""
<p class="lede">Parliamentary privilege is the older of the two doctrines this page is concerned with — older than the Constitution, older than the Republic. It is the rule that lets a House of Parliament govern itself, protect its members, and refuse, in defined ways, to be interrupted by the courts.</p>

<h2>1. The constitutional anchor: Article 105</h2>
<p>Article 105 of the Constitution sets out the privileges of Parliament and its members. Two are textual and absolute: freedom of speech in Parliament (subject only to the Constitution and the rules of the House), and immunity from liability in any court for anything said or any vote given in the House or any committee. A parallel provision for State Legislatures lives in Article 194.</p>
<p>Beyond those textual rights, Article 105(3) preserves "other powers, privileges and immunities" of each House and its members — historically equated to those of the House of Commons at the commencement of the Constitution, until defined by Parliament itself.</p>

<h2>2. Freedom of speech inside the House</h2>
<p>Freedom of speech in Parliament is the keystone. It is wider than the right under Article 19(1)(a): a Member may say things on the floor that would attract liability outside it, and may not be sued or prosecuted for those words. The discipline that constrains this freedom is internal — through rules of order, the Chair, and the House's own committees on privilege and ethics.</p>

<blockquote>The privilege of free speech in Parliament is not an indulgence to the Member; it is a protection of the proceedings.</blockquote>

<h2>3. Immunity from judicial process</h2>
<p>The companion right is procedural. No Member shall be liable to any proceedings in any court in respect of anything said or any vote given in the House. The Supreme Court read this strictly in <em>P. V. Narasimha Rao v. State</em> (1998), and revisited the underlying logic in later decisions; the reach of the immunity, particularly where alleged conduct sits outside the four walls of the House, remains a live question.</p>

<h2>4. Internal autonomy and the privilege power</h2>
<p>Each House controls its own proceedings. It can punish its members for breach of privilege or contempt; it can, in defined circumstances, punish non-members for the same. The architecture is not unlimited — courts have repeatedly affirmed that fundamental rights are not extinguished at the door of the House — but it is real, and it is jealously guarded.</p>

<h2>5. The codification question</h2>
<p>The Constitution itself contemplated that Parliament would, in time, define its privileges by law. Parliament has so far chosen not to. Codification has been debated repeatedly: it would offer clarity to the press, to citizens, and to courts; it would also, the argument runs, freeze a doctrine whose strength lies in its responsiveness to circumstance.</p>

<h2>6. Privilege in a constitutional democracy</h2>
<p>The privileges of Parliament exist not for the benefit of the Member but for the institution. They are best read as the operating system on which legislative democracy runs — neither extra-constitutional nor untouchable, but indispensable to the work the House does. The two-volume reference traces this arc through Indian and comparative material; <a href="{WEEK}" rel="noopener" target="_blank">a recent interview</a> with the work's author offers a public-facing summary of why the subject still matters.</p>
"""

# -------- Essay 3 --------
e3_body = f"""
<p class="lede">It is easy to read anti-defection law and parliamentary privileges as a subject for textbooks and law-school seminars. In practice, both turn up in unannounced ways in the working life of an advocate.</p>

<h2>1. Election and post-election work</h2>
<p>Election petitions under the Representation of the People Act, 1951, are the obvious meeting point with election law. But the Tenth Schedule's disqualification ground is not confined to election petitions: a sitting member's seat may be put at risk by a reference to the Speaker months or years after the poll. Counsel advising a defecting legislator, a party whip, or an aggrieved petitioner needs to know how the Schedule has been read in the latest line of cases.</p>

<h2>2. Disqualification references and writ practice</h2>
<p>The post-<em>Kihoto Hollohan</em> jurisprudence has expanded the judicial review available against Speakers' orders, and against their delay in deciding. Writ practice in constitutional courts therefore carries a steady current of Tenth Schedule matters — challenges to disqualification, to delay, to procedure before the presiding officer, and to the political consequences of all three.</p>

<blockquote>For counsel, the doctrine is not a separate subject. It is a layer that runs underneath election law, constitutional law, and the law of parliamentary practice.</blockquote>

<h2>3. Privilege notices and contempt proceedings</h2>
<p>The privileges side of the subject reaches a different set of clients: journalists, editors, broadcasters, and citizens who find themselves summoned before a Committee of Privileges. Advising on such notices calls for an unusual mix of constitutional litigation, parliamentary practice, and old House-of-Commons authority — most of which is buried in places that a general reference cannot easily surface.</p>

<h2>4. Constitutional litigation more broadly</h2>
<p>Both doctrines also turn up in larger constitutional litigation: floor tests after a hung verdict, references on the powers of the Governor, disputes about the conduct of legislative business, and questions about the relationship between the legislature and the courts. The two-volume reference is, in this sense, a working tool — not a museum piece.</p>

<h2>5. For researchers and students</h2>
<p>For scholars and law students, the appeal is different. The Tenth Schedule is a compact case study in how a constitutional amendment plays out across four decades of practice. The privileges chapter is a case study of how an unwritten doctrine sits inside a written constitution. Both reward sustained reading.</p>

<h2>6. A practical reading order</h2>
<p>Practitioners reading the two volumes for the first time often find it useful to begin with the Tenth Schedule chapters, then move to privileges, and only then to the comparative material. The structure of the work supports that order. For the purchase link, the <a href="{AMAZON}" rel="noopener" target="_blank">Amazon listing</a> is the most accessible; <a href="{EBC}" rel="noopener" target="_blank">EBC's storefront</a> remains the canonical source.</p>
"""


def write_page(slug, **kw):
    p = OUT / f"{slug}.html"
    p.write_text(page(**kw), encoding="utf-8")
    print("wrote", p)


write_page(
    "anti-defection-law-india",
    title="What is the Anti-Defection Law in India?",
    description="A working overview of India's anti-defection law — the Tenth Schedule, its grounds for disqualification, the Speaker's role, and what the courts have made of it since Kihoto Hollohan. Curated by Shaunak Kashyap, Advocate.",
    meta_line="Essay · 01 &nbsp;·&nbsp; Doctrine &nbsp;·&nbsp; Curated by Shaunak Kashyap, Advocate",
    headline="What is the Anti-Defection Law in India?",
    body_html=e1_body,
)

write_page(
    "parliamentary-privileges-legislative-independence",
    title="Parliamentary Privileges and Legislative Independence",
    description="An essay on Article 105, freedom of speech inside the House, immunity from judicial process, and the open question of codification — read as a single doctrinal arc. Curated by Shaunak Kashyap, Advocate.",
    meta_line="Essay · 02 &nbsp;·&nbsp; Privilege &nbsp;·&nbsp; Curated by Shaunak Kashyap, Advocate",
    headline="Parliamentary Privileges and Legislative Independence",
    body_html=e2_body,
)

write_page(
    "why-this-matters-to-advocates",
    title="Why this subject matters to advocates and researchers",
    description="Where anti-defection law and parliamentary privileges turn up in real practice — election petitions, disqualification references, contempt notices, and constitutional litigation. Curated by Shaunak Kashyap, Advocate.",
    meta_line="Essay · 03 &nbsp;·&nbsp; Practice &nbsp;·&nbsp; Curated by Shaunak Kashyap, Advocate",
    headline="Why this subject matters to advocates and researchers.",
    body_html=e3_body,
)

print("Done.")
