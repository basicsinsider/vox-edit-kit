"""ivs04 derived maps: Russia crops (world night / satdesat) + country fill PNGs; eastern_europe fills.
Run: .venv/bin/python project/ivan/gen/ivs04_assets.py   (writes assets/ivan/ivs04/derived/)"""
import re, json, os
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
R = os.path.dirname(os.path.abspath(__file__)) + "/../../.."
K = R + "/assets/maps/kit/"; O = R + "/assets/ivan/ivs04/derived/"
def subpaths(svg, cid):
    m = re.search(r'<path id="' + cid + r'"[^>]*d="([^"]*)"', svg)
    out = []
    for sp in m.group(1).split("M")[1:]:
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sp)]
        ok = [pts[0]]
        for p in pts[1:]:
            if abs(p[0] - ok[-1][0]) > 400: ok = None; break
            ok.append(p)
        if ok and len(ok) > 2: out.append(ok)
    return out
def fill(svg, cid, size, tf, rgb, name, blur=0):
    im = Image.new("L", size, 0); d = ImageDraw.Draw(im)
    for sp in subpaths(svg, cid): d.polygon([tf(p) for p in sp], fill=255)
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    rgba = Image.new("RGBA", size, rgb + (0,)); rgba.putalpha(im); rgba.save(O + name); print(name, size)
def edge(svg, cid, size, tf, rgb, name, w):
    im = Image.new("RGBA", size, (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for sp in subpaths(svg, cid):
        q = [tf(p) for p in sp]; d.line(q + [q[0]], fill=rgb + (255,), width=w, joint="curve")
    im.save(O + name); print(name)
# --- Russia crop of the world maps: lon 18..112, lat 38..72
L0, L1, A0, A1 = 18, 112, 30, 78
ws = open(K + "world_overlay.svg").read()
k = 45.5111
box = (round((L0 + 180) * k), round((90 - A1) * k), round((L1 + 180) * k), round((90 - A0) * k))
night = Image.open(K + "world_night.jpg").crop(box); night.save(O + "russia_night.jpg", quality=90); print("russia_night", night.size)
atl = Image.open(K + "world_atlas.jpg").crop(box); atl.save(O + "russia_atlas.jpg", quality=90); print("russia_atlas", atl.size)
k2 = 21600 / 360
box2 = (round((L0 + 180) * k2), round((90 - A1) * k2), round((L1 + 180) * k2), round((90 - A0) * k2))
sd = Image.open(K + "world_satdesat_21600.jpg").crop(box2).resize(night.size, Image.LANCZOS); sd.save(O + "russia_satdesat.jpg", quality=90); print("russia_satdesat", sd.size)
tf = lambda p: (p[0] - box[0], p[1] - box[1])
fill(ws, "c-russia", night.size, tf, (179, 42, 34), "russia_fill_ru.png")
fill(ws, "c-ukraine", night.size, tf, (147, 189, 232), "russia_fill_ua.png")
edge(ws, "c-ukraine", night.size, tf, (147, 189, 232), "russia_edge_ua.png", 3)
json.dump({"lon0": L0, "lat1": A1, "k": k, "w": night.size[0], "h": night.size[1],
           "formula": "x=(lon-18)*45.5111, y=(78-lat)*45.5111"}, open(O + "russia_map.json", "w"), indent=1)
# --- eastern europe atlas fills (kit pixel space 6206x4800)
es = open(K + "eastern_europe_overlay.svg").read()
ident = lambda p: p
fill(es, "c-russia", (6206, 4800), ident, (179, 42, 34), "ee_fill_ru.png")
fill(es, "c-ukraine", (6206, 4800), ident, (37, 99, 176), "ee_fill_ua.png")
