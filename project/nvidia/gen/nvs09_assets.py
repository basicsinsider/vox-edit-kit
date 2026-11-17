"""nvs09 derived assets: China fill/stroke SVGs in the china_* map-kit pixel space (6383x4368)."""
import re, pathlib
R = pathlib.Path(__file__).resolve().parents[3]
src = (R / "assets/maps/kit/china_overlay.svg").read_text()
m = re.search(r'<path[^>]*id="c-china"[^>]*>', src)
d = re.search(r'\sd="([^"]+)"', m.group(0)).group(1)
out = R / "assets/nvidia/nvs09/derived"
out.mkdir(parents=True, exist_ok=True)
W, H = 6383, 4368
hdr = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
(out / "china_fill.svg").write_text(hdr + f'<path d="{d}" fill="#dc2f3c" fill-rule="evenodd"/></svg>')
(out / "china_stroke.svg").write_text(hdr + f'<path d="{d}" fill="none" stroke="#f6a4a9" stroke-width="7" stroke-linejoin="round"/></svg>')
print("ok", len(d))
