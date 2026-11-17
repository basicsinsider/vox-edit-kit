"""nvs22 derived assets: Malaysia / China fills + border lines in the southeast_asia kit pixel space (5428x7030),
desaturated Johor (Sedenak Tech Park) aerial. Run: .venv/bin/python project/nvidia/gen/nvs22_assets.py"""
import re, os
from PIL import Image, ImageEnhance
ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
OUT = os.path.join(ROOT, "assets/nvidia/nvs22/derived")
os.makedirs(OUT, exist_ok=True)
s = open(os.path.join(ROOT, "assets/maps/kit/southeast_asia_overlay.svg")).read()
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5428 7030" width="5428" height="7030">'
def d_of(cid):
    return re.search(r'<path[^>]*id="%s"[^>]*\bd="([^"]+)"' % cid, s).group(1)
def write(name, body):
    open(os.path.join(OUT, name), "w").write(HEAD + body + "</svg>")
# Malaysia: neutral bone fill + bright edge (reference ast_b15cdcc28a634241: one country lit, white border)
write("sea_malaysia_fill.svg", '<path d="%s" fill="#f0efe8" fill-opacity="0.30" stroke="#f0efe8" stroke-width="7" stroke-linejoin="round"/>' % d_of("c-malaysia"))
# China: red fill (night maps ~0.5) + red-light stroke (SEGMENTS §2)
write("sea_china_fill.svg", '<path d="%s" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="6" stroke-linejoin="round"/>' % (d_of("c-china") + d_of("c-hong_kong")))
# all country borders, thin bone
cg = re.search(r'<g id="countries">(.*?)</g>', s, re.S).group(1)
ds = re.findall(r'\bd="([^"]+)"', cg)
write("sea_borders.svg", '<g fill="none" stroke="#f0efe8" stroke-opacity="0.45" stroke-width="3" stroke-linejoin="round">' + "".join('<path d="%s"/>' % d for d in ds) + "</g>")
# Johor aerial, desaturated (graphite photo tint, SEGMENTS §2) + slight contrast
im = Image.open(os.path.join(ROOT, "assets/maps/kit/aerial_johor_data_centers_z16.jpg")).convert("RGB")
im = ImageEnhance.Color(im).enhance(0.18); im = ImageEnhance.Contrast(im).enhance(1.12)
im.save(os.path.join(OUT, "johor_aerial_desat.jpg"), quality=90)
print("ok")
