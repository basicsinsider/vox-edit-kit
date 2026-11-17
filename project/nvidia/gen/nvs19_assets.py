"""nvs19 derived assets: China night map at 2560 px + China mask/outline, TSMC Fab 14B 2560 px.
Run: .venv/bin/python project/nvidia/gen/nvs19_assets.py"""
import re, json
from PIL import Image
R = "assets/nvidia/nvs19/derived/"
K = 2560 / 6383
im = Image.open("assets/maps/kit/china_night.jpg").convert("RGB")
W, H = 2560, round(4368 * K)
im.resize((W, H), Image.LANCZOS).save(R + "china_night_2560.jpg", quality=90)
s = open("assets/maps/kit/china_overlay.svg").read()
d = re.search(r'<path id="c-china"[^>]*d="([^"]*)"', s).group(1)
def scale_simplify(d, k, tol):
    out = []
    for sub in re.split(r"(?=M)", d):
        pts = [(float(a) * k, float(b) * k) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", sub)]
        if len(pts) < 3: continue
        keep = [pts[0]]
        for p in pts[1:]:
            if abs(p[0] - keep[-1][0]) + abs(p[1] - keep[-1][1]) >= tol: keep.append(p)
        if len(keep) < 4: continue
        out.append("M" + " L".join("%.1f %.1f" % p for p in keep) + " Z")
    return " ".join(out)
full = scale_simplify(d, K, 0.6)
open(R + "china_mask_2560.svg", "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d"><path fill="#fff" d="%s"/></svg>' % (W, H, W, H, full))
outline = scale_simplify(d, K, 7.0)
json.dump({"w": W, "h": H, "k": K, "outline": outline}, open(R + "china_outline_2560.json", "w"))
print(W, H, len(full), len(outline))
t = Image.open("assets/nvidia/shared/places/tsmc_fab14b.jpg").convert("RGB")
t.resize((2560, round(t.height * 2560 / t.width)), Image.LANCZOS).save(R + "tsmc_fab14b_2560.jpg", quality=88)
