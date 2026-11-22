"""cts04 derived assets (editor cts04, 2026-11-22). Run: .venv/bin/python project/cartels/gen/cts04_assets.py <scratch_dir>
scratch_dir holds the raw downloads (logged in assets/cartels/cts04/SOURCES.md)."""
import sys, os
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SCR = sys.argv[1]
P = f"{R}/assets/cartels/cts04/photos"; D = f"{R}/assets/cartels/cts04/derived"
os.makedirs(P, exist_ok=True); os.makedirs(D, exist_ok=True)
def save(im, p, q=90): im.convert("RGB").save(p, quality=q); print(p, im.size)
# originals kept as downloaded
for src, dst in [("hx_Gd7WEsyXcAAyoc_.jpg", "seizure_truckbed_gabseg.jpg"),
                 ("exp_orig.jpg", "seizure_collage_gabseg_expansion.jpg")]:
    save(Image.open(f"{SCR}/{src}"), f"{P}/{dst}")
eje = Image.open(f"{SCR}/eje_shot.png").convert("RGB")
save(eje, f"{P}/ejecentral_guacamaya_2022_page.jpg", 88)
# derived
h = Image.open(f"{P}/seizure_truckbed_gabseg.jpg")
save(h.crop((0, 0, 1600, 900)), f"{D}/seizure_hero_1600.jpg")
e = Image.open(f"{P}/seizure_collage_gabseg_expansion.jpg")
save(e.crop((912, 14, 1800, 1200)), f"{D}/seizure_bags_cab.jpg")
save(eje.crop((260, 200, 2440, 520)), f"{D}/eje_clip_headline.jpg")
save(eje.crop((260, 1040, 1860, 1490)), f"{D}/eje_clip_body.jpg")
pst = Image.open(f"{R}/assets/cartels/people/meza_fbi_poster_1.jpg")
save(pst.crop((24, 2734, 1782, 2781)), f"{D}/fbi_poster_2012_line.jpg")
g = Image.open(f"{R}/assets/cartels/people/guzman_booking_1.jpg")
save(g.crop((1000, 0, 2000, 1330)), f"{D}/guzman_booking_front.jpg")
# seamless grid-paper tile for the revolving-door board (crop the Texturelabs scan to whole grid cells, edges/corner dropped)
gp = Image.open(f"{R}/assets/textures/paper_graph_01_hires.jpg")
save(gp.crop((140, 162, 4064, 3010)), f"{D}/graph_tile.jpg", 92)
