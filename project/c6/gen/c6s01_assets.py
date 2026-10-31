"""c6s01 derived assets (run with .venv/bin/python from the repo root). Idempotent.
Outputs assets/c6/derived/c6s01/ + paths.json (inlined into compositions/c6s01.html by build_c6s01.py)."""
import json, re, shutil, subprocess, pathlib
from PIL import Image, ImageFilter, ImageDraw, ImageChops
Image.MAX_IMAGE_PIXELS = None
R = pathlib.Path(".")
O = R / "assets/c6/derived/c6s01"; O.mkdir(parents=True, exist_ok=True)
K = R / "assets/maps/kit"

def frame(src, t, out):
    if not (O / out).exists():
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", str(O / out)], check=True)

# 1971 film stills (UN film, fair use)
frame("assets/c6/footage/un1971_vote_hall_pan_to_board.mp4", 4.6, "un1971_hall_wide.jpg")
frame("assets/c6/footage/un1971_us_desk.mp4", 0.3, "un1971_delegates_seated.jpg")
frame("assets/c6/footage/un1971_celebration_delegate_clapping.mp4", 1.5, "un1971_dancing_still.jpg")

# real slogan wall (Taichung) — strip of the eight characters for the scroll + decoration
src = R / "assets/c6/photos/slogan_zhuangjing_ziqiang_taichung_wall.jpg"
if not (O / "slogan_strip.jpg").exists():
    im = Image.open(src).convert("RGB")
    im.crop((270, 500, 1690, 700)).save(O / "slogan_strip.jpg", quality=92)

# Taiwan relief (map kit night) at half size + baked celadon fill (halftone + soft glow) in the same pixel space
if not (O / "taiwan_celadon.png").exists():
    W, H = 1623, 2200
    Image.open(K / "taiwan_night.jpg").resize((W, H), Image.LANCZOS).save(O / "taiwan_night_1623.jpg", quality=90)
    m = Image.open(K / "taiwan_landmask.png").convert("L").resize((W, H), Image.LANCZOS)
    m = m.point(lambda v: 255 if v > 127 else 0)
    cel = (159, 199, 178); dark = (111, 156, 134)
    fill = Image.new("RGB", (W, H), cel)
    dots = Image.new("L", (W, H), 0); d = ImageDraw.Draw(dots)
    s = 11
    for y in range(-s, H + s, s):
        for x in range(-s, W + s, s):
            ox = (s / 2) if (y // s) % 2 else 0
            d.ellipse((x + ox - 2.6, y - 2.6, x + ox + 2.6, y + 2.6), fill=150)
    fill = Image.composite(Image.new("RGB", (W, H), dark), fill, dots)
    edge = m.filter(ImageFilter.GaussianBlur(9))
    glow = Image.new("RGBA", (W, H), cel + (0,)); glow.putalpha(edge.point(lambda v: int(v * 0.55)))
    body = fill.convert("RGBA"); body.putalpha(m.point(lambda v: int(v * 0.92)))
    out = Image.alpha_composite(glow, body)
    out.save(O / "taiwan_celadon.png", optimize=True)

def svg_paths(svgfile, ids):
    s = pathlib.Path(svgfile).read_text()
    res = {}
    for i in ids:
        m = re.search(r'<path id="c-%s"[^>]* d="([^"]+)"' % i, s) or re.search(r'<path[^>]*id="c-%s"[^>]*d="([^"]+)"' % i, s)
        if m: res[i] = m.group(1)
    return res

def scale_d(d, sx, sy, nd=1, minstep=2.0):
    out = []
    for sub in re.split(r"(?=M)", d):
        pts = re.findall(r"(-?\d+(?:\.\d+)?),?\s*(-?\d+(?:\.\d+)?)", sub)
        if len(pts) < 3: continue
        q = []; last = None
        for x, y in pts:
            X, Y = float(x) * sx, float(y) * sy
            if last and abs(X - last[0]) + abs(Y - last[1]) < minstep: continue
            q.append((X, Y)); last = (X, Y)
        if len(q) < 3: continue
        out.append("M" + "L".join(f"{x:.{nd}f} {y:.{nd}f}" for x, y in q) + "Z")
    return "".join(out)

P = {}
c3 = json.load(open("assets/c3/derived/c3s03/paths.json"))
af = c3["africa"]["d"]
P["africa"] = {"size": c3["africa"]["size"], "d": af}
switched = ["canada", "italy", "turkey", "iran", "belgium", "peru", "lebanon", "mexico", "argentina", "japan", "germany",
            "australia", "new_zealand", "greece", "malaysia", "brazil", "philippines", "thailand"]
P["world"] = {"size": c3["world"]["size"], "order": switched, "d": {k: c3["world"]["d"][k] for k in switched + ["taiwan", "china"]}}
ea = svg_paths(K / "east_asia_overlay.svg", ["japan", "china", "taiwan", "south_korea"])
P["east_asia"] = {"size": [3199, 2475], "d": {k: scale_d(v, 0.5, 0.5, 0, 7.0) for k, v in ea.items()}}
json.dump(P, open(O / "paths.json", "w"))
print({k: (v["size"], {n: len(d) for n, d in v["d"].items()} if k != "africa" else len(v["d"])) for k, v in P.items()})

# newspaper pages at a browser-friendly size (≤ native)
if not (O / "kansan_1971-10-26_1800.jpg").exists():
    Image.open("assets/c3/newspapers/university_daily_kansan_1971-10-26_frontpage.jpg").convert("L").resize((1800, 2254), Image.LANCZOS).save(O / "kansan_1971-10-26_1800.jpg", quality=90)
