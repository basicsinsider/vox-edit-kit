"""nvs08 derived assets (crops of shared docs/news + map overlays). Run: .venv/bin/python project/nvidia/gen/nvs08_assets.py"""
import re
from PIL import Image

D = "assets/nvidia/nvs08/derived/"
SH = "assets/nvidia/shared/"
K = "assets/maps/kit/"

# --- surveillance stills (DOJ indictment images) ---
c = Image.open(SH + "news/s07_still_warehouse_tomshw.jpg").convert("RGB")      # Tom's Hardware composite of DOJ stills (clean, no ellipses)
c.crop((0, 0, 760, 792)).save(D + "still_hairdryer.jpg", quality=92)
w = Image.open(SH + "docs/doj_indictment_warehouse_stills_p15.png").convert("RGB")  # indictment p15, left still (17:01)
w.crop((50, 44, 922, 886)).save(D + "still_warehouse_room.jpg", quality=92)
l = Image.open(SH + "people/liaw_1.jpg").convert("RGB")                          # 326 px source: Liaw is the man on the left
l.crop((18, 82, 168, 232)).save(D + "liaw_face_crop.jpg", quality=95)
m = Image.open(SH + "news/s02_tomshw_megaspeed.jpg").convert("RGB")              # headline + dek, no photo
m.crop((40, 40, 1300, 800)).save(D + "tomshw_megaspeed_head.jpg", quality=92)
hd = Image.open(SH + "hardware/cutouts/hairdryer_cutout.png").convert("RGBA")
hd.thumbnail((700, 700)); hd.save(D + "hairdryer_cutout_700.png")


def paths(svg, ids):
    s = open(svg).read()
    out = {}
    for cid in ids:
        mm = re.search(r'<path[^>]*id="%s"[^>]*\sd="([^"]+)"' % cid, s) or re.search(r'<path[^>]*\sd="([^"]+)"[^>]*id="%s"' % cid, s)
        out[cid] = mm.group(1) if mm else None
    return out


def group(svg, gid):
    s = open(svg).read()
    mm = re.search(r'<g id="%s">(.*?)</g>' % gid, s, re.S)
    return mm.group(1) if mm else ""


# --- pacific: country borders + China fill (same pixel space as pacific_night.jpg 6380x2420) ---
W, H = 6380, 2420
bord = group(K + "pacific_overlay.svg", "countries")
open(D + "pac_borders.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><g fill="none" stroke="#f0efe8" stroke-width="3" stroke-opacity="0.42" stroke-linejoin="round">{bord}</g></svg>')
p = paths(K + "pacific_overlay.svg", ["c-china"])
open(D + "pac_china_fill.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><path d="{p["c-china"]}" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="5" stroke-linejoin="round"/></svg>')

# --- southeast asia: borders + soft fills of the SE Asian countries ---
W, H = 5428, 7030
bord = group(K + "southeast_asia_overlay.svg", "countries")
open(D + "sea_borders.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><g fill="none" stroke="#f0efe8" stroke-width="4" stroke-opacity="0.45" stroke-linejoin="round">{bord}</g></svg>')
ids = ["c-malaysia", "c-singapore", "c-thailand", "c-vietnam", "c-indonesia", "c-philippines", "c-cambodia", "c-brunei"]
p = paths(K + "southeast_asia_overlay.svg", ids)
body = "".join(f'<path d="{d}"/>' for d in p.values() if d)
open(D + "sea_region_fill.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><g fill="#f0efe8" fill-opacity="0.16" stroke="#f0efe8" stroke-opacity="0.7" stroke-width="6">{body}</g></svg>')
print({k: bool(v) for k, v in p.items()})
