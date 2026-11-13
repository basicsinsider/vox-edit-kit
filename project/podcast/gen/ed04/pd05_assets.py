"""pd05 derived map: Bay Area atlas -> silicon (cool grey) relief, water flat, padded with sea on the left.
Output assets/podcast/pd05/bay_area_silicon_2909.jpg ; pixel space: X' = (X + 1300) * 0.4, Y' = (Y - 921) * 0.4
where X = (lon + 123.0) * 4118.4, Y = (38.25 - lat) * 5200 (kit bay_area.json). Usage: .venv/bin/python project/podcast/gen/ed04/pd05_assets.py"""
import numpy as np
from PIL import Image, ImageFilter
Image.MAX_IMAGE_PIXELS = None
K = 'assets/maps/kit/'
a = Image.open(K + 'bay_area_atlas.jpg').convert('L')
m = Image.open(K + 'bay_area_landmask.png').convert('L').resize(a.size)
y0, y1 = 921, 5321
a = a.crop((0, y0, a.width, y1)); m = m.crop((0, y0, m.width, y1))
sc = 0.4
a = a.resize((round(a.width * sc), round(a.height * sc)), Image.LANCZOS)
m = m.resize(a.size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.8))
L = np.asarray(a, np.float32) / 255.0
M = np.asarray(m, np.float32) / 255.0
lo, hi = np.percentile(L[M > 0.5], [1, 99.5])
t = np.clip((L - lo) / (hi - lo), 0, 1) ** 1.15
dark = np.array([0x6b, 0x70, 0x7b], np.float32); light = np.array([0xef, 0xee, 0xe8], np.float32)
land = dark + (light - dark) * t[..., None]
sea = np.array([0xa9, 0xae, 0xb8], np.float32)
out = sea + (land - sea) * M[..., None]
# thin darker shoreline
edge = np.asarray(m.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1.2)), np.float32) / 255.0
out = out * (1 - np.clip(edge * 2.2, 0, 0.45)[..., None])
pad = round(1300 * sc)
full = np.empty((out.shape[0], out.shape[1] + pad, 3), np.float32); full[:, :pad] = sea; full[:, pad:] = out
im = Image.fromarray(np.clip(full, 0, 255).astype(np.uint8)); print(im.size, 'landmask mean', M.mean())
im.save('assets/podcast/pd05/bay_area_silicon_2909.jpg', quality=90)
