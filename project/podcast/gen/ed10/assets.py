#!/usr/bin/env python3
"""ED10 derived assets for pd21-pd24 (maps in the podcast palette + inline path data).
Run from the repo root: .venv/bin/python project/podcast/gen/ed10/assets.py"""
import json, re, os
import numpy as np
from PIL import Image, ImageFilter
Image.MAX_IMAGE_PIXELS = None
KIT = "assets/maps/kit/"
OUT = "assets/podcast/"
HERE = os.path.dirname(os.path.abspath(__file__))

def rdp(pts, eps):
    if len(pts) < 3: return pts
    a, b = np.array(pts[0]), np.array(pts[-1]); P = np.array(pts)
    ab = b - a; L = np.hypot(*ab)
    d = np.hypot(*(P - a).T) if L == 0 else np.abs(ab[0] * (P[:, 1] - a[1]) - ab[1] * (P[:, 0] - a[0])) / L
    i = int(d.argmax())
    if d[i] > eps: return rdp(pts[:i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]

def simplify(d, k, eps, min_area):
    out = []
    for sub in d.split("M")[1:]:
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", sub)]
        pts = [(nums[i] * k, nums[i + 1] * k) for i in range(0, len(nums) - 1, 2)]
        if len(pts) < 4: continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if (max(xs) - min(xs)) * (max(ys) - min(ys)) < min_area: continue
        h = len(pts) // 2                       # halves separately (closed rings collapse otherwise, MANUAL 4.2)
        s = rdp(pts[:h + 1], eps)[:-1] + rdp(pts[h:], eps)
        if len(s) < 3: continue
        out.append("M" + "L".join("%.1f,%.1f" % p for p in s) + "Z")
    return "".join(out)

def overlay_paths(svgfile, ids, k, eps=1.0, min_area=30):
    s = open(svgfile).read(); res = {}
    for i in ids:
        m = re.search(r'id="c-%s"[^>]*? d="([^"]+)"' % i, s)
        if not m: print("missing", i); continue
        res[i] = simplify(m.group(1), k, 0.6 if i in ('taiwan', 'hong_kong') else 0.8 if i == 'china' else eps, 8 if i == 'taiwan' else 150 if i == 'china' else min_area)
    return res

def silicon(rgb, mask, land_lo, land_hi, sea_lo, sea_hi, tint=(0.96, 1.0, 1.06)):
    g = np.asarray(rgb.convert("L"), dtype=np.float32) / 255.0
    m = np.asarray(mask.resize(rgb.size, Image.LANCZOS).convert("L"), dtype=np.float32) / 255.0
    def norm(a, sel):
        lo, hi = np.percentile(a[sel], 2), np.percentile(a[sel], 98); return np.clip((a - lo) / max(hi - lo, 1e-3), 0, 1)
    land = land_lo + norm(g, m > 0.5) * (land_hi - land_lo)
    sea = sea_lo + norm(g, m < 0.5) * (sea_hi - sea_lo)
    v = land * m + sea * (1 - m)
    out = np.stack([np.clip(v * t, 0, 1) for t in tint], -1)
    return Image.fromarray((out * 255).astype(np.uint8))

def east_asia():
    W, H = 3199, 2475; k = W / 6398
    atlas = Image.open(KIT + "east_asia_atlas.jpg").convert("RGB").resize((W, H), Image.LANCZOS)
    mask = Image.open(KIT + "east_asia_landmask.png")
    # pd22: pale silicon relief on a dark slate sea (ref 7c824c47)
    silicon(atlas, mask, 0.52, 0.92, 0.07, 0.15).save(OUT + "pd22/ea_silicon_3199.jpg", quality=88)
    # pd24: pale "paper atlas" (ref 8689427d): light land, light blue-grey sea
    silicon(atlas, mask, 0.66, 0.95, 0.50, 0.62, tint=(0.97, 1.0, 1.04)).save(OUT + "pd24/ea_paper_3199.jpg", quality=88)
    ids = ["china", "taiwan", "japan", "south_korea", "north_korea", "mongolia", "russia", "vietnam", "philippines", "laos", "myanmar", "thailand", "hong_kong"]
    return {"size": [W, H], "note": "x=(lon-100)*63.975, y=(48-lat)*75", "d": overlay_paths(KIT + "east_asia_overlay.svg", ids, k, 2.0, 60)}

def taiwan():
    W, H = 1623, 2200; k = W / 3246
    atlas = Image.open(KIT + "taiwan_atlas.jpg").convert("RGB").resize((W, H), Image.LANCZOS)
    mask = Image.open(KIT + "taiwan_landmask.png").convert("L").resize((W, H), Image.LANCZOS)
    m = np.asarray(mask, dtype=np.float32) / 255.0
    # cut the Fujian (PRC) coast in the NW corner: lon < 120.05, lat > 24.9 (MANUAL 4.2, c5s01)
    x0 = int((120.05 - 119.3) / (122.2 - 119.3) * W); y0 = int((25.4 - 24.9) / (25.4 - 21.8) * H)
    m[:y0, :x0] = 0
    silicon(atlas, mask, 0.62, 0.96, 0.50, 0.60, tint=(0.97, 1.0, 1.04)).save(OUT + "pd24/tw_paper_1623.jpg", quality=90)
    # board-green fill, relief kept as shading (multiplied in the composition)
    g = np.asarray(atlas.convert("L"), dtype=np.float32) / 255.0
    lo, hi = np.percentile(g[m > 0.5], 2), np.percentile(g[m > 0.5], 98)
    sh = 0.62 + 0.38 * np.clip((g - lo) / (hi - lo), 0, 1)
    col = np.array([0x2f, 0x9e, 0x5b], dtype=np.float32)
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., :3] = np.clip(col * sh[..., None] * 1.12, 0, 255).astype(np.uint8)
    rgba[..., 3] = (m * 255).astype(np.uint8)
    Image.fromarray(rgba).save(OUT + "pd24/tw_green_1623.png", optimize=True)
    return {"size": [W, H], "note": "x=(lon-119.3)*559.66, y=(25.4-lat)*611.1"}

def dejump(d):
    out = []
    for sub in d.split("M")[1:]:
        n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sub)]
        xs = n[0::2]
        if len(xs) > 1 and max(abs(a - b) for a, b in zip(xs, xs[1:])) > 3000: continue
        out.append("M" + sub)
    return "".join(out)

def cards():
    def crop(src, box, size, out, q=88):
        im = Image.open(src).convert("L").crop(box).resize(size, Image.LANCZOS); im.save(OUT + out, quality=q)
    im = Image.open("assets/c3/photos/mao_tse_tung_portrait.jpg"); print("mao", im.size)
    crop("assets/c3/photos/mao_tse_tung_portrait.jpg", (40, 60, 700, 885), (640, 800), "pd21/mao_card.jpg")
    im = Image.open("assets/c4/photos/chiang_kaishek_uniform_portrait_1945_nara.jpg"); print("chiang", im.size)
    crop("assets/c4/photos/chiang_kaishek_uniform_portrait_1945_nara.jpg", (330, 260, 2530, 3010), (640, 800), "pd21/chiang_card.jpg")
    Image.open("assets/c3/flags/flag_us_48star_1912_1959.png").convert("L").resize((640, 337), Image.LANCZOS).convert("RGB").save(OUT + "pd21/us48_grey.jpg", quality=90)
    Image.open("assets/c3/derived/c3s02/sc_poster.jpg").convert("L").crop((0, 20, 2337, 1270)).save(OUT + "pd21/sc_poster_top.jpg", quality=88)

def cards24():
    im = Image.open("assets/c4/paintings/emperor_meiji_portrait_painting.jpg").convert("L")
    im.crop((250, 60, 1650, 1810)).resize((640, 800), Image.LANCZOS).save(OUT + "pd24/meiji_card.jpg", quality=88)
    im = Image.open("assets/c4/photos/taihoku_1930s_street_joss_paper_store.jpg").convert("L")
    im.crop((0, 380, 1280, 1980)).resize((960, 1200), Image.LANCZOS).save(OUT + "pd24/taihoku_street_card.jpg", quality=88)

def world():
    p = json.load(open("assets/c3/derived/c3s03/paths.json"))["world"]
    rec = json.load(open("assets/c3/data/recognition.json"))
    return {"size": p["size"], "k": p["k"], "d": {k: dejump(v) for k, v in p["d"].items()}, "roc1969": rec["snapshots_roc_recognisers"].get("1969")}

if __name__ == "__main__":
    cards()
    cards24()
    data = {"ea": east_asia(), "tw": taiwan(), "world": world()}
    json.dump(data, open(os.path.join(HERE, "maps.json"), "w"))
    for k, v in data.items(): print(k, v["size"], {a: len(b) for a, b in v.get("d", {}).items()} if k != "world" else len(v["d"]))
    print(data["world"]["roc1969"])
