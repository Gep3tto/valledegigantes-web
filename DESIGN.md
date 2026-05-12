---
name: AFER Greens / Valle de Gigantes
description: Certified artisanal chile and melon exporter from Saucillo, Chihuahua — premium B2B brand site.
colors:
  harvest-amber:       "#F7931E"
  harvest-amber-light: "#FBBD6E"
  harvest-amber-glow:  "#FFF3E0"
  cantera-deep:        "#042E28"
  cantera-mid:         "#07433A"
  cantera-teal:        "#0D6558"
  cantera-light:       "#1A8A78"
  agave-pale:          "#A8C4A9"
  agave-sage:          "#688F6A"
  agave-soft:          "#E8F0E8"
  scs-green:           "#78A22F"
  white:               "#FDFCFA"
  snow:                "#F7F5F0"
  pearl:               "#EDEAE3"
  fog:                 "#D5D0C6"
  stone:               "#9B9585"
  slate:               "#6B6560"
  charcoal:            "#3D3A35"
  ink:                 "#1D1B18"
typography:
  display:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(3.2rem, 7vw, 7rem)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: "normal"
  headline:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(2.4rem, 5vw, 4.5rem)"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: "normal"
  title:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(1.4rem, 2.5vw, 1.9rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "normal"
  body:
    fontFamily: "'Outfit', -apple-system, sans-serif"
    fontSize: "clamp(1rem, 1.5vw, 1.15rem)"
    fontWeight: 300
    lineHeight: 1.75
    letterSpacing: "normal"
  label:
    fontFamily: "'Outfit', -apple-system, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.28em"
rounded:
  pill:   "100px"
  card:   "6px"
  input:  "8px"
  icon:   "10px"
  wrap:   "12px"
  circle: "50%"
spacing:
  section-v: "clamp(80px, 12vh, 140px)"
  section-h: "clamp(24px, 6vw, 100px)"
  gap-grid:  "clamp(40px, 6vw, 100px)"
  gap-card:  "28px"
components:
  button-primary:
    backgroundColor: "{colors.harvest-amber}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "16px 38px"
  button-primary-hover:
    backgroundColor: "{colors.harvest-amber-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "16px 38px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.agave-pale}"
    rounded: "{rounded.pill}"
    padding: "15px 34px"
  button-ghost-hover:
    backgroundColor: "rgba(255,255,255,0.08)"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "15px 34px"
  button-submit:
    backgroundColor: "{colors.harvest-amber}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "18px 40px"
    width: "100%"
  input-default:
    backgroundColor: "rgba(255,255,255,0.05)"
    textColor: "{colors.white}"
    rounded: "{rounded.input}"
    padding: "14px 18px"
  input-focus:
    backgroundColor: "rgba(247,147,30,0.06)"
    textColor: "{colors.white}"
    rounded: "{rounded.input}"
    padding: "14px 18px"
  card-light:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.card}"
    padding: "44px 32px 36px"
  card-dark:
    backgroundColor: "rgba(168,196,169,0.05)"
    rounded: "{rounded.card}"
    padding: "32px 28px"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.agave-pale}"
  nav-cta:
    backgroundColor: "{colors.harvest-amber}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "9px 24px"
---

# Design System: AFER Greens / Valle de Gigantes

## 1. Overview

**Creative North Star: "The Export Estate"**

This is the visual language of a Chihuahuan terroir estate seen through the eye of an international buyer: a premium certified supplier that communicates confidence through restraint, not decoration. The aesthetic owes more to a high-end mezcal house or a single-origin coffee exporter than to any agricultural commodity site. Surfaces are authoritative and dark; the accent is warm but controlled; nothing shouts.

The dominant ground is deep cantera teal, a near-black that reads as serious and grounded, not tech-dark. Harvest amber appears sparingly — a single heat source on the page. Agave pale carries secondary text and supporting tone, connecting the amber and the dark without softening them. Light sections (certification, presentation) switch to off-white snow to create breathing room, but they stay in the same family of warm-tinted neutrals.

Motion is minimal and purposeful: staggered entrances, parallax scroll, and hover reveals — none of it decorative. The interface does not perform; it invites scrutiny. An export buyer should feel they are looking at a supplier that has nothing to hide and everything to show.

This system explicitly rejects: generic agricultural-commodity aesthetics (stock tractors, green-yellow palette, clip-art certifications); hipster-foodie warmth (kraft textures, hand-lettered logotypes, Instagram-organic feel); SaaS/tech-startup patterns (hero metrics on gradient backgrounds, card grids, Inter everywhere); and institutional bureaucracy (heavy tables, muted government-gray tone).

**Key Characteristics:**
- Deep cantera teal base with a single amber accent at ≤10% coverage per surface
- Fraunces (serif) for all display and identity moments; Outfit (sans) for all body, label, and interface copy
- Full-capsule pill buttons; gently curved cards (6px); near-flat elevation with amber glow on CTAs only
- Fluid spacing and type scales via `clamp()` — no breakpoint-specific magic numbers
- Grain overlay (fixed, `mix-blend-mode: overlay`) throughout all dark sections
- Custom cursor on desktop (amber dot + trailing ring); disabled on mobile


## 2. Colors: The Cantera Palette

Three chromatic families — amber heat, cantera depth, agave support — grounded in a warm-tinted neutral ramp. Every neutral is tinted toward the brand hue; pure `#000` and `#fff` are prohibited.

### Primary
- **Harvest Amber** (`#F7931E`, `oklch(70% 0.175 55)`): The single heat source. Used for: primary CTA buttons and their glow, section eyebrow labels, product tag accents, nav underline animation, amber-on-dark text emphasis. Never used as a background for body text or as a dominant surface.
- **Harvest Amber Light** (`#FBBD6E`, `oklch(80% 0.14 60)`): Hover state only. The button lightens on hover — it does not darken. Appears nowhere at rest.
- **Harvest Amber Glow** (`#FFF3E0`, `oklch(97% 0.03 75)`): Tinted background for amber-related hover states on light surfaces (e.g. pillar cards on hover). Never used as a section background.

### Secondary
- **Cantera Deep** (`#042E28`, `oklch(18% 0.04 185)`): The primary surface. Body background, footer, hero base. The darkest teal — grounding everything.
- **Cantera Mid** (`#07433A`, `oklch(27% 0.05 185)`): Contact section and deep layering. One step above Deep.
- **Cantera Teal** (`#0D6558`, `oklch(42% 0.065 185)`): Product section background, pillar icon fill. The mid-tone entry into the teal scale.
- **Cantera Light** (`#1A8A78`, `oklch(52% 0.07 185)`): Occasional accent within teal sections. Not a standalone surface.

### Tertiary
- **Agave Pale** (`#A8C4A9`, `oklch(78% 0.04 155)`): Body text on dark backgrounds, nav links at rest, supporting descriptors. The primary text tone on cantera surfaces.
- **Agave Sage** (`#688F6A`, `oklch(58% 0.055 155)`): Less-used green; about section text color. Darker and more saturated than Agave Pale.
- **Agave Soft** (`#E8F0E8`, `oklch(94% 0.018 155)`): Very pale sage; minor backgrounds on light sections.
- **SCS Green** (`#78A22F`, `oklch(56% 0.12 130)`): Reserved exclusively for Primus GFS / SCS Global certification references. Do not use for any other purpose.

### Neutral
- **White** (`#FDFCFA`, `oklch(99% 0.004 90)`): Primary light-section surface (Nosotros, Certificaciones). Not pure white — warm-tinted.
- **Snow** (`#F7F5F0`, `oklch(97% 0.007 85)`): Secondary light surface; pillar card backgrounds; light section padding areas.
- **Pearl** (`#EDEAE3`, `oklch(93% 0.01 85)`): Borders and dividers on light sections. Card borders in cert section.
- **Fog** (`#D5D0C6`, `oklch(84% 0.01 80)`): Lighter divider; less used.
- **Stone** (`#9B9585`, `oklch(64% 0.01 75)`): Muted UI labels — contact section `h4` labels, cert number metadata. Never for body copy.
- **Slate** (`#6B6560`, `oklch(46% 0.01 65)`): Supporting text on light backgrounds (certs intro, pres intro). Verify 4.5:1 against Snow before use.
- **Charcoal** (`#3D3A35`, `oklch(28% 0.01 65)`): Dark text on light surfaces; rarely needed given the split between dark and light sections.
- **Ink** (`#1D1B18`, `oklch(12% 0.008 70)`): Text on amber CTA buttons and amber backgrounds (stats bar). The only near-black in the system.

### Named Rules
**The Rarity Rule.** Harvest Amber covers ≤10% of any given dark surface. A page where amber is everywhere has lost its edge; a page where it appears once or twice has authority. The amber strip and CTA buttons are the quota.

**The SCS Quarantine Rule.** SCS Green (`#78A22F`) is reserved for Primus GFS certification contexts only. Using it for decorative accents or non-certification UI dilutes the credibility signal it carries.

**The Warm Tint Rule.** Every neutral in this system is tinted toward the brand hue. Pure `#000000` and `#ffffff` are prohibited. The darkest surface is Cantera Deep; the lightest is White. Nothing outside this ramp.


## 3. Typography

**Display Font:** Fraunces (Google Fonts, optical-size-aware serif with `opsz` axis, 9–144; fallback: Georgia, serif)
**Body Font:** Outfit (Google Fonts, geometric humanist sans; fallback: -apple-system, sans-serif)

**Character:** Fraunces is a newspaper-editorial serif with dramatic weight contrast at 900 and soft italic personality at lower weights — it signals authority and origin without formality. Outfit is clean and legible at small sizes without the coldness of geometric grotesques; it pairs with Fraunces by staying neutral. The pairing reads as: a commodity that takes itself seriously enough to have a byline.

### Hierarchy
- **Display** (Fraunces 900, `clamp(3.2rem, 7vw, 7rem)`, line-height 1.0): Hero `h1` only. Used once per page, never repeated. Italic `<em>` in amber for the key brand phrase.
- **Headline** (Fraunces 900, `clamp(2.4rem, 5vw, 4.5rem)`, line-height 1.05): Section `h2` titles throughout. Italic `<em>` in amber for the thematic word per section. Sentence-case.
- **Title** (Fraunces 700, `clamp(1.4rem, 2.5vw, 1.9rem)`, line-height 1.15): Product card headings (`h3`), cert card headings, form section titles. Less dramatic — carries content, not identity.
- **Body** (Outfit 300, `clamp(1rem, 1.5vw, 1.15rem)`, line-height 1.75): All paragraph copy. Max line length 520px or ~65ch on desktop. Weight 300 (light) to let Fraunces headlines dominate.
- **Label** (Outfit 600, `0.72–0.82rem`, letter-spacing `0.18–0.30em`, uppercase): Section eyebrow labels, stat labels, tag content, contact `h4` metadata, nav links. Always uppercase, always tracked. The secondary rhythm element that gives structure without competing with Fraunces.

### Named Rules
**The Fraunces-Only Rule.** Fraunces is used exclusively for display, headline, and title roles. It never appears in label, body, or UI copy. Outfit never appears in headline or display roles. The split is absolute.

**The Italic Amber Rule.** Each `h1` and `h2` contains exactly one `<em>` rendered in italic Fraunces and Harvest Amber. This is the typographic heartbeat of the system. Do not use `<em>` for general emphasis; do not use amber on non-italic Fraunces.

**The 65ch Rule.** Body paragraphs are capped at ~520px / 65ch max-width. Wider line lengths on large viewports are prohibited. Apply `max-width: 520px` or equivalent on all `.sub`, `.intro`, and `.tagline` elements.


## 4. Elevation

This system is flat by default, with a single intentional exception: amber glow on primary CTAs. Surfaces do not use shadows to separate from each other; section boundaries are communicated through background-color contrast (deep cantera vs. snow vs. cantera teal). Shadows appear only as state responses (hover) or as a singular brand signal (CTA glow).

### Shadow Vocabulary
- **CTA Amber Glow** (`box-shadow: 0 4px 28px rgba(247,147,30,0.35)`): Applied to all primary amber buttons at rest. The only shadow that appears without interaction. It signals "this is where to act."
- **CTA Amber Hover** (`box-shadow: 0 10px 40px rgba(247,147,30,0.5)`): The glow deepens and lifts on hover (`translateY(-3px)`). Not a separate component — the hover intensification of the glow.
- **Card Ambient** (`box-shadow: 0 2px 20px rgba(4,46,40,0.04)`): Barely perceptible shadow on light-section cards (cert cards, pres cards). Its job is to lift the card 1px from the surface — not to dramatize it. If you can clearly see the shadow, it is too strong.
- **Card Hover** (`box-shadow: 0 10px 40px rgba(4,46,40,0.08)`): Appears on `transform: translateY(-4px)` hover. Still teal-tinted, not black — stays in the system's hue.
- **Product Image** (`box-shadow: 0 20px 60px rgba(4,46,40,0.5)`): The heaviest shadow in the system. Used once per product page on the hero product image. Grounds the photography against the dark background.

### Named Rules
**The Flat Surface Rule.** Surfaces between sections carry no shadows between them. Section depth is achieved through background contrast, not elevation. If you are reaching for a section-level shadow, use a background-color change instead.

**The One Glow Rule.** Amber glow belongs exclusively to primary CTA buttons. No other element in the system uses an amber-tinted shadow. Aglow amber on cards, headers, or decorative elements dilutes the CTA signal.


## 5. Components

### Buttons
Buttons in this system are confident but not loud. The pill shape (100px radius) is the dominant trait — it communicates approachability without sacrificing authority. Transitions are deliberate and visible; hover feedback is clear without theatrics.

- **Shape:** Full capsule (100px radius). No rectangular or slightly-rounded buttons in this system.
- **Primary:** Harvest Amber background (`#F7931E`), Ink text (`#1D1B18`), padding `16px 38px`, amber glow `0 4px 28px rgba(247,147,30,0.35)` at rest. Hover: lightens to Harvest Amber Light (`#FBBD6E`), lifts `translateY(-3px)`, glow deepens.
- **Ghost:** Transparent background, Agave Pale text, `1.5px solid rgba(168,196,169,0.4)` border, padding `15px 34px`. Hover: background `rgba(255,255,255,0.08)`, text White, border White. Used alongside Primary as a secondary action.
- **Nav CTA:** Same as Primary but smaller (`9px 24px`), lighter glow (`0 2px 16px`). The nav entry point to the quote form.
- **Submit:** Full-width Primary variant, padding `18px 40px`. `cursor: none` on desktop (inherits custom cursor from body).
- **Transition:** `transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s, background 0.3s`. No bounce, no elastic.

### Cards / Containers
Cards are not the default layout choice. When used, they are understated: minimal border, barely visible shadow, rounded corners that whisper rather than shout.

- **Light Section Cards** (cert cards, pres cards): White background (`#FDFCFA`), `1px solid {colors.pearl}`, `0 2px 20px rgba(4,46,40,0.04)` shadow, `6px` radius, `44px 32px 36px` padding. Hover: `translateY(-4px)`, shadow intensifies to `0 10px 40px rgba(4,46,40,0.08)`.
- **Dark Section Specs** (spec cards): `rgba(168,196,169,0.05)` background, `1px solid rgba(168,196,169,0.1)` border, no visible shadow, `6px` radius, `32px 28px`. Hover: background shifts to `rgba(247,147,30,0.05)`, `translateY(-4px)`.
- **Contact Form Wrap:** `rgba(255,255,255,0.04)` background, `1px solid rgba(168,196,169,0.12)` border, `12px` radius, `clamp(32px, 4vw, 56px)` padding. This is a glass-adjacent container — justified by function (it isolates the form on a dark surface), never replicated decoratively.
- **Pillar Cards** (about section): `#F7FAF7` background, `1px solid rgba(13,101,88,0.12)` border, `8px` radius, `20px` padding. Hover: border `rgba(247,147,30,0.35)`, background `#FFF8EE`. 2×2 grid only; never more or fewer.

### Inputs / Fields
Form inputs sit on the dark cantera contact section. They use semi-transparent tinted glass backgrounds to stay in the surface family, not white boxes that would look grafted on.

- **Default:** `rgba(255,255,255,0.05)` background, `1.5px solid rgba(168,196,169,0.18)` border, `8px` radius, Outfit 0.95rem, `14px 18px` padding, White text. Placeholder: `rgba(168,196,169,0.35)`.
- **Focus:** Border shifts to Harvest Amber, background `rgba(247,147,30,0.06)`, focus ring `0 0 0 3px rgba(247,147,30,0.45)`. The focus ring must meet WCAG 2.2 AA — use minimum 45% opacity, not 10%.
- **Select:** `-webkit-appearance: none`; styled identically to text inputs. Option background uses `{colors.cantera-mid}`.
- **Textarea:** `min-height: 120px`, `resize: vertical` only.

### Navigation
The header is transparent at page top and transitions to a blurred dark glass on scroll. On product subpages, the scrolled state is active from load.

- **At rest:** Transparent, no border, no background. Logo and links appear directly over the hero image.
- **Scrolled (`.scrolled`):** `rgba(4,46,40,0.92)` background, `backdrop-filter: blur(18px) saturate(160%)`, `1px solid rgba(247,147,30,0.12)` border-bottom. Transition `0.5s ease-in-out`.
- **Nav links:** Outfit 500, `0.9rem`, letter-spacing `0.08em`, Agave Pale at rest, White on hover. Underline animation: a `width: 0 → 100%` pseudo-element in Harvest Amber, `2px` height, `0.35s ease-out-expo`.
- **Logo:** Inverted white filter (`brightness(0) invert(1)`). Height `100px` at rest → `64px` on scroll (`0.4s` ease-out-expo). On mobile: `70px` fixed.
- **Mobile:** Nav stacks vertically at ≤768px. `cursor: auto` restored; custom cursor elements display none.

### Product Cards (Signature Component)
Full-bleed photography cards with overlay gradients, numbered in Fraunces, and reveal text on hover. The numbering system (`01` through `04`) is structural identity, not decoration.

- **Container:** `position: relative`, `overflow: hidden`, `aspect-ratio: 4/3` (desktop), `aspect-ratio: 3/4` (mobile).
- **Image:** `object-fit: cover`, `filter: saturate(0.8) brightness(0.8)` at rest. Hover: `transform: scale(1.06)`, `filter: saturate(1) brightness(0.88)`.
- **Overlay:** `linear-gradient(to top, rgba(4,46,40,0.95) 0%, rgba(4,46,40,0.3) 55%, transparent 100%)`. Hover: deepens to `0.98` at bottom, adds `rgba(247,147,30,0.08)` at top.
- **Number:** Fraunces 900, `5rem`, `rgba(247,147,30,0.2)` at rest → `0.5` on hover, `translateY(-4px)` on hover.
- **Tag:** Outfit 600, `0.7rem`, letter-spacing `0.18em`, uppercase, Harvest Amber text, `1px solid rgba(247,147,30,0.4)` border, `100px` radius, `5px 14px` padding. No fill — outline chip only.

### Ticker Strip (Signature Component)
An amber marquee band between the hero and the first content section. `aria-hidden="true"`. Outlet 600, `0.82rem`, letter-spacing `0.18em`, uppercase, Ink text on Harvest Amber background. Infinite scroll via `@keyframes marquee` on `transform: translateX(-50%)`. Two copies of content ensure seamless loop.


## 6. Do's and Don'ts

### Do:
- **Do** use Harvest Amber (`#F7931E`) for CTAs, eyebrow labels, and single-word italic emphasis in Fraunces headings — and nowhere else.
- **Do** tint every neutral toward the brand hue. The lightest surface is `#FDFCFA` (White); the darkest is `#042E28` (Cantera Deep). Pure `#000` and `#fff` are prohibited.
- **Do** use `<em>` in Fraunces headings to render in italic amber — one `<em>` per heading, the thematic anchor word.
- **Do** apply `will-change: transform` and position cursor elements with `transform: translate()`, not `top`/`left`, to keep the cursor compositor-only.
- **Do** verify 4.5:1 contrast ratio for all text against its background before shipping. Pay special attention to `rgba`-opacity text on dark surfaces (footer, stat labels).
- **Do** honor `prefers-reduced-motion` for all scroll-reveal animations and the parallax hero.
- **Do** use Fraunces exclusively for display, headline, and title roles; Outfit exclusively for body, label, and interface copy. The split is absolute.
- **Do** keep product photography desaturated at rest (`saturate(0.8)`) and let hover restore color — it makes the page feel like it responds to attention.
- **Do** reserve SCS Green (`#78A22F`) for Primus GFS certification contexts only. Never use it as a decorative accent.
- **Do** use `clamp()` for all font sizes and horizontal padding. Never hardcode breakpoint-specific size overrides.

### Don't:
- **Don't** make this look like a generic agro-commodity site. No stock-photo tractors, no green-and-yellow palette, no clip-art certification badges. This is an export estate, not a co-op catalog.
- **Don't** use hipster-foodie aesthetics. No kraft paper textures, no hand-lettered treatments, no warm Instagram-organic softness. The brand is serious and northern, not cozy and artisanal-market.
- **Don't** import SaaS or tech-startup patterns. No hero metrics on gradient backgrounds (big number + small label + gradient = the banned hero-metric template), no card grids of icon + heading + text, no Inter anywhere in this system.
- **Don't** allow institutional or government tone. No heavy data tables as a layout choice, no bureaucratic gray, no overly formal language or visual density.
- **Don't** use `border-left` or `border-right` greater than 1px as a colored decorative accent on cards, list items, or specification items. This is the banned side-stripe pattern. Use leading icons, tinted backgrounds, or full borders instead.
- **Don't** use gradient text (`background-clip: text` with a gradient). A single solid color with weight or size contrast carries all needed emphasis.
- **Don't** use glassmorphism decoratively. The contact form wrap and scrolled header use backdrop-filter because they are functionally justified. Any other blur or glass effect is prohibited.
- **Don't** animate CSS layout properties (width, height, top, left, padding, margin). All motion must be on `transform` and `opacity` only.
- **Don't** use bounce, elastic, or spring easing. The only easing in this system is `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-expo) and `cubic-bezier(0.4, 0, 0.2, 1)` (ease-in-out). Period.
- **Don't** remove `outline` from interactive elements without providing a WCAG 2.2 AA-compliant custom focus indicator. The focus ring on inputs must be visible at minimum 45% amber opacity.
- **Don't** use Harvest Amber as a background for body text sections. It is a CTA and accent color, not a surface. The stats bar amber background is the sole exception — and even there, text must be Ink at full opacity for contrast compliance.
- **Don't** let the footer text fall below WCAG AA contrast. `rgba(168,196,169,0.4)` on Cantera Deep fails (≈ 2.5:1). Footer text must be ≥ 75% opacity Agave Pale on dark surfaces.
