"""Derived assets for compositions/c5s01.html (run from repo root with .venv/bin/python).
Outputs -> assets/c5/derived/c5s01/ ."""
import re, subprocess, json
from PIL import Image, ImageDraw, ImageFilter, ImageChops
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"
O = "assets/c5/derived/c5s01/"
CEL = (159, 199, 178); RED = (224, 63, 44)

def dots(size, cell, amp=0.55):
    """halftone dot screen (L): 255 = paper, dots darker"""
    w, h = size
    im = Image.new("L", (w, h), 255); d = ImageDraw.Draw(im)
    r = cell * amp / 2
    for y in range(0, h + cell, cell):
        off = (cell // 2) if (y // cell) % 2 else 0
        for x in range(-cell, w + cell, cell):
            d.ellipse([x + off - r, y - r, x + off + r, y + r], fill=150)
    return im

# 1) Taiwan: night relief (half res) + celadon halftone fill from the landmask
s = 0.5
tw = Image.open(K + "taiwan_night.jpg").convert("RGB")
W, H = int(tw.width * s), int(tw.height * s)
tw.resize((W, H), Image.LANCZOS).save(O + "taiwan_night_half.jpg", quality=90)
Image.open(K + "taiwan_atlas.jpg").convert("RGB").resize((W, H), Image.LANCZOS).save(O + "taiwan_atlas_half.jpg", quality=90)
m = Image.open(K + "taiwan_landmask.png").convert("L").resize((W, H), Image.LANCZOS)
fill = Image.new("RGB", (W, H), CEL)
ht = dots((W, H), 9)
fill = ImageChops.multiply(fill, Image.merge("RGB", [ht.point(lambda v: 170 + v // 3)] * 3))
fill.putalpha(m.point(lambda v: int(v * 0.86)))
fill.save(O + "taiwan_celadon_fill.png")
edge = m.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(4))
g = Image.new("RGB", (W, H), CEL); g.putalpha(edge.point(lambda v: min(255, v * 3)))
g.save(O + "taiwan_celadon_glow.png")

# 2) East Asia night (half res) + China red halftone fill + Taiwan celadon fill (rasterised overlay paths)
ea = Image.open(K + "east_asia_night.jpg").convert("RGB")
s2 = 0.5
W2, H2 = int(ea.width * s2), int(ea.height * s2)
ea.resize((W2, H2), Image.LANCZOS).save(O + "east_asia_night_half.jpg", quality=90)
svg = open(K + "east_asia_overlay.svg").read()
lm = Image.open(K + "east_asia_landmask.png").convert("L").resize((W2, H2), Image.LANCZOS)
def raster(cid):
    d = re.search(r'<path id="%s"[^>]* d="([^"]+)"' % cid, svg).group(1)
    im = Image.new("L", (W2, H2), 0); dr = ImageDraw.Draw(im)
    for sub in d.split("M")[1:]:
        pts = [tuple(float(v) * s2 for v in p.split(",")) for p in re.split(r"[LZ]", sub) if "," in p]
        if len(pts) < 3 or any(p[0] < -50 for p in pts): continue
        dr.polygon(pts, fill=255)
    return ImageChops.multiply(im, lm.point(lambda v: 255 if v > 40 else 0)).filter(ImageFilter.GaussianBlur(1.2))
for cid, col, name in [("c-china", RED, "china_red_fill"), ("c-taiwan", CEL, "taiwan_cel_fill_ea")]:
    a = raster(cid)
    f = Image.new("RGB", (W2, H2), col)
    f = ImageChops.multiply(f, Image.merge("RGB", [dots((W2, H2), 8).point(lambda v: 175 + v // 3)] * 3))
    f.putalpha(a.point(lambda v: int(v * 0.8)))
    f.save(O + name + ".png")
    e = a.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(5))
    gg = Image.new("RGB", (W2, H2), col); gg.putalpha(e.point(lambda v: min(255, v * 3)))
    gg.save(O + name.replace("fill", "glow") + ".png")

# 3) Tiananmen 2.5D layers (modern CC BY-SA photo): far plate, gate with sky keyed, near ground strip
ti = Image.open("assets/c5/photos/tiananmen_mao_portrait_gatetower_modern.jpg").convert("RGB").resize((2400, 1800), Image.LANCZOS)
ti.save(O + "tian_far.jpg", quality=88)
hsv = ti.convert("HSV"); L = ti.convert("L")
sky = Image.eval(L, lambda v: 255 if v > 168 else 0)
sat = hsv.split()[1].point(lambda v: 255 if v < 60 else 0)
sky = ImageChops.multiply(sky, sat)
# only the top region counts as sky (flood from the top rows)
top = Image.new("L", ti.size, 0); ImageDraw.Draw(top).rectangle([0, 0, 2400, 520], fill=255)
sky = ImageChops.multiply(sky, top).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2))
gate = ti.copy(); gate.putalpha(ImageChops.invert(sky)); gate.save(O + "tian_gate.png")
near = ti.copy(); na = Image.new("L", ti.size, 0); dn = ImageDraw.Draw(na)
for y in range(1800):
    v = 0 if y < 1330 else min(255, int((y - 1330) / 140 * 255))
    dn.line([(0, y), (2400, y)], fill=v)
near.putalpha(na); near.save(O + "tian_near.png")

# 4) stills from footage
def still(src, t, out):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", out], check=True)
still("assets/intro/footage/taiwan_1960_presidential_office_taipei.mp4", 2.0, O + "presidential_office_1960_still.jpg")
still("assets/intro/footage/fab_hk_workers_microscope_rows_a.mp4", 4.0, O + "fab_rows_still.jpg")
# 5) halftone factory base for the growth bars (Nanzih EPZ factory, sky keyed)
subprocess.run([".venv/bin/python", "tools/halftone.py", "--sky-key", "--transparent-paper", "--cell", "7",
                "assets/intro/photos/nanzih_epz_ose_factory.jpg", O + "nanzih_factory_halftone.png"], check=True)
print("ok")
