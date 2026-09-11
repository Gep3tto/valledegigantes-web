# Images

The site is served from the repo root on GitHub Pages. Full-size originals stay at the
root under their historical names because those URLs are indexed and used as Open Graph
and schema images. Responsive variants live in `/img` and are generated, never edited.

## Root originals (tracked)

| Name | What it is | Source |
|---|---|---|
| `logo` | Brand logo | Owner |
| `rancho`, `rancho-1920` | Storm over the chile field | Photograph |
| `chiltepin`, `chiltepin-1200` | Chiltepín in hand over the drying bed | Photograph |
| `jalapeno`, `jalapeno-1200` | Harvest crew emptying a bucket into a bin | Photograph |
| `melon` | Cantaloupe on desert soil, one cut open | Generated (gpt-image-2), see SPEC.md §14 |
| `chipotle` | Dried chipotles on a wooden drying tray | Generated |
| `chiltepin-100g`, `chiltepin-1kg`, `chiltepin-10kg` | Chiltepín presentations | Generated |
| `jalapeno-17kg`, `jalapeno-30kg` | Jalapeño presentations | Generated |
| `chipotle-30kg` | Chipotle presentation | Generated |
| `melon-granel` | Melon bulk bin | Generated |

Each ships as `.jpg` plus `.webp`.

## Generated variants (`/img`, tracked, do not edit)

Made by `python tools/images.py` from the root originals:

- Hero: `rancho-768/1280/1920`
- Product heroes and home card: `<name>-480/960/1440`
- Home row thumbnails and "otros productos": `<name>-112/224` (square crops)
- Presentations: `<name>-480/960`
- Link previews: `og-home`, `og-melon`, `og-chiltepin`, `og-jalapeno`, `og-chipotle` at 1200×630

Re-run the script after replacing any root original.

## Sources (not tracked)

Original PNG exports and the full-resolution generated files live outside the repo:

```
C:\Users\Andres\Dropbox\AFER Greens\Branding\Web image sources\
```

To replace an image: put the new original there, export a `.jpg` (quality 82) and a
`.webp` (quality 78) to the repo root under the existing name, then run
`python tools/images.py <name>`.
