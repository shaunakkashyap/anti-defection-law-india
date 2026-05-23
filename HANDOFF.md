# Book Website Preview — Handoff

## Project

- **project_path:** `/home/user/workspace/anti-defection-book`
- **entry_point:** `index.html`
- **site_name suggestion:** `Anti-Defection Law and Parliamentary Privileges — Kashyap Chambers`
- **Suggested subdomain (if later publishing):** `kashyap-chambers` or `anti-defection-law`
- **Status:** Static, fully self-contained, no backend, no runtime API calls. Ready for `deploy_website`.

## Pages

| Path | Title |
| --- | --- |
| `index.html` | Home — hero, about the volumes, why-it-matters, curator profile, essays preview, sources |
| `blog/index.html` | Essays index |
| `blog/anti-defection-law-india.html` | Essay 01 — What is the Anti-Defection Law in India? |
| `blog/parliamentary-privileges-legislative-independence.html` | Essay 02 — Parliamentary Privileges and Legislative Independence |
| `blog/why-this-matters-to-advocates.html` | Essay 03 — Why this subject matters to advocates and researchers |

Plus `robots.txt`, `sitemap.xml`, and a custom inline SVG logo / favicon (`images/favicon.svg`).

## Design Choices

- **Art direction:** constitutional law / parliamentary scholarship. Deep ink navy (`#0e1a2b`) on warm parchment ivory (`#f5efe1`), restrained oxidized gold accent (`#a47a2b`), maroon reserved for primary-button hover. No gradients.
- **Typography:** Cormorant Garamond (display serif) + Source Serif 4 (body) + Inter (UI chrome only). Italic display serif used for the book title's "Parliamentary Privileges" emphasis, pull-quotes, and section numerals.
- **Logo:** Inline SVG of stylized parallel pillars + capital/base lines — reads as "columns of a chamber" without imitating any government insignia. Works mono in dark and light.
- **Imagery:** Three generated photographs — atmospheric law library (hero), Indian parliamentary chamber interior architectural detail (curator section), and a still life of two navy hardback volumes (hero side). No stock, no text in images, no flags or insignia.
- **Layout:** Editorial two-column splits, three-card grids, narrow article column (720px max), generous section padding `clamp(3.5rem, 7vw, 6.5rem)`. Sticky translucent header with backdrop-blur and gold underline for active nav.

## Content / Tone

- Authoritative, restrained, Indian legal-professional register. No marketing exclamations. Sentences are written to read aloud well.
- **Authorship language is deliberately careful.** The book's authored-by metadata names Subhash C. Kashyap (consistent with EBC, Goodreads, Open Library). The site describes Shaunak Kashyap, Advocate, as the **curator** who "spotlights" the work — never as the author. This leaves room for the user to correct later without retracting any claim. Wording on the home page uses "Authored by Subhash C. Kashyap; published by Eastern Book Company. Curated and highlighted by Shaunak Kashyap, Advocate of Kashyap Chambers."
- Target keywords appear naturally in copy, headings, meta tags, alt text, and JSON-LD: "Shaunak Kashyap, Advocate", "Shaunak Kashyap", "Kashyap Chambers", "Anti-Defection Law and Parliamentary Privileges", "Tenth Schedule", "parliamentary privileges", "constitutional law India", "election law India".

## SEO

- Unique `<title>` and `<meta name="description">` per page; all under recommended length where possible.
- Open Graph + Twitter card on every page.
- Canonical link tags on every page.
- JSON-LD on home page: `Book` (with `Offer` pointing to the Amazon URL and `sameAs` to EBC/Goodreads/Open Library), `WebPage`, and `Person` (Shaunak Kashyap → Kashyap Chambers).
- JSON-LD `Article` schema on each essay page.
- `robots.txt` and `sitemap.xml` present (note: relative URLs — once deployed, host name will resolve via deploy URL).
- Semantic HTML (`<header>`, `<main>`, `<article>`, `<section>`, `<footer>`), one `<h1>` per page, proper heading hierarchy.

## CTAs

- **Primary:** Amazon listing (`https://www.amazon.in/Anti-Defection-Law-Parliamentary-Privileges-vols/dp/8195609961`) — appears in hero, profile section, essays index, every article page, and footer.
- **Secondary:** EBC listing — appears in hero (ghost button), article CTAs, and footer.
- All purchase links open in a new tab with `rel="noopener"`.

## Footer Sources

Linked in footer of every page: Amazon, EBC, Goodreads, Open Library, PRS Legislative Research, The Week interview, and essays index.

## Visual QA

Three reference screenshots saved at project root (also delete-safe for the parent agent to view):

- `preview-home-desktop.png` — desktop full-page home
- `preview-home-mobile.png` — 390px mobile home
- `preview-article-desktop.png` — desktop full-page essay

QA notes: Hero, three-card grid, dark curator profile, and essay typography all render cleanly. Mobile nav collapses (current behaviour is "hide" rather than hamburger — acceptable for a preview because all key destinations are reachable from the body and footer; the parent agent or user can add a hamburger menu later if desired).

## Deploy

```
deploy_website(
  user_description="Deploying Anti-Defection Law book preview site",
  project_path="/home/user/workspace/anti-defection-book",
  site_name="Anti-Defection Law and Parliamentary Privileges — Kashyap Chambers",
  entry_point="index.html",
)
```

No backend, no install/run command needed. Total project weight ~11 MB (mostly the three generated images at full PNG resolution). If a tighter weight is desired, the images can be downscaled or converted to WebP — not strictly necessary for a preview.

## Follow-ups for the parent agent / user

1. Confirm authorship language. If Shaunak Kashyap is in fact a co-author (or sole author) of the 4th edition, swap "Curated and highlighted by" → "Co-authored by" on the home hero and in the JSON-LD `author` field. The careful wording was chosen because public metadata across Amazon (which 503'd on fetch), EBC, Goodreads, and Open Library currently names Subhash C. Kashyap as author.
2. The user may want a real headshot of Shaunak Kashyap to replace the architectural detail in the curator section.
3. If the site is later upgraded to a permanent `*.pplx.app` URL via `publish_website`, regenerate JSON-LD `url` and canonical fields to absolute URLs.
4. Optional: convert the three hero/section images to WebP to drop page weight from ~11 MB to under 1 MB.
