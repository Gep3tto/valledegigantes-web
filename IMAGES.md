# Images

All images live at the repo root because the site is served from it (GitHub Pages) and the URLs are indexed and used as Open Graph images. Do not move or rename them.

## Web files (tracked)

| Name pattern | What it is | Formats |
|---|---|---|
| `logo` | Brand logo | png, webp |
| `rancho`, `rancho-1920` | Hero photo of the ranch | jpg, webp |
| `chiltepin`, `jalapeno`, `chipotle`, `melon` | Product hero photo | jpg, webp |
| `chiltepin-1200`, `jalapeno-1200` | Product hero resized to 1200 px wide | jpg |
| `chiltepin-100g`, `chiltepin-1kg`, `chiltepin-10kg` | Chiltepín presentations | jpg, webp |
| `jalapeno-17kg`, `jalapeno-30kg` | Jalapeño presentations | jpg, webp |
| `chipotle-30kg` | Chipotle presentation | jpg, webp |
| `melon-granel` | Melón presentation | jpg, webp |

Chipotle and melón use the base `.jpg` at 1200 px, so they have no `-1200` variant.

## Source files (not tracked)

The original PNG exports for the presentation images are kept out of the repo to keep it lean:

```
C:\Users\Andres\Dropbox\AFER Greens\Branding\Web image sources\
```

Regenerate a jpg/webp from a source there, then commit only the jpg and webp.
