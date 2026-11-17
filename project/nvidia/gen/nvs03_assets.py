"""nvs03 derived map assets (editor nvs03, 2026-11-17).
Outputs -> assets/nvidia/nvs03/derived/
  world_crop.jpg (+ fills *.svg in the same pixel space)  : IP-theft / WTO world map (sc012)
  china_fill.svg, china_line.svg                            : China map (sc009), china_night pixel space
  ea_china.svg, ea_taiwan.svg                               : Taiwan Strait (sc017), east_asia pixel space
  silhouettes.json                                          : US (lower 48) + China outline paths for the paper diagram (sc007)
Run: .venv/bin/python project/nvidia/gen/nvs03_assets.py
"""
import json, re, os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
K = os.path.join(ROOT, "assets/maps/kit")
OUT = os.path.join(ROOT, "assets/nvidia/nvs03/derived")
os.makedirs(OUT, exist_ok=True)


def paths(svgfile, ids):
    src = open(svgfile).read()
    res = {}
    for i in ids:
        m = re.search(r'id="c-%s"[^>]*?\sd="([^"]+)"' % i, src)
        if not m:
            raise SystemExit("missing " + i + " in " + svgfile)
        res[i] = m.group(1)
    return res


def subpaths(d):
    out = []
    for sp in d.split("M")[1:]:
        pts = []
        for tok in re.findall(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", sp):
            pts.append((float(tok[0]), float(tok[1])))
        if len(pts) > 2:
            out.append(pts)
    return out


def tf(sps, f, keep=None, minstep=1.5, minlen=4):
    """transform subpaths with f(x,y)->(x,y); drop near-duplicate points; keep(pts)->bool"""
    res = []
    for pts in sps:
        if keep and not keep(pts):
            continue
        q = [f(*p) for p in pts]
        r = [q[0]]
        for p in q[1:]:
            if abs(p[0] - r[-1][0]) + abs(p[1] - r[-1][1]) >= minstep:
                r.append(p)
        # drop antimeridian jumps
        if any(abs(r[i][0] - r[i - 1][0]) > 400 for i in range(1, len(r))):
            continue
        if len(r) >= minlen:
            res.append(r)
    return res


def dstr(sps):
    return "".join("M" + "L".join("%.1f,%.1f" % p for p in pts) + "Z" for pts in sps)


def svgfile(name, w, h, body):
    open(os.path.join(OUT, name), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">%s</svg>' % (w, h, w, h, body))


# ---------- world crop ----------
PPD = 45.5111
LON0, LON1, LAT0, LAT1 = -128.0, 148.0, 64.0, -44.0
F = 0.6
x0, y0 = (LON0 + 180) * PPD, (90 - LAT0) * PPD
x1, y1 = (LON1 + 180) * PPD, (90 - LAT1) * PPD
W, H = int(round((x1 - x0) * F)), int(round((y1 - y0) * F))
if not os.path.exists(os.path.join(OUT, "world_crop.jpg")):
    im = Image.open(os.path.join(K, "world_night.jpg")).crop((int(x0), int(y0), int(x0) + int(round(x1 - x0)), int(y0) + int(round(y1 - y0))))
    im = im.resize((W, H), Image.LANCZOS)
    im.save(os.path.join(OUT, "world_crop.jpg"), quality=88)
fw = lambda x, y: ((x - x0) * F, (y - y0) * F)
GS = ["brazil", "argentina", "mexico", "colombia", "peru", "chile", "bolivia", "venezuela", "ecuador", "paraguay", "uruguay",
      "india", "pakistan", "bangladesh", "indonesia", "vietnam", "thailand", "philippines", "malaysia",
      "south_africa", "nigeria", "egypt", "kenya", "ethiopia", "algeria", "morocco", "ghana", "angola", "tanzania",
      "dem_rep_congo", "sudan", "mozambique", "zambia", "zimbabwe", "namibia", "botswana", "mali", "niger", "chad",
      "cameroon", "c_te_d_ivoire", "libya", "tunisia", "somalia", "uganda", "madagascar", "mauritania", "senegal",
      "burkina_faso", "guinea", "central_african_rep", "gabon", "congo", "s_sudan", "w_sahara", "eritrea", "benin", "togo",
      "liberia", "sierra_leone", "malawi", "guatemala", "honduras", "nicaragua", "cuba", "guyana", "suriname", "myanmar",
      "cambodia", "laos", "sri_lanka", "nepal", "panama", "costa_rica", "el_salvador", "belize", "haiti", "dominican_rep",
      "rwanda", "burundi", "lesotho", "eswatini", "djibouti", "guinea_bissau", "gambia", "eq_guinea"]
WP = paths(os.path.join(K, "world_overlay.svg"), ["china", "united_states_of_america", "germany", "united_kingdom", "france"] + GS)
inb = lambda pts: any(-128 <= x / PPD - 180 <= 148 for x, _ in pts)
lower48 = lambda pts: all(-126 <= x / PPD - 180 <= -66 and 24 <= 90 - y / PPD <= 50 for x, y in pts[:5])
fr_main = lambda pts: all(-6 <= x / PPD - 180 <= 10 and 41 <= 90 - y / PPD <= 52 for x, y in pts[:5])
styles = {
    "w_china": ("china", None, 'fill="#dc2f3c" fill-opacity="0.55" stroke="#f6a4a9" stroke-width="3"'),
    "w_us": ("united_states_of_america", lower48, 'fill="#2a9fc9" fill-opacity="0.55" stroke="#9fdcf0" stroke-width="3"'),
    "w_de": ("germany", None, 'fill="#9fdcf0" fill-opacity="0.7" stroke="#f0efe8" stroke-width="2"'),
    "w_uk": ("united_kingdom", None, 'fill="#9fdcf0" fill-opacity="0.7" stroke="#f0efe8" stroke-width="2"'),
    "w_fr": ("france", fr_main, 'fill="#9fdcf0" fill-opacity="0.7" stroke="#f0efe8" stroke-width="2"'),
}
for name, (cid, keep, st) in styles.items():
    sps = tf(subpaths(WP[cid]), fw, keep=keep, minstep=1.0, minlen=3)
    svgfile(name + ".svg", W, H, '<path d="%s" %s stroke-linejoin="round"/>' % (dstr(sps), st))
gs = []
for c in GS:
    gs += tf(subpaths(WP[c]), fw, keep=inb, minstep=1.5, minlen=4)
svgfile("w_gs.svg", W, H, '<path d="%s" fill="#c3c7c8" fill-opacity="0.42" stroke="#f0efe8" stroke-opacity="0.75" stroke-width="2" stroke-linejoin="round"/>' % dstr(gs))
meta = {"width": W, "height": H, "formula": "x=(lon+128)*%.4f ; y=(64-lat)*%.4f" % (PPD * F, PPD * F)}
P = lambda lon, lat: (round((lon - LON0) * PPD * F, 1), round((LAT0 - lat) * PPD * F, 1))
meta["places"] = {"china": P(103, 35.5), "us": P(-99, 39), "germany": P(10.4, 51.1), "uk": P(-2.5, 53.5), "france": P(2.4, 46.6),
                  "geneva": P(6.14, 46.2), "washington": P(-77.04, 38.9), "beijing": P(116.4, 39.9),
                  "gs_africa": P(20, 2), "gs_sam": P(-58, -12), "gs_asia": P(80, 20)}
json.dump(meta, open(os.path.join(OUT, "world_crop.json"), "w"), indent=1)

# ---------- china map (china_night pixel space 6383x4368) ----------
CP = paths(os.path.join(K, "china_overlay.svg"), ["china", "taiwan"])
idn = lambda x, y: (x, y)
c_sps = tf(subpaths(CP["china"]), idn, minstep=2.0)
svgfile("china_fill.svg", 6383, 4368, '<path d="%s" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="7" stroke-linejoin="round"/>' % dstr(c_sps))

# ---------- east asia (6398x4950) ----------
EP = paths(os.path.join(K, "east_asia_overlay.svg"), ["china", "taiwan"])
svgfile("ea_china.svg", 6398, 4950, '<path d="%s" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="5" stroke-linejoin="round"/>' % dstr(tf(subpaths(EP["china"]), idn, minstep=2.0)))
svgfile("ea_taiwan.svg", 6398, 4950, '<path d="%s" fill="#f0efe8" fill-opacity="0.16" stroke="#9fdcf0" stroke-width="6" stroke-linejoin="round"/>' % dstr(tf(subpaths(EP["taiwan"]), idn, minstep=1.0, minlen=3)))

# ---------- silhouettes for the paper diagram ----------
def fit(sps, box):
    xs = [p[0] for s in sps for p in s]; ys = [p[1] for s in sps for p in s]
    bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
    s = min(box / (bx1 - bx0), box / (by1 - by0))
    out = [[((x - bx0) * s, (y - by0) * s) for x, y in sp] for sp in sps]
    out = [[p for i, p in enumerate(sp) if i == 0 or abs(p[0] - sp[i - 1][0]) + abs(p[1] - sp[i - 1][1]) > 0] for sp in out]
    return out, (bx1 - bx0) * s, (by1 - by0) * s
us48 = tf(subpaths(WP["united_states_of_america"]), idn, keep=lower48, minstep=14, minlen=10)
cn = tf(subpaths(WP["china"]), idn, minstep=14, minlen=10)
us_f, uw, uh = fit(us48, 560)
cn_f, cw, ch = fit(cn, 520)
json.dump({"us": {"d": dstr(us_f), "w": uw, "h": uh}, "china": {"d": dstr(cn_f), "w": cw, "h": ch}},
          open(os.path.join(OUT, "silhouettes.json"), "w"))
print("world", W, H, meta["places"])
print("silhouettes", len(dstr(us_f)), len(dstr(cn_f)), uw, uh, cw, ch)
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT, f)))
