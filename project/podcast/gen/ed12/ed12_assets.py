"""ED12 derived assets (pd29 route map, pd30 Africa). Run: .venv/bin/python project/podcast/gen/ed12/ed12_assets.py
Sources: assets/maps/kit/world_night.jpg, world_atlas.jpg, world_overlay.svg (Natural Earth / AWS Terrain Tiles, PD)."""
import re, json, math
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
KIT = "assets/maps/kit/"
K = 45.5111
svg = open(KIT + "world_overlay.svg", encoding="utf8").read()

def rings(cid):
    m = re.search(r'<path id="c-%s" [^>]*? d="([^"]+)"' % re.escape(cid), svg)
    assert m, cid
    out = []
    for sub in m.group(1).split("M"):
        sub = sub.strip().rstrip("Z")
        if not sub: continue
        pts = [tuple(map(float, p.split(","))) for p in sub.replace("Z", "").split("L") if p]
        out.append([(x / K - 180, 90 - y / K) for x, y in pts])   # lon, lat
    return out

def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    dm, im = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * (pts[i][0] - x1) - dx * (pts[i][1] - y1)) / L
        if d > dm: dm, im = d, i
    if dm > eps: return rdp(pts[:im + 1], eps)[:-1] + rdp(pts[im:], eps)
    return [pts[0], pts[-1]]

def simp_ring(pts, eps):          # closed ring: simplify the two halves separately (MANUAL 4.2)
    if len(pts) < 8: return pts
    h = len(pts) // 2
    return rdp(pts[:h + 1], eps)[:-1] + rdp(pts[h:], eps)

def area(p):
    return abs(sum(p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1] for i in range(len(p)))) / 2

def path(cid, fx, fy, eps, amin, lonmin=-999):
    d, polys = "", []
    for r in rings(cid):
        if max(abs(r[i][0] - r[i - 1][0]) for i in range(1, len(r))) > 30: continue   # antimeridian
        if min(p[0] for p in r) < lonmin: continue
        px = [(fx(lo), fy(la)) for lo, la in r]
        if area(px) < amin: continue
        px = simp_ring(px, eps)
        if len(px) < 3: continue
        polys.append(px)
        d += "M" + "L".join("%.1f,%.1f" % p for p in px) + "Z"
    return d, polys

def centroid(polys):
    p = max(polys, key=area); a = cx = cy = 0
    for i in range(len(p)):
        x0, y0 = p[i]; x1, y1 = p[(i + 1) % len(p)]; c = x0 * y1 - x1 * y0
        a += c; cx += (x0 + x1) * c; cy += (y0 + y1) * c
    return [round(cx / (3 * a), 1), round(cy / (3 * a), 1)]

# ---------------- pd29: world night base + Asia detail ----------------
def pd29():
    # equirectangular with standard parallel ~40 N: lon px = 0.77 * lat px (truer shapes at the route's latitude, action near frame centre)
    L0, L1, A0, A1, P, PX = -135, 150, 86, -40, 16, 12.32
    src = Image.open(KIT + "world_night.jpg")
    box = lambda l0, l1, a0, a1: tuple(int(round(v)) for v in ((l0 + 180) * K, (90 - a0) * K, (l1 + 180) * K, (90 - a1) * K))
    src.crop(box(L0, L1, A0, A1)).resize((round((L1 - L0) * PX), (A0 - A1) * P), Image.LANCZOS).save("assets/podcast/pd29/world_night_base.jpg", quality=88)
    D = dict(l0=24, l1=135, a0=58, a1=2, p=40)
    src.crop(box(D["l0"], D["l1"], D["a0"], D["a1"])).resize((round((D["l1"] - D["l0"]) * D["p"] * PX / P), (D["a0"] - D["a1"]) * D["p"]), Image.LANCZOS).save("assets/podcast/pd29/asia_night_detail.jpg", quality=88)
    fx, fy = (lambda lo: (lo - L0) * PX), (lambda la: (A0 - la) * P)
    out = {"formula": "x=(lon+135)*12.32, y=(86-lat)*16", "w": round((L1 - L0) * PX), "h": (A0 - A1) * P,
           "detail": {"left": round(fx(D["l0"]), 1), "top": fy(D["a0"]), "width": round((D["l1"] - D["l0"]) * PX, 1), "height": (D["a0"] - D["a1"]) * P}, "paths": {}, "pts": {}}
    for cid, key, eps, amin, lm in [("united_states_of_america", "us", 0.7, 30, -130), ("pakistan", "pakistan", 0.25, 2, -999), ("china", "china", 0.3, 4, -999),
                                    ("india", "india", 0.3, 4, -999), ("taiwan", "taiwan", 0.1, 0.5, -999)]:
        out["paths"][key] = path(cid, fx, fy, eps, amin, lm)[0]
    for k, (lo, la) in {"washington": (-77.04, 38.9), "islamabad": (73.05, 33.69), "beijing": (116.4, 39.9), "taipei": (121.56, 25.03), "delhi": (77.2, 28.6)}.items():
        out["pts"][k] = [round(fx(lo), 1), round(fy(la), 1)]
    json.dump(out, open("assets/podcast/pd29/pd29_map.json", "w"))
    print("pd29", {k: len(v) for k, v in out["paths"].items()}, out["pts"])

# ---------------- pd30: Africa atlas relief (alpha = African countries) + country paths ----------------
# order = real order of independence up to 1971 (no years are shown on screen); `old` = independent before 1956; `col` = still colonies in 1971
NEW = ["sudan", "morocco", "tunisia", "ghana", "guinea", "cameroon", "togo", "madagascar", "dem_rep_congo", "somalia", "benin", "niger", "burkina_faso",
       "c_te_d_ivoire", "chad", "central_african_rep", "congo", "gabon", "senegal", "mali", "nigeria", "mauritania", "sierra_leone", "tanzania", "burundi",
       "rwanda", "algeria", "uganda", "kenya", "malawi", "zambia", "gambia", "botswana", "lesotho", "eswatini", "eq_guinea"]
OLD = ["egypt", "ethiopia", "liberia", "south_africa", "libya"]
REST = ["angola", "mozambique", "guinea_bissau", "namibia", "zimbabwe", "w_sahara", "djibouti", "eritrea", "s_sudan", "somaliland"]
def pd30():
    L0, L1, A0, A1, P = -20, 54, 39, -37, 24
    W, H = (L1 - L0) * P, (A0 - A1) * P
    src = Image.open(KIT + "world_atlas.jpg")
    crop = src.crop(tuple(int(round(v)) for v in ((L0 + 180) * K, (90 - A0) * K, (L1 + 180) * K, (90 - A1) * K))).resize((W, H), Image.LANCZOS).convert("L")
    fx, fy = (lambda lo: (lo - L0) * P), (lambda la: (A0 - la) * P)
    mask = Image.new("L", (W * 2, H * 2), 0); dr = ImageDraw.Draw(mask)
    out = {"formula": "x=(lon+20)*24, y=(39-lat)*24", "w": W, "h": H, "new": [], "old": [], "rest": []}
    for grp, ids in (("new", NEW), ("old", OLD), ("rest", REST)):
        for cid in ids:
            d, polys = path(cid, fx, fy, 0.6, 3 if cid not in ("gambia", "lesotho", "eswatini", "rwanda", "burundi", "djibouti", "eq_guinea") else 0.3)
            for p in path(cid, fx, fy, 0.05, 0.3)[1]: dr.polygon([(x * 2, y * 2) for x, y in p], fill=255)
            out[grp].append({"id": cid, "d": d, "c": centroid(polys)})
    # Sudan in 1956 included today's South Sudan; Ethiopia included Eritrea; Somalia (1960) included Somaliland -> merged on screen by drawing both paths
    mask = mask.resize((W, H), Image.LANCZOS)
    im = Image.merge("LA", (crop, mask))
    im.save("assets/podcast/pd30/africa_relief_grey.png", optimize=True)
    json.dump(out, open("assets/podcast/pd30/pd30_africa.json", "w"))
    print("pd30", W, H, len(out["new"]), sum(len(c["d"]) for g in ("new", "old", "rest") for c in out[g]))

if __name__ == "__main__":
    import sys
    a = sys.argv[1:] or ["pd29", "pd30"]
    if "pd29" in a: pd29()
    if "pd30" in a: pd30()
