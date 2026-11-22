"""Build compositions/cts01.html from cts01_template.html, inlining the map data (pixel positions computed from the kit json files).
Run: python3 project/cartels/gen/build_cts01.py   (after cts01_assets.py)"""
import json, math, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
KIT = f"{ROOT}/assets/maps/kit"
DER = f"{ROOT}/assets/cartels/cts01/derived"
src = open(f"{ROOT}/project/cartels/gen/cts01_template.html").read()

# ---- inset card (sc002): wide Mexico (60 px/deg, x=(lon+118)*60, y=(33-lat)*60) + kit sinaloa close-up ----
wide = json.load(open(f"{DER}/mexico_wide.json"))
close = json.load(open(f"{DER}/sinaloa_close.json"))
sj = json.load(open(f"{KIT}/sinaloa.json"))
WX = lambda lon: (lon + 118) * 60.0
WY = lambda lat: (33 - lat) * 60.0
CX = lambda lon: (lon + 110.0) * 1258.32
CY = lambda lat: (27.4 - lat) * 1400.0
b = [WX(-109.6), WY(26.6), WX(-107.0) - WX(-109.6), WY(24.8) - WY(26.6)]
gx, gy = sj["places"]["guasave"]["x"], sj["places"]["guasave"]["y"]
CW = 784
cs0 = CW / (CX(-107.0) - CX(-109.6))
M = {
    "gw": [b[0] + b[2] / 2, b[1] + b[3] / 2],
    "box": [round(v, 1) for v in b],
    "gc": [round(CX(-108.3), 1), round(CY(25.7), 1)],
    "gc2": [2150, 2700], "cs0": round(cs0, 4), "cs1": 0.45,
    "gu": [gx, gy], "sl": [2560 - 95 / 0.45, 3000],
    "sinC": close["sinaloa"],
}

# ---- aerials (sc004 Kuroda Park z18, sc007 Guasave z16) — kit files if present ----
def merc(lon, lat, z, x0, y0):
    n = 2 ** z
    x = ((lon + 180) / 360 * n - x0) * 256
    r = math.radians(lat)
    y = ((1 - math.log(math.tan(r) + 1 / math.cos(r)) / math.pi) / 2 * n - y0) * 256
    return x, y

def aerial(name):
    p = f"{KIT}/aerial_{name}.json"
    if not os.path.exists(p):
        return None
    j = json.load(open(p))
    tb = j["tile_bounds"]
    return j, (lambda lon, lat: merc(lon, lat, j["zoom"], tb["x0"], tb["y0"]))

KP = (-108.47593, 25.58140)
a = aerial("guasave_kuroda_park_z18")
if a:
    j, P = a
    kx, ky = P(*KP)
    ol = ""
    svgp = f"{KIT}/aerial_guasave_kuroda_park_z18_overlay.svg"
    for cand in (svgp,):
        if os.path.exists(cand):
            m = re.search(r'id="o-kuroda_park"[^>]*\sd="([^"]+)"', open(cand).read()) or re.search(r'd="([^"]+)"[^>]*id="o-kuroda_park"', open(cand).read())
            if m: ol = m.group(1)
    if "outlines" in j and not ol:
        o = j["outlines"].get("kuroda_park")
        if isinstance(o, str): ol = o
    AER = {"src": f"assets/maps/kit/{j['image']}", "w": j["width"], "h": j["height"], "kp": [kx, ky]}
else:
    AER = None
M["aerial_ok"] = bool(AER)

out = src
src_aer = AER or {"src": "assets/maps/kit/sinaloa_sat.jpg", "w": 4027, "h": 4060, "kp": [1917, 2545]}
out = out.replace("__AER_SRC__", src_aer["src"]).replace("__AER_W__", str(src_aer["w"])).replace("__AER_H__", str(src_aer["h"]))
M["aer"] = json.load(open(f"{ROOT}/project/cartels/gen/cts01_aerial.json")) if os.path.exists(f"{ROOT}/project/cartels/gen/cts01_aerial.json") else {}
if a and j.get("outlines_px", {}).get("kuroda_park"):   # OSM stadium outline (ODbL) from the kit json
    M["aer"]["outline"] = "".join("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in ring) + "Z" for ring in j["outlines_px"]["kuroda_park"])
    M["aer"]["kp"] = [kx, ky]


c = aerial("guasave_z16")
src_city = {"src": f"assets/maps/kit/{c[0]['image']}", "w": c[0]["width"], "h": c[0]["height"]} if c else {"src": "assets/maps/kit/sinaloa_sat.jpg", "w": 4027, "h": 4060}
out = out.replace("__CITY_SRC__", src_city["src"]).replace("__CITY_W__", str(src_city["w"])).replace("__CITY_H__", str(src_city["h"]))
M["city"] = json.load(open(f"{ROOT}/project/cartels/gen/cts01_city.json")) if os.path.exists(f"{ROOT}/project/cartels/gen/cts01_city.json") else {}

HL = json.load(open(f"{ROOT}/project/cartels/gen/cts01_hl.json")) if os.path.exists(f"{ROOT}/project/cartels/gen/cts01_hl.json") else {"x": 600, "y": 440, "w": 300}
out = out.replace("__HL_X__", str(HL["x"])).replace("__HL_Y__", str(HL["y"])).replace("__HL_W__", str(HL["w"]))
out = out.replace("__MAPDATA__", json.dumps(M))
open(f"{ROOT}/compositions/cts01.html", "w").write(out)
print("wrote compositions/cts01.html", len(out), "aerial:", bool(AER), "city:", bool(c))
