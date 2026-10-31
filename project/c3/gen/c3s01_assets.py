"""c3s01 derived assets (run: .venv/bin/python project/c3/gen/c3s01_assets.py from the repo root).
Outputs -> assets/c3/derived/c3s01/ : us_paths.json (kit us_overlay states, simplified, native 6392x3524 px),
pacific_taiwan.json, us_atlas_3840.jpg, hoover_tower_fg.png / _sky.jpg (2.5D), sv2014_halftone.png."""
import json, re, os, math
from PIL import Image, ImageFilter
import numpy as np
OUT = "assets/c3/derived/c3s01"; os.makedirs(OUT, exist_ok=True)
Image.MAX_IMAGE_PIXELS = None

def rdp(pts, eps):
    if len(pts) < 3: return pts
    a, b = np.array(pts[0]), np.array(pts[-1]); ab = b - a; L = np.hypot(*ab)
    P = np.array(pts)
    d = np.abs(ab[0] * (P[:, 1] - a[1]) - ab[1] * (P[:, 0] - a[0])) / L if L > 0 else np.hypot(*(P - a).T)
    i = int(np.argmax(d))
    if d[i] > eps: return rdp(pts[:i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]

def simplify(d, eps, minlen=0):
    out = []
    for sub in [s for s in d.split("M") if s.strip()]:
        nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", sub)]
        pts = [(nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2)]
        if len(pts) < 3: continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if max(xs) - min(xs) < minlen and max(ys) - min(ys) < minlen: continue
        if max(abs(pts[i][0] - pts[i - 1][0]) for i in range(1, len(pts))) > 400: continue  # antimeridian guard
        h = len(pts) // 2   # simplify the two halves separately (closed rings, MANUAL 4.2)
        s = rdp(pts[:h + 1], eps)[:-1] + rdp(pts[h:], eps)
        if len(s) < 3: continue
        out.append("M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in s) + "Z")
    return "".join(out)

def paths(svgfile, prefix):
    txt = open(svgfile).read()
    return {m.group(1): m.group(2) for m in re.finditer(r'<path id="' + prefix + r'([^"]+)"[^>]*? d="([^"]+)"', txt)}

if False: pass
us = paths("assets/maps/kit/us_overlay.svg", "st-")
if not us:  # attribute order fallback
    txt = open("assets/maps/kit/us_overlay.svg").read()
    us = {m.group(2): m.group(1) for m in re.finditer(r'<path[^>]*? d="([^"]+)"[^>]*? id="st-([^"]+)"', txt)}
us_s = {k: simplify(v, 2.2, 12) for k, v in us.items()}
json.dump(us_s, open(f"{OUT}/us_paths.json", "w"))
print("us states", len(us_s), sum(len(v) for v in us_s.values()))

pac = paths("assets/maps/kit/pacific_overlay.svg", "c-")
tw = simplify(pac.get("taiwan", ""), 0.8, 2)
json.dump({"taiwan": tw}, open(f"{OUT}/pacific_taiwan.json", "w"))
print("taiwan", len(tw))

im = Image.open("assets/maps/kit/us_atlas.jpg"); im.resize((3840, round(3524 * 3840 / 6392)), Image.LANCZOS).save(f"{OUT}/us_atlas_3840.jpg", quality=90)

# Hoover Tower 2.5D: sky key on the clear-blue Jan 2013 photo -> foreground (tower + palms) with alpha, and a sky plate
t = Image.open("assets/c3/photos/hoover_tower_jan2013.jpg").convert("RGB")
t = t.resize((1650, 2750), Image.LANCZOS)
a = np.asarray(t).astype(np.int16); r, g, b = a[..., 0], a[..., 1], a[..., 2]
sky = (b > r + 40) & (b > g + 5) & (b > 120)
m = (~sky).astype(np.uint8) * 255
mi = Image.fromarray(m).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
fg = t.copy(); fg.putalpha(mi); fg.save(f"{OUT}/hoover_tower_fg.png")
skyp = t.filter(ImageFilter.GaussianBlur(18)); skyp.save(f"{OUT}/hoover_tower_sky.jpg", quality=88)
print("hoover ok", sky.mean())

# USGS 1961 Palo Alto quad crop (C3S028): Stanford, HP garage, HP Page Mill, Varian, Fairchild 844 Charleston
u = Image.open("assets/c2/maps/usgs_palo_alto_1961_24k.jpg").convert("RGB")
u.crop((3500, 3000, 6588, 5600)).save(f"{OUT}/usgs_palo_alto_1961_crop.jpg", quality=88)   # origin (3500,3000)
# kit northeast atlas crop around New York (C3S013 panel, C3S014 map)
n = Image.open("assets/maps/kit/northeast_atlas.jpg").convert("RGB")
n.crop((300, 2300, 2900, 4129)).save(f"{OUT}/northeast_ny_crop.jpg", quality=88)            # origin (300,2300)
print("crops ok")
