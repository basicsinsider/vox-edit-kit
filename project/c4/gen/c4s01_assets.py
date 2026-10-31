"""Derived assets for compositions/c4s01.html (map crops from assets/maps/kit + simplified country paths).
Run: .venv/bin/python project/c4/gen/c4s01_assets.py   → assets/c4/derived/c4s01/
"""
import re, json, pathlib
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = pathlib.Path("assets/maps/kit"); O = pathlib.Path("assets/c4/derived/c4s01"); O.mkdir(parents=True, exist_ok=True)
WPX = 45.5111

def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = (dx * dx + dy * dy) ** 0.5 or 1e-9
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / L
        if d > dmax: dmax, idx = d, i
    if dmax > eps: return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]

def paths(svgfile, ids):
    src = open(svgfile).read(); out = {}
    for cid in ids:
        m = re.search(r'<path id="c-%s"[^>]* d="([^"]+)"' % cid, src)
        if not m: print("missing", cid); continue
        out[cid] = [[(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", sub)] for sub in re.split(r"M", m.group(1).replace("Z","").replace("z","")) if sub.strip()]
    return out

def to_d(rings, f, eps, minlen=6):
    d = ""
    for r in rings:
        p = [f(x, y) for x, y in r]
        if max(abs(p[i][0] - p[i - 1][0]) for i in range(1, len(p))) > 400: continue  # antimeridian
        h = len(p) // 2
        p = rdp(p[:h + 1], eps)[:-1] + rdp(p[h:], eps)   # closed ring: simplify two halves
        if len(p) < 3: continue
        xs = [q[0] for q in p]; ys = [q[1] for q in p]
        if max(xs) - min(xs) < minlen and max(ys) - min(ys) < minlen: continue
        d += "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in p) + "Z"
    return d

import sys
ONLY_TW = "--tw" in sys.argv
res = {}
if not ONLY_TW:
    world_n = Image.open(K / "world_night.jpg")
    world_a = Image.open(K / "world_atlas.jpg")
    def crop(img, lon0, lat0, lon1, lat1, scale, name):
        box = tuple(int(round(v)) for v in ((lon0 + 180) * WPX, (90 - lat1) * WPX, (lon1 + 180) * WPX, (90 - lat0) * WPX))
        im = img.crop(box)
        if scale != 1: im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        im.convert("RGB").save(O / name, quality=88); print(name, im.size)
        return box, im.size

    # Eurasia (Warsaw Pact → China), native res
    box, size = crop(world_n, 2, 15, 138, 62, 1.0, "eurasia_night.jpg")
    wp = ["russia", "ukraine", "belarus", "lithuania", "latvia", "estonia", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan",
          "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan", "poland", "czechia", "slovakia", "hungary", "romania", "bulgaria", "albania", "germany", "china", "taiwan", "mongolia"]
    P = paths(K / "world_overlay.svg", wp)
    f = lambda x, y: (x - box[0], y - box[1])
    res["eurasia"] = {"size": size, "box": box, "d": {k: to_d(v, f, 4.0, 18) for k, v in P.items()}}
    lonlat = lambda lon, lat: ((lon + 180) * WPX - box[0], (90 - lat) * WPX - box[1])
    # inner German border (approx.) → clip polygon for East Germany (GDR)
    res["eurasia"]["gdr_clip"] = "M" + "L".join("%.0f %.0f" % lonlat(*p) for p in [(10.9, 55.5), (10.9, 54.0), (10.6, 53.4), (11.0, 52.9), (10.8, 52.2), (10.3, 51.6), (9.9, 51.3), (10.2, 50.6), (10.6, 50.3), (11.4, 50.4), (12.1, 50.3), (16, 50.3), (16, 55.5)]) + "Z"

    # Africa (night for C4S013–014, atlas for C4S016), native res
    box, size = crop(world_n, -60, -40, 95, 42, 1.0, "africa_night.jpg")
    crop(world_a, -60, -40, 95, 42, 1.0, "africa_atlas.jpg")
    af = ["ghana", "guinea", "nigeria", "senegal", "mali", "c_te_d_ivoire", "cameroon", "chad", "niger", "congo", "dem_rep_congo", "gabon",
          "central_african_rep", "madagascar", "somalia", "mauritania", "burkina_faso", "togo", "benin", "tanzania", "uganda", "kenya", "zambia",
          "malawi", "sudan", "s_sudan", "morocco", "tunisia", "algeria", "sierra_leone", "rwanda", "burundi", "libya", "egypt", "ethiopia", "liberia",
          "south_africa", "angola", "mozambique", "namibia", "botswana", "zimbabwe", "w_sahara", "eritrea", "djibouti", "somaliland", "gambia",
          "guinea_bissau", "eq_guinea", "lesotho", "eswatini"]
    P = paths(K / "world_overlay.svg", af)
    f = lambda x, y: (x - box[0], y - box[1])
    res["africa"] = {"size": size, "box": box, "d": {k: to_d(v, f, 2.0) for k, v in P.items()}}
    del world_n

    # War-room world plate (atlas, 0.375 → 6144×3072, ~17 px/deg)
    im = world_a.resize((6144, 3072), Image.LANCZOS); im.save(O / "world_atlas_6144.jpg", quality=86); print("world", im.size)
    del world_a, im

    # East Asia night 0.5 (China red / Taiwan celadon) — C4S017
    ea = Image.open(K / "east_asia_night.jpg"); s = 0.5
    ea.resize((int(ea.width * s), int(ea.height * s)), Image.LANCZOS).save(O / "east_asia_night_3199.jpg", quality=88)
    P = paths(K / "east_asia_overlay.svg", ["china", "taiwan", "japan", "south_korea", "north_korea", "mongolia", "vietnam", "philippines"])
    f = lambda x, y: (x * s, y * s)
    res["east_asia"] = {"size": [int(ea.width * s), int(ea.height * s)], "d": {k: to_d(v, f, 2.0, 8) for k, v in P.items()}}
    json.dump(res, open(O / "paths.json", "w"))
    for k, v in res.items(): print(k, {c: len(d) for c, d in v["d"].items()})

# Celadon Taiwan relief cut-out (motif: relief + celadon wash, alpha from the kit landmask) — C4S010/014/017
if True:
    from PIL import ImageOps, ImageFilter
    tw = Image.open(K / "taiwan_atlas.jpg").convert("L"); mk = Image.open(K / "taiwan_landmask.png").convert("L")
    s = 900 / tw.height; size = (int(tw.width * s), 900)
    tw = ImageOps.autocontrast(tw.resize(size, Image.LANCZOS), cutoff=1); mk = mk.resize(size, Image.LANCZOS)
    cel = (159, 199, 178); dark = (56, 92, 78)
    rgb = ImageOps.colorize(tw, dark, (226, 240, 230), mid=cel)
    out = rgb.convert("RGBA"); out.putalpha(mk.filter(ImageFilter.GaussianBlur(0.8)))
    bb = mk.point(lambda v: 255 if v > 128 else 0).getbbox(); out = out.crop(bb); out.save(O / "taiwan_celadon_relief.png"); print("taiwan", out.size)
