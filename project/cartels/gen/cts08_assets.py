"""cts08 derived assets (US vs Cartels): Caribbean/Pacific night map crop + country overlays, Caracas Esri inset,
country silhouettes for the balance-scale medallions.   Run: .venv/bin/python project/cartels/gen/cts08_assets.py
Map crop: americas_night (kit, 45.5111 px/deg, = world_overlay.svg pixel space) lon -125..-55, lat 50..0.
In the crop: x = (lon + 125) * 45.5111 ; y = (50 - lat) * 45.5111."""
import os, re, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = f"{ROOT}/assets/cartels/cts08/derived"; os.makedirs(OUT, exist_ok=True)
K = 45.5111
LON0, LAT1, LON1, LAT0 = -125, 50, -55, 0
WX0, WY0 = (LON0 + 180) * K, (90 - LAT1) * K          # world px of the crop corner
AX0, AY0 = WX0 - 2276, WY0 - 1593                      # americas_night px
W, H = round((LON1 - LON0) * K), round((LAT1 - LAT0) * K)

def crop_map():
    im = Image.open(f"{ROOT}/assets/maps/kit/americas_night.jpg")
    c = im.crop((round(AX0), round(AY0), round(AX0) + W, round(AY0) + H))
    c.save(f"{OUT}/carib_night.jpg", quality=90); print("map", c.size)

def country_polys(names):
    s = open(f"{ROOT}/assets/maps/kit/world_overlay.svg").read()
    out = {}
    for n in names:
        m = re.search(r'<path id="c-%s"[^>]* d="([^"]+)"' % n, s)
        polys = []
        for sub in m.group(1).split("M")[1:]:
            pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sub)]
            if len(pts) < 3: continue
            if max(abs(pts[i][0] - pts[i - 1][0]) for i in range(1, len(pts))) > 4000: continue
            polys.append([(x - WX0, y - WY0) for x, y in pts])
        out[n] = polys
    return out

def overlays():
    names = ["united_states_of_america", "mexico", "venezuela", "colombia", "cuba", "guatemala", "honduras", "nicaragua",
             "el_salvador", "costa_rica", "panama", "belize", "haiti", "dominican_rep", "ecuador", "canada", "jamaica",
             "puerto_rico", "bahamas", "guyana", "brazil", "peru", "trinidad_and_tobago", "suriname"]
    P = country_polys(names)
    S = 2  # supersample
    # all borders: bone hairlines
    b = Image.new("L", (W * S, H * S), 0); d = ImageDraw.Draw(b)
    for n, ps in P.items():
        for p in ps: d.line([(x * S, y * S) for x, y in p] + [(p[0][0] * S, p[0][1] * S)], fill=255, width=3 * S)
    b = b.resize((W, H), Image.LANCZOS)
    rgba = Image.new("RGBA", (W, H), (243, 237, 225, 0)); rgba.putalpha(b.point(lambda v: int(v * 0.42)))
    rgba.save(f"{OUT}/carib_borders.png"); print("borders")
    def fill(name, rgb, a, stroke_rgb, fname, sa=0.9):
        m = Image.new("L", (W * S, H * S), 0); dd = ImageDraw.Draw(m)
        for p in P[name]: dd.polygon([(x * S, y * S) for x, y in p], fill=255)
        m = m.resize((W, H), Image.LANCZOS)
        e = Image.new("L", (W * S, H * S), 0); de = ImageDraw.Draw(e)
        for p in P[name]: de.line([(x * S, y * S) for x, y in p] + [(p[0][0] * S, p[0][1] * S)], fill=255, width=5 * S)
        e = e.resize((W, H), Image.LANCZOS)
        fa = np.asarray(m, np.float32) / 255 * a; ea = np.asarray(e, np.float32) / 255 * sa
        rgbF = np.array(rgb, np.float32); rgbE = np.array(stroke_rgb, np.float32)
        A = ea + fa * (1 - ea)
        C = (rgbE[None, None] * ea[..., None] + rgbF[None, None] * (fa * (1 - ea))[..., None]) / np.maximum(A, 1e-4)[..., None]
        img = np.dstack([C, A * 255]).clip(0, 255).astype(np.uint8)
        Image.fromarray(img, "RGBA").save(f"{OUT}/{fname}"); print(fname)
    fill("venezuela", (200, 193, 182), 0.30, (243, 237, 225), "carib_venezuela.png")
    fill("united_states_of_america", (111, 147, 180), 0.42, (188, 209, 228), "carib_usa.png")
    fill("mexico", (154, 154, 78), 0.40, (211, 211, 156), "carib_mexico.png")
    # white+alpha silhouettes for the medallions (cropped to bbox, 900 px wide)
    for n, fn in (("mexico", "sil_mexico.png"), ("united_states_of_america", "sil_usa.png")):
        ps = [p for p in P[n] if (max(x for x, _ in p) - min(x for x, _ in p)) > 30]
        if n == "united_states_of_america":   # lower 48 only (drop Alaska/Hawaii: west of lon -125 already cropped)
            ps = [p for p in ps if min(x for x, _ in p) > -10 and max(x for x, _ in p) < 3200 and min(y for _, y in p) > 0]
        xs = [x for p in ps for x, _ in p]; ys = [y for p in ps for _, y in p]
        x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys); sc = 900 / (x1 - x0)
        m = Image.new("L", (900 * S, round((y1 - y0) * sc) * S + 2), 0); dd = ImageDraw.Draw(m)
        for p in ps: dd.polygon([((x - x0) * sc * S, (y - y0) * sc * S) for x, y in p], fill=255)
        m = m.resize((900, round((y1 - y0) * sc)), Image.LANCZOS)
        img = Image.new("RGBA", m.size, (255, 255, 255, 0)); img.putalpha(m); img.save(f"{OUT}/{fn}"); print(fn, img.size)

def caracas():
    sys.path.insert(0, f"{ROOT}/tools"); import map_tiles as mt
    z, lon0, lat0, lon1, lat1 = 12, -67.16, 10.36, -66.70, 10.62
    os.environ["MK_CACHE"] = mt.CACHE
    mt.fetch("esri", z, lon0, lat0, lon1, lat1)
    ts = mt.tiles(z, lon0, lat0, lon1, lat1)
    xs = sorted({x for x, _ in ts}); ys = sorted({y for _, y in ts})
    mos = Image.new("RGB", (256 * len(xs), 256 * len(ys)))
    for x, y in ts: mos.paste(Image.open(mt.path("esri", z, x, y)), ((x - xs[0]) * 256, (y - ys[0]) * 256))
    px = lambda lon: (mt.tx(lon, z) - xs[0]) * 256; py = lambda lat: (mt.ty(lat, z) - ys[0]) * 256
    c = mos.crop((round(px(lon0)), round(py(lat1)), round(px(lon1)), round(py(lat0))))
    c.save(f"{OUT}/caracas_esri_z12.jpg", quality=90)
    # pin position of Caracas centre (Plaza Bolívar) inside the crop
    print("caracas", c.size, "pin", px(-66.9146) - px(lon0), py(10.50609) - py(lat1))

if __name__ == "__main__":
    what = sys.argv[1:] or ["map", "overlays", "caracas"]
    if "map" in what: crop_map()
    if "overlays" in what: overlays()
    if "caracas" in what: caracas()
