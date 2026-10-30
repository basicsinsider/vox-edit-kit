"""Print-style halftone renderer (45° dot screen) with optional sky-key cutout.

Usage:
  python tools/halftone.py IN.jpg OUT.png [--sky-key] [--water Y] [--cell 7] [--ink 1c1e22] [--paper e9e4da] [--transparent-paper]
    --sky-key            cut away a plain sky above a skyline (column scan from the top)
    --water Y            crop/stop the cutout at row Y (e.g. a waterline)
    --mask M.png         use an existing alpha mask (white = keep) instead of --sky-key
    --transparent-paper  paper areas become transparent (dots only), for overlaying on coloured grounds
Needs numpy and Pillow (venv: .venv).
"""
import argparse
import numpy as np
from PIL import Image
from PIL import ImageFilter


def gaussian_filter(arr, sigma):
    """Gaussian blur via Pillow (works on 1-D or 2-D float arrays in any range)."""
    a = np.asarray(arr, dtype=float)
    one_d = a.ndim == 1
    if one_d:
        a = a[None, :]
    lo, hi = a.min(), a.max()
    span = (hi - lo) or 1.0
    img = Image.fromarray(((a - lo) / span * 255).round().astype(np.uint8), mode="L")
    out = np.asarray(img.filter(ImageFilter.GaussianBlur(sigma))).astype(float) / 255 * span + lo
    return out[0] if one_d else out


def median_filter(arr, size):
    a = np.asarray(arr)
    pad = size // 2
    p = np.pad(a, pad, mode="edge")
    return np.array([np.median(p[i:i + size]) for i in range(len(a))]).astype(a.dtype)

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--sky-key", action="store_true")
ap.add_argument("--water", type=int, default=0)
ap.add_argument("--mask")
ap.add_argument("--cell", type=float, default=7.0)
ap.add_argument("--ink", default="1c1e22")
ap.add_argument("--paper", default="e9e4da")
ap.add_argument("--transparent-paper", action="store_true")
a = ap.parse_args()

im = np.asarray(Image.open(a.inp).convert("L")).astype(float)
H, W = im.shape
bottom = a.water or H
mask = np.ones((H, W))
if a.sky_key:
    sky = gaussian_filter(np.median(im[:60, :], axis=0), 25)
    sm = gaussian_filter(im, 1.2)
    top = np.full(W, bottom)
    for x in range(W):
        d = np.abs(sm[:bottom, x] - sky[x]) > 16
        top[x] = np.argmax(d) if d.any() else bottom
    top = median_filter(top, 31)
    mask = np.zeros((H, W))
    for x in range(W):
        mask[top[x]:bottom, x] = 1
    mask = gaussian_filter(mask, 0.8)
elif a.mask:
    mask = np.asarray(Image.open(a.mask).convert("L").resize((W, H))).astype(float) / 255

g = gaussian_filter(im / 255.0, 1.0)
yy, xx = np.mgrid[0:H, 0:W].astype(float)
ang = np.deg2rad(45)
u = (xx * np.cos(ang) + yy * np.sin(ang)) / a.cell
v = (-xx * np.sin(ang) + yy * np.cos(ang)) / a.cell
dist = np.sqrt((u - np.floor(u) - 0.5) ** 2 + (v - np.floor(v) - 0.5) ** 2)
rad = np.sqrt(np.clip(1 - g, 0, 1) ** 0.9) * 0.62
ink = gaussian_filter((dist < rad).astype(float), 0.5)

hexc = lambda h: np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)])
paper, inkc = hexc(a.paper), hexc(a.ink)
rgb = (paper[None, None] * (1 - ink[..., None]) + inkc[None, None] * ink[..., None]).astype(np.uint8)
alpha = mask * (ink if a.transparent_paper else 1)
out = np.dstack([rgb, (alpha * 255).astype(np.uint8)])[:bottom]
Image.fromarray(out, "RGBA").save(a.out)
print("wrote", a.out, out.shape[1], "x", out.shape[0])
