"""nvs22 derived assets: Southeast Asia map overlays (Malaysia / China fills, borders) + Johor aerial grade.
Run from repo root: python3 project/nvidia/gen/nvs22_assets.py"""
import re
from PIL import Image, ImageEnhance
OUT = "assets/nvidia/nvs22/derived/"
s = open("assets/maps/kit/southeast_asia_overlay.svg").read()
def path(cid):
    return re.search(r'<path[^>]*id="%s"[^>]*\sd="([^"]+)"' % cid, s).group(1)
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5428 7030" width="5428" height="7030">'
def write(name, body):
    open(OUT + name, "w").write(HEAD + body + "</svg>")
write("sea_malaysia_fill.svg", '<path d="%s" fill="#f0efe8" fill-opacity="0.34" stroke="#f0efe8" stroke-width="7" stroke-linejoin="round"/>' % path("c-malaysia"))
write("sea_china_fill.svg", '<path d="%s" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="7" stroke-linejoin="round"/>' % path("c-china"))
cs = re.search(r'<g id="countries">(.*?)</g>', s, re.S).group(1)
cs = re.sub(r'id="[^"]*"|data-name="[^"]*"', "", cs)
write("sea_borders.svg", '<g fill="none" stroke="#f0efe8" stroke-opacity="0.45" stroke-width="3" stroke-linejoin="round">%s</g>' % cs)
# Johor aerial: slightly desaturated copy for the cards backdrop (blur done in CSS)
im = Image.open("assets/maps/kit/aerial_johor_data_centers_z16.jpg").convert("RGB")
ImageEnhance.Color(im).enhance(0.55).save(OUT + "johor_aerial_desat.jpg", quality=88)
# crop of the twin data halls for the polaroid (pin 1680,1533)
im.crop((1680 - 420, 1533 - 330, 1680 + 420, 1533 + 330)).save(OUT + "johor_halls_crop.jpg", quality=90)
print("ok")
