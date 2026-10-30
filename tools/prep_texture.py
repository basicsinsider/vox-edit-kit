"""Prepares a raw texture download for use in the edit (MANUAL §3.3).

Writes, next to the chosen name in assets/textures/:
  NAME.jpg            1920 px wide working copy
  NAME_hires.jpg      full resolution (q95)
  NAME_norm.jpg       desaturated, median shifted to 50 % grey (for overlay / soft-light blends)
  NAME_norm_hires.jpg
and keeps the original in assets/textures/_raw/. Prints the recommended blend mode from the background tone.

Usage: .venv/bin/python tools/prep_texture.py RAW_FILE NAME [--no-norm]
  e.g. .venv/bin/python tools/prep_texture.py ~/Downloads/grunge_360.jpg dust_04
"""
import shutil, sys, pathlib
import numpy as np
from PIL import Image

if len(sys.argv) < 3:
    sys.exit(__doc__)
raw, name = pathlib.Path(sys.argv[1]), sys.argv[2]
root = pathlib.Path(__file__).resolve().parent.parent / "assets/textures"
(root / "_raw").mkdir(parents=True, exist_ok=True)
shutil.copy2(raw, root / "_raw" / raw.name)

im = Image.open(raw).convert("RGB")
im.save(root / f"{name}_hires.jpg", quality=95)
w = 1920
im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(root / f"{name}.jpg", quality=92)

grey = np.asarray(im.convert("L"), dtype=float)
med = float(np.median(grey))
if "--no-norm" not in sys.argv:
    norm = np.clip(grey + (128 - med), 0, 255).astype(np.uint8)
    n = Image.fromarray(norm)
    n.save(root / f"{name}_norm_hires.jpg", quality=95)
    n.resize((w, round(n.height * w / n.width)), Image.LANCZOS).save(root / f"{name}_norm.jpg", quality=92)

blend = "screen (dark background)" if med < 70 else "multiply (light background)" if med > 185 else "overlay / soft-light (use the _norm file)"
print(f"{name}: {im.width}x{im.height}, median {med:.0f} -> recommended blend: {blend}")
print("Now add a row to assets/textures/SOURCES.md (file, Texturelabs page URL, licence, size, blend).")
