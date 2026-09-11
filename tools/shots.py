"""Full-page screenshots at exact viewports for visual review.

    python tools/shots.py http://127.0.0.1:8766/ home
    python tools/shots.py http://127.0.0.1:8766/melon/ melon --mobile-only

Writes <name>-desktop.jpg and <name>-mobile.jpg (mobile tiled into 3 panels) to OUT.
"""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image

OUT = os.environ.get("SHOTS_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_shots"))
VIEWPORTS = {"desktop": (1440, 900, 1), "mobile": (390, 844, 2)}


def tile(path, n=3, gap=16, scale=0.75):
    im = Image.open(path)
    ph = -(-im.height // n)
    sheet = Image.new("RGB", (im.width * n + gap * (n - 1), ph), (40, 40, 40))
    for i in range(n):
        sheet.paste(im.crop((0, i * ph, im.width, min(im.height, (i + 1) * ph))), (i * (im.width + gap), 0))
    sheet = sheet.resize((round(sheet.width * scale), round(sheet.height * scale)), Image.LANCZOS)
    sheet.save(path, quality=72)


def main(url, name, only=None):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for vp, (w, h, dpr) in VIEWPORTS.items():
            if only and vp != only: continue
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=dpr,
                                reduced_motion="reduce", locale="es-MX")
            page = ctx.new_page()
            page.goto(url, wait_until="networkidle")
            page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => { i.loading = 'eager'; })")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(800)
            # open the mobile menu screenshot separately
            path = os.path.join(OUT, f"{name}-{vp}.png")
            page.screenshot(path=path, full_page=True)
            im = Image.open(path).convert("RGB")
            jpg = path[:-4] + ".jpg"
            if vp == "desktop":
                im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS).save(jpg, quality=72)
            else:
                im.resize((390, round(im.height * 390 / im.width)), Image.LANCZOS).save(jpg, quality=80)
                tile(jpg)
            os.remove(path)
            print(vp, Image.open(jpg).size, jpg)
            ctx.close()
        b.close()


if __name__ == "__main__":
    url, name = sys.argv[1], sys.argv[2]
    only = "mobile" if "--mobile-only" in sys.argv else ("desktop" if "--desktop-only" in sys.argv else None)
    main(url, name, only)
