"""cts03 derived map assets (run from repo root with .venv/bin/python).
- graded crops of the kit mexico_relief (routes) and mexico_sat (Sonora 2010) -> assets/cartels/cts03/derived/
- vector data (mexico pixel space, minus the crop offset) -> project/cartels/gen/cts03_mapdata.json
"""
import json, re
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"
OUT = "assets/cartels/cts03/derived/"
MX = json.load(open(K + "mexico.json"))
CROP = (0, 0, 3400, 3000)                       # mexico px: x 0..3400 (118-99.2 W), y 0..3000 (36-21 N)
SON = (500, 300, 2300, 1700)                    # Sonora crop for the 2010 scene

def mx(lon, lat):
    return ((lon + 118) * 181.26, (36 - lat) * 200)

def paths(svg_file, ids):
    s = open(svg_file).read()
    out = {}
    for i in ids:
        m = re.search(r'<path[^>]*id="' + re.escape(i) + r'"[^>]*>', s)
        if not m:
            m = re.search(r'<g[^>]*id="' + re.escape(i) + r'"[^>]*>(.*?)</g>', s, re.S)
            ds = re.findall(r'd="([^"]+)"', m.group(1)) if m else []
        else:
            ds = re.findall(r'\bd="([^"]+)"', m.group(0))
        out[i] = " ".join(ds)
    return out

def xform(d, f, tol=1.6):
    """transform + thin a M..L..Z path (drop points closer than tol px to the last kept one)."""
    out = []
    for sub in re.split(r'(?=M)', d.strip()):
        if not sub.strip(): continue
        closed = "Z" in sub
        nums = [float(v) for v in re.findall(r'-?\d+\.?\d*', sub)]
        pts = [f(nums[k], nums[k + 1]) for k in range(0, len(nums) - 1, 2)]
        keep = [pts[0]]
        for q in pts[1:]:
            if abs(q[0] - keep[-1][0]) + abs(q[1] - keep[-1][1]) >= tol: keep.append(q)
        if len(keep) < 2: continue
        out.append("M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in keep) + ("Z" if closed else ""))
    return "".join(out)

def xform_old(d, f):
    toks = re.findall(r'[MLZmlzQCH V]|-?\d+\.?\d*', d)
    res, nums, cmd = [], [], None
    def flush():
        for k in range(0, len(nums) - 1, 2):
            x, y = f(nums[k], nums[k + 1]); res.append(f"{x:.1f},{y:.1f}")
        nums.clear()
    for t in toks:
        if t.strip() in ("M", "L", "Z"):
            flush(); res.append(t)
        elif t.strip():
            nums.append(float(t))
    flush()
    return " ".join(res).replace(" ,", ",")

def main():
    # --- images
    im = Image.open(K + "mexico_relief.jpg").convert("RGB").crop(CROP)
    a = np.asarray(im).astype(np.float32) / 255.0
    lum = a.mean(axis=2, keepdims=True)
    # dark slate grade (ref ast_c0cbc155: cool grey terrain, glowing route): lift shadows a bit, pull highlights down
    dark = np.array([0.055, 0.07, 0.08]); light = np.array([0.66, 0.70, 0.71])
    g = dark + (light - dark) * np.clip((lum - 0.12) / 0.86, 0, 1) ** 1.45
    land = lum[..., 0] > 0.30                     # relief land is pale; sea is dark slate
    sea = np.array([0.055, 0.075, 0.095])
    g[~land] = sea * 0.9 + g[~land] * 0.1
    Image.fromarray((np.clip(g, 0, 1) * 255).astype(np.uint8)).save(OUT + "mx_relief_dark.jpg", quality=90)
    s = Image.open(K + "mexico_sat.jpg").convert("RGB").crop(SON)
    s = ImageEnhance.Color(s).enhance(0.55); s = ImageEnhance.Contrast(s).enhance(1.12); s = ImageEnhance.Brightness(s).enhance(0.86)
    s.save(OUT + "son_sat_warm.jpg", quality=90)
    # --- vectors
    ids = ["st-sonora", "st-sinaloa", "st-chihuahua", "us-arizona", "b-us_mexico", "hwy-mex15-north"]
    P = paths(K + "mexico_overlay.svg", ids)
    sh = lambda ox, oy: (lambda x, y: (x - ox, y - oy))
    data = {"crop": CROP, "son": SON, "paths": {}, "sonpaths": {}, "places": {}}
    for i, d in P.items():
        data["paths"][i] = xform(d, sh(CROP[0], CROP[1]))
        data["sonpaths"][i] = xform(d, sh(SON[0], SON[1]))
    SP = paths(K + "sinaloa_overlay.svg", ["rg-northern_sinaloa"])
    def sin2mx(x, y):
        lon = x / 1258.32 - 110; lat = 27.4 - y / 1400
        X, Y = mx(lon, lat); return X - CROP[0], Y - CROP[1]
    data["paths"]["rg-northern_sinaloa"] = xform(SP["rg-northern_sinaloa"], sin2mx)
    for k in ["los_mochis", "guasave", "topolobampo", "culiacan", "navojoa", "ciudad_obregon", "hermosillo", "guaymas",
              "nogales_sonora", "nogales_arizona", "tubutama", "tucson", "phoenix"]:
        p = MX["places"].get(k)
        if p: data["places"][k] = [round(p["x"] - CROP[0], 1), round(p["y"] - CROP[1], 1)]
    # boat route along the Gulf of California coast (offshore waypoints, checked against the landmask)
    lm = Image.open(K + "mexico_landmask.png").convert("L")
    wp = [(-109.03, 25.60), (-109.2, 25.45), (-109.55, 25.85), (-109.80, 26.45), (-110.25, 26.95), (-110.62, 27.42),
          (-110.98, 27.78), (-111.45, 28.15), (-111.95, 28.55), (-111.95, 28.80)]   # Topolobampo -> Bahía de Kino
    chk = []
    for lon, lat in wp:
        X, Y = mx(lon, lat); chk.append(lm.getpixel((int(X), int(Y))))
    data["boat"] = [[round(mx(lo, la)[0] - CROP[0], 1), round(mx(lo, la)[1] - CROP[1], 1)] for lo, la in wp]
    data["boat_landmask"] = chk
    json.dump(data, open("project/cartels/gen/cts03_mapdata.json", "w"))
    print("landmask at boat waypoints (0 = sea):", chk)
    print({k: len(v) for k, v in data["paths"].items()})
    print(data["places"])

if __name__ == "__main__":
    main()
