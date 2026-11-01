"""ivs06 derived assets: padded Eastern-Europe night map (Warsaw→Ukraine), police photo crop, Lada X-ray plates."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops
Image.MAX_IMAGE_PIXELS = None
R = "/home/user/vox-edit-kit/"
D = R + "assets/ivan/ivs06/derived/"

def padded_map():
    kit = Image.open(R + "assets/maps/kit/eastern_europe_night.jpg").convert("RGB")
    X0, X1, Y0, Y1 = -886, 3251, 1560, 3840          # kit pixel space (x=(lon-20)*147.768, y=(62-lat)*240)
    W, H = X1 - X0, Y1 - Y0
    out = Image.new("RGB", (W, H))
    # left pad from the world night relief (45.511 px/deg, unsquashed)
    w = Image.open(R + "assets/maps/kit/world_night.jpg").convert("RGB")
    k = 45.511
    lon0, lon1 = 20 + X0 / 147.768, 20 + 80 / 147.768
    lat0, lat1 = 62 - Y0 / 240, 62 - Y1 / 240
    box = (int((lon0 + 180) * k), int((90 - lat0) * k), int((lon1 + 180) * k) + 1, int((90 - lat1) * k) + 1)
    pad = w.crop(box).resize((80 - X0, H), Image.LANCZOS)
    out.paste(pad, (0, 0))
    kc = kit.crop((0, Y0, X1, Y1))
    # feather the seam over 80 px
    m = Image.new("L", kc.size, 255)
    dr = ImageDraw.Draw(m)
    for i in range(80):
        dr.line([(i, 0), (i, H)], fill=int(255 * i / 80))
    out.paste(kc, (-X0, 0), m)
    out.save(D + "ee_night_warsaw_pad.jpg", quality=90)
    print("map", out.size, "offset x", X0, "y", Y0)

def police():
    im = Image.open(R + "assets/ivan/ivs06/photos/dps_post_officer_car.jpg").convert("RGB")
    c = im.crop((0, 470, 1920, 1550 - 470 + 470)) if False else im.crop((0, 440, 1920, 1520))
    c.save(D + "dps_officer_car_crop.jpg", quality=90); print("police", c.size)

def lada():
    im = Image.open(R + "assets/ivan/ivs06/photos/lada_granta_side.jpg").convert("RGB")   # 1920x744
    poly = [(32, 560), (28, 470), (40, 380), (45, 300), (62, 255), (110, 228), (280, 205), (330, 180), (480, 85), (560, 62),
            (700, 52), (860, 50), (1000, 58), (1110, 76), (1200, 120), (1360, 222), (1520, 262), (1700, 300), (1800, 330),
            (1860, 380), (1895, 450), (1890, 540), (1860, 575), (1720, 590), (1705, 640), (1660, 700), (1560, 718),
            (1460, 700), (1410, 640), (1400, 605), (600, 610), (570, 670), (500, 715), (400, 722), (320, 690), (290, 620),
            (280, 590), (120, 585)]
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).polygon(poly, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(2))
    car = im.copy(); car.putalpha(m)
    car.save(D + "lada_cut.png"); print("lada cut")
    # X-ray plate: grey, inverted, edge-enhanced
    g = ImageOps.grayscale(im)
    inv = ImageOps.invert(g)
    edges = g.filter(ImageFilter.FIND_EDGES).point(lambda v: min(255, v * 3))
    xr = ImageChops.add(ImageOps.autocontrast(inv, cutoff=2).point(lambda v: int(v * 0.55)), edges)
    xr = Image.merge("RGBA", (xr, xr, xr, m))
    xr.save(D + "lada_xray.png"); print("xray")


def borders():
    """Simplified country outlines in the padded-map pixel space (x+886, y-1560) → derived/ee_pad_borders.json"""
    import re, json
    s = open(R + "assets/maps/kit/eastern_europe_overlay.svg").read()
    out = {}
    for cid in ["c-russia", "c-ukraine", "c-crimea", "c-poland", "c-belarus", "c-moldova", "c-lithuania", "c-romania", "c-slovakia", "c-hungary"]:
        d = re.search(r'<path id="%s"[^>]*\sd="([^"]*)"' % cid, s).group(1)
        subs = []
        for sp in d.split("M")[1:]:
            pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sp)]
            pts = [(x + 886, y - 1560) for x, y in pts]
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            if max(xs) < -50 or min(xs) > 4187 or max(ys) < -50 or min(ys) > 2330: continue
            if max(xs) - min(xs) < 25 and max(ys) - min(ys) < 25: continue
            pts = [(min(4300, max(-150, x)), min(2450, max(-150, y))) for x, y in pts]   # clamp = clip to a box around the canvas
            keep = [pts[0]]
            for p in pts[1:]:
                if (p[0] - keep[-1][0]) ** 2 + (p[1] - keep[-1][1]) ** 2 >= 36: keep.append(p)
            if not keep or len(keep) < 4: continue
            subs.append("M" + "L".join("%d,%d" % (round(x), round(y)) for x, y in keep) + "Z")
        out[cid] = "".join(subs)
        print(cid, len(out[cid]))
    json.dump(out, open(D + "ee_pad_borders.json", "w"))

for f in sys.argv[1:] or ["padded_map", "lada", "borders"]:
    globals()[f]()
