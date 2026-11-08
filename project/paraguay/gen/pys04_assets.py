"""pys04 derived assets: 2.5D layers of the ueno tower (Reuters aerial), Visión Banco plate.
Run: .venv/bin/python project/paraguay/gen/pys04_assets.py  (from the repo root)"""
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import json, os
SRC = "assets/paraguay/shared/photos/ueno_tower_aerial_reuters.jpg"
OUT = "assets/paraguay/pys04/derived"
os.makedirs(OUT, exist_ok=True)
im = Image.open(SRC).convert("RGB")
W, H = im.size
poly = [(525, 271), (1379, 271), (1381, 351), (1427, 353), (1419, 700), (1402, 1080), (513, 1080), (499, 700),
        (490, 516), (461, 507), (459, 355), (524, 351)]
m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon(poly, fill=255)
m = m.filter(ImageFilter.GaussianBlur(1.6))
tower = im.copy(); tower.putalpha(m)
tower.save(f"{OUT}/tower_fg.png")
# backdrop: fill the tower area by repeatedly smearing the neighbours in (cheap inpaint), then blur that area
bg = im.copy()
hole = Image.new("L", (W, H), 0); ImageDraw.Draw(hole).polygon(poly, fill=255)
hole = hole.filter(ImageFilter.MaxFilter(9))
fill = im.copy()
# horizontal smear: for each row, linear blend between left and right edge colours of the hole
px = fill.load(); hp = hole.load()
for y in range(H):
    xs = [x for x in range(0, W, 1) if hp[x, y] > 0]
    if not xs: continue
    x0, x1 = max(0, xs[0] - 6), min(W - 1, xs[-1] + 6)
    c0, c1 = im.getpixel((x0, y)), im.getpixel((x1, y))
    for x in range(xs[0], xs[-1] + 1):
        f = (x - x0) / max(1, x1 - x0)
        px[x, y] = tuple(int(c0[i] * (1 - f) + c1[i] * f) for i in range(3))
fill = fill.filter(ImageFilter.GaussianBlur(14))
bg.paste(fill, (0, 0), hole.filter(ImageFilter.GaussianBlur(6)))
bg.save(f"{OUT}/tower_bg.jpg", quality=90)
json.dump({"src": SRC, "size": [W, H], "layers": {"tower_bg.jpg": [0, 0], "tower_fg.png": [0, 0]}, "poly": poly},
          open(f"{OUT}/tower_layout.json", "w"), indent=1)
print("ok")

# ---- map crop around Paraguay from the kit's south_america_night (native px, 1:1) ----
import re
X0, Y0, MW, MH = 1860, 2700, 2160, 1215   # crop box in south_america px (camera can push ~12 %)
sa = Image.open("assets/maps/kit/south_america_night.jpg").convert("RGB")
sa.crop((X0, Y0, X0 + MW, Y0 + MH)).save(f"{OUT}/py_night_crop.jpg", quality=92)
s = open("assets/maps/kit/south_america_overlay.svg").read()
paths = {}
for cid in ["c-paraguay", "river-paraguay", "river-parana"]:
    paths[cid] = re.search(r'<path id="%s"[^>]* d="([^"]*)"' % cid, s).group(1)
json.dump({"crop": [X0, Y0, MW, MH], "paths": paths}, open(f"{OUT}/py_map_paths.json", "w"))
print("map ok")
