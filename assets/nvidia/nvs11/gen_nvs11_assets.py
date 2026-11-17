"""nvs11 derived assets (run from repo root with .venv/bin/python assets/nvidia/nvs11/gen_nvs11_assets.py).
1. pacific_world_night.jpg  : world_night crop 45E..293E (=67W) x 80N..60S, half resolution (22.756 px/deg)
2. pw_china.svg / pw_usa.svg : China / USA outlines in that pixel space (lon<0 -> +360)
3. cn_china_fill.svg         : China outline in the china_* kit pixel space (6383x4368)
4. fortune_dc_dissent crop    : headline + photo block of the Fortune article screenshot
5. fortune_memphis_crop.jpg  : headline + photo block of shared/news/s08_fortune_memphis.jpg
6. liang_card.jpg            : Liang Wenfeng crop from shared/people/liang_1.jpg (native pixels)
"""
import re, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = "assets/maps/kit/"; O = "assets/nvidia/nvs11/derived/"
PX = 16384 / 360.0
LON0, LON1, LAT0, LAT1, SC = 45, 293, 80, -60, 0.5

def world_path(svgtxt, cid):
    m = re.search(r'id="%s"[^>]*?\sd="([^"]+)"' % cid, svgtxt)
    return m.group(1)

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
        q = pts[::step] + [pts[-1]]
        q = [f(x, y) for x, y in q]
        parts.append("M" + "L".join("%.1f,%.1f" % p for p in q) + "Z")
    return "".join(parts)

def main():
    w = Image.open(K + "world_night.jpg")
    x0, y0 = int(LON0 * PX + 180 * PX), int((90 - LAT0) * PX)
    x1, y1 = int(16384 + (LON1 - 360 + 180) * PX), int((90 - LAT1) * PX)
    a = w.crop((x0, y0, 16384, y1)); b = w.crop((0, y0, x1 - 16384, y1))
    m = Image.new("RGB", (a.width + b.width, a.height)); m.paste(a, (0, 0)); m.paste(b, (a.width, 0))
    m = m.resize((int(m.width * SC), int(m.height * SC)), Image.LANCZOS)
    m.save(O + "pacific_world_night.jpg", quality=88); print("map", m.size)
    s = open(K + "world_overlay.svg").read()
    def f(x, y):
        if x < 180 * PX: x += 16384      # western hemisphere -> east of the antimeridian
        return ((x - x0) * SC, (y - y0) * SC)
    for cid, name in [("c-china", "pw_china"), ("c-united_states_of_america", "pw_usa")]:
        d = to_d(subpaths(world_path(s, cid)), f)
        open(O + name + ".svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d"><path d="%s"/></svg>' % (m.width, m.height, m.width, m.height, d))
        print(name, len(d))
    c = open(K + "china_overlay.svg").read()
    d = to_d(subpaths(world_path(c, "c-china")), lambda x, y: (x, y), minpts=8, step=3)
    open(O + "cn_china_fill.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6383 4368" width="6383" height="4368"><path d="%s"/></svg>' % d)
    print("cn", len(d))
    src = "work/nvs11_scratch/dl/fortune_dissent.png"
    try:
        im = Image.open(src).convert("RGB").crop((240, 960, 2960, 1960)); im.save("assets/nvidia/nvs11/news/fortune_dc_dissent_2026-06-16.jpg", quality=90); print("fortune", im.size)
    except FileNotFoundError: print("fortune screenshot missing (kept the saved crop)")
    mm = Image.open("assets/nvidia/shared/news/s08_fortune_memphis.jpg").convert("RGB").crop((240, 384, 2960, 1384)); mm.save(O + "fortune_memphis_crop.jpg", quality=90); print("memphis", mm.size)
    l = Image.open("assets/nvidia/shared/people/liang_1.jpg").convert("RGB").crop((262, 70, 532, 330)); l.save(O + "liang_card.jpg", quality=92); print("liang", l.size)

main()
