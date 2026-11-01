#!/usr/bin/env python3
"""ivs07 build: inline simplified map paths (Eastern-Europe kit pixel space) into the composition.

src  : project/ivan/gen/ivs07_src.html   (edit this)
out  : compositions/ivs07.html           (generated — do not edit by hand)
Usage: python3 project/ivan/gen/ivs07_build.py
"""
import json, re, pathlib, math

ROOT = pathlib.Path(__file__).resolve().parents[3]
KIT = ROOT / "assets/maps/kit"
svg = (KIT / "eastern_europe_overlay.svg").read_text()
meta = json.loads((KIT / "eastern_europe.json").read_text())
KX, KY = 147.768, 240.0
px = lambda lon, lat: (round((lon - 20) * KX, 1), round((62 - lat) * KY, 1))

BOX = (900, 700, 4600, 4700)   # x0 y0 x1 y1 of the camera's reach (lon ~26–51, lat ~42.5–59)


def simplify(cid, tol=5.0):
    m = re.search(r'<path id="%s"[^>]*d="([^"]*)"' % cid, svg)
    out = []
    for sub in m.group(1).split("M")[1:]:
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?\d+\.?\d*,-?\d+\.?\d*", sub)]
        if len(pts) < 3:
            continue
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        if max(xs) < BOX[0] or min(xs) > BOX[2] or max(ys) < BOX[1] or min(ys) > BOX[3]:
            continue
        # clamp to a box a little larger than the camera's reach (keeps the fill valid inside it; kills antimeridian runs)
        pts = [(min(max(x, -400), 7000), min(max(y, -400), 5400)) for x, y in pts]
        keep = [pts[0]]
        for p in pts[1:]:
            if math.hypot(p[0] - keep[-1][0], p[1] - keep[-1][1]) >= tol:
                keep.append(p)
        if not keep or len(keep) < 3:
            continue
        out.append("M" + "L".join(f"{x:.0f},{y:.0f}" for x, y in keep) + "Z")
    return "".join(out)


paths = {
    "ru": simplify("c-russia"),
    "ua": simplify("c-ukraine") + simplify("c-crimea"),
    "by": simplify("c-belarus"),
}
P = meta["places"]
city = {k: px(P[k]["lon"], P[k]["lat"]) for k in ["moscow", "kyiv", "ryazan", "voronezh", "rostov_on_don", "kursk", "belgorod", "kharkiv"]}
city["tula"] = px(37.62, 54.19)
city["oryol"] = px(36.08, 52.97)
city["bryansk"] = px(34.37, 53.25)
paths["city"] = city
src = (ROOT / "project/ivan/gen/ivs07_src.html").read_text()
out = src.replace("/*@PATHS@*/", "const MAP = " + json.dumps(paths, separators=(",", ":")) + ";")
(ROOT / "compositions/ivs07.html").write_text(out)
print("ru", len(paths["ru"]), "ua", len(paths["ua"]), "by", len(paths["by"]), "->", len(out), "bytes")
