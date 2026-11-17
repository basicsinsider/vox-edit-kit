"""nvs04 derived map assets (run from repo root with .venv/bin/python).
- us_fill.png      : USA fill (ice) + outline in us_* kit pixel space, half resolution (3196x1762)
- world_night_8k.jpg: world_night.jpg downscaled to 8192x4096 (x=(lon+180)*22.7556, y=(90-lat)*22.7556)
- taiwan_sea.txt   : Taiwan path from southeast_asia_overlay.svg (inlined into the composition)
"""
import re, pathlib
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
K = pathlib.Path("assets/maps/kit"); O = pathlib.Path("assets/nvidia/nvs04/derived")

def subpaths(d):
    out = []
    for sp in re.split(r"(?=M)", d):
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?\d+\.?\d*,-?\d+\.?\d*", sp)]
        if len(pts) > 2: out.append(pts)
    return out

s = (K / "us_overlay.svg").read_text()
d = re.search(r'<path id="c-united_states_of_america"[^>]* d="([^"]*)"', s).group(1)
W, H, f = 6392 // 2, 3524 // 2, 0.5
fill = Image.new("L", (W, H), 0); dr = ImageDraw.Draw(fill)
line = Image.new("L", (W, H), 0); dl = ImageDraw.Draw(line)
for pts in subpaths(d):
    q = [(x * f, y * f) for x, y in pts]
    if max(abs(q[i][0] - q[i - 1][0]) for i in range(1, len(q))) > 400: continue
    dr.polygon(q, fill=255); dl.line(q + [q[0]], fill=255, width=3)
ice = (42, 159, 201); icel = (159, 220, 240)
img = Image.new("RGBA", (W, H), ice + (0,))
a = fill.point(lambda v: int(v * 0.55))
img.putalpha(a)
lc = Image.new("RGBA", (W, H), icel + (255,)); lc.putalpha(line)
img = Image.alpha_composite(img, lc)
img.save(O / "us_fill.png", optimize=True)

w = Image.open(K / "world_night.jpg"); w.resize((8192, 4096), Image.LANCZOS).save(O / "world_night_8k.jpg", quality=88)

s = (K / "southeast_asia_overlay.svg").read_text()
d = re.search(r'<path id="c-taiwan"[^>]* d="([^"]*)"', s).group(1)
(O / "taiwan_sea.txt").write_text(d)
print("ok", len(d))
