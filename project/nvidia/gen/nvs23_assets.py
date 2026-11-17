#!/usr/bin/env python3
"""nvs23 derived assets (run from the repo root: python3 project/nvidia/gen/nvs23_assets.py).
- country fills/strokes as standalone SVGs in the kit map pixel spaces (southeast_asia, china)
- the last face-cam frame (freeze under the designed ending fade)
Output: assets/nvidia/nvs23/derived/
"""
import re, subprocess, os

OUT = "assets/nvidia/nvs23/derived"
os.makedirs(OUT, exist_ok=True)
RED, REDL, BONE, ICEL = "#dc2f3c", "#f6a4a9", "#f0efe8", "#9fdcf0"


def path(svg, cid):
    m = re.search(r'<path id="c-%s"[^>]*d="([^"]*)"' % cid, svg)
    return m.group(1)


def write(name, w, h, body):
    open(os.path.join(OUT, name), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">%s</svg>' % (w, h, w, h, body))


# world-kit crops (one frame holds S China, Taiwan and Malaysia)
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
wsvg = open("assets/maps/kit/world_overlay.svg").read()
CROPS = {  # name: (base file, px per degree, lon0, lon1, lat1 (top), lat0 (bottom), world-px factor)
    "wn": ("assets/maps/kit/world_night.jpg", 16384 / 360, 85, 135, 36, -2, 1.0),
    "ws": ("assets/maps/kit/world_satdesat_21600.jpg", 60.0, 88, 132, 34, -3, 21600 / 16384),
}
for nm, (src, k, lo0, lo1, la1, la0, f) in CROPS.items():
    x0, y0 = (lo0 + 180) * k, (90 - la1) * k
    w, h = round((lo1 - lo0) * k), round((la1 - la0) * k)
    Image.open(src).crop((round(x0), round(y0), round(x0) + w, round(y0) + h)).convert("RGB").save(
        os.path.join(OUT, "%s_crop.jpg" % nm), quality=90)
    g = 'transform="translate(%.2f %.2f) scale(%.6f)"' % (-round(x0), -round(y0), f)
    write("%s_china_fill.svg" % nm, w, h, '<g %s><path d="%s" fill="%s" fill-opacity="0.5" fill-rule="evenodd"/></g>' % (g, path(wsvg, "china"), RED))
    write("%s_china_stroke.svg" % nm, w, h, '<g %s><path d="%s" fill="none" stroke="%s" stroke-width="%.2f" stroke-linejoin="round"/></g>' % (g, path(wsvg, "china"), REDL, 3.2 / f))
    write("%s_taiwan.svg" % nm, w, h, '<g %s><path d="%s" fill="%s" fill-opacity="0.16" stroke="%s" stroke-width="%.2f" stroke-linejoin="round"/></g>' % (g, path(wsvg, "taiwan"), BONE, BONE, 2.6 / f))
    write("%s_malaysia.svg" % nm, w, h, '<g %s><path d="%s" fill="%s" fill-opacity="0.12" stroke="%s" stroke-width="%.2f" stroke-linejoin="round"/></g>' % (g, path(wsvg, "malaysia"), BONE, BONE, 2.6 / f))
    print(nm, w, h, "x=(lon-%d)*%.4f ; y=(%d-lat)*%.4f" % (lo0, k, la1, k))

ch = open("assets/maps/kit/china_overlay.svg").read()
W2, H2 = 6383, 4368
cn2 = path(ch, "china")
write("cn_china_fill.svg", W2, H2, '<path d="%s" fill="%s" fill-opacity="0.45" fill-rule="evenodd"/>' % (cn2, RED))
# the "data wall": a thick red-light border + a dark outer glow band
write("cn_china_wall.svg", W2, H2,
      '<path d="%s" fill="none" stroke="%s" stroke-opacity="0.35" stroke-width="44" stroke-linejoin="round"/>'
      '<path d="%s" fill="none" stroke="%s" stroke-width="14" stroke-linejoin="round"/>' % (cn2, RED, cn2, REDL))

# last decodable face-cam frame (file ends 2400.600; 30 fps) for the end freeze
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "2400.52", "-i", "assets/facecam/nvidia_facecam_master.mp4",
                "-frames:v", "1", "-q:v", "2", os.path.join(OUT, "fc_last_2400_53.jpg")], check=True)
print("ok")
