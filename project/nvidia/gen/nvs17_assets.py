"""nvs17 derived assets.
- China fill / stroke SVGs in the china_* map-kit pixel space (6383x4368)            -> cn_china_{fill,stroke}.svg
- China / Malaysia / Singapore outlines in the southeast_asia_* pixel space (5428x7030) -> sea_*.svg
- a tight China silhouette (own viewBox = China's bbox in the china_* space)            -> china_shape.svg
Run: python3 project/nvidia/gen/nvs17_assets.py
"""
import re, pathlib
R = pathlib.Path(__file__).resolve().parents[3]
out = R / "assets/nvidia/nvs17/derived"
out.mkdir(parents=True, exist_ok=True)


def path_d(overlay, cid):
    src = (R / "assets/maps/kit" / overlay).read_text()
    m = re.search(r'<path[^>]*id="c-%s"[^>]*>' % cid, src)
    return re.search(r'\sd="([^"]+)"', m.group(0)).group(1)


def hdr(W, H, vb=None):
    vb = vb or f"0 0 {W} {H}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{W}" height="{H}">'


# china_* space
d = path_d("china_overlay.svg", "china")
W, H = 6383, 4368
(out / "cn_china_fill.svg").write_text(hdr(W, H) + f'<path d="{d}" fill="#dc2f3c" fill-rule="evenodd"/></svg>')
(out / "cn_china_stroke.svg").write_text(hdr(W, H) + f'<path d="{d}" fill="none" stroke="#f6a4a9" stroke-width="7" stroke-linejoin="round"/></svg>')
# bbox of the China path (drop sub-paths far outside)
nums = [tuple(map(float, p)) for p in re.findall(r'(-?\d+\.?\d*),(-?\d+\.?\d*)', d)]
xs = [p[0] for p in nums if 0 <= p[0] <= W]; ys = [p[1] for p in nums if 0 <= p[1] <= H]
x0, x1, y0, y1 = min(xs) - 20, max(xs) + 20, min(ys) - 20, max(ys) + 20
bw, bh = x1 - x0, y1 - y0
(out / "china_shape.svg").write_text(hdr(round(bw), round(bh), f"{x0:.0f} {y0:.0f} {bw:.0f} {bh:.0f}") +
                                     f'<path d="{d}" fill="#dc2f3c" fill-rule="evenodd"/></svg>')
print("china bbox", x0, y0, bw, bh)

# southeast_asia_* space
W, H = 5428, 7030
for cid, fill, stroke in [("china", "#dc2f3c", "#f6a4a9")]:
    d = path_d("southeast_asia_overlay.svg", cid)
    (out / f"sea_{cid}_fill.svg").write_text(hdr(W, H) + f'<path d="{d}" fill="{fill}" fill-rule="evenodd"/></svg>')
    (out / f"sea_{cid}_stroke.svg").write_text(hdr(W, H) + f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="6" stroke-linejoin="round"/></svg>')
ds = [path_d("southeast_asia_overlay.svg", c) for c in ("malaysia", "singapore")]
(out / "sea_my_sg_stroke.svg").write_text(hdr(W, H) + "".join(
    f'<path d="{x}" fill="#f0efe8" fill-opacity="0.10" stroke="#f0efe8" stroke-opacity="0.7" stroke-width="5" stroke-linejoin="round"/>' for x in ds) + "</svg>")
print("ok")
