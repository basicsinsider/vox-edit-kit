#!/usr/bin/env python3
"""ED13 (pd33–pd35) derived assets -> assets/podcast/pd33/.  Run from the repo root: python3 project/podcast/gen/ed13/ed13_assets.py
Needs ffmpeg + PIL. The vote-board frame was grabbed from the archive.org UN film (see SOURCES.md) — not re-fetched here."""
import subprocess
from PIL import Image
OUT = "assets/podcast/pd33/"
# 1) stills from the UN 1971 celebration film (already in the repo)
for t, name in ((7.5, "un1971_celebration_hall_still.jpg"), (4.0, "un1971_celebration_delegate_still.jpg")):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", "assets/c6/footage/un1971_celebration_delegate_clapping.mp4",
                    "-frames:v", "1", "-q:v", "2", OUT + name], check=True)
# 2) the slogan wall, cropped to the eight characters (Taichung, Commons CC BY 2.0)
Image.open("assets/c6/photos/slogan_zhuangjing_ziqiang_taichung_wall.jpg").crop((120, 420, 1720, 820)).save(OUT + "slogan_wall_crop.jpg", quality=92)
# 3) Jimmy Carter from NARA 183157 (Deng cropped out — he is revealed later, in pd35)
Image.open("assets/c6/photos/deng_xiaoping_carter_1979_nara183157.jpg").crop((945, 360, 1345, 860)).save(OUT + "carter_1979_crop_nara183157.jpg", quality=92)
print("ok")
