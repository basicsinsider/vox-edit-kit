"""Derived assets for compositions/c3s02.html (chunk c3, segment 2, LOCAL 200.34-404.17).
Run from anywhere: .venv/bin/python project/c3/gen/c3s02_assets.py
Writes assets/c3/derived/c3s02/*: kit map crops (never upscaled), baked celadon/red fills, simplified paths (c3s02_maps.json),
an Esri z9 Taiwan-Strait mosaic (tiles fetched by tools/map_tiles.py into /tmp/mk/tiles), photo crops and stills."""
import json, re, math, pathlib, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageChops, ImageDraw
Image.MAX_IMAGE_PIXELS = None
R = pathlib.Path(__file__).resolve().parents[3]
K = R / "assets/maps/kit"
O = R / "assets/c3/derived/c3s02"; O.mkdir(parents=True, exist_ok=True)
J = {}

def paths_from(svgfile, ids):
    s = (K / svgfile).read_text(); res = {}
    for i in ids:
        m = re.search(r'<path id="%s"[^>]*\sd="([^"]+)"' % i, s); res[i] = m.group(1) if m else ""
    return res

def polys(d, ox=0, oy=0, sc=1.0, jump=400):
    out = []
    for sp in re.findall(r'M[^M]+', d):
        pts = [((float(a) - ox) * sc, (float(b) - oy) * sc) for a, b in re.findall(r'(-?\d+\.?\d*)[, ](-?\d+\.?\d*)', sp)]
        if any(abs(pts[i][0] - pts[i - 1][0]) > jump * sc for i in range(1, len(pts))): continue
        if len(pts) > 2: out.append(pts)
    return out

def to_d(ps, step):
    res = []
    for p in ps:
        q = []
        for x, y in p:
            if not q or abs(x - q[-1][0]) + abs(y - q[-1][1]) >= step: q.append((x, y))
        if len(q) > 3: res.append("M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in q) + "Z")
    return "".join(res)

def crop(src, box, w, name, q=88):
    im = Image.open(K / src).convert("RGB").crop(box)
    sc = min(1.0, w / im.width)
    if sc < 1: im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    im.save(O / name, quality=q); return sc, im.size

def wash(mask, rgb, a_in=0.78, a_rim=0.6, rimw=9):
    """celadon watercolour wash: soft interior + darker rim, alpha = mask"""
    inner = mask.filter(ImageFilter.GaussianBlur(10))
    rim = ImageChops.subtract(mask, mask.filter(ImageFilter.MinFilter(rimw)))
    alpha = ImageChops.add(inner.point(lambda v: int(v * a_in)), rim.point(lambda v: int(v * a_rim)))
    alpha = ImageChops.multiply(alpha, mask.filter(ImageFilter.GaussianBlur(1.5)))
    im = Image.new("RGBA", mask.size, rgb + (0,)); im.putalpha(alpha); return im

CEL = (159, 199, 178); RED = (224, 63, 44)

# ---------- Taiwan close-up (night relief + satdesat) : C3S044 / C3S048 ----------
mk = Image.open(K / "taiwan_landmask.png").convert("L")
for name, src, H in [("tw_night", "taiwan_night.jpg", 2200), ("tw_sat", "taiwan_satdesat.jpg", 2600)]:
    im = Image.open(K / src).convert("RGB"); sc = H / im.height; Wd = round(im.width * sc)
    im.resize((Wd, H), Image.LANCZOS).save(O / f"{name}.jpg", quality=88)
    J[name] = {"size": [Wd, H], "sc": sc, "sea": list(im.resize((1, 1)).getpixel((0, 0))),
               "corner": list(im.getpixel((5, 5)))}
m = mk.resize(tuple(J["tw_night"]["size"]), Image.LANCZOS)
wash(m, CEL).save(O / "tw_celadon.png")
a = Image.new("RGBA", m.size, (255, 255, 255, 0)); a.putalpha(m); a.save(O / "tw_mask.png")
tj = json.load(open(K / "taiwan.json"))["places"]
J["tw_night"]["taipei"] = [tj["taipei"]["x"] * J["tw_night"]["sc"], tj["taipei"]["y"] * J["tw_night"]["sc"]]
J["tw_night"]["hsinchu"] = [tj["hsinchu_city"]["x"] * J["tw_night"]["sc"], tj["hsinchu_city"]["y"] * J["tw_night"]["sc"]]

# ---------- Pacific night : C3S046 (Taiwan -> Silicon Valley), lon 108E .. 118W(=242), lat 12..52 ----------
x0, y0, x1, y1 = round((108 - 100) * 44), round((60 - 52) * 44), round((242 - 100) * 44), round((60 - 12) * 44)
sc, size = crop("pacific_night.jpg", (x0, y0, x1, y1), 6000, "pac_night.jpg")
P = paths_from("pacific_overlay.svg", ["c-taiwan"])
tw = polys(P["c-taiwan"], x0, y0, sc)
mkp = Image.new("L", size, 0); dr = ImageDraw.Draw(mkp)
for p in tw: dr.polygon(p, fill=255)
bb = mkp.getbbox(); pad = 12; bb = (bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)
wash(mkp.crop(bb).filter(ImageFilter.GaussianBlur(0.6)), CEL, 0.9, 0.5, 3).save(O / "pac_tw_fill.png")
pp = json.load(open(K / "pacific.json"))["places"]
st_lon, st_lat = -122.17 + 360, 37.43
J["pac"] = {"size": size, "sc": sc, "tw_box": list(bb),
            "taipei": [(pp["taipei"]["x"] - x0) * sc, (pp["taipei"]["y"] - y0) * sc],
            "sv": [((st_lon - 100) * 44 - x0) * sc, ((60 - st_lat) * 44 - y0) * sc]}

# ---------- East Asia night relief : C3S054 + C3S073 (one projection), lon 100..134, lat 16..46 ----------
x0, y0, x1, y1 = 0, round((48 - 46) * 150), round(34 * 127.95), round((48 - 16) * 150)
sc, size = crop("east_asia_night.jpg", (x0, y0, x1, y1), 3600, "ea_night.jpg")
P = paths_from("east_asia_overlay.svg", ["c-china", "c-taiwan", "c-hong_kong", "c-macao"])
ch = polys(P["c-china"], x0, y0, sc) + polys(P["c-hong_kong"], x0, y0, sc) + polys(P["c-macao"], x0, y0, sc)
tw = polys(P["c-taiwan"], x0, y0, sc)
J["ea"] = {"size": size, "sc": sc, "ox": x0, "oy": y0, "china": to_d(ch, 3), "taiwan": to_d(tw, 1.5),
           "lon": [100, 134], "lat": [16, 46]}
ep = json.load(open(K / "east_asia.json"))["places"]
J["ea"]["places"] = {k: [(ep[k]["x"] - x0) * sc, (ep[k]["y"] - y0) * sc] for k in ("taipei", "beijing", "shanghai", "fuzhou", "xiamen", "nanjing", "guangzhou")}
# Taiwan celadon wash for the drain (baked: watercolour edge) in the ea pixel space
mkt = Image.new("L", size, 0); dr = ImageDraw.Draw(mkt)
for p in tw: dr.polygon(p, fill=255)
bb = mkt.getbbox(); pad = 14; bb = (bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)
wash(mkt.crop(bb).filter(ImageFilter.GaussianBlur(0.8)), CEL, 0.85, 0.55, 5).save(O / "ea_tw_fill.png")
J["ea"]["tw_box"] = list(bb)
# burn mask for C3S073 (white = burnt/red visible, ragged edge), tall: top white, bottom black, edge noise
Wm, Hm = 900, 2400
rng = np.random.default_rng(7300)
yy = np.arange(Hm)[:, None]; xx = np.arange(Wm)[None, :]
n = np.zeros((Hm, Wm))
for f, amp in [(6, 60), (14, 28), (40, 10)]:
    ph = rng.uniform(0, 6.28, 4)
    n += amp * (np.sin(xx / Wm * f * 6.28 + ph[0]) * 0.5 + np.sin(xx / Wm * f * 3.7 + ph[1]) * 0.5)
edge = Hm / 2 + n
v = np.clip((edge - yy) / 10.0 + 0.5, 0, 1)
Image.fromarray((v * 255).astype(np.uint8), "L").filter(ImageFilter.GaussianBlur(2)).save(O / "burn_mask.png")
J["burn"] = [Wm, Hm]

# ---------- World night : C3S067-068, lon -135..165, lat -50..80 ----------
WD = 45.5111
x0, y0, x1, y1 = round((-135 + 180) * WD), round((90 - 80) * WD), round((165 + 180) * WD), round((90 + 50) * WD)
sc, size = crop("world_night.jpg", (x0, y0, x1, y1), 5200, "world_night.jpg")
J["world"] = {"size": size, "sc": sc, "lon0": -135, "lat0": 80, "deg": WD * sc}

# ---------- vintage world atlas plate : C3S049, lon -170..180, lat -50..76 (paper) ----------
x0, y0, x1, y1 = round((-170 + 180) * WD), round((90 - 76) * WD), round((180 + 180) * WD), round((90 + 50) * WD)
sc, size = crop("world_atlas.jpg", (x0, y0, x1, y1), 6000, "world_atlas.jpg", q=86)
J["atlas"] = {"size": size, "sc": sc, "lon0": -170, "lat0": 76, "deg": WD * sc}

# ---------- Taiwan Strait satellite (Esri z9 mosaic, web mercator) : C3S074 ----------
Z = 9; lon0, lat0, lon1, lat1 = 115.5, 20.4, 125.6, 27.6
def tx(lon): return (lon + 180) / 360 * 2 ** Z * 256
def ty(lat):
    r = math.radians(lat); return (1 - math.log(math.tan(r) + 1 / math.cos(r)) / math.pi) / 2 * 2 ** Z * 256
X0, X1, Y0, Y1 = int(tx(lon0)), int(tx(lon1)), int(ty(lat1)), int(ty(lat0))
mos = Image.new("RGB", (X1 - X0, Y1 - Y0))
for x in range(X0 // 256, X1 // 256 + 1):
    for y in range(Y0 // 256, Y1 // 256 + 1):
        p = pathlib.Path(f"/tmp/mk/tiles/esri/{Z}_{x}_{y}.jpg")
        if p.exists(): mos.paste(Image.open(p).convert("RGB"), (x * 256 - X0, y * 256 - Y0))
# desaturate toward the s02 look (keep a little colour)
g = mos.convert("L").convert("RGB"); mos2 = Image.blend(mos, g, 0.55)
mos2.save(O / "strait_sat.jpg", quality=88)
def merc(lon, lat): return [tx(lon) - X0, ty(lat) - Y0]
J["strait"] = {"size": list(mos.size), "z": Z, "X0": X0, "Y0": Y0,
               "fuzhou": merc(119.30, 26.08), "tw_c": merc(120.95, 23.65), "xiamen": merc(118.09, 24.48), "taipei": merc(121.5654, 25.033),
               "keelung": merc(121.74, 25.13), "kaohsiung": merc(120.30, 22.62), "mid": merc(120.3, 25.2)}
# Taiwan land mask re-projected from the kit landmask (plate carree, 1119.352 px/deg lon, 1222 px/deg lat)
tm = np.array(mk) > 127
Wt, Ht = mos.size
xs = np.arange(Wt) + X0; ys = np.arange(Ht) + Y0
lon = xs / (2 ** Z * 256) * 360 - 180
latr = np.degrees(np.arctan(np.sinh(math.pi * (1 - 2 * ys / (2 ** Z * 256)))))
px = np.clip(((lon - 119.3) * 1119.352).astype(int), 0, mk.width - 1)
py = np.clip(((25.4 - latr) * 1222).astype(int), 0, mk.height - 1)
inside = ((lon >= 119.3) & (lon <= 122.2))[None, :] & ((latr >= 21.8) & (latr <= 25.4))[:, None]
M = tm[py[:, None], px[None, :]] & inside
mimg = Image.fromarray((M * 255).astype(np.uint8), "L")
bb = mimg.getbbox(); pad = 12; bb = (bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)
wash(mimg.crop(bb).filter(ImageFilter.GaussianBlur(0.8)), CEL, 0.82, 0.6, 5).save(O / "strait_tw_fill.png")
J["strait"]["tw_box"] = list(bb)

# ---------- photos / documents ----------
A = R / "assets"
def pc(src, box, name, maxw=2400, q=88):
    im = Image.open(A / src).convert("RGB")
    if box: im = im.crop(box)
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(O / name, quality=q); return list(im.size)
J["kansan"] = pc("c3/newspapers/university_daily_kansan_1971-10-26_frontpage.jpg", (300, 1100, 4400, 5400), "kansan_page.jpg", 3000)
J["kansan_sc"] = 3000 / 4100
J["kansan_card"] = pc("c3/newspapers/university_daily_kansan_1971-10-26_frontpage.jpg", (2330, 1820, 4370, 2700), "kansan_headline_card.jpg", 1400)
J["kansan_col"] = pc("c3/newspapers/university_daily_kansan_1971-10-26_frontpage.jpg", (2330, 2290, 3010, 3330), "kansan_column.jpg", 680)
J["park_chip"] = pc("maps/kit/aerial_stanford_z17.jpg", (2000, 1800, 3400, 2900), "park_chip.jpg", 700)
J["formosa"] = pc("intro/maps/formosa_1943_japanese_aviation_map.jpg", None, "formosa_1943.jpg", 3000)
J["sc_poster"] = pc("c3/posters/nara_515905_united_nations_security_council.jpg", None, "sc_poster.jpg", 2337)
J["fdr"] = pc("c3/photos/fdr_portrait_perskie_1944.png", (520, 160, 1820, 1460), "fdr_circle.jpg", 700)
J["chiang"] = pc("c3/photos/chiang_kai_shek_portrait.jpg", (300, 0, 2300, 2400), "chiang_poster.jpg", 1300)
J["mao"] = pc("c3/photos/mao_tse_tung_portrait.jpg", None, "mao_poster.jpg", 740)
J["mao_c"] = pc("c3/photos/mao_tse_tung_portrait.jpg", (90, 60, 690, 660), "mao_circle.jpg", 600)
J["ww2a"] = pc("c3/photos/ww2_sc184778_chinese_american_troops_truck.jpg", None, "ww2_truck.jpg", 2400)
J["ww2b"] = pc("c3/photos/ww2_sc190514_american_trained_chinese_22nd_division.jpg", None, "ww2_22nd.jpg", 1669)
J["cairo"] = pc("c3/photos/cairo_1943_fdr_chiang_churchill.jpg", None, "cairo.jpg", 2005)
J["surrender"] = pc("c3/newspapers/japan_surrender_1945_slnsw.jpg", None, "surrender.jpg", 1600)
for nm, src, t in [("still_presoffice", "intro/footage/taiwan_1960_presidential_office_taipei.mp4", 3.0),
                   ("still_chiang1949", "c3/footage/newsreel_1949_chiang_kai_shek_closeup.mp4", 2.0),
                   ("still_charter_book", "c3/footage/newsreel_1945_un_charter_book.mp4", 3.2)]:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(A / src), "-frames:v", "1", "-q:v", "2", str(O / f"{nm}.jpg")], check=True)
json.dump(J, open(O / "c3s02_maps.json", "w"), separators=(",", ":"))
print({k: (v["size"] if isinstance(v, dict) and "size" in v else v) for k, v in J.items() if k not in ("ea",)}, "ea", J["ea"]["size"], len(J["ea"]["china"]))
