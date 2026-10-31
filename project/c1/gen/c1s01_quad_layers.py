"""c1s01 · C1S027 2.5D Main Quad layers from the Detroit Publishing photochrom of the Inner Quad west entrance (c1900).
Writes assets/c1/cutouts/quad_layers/{sky.jpg, quad.png, bush.png, layout.json}. Run: .venv/bin/python project/c1/gen/c1s01_quad_layers.py"""
import json, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

R = pathlib.Path(__file__).resolve().parents[3]
src = Image.open(R / "assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg").convert("RGB")
k = src.size[0] / 1600.0
box = [int(22 * k), int(26 * k), int(1568 * k), int(745 * k)]
im = src.crop(box)
W = 2880; H = round(im.size[1] * W / im.size[0])
im = im.resize((W, H), Image.LANCZOS)
s = W / 1546.0                                   # 1600-preview px (after crop offset) -> layer px
P = lambda pts: [((x - 22) * s, (y - 26) * s) for x, y in pts]
a = np.asarray(im).astype(np.float32)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
# sky: cool/cyan, bright, low red; connected to the top edge
lum = (r + g + b) / 3
tex = np.sqrt(np.maximum(ndimage.uniform_filter(lum ** 2, 9) - ndimage.uniform_filter(lum, 9) ** 2, 0))
cand = (g >= r - 4) & (r > 150) & (g > 180) & (b < g + 6) & (tex < 7)
lab, n = ndimage.label(cand)
top = set(np.unique(lab[0, :])) - {0}
sky = np.isin(lab, list(top))
sky = ndimage.binary_closing(sky, iterations=2)
sky = ndimage.binary_fill_holes(sky | (np.arange(H)[:, None] < 2)) & (np.arange(H)[:, None] < H * 0.62)
alpha = Image.fromarray(((~sky) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6))
out = R / "assets/c1/cutouts/quad_layers"; out.mkdir(parents=True, exist_ok=True)
im.save(out / "sky.jpg", quality=88)
q = im.copy(); q.putalpha(alpha); q.save(out / "quad.png", optimize=True)
# near layer: the big left shrub bed (hand polygon, feathered) — sits in front of the arcade
m = Image.new("L", (W, H), 0)
ImageDraw.Draw(m).polygon(P([(22, 250), (150, 175), (300, 185), (420, 250), (520, 330), (610, 360), (700, 395), (775, 465),
                              (830, 560), (852, 640), (760, 662), (500, 672), (22, 686)]), fill=255)
m = m.filter(ImageFilter.GaussianBlur(10))
bm = Image.fromarray((np.asarray(m).astype(np.float32) * np.asarray(alpha).astype(np.float32) / 255).astype(np.uint8))
bush = im.copy(); bush.putalpha(bm); bush.save(out / "bush.png", optimize=True)
json.dump({"w": W, "h": H, "src": "assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg", "crop_box_src_px": box,
           "arch_centre": [round((1000 - 22) * s), round((420 - 26) * s)],
           "note": "sky.jpg = full plate (blur it as the far layer); quad.png = plate minus sky; bush.png = left shrub bed (near layer)"},
          open(out / "layout.json", "w"), indent=1)
print("ok", W, H)
