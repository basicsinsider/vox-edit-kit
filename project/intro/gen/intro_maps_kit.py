"""Intro map pass (Krish round 3, MANUAL §10.9 "Map quality"): re-project the map kit (assets/maps/kit) into the
EXACT pixel spaces the intro compositions already use, so every route / fill / pin / overlay path keeps working and
only the <img src> changes. Output: assets/intro/derived/maps/.  Run one step at a time (the world rasters are big):
  .venv/bin/python project/intro/gen/intro_maps_kit.py pacific | world | taiwan | hsinchu | all
Spaces (old asset -> formula):
  pacific  5700x1440  x=(lon-110)*30, y=(56-lat)*30      (IS006 base; IS028 uses the same geography at 15 px/deg)
  world    3840x1920 / 4320x2160  x=(lon+180)*k, y=(90-lat)*k  (IS016 k=10.667; IS048/049/055 k=12)
  taiwan   2480x3040  x=(lon-119.2)*800, y=(25.5-lat)*800  (IS035, IS045, IS050, IS053)
  hsinchu  3728x2823  Web Mercator z15, x = X15 - 7011944.22, y = Y15 - 3596456.58  (IS053 satellite)"""
import sys, pathlib, gc
from PIL import Image, ImageFilter, ImageChops, ImageStat
Image.MAX_IMAGE_PIXELS = None
R = pathlib.Path(__file__).resolve().parents[3]
K = R / "assets/maps/kit"; O = R / "assets/intro/derived/maps"; O.mkdir(parents=True, exist_ok=True)
WK = 16384 / 360.0   # world kit px/deg (45.5111)


def world_crop(name, lon0, lon1, lat0, lat1):
    """Native-resolution crop of a kit world raster; lon1 may exceed 180 (wraps across the antimeridian)."""
    im = Image.open(K / name).convert("RGB")
    y0, y1 = round((90 - lat1) * WK), round((90 - lat0) * WK)
    if lon1 <= 180:
        out = im.crop((round((lon0 + 180) * WK), y0, round((lon1 + 180) * WK), y1))
    else:
        a = im.crop((round((lon0 + 180) * WK), y0, 16384, y1)); b = im.crop((0, y0, round((lon1 - 180) * WK), y1))
        out = Image.new("RGB", (a.width + b.width, y1 - y0)); out.paste(a, (0, 0)); out.paste(b, (a.width, 0))
    del im; gc.collect(); return out


def pacific():
    # 110E -> 60W (=300), 56N -> 8N at 45 px/deg = 1.5x the old 5700x1440 space (IS006 + IS028)
    c = world_crop("world_atlas.jpg", 110, 300, 8, 56)
    c.resize((8550, 2160), Image.LANCZOS).save(O / "pacific_atlas_8550.jpg", quality=90); del c; gc.collect()
    # Taiwan-strait inset for IS006's opening close-up (zoom 6-7): east_asia_atlas native, 116-127E, 19-29N
    ea = Image.open(K / "east_asia_atlas.jpg").convert("RGB")
    box = (round((116 - 100) * 127.95), round((48 - 29) * 150), round((127 - 100) * 127.95), round((48 - 19) * 150))
    ins = ea.crop(box); ins.save(O / "pacific_inset_taiwan_116_127E_19_29N.jpg", quality=90)
    print("pacific ok", ins.size)


def world():
    w = Image.open(K / "world_night.jpg").convert("RGB")
    w.resize((7680, 3840), Image.LANCZOS).save(O / "world_night_7680.jpg", quality=88)
    w.resize((4320, 2160), Image.LANCZOS).save(O / "world_night_4320.jpg", quality=88)
    w.crop((round((110 + 180) * WK), round((90 - 34) * WK), round((134 + 180) * WK), round((90 - 10) * WK))).save(
        O / "world_night_inset_110_134E_10_34N.jpg", quality=90)
    del w; gc.collect()
    a = Image.open(K / "world_atlas.jpg").convert("RGB")
    a.resize((6480, 3240), Image.LANCZOS).save(O / "world_atlas_6480.jpg", quality=88)
    print("world ok")


def taiwan():
    # old space u,v -> kit taiwan px: X=(u/800-0.1)*1119.352, Y=(v/800-0.1)*1222  (bounds 0.1 deg tighter: fill with kit sea)
    for v in ("atlas", "night", "sat"):
        im = Image.open(K / f"taiwan_{v}.jpg").convert("RGB")
        sea = im.getpixel((8, im.height - 8))
        out = im.transform((2480, 3040), Image.AFFINE, (1119.352 / 800, 0, -111.9352, 0, 1222 / 800, -122.2),
                           resample=Image.BICUBIC, fillcolor=sea)
        out.save(O / f"taiwan_{v}_2480.jpg", quality=90); print("taiwan", v, sea)


def hsinchu():
    # s2 space (3728x2823, z15) at 1.25x; base = Sentinel-2 (graded toward the Esri colours), core = Esri z17 aerial
    S = 1.25; W, H = round(3728 * S), round(2823 * S)
    base = Image.open(R / "assets/intro/maps/hsinchu_s2cloudless2016.jpg").convert("RGB").resize((W, H), Image.LANCZOS)
    ae = Image.open(K / "aerial_hsinchu_park_z17.jpg").convert("RGB")
    # x17 = 4*(u/S + 7011944.22) - 109587*256 ; y17 = 4*(v/S + 3596456.58) - 56214*256
    cx, cy = 4 * 7011944.22 - 109587 * 256, 4 * 3596456.58 - 56214 * 256
    data = (4 / S, 0, cx, 0, 4 / S, cy)
    warped = ae.transform((W, H), Image.AFFINE, data, resample=Image.BICUBIC)
    m = Image.new("L", ae.size, 0); m.paste(255, (60, 60, ae.width - 60, ae.height - 60)); m = m.filter(ImageFilter.GaussianBlur(50))
    mask = m.transform((W, H), Image.AFFINE, data, resample=Image.BILINEAR)
    # match the Sentinel base to the Esri core (mean/std per channel inside the overlap)
    hard = mask.point(lambda p: 255 if p > 250 else 0)
    sb, sa = ImageStat.Stat(base, hard), ImageStat.Stat(warped, hard)
    bands = []
    for i, ch in enumerate(base.split()):
        g = sa.stddev[i] / max(sb.stddev[i], 1); o = sa.mean[i] - sb.mean[i] * g
        bands.append(ch.point(lambda p, g=g, o=o: max(0, min(255, round(p * g + o)))))
    base = Image.merge("RGB", bands)
    out = Image.composite(warped, base, mask)
    out.save(O / "hsinchu_s2_esri_z17_4660.jpg", quality=90); print("hsinchu ok", out.size)


steps = {"pacific": pacific, "world": world, "taiwan": taiwan, "hsinchu": hsinchu}
for a in (sys.argv[1:] or ["all"]):
    for k, f in steps.items():
        if a in (k, "all"): f()
