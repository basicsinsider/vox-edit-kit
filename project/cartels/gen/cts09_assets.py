"""cts09 derived assets (cts09 editor, 2026-11-22).
  .venv/bin/python project/cartels/gen/cts09_assets.py
Writes assets/cartels/cts09/derived/ (crops of shared captures + a map cut-out) and
project/cartels/gen/cts09_paths.json (simplified map paths, pasted into compositions/cts09.html).
  MX.* : assets/maps/kit/mexico.json pixel space (5800x4400)
  CH.* : assets/maps/kit/chihuahua.json pixel space (3857x4900)
"""
import re, os, json, sys
sys.setrecursionlimit(20000)
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
K = f"{ROOT}/assets/maps/kit"
N = f"{ROOT}/assets/cartels/news"
OUT = f"{ROOT}/assets/cartels/cts09/derived"
os.makedirs(OUT, exist_ok=True)


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = np.array(pts[0]), np.array(pts[-1])
    d = b - a
    n = np.hypot(*d)
    P = np.array(pts)
    dist = np.abs(d[0] * (P[:, 1] - a[1]) - d[1] * (P[:, 0] - a[0])) / n if n > 0 else np.hypot(*(P - a).T)
    i = int(np.argmax(dist))
    if dist[i] > eps:
        return rdp(pts[: i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]


def subpaths(d):
    out = []
    for sp in re.split(r"(?=M)", d):
        nums = list(map(float, re.findall(r"-?\d+(?:\.\d+)?", sp)))
        if len(nums) >= 4:
            out.append(list(zip(nums[0::2], nums[1::2])))
    return out


def getd(svg, pid):
    m = re.search(r'id="%s"[^>]*?\sd="([^"]+)"' % pid, svg)
    return m.group(1)


def simp(d, eps, closed=True, minlen=8):
    res = []
    for pts in subpaths(d):
        if len(pts) < 2:
            continue
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        if max(xs) - min(xs) < minlen and max(ys) - min(ys) < minlen:
            continue
        if closed:
            h = len(pts) // 2
            s = rdp(pts[: h + 1], eps)[:-1] + rdp(pts[h:], eps)
            if len(s) < 3:
                continue
        else:
            s = rdp(pts, eps)
        res.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in s) + ("Z" if closed else ""))
    return "".join(res)


paths = {}
mx = open(f"{K}/mexico_overlay.svg").read()
ch = open(f"{K}/chihuahua_overlay.svg").read()
for k, pid, eps, closed in [("MX_chih", "st-chihuahua", 1.2, True), ("MX_border", "b-us_mexico", 1.2, False),
                            ("MX_m45", "hwy-mex45", 1.0, False), ("MX_tx", "us-texas", 1.5, True), ("MX_nm", "us-new_mexico", 1.5, True),
                            ("CH_chih", "st-chihuahua", 4.0, True), ("CH_border", "b-us_mexico", 1.5, False), ("CH_m45", "hwy-mex45", 1.2, False), ("CH_sierra", "rg-sierra_tarahumara", 5.0, True)]:
    paths[k] = simp(getd(mx if k.startswith("MX") else ch, pid), eps, closed)
    print(k, len(paths[k]))
json.dump(paths, open(f"{ROOT}/project/cartels/gen/cts09_paths.json", "w"))

# ---- Chihuahua cut out of the mexico relief (pale relief inside the state, alpha outside) ----
rel = Image.open(f"{K}/mexico_relief.jpg").convert("RGB")
d = getd(mx, "st-chihuahua")
polys = subpaths(d)
allp = [p for pl in polys for p in pl]
x0, y0 = int(min(p[0] for p in allp)) - 8, int(min(p[1] for p in allp)) - 8
x1, y1 = int(max(p[0] for p in allp)) + 8, int(max(p[1] for p in allp)) + 8
mask = Image.new("L", rel.size, 0)
dr = ImageDraw.Draw(mask)
for pl in polys:
    dr.polygon(pl, fill=255)
land = Image.open(f"{K}/mexico_landmask.png").convert("L")
mask = Image.fromarray(np.minimum(np.array(mask), np.array(land))).filter(ImageFilter.GaussianBlur(1.2))
cut = rel.crop((x0, y0, x1, y1)).convert("RGBA")
cut.putalpha(mask.crop((x0, y0, x1, y1)))
cut.save(f"{OUT}/chihuahua_relief_cut.png")
print("cut", (x0, y0, x1 - x0, y1 - y0))
json.dump({"chih_cut": [x0, y0, x1 - x0, y1 - y0]}, open(f"{OUT}/cts09_layout.json", "w"))

# ---- Zuany photos (lead images of the two Infobae articles, cropped out of the page captures) ----
Image.open(f"{N}/n04_infobae_nyt_zuany_full.jpg").crop((706, 1396, 2412, 2528)).convert("RGB").save(f"{OUT}/zuany_office.jpg", quality=92)
Image.open(f"{N}/n04_infobae_zuany_us_full.jpg").crop((706, 1396, 2412, 2374)).convert("RGB").save(f"{OUT}/zuany_podium.jpg", quality=92)
# ---- article crops ----
Image.open(f"{N}/n04_infobae_nyt_zuany.jpg").crop((120, 110, 2620, 1010)).convert("RGB").save(f"{OUT}/infobae_nyt_head.jpg", quality=92)
Image.open(f"{N}/n04_eluniversal_nyt_zuany_k1.jpg").crop((330, 30, 1620, 920)).convert("RGB").save(f"{OUT}/eluniversal_visa_par.jpg", quality=92)
Image.open(f"{N}/n04_eluniversal_nyt_zuany_k2.jpg").crop((330, 590, 1620, 1620)).convert("RGB").save(f"{OUT}/eluniversal_nyt_par.jpg", quality=92)
for f in sorted(os.listdir(OUT)):
    if f.endswith((".jpg", ".png")):
        print(f, Image.open(f"{OUT}/{f}").size)
