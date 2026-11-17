"""nvs15 derived assets: (1) headline crop of shared/news/s12_thehackernews.jpg (greyscale, page white kept for multiply),
(2) China (red) + USA (ice) fills on the kit Pacific pixel space (6380x2420) from pacific_overlay.svg."""
import re, sys
from PIL import Image, ImageDraw, ImageOps
R = "/home/user/vox-edit-kit/" if len(sys.argv) < 2 else sys.argv[1]
OUT = R + "assets/nvidia/nvs15/derived/"
im = Image.open(R + "assets/nvidia/shared/news/s12_thehackernews.jpg").convert("RGB")
crop = ImageOps.grayscale(im.crop((100, 40, 2360, 340)))
crop.save(OUT + "s12_headline_crop.png")
print("crop", crop.size)
svg = open(R + "assets/maps/kit/pacific_overlay.svg").read()
W, H = 6380, 2420
def polys(cid):
    d = re.search(r'id="%s"[^>]*\sd="([^"]+)"' % cid, svg).group(1)
    out = []
    for sub in d.split("M")[1:]:
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sub)]
        if len(pts) > 2: out.append(pts)
    return out
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dr = ImageDraw.Draw(img)
for cid, col in (("c-china", (220, 47, 60, 255)), ("c-united_states_of_america", (42, 159, 201, 255))):
    for p in polys(cid):
        if max(x for x, _ in p) < -50 or min(x for x, _ in p) > W + 50: continue
        dr.polygon(p, fill=col)
img.save(OUT + "pacific_cn_us_fill.png", optimize=True)
print("fill ok")
