"""pys07 derived images (duotones/grades). Run: .venv/bin/python project/paraguay/gen/pys07_assets.py"""
from PIL import Image, ImageOps, ImageEnhance
import os
S = "assets/paraguay/shared/photos/"; O = "assets/paraguay/pys07/derived/"
os.makedirs(O, exist_ok=True)
def hx(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def duo(src, dst, dark, light, contrast=1.1, bright=1.0, maxw=1920):
    im = Image.open(S + src).convert("L")
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(contrast); im = ImageEnhance.Brightness(im).enhance(bright)
    ImageOps.colorize(im, hx(dark), hx(light)).save(O + dst, quality=92)
duo("pena_sash_crop.jpg", "pena_sash_duo.jpg", "#1d1424", "#efe6dc", 1.08)
duo("pena_closeup.jpg", "pena_closeup_plum.jpg", "#140c19", "#e3cfe8", 1.12, 0.92)
duo("ueno_tower_aerial_reuters.jpg", "ueno_tower_teal.jpg", "#06201d", "#c9efe8", 1.1, 0.9)
duo("bcp_building_2.jpg", "bcp_building_mate.jpg", "#0e1311", "#e8e4d6", 1.15, 0.85, 1280)
print("ok")
# BCP HQ on the Asunción skyline (3840 px source) — native-resolution 1920x1080 crop around the building, mate grade
im = Image.open(S + "bcp_building.jpg").convert("RGB").crop((1300, 760, 3220, 1840))
g = ImageOps.grayscale(im); im = Image.blend(im, Image.merge("RGB", (g, g, g)), 0.6)
ImageEnhance.Contrast(im).enhance(1.08).save(O + "bcp_skyline_crop.jpg", quality=92)
