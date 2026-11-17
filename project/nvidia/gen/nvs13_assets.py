"""nvs13 derived assets: Pacific-centred world night crop (lon 62E -> 64W, lat 76N -> 56S) + China/US fill masks.
Run: .venv/bin/python project/nvidia/gen/nvs13_assets.py   -> assets/nvidia/nvs13/derived/
"""
import re, json, os
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
OUT = os.path.join(ROOT, "assets/nvidia/nvs13/derived"); os.makedirs(OUT, exist_ok=True)
K = 45.5111                      # world px per degree
LON0, LON1, LAT0, LAT1 = 62.0, 296.0, 76.0, -56.0   # 296 = 64W
W_OUT = 2400
k = W_OUT / ((LON1 - LON0) * K)
H_OUT = round((LAT0 - LAT1) * K * k)
x0 = LON0 + 180   # in world px units / K

def wx(lon):   # world x for lon in [70, 300]
    return ((lon if lon <= 180 else lon - 360) + 180) * K

world = Image.open(os.path.join(ROOT, "assets/maps/kit/world_night.jpg"))
ya, yb = round((90 - LAT0) * K), round((90 - LAT1) * K)
a = world.crop((round(wx(LON0)), ya, 16384, yb))
b = world.crop((0, ya, round(wx(LON1)), yb))
pano = Image.new("RGB", (a.width + b.width, a.height)); pano.paste(a, (0, 0)); pano.paste(b, (a.width, 0))
pano = pano.resize((W_OUT, H_OUT), Image.LANCZOS)
pano.save(os.path.join(OUT, "pacific_world_night.jpg"), quality=90)

svg = open(os.path.join(ROOT, "assets/maps/kit/world_overlay.svg")).read()
def mask(cid, name, rgba, edge):
    d = re.search(r'<path id="%s"[^>]*d="([^"]+)"' % cid, svg).group(1)
    im = Image.new("RGBA", (W_OUT, H_OUT), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    for sub in d.split("M")[1:]:
        pts = [tuple(map(float, p.split(","))) for p in re.split(r"[LZ]", sub) if p.strip()]
        out = []
        for (x, y) in pts:
            if x < wx(LON0) - 1: x += 16384          # west of 70E -> east side of the antimeridian
            out.append(((x - wx(LON0)) * k, (y - ya) * k))
        xs = [p[0] for p in out]
        if max(xs) - min(xs) > W_OUT * 0.5: continue   # broken ring across the seam
        if len(out) > 2: dr.polygon(out, fill=rgba)
    a = im.split()[3]
    e = a.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(3))
    ed = Image.new("RGBA", im.size, edge); ed.putalpha(e.point(lambda v: 255 if v > 40 else 0))
    im = Image.alpha_composite(im, ed)
    im.save(os.path.join(OUT, name))
    bb = a.getbbox(); print(name, bb)
    return bb
info = {"size": [W_OUT, H_OUT], "k": k, "lon0": LON0, "lat0": LAT0,
        "formula": "x = ((lon<62?lon+360:lon) - 62) * 45.5111 * k ; y = (76 - lat) * 45.5111 * k"}
info["china_bbox"] = mask("c-china", "china_fill.png", (220, 47, 60, 125), (246, 164, 169, 255))
info["usa_bbox"] = mask("c-united_states_of_america", "usa_fill.png", (42, 159, 201, 125), (159, 220, 240, 255))
def P(lon, lat): return [round(((lon if lon >= 62 else lon + 360) - 62) * K * k, 1), round((76 - lat) * K * k, 1)]
info["places"] = {"beijing": P(116.4, 39.9), "china_c": P(104, 34), "us_c": P(-99, 39), "washington": P(-77.0, 38.9), "shenzhen": P(114.06, 22.54)}
json.dump(info, open(os.path.join(OUT, "pacific_world.json"), "w"), indent=1)
print(json.dumps(info))
