"""cts12 derived assets (run: .venv/bin/python project/cartels/gen/cts12_assets.py). Writes assets/cartels/cts12/derived/."""
import json, re, subprocess
from PIL import Image, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
R = "assets/cartels/cts12/derived/"
# 1. northern-Sinaloa relief crop for the 3D net board (sinaloa kit px − (900,1400))
im = Image.open("assets/maps/kit/sinaloa_relief.jpg").crop((900, 1400, 3700, 3900))
im.save(R + "sinaloa_relief_net.jpg", quality=86)
# 2. North-America night crop for the flight Mexico City -> San Diego: px = kit − (0,1000)
im = Image.open("assets/maps/kit/north_america_night.jpg").crop((0, 1000, 4000, 4400))
im.save(R + "na_night_flight.jpg", quality=86)
s = open("assets/maps/kit/north_america_overlay.svg").read()
def tr(d, ox, oy, k):
    return re.sub(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", lambda m: "%.1f,%.1f" % ((float(m.group(1)) - ox) * k, (float(m.group(2)) - oy) * k), d)
bd = re.search(r'id="b-us_mexico"[^>]*\sd="([^"]+)"', s).group(1)
json.dump({"border": tr(bd, 0, 1000, 1.0)}, open(R + "na_flight_paths.json", "w"))
# 3. Infobae article (headline + dek) crop
im = Image.open("assets/cartels/news/n09_infobae_apec_trump.jpg").crop((120, 470, 2600, 980))
im.save(R + "infobae_apec_head.jpg", quality=90)
# 4. El Universal photo (special forces, helmets) crop below the headline
im = Image.open("assets/cartels/news/n01_eluniversal_lobos.jpg")
print("eluniversal", im.size)
im.crop((160, 880, 2360, 1584)).save(R + "eluniversal_fes_photo.jpg", quality=90)
# 5. house: still frames from the SEDENA arrest video (white walls)
for t in ("5.6", "3.4"):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", "assets/cartels/footage/m6_arrest_full31s.mp4", "-frames:v", "1",
                    "-q:v", "2", R + "sedena_house_%s.jpg" % t.replace(".", "_")], check=True)
print("ok")
