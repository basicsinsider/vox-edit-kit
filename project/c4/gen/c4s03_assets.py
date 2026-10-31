"""Derived assets for compositions/c4s03.html (C4S070–C4S104). Run: .venv/bin/python project/c4/gen/c4s03_assets.py
Inputs: map kit, c4 footage, _tmp/c4s03 downloads (moved into assets/c4/{maps,photos}). Outputs: assets/c4/derived/c4s03/."""
import os, re, json, shutil, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = os.path.dirname(os.path.abspath(__file__)) + "/../../.."
os.chdir(R)
D = "assets/c4/derived/c4s03"; os.makedirs(D, exist_ok=True)
K = "assets/maps/kit"

def mv(src, dst):
    if os.path.exists(src) and not os.path.exists(dst): shutil.copy(src, dst)

# raw downloads -> asset folders (logged in SOURCES.md)
mv("_tmp/c4s03/takao.jpg", "assets/c4/maps/takao_1945_ams_city_plan.jpg")
mv("_tmp/c4s03/kaohsiung_z16.jpg", "assets/c4/maps/kaohsiung_harbour_epz_esri_z16.jpg")
mv("_tmp/c4s03/lin.jpg", "assets/c4/photos/lin_family_taiwanese_gentry_london.jpg")
mv("_tmp/c4s03/shenzhen.jpg", "assets/c4/photos/shenzhen_skyline_from_shenzhen_bay.jpg")

# 1. world night 4096 (x=(lon+180)*11.3778, y=(90-lat)*11.3778)
if not os.path.exists(f"{D}/world_night_4096.jpg"):
    Image.open(f"{K}/world_night.jpg").resize((4096, 2048), Image.LANCZOS).save(f"{D}/world_night_4096.jpg", quality=90)

# 2. Taiwan celadon fill (white+alpha mask rule, MANUAL 4.2) for the taiwan_night plate, half size 1623x2200
tm = Image.open(f"{K}/taiwan_landmask.png").convert("L").resize((1623, 2200), Image.LANCZOS)
fill = Image.new("RGBA", tm.size, (159, 199, 178, 255)); fill.putalpha(tm.filter(ImageFilter.GaussianBlur(1.2)))
fill.save(f"{D}/taiwan_celadon_fill_half.png")
Image.open(f"{K}/taiwan_night.jpg").resize((1623, 2200), Image.LANCZOS).save(f"{D}/taiwan_night_half.jpg", quality=90)

# 3. Taiwan path from the east_asia overlay (for C4S095 fill)
svg = open(f"{K}/east_asia_overlay.svg").read()
m = re.search(r'<path id="c-taiwan"[^>]* d="([^"]+)"', svg)
json.dump({"taiwan_d": m.group(1) if m else ""}, open(f"{D}/east_asia_taiwan_path.json", "w"))

# 4. footage stills
def frame(clip, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", clip, "-frames:v", "1", "-q:v", "2", out])
F = "assets/c4/footage"
frame(f"{F}/taiwan_1960_campus_students_bicycles.mp4", 3.0, f"{D}/ntu_campus_1960_frame.jpg")
frame(f"{F}/taiwan_1960_officials_ribbon_ceremony.mp4", 5.2, f"{D}/officials_1960_frame.jpg")
frame(f"{F}/formosa_1961_chiang_kaishek_officials_steps.mp4", 1.2, f"{D}/officials_steps_1961_a.jpg")
frame(f"{F}/formosa_1961_chiang_kaishek_officials_steps.mp4", 4.0, f"{D}/officials_steps_1961_b.jpg")
frame(f"{F}/formosa_1961_chiang_kaishek_officials_steps.mp4", 7.5, f"{D}/officials_steps_1961_c.jpg")
frame(f"{F}/taiwan_1960_red_brick_hall_cyclists.mp4", 1.0, f"{D}/red_brick_hall_1960_frame.jpg")
frame(f"{F}/taiwan_1960_school_building.mp4", 8.0, f"{D}/school_building_1960_frame.jpg")
frame(f"{F}/taiwan_1960_students_writing_class.mp4", 6.0, f"{D}/students_writing_1960_frame.jpg")
print("ok")

# 5. C4S088 2.5D backdrop: the NARA photo at the cut-out's size (1/1.96) with the figure removed (normalised-blur inpaint)
if not os.path.exists(f"{D}/chiang_backdrop_nofigure.jpg"):
    cut = Image.open("assets/c4/cutouts/chiang_kaishek_uniform_cape_cutout.png")
    src = Image.open("assets/c4/photos/chiang_kaishek_uniform_cape_map_nara.jpg").convert("RGB").resize(cut.size, Image.LANCZOS)
    a = np.asarray(cut.split()[3].filter(ImageFilter.MaxFilter(31))).astype(float) / 255
    keep = (a < 0.05).astype(float)
    img = np.asarray(src).astype(float)
    from scipy.ndimage import gaussian_filter
    hole = keep < 0.5
    # diffusion fill on a 1/8 copy (Laplace inpaint), upscale, blur, paste into the hole only
    sm = (img.shape[1] // 8, img.shape[0] // 8)
    imS = np.asarray(Image.fromarray(img.astype(np.uint8)).resize(sm, Image.BILINEAR)).astype(float)
    hS = np.asarray(Image.fromarray((hole * 255).astype(np.uint8)).resize(sm, Image.NEAREST)) > 127
    f = imS.copy(); f[hS] = imS[~hS].mean(0)
    for _ in range(1500):
        avg = (np.roll(f, 1, 0) + np.roll(f, -1, 0) + np.roll(f, 1, 1) + np.roll(f, -1, 1)) / 4
        f[hS] = avg[hS]
    big = np.asarray(Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).resize(cut.size, Image.BICUBIC)).astype(float)
    big = np.stack([gaussian_filter(big[..., c], 6) for c in range(3)], -1)
    out = img.copy(); out[hole] = big[hole]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2)).save(f"{D}/chiang_backdrop_nofigure.jpg", quality=88)
