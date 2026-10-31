"""Derived assets for compositions/c4s02.html (chunk c4, segment 2). Run: .venv/bin/python project/c4/gen/c4s02_assets.py
Writes assets/c4/derived/c4s02/*: map crops from assets/maps/kit (native or downscaled, never upscaled), country paths in the
crop pixel space (paths.json), Taiwan alpha masks/fills and the isotype grid inside the island (isotype.json)."""
import json, re, pathlib
from PIL import Image, ImageFilter, ImageChops
Image.MAX_IMAGE_PIXELS = None
R = pathlib.Path(__file__).resolve().parents[3]
K = R / "assets/maps/kit"
O = R / "assets/c4/derived/c4s02"; O.mkdir(parents=True, exist_ok=True)
out = {}

def paths_from(svgfile, ids):
    s = (K / svgfile).read_text()
    res = {}
    for i in ids:
        m = re.search(r'<path id="%s"[^>]*\sd="([^"]+)"' % i, s)
        res[i] = m.group(1) if m else ""
    return res

def transform(d, ox, oy, sc, minstep=1.5, jump=400):
    subs = re.findall(r'M[^M]+', d)
    outp = []
    for sp in subs:
        pts = [(float(a), float(b)) for a, b in re.findall(r'(-?\d+\.?\d*),(-?\d+\.?\d*)', sp)]
        q = []
        for x, y in pts:
            X, Y = (x - ox) * sc, (y - oy) * sc
            if q and abs(X - q[-1][0]) > jump: q = None; break
            if not q or abs(X - q[-1][0]) + abs(Y - q[-1][1]) >= minstep: q.append((X, Y))
        if not q or len(q) < 3: continue
        outp.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in q) + "Z")
    return "".join(outp)

def crop(src, box, w, name, q=88):
    im = Image.open(K / src).convert("RGB").crop(box)
    sc = min(1.0, w / im.width)
    if sc < 1: im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    im.save(O / name, quality=q)
    return sc, im.size

# --- C4S040 East Asia (night) : lon 106-146, lat 16-44
x0, y0, x1, y1 = round((106 - 100) * 127.95), round((48 - 44) * 150), round((146 - 100) * 127.95), round((48 - 16) * 150)
sc, size = crop("east_asia_night.jpg", (x0, y0, x1, y1), 3600, "ea_night.jpg")
P = paths_from("east_asia_overlay.svg", ["c-taiwan", "c-japan", "c-china", "c-south_korea", "c-north_korea", "c-philippines", "c-vietnam"])
out["ea"] = {"size": size, "sc": sc, "ox": x0, "oy": y0, "lon": [106, 146], "lat": [16, 44],
             "paths": {k: transform(v, x0, y0, sc) for k, v in P.items()},
             "taipei": [(2759.3 - x0) * sc, (3445.0 - y0) * sc]}

# --- C4S053 world (night) : lon -130..170, lat -48..68
W = 45.5111
x0, y0, x1, y1 = round((-130 + 180) * W), round((90 - 68) * W), round((170 + 180) * W), round((90 + 48) * W)
sc, size = crop("world_night.jpg", (x0, y0, x1, y1), 4800, "world_night.jpg")
P = paths_from("world_overlay.svg", ["c-taiwan", "c-china"])
out["world"] = {"size": size, "sc": sc, "ox": x0, "oy": y0, "paths": {k: transform(v, x0, y0, sc, 1.0) for k, v in P.items()},
                "px": lambda: None}
del out["world"]["px"]
out["world"]["deg"] = W * sc

# --- C4S066 inset (paper, atlas) : lon 72-136, lat 16-54
x0, y0, x1, y1 = round((72 + 180) * W), round((90 - 54) * W), round((136 + 180) * W), round((90 - 16) * W)
sc, size = crop("world_atlas.jpg", (x0, y0, x1, y1), 2400, "asia_atlas.jpg")
P = paths_from("world_overlay.svg", ["c-taiwan", "c-china"])
out["asia"] = {"size": size, "sc": sc, "ox": x0, "oy": y0, "paths": {k: transform(v, x0, y0, sc, 1.0) for k, v in P.items()}}

# --- C4S049 Pacific (night) : lon 108E .. 112W(=248), lat 8..56
x0, y0, x1, y1 = round((108 - 100) * 44), round((60 - 56) * 44), round((248 - 100) * 44), round((60 - 8) * 44)
sc, size = crop("pacific_night.jpg", (x0, y0, x1, y1), 4400, "pacific_night.jpg")
pj = json.load(open(K / "pacific.json"))["places"]
out["pac"] = {"size": size, "sc": sc, "ox": x0, "oy": y0,
              "taipei": [(pj["taipei"]["x"] - x0) * sc, (pj["taipei"]["y"] - y0) * sc],
              "sf": [((237.58 - 100) * 44 - x0) * sc, ((60 - 37.77) * 44 - y0) * sc]}
P = paths_from("pacific_overlay.svg", ["c-taiwan"])
out["pac"]["paths"] = {k: transform(v, x0, y0, sc, 0.5) for k, v in P.items()}

# --- C4S041 1943 Far East atlas plate (native crop)
im = Image.open(K / "scans/far_east_1943.jpg").convert("RGB").crop((2700, 1450, 5300, 3450)); im.save(O / "fareast1943.jpg", quality=90)
out["fe"] = {"size": im.size, "ox": 2700, "oy": 1450, "taipei": [3900 - 2700, 2660 - 1450]}

# --- C4S043 CIA 1949 Taiwan Province (strait) : crop + downscale
x0, y0, x1, y1 = 700, 1700, 4858, 6100
im = Image.open(K / "scans/cia_formosa_1949.jpg").convert("RGB").crop((x0, y0, x1, y1))
sc = 2800 / im.width; im = im.resize((2800, round(im.height * sc)), Image.LANCZOS); im.save(O / "cia1949.jpg", quality=88)
cj = json.load(open(K / "scans/cia_formosa_1949.json"))["places"]
out["cia"] = {"size": im.size, "sc": sc, "places": {k: [(v["x"] - x0) * sc, (v["y"] - y0) * sc] for k, v in cj.items()}}

# --- Taiwan night ghost + alpha mask + celadon wash (C4S037, C4S060) and isotype grid (C4S046)
tw = Image.open(K / "taiwan_night.jpg").convert("RGB")
mk = Image.open(K / "taiwan_landmask.png").convert("L")
H = 1300; sc = H / tw.height; Wd = round(tw.width * sc)
tw.resize((Wd, H), Image.LANCZOS).save(O / "tw_night.jpg", quality=88)
m = mk.resize((Wd, H), Image.LANCZOS)
a = Image.new("RGBA", (Wd, H), (255, 255, 255, 0)); a.putalpha(m); a.save(O / "tw_mask.png")
# celadon wash: soft watercolour edge (darker rim)
inner = m.filter(ImageFilter.GaussianBlur(10))
rim = ImageChops.subtract(m, m.filter(ImageFilter.MinFilter(9)))
col = Image.new("RGBA", (Wd, H), (159, 199, 178, 0))
alpha = ImageChops.add(inner.point(lambda v: int(v * 0.78)), rim.point(lambda v: int(v * 0.6)))
alpha = ImageChops.multiply(alpha, m.filter(ImageFilter.GaussianBlur(1.5)))
col.putalpha(alpha); col.save(O / "tw_celadon.png")
# outline (edge) for the ink outline on graph paper
edge = ImageChops.subtract(m.filter(ImageFilter.MaxFilter(5)), m.filter(ImageFilter.MinFilter(5)))
ink = Image.new("RGBA", (Wd, H), (20, 27, 36, 0)); ink.putalpha(edge.point(lambda v: 255 if v > 90 else 0)); ink.save(O / "tw_outline_ink.png")
out["tw"] = {"size": [Wd, H], "sc": sc}
# isotype cells (island drawn 860 px tall in C4S046)
ih = 860; s2 = ih / H; mm = m.resize((round(Wd * s2), ih), Image.LANCZOS)
cell = 30; cells = []
for y in range(0, ih, cell):
    for x in range(0, mm.width, cell):
        box = mm.crop((x, y, x + cell, y + cell)); v = sum(box.getdata()) / (cell * cell * 255)
        if v > 0.55: cells.append([x, y])
out["iso"] = {"w": mm.width, "h": ih, "cell": cell, "cells": cells}

# (full path set not written; see c4s02_small.json)
print({k: (v.get("size") if isinstance(v, dict) else None) for k, v in out.items()}, len(cells), "iso cells")

# ---------------- baked fills (PNG) + small path set for the composition ----------------
from PIL import ImageDraw
def polys(d):
    return [[(float(a), float(b)) for a, b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', sp)] for sp in re.findall(r'M[^M]+', d)]
def bake(key, pid, rgb, name, alpha=235, blur=1.2):
    v = out[key]; w, h = v["size"]
    m = Image.new("L", (w, h), 0); dr = ImageDraw.Draw(m)
    for p in polys(v["paths"][pid]):
        if len(p) > 2: dr.polygon(p, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(blur))
    im = Image.new("RGBA", (w, h), rgb + (0,)); im.putalpha(m.point(lambda q: q * alpha // 255))
    bb = m.getbbox(); im = im.crop(bb); im.save(O / name)
    return list(bb)
small = {}
small["ea_tw"] = bake("ea", "c-taiwan", (159, 199, 178), "ea_tw_fill.png")
small["world_tw"] = bake("world", "c-taiwan", (159, 199, 178), "world_tw_fill.png", blur=0.8)
small["asia_tw"] = bake("asia", "c-taiwan", (159, 199, 178), "asia_tw_fill.png", blur=0.8)
small["asia_cn"] = bake("asia", "c-china", (224, 63, 44), "asia_cn_fill.png", alpha=200, blur=1.0)
small["pac_tw"] = bake("pac", "c-taiwan", (159, 199, 178), "pac_tw_fill.png", blur=0.6)
def simp(d, step):
    res = []
    for p in polys(d):
        q = []
        for x, y in p:
            if not q or abs(x - q[-1][0]) + abs(y - q[-1][1]) >= step: q.append((x, y))
        if len(q) > 4: res.append("M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in q) + "Z")
    return "".join(res)
small["ea_japan"] = simp(out["ea"]["paths"]["c-japan"], 10)
small["ea_taiwan"] = simp(out["ea"]["paths"]["c-taiwan"], 4)
small["ea_size"] = out["ea"]["size"]; small["world_size"] = out["world"]["size"]; small["asia_size"] = out["asia"]["size"]
small["pac"] = {k: out["pac"][k] for k in ("size", "taipei", "sf")}
small["cia"] = out["cia"]; small["fe"] = out["fe"]; small["iso"] = out["iso"]; small["tw"] = out["tw"]
small["world_deg"] = out["world"]["deg"]; small["world_ox"] = out["world"]["ox"]; small["world_oy"] = out["world"]["oy"]
json.dump(small, open(O / "c4s02_small.json", "w"))
print("small json", len(json.dumps(small)), {k: v for k, v in small.items() if k.endswith(("_tw", "_cn"))})

# ---------------- photo crops (inside the prints / objects) ----------------
P = R / "assets/c4"
def pcrop(src, box, name, maxw=2400):
    im = Image.open(P / src).convert("RGB").crop(box)
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(O / name, quality=90); return im.size
pcrop("photos/formosa_1945_takao_city_bombing_usaf.jpg", (480, 430, 4060, 3450), "takao_city_bombing_crop.jpg")
pcrop("photos/formosa_1945_takao_harbor_b24_bombing_usaf.jpg", (700, 420, 4020, 3440), "takao_harbor_bombing_crop.jpg")
pcrop("photos/tiananmen_gate_mao_portrait_modern.jpg", (1600, 1040, 2140, 1700), "mao_portrait_crop.jpg")
# Taiwan landmask re-projected into the CIA 1949 crop (C4S043 celadon fill)
cia = out["cia"]; s = cia["sc"]
kx = 634.2 / 1119.352 * s; ky = 702.8 / 1222 * s
X0 = (2429 + (119.3 - 120) * 634.2 - 700) * s; Y0 = (3428 - (25.4 - 25) * 702.8 - 1700) * s
mk = Image.open(K / "taiwan_landmask.png").convert("L")
m2 = mk.resize((round(mk.width * kx), round(mk.height * ky)), Image.LANCZOS)
col = Image.new("RGBA", m2.size, (159, 199, 178, 0)); col.putalpha(m2.point(lambda v: v * 215 // 255)); col.save(O / "cia_tw_fill.png")
small["cia_tw"] = [X0, Y0, m2.width, m2.height]
json.dump(small, open(O / "c4s02_small.json", "w"))
print("cia_tw", small["cia_tw"])
print(pcrop("documents/taiwan_cement_share_certificate_1950s.jpg", (160, 100, 3500, 2880), "share_certificate_crop.jpg"))
