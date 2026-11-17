#!/usr/bin/env python3
"""nvs19 derived assets (run from repo root with .venv/bin/python).
us_west_night_2560.jpg  = assets/maps/kit/us_night.jpg cropped x 0..4300, y 798..3324 (lon -126..-85.6, lat 44..25.0), scaled k=2560/4300
us_states_2560.svg      = kit us_overlay.svg state + country outlines in the same pixel space (stroke only)
us_texas_2560.svg / us_california_2560.svg = solid fills (CSS mask-image)
"""
import re, json
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"
OUT = "assets/nvidia/nvs19/derived/"
X0, Y0, X1, Y1 = 0, 798, 4300, 3324
k = 2560 / (X1 - X0)
W, H = 2560, round((Y1 - Y0) * k)

im = Image.open(K + "us_night.jpg").crop((X0, Y0, X1, Y1)).resize((W, H), Image.LANCZOS)
im.save(OUT + "us_west_night_2560.jpg", quality=88)

svg = open(K + "us_overlay.svg").read()
def tf(d):
    def rep(m):
        x, y = float(m.group(1)), float(m.group(2))
        return "%.1f,%.1f" % ((x - X0) * k, (y - Y0) * k)
    return re.sub(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", rep, d)
def path(id_):
    m = re.search(r'<path[^>]*id="' + id_ + r'"[^>]*d="([^"]+)"', svg)
    return tf(m.group(1))
states = re.findall(r'<path id="(st-[a-z_]+)"[^>]*d="([^"]+)"', svg)
usa = path("c-united_states_of_america")
mex = path("c-mexico")
lines = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (W, H, W, H)]
lines.append('<g fill="none" stroke="#f0efe8" stroke-opacity="0.35" stroke-width="1.6" stroke-linejoin="round">')
for sid, d in states:
    lines.append('<path d="%s"/>' % tf(d))
lines.append('</g><g fill="none" stroke="#f0efe8" stroke-opacity="0.6" stroke-width="2.4" stroke-linejoin="round"><path d="%s"/><path d="%s"/></g></svg>' % (usa, mex))
open(OUT + "us_states_2560.svg", "w").write("\n".join(lines))
for name in ["texas", "california"]:
    d = path("st-" + name)
    open(OUT + "us_%s_2560.svg" % name, "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d"><path fill="#fff" d="%s"/></svg>' % (W, H, W, H, d))
json.dump({"w": W, "h": H, "k": k, "x0": X0, "y0": Y0, "texas": path("st-texas"), "california": path("st-california")},
          open(OUT + "us_west_paths_2560.json", "w"))
print("map", W, H, k)
print("dallas", (3111.1 - X0) * k, (2290.7 - Y0) * k, "san_jose", (438.2 - X0) * k, (1684.0 - Y0) * k)

