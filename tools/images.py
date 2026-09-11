"""Generate responsive image variants for the site.

Reads the full-size originals at the repo root (or a path passed on the command line)
and writes width variants to /img as webp + jpg. Run from the repo root:

    python tools/images.py            # all products + hero
    python tools/images.py melon.jpg  # one file

Sources with transparent PNG originals live outside the repo (see IMAGES.md).
"""
import sys, os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img")

# name -> (widths, square thumb widths)
PLAN = {
    "rancho":         ([768, 1280, 1920], []),
    "melon":          ([480, 960, 1440], [112, 224]),
    "chiltepin":      ([480, 960, 1440], [112, 224]),
    "jalapeno":       ([480, 960, 1440], [112, 224]),
    "chipotle":       ([480, 960, 1440], [112, 224]),
    "chiltepin-100g": ([480, 960], []),
    "chiltepin-1kg":  ([480, 960], []),
    "chiltepin-10kg": ([480, 960], []),
    "jalapeno-17kg":  ([480, 960], []),
    "jalapeno-30kg":  ([480, 960], []),
    "chipotle-30kg":  ([480, 960], []),
    "melon-granel":   ([480, 960], []),
}
OG = {"og-home": "melon", "og-melon": "melon", "og-chiltepin": "chiltepin",
      "og-jalapeno": "jalapeno", "og-chipotle": "chipotle"}   # 1200x630 crops for link previews

WEBP_Q, JPG_Q = 78, 82


def save(im, path_base):
    im.save(path_base + ".webp", "WEBP", quality=WEBP_Q, method=6)
    im.save(path_base + ".jpg", "JPEG", quality=JPG_Q, optimize=True, progressive=True)


def variants(name):
    src = os.path.join(ROOT, name + ".jpg")
    if not os.path.exists(src):
        print("skip (no source):", name); return
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    widths, thumbs = PLAN[name]
    for w in widths:
        if w >= im.width: continue
        h = round(im.height * w / im.width)
        save(im.resize((w, h), Image.LANCZOS), os.path.join(OUT, f"{name}-{w}"))
    for t in thumbs:
        save(ImageOps.fit(im, (t, t), Image.LANCZOS, centering=(0.5, 0.45)), os.path.join(OUT, f"{name}-{t}"))
    print("ok:", name, widths, thumbs)


def og(name, source):
    src = os.path.join(ROOT, source + ".jpg")
    if not os.path.exists(src):
        print("skip (no source):", source); return
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=(0.5, 0.55)).save(
        os.path.join(OUT, name + ".jpg"), "JPEG", quality=80, optimize=True, progressive=True)
    print("ok:", name)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    args = [a.replace(".jpg", "") for a in sys.argv[1:]]
    for n in (args or list(PLAN)):
        variants(n)
    for n, s in OG.items():
        if not args or s in args:
            og(n, s)
