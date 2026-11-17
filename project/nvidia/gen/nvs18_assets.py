"""nvs18 derived assets: China night-map crop + China outline in crop px, and the sky-keyed foreground of the Kwai Tsing
cranes photo (for the 600,000 numerals hero). Run: .venv/bin/python project/nvidia/gen/nvs18_assets.py"""
import json, re
import numpy as np
from PIL import Image, ImageFilter
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"
OUT = "assets/nvidia/nvs18/derived/"

def china_crop():
    # crop x 2350..5350, y 2400..4088 of china_night (6383x4368) = lon 97.8..130.7, lat 33.6..18.5, scaled to 2560 wide
    x0, y0, x1, y1 = 2350, 2400, 5350, 4088
    s = 2560 / (x1 - x0)
    im = Image.open(K + "china_night.jpg").crop((x0, y0, x1, y1)).resize((2560, round((y1 - y0) * s)), Image.LANCZOS)
    im.save(OUT + "china_night_crop.jpg", quality=90)
    svg = open(K + "china_overlay.svg").read()
    def path(pid):
        m = re.search(r'id="%s"[^>]*\sd="([^"]+)"' % pid, svg)
        d = m.group(1)
        def tr(mm):
            x, y = float(mm.group(1)), float(mm.group(2))
            return "%.1f %.1f" % ((x - x0) * s, (y - y0) * s)
        return re.sub(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", tr, d)
    pl = json.load(open(K + "china.json"))["places"]
    P = {k: [round((pl[k]["x"] - x0) * s, 1), round((pl[k]["y"] - y0) * s, 1)] for k in ["hong_kong", "shenzhen", "guangzhou", "shanghai"]}
    json.dump({"w": 2560, "h": im.size[1], "s": s, "china": path("c-china"), "taiwan": path("c-taiwan"),
               "hong_kong": path("c-hong_kong"), "places": P}, open(OUT + "china_crop.json", "w"))
    print("china crop", im.size, P)

def cranes_fg():
    im = Image.open("assets/nvidia/nvs18/photos/kwai_tsing_cranes_2024.jpg").convert("RGB")
    a = np.asarray(im).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    sat = (mx - mn) / np.maximum(mx, 1)
    H, W = mx.shape
    yy = np.arange(H)[:, None].repeat(W, 1)
    # sky: bright-ish, unsaturated, blue >= red, above the horizon band
    sky = (mx > 150) & (sat < 0.22) & (b >= r - 4) & (yy < 760)
    sky[:520] |= ((mx > 120) & (sat < 0.3))[:520]
    # keep only sky connected to the top: flood from row 0 via scanline (simple iterative dilation inside the candidate)
    reach = np.zeros_like(sky); reach[0] = sky[0]
    for y in range(1, H):
        row = sky[y] & (reach[y - 1] | np.roll(reach[y - 1], 1) | np.roll(reach[y - 1], -1))
        # spread along the row
        if row.any():
            idx = np.where(sky[y])[0]
            segs = np.split(idx, np.where(np.diff(idx) != 1)[0] + 1)
            for sg in segs:
                if row[sg].any(): row[sg] = True
        reach[y] = row
    reach[:550] = True
    alpha = Image.fromarray(((~reach) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    fg = im.copy(); fg.putalpha(alpha)
    fg.save(OUT + "kwai_tsing_cranes_fg.png")
    print("fg saved; sky share", reach.mean())

def simplify(d, tol=3.0):
    out = []
    for sub in re.findall(r"M[^M]+", d):
        pts = [(float(a), float(b)) for a, b in re.findall(r"(-?\d+\.?\d*) (-?\d+\.?\d*)", sub)]
        keep = [pts[0]]
        for p in pts[1:]:
            if abs(p[0] - keep[-1][0]) + abs(p[1] - keep[-1][1]) >= tol: keep.append(p)
        if len(keep) < 4: continue
        out.append("M" + "L".join("%d %d" % (round(x), round(y)) for x, y in keep) + "Z")
    return "".join(out)

def slim():
    j = json.load(open(OUT + "china_crop.json"))
    for k in ["china", "taiwan", "hong_kong"]: j[k] = simplify(j[k], 5.0 if k == "china" else 1.5)
    json.dump(j, open(OUT + "china_crop.json", "w"))
    print({k: len(j[k]) for k in ["china", "taiwan", "hong_kong"]})

if __name__ == "__main__":
    import sys
    if "slim" in sys.argv: slim()
    else: china_crop(); cranes_fg(); slim()
