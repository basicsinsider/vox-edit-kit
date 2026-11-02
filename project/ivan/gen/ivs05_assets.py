"""ivs05 derived maps: Russia-wide night crop (world kit) + Eastern Europe night crop, with country paths
transformed into each crop's pixel space -> assets/ivan/ivs05/derived/ (jpg + paths json). Run from repo root."""
import re, json
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
OUT = "assets/ivan/ivs05/derived/"

def subpaths(d):
    out = []
    for part in re.split(r"(?=M)", d):
        pts = [(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", part)]
        if len(pts) > 2: out.append(pts)
    return out

def to_d(subs, f, W, H, minstep=2.5, margin=200):
    res = []
    for pts in subs:
        q = [f(x, y) for x, y in pts]
        xs = [p[0] for p in q]; ys = [p[1] for p in q]
        if max(xs) < -margin or min(xs) > W + margin or max(ys) < -margin or min(ys) > H + margin: continue
        pieces, keep = [], [q[0]]
        for p in q[1:]:
            if abs(p[0] - keep[-1][0]) > 400: pieces.append(keep); keep = [p]; continue   # antimeridian jump -> split
            if abs(p[0] - keep[-1][0]) + abs(p[1] - keep[-1][1]) >= minstep: keep.append(p)
        pieces.append(keep)
        for k in pieces:
            if len(k) >= 3: res.append("M" + "L".join("%.1f,%.1f" % p for p in k) + "Z")
        continue
        res.append("M" + "L".join("%.1f,%.1f" % p for p in keep) + "Z")
    return "".join(res)

def path_of(svg, cid):
    return re.search(r'<path id="%s"[^>]*d="([^"]*)"' % cid, svg).group(1)

# ---- A: Russia-wide from world_night (45.511 px/deg) -> lon 15..120, lat 28..82 at 32 px/deg
K = 45.511; L0, L1, B0, B1, P = 15, 120, 28, 82, 32
im = Image.open("assets/maps/kit/world_night.jpg")
box = (int((L0 + 180) * K), int((90 - B1) * K), int((L1 + 180) * K), int((90 - B0) * K))
W, H = int((L1 - L0) * P), int((B1 - B0) * P)
im.crop(box).resize((W, H), Image.LANCZOS).save(OUT + "russia_wide_night.jpg", quality=86)
svg = open("assets/maps/kit/world_overlay.svg").read()
fa = lambda x, y: ((x / K - 180 - L0) * P, (y / K - (90 - B1)) * P)
wa = {"w": W, "h": H, "ppd": P, "lon0": L0, "lat1": B1,
      "russia": to_d(subpaths(path_of(svg, "c-russia")), fa, W, H, 5.0),
      "ukraine": to_d(subpaths(path_of(svg, "c-ukraine")), fa, W, H, 3.0)}
# Crimea belongs to Ukraine (Krish fix round 1): take #c-crimea from the Eastern Europe overlay (x=(lon-20)*147.768,
# y=(62-lat)*240) and re-project into this crop; the composition adds it to Ukraine and masks it out of Russia.
ees = open("assets/maps/kit/eastern_europe_overlay.svg").read()
fc = lambda x, y: ((x / 147.768 + 20 - L0) * P, (B1 - (62 - y / 240)) * P)
wa["crimea"] = to_d(subpaths(path_of(ees, "c-crimea")), fc, W, H, 1.5)
print("A", W, H, len(wa["russia"]), len(wa["ukraine"]), len(wa["crimea"]))

# ---- B: Eastern Europe night crop lon 28..56, lat 46..60, half resolution
ee = json.load(open("assets/maps/kit/eastern_europe.json"))
kx, ky = ee["px_per_degree_lon"], ee["px_per_degree_lat"]
E0, E1, N0, N1, S = 28, 56, 46, 60, 0.5
im = Image.open("assets/maps/kit/eastern_europe_night.jpg")
box = (int((E0 - 20) * kx), int((62 - N1) * ky), int((E1 - 20) * kx), int((62 - N0) * ky))
Wb, Hb = int((box[2] - box[0]) * S), int((box[3] - box[1]) * S)
im.crop(box).resize((Wb, Hb), Image.LANCZOS).save(OUT + "ee_night_crop.jpg", quality=86)
svg = open("assets/maps/kit/eastern_europe_overlay.svg").read()
fb = lambda x, y: ((x - box[0]) * S, (y - box[1]) * S)
wb = {"w": Wb, "h": Hb, "kx": kx * S, "ky": ky * S, "lon0": E0, "lat1": N1,
      "russia": to_d(subpaths(path_of(svg, "c-russia")), fb, Wb, Hb, 7.0),
      "ukraine": to_d(subpaths(path_of(svg, "c-ukraine")) + subpaths(path_of(svg, "c-crimea")), fb, Wb, Hb, 4.0)}
print("B", Wb, Hb, len(wb["russia"]), len(wb["ukraine"]))
json.dump({"wide": wa, "ee": wb}, open(OUT + "ivs05_map_paths.json", "w"))

# ---- C: Alabuga SEZ (Yelabuga) Esri z16 mosaic -> 1920x1080 (fetch: MK_CACHE=/tmp/ivs05/tiles python3 tools/map_tiles.py
#      fetch esri 16 51.985 55.812 52.095 55.862; mosaic tiles x 42231.., y 20452.. (21x17) -> crop (600,1500,4700,3806) -> resize)
