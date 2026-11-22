"""cts01 derived assets (cold open). Run: .venv/bin/python project/cartels/gen/cts01_assets.py
- meza_cut.png: Meza Flores FBI portrait, background keyed by flood fill from the borders (plain studio background)."""
import numpy as np, os
from PIL import Image, ImageFilter
from scipy import ndimage
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = f"{ROOT}/assets/cartels/cts01/derived"
os.makedirs(OUT, exist_ok=True)

def meza():
    im = Image.open(f"{ROOT}/assets/cartels/people/meza_fbi_photo_1.jpg").convert("RGB")
    a = np.asarray(im).astype(float)
    sm = ndimage.gaussian_filter(a, (2, 2, 0))
    # background colour = median of the top corners
    bg = np.median(np.concatenate([sm[:40, :40].reshape(-1, 3), sm[:40, -40:].reshape(-1, 3)]), 0)
    d = np.sqrt(((sm - bg) ** 2).sum(2))
    cand = d < 30
    lab, n = ndimage.label(cand)
    border = set(np.unique(np.concatenate([lab[0], lab[:, 0], lab[:, -1]]))) - {0}
    bgm = np.isin(lab, list(border))
    bgm = ndimage.binary_opening(bgm, iterations=2)
    fg = ~bgm
    fg = ndimage.binary_fill_holes(fg)
    fg = ndimage.binary_erosion(fg, iterations=5)
    Image.fromarray((fg * 255).astype(np.uint8)).save(f"{OUT}/meza_mask.png")
    alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6))
    print("bg", bg, "fg share", fg.mean())
    out = im.copy(); out.putalpha(alpha)
    out.save(f"{OUT}/meza_cut.png")

if __name__ == "__main__":
    meza()


def simplify(pts, tol):
    """Ramer-Douglas-Peucker on an open polyline."""
    import numpy as np
    pts = np.asarray(pts, float)
    if len(pts) < 3: return pts.tolist()
    a, b = pts[0], pts[-1]
    ab = b - a; L = np.hypot(*ab) or 1e-9
    q = pts - a; d = np.abs(ab[0] * q[:, 1] - ab[1] * q[:, 0]) / L
    i = int(d.argmax())
    if d[i] > tol:
        return simplify(pts[:i + 1], tol)[:-1] + simplify(pts[i:], tol)
    return [a.tolist(), b.tolist()]

def ring_d(ring, tol):
    h = len(ring) // 2   # simplify the two halves separately (MANUAL: RDP collapses closed rings)
    s = simplify(ring[:h + 1], tol)[:-1] + simplify(ring[h:], tol)
    return "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in s) + "Z"

def mexico_wide():
    """Inset card map: Mexico from the kit's americas_satdesat (60 px/deg), lon -118..-86, lat 33..14 -> 1920x1140,
    plus the Sinaloa state outline (Natural Earth admin-1) in the same pixel space."""
    import json
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(f"{ROOT}/assets/maps/kit/americas_satdesat.jpg")
    X = lambda lon: (lon + 180) * 60.0 - 3000
    Y = lambda lat: (90 - lat) * 60.0 - 2100
    L0, L1, A1, A0 = -118.0, -86.0, 33.0, 14.0
    box = (round(X(L0)), round(Y(A1)), round(X(L1)), round(Y(A0)))
    im.crop(box).save(f"{OUT}/mexico_wide_satdesat.jpg", quality=90)
    gj = json.load(open(f"{ROOT}/work/mapC/vec/ne_10m_admin_1.geojson"))
    out = {"box": box, "formula": "x=(lon+118)*60 ; y=(33-lat)*60"}
    for f in gj["features"]:
        p = f["properties"]
        if p.get("adm0_a3") == "MEX" and p.get("name") in ("Sinaloa",):
            g = f["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            ds = []
            for poly in polys:
                ring = [((lon - L0) * 60, (A1 - lat) * 60) for lon, lat in poly[0]]
                if len(ring) > 40: ds.append(ring_d(ring, 0.6))
            out["sinaloa"] = "".join(ds)
    json.dump(out, open(f"{OUT}/mexico_wide.json", "w"))
    print("wide", box, len(out.get("sinaloa", "")))

def sinaloa_close():
    """st-sinaloa outline from the kit sinaloa_overlay.svg, simplified (pixel space of sinaloa_*.jpg 4027x4060)."""
    import re, json
    s = open(f"{ROOT}/assets/maps/kit/sinaloa_overlay.svg").read()
    m = re.search(r'id="st-sinaloa"[^>]*?d="([^"]+)"', s) or re.search(r'd="([^"]+)"[^>]*id="st-sinaloa"', s)
    d = m.group(1)
    ds = []
    for sub in d.split("M")[1:]:
        pts = [tuple(map(float, q.split(","))) for q in sub.rstrip("Z").split("L") if q]
        if len(pts) > 40: ds.append(ring_d(pts, 5.0))
    json.dump({"sinaloa": "".join(ds)}, open(f"{OUT}/sinaloa_close.json", "w"))
    print("close", len("".join(ds)))


def aerial(name, z, lon0, lat0, lon1, lat1, cache=f"{ROOT}/work/cts01/tiles"):
    """Esri World Imagery mosaic (web mercator) — same recipe as the kit aerials; tiles fetched with
    MK_CACHE=work/cts01/tiles tools/map_tiles.py fetch esri z lon0 lat0 lon1 lat1."""
    import math, json
    tx = lambda lon: (lon + 180) / 360 * 2 ** z
    ty = lambda lat: (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * 2 ** z
    x0, x1 = int(tx(lon0)), int(tx(lon1)); y0, y1 = int(ty(lat1)), int(ty(lat0))
    im = Image.new("RGB", ((x1 - x0 + 1) * 256, (y1 - y0 + 1) * 256))
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            im.paste(Image.open(f"{cache}/esri/{z}_{x}_{y}.jpg").convert("RGB"), ((x - x0) * 256, (y - y0) * 256))
    im.save(f"{OUT}/{name}.jpg", quality=90)
    j = {"name": name, "image": f"{name}.jpg", "width": im.width, "height": im.height, "zoom": z,
         "tile_bounds": {"x0": x0, "x1": x1, "y0": y0, "y1": y1},
         "source": "Esri World Imagery tiles, stitched unmodified", "credit": "Imagery: Esri, Maxar, Earthstar Geographics"}
    json.dump(j, open(f"{OUT}/{name}.json", "w"), indent=1)
    print(name, im.size)

def aerials():
    aerial("aerial_kuroda_z18", 18, -108.4830, 25.5760, -108.4690, 25.5870)
    aerial("aerial_guasave_z16", 16, -108.5050, 25.5450, -108.4350, 25.6000)
