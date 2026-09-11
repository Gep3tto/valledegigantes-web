# SPEC — afergreens.com rebuild brief

Prompt to bring the current site up to the bar set by AUDIT.md (2026-07-08),
without changing its design direction. Companion documents, all authoritative:

- `PRODUCT.md` — audience, purpose, voice. Wins every conflict.
- `DESIGN.md` — palette, type, components, named rules. Amended below where the audit found it self-contradictory.
- `AUDIT.md` — 117 verified findings. The P0 table is the acceptance list.

Anything marked `[DATO]` is a fact only the owner can supply. Build with a visible
placeholder, never invent the value.

## 01. GOAL

Turn a good-looking brochure into a B2B qualifying instrument. A wholesale or export
buyer landing on any page, on a phone, must within one screen be able to: see what is
sold and from where, see that it is Primus GFS certified, and reach a quote request
or WhatsApp in one tap. Every fix in this spec serves that sentence.

Keep the "Export Estate" look. This is not a redesign. The four mockup directions in
`Dropbox/AFER Greens/Branding/Web mockups 2026-07 (referencia)` are reference only.

## 02. TECH STACK

- Static HTML, CSS and vanilla JS. No framework, no build step required to deploy.
- Hosted on GitHub Pages from `main`, custom domain `www.afergreens.com` (CNAME present).
- One shared stylesheet `assets/site.css` and one shared script `assets/site.js`,
  replacing the ~2,300 lines duplicated across the four product pages. Page-specific
  CSS stays inline in that page's `<head>` only when it is truly page-specific.
- No third-party runtime scripts. Icons are inline SVG (copy the ~12 Lucide paths,
  ISC licence). Fonts self-hosted as subset woff2 in `assets/fonts/`.
- Image variants generated once with a script committed at `tools/images.py`
  (Pillow). Source PNGs live outside the repo (see `IMAGES.md`).
- Forms post to FormSubmit using the random-string alias, captcha enabled.
- A `404.html` at the root, branded, in Spanish, linking the four products and the form.
- `.gitignore` excludes `.claude/`, `.impeccable/`, `__pycache__/`. They are dev tooling
  and must not deploy.

## 03. DESIGN SYSTEM

Use `DESIGN.md` as written, with these amendments. Update `DESIGN.md` itself in the
same change so the spec and the code agree.

Colors (unchanged tokens, corrected usage):

- Stone `#9B9585` is restricted to light surfaces. Labels on dark surfaces use
  Agave Pale at 100% or Fog `#D5D0C6`.
- Add `scs-green-text: #567A1A`. SCS Green `#78A22F` stays for the badge fill only;
  all certification text, numbers and links use the dark variant (≥4.5:1 on Snow/White).
- On Cantera Teal `#0D6558` sections, body text is Agave Soft `#E8F0E8` and eyebrow
  labels are Amber Light `#FBBD6E` or White. Amber `#F7931E` on that surface fails AA.
- Delete the six off-palette colors introduced on product pages, including
  `#E8830A`. No new tokens are needed once the amber CTA strip is gone.
- Placeholder text is `rgba(168,196,169,0.75)`. Footer text is Agave Pale ≥75%.
- Focus ring is a 2px solid Amber outline with 2px offset on every interactive
  element, via `:focus-visible`. The 45% translucent ring in DESIGN.md is replaced.

Typography: unchanged. Fraunces for display, headline, title. Outfit for everything
else, including contact values (currently wrong). All sizes via `clamp()`; delete the
hard-coded 480px hero override. Every paragraph capped at 520px / 65ch.

Named rules that the current code breaks and this build must honor:

- Rarity Rule: amber ≤10% of any surface. No amber section backgrounds anywhere.
- One Glow Rule: amber shadow on primary buttons only.
- SCS Quarantine Rule: SCS green only in certification contexts.
- No icon + heading + text card grids. The ficha técnica becomes a two-column
  definition list on a dark spec surface, not six cards.
- Motion only on `transform` and `opacity`. The header scroll effect switches
  from animating height/padding to `transform: scale()` on the logo and a
  background-opacity fade.

Layout tokens from `DESIGN.md` apply. Add `scroll-margin-top: var(--header-h)` to
every anchored section.

## 04. PAGE STRUCTURE

Five existing pages keep their URLs. Two new files. English versions are Phase 2.

Home `/`:

1. Header (compact, see 11)
2. Hero
3. Certification strip (one line, verifiable)
4. Products (four cards, existing signature component)
5. Availability calendar
6. Nosotros (facts, people, founding year)
7. Certificaciones (real marks, PDF links)
8. FAQ
9. Contacto (form + WhatsApp + direct channels)
10. Footer (real navigation)

Product pages `/chiltepin/`, `/jalapeno/`, `/chipotle/`, `/melon/`:

1. Header
2. Breadcrumb (Inicio › Productos › Producto, real URLs, `aria-label="Ruta de navegación"`)
3. Product hero (photo, name, one-line spec, Primus GFS chip linking to the certificate)
4. Ficha técnica (definition list, printable)
5. Presentaciones (existing cards, neutral styling, no SCS green)
6. Logística y disponibilidad
7. Usos
8. Otros productos (three sibling links)
9. CTA band (Cantera Mid, amber pill button, WhatsApp secondary)
10. Footer

New: `404.html`, `aviso-de-privacidad.html` (plain page, Snow surface).

Remove: the ticker marquee. It is decorative, fails WCAG 2.2.2 without a pause
control, and carries superlatives. A static one-line certification strip replaces it.

## 05. HERO

Copy leads with what, where and proof. Voice per PRODUCT.md: declarative, no superlatives.

- Eyebrow: `VALLE DE GIGANTES · SAUCILLO, CHIHUAHUA` (label style)
- H1 (Fraunces, one amber italic `<em>`):
  `Chile y melón de <em>exportación</em>, certificados Primus GFS.`
- Sub (≤65ch): `Chiltepín, jalapeño, chipotle ahumado con mezquite y melón Gran Torino. Mayoreo, procesadoras y exportación a Estados Unidos.`
- Primary CTA (amber pill): `Solicitar cotización` → `#contacto`
- Secondary CTA (ghost): `Ver productos y fichas técnicas` → `#productos`
- Third action, text link with WhatsApp icon: `Escríbenos por WhatsApp` → `wa.me/526141690797?text=…`
- Certification strip directly under the actions:
  `Primus GFS · Campo #373629 · Cuadrilla #373630 · Empaque #373631 · Verificable` with each number linking to its Azzule PDF (`target="_blank"`, with "abre en ventana nueva" in the accessible name).

Layout: `min-height: 100dvh`, no 700px floor on mobile. Content top-aligned below
the header on viewports under 700px tall so H1 and the primary CTA are visible at
load. Add a top scrim to the hero overlay (`rgba(4,46,40,0.75) → transparent` over
the first 180px) so nav links pass contrast over the sky.

Hero image: `rancho` at 768 / 1280 / 1920 widths, webp with jpg fallback,
`fetchpriority="high"`, no `<link rel=preload>`.

## 06. PRODUCTS

Keep the signature product card. Fix its content.

- Eyebrow `— Productos`, H2 `Cuatro cultivos del <em>norte</em>.` (replaces "Lo mejor del norte")
- Card text is a fact, not an adjective. One line each:
  - Chiltepín: `50,000–100,000 SHU · seco y fresco · 100 g, 1 kg, 10 kg`
  - Jalapeño: `2,500–8,000 SHU · fresco · caja 17 kg (1 1/9 bushel), arpilla 30 kg`
  - Chipotle: `jalapeño ahumado con mezquite · arpilla 30 kg`
  - Melón Gran Torino: `2–3 kg por pieza · calibres 9's y 9j's · granel`
- Card link accessible name is the product name only. Image `alt` is empty inside the link.
- Card images at 480 / 960 / 1440 widths, `sizes="(min-width: 768px) 50vw, 100vw"`.
- Homepage and product pages must agree on presentations and fresh/dry status.
  The homepage currently says chiltepín is sold dry only; the product page sells both. Product page wins.

## 07. FICHA TÉCNICA AND LOGISTICS (product pages)

Replace the six descriptor cards with a definition list, two columns on desktop,
one on mobile, on the dark spec surface. Rows, in order:

- Origen · Variedad · Picor (SHU) or Brix `[DATO: melón °Brix]` · Calibre · Forma y color · Proceso (chipotle only) · Vida de anaquel · Certificación (with PDF link)

Add a second list, `Logística y disponibilidad`:

- Temporada: months available, fresh vs dry. `[DATO per product]`. Dried chiltepín and chipotle may state `Todo el año` if true.
- Pedido mínimo: `[DATO per presentation]`
- Empaque: cajas por tarima, tarimas por contenedor `[DATO]`
- Incoterms ofrecidos: `[DATO, e.g. EXW Saucillo, FOB frontera]`
- Tiempo de entrega: `[DATO]`
- Fracción arancelaria (HS): `[DATO]`
- Ficha técnica PDF: link to `/fichas/<producto>.pdf` `[DATO: owner supplies or we generate from the page via print stylesheet]`

Each product page carries the same availability data as the homepage calendar
(section 04, item 5): a 12-column strip per product, filled months in Amber Light on
Cantera Mid, with a text equivalent for screen readers.

Product JSON-LD: keep `Product` + `BreadcrumbList`. Remove `PriceSpecification`.
Offers use `"availability"` that matches the real season and `"businessFunction":
"http://purl.org/goodrelations/v1#Sell"` with no price. Fix the dangling cross-page
`@id` references and the breadcrumb fragment URL.

## 08. CERTIFICATIONS

The number-one trust signal, so it appears three times: nav, hero strip, section.

- Nav gets `Certificaciones` on all pages, same order everywhere:
  `Productos · Certificaciones · Nosotros · Cotizar`.
- Section: three cards on White, one per certificate, using the real Primus GFS
  and SCS Global Services marks `[DATO: owner supplies logo files or confirms rights]`.
  No Lucide icons in green circles. Each card: scope (Campo / Cuadrilla de cosecha /
  Empaque), number, auditor, `Ver certificado (PDF)`.
- Text in `scs-green-text`; badge fill in SCS Green.
- Product-page hero chip `Primus GFS` links to the relevant certificate PDF.

## 09. FAQ

New homepage section on Snow, eight questions, accordion with native
`<details>/<summary>` (no JS needed, keyboard-accessible by default). Answers are
plain facts, ≤65ch lines, and are mirrored verbatim in `FAQPage` JSON-LD.

1. ¿Qué es el chiltepín y qué tan picante es?
2. ¿Cuál es el pedido mínimo? `[DATO]`
3. ¿En qué meses hay jalapeño y melón frescos? `[DATO]`
4. ¿Exportan a Estados Unidos? ¿Bajo qué Incoterms? `[DATO]`
5. ¿Cómo verifico la certificación Primus GFS? (answer links the three PDFs)
6. ¿Cómo se ahúma el chipotle? (mezquite, process, time)
7. ¿Cuánto tarda una cotización y un primer embarque? `[DATO]`
8. ¿Dónde están ubicados? (canonical address, see 10)

## 10. CONTACT AND QUOTE

Conversion surface. Every line here is a P0 or P1 finding.

- Section on Cantera Mid. Form first on mobile, contact channels second.
- Fields: Empresa (required), Correo (required), Teléfono o WhatsApp (optional),
  Producto (select with visible chevron, preselected from `?producto=` when arriving
  from a product page), Volumen estimado (optional short text), Mensaje (optional).
  Inputs at 16px minimum to stop iOS zoom.
- Privacy line above the button linking `aviso-de-privacidad.html`, per LFPDPPP.
- Submit (amber, full width): `Solicitar cotización`.
- Success and error containers exist in the initial markup with `role="status"` and
  `role="alert"`; on success, focus moves to the success heading. Success copy commits
  to a response time `[DATO: e.g. "Respondemos en un día hábil"]`.
- No-JS fallback: `_next` set to `/gracias.html` so a plain POST lands on a branded page.
- Endpoint: FormSubmit random alias, `_captcha` on, honeypot kept.
- WhatsApp: persistent floating button on all pages, bottom right, 56px, visible
  after the hero. Pre-filled message per page, e.g.
  `Hola, me interesa cotizar chiltepín (presentación y volumen: ).`
- Direct channels listed with 44px touch targets: teléfono, WhatsApp, correo, dirección.
- Canonical address, used identically in the visible block, footer, JSON-LD and
  `llms.txt`: `Rancho Valle de Gigantes, La Cruz, Municipio de Saucillo, Chihuahua, CP 33676` `[DATO: confirm]`.

Footer, all pages: four product links with descriptive anchors, Certificaciones,
Nosotros, Contacto, Aviso de privacidad, the canonical address, and the phone.

## 11. INTERACTIONS

- Header: single row, 64–72px, on every viewport. Logo left (max 44px tall on
  mobile), `Cotizar` pill right, hamburger opening a full-screen sheet on ≤768px.
  Background is a persistent `rgba(4,46,40,0.85)` with `backdrop-filter` on scroll only.
- Scroll reveals via one shared `IntersectionObserver`, fire once, `opacity` +
  `transform` only. Content is visible without JS (no `opacity:0` default; add the
  hidden class from JS).
- Parallax and custom cursor are gated behind
  `@media (hover: hover) and (pointer: fine)` and a JS-added `html.js-cursor` class.
  The requestAnimationFrame loop stops when the cursor is hidden or the tab is idle.
  `cursor: pointer` overrides are removed so there is never a double cursor.
- Grain overlay is kept but rendered as a static tiled PNG at 3% opacity, not a
  `mix-blend-mode` layer over the whole viewport.
- Hover on product cards, buttons and links per `DESIGN.md`. No fake hover on
  non-interactive tags.
- Only two easings exist: `cubic-bezier(0.16,1,0.3,1)` and `cubic-bezier(0.4,0,0.2,1)`.

## 12. ACCESSIBILITY

Target WCAG 2.1 AA, verified, not assumed.

- `<a href="#contenido">Saltar al contenido</a>` first in `<body>`; `<main id="contenido">` on every page.
- Every text/background pair in section 03 measured at ≥4.5:1 (≥3:1 for ≥24px). Include the breadcrumb, form labels, placeholders, cert text, footer, products intro.
- `:focus-visible` styles on every link, button, input, summary and the WhatsApp button.
- `prefers-reduced-motion: reduce` disables reveals, parallax, cursor, smooth scroll, the scroll pulse, and restores `cursor: auto`.
- No auto-moving content longer than 5s (ticker removed).
- Icon-only controls carry `aria-label`. External links say they open in a new window.
- Touch targets ≥44px. Nav order identical on all pages. `html lang="es-MX"`.
- Print stylesheet on product pages: dark text on white, header/cursor/grain hidden, spec lists expanded, certificate URLs printed after their links.

## 13. PERFORMANCE

Budgets, measured on a throttled mobile profile, cold cache:

- Home ≤600 KB fully scrolled, ≤250 KB above the fold. Product pages ≤350 KB.
- LCP <2.5s, CLS <0.05, no render-blocking third-party requests.
- Images: three widths each, webp + jpg, `srcset`/`sizes`, `width`/`height` on every `<img>`, lazy below the fold. Re-encode chipotle and melón webp at q75.
- Fonts: two Fraunces faces (900 roman, 400 italic) and two Outfit weights (300, 600), subset to Latin + Spanish, `font-display: swap`, preloaded.
- One CSS file, one JS file, both under 40 KB gzipped. No unpkg, no CDN.
- `og:image` per page at 1200×630, <200 KB, landscape crops of the product photo.
- Sitemap `lastmod` set from the build date. `llms.txt` rewritten with markdown links to the four product pages and a Certificaciones section listing the three PDFs.
- JSON-LD: logo dimensions corrected to 1107×487; `sameAs` populated `[DATO: Google Business Profile, LinkedIn]` or the key removed until then; `availableLanguage` limited to `es` until English ships.

## 14. OWNER INPUTS REQUIRED

Collect before the build starts. Placeholders ship if missing, but the page will say so.

| Item | Where used |
|---|---|
| Harvest months per product, fresh and dry | 04.5, 07, 09 |
| Minimum order per presentation | 07, 09 |
| Boxes per pallet, pallets per container | 07 |
| Incoterms offered, lead time, HS codes | 07, 09 |
| Melón °Brix range | 07 |
| Canonical address wording | 10 |
| Response-time promise | 10 |
| Founding year, hectares, names of the people in Nosotros | 04.6 |
| Primus GFS / SCS logo files and usage rights | 08 |
| Google Business Profile and LinkedIn URLs | 13 |
| Spec-sheet PDFs, or approval to generate them from the pages | 07 |

## 15. ACCEPTANCE

Done means every row passes, checked in a real browser at 375×667 and 1440×900.

- [ ] All ten P0 findings in `AUDIT.md` closed, with the file:line cited in the commit that closes each.
- [ ] H1, primary CTA and certification strip visible at load on a 375×667 viewport.
- [ ] Header ≤72px on mobile; anchor links land with the heading fully visible.
- [ ] Zero requests to unpkg or any third-party script host.
- [ ] Lighthouse mobile: Performance ≥90, Accessibility 100, SEO 100 on all five pages.
- [ ] axe DevTools reports zero violations on all five pages.
- [ ] Schema validator: `Product`, `FAQPage`, `BreadcrumbList`, `Organization` with no errors or warnings.
- [ ] A quote submitted from `/chiltepin/` arrives with Producto preselected, and the sender sees a confirmation without JS and with a screen reader.
- [ ] Ficha técnica prints legibly to one page.
- [ ] `git diff --stat` shows the four product pages each under 400 lines after extracting shared CSS/JS.

## 16. NOT IN SCOPE

- New visual direction, new palette, new typography.
- English pages and `hreflang` (Phase 2, the largest remaining AEO gap once this ships).
- A CMS, a framework migration, or a form backend beyond FormSubmit.
- New photography.
