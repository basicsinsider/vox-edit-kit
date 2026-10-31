"""Derived assets for compositions/c3s03.html (c3 LOCAL 404.17–602.02).
Run from the project root: .venv/bin/python project/c3/gen/c3s03_assets.py  → assets/c3/derived/c3s03/
Map crops from assets/maps/kit (world night 6144, East Asia satdesat 0.5, Africa Blue-Marble satdesat crop),
simplified country paths (paths.json), footage freeze frames."""
import re, json, pathlib, subprocess
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = pathlib.Path("assets/maps/kit"); O = pathlib.Path("assets/c3/derived/c3s03"); O.mkdir(parents=True, exist_ok=True)

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

def paths(svgfile, ids=None):
    src = open(svgfile).read(); out = {}
    for m in re.finditer(r'<path id="c-([a-z_]+)"[^>]* d="([^"]+)"', src):
        cid = m.group(1)
        if ids and cid not in ids: continue
        out[cid] = [[(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", sub)]
                    for sub in re.split(r"M", m.group(2).replace("Z", "").replace("z", "")) if sub.strip()]
    return out

def to_d(rings, f, eps, minlen=6):
    d = ""
    for r in rings:
        if len(r) < 3: continue
        p = [f(x, y) for x, y in r]
        if max(abs(p[i][0] - p[i - 1][0]) for i in range(1, len(p))) > 300: continue   # antimeridian
        h = len(p) // 2
        p = rdp(p[:h + 1], eps)[:-1] + rdp(p[h:], eps)
        if len(p) < 3: continue
        xs = [q[0] for q in p]; ys = [q[1] for q in p]
        if max(xs) - min(xs) < minlen and max(ys) - min(ys) < minlen: continue
        d += "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in p) + "Z"
    return d

res = {}
# --- world night 6144 (x=(lon+180)*17.0667, y=(90-lat)*17.0667) — C3S078, C3S094, C3S098
if not (O / "world_night_6144.jpg").exists():
    Image.open(K / "world_night.jpg").resize((6144, 3072), Image.LANCZOS).save(O / "world_night_6144.jpg", quality=88)
s = 6144 / 16384
P = paths(K / "world_overlay.svg")
res["world"] = {"size": [6144, 3072], "k": 17.0667, "d": {k: to_d(v, lambda x, y: (x * s, y * s), 1.6, 3) for k, v in P.items() if k not in ("antarctica",)}}
res["world"]["d"] = {k: v for k, v in res["world"]["d"].items() if v}

# --- East Asia satdesat 0.5 — C3S080
if not (O / "east_asia_satdesat_3199.jpg").exists():
    ea = Image.open(K / "east_asia_satdesat.jpg"); ea.resize((ea.width // 2, ea.height // 2), Image.LANCZOS).save(O / "east_asia_satdesat_3199.jpg", quality=88)
P = paths(K / "east_asia_overlay.svg", ["china", "taiwan"])
res["east_asia"] = {"size": [3199, 2475], "d": {k: to_d(v, lambda x, y: (x * 0.5, y * 0.5), 1.2, 4) for k, v in P.items()}}

# --- Africa Blue Marble satdesat crop: lon -25..60, lat -38..40 at 36 px/deg — C3S104
A = dict(lon0=-25, lon1=60, lat0=-38, lat1=40, k=36.0)
W, H = int((A["lon1"] - A["lon0"]) * A["k"]), int((A["lat1"] - A["lat0"]) * A["k"])
if not (O / "africa_satdesat.jpg").exists():
    big = Image.open(K / "world_satdesat_21600.jpg"); KB = 60.0
    box = (int((A["lon0"] + 180) * KB), int((90 - A["lat1"]) * KB), int((A["lon1"] + 180) * KB), int((90 - A["lat0"]) * KB))
    big.crop(box).resize((W, H), Image.LANCZOS).save(O / "africa_satdesat.jpg", quality=88); del big
af = None
P = paths(K / "world_overlay.svg")
WK = 45.5111
f = lambda x, y: ((x / WK - 180 - A["lon0"]) * A["k"], (90 - y / WK - (90 - A["lat1"])) * A["k"])
afr = ["ghana", "guinea", "nigeria", "senegal", "mali", "c_te_d_ivoire", "cameroon", "chad", "niger", "congo", "dem_rep_congo", "gabon",
       "central_african_rep", "madagascar", "somalia", "mauritania", "burkina_faso", "togo", "benin", "tanzania", "uganda", "kenya", "zambia",
       "malawi", "sudan", "s_sudan", "morocco", "tunisia", "algeria", "sierra_leone", "rwanda", "burundi", "libya", "egypt", "ethiopia", "liberia",
       "south_africa", "angola", "mozambique", "namibia", "botswana", "zimbabwe", "w_sahara", "eritrea", "djibouti", "somaliland", "gambia",
       "guinea_bissau", "eq_guinea", "lesotho", "eswatini"]
res["africa"] = {"size": [W, H], "geo": A, "d": {k: to_d(P[k], f, 1.4, 4) for k in afr if k in P}}

# --- Asia Blue Marble satdesat crop: lon 70..140, lat 14..56 at 45 px/deg — C3S080 (whole China + Taiwan)
B = dict(lon0=70, lon1=140, lat0=14, lat1=56, k=45.0)
W2, H2 = int((B["lon1"] - B["lon0"]) * B["k"]), int((B["lat1"] - B["lat0"]) * B["k"])
if not (O / "asia_satdesat.jpg").exists():
    big = Image.open(K / "world_satdesat_21600.jpg"); KB = 60.0
    box = (int((B["lon0"] + 180) * KB), int((90 - B["lat1"]) * KB), int((B["lon1"] + 180) * KB), int((90 - B["lat0"]) * KB))
    big.crop(box).resize((W2, H2), Image.LANCZOS).save(O / "asia_satdesat.jpg", quality=88); del big
g = lambda x, y: ((x / WK - 180 - B["lon0"]) * B["k"], (90 - y / WK - (90 - B["lat1"])) * B["k"])
res["asia"] = {"size": [W2, H2], "geo": B, "d": {k: to_d(P[k], g, 1.2, 4) for k in ["china", "taiwan", "mongolia"]}}
del res["east_asia"]

# --- 1950 PRC stamp: crop off the black scan margin
st = Image.open("assets/c3/posters/prc_stamp_1950_sino_soviet_friendship.jpg").convert("RGB")
bb = st.convert("L").point(lambda v: 255 if v > 150 else 0).getbbox(); st.crop(bb).save(O / "prc_stamp_1950_crop.jpg", quality=92); print("stamp", bb)

json.dump(res, open(O / "paths.json", "w"), separators=(",", ":"))
for k, v in res.items(): print(k, v["size"], len(v["d"]), sum(len(x) for x in v["d"].values()))

# --- freeze frames (last/held frames under short clips)
def still(src, t, name):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", str(O / name)], check=True)
still("assets/intro/footage/rotary_phone_1970_dialing.mp4", 2.58, "rotary_phone_freeze.jpg")
still("assets/c4/footage/un_1950_security_council_president_china_delegate.mp4", 4.6, "un_1950_roc_delegate_last.jpg")
still("assets/c3/footage/newsreel_1960_un_general_assembly_hall_wide.mp4", 6.9, "un_ga_1960_hall_last.jpg")
print("stills ok")
