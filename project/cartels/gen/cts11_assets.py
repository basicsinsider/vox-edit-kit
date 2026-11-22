"""cts11 derived assets: photo crops from logged news screenshots, news cards, map overlay paths (JSON).
Run: .venv/bin/python project/cartels/gen/cts11_assets.py   (from the repo root)"""
import json, re
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
N = "assets/cartels/news/"
O = "assets/cartels/cts11/derived/"

def crop(src, box, out, q=90, maxw=None):
    im = Image.open(src).convert("RGB").crop(box)
    if maxw and im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(O + out, quality=q); print(out, im.size)

# --- photos (from Infobae article pages, captured by the news gatherer) ---
crop(N + "n04_infobae_nyt_zuany_full.jpg", (702, 1390, 2413, 2533), "zuany_office.jpg")          # Zuany in his office (10 Nov 2026 article)
crop(N + "n04_infobae_nyt_zuany_full.jpg", (702, 4658, 2413, 5617), "zuany_jauregui_fge.jpg")   # caption: Zuany Portillo … Crédito: FGE Chihuahua
crop(N + "n04_infobae_jauregui_full.jpg", (702, 1390, 2413, 2533), "jauregui_reuters.jpg")      # caption: César Jáuregui … REUTERS/José Luis González
# --- news cards ---
crop(N + "n04_aljazeera_crash.jpg", (130, 440, 1730, 1608), "card_aj_crash.jpg")
crop(N + "n04_pbs_crash_cia.jpg", (127, 452, 1979, 1789), "card_pbs_cia.jpg")
crop(N + "n04_cbs_not_informed_k1.jpg", (240, 420, 1640, 1800), "card_cbs_informed.jpg")
crop(N + "n04_pbs_sheinbaum_explanation.jpg", (100, 490, 2000, 1690), "card_pbs_sheinbaum.jpg")

# --- map overlay paths ---
def paths(region, ids):
    s = open(f"assets/maps/kit/{region}_overlay.svg").read(); out = {}
    for m in re.finditer(r'<path id="([^"]+)"[^>]*d="([^"]+)"', s):
        if m.group(1) in ids:
            d = re.sub(r"(\d+)\.(\d)\d*", lambda k: k.group(1) if k.group(2) in "01234" else str(int(k.group(1)) + 1), m.group(2))
            out[m.group(1)] = d
    return out
data = {"chihuahua": paths("chihuahua", {"st-chihuahua", "rg-sierra_tarahumara", "b-us_mexico"}),
        "mexico": paths("mexico", {"st-chihuahua", "b-us_mexico"})}
json.dump(data, open(O + "paths.json", "w"))
print({k: {i: len(v) for i, v in d.items()} for k, d in data.items()})

# --- portraits for CT.file (from the FGE Chihuahua photo of Zuany Portillo + César Jáuregui Moreno) ---
crop(O + "zuany_jauregui_fge.jpg", (66, 0, 686, 766), "file_zuany.jpg")
crop(O + "zuany_jauregui_fge.jpg", (905, 0, 1525, 766), "file_jauregui.jpg")

# --- stills from the shared footage (blurred fills / end-of-clip fallback) ---
import subprocess
F = "assets/cartels/footage/"
for src, t, out in [("x_chihuahua_narcolab_b.mp4", 3.0, "still_lab_b.jpg"), ("x_chihuahua_narcolab_a.mp4", 6.0, "still_lab_a1.jpg"),
                    ("x_chihuahua_narcolab_a.mp4", 11.0, "still_lab_a2.jpg"), ("m5_sub_chepe_canyon.mp4", 7.25, "still_canyon_end.jpg")]:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", F + src, "-frames:v", "1", "-q:v", "3", O + out], check=True)
    print(out)
