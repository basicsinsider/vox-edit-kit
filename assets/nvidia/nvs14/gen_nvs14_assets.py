"""nvs14 derived assets (run from repo root: .venv/bin/python assets/nvidia/nvs14/gen_nvs14_assets.py)
1. pacific_us_night.jpg : world_night crop 70E..320E (=40W) x 82N..40S at half resolution (22.756 px/deg)
                          x = (lon(+360 if <0) - 70) * 22.756 ; y = (82 - lat) * 22.756
2. pu_china.svg / pu_usa.svg : China / USA outlines in that pixel space (CSS masks)
3. sherwood_head.jpg  : headline + standfirst block of shared/news/s11_sherwood_gpus.jpg (y 990-1470)
4. sherwood_photo.jpg : the article's lead photo (x 300-1500, y 30-930)
"""
import re
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"; O = "assets/nvidia/nvs14/derived/"
PX = 16384 / 360.0
LON0, LON1, LAT0, LAT1, SC = 70, 320, 82, -40, 0.5

def world_path(svgtxt, cid):
    return re.search(r'id="%s"[^>]*?\sd="([^"]+)"' % cid, svgtxt).group(1)

def subpaths(d):
    out = []
    for sp in re.split(r'(?=M)', d):
        nums = list(map(float, re.findall(r'-?\d+\.?\d*', sp)))
        pts = list(zip(nums[0::2], nums[1::2]))
        if len(pts) > 2: out.append(pts)
    return out

def to_d(subs, f, minpts=6, step=2):
    parts = []
    for pts in subs:
        if len(pts) < minpts: continue
        q = [f(x, y) for x, y in pts[::step] + [pts[-1]]]
        parts.append("M" + "L".join("%.1f,%.1f" % p for p in q) + "Z")
    return "".join(parts)

def main():
    w = Image.open(K + "world_night.jpg")
    x0, y0 = int((LON0 + 180) * PX), int((90 - LAT0) * PX)
    x1, y1 = int(16384 + (LON1 - 360 + 180) * PX), int((90 - LAT1) * PX)
    a = w.crop((x0, y0, 16384, y1)); b = w.crop((0, y0, x1 - 16384, y1))
    m = Image.new("RGB", (a.width + b.width, a.height)); m.paste(a, (0, 0)); m.paste(b, (a.width, 0))
    m = m.resize((int(m.width * SC), int(m.height * SC)), Image.LANCZOS)
    m.save(O + "pacific_us_night.jpg", quality=88); print("map", m.size)
    s = open(K + "world_overlay.svg").read()
    def f(x, y):
        if x < 180 * PX: x += 16384
        return ((x - x0) * SC, (y - y0) * SC)
    for cid, name in [("c-china", "pu_china"), ("c-united_states_of_america", "pu_usa")]:
        d = to_d(subpaths(world_path(s, cid)), f)
        open(O + name + ".svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d"><path d="%s"/></svg>' % (m.width, m.height, m.width, m.height, d))
        print(name, len(d))
    sw = Image.open("assets/nvidia/shared/news/s11_sherwood_gpus.jpg").convert("RGB")
    sw.crop((0, 990, 1800, 1470)).save(O + "sherwood_head.jpg", quality=92)
    sw.crop((300, 30, 1500, 930)).save(O + "sherwood_photo.jpg", quality=90)
    print("sherwood ok")

main()
