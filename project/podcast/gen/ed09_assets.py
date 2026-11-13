#!/usr/bin/env python3
"""ED09 derived assets for pd17–pd20 (idempotent). Run: .venv/bin/python project/podcast/gen/ed09_assets.py"""
import json, re, os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = lambda *a: os.path.join(R, *a)
K = 3840 / 6392.0

# --- US maps (kit us_* 6392x3524 -> 3840x2117) ---
def us(src, dst, grey):
    if os.path.exists(P(dst)): return
    im = Image.open(P(src)).convert("RGB").resize((3840, 2117), Image.LANCZOS)
    if grey:   # cool silicon grey atlas (paper scene)
        g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)
        im = ImageOps.colorize(g, (58, 63, 74), (238, 238, 232), mid=(176, 180, 186))
    im.save(P(dst), quality=88)
us("assets/maps/kit/us_atlas.jpg", "assets/podcast/pd18/us_atlas_silicon_3840.jpg", True)
us("assets/maps/kit/us_night.jpg", "assets/podcast/pd19/us_night_3840.jpg", False)

def scale_path(d, k):
    out = []
    for m in re.finditer(r"([MLZ])\s*(-?[\d.]+)?[ ,]*(-?[\d.]+)?", d):
        c, x, y = m.groups()
        out.append("Z" if c == "Z" else "%s%d %d" % (c, round(float(x) * k), round(float(y) * k)))
    return "".join(out)
sp = json.load(open(P("assets/c3/derived/c3s01/us_paths.json")))
states = {k: scale_path(v, K) for k, v in sp.items()}
def centroid(d):
    best = None
    for sub in d.split("M")[1:]:
        pts = [tuple(map(float, p.split())) for p in sub.replace("Z", "").split("L") if p.strip()]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        a = (max(xs) - min(xs)) * (max(ys) - min(ys))
        if best is None or a > best[0]: best = (a, [min(xs), min(ys), max(xs), max(ys)])
    return best[1]
out = {"size": [3840, 2117], "k": K, "states": states, "bbox": {k: centroid(v) for k, v in states.items()},
       "places": {"new_york": [5539.1 * K, 1235.2 * K], "albany": [5565.7 * K, 977.2 * K], "sacramento": [(-121.4944 + 126) * 106.533 * K, (50 - 38.5816) * 133 * K],
                  "san_francisco": [381.5 * K, 1625.9 * K]}}
json.dump(out, open(P("assets/podcast/pd18/us_paths_3840.json"), "w"), separators=(",", ":"))

# --- East Asia night (kit 6398x4950 -> 3199x2475; same space as assets/c6/derived/c6s01/paths.json east_asia) ---
dst = "assets/podcast/pd20/east_asia_night_3199.jpg"
if not os.path.exists(P(dst)):
    Image.open(P("assets/maps/kit/east_asia_night.jpg")).convert("RGB").resize((3199, 2475), Image.LANCZOS).save(P(dst), quality=88)
ea = json.load(open(P("assets/c6/derived/c6s01/paths.json")))["east_asia"]["d"]
json.dump({"size": [3199, 2475], "formula": "x=(lon-100)*63.975; y=(48-lat)*75", "china": ea["china"], "taiwan": ea["taiwan"]},
          open(P("assets/podcast/pd20/east_asia_paths.json"), "w"), separators=(",", ":"))
print("ok", {k: len(v) for k, v in states.items() if k in ("california", "new_york")}, sum(len(v) for v in states.values()))
