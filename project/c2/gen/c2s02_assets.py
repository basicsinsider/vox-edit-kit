"""Derived assets for compositions/c2s02.html (run from the project root with .venv/bin/python).
Downscaled/cropped map pieces (keeps decode memory low), keyed TV screen, medal and logo crops, footage stills."""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
OUT = "assets/c2/derived/c2s02"; os.makedirs(OUT, exist_ok=True)
info = {}

def save(im, name, q=88):
    p = f"{OUT}/{name}"
    if name.endswith(".png"): im.save(p, optimize=True)
    else: im.convert("RGB").save(p, quality=q)
    info[name] = im.size; print(name, im.size)

# US night (map kit) 6392x3524 -> 3200 wide (53.27 px/deg lon, 66.58 px/deg lat)
us = Image.open("assets/maps/kit/us_night.jpg"); k = 3200 / us.width
save(us.resize((3200, round(us.height * k)), Image.LANCZOS), "us_night_3200.jpg")
ua = Image.open("assets/maps/kit/us_atlas.jpg")
save(ua.resize((3200, round(ua.height * k)), Image.LANCZOS), "us_atlas_3200.jpg")
info["us_k"] = k

# Bay Area satdesat crop (native) around Palo Alto / Mountain View
ba = Image.open("assets/maps/kit/bay_area_satdesat.jpg")
save(ba.crop((2400, 3200, 5000, 5400)), "bay_satdesat_pa.jpg"); info["bay_satdesat_pa_off"] = (2400, 3200)
bt = Image.open("assets/maps/kit/bay_area_atlas.jpg")
save(bt.crop((1700, 2000, 4500, 4800)).resize((2100, 2100), Image.LANCZOS), "bay_atlas_sf_stanford.jpg")
info["bay_atlas_off"] = (1700, 2000, 0.75)

# Stanford aerial z17 -> 0.75
ae = Image.open("assets/maps/kit/aerial_stanford_z17.jpg")
save(ae.resize((3264, 2880), Image.LANCZOS), "aerial_stanford_075.jpg")

# USGS quads: 1948 15' (Palo Alto + Mountain View, native crop) and 1953 7.5' (Stanford lands, 0.5)
q48 = Image.open("assets/c2/maps/usgs_palo_alto_1948_62k.jpg")
save(q48.crop((380, 900, 3300, 3100)), "usgs1948_pa_mv.jpg"); info["usgs1948_off"] = (380, 900)
q53 = Image.open("assets/c2/maps/usgs_palo_alto_1953_24k.jpg")
save(q53.crop((600, 2700, 5900, 6800)).resize((2650, 2050), Image.LANCZOS), "usgs1953_stanford_lands.jpg"); info["usgs1953_off"] = (600, 2700, 0.5)

# 1950s RCA Victor console TV, screen keyed transparent (rounded tube, hand-measured), 0.625 scale
tv = Image.open("assets/c2/objects/rca_victor_tv_1950s_ohio.jpg").convert("RGBA")
m = Image.new("L", tv.size, 255); d = ImageDraw.Draw(m)
d.rounded_rectangle((1705, 742, 2368, 1326), radius=150, fill=0)
m = m.filter(ImageFilter.GaussianBlur(2))
tv.putalpha(m); s = 0.625
save(tv.resize((round(tv.width * s), round(tv.height * s)), Image.LANCZOS), "tv_rca_1950s_keyed.png")
scr = {"x": 1705 * s, "y": 742 * s, "w": (2368 - 1705) * s, "h": (1326 - 742) * s, "radius": 150 * s, "image": "tv_rca_1950s_keyed.png", "size": [2400, 1600]}
json.dump(scr, open(f"{OUT}/tv_rca_1950s_keyed_screen.json", "w"), indent=1)

# Nobel medal (Fleming's 1945 medal, NMS) -> circular cut-out
md = Image.open("_tmp/c2s02/nobel_medal.jpg").convert("RGBA")
cx, cy, r = 984, 577, 418
c = md.crop((cx - r, cy - r, cx + r, cy + r)); mm = Image.new("L", c.size, 0)
ImageDraw.Draw(mm).ellipse((4, 4, 2 * r - 4, 2 * r - 4), fill=255); c.putalpha(mm.filter(ImageFilter.GaussianBlur(1.5)))
os.makedirs("assets/c2/objects", exist_ok=True)
md.convert("RGB").save("assets/c2/objects/nobel_medal_fleming_1945.jpg", quality=90)
save(c, "nobel_medal_cut.png")

# HP 1958 annual-report cover: the period 'hp' logo tile
hp = Image.open("assets/c2/documents/hp_annual_report_1958_cover_hp_logo.jpg")
save(hp.crop((300, 0, 2100, 2200)).resize((720, 880), Image.LANCZOS), "hp_logo_tile_1958.jpg")

# footage stills
for src, t, name in [("assets/c2/footage/bell_transistor1953_engineers_at_benches.mp4", 6.0, "engineers_still.jpg")]:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", f"{OUT}/{name}"], check=True)
json.dump(info, open(f"{OUT}/_info.json", "w"), indent=1)
