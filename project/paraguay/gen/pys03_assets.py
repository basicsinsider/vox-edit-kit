"""pys03 derived assets: world crop (night) + region overlays, Paraguay night crop + fill overlay.
Run: .venv/bin/python project/paraguay/gen/pys03_assets.py   (from the repo root)"""
import re, pathlib
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = pathlib.Path("assets/maps/kit"); OUT = pathlib.Path("assets/paraguay/pys03/derived"); OUT.mkdir(parents=True, exist_ok=True)
P = 45.5111
# ---- world crop: lon -125..145, lat 78..-74 (16:9)
x0, x1 = (-125 + 180) * P, (145 + 180) * P
y0 = (90 - 78) * P; y1 = y0 + (x1 - x0) * 9 / 16
print("world crop px", x0, y0, x1, y1)
w = Image.open(K / "world_night.jpg").crop((round(x0), round(y0), round(x1), round(y1))).resize((3840, 2160), Image.LANCZOS)
w.save(OUT / "world_night_crop.jpg", quality=90)
src = (K / "world_overlay.svg").read_text()
paths = dict(re.findall(r'<path id="c-([a-z_]+)"[^>]*?d="([^"]+)"', src))
def clean(d):
    out = []
    for sp in re.split(r"(?=M)", d):
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]
        pts = list(zip(nums[0::2], nums[1::2]))
        if not pts: continue
        if any(abs(a[0] - b[0]) > 400 for a, b in zip(pts, pts[1:])): continue
        if max(p[0] for p in pts) < x0 - 50 or min(p[0] for p in pts) > x1 + 50: continue
        keep = [pts[0]]
        for q in pts[1:]:
            if abs(q[0] - keep[-1][0]) + abs(q[1] - keep[-1][1]) >= 6: keep.append(q)
        if len(keep) < 4: continue
        out.append("M" + "L".join(f"{a:.0f},{b:.0f}" for a, b in keep) + "Z")
    return "".join(out)
G = {
  "asia": ["south_korea", "japan", "india", "indonesia", "thailand", "philippines", "malaysia"],
  "southam": ["brazil", "chile", "colombia", "argentina", "peru", "ecuador", "venezuela", "uruguay", "bolivia"],
  "mideast": ["saudi_arabia", "united_arab_emirates", "kuwait", "qatar", "lebanon", "oman", "bahrain", "jordan"],
  "us": ["united_states_of_america"],
  "paraguay": ["paraguay"],
}
STY = {"asia": 'fill="#93e0d3" fill-opacity="0.55" stroke="#93e0d3" stroke-width="7"',
       "southam": 'fill="#93e0d3" fill-opacity="0.55" stroke="#93e0d3" stroke-width="7"',
       "mideast": 'fill="#93e0d3" fill-opacity="0.55" stroke="#93e0d3" stroke-width="7"',
       "us": 'fill="#c3c7c1" fill-opacity="0.22" stroke="#c3c7c1" stroke-width="6" stroke-opacity="0.8"',
       "paraguay": 'fill="#cf5a33" fill-opacity="0.8" stroke="#f1b296" stroke-width="7"'}
vb = f"{x0:.1f} {y0:.1f} {x1-x0:.1f} {y1-y0:.1f}"
allc = "".join(f'<path d="{clean(d)}"/>' for k, d in paths.items() if k != "antarctica")
(OUT / "world_borders.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="3840" height="2160"><g fill="none" stroke="#f2eee3" stroke-opacity="0.32" stroke-width="5">{allc}</g></svg>')
for g, ids in G.items():
    body = "".join(f'<path d="{clean(paths[i])}"/>' for i in ids)
    (OUT / f"world_{g}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="3840" height="2160"><g {STY[g]} stroke-linejoin="round">{body}</g></svg>')
# ---- Paraguay night, half res + overlay (same 0.5 space)
py = Image.open(K / "paraguay_night.jpg"); py.resize((2568, 2520), Image.LANCZOS).save(OUT / "paraguay_night_half.jpg", quality=90)
ps = (K / "paraguay_overlay.svg").read_text()
pp = dict(re.findall(r'<path id="c-([a-z_]+)"[^>]*?d="([^"]+)"', ps))
riv = dict(re.findall(r'<path id="river-([a-z_]+)"[^>]*?d="([^"]+)"', ps))
bor = "".join(f'<path d="{pp[k]}"/>' for k in ["brazil", "argentina", "bolivia"])
rv = "".join(f'<path d="{riv[k]}"/>' for k in ["paraguay", "parana", "pilcomayo"] if k in riv)
(OUT / "paraguay_overlay_pys03.svg").write_text(
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5136 5040" width="2568" height="2520">'
  f'<g fill="none" stroke="#9fc3e3" stroke-opacity="0.5" stroke-width="5">{rv}</g>'
  f'<g fill="none" stroke="#f2eee3" stroke-opacity="0.4" stroke-width="4">{bor}</g>'
  f'<path d="{pp["paraguay"]}" fill="#cf5a33" fill-opacity="0.55" stroke="#f1b296" stroke-width="6" stroke-linejoin="round"/></svg>')
print("ok")
