"""Derived assets for compositions/c6s02.html (C6S042–C6S076). Run: .venv/bin/python project/c6/gen/c6s02_assets.py
Writes assets/c6/derived/c6s02/* and assets/c6/derived/c6s02/paths.json (inlined by build_c6s02.py)."""
import json, re, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
P = lambda *a: os.path.join(R, *a)
OUT = P("assets/c6/derived/c6s02"); os.makedirs(OUT, exist_ok=True)
paths = {}

def subpaths(d):
    out = []
    for sp in re.split(r"(?=M)", d):
        pts = [tuple(map(float, q)) for q in re.findall(r"(-?[\d.]+),(-?[\d.]+)", sp)]
        if len(pts) > 2: out.append(pts)
    return out
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
def simp(ring, eps):
    h = len(ring) // 2
    return rdp(ring[:h + 1], eps)[:-1] + rdp(ring[h:], eps)
def getd(svgfile, pid):
    s = open(svgfile).read(); m = re.search(r'id="%s"[^>]*\sd="([^"]+)"' % pid, s)
    return m.group(1)
def dstr(rings):
    return " ".join("M" + " L".join("%.1f %.1f" % p for p in r) + "Z" for r in rings)

# ---------- 1. Moscow plan 1917 (C6S053/054/057) ----------
m = Image.open(P("_tmp/c6s02/moscow1917a.jpg")).convert("RGB")
m.crop((1100, 0, 3840, 2700)).save(P("assets/c6/derived/c6s02/moscow_plan_1917_crop.jpg"), quality=90)
# Volkhonka 16 (Moscow Sun Yat-sen University) ≈ orig (2030,1560) → crop (930,1560)

# ---------- 2. Eurasia atlas crop + USSR outline + route (C6S049) ----------
E = json.load(open(P("assets/c4/maps/eurasia.json")))
ex = lambda lon: (lon + 180) * 45.5111 - 7646; ey = lambda lat: (90 - lat) * 45.5111 - 728
x0, y0, x1, y1 = int(ex(20)), int(ey(74)), int(ex(140)), int(ey(20)); K = 0.75
ea = Image.open(P("assets/c4/maps/eurasia_atlas.jpg")).crop((x0, y0, x1, y1))
ea = ea.resize((int(ea.width * K), int(ea.height * K)), Image.LANCZOS); ea.save(P("assets/c6/derived/c6s02/eurasia_atlas_crop.jpg"), quality=88)
tx = lambda lon: (ex(lon) - x0) * K; ty = lambda lat: (ey(lat) - y0) * K
ussr = [[((x - x0) * K, (y - y0) * K) for x, y in r] for r in subpaths(getd(P("assets/c4/maps/eurasia_overlay.svg"), "h-ussr"))]
ussr = [simp(r, 3.0) for r in ussr if len(r) > 40]
paths["euW"], paths["euH"] = ea.width, ea.height
paths["ussr"] = dstr(ussr)
route = [(121.47, 31.23), (126.5, 35.5), (131.9, 43.1), (127.5, 49.8), (113.5, 52.0), (104.3, 52.3), (92.9, 56.0), (82.9, 55.0), (73.4, 55.0), (60.6, 56.8), (49.1, 55.8), (37.62, 55.75)]
paths["route"] = [[round(tx(a), 1), round(ty(b), 1)] for a, b in route]
paths["moscowEU"] = [round(tx(37.62), 1), round(ty(55.75), 1)]; paths["shanghaiEU"] = [round(tx(121.47), 1), round(ty(31.23), 1)]

# ---------- 3. World night (wide) + full-res East Asia patch + Taiwan (C6S062) ----------
W = Image.open(P("assets/maps/kit/world_night.jpg"))
W.resize((4096, 2048), Image.LANCZOS).save(P("assets/c6/derived/c6s02/world_night_4096.jpg"), quality=88)
wx = lambda lon: (lon + 180) * 45.5111; wy = lambda lat: (90 - lat) * 45.5111
px0, py0, px1, py1 = int(wx(95)), int(wy(50)), int(wx(150)), int(wy(0))
W.crop((px0, py0, px1, py1)).save(P("assets/c6/derived/c6s02/world_night_patch_ea.jpg"), quality=90)
paths["patch"] = [px0 / 4, py0 / 4, (px1 - px0) / 4, (py1 - py0) / 4]   # in 4096 space
tw = subpaths(getd(P("assets/maps/kit/world_overlay.svg"), "c-taiwan"))
paths["twWorld"] = dstr([[(x / 4, y / 4) for x, y in simp(r, 1.0)] for r in tw])   # 4096 space
paths["twWorldC"] = [round(wx(120.95) / 4, 1), round(wy(23.7) / 4, 1)]

# ---------- 4. Claim map (C6S075–076): native crop of the kit world night relief, lon 70–138E, lat 15–56N ----------
gx0, gy0, gx1, gy1 = int(wx(70)), int(wy(56)), int(wx(138)), int(wy(15))
en = W.crop((gx0, gy0, gx1, gy1)); en.save(P("assets/c6/derived/c6s02/claim_night_crop.jpg"), quality=88)
paths["eaW"], paths["eaH"] = en.width, en.height
wov = open(P("assets/maps/kit/world_overlay.svg")).read()
def wd(pid): return re.search(r'id="%s"[^>]*\sd="([^"]+)"' % pid, wov).group(1)
china = [[(x - gx0, y - gy0) for x, y in r] for r in subpaths(wd("c-china"))]
def fillpng(rings, rgb, name, blur=0):
    im = Image.new("L", (en.width, en.height), 0); d = ImageDraw.Draw(im)
    for r in rings: d.polygon(r, fill=255)
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    col = Image.new("RGBA", im.size, rgb + (255,)); col.putalpha(im); col.save(P("assets/c6/derived/c6s02/" + name))
fillpng(china, (159, 199, 178), "claim_china_celadon.png", 1.5)
fillpng(china, (224, 63, 44), "claim_china_red.png", 1.5)
paths["eaChina"] = dstr([simp(r, 2.5) for r in china if len(r) > 30])
cx = lambda lon: (lon - 70) * 45.5111; cy = lambda lat: (56 - lat) * 45.5111
paths["eaTwBox"] = [round(cx(119.3), 1), round(cy(25.4), 1), round(2.9 * 45.5111, 1), round(3.6 * 45.5111, 1)]
paths["eaTwC"] = [round(cx(120.95), 1), round(cy(23.7), 1)]
paths["eaBeijing"] = [round(cx(116.4), 1), round(cy(39.9), 1)]
# ---------- 5. Taiwan outline (kit) normalised to a 1000-px-tall box (C6S047 faint, C6S066 blueprint) ----------
T = json.load(open(P("assets/maps/kit/taiwan.json")))
tr = max(subpaths(getd(P("assets/maps/kit/taiwan_overlay.svg"), "c-taiwan")), key=len)
xs = [p[0] for p in tr]; ys = [p[1] for p in tr]; mx, my, H = min(xs), min(ys), max(ys) - min(ys)
tn = [((x - mx) / H * 1000, (y - my) / H * 1000) for x, y in tr]
paths["twBox"] = dstr([simp(tn, 2.0)]); paths["twBoxW"] = round((max(xs) - mx) / H * 1000, 1)
# kit taiwan px → lon/lat helpers for the C6S066 substations (lon,lat → box)
tlon = lambda x: 119.3 + x / 1119.352; tlat = lambda y: 25.4 - y / 1222.0
bx = lambda lon: ((lon - 119.3) * 1119.352 - mx) / H * 1000; by = lambda lat: ((25.4 - lat) * 1222.0 - my) / H * 1000
paths["twCities"] = {k: [round(bx(a), 1), round(by(b), 1)] for k, (a, b) in {
    "taipei": (121.56, 25.03), "keelung": (121.74, 25.13), "hsinchu": (120.97, 24.81), "taichung": (120.68, 24.15),
    "sunmoon": (120.91, 23.86), "chiayi": (120.45, 23.48), "tainan": (120.2, 22.99), "kaohsiung": (120.30, 22.62),
    "hualien": (121.6, 23.98), "taitung": (121.15, 22.75), "yilan": (121.75, 24.75)}.items()}

# ---------- 6. Formosa 1943 map: dot positions inside the island (C6S070) ----------
fx = lambda lon: (298 + (lon - 120) * 174.4) * 3; fy = lambda lat: (190 + (25 - lat) * 190) * 3
poly = [(fx(tlon(x)), fy(tlat(y))) for x, y in tr]
mask = Image.new("L", (3840, 3500), 0); ImageDraw.Draw(mask).polygon(poly, fill=255)
mask = mask.filter(ImageFilter.MinFilter(41))
rnd = random.Random(7000); dots = []
while len(dots) < 46:
    x, y = rnd.uniform(1000, 2200), rnd.uniform(400, 2900)
    if mask.getpixel((int(x), int(y))) > 128 and all((x - a) ** 2 + (y - b) ** 2 > 120 ** 2 for a, b in dots): dots.append((round(x), round(y)))
paths["fmDots"] = sorted(dots, key=lambda p: p[1])
paths["fmOutline"] = dstr([simp(poly, 4.0)])

# ---------- 7. stills / crops ----------
Image.open(P("_tmp/c6s02/cck_cut.png")).save(P("assets/c6/derived/c6s02/cck_cutout.png"))
kt = Image.open(P("assets/c6/photos/chiang_ching_kuo_with_li_kwoh_ting_print.jpg")).convert("RGB")
w, h = kt.size; crop = kt.crop((985, 830, 1425, 1420))
ImageOps.autocontrast(ImageOps.grayscale(crop), cutoff=1).save(P("assets/c6/derived/c6s02/kt_li_crop.jpg"), quality=92)
Image.open(P("_tmp/c6s02/steps_5.jpg")).save(P("assets/c6/derived/c6s02/roc_generals_steps_1961_still.jpg"), quality=92)
Image.open(P("_tmp/c6s02/po_crowd.jpg")).save(P("assets/c6/derived/c6s02/presidential_office_rally_1961_still.jpg"), quality=92)
json.dump(paths, open(P("assets/c6/derived/c6s02/paths.json"), "w"))
print({k: (len(v) if isinstance(v, str) else v) for k, v in paths.items() if k not in ("fmDots",)})

# ---------- 8. more crops (second pass) ----------
ea_at = Image.open(P("assets/maps/kit/east_asia_atlas.jpg"))
mini = ea_at.crop((int(ax(106)), int(ay(37)), int(ax(126)), int(ay(20)))); s = 720 / mini.width
mini = mini.resize((720, int(mini.height * s)), Image.LANCZOS); mini.save(P("assets/c6/derived/c6s02/ea_atlas_mini.jpg"), quality=90)
mm = lambda lon, lat: [round((ax(lon) - ax(106)) * s, 1), round((ay(lat) - ay(37)) * s, 1)]
paths["miniW"], paths["miniH"] = mini.width, mini.height
paths["miniChina"] = mm(116.4, 30.6); paths["miniTaipei"] = mm(121.56, 25.03); paths["miniNanjing"] = mm(118.8, 32.06)
z82 = Image.open(P("_tmp/c6s02/zis_82.jpg")); z82.crop((240, 190, 1010, 610)).save(P("assets/c6/photos/soviet_zis_plant_scaffold_1931.jpg"), quality=92)
dl = Image.open(P("_tmp/c6s02/deng_lizhi.jpg")); dl.crop((40, 150, 740, 680)).save(P("assets/c6/photos/deng_xiaoping_billboard_shenzhen_lizhi_park_2025_crop.jpg"), quality=92)
json.dump(paths, open(P("assets/c6/derived/c6s02/paths.json"), "w"))
print("mini", paths["miniW"], paths["miniH"], paths["miniChina"], paths["miniTaipei"])
