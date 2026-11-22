"""cts13 derived map layers (run with .venv/bin/python from the repo root).
sinaloa: northern-Sinaloa region fill + Sinaloa state outline as transparent PNGs in the kit's sinaloa pixel space (half resolution)."""
import re, os
from PIL import Image, ImageDraw, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
KIT = os.path.join(ROOT, "assets/maps/kit")
OUT = os.path.join(ROOT, "assets/cartels/cts13/derived")

def rings(svg, pid):
    m = re.search(r'id="' + pid + r'"[^>]*\sd="([^"]*)"', svg)
    out = []
    for sub in re.split(r"(?=M)", m.group(1)):
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sub)]
        if len(pts) > 2: out.append(pts)
    return out

def layer(region, pid, w, h, fill=None, stroke=None, width=3, scale=0.5, blur=0):
    svg = open(os.path.join(KIT, region + "_overlay.svg")).read()
    W, H = int(w * scale), int(h * scale)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for r in rings(svg, pid):
        q = [(x * scale, y * scale) for x, y in r]
        if fill: d.polygon(q, fill=fill)
        if stroke: d.line(q + [q[0]], fill=stroke, width=width, joint="curve")
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    return im

if __name__ == "__main__":
    layer("sinaloa", "rg-northern_sinaloa", 4027, 4060, fill=(236, 100, 36, 255)).save(os.path.join(OUT, "sin_north_fill.png"), optimize=True)
    layer("sinaloa", "rg-northern_sinaloa", 4027, 4060, stroke=(247, 180, 140, 255), width=3).save(os.path.join(OUT, "sin_north_edge.png"), optimize=True)
    layer("sinaloa", "st-sinaloa", 4027, 4060, stroke=(243, 237, 225, 255), width=2).save(os.path.join(OUT, "sin_state_edge.png"), optimize=True)
    print("ok")
