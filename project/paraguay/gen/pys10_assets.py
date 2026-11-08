# pys10 derived photos (run from the repo root with .venv/bin/python). Footage trim:
# ffmpeg -ss 0 -t 6 -i assets/paraguay/shared/footage/uh_carvallo_arrives_fiscalia.mp4 -an -vf fps=24 -c:v libx264 -crf 18 -pix_fmt yuv420p assets/paraguay/pys10/derived/carvallo_fiscalia.mp4
import sys
from PIL import Image, ImageOps, ImageEnhance
S='assets/paraguay/shared/photos/'; D='assets/paraguay/pys10/derived/'
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def duo(src, out, dark, light, w=None, contrast=1.1, crop=None):
    im=Image.open(S+src).convert('RGB')
    if crop: im=im.crop(crop)
    if w and im.width>w: im=im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    g=ImageEnhance.Contrast(ImageOps.grayscale(im)).enhance(contrast)
    ImageOps.colorize(g, hexc(dark), hexc(light)).save(D+out, quality=90)
def mate(src, out, w=None, sat=0.25, bright=0.85, crop=None):
    im=Image.open(S+src).convert('RGB')
    if crop: im=im.crop(crop)
    if w and im.width>w: im=im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    im=ImageEnhance.Color(im).enhance(sat); im=ImageEnhance.Brightness(im).enhance(bright)
    im.save(D+out, quality=90)
mate('bcp_logo_glass_efe.jpg','bcp_glass_mate.jpg', sat=0.3, bright=0.8)
duo('bcp_building_2.jpg','bcp_plum.jpg','#1c0f24','#e8dcef')
duo('ueno_sign_hq_reuters.jpg','ueno_teal.jpg','#06231f','#dff4ef')
mate('police_guard_ueno_hq_afp.jpg','police_ueno_mate.jpg', sat=0.35, bright=0.9)
duo('carvallo_2025.jpg','carvallo_duo.jpg','#14110f','#efe9dc', contrast=1.05)
