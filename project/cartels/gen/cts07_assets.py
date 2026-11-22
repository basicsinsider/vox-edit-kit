"""cts07 derived assets (THE DEAL / CIA drones / rulebook / JIATF-CC / target package).
Run: .venv/bin/python project/cartels/gen/cts07_assets.py   → assets/cartels/cts07/derived/ + derived/paths.json
Everything is cropped from the map kit (assets/maps/kit, see its README "Cartels project") or from files logged in
assets/cartels/cts07/SOURCES.md. Pixel spaces are written to derived/paths.json (the composition inlines the paths)."""
import json, re, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
KIT = os.path.join(ROOT, "assets/maps/kit")
OUT = os.path.join(ROOT, "assets/cartels/cts07/derived")
PH = os.path.join(ROOT, "assets/cartels/cts07/photos")
os.makedirs(OUT, exist_ok=True)
SVG = open(os.path.join(KIT, "mexico_overlay.svg")).read()


def path_d(pid):
    m = re.search(r'<path id="' + re.escape(pid) + r'"[^>]*d="([^"]*)"', SVG)
    return m.group(1)


def subpaths(d):
    out = []
    for part in re.split(r"(?=M)", d):
        pts = [(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", part)]
        if len(pts) > 1:
            out.append(pts)
    return out


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = np.array(pts[0]), np.array(pts[-1])
    P = np.array(pts)
    ab = b - a
    n = np.hypot(*ab)
    if n == 0:
        dist = np.hypot(*(P - a).T)
    else:
        dist = np.abs(ab[0] * (P[:, 1] - a[1]) - ab[1] * (P[:, 0] - a[0])) / n
    i = int(np.argmax(dist))
    if dist[i] > eps:
        l = rdp(pts[: i + 1], eps)
        r = rdp(pts[i:], eps)
        return l[:-1] + r
    return [pts[0], pts[-1]]


def tf(pts, x0, y0, s):
    return [((x - x0) * s, (y - y0) * s) for x, y in pts]


def fill_png(ids, crop, s, size, rgb, name, landmask=True):
    """rasterise kit polygons into an RGBA fill in the crop's output pixels (alpha = shape ∩ land)."""
    x0, y0 = crop
    W, H = size
    m = Image.new("L", (W, H), 0)
    dr = ImageDraw.Draw(m)
    for pid in ids:
        for sp in subpaths(path_d(pid)):
            dr.polygon(tf(sp, x0, y0, s), fill=255)
    if landmask:
        lm = Image.open(os.path.join(KIT, "mexico_landmask.png")).convert("L")
        lm = lm.crop((x0, y0, x0 + W / s, y0 + H / s)).resize((W, H), Image.LANCZOS)
        m = Image.fromarray((np.asarray(m, dtype=np.float32) * np.asarray(lm, dtype=np.float32) / 255).astype(np.uint8))
    m = m.filter(ImageFilter.GaussianBlur(1.2))
    rgba = Image.new("RGBA", (W, H), rgb + (0,))
    rgba.putalpha(m)
    rgba.save(os.path.join(OUT, name), optimize=True)


def line_d(pid, crop, s, eps):
    x0, y0 = crop
    parts = []
    for sp in subpaths(path_d(pid)):
        q = rdp(tf(sp, x0, y0, s), eps)
        parts.append("M" + " L".join("%.1f %.1f" % p for p in q))
    return " ".join(parts)


paths = {}
STEEL, OLIVE = (0x6F, 0x93, 0xB4), (0x9A, 0x9A, 0x4E)

# ---- A · US–Mexico on the night relief (sc001): kit x 0..4200, y 0..2362 → 2880×1620 ----
A0, AS = (0, 0), 2880 / 4200
img = Image.open(os.path.join(KIT, "mexico_night.jpg")).crop((0, 0, 4200, 2362)).resize((2880, 1620), Image.LANCZOS)
img.save(os.path.join(OUT, "a_border_night.jpg"), quality=90)
fill_png(["c-united_states_of_america"], A0, AS, (2880, 1620), STEEL, "a_fill_us.png")
fill_png(["c-mexico"], A0, AS, (2880, 1620), OLIVE, "a_fill_mx.png")
paths["a_border"] = line_d("b-us_mexico", A0, AS, 0.8)
paths["a_scale"] = AS

# ---- B · southern Arizona / Sonora on the desaturated satellite (sc008): kit x 500..2900, y 150..1500 (native) ----
B0 = (500, 150)
img = Image.open(os.path.join(KIT, "mexico_satdesat.jpg")).crop((500, 150, 2900, 1500))
img.save(os.path.join(OUT, "b_arizona_satdesat.jpg"), quality=90)
fill_png(["us-arizona"], B0, 1.0, (2400, 1350), STEEL, "b_fill_az.png")
paths["b_border"] = line_d("b-us_mexico", B0, 1.0, 0.8)
paths["b_az"] = line_d("us-arizona", B0, 1.0, 0.8)
mj = json.load(open(os.path.join(KIT, "mexico.json")))
paths["b_places"] = {k: [round(mj["places"][k]["x"] - B0[0], 1), round(mj["places"][k]["y"] - B0[1], 1)]
                     for k in ["tucson", "davis_monthan_afb", "phoenix", "nogales_arizona", "hermosillo"]}

# ---- C · Sierra Madre (Sinaloa/Durango foothills) Esri imagery for the drone feed (sc004) ----
img = Image.open(os.path.join(KIT, "sinaloa_sat.jpg")).crop((2160, 260, 4027, 1310))
img.save(os.path.join(OUT, "c_sierra_sat.jpg"), quality=90)

# ---- D · Davis-Monthan AFB aerial (sc009 zoom box): x 0..4800, y 300..3000 → 3200×1800 ----
img = Image.open(os.path.join(KIT, "aerial_tucson_davis_monthan_z16.jpg")).crop((0, 300, 4800, 3000)).resize((3200, 1800), Image.LANCZOS)
img.save(os.path.join(OUT, "d_davis_monthan.jpg"), quality=90)
dj = json.load(open(os.path.join(KIT, "aerial_tucson_davis_monthan_z16.json")))
paths["d_pin"] = [round((dj["places"]["davis_monthan_afb"]["x"] - 0) * 2 / 3, 1), round((dj["places"]["davis_monthan_afb"]["y"] - 300) * 2 / 3, 1)]

json.dump(paths, open(os.path.join(OUT, "paths.json"), "w"), indent=0)
print({k: (v if not isinstance(v, str) else len(v)) for k, v in paths.items()})
