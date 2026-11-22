"""cts05 derived assets: cleaned cutouts as duotone halftone PNGs (ref ast_4b7fb0fe0a134429 collage), document crops.
Run: .venv/bin/python project/cartels/gen/cts05_assets.py"""
import numpy as np
from PIL import Image
D = "assets/cartels/cts05/derived/"

def hexrgb(h): h = h.lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)

def duotone_halftone(src, out, dark, light, cell=7, clean=None, maxw=1100):
    im = Image.open(src).convert("RGBA")
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    a = np.asarray(im).astype(float)
    alpha = a[..., 3]
    if clean: alpha = clean(alpha, im.width, im.height)
    L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]) / 255.0
    L = np.clip((L - 0.08) / 0.84, 0, 1) ** 0.9
    # 45° dot screen: darkness -> dot coverage
    h, w = L.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    u = (xx + yy) / np.sqrt(2) / cell; v = (xx - yy) / np.sqrt(2) / cell
    du = u - np.floor(u) - 0.5; dv = v - np.floor(v) - 0.5
    r = np.sqrt(du * du + dv * dv)                       # 0 .. 0.707
    dark_amt = 1 - L
    rad = np.sqrt(dark_amt) * 0.62
    dot = np.clip((rad - r) * cell * 1.2 + 0.5, 0, 1)   # antialiased dots
    tone = 0.55 * dark_amt + 0.45 * dot                  # keep photo detail + print dots
    tone = np.clip(tone, 0, 1)[..., None]
    c = hexrgb(light) * (1 - tone) + hexrgb(dark) * tone
    o = np.dstack([c, alpha]).clip(0, 255).astype(np.uint8)
    Image.fromarray(o, "RGBA").save(out)
    print(out, o.shape)

def clean_trump(al, w, h):
    al = al.copy()
    sx = w / 920.0
    yy, xx = np.mgrid[0:h, 0:w] / sx                       # crop-space coordinates (crop of 920 px)
    al[(xx < 300) & (yy < 285)] = 0                          # VP Vance's hands (top-left)
    al[(xx < 215) & (yy < 545 - xx * 270 / 210)] = 0         # matting ghost above the left shoulder line
    al[al < 150] = 0
    return al

if __name__ == "__main__":
    duotone_halftone(D + "trump_cut.png", D + "trump_duo.png", "#1a2836", "#d9e4ee", clean=clean_trump)
    duotone_halftone(D + "sheinbaum_cut.png", D + "sheinbaum_duo.png", "#2a2b14", "#e8e8c4")
