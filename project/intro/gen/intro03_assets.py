"""Derived assets for compositions/intro03.html (crops, grades, simplified map paths).
Run: .venv/bin/python project/intro/gen/intro03_assets.py   -> assets/intro/derived/intro03/ + data.json"""
import json, pathlib, subprocess
from PIL import Image, ImageOps, ImageEnhance
R = pathlib.Path(__file__).resolve().parents[3]
A = R / "assets/intro"; O = A / "derived/intro03"; O.mkdir(parents=True, exist_ok=True)

def crop(src, box, out, size=None, q=88):
    im = Image.open(A / src).convert("RGB").crop(box)
    if size: im = im.resize(size, Image.LANCZOS)
    im.save(O / out, quality=q); return im

# portraits
crop("photos/chang_2018.jpg", (330, 0, 1290, 1280), "chang_poster.jpg", (840, 1120))
crop("photos/tsao_portrait_studio.jpg", (40, 60, 1240, 1660), "tsao_poster.jpg", (840, 1120))
crop("photos/chang_award.jpg", (1050, 60, 1430, 440), "chang_circle.jpg", (420, 420))
crop("photos/tsao_rally_2023.jpg", (780, 560, 1130, 910), "tsao_circle.jpg", (420, 420))

# world maps: beige (paper) + dark (night) grades of the NASA desat basemap at 0.4 scale
w = Image.open(A / "maps/world_basemap_desat.jpg").convert("L").resize((4320, 2160), Image.LANCZOS)
w = ImageEnhance.Contrast(w).enhance(1.15)
beige = ImageOps.colorize(w, black="#6f6656", white="#efe6d2", mid="#c9bea6"); beige.save(O / "world_beige.jpg", quality=86)
dark = ImageOps.colorize(w, black="#07090c", white="#8d9296", mid="#2b3036"); dark.save(O / "world_dark.jpg", quality=86)

# simplified country paths (scale 0.4)
wj = json.load(open(A / "maps/world_basemap_desat.json"))
import re
def simp(d, s=0.4, step=0.9):
    out = []
    for sub in re.split(r"(?=M)", d):
        pts = re.findall(r"(-?[\d.]+),(-?[\d.]+)", sub)
        if len(pts) < 3: continue
        keep, last = [], None
        for x, y in pts:
            x, y = float(x) * s, float(y) * s
            if last is None or abs(x - last[0]) + abs(y - last[1]) > step * 2.2:
                keep.append((x, y)); last = (x, y)
        if len(keep) < 3: continue
        xs = [p[0] for p in keep]; ys = [p[1] for p in keep]
        if (max(xs) - min(xs)) * (max(ys) - min(ys)) < 30: continue
        out.append("M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in keep) + "Z")
    return "".join(out)
C = wj["countries"]
west = ["United States of America", "Canada", "Mexico", "Brazil", "Argentina", "Chile", "Peru", "Colombia", "Venezuela", "Bolivia",
        "United Kingdom", "France", "Germany", "Spain", "Italy", "Portugal", "Netherlands", "Belgium", "Switzerland", "Austria",
        "Poland", "Sweden", "Norway", "Finland", "Denmark", "Ireland", "Greece", "Czechia", "Hungary", "Romania", "Ukraine",
        "Ecuador", "Uruguay", "Paraguay", "Iceland", "Bulgaria", "Serbia", "Croatia", "Slovakia", "Belarus", "Lithuania", "Latvia", "Estonia",
        "Guatemala", "Honduras", "Nicaragua", "Cuba", "Panama", "Costa Rica", "Guyana", "Suriname", "Bosnia and Herz.", "Albania", "Slovenia", "Moldova", "North Macedonia", "Montenegro", "Kosovo", "Luxembourg", "El Salvador", "Belize", "Dominican Rep.", "Haiti", "Jamaica", "Greenland"]
missing = [k for k in west if k not in C]
copies = {"India": "bangalore", "China": "shenzhen", "Israel": "tel_aviv", "France": "sophia_antipolis", "Russia": "skolkovo_moscow",
          "Japan": "tsukuba", "United Kingdom": "london", "Germany": "berlin", "Singapore": "singapore", "United Arab Emirates": "dubai",
          "South Korea": "seoul", "Brazil": None, "Chile": None, "Canada": None, "Malaysia": None, "Nigeria": None, "Kenya": None, "Australia": None}
missing += [k for k in copies if k not in C]
data = {"west": "".join(simp(C[k]["d"]) for k in west if k in C),
        "copies": {k: simp(C[k]["d"], step=1.2) for k in copies if k in C},
        "taiwan": simp(C["Taiwan"]["d"], step=0.2) if "Taiwan" in C else "",
        "places": {k: [round(v["x"] * 0.4, 1), round(v["y"] * 0.4, 1)] for k, v in wj["places"].items()}}
# country centroids for copies without a named place
for k in copies:
    if k in C and not copies[k]:
        pts = [tuple(map(float, p)) for p in re.findall(r"(-?[\d.]+),(-?[\d.]+)", C[k]["d"])]
        xs = sorted(p[0] for p in pts); ys = sorted(p[1] for p in pts)
        data["places"][k] = [round(xs[len(xs)//2] * 0.4, 1), round(ys[len(ys)//2] * 0.4, 1)]
    elif k in C: data["places"][k] = data["places"][copies[k]]
data["copyPlace"] = {k: (copies[k] or k) for k in copies if k in C}
# Taiwan relief outline (2480x3040 space)
tj = json.load(open(A / "maps/taiwan_relief_grey.json"))
data["twRelief"] = tj["countries"]["Taiwan"]["d"]
data["twPlaces"] = {k: [v["x"], v["y"]] for k, v in tj["places"].items()}
# Hsinchu satellite (3728x2823) features
sj = json.load(open(A / "maps/hsinchu_s2cloudless2016.json"))
data["hs"] = {k: {"name": v["name"], "d": v["d"]} for k, v in sj["osm_features"].items()}
data["hsPlaces"] = {k: [v["x"], v["y"]] for k, v in sj["places"].items()}
json.dump(data, open(O / "data.json", "w"), separators=(",", ":"))
print("missing:", missing, "bytes:", (O / "data.json").stat().st_size)

# historic Taiwan stills (1960 colour film) for the D07 collage
for f, t in [("taiwan_1960_taipei_boulevard_high_angle", 4), ("taiwan_1960_taipei_north_gate_traffic", 3), ("taiwan_1960_sun_moon_lake", 5)]:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(A / f"footage/{f}.mp4"), "-frames:v", "1", "-q:v", "3", str(O / f"{f}.jpg")], check=True)
print("ok")
