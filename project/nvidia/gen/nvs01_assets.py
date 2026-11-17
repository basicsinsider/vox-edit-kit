"""nvs01 derived assets (run from repo root with .venv/bin/python):
- headline cards cropped from the REAL article captures in assets/nvidia/shared/news (no edits, crop only)
- map crops (pearl_river_delta, southeast_asia) + overlay/fill SVGs in the crop's pixel space
"""
import re
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = 'assets/maps/kit/'
N = 'assets/nvidia/shared/news/'
OUT = 'assets/nvidia/nvs01/derived/'
import os
os.makedirs(OUT, exist_ok=True)


def crop(src, box, out, q=90):
    im = Image.open(src).convert('RGB').crop(box)
    im.save(OUT + out, quality=q)
    print(out, im.size)


# --- headline cards (crop only) ---
crop(N + 's01_aljazeera.jpg', (20, 262, 1580, 700), 'card_aljazeera.jpg')       # headline + deck (stepped down / Chinese espionage)
crop(N + 's01_nbc.jpg', (110, 290, 2090, 810), 'card_nbc.jpg')                  # headline + deck on navy
crop(N + 's07_doj_sdny.jpg', (600, 860, 2620, 1362), 'card_doj_sdny.jpg')       # PRESS RELEASE · Three Charged … · date
crop(N + 's02_tomshw_megaspeed2b.jpg', (60, 150, 1262, 715), 'card_tomshw_megaspeed.jpg')

# --- Pearl River Delta crop ---
PX0, PY0, PW, PH = 2000, 1400, 2600, 2400
for v in ('satdesat', 'night'):
    Image.open(K + 'pearl_river_delta_%s.jpg' % v).crop((PX0, PY0, PX0 + PW, PY0 + PH)).save(OUT + 'prd_%s_crop.jpg' % v, quality=88)
svg = open(K + 'pearl_river_delta_overlay.svg').read()


def path_d(s, pid):
    m = re.search(r'<path id="%s"[^>]*?d="([^"]+)"' % pid, s)
    return m.group(1)


vb = 'viewBox="%d %d %d %d" width="%d" height="%d"' % (PX0, PY0, PW, PH, PW, PH)
open(OUT + 'prd_china_fill.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" %s><path d="%s" fill="#dc2f3c" fill-opacity="0.42" fill-rule="evenodd" stroke="#f6a4a9" stroke-opacity="0.8" stroke-width="5"/></svg>'
    % (vb, path_d(svg, 'c-china')))
open(OUT + 'prd_border.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" %s><path d="%s" fill="none" stroke="#f0efe8" stroke-opacity="0.75" stroke-width="5" stroke-dasharray="22 14"/></svg>'
    % (vb, path_d(svg, 'b-hk_mainland_border')))

# --- Southeast Asia crop ---
SX0, SY0, SW, SH = 0, 900, 5428, 5300
for v in ('night',):
    Image.open(K + 'southeast_asia_%s.jpg' % v).crop((SX0, SY0, SX0 + SW, SY0 + SH)).save(OUT + 'sea_%s_crop.jpg' % v, quality=86)
s2 = open(K + 'southeast_asia_overlay.svg').read()
vb2 = 'viewBox="%d %d %d %d" width="%d" height="%d"' % (SX0, SY0, SW, SH, SW, SH)
m = re.search(r'<g id="countries">(.*?)</g>', s2, re.S)
borders = re.sub(r'<circle[^>]*/>', '', m.group(1))
open(OUT + 'sea_borders.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" %s><g fill="none" stroke="#f0efe8" stroke-opacity="0.42" stroke-width="3">%s</g></svg>' % (vb2, borders))
open(OUT + 'sea_china_fill.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" %s><path d="%s" fill="#dc2f3c" fill-opacity="0.45" fill-rule="evenodd" stroke="#f6a4a9" stroke-opacity="0.85" stroke-width="6"/></svg>'
    % (vb2, path_d(s2, 'c-china')))
for c in ('malaysia', 'singapore'):
    open(OUT + 'sea_%s_line.svg' % c, 'w').write(
        '<svg xmlns="http://www.w3.org/2000/svg" %s><path d="%s" fill="#f0efe8" fill-opacity="0.10" fill-rule="evenodd" stroke="#f0efe8" stroke-opacity="0.95" stroke-width="7"/></svg>'
        % (vb2, path_d(s2, 'c-' + c)))
others = ''.join('<path d="%s"/>' % path_d(s2, 'c-' + c) for c in ('thailand', 'vietnam', 'indonesia', 'philippines', 'cambodia'))
open(OUT + 'sea_others_line.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" %s><g fill="#f0efe8" fill-opacity="0.06" fill-rule="evenodd" stroke="#f0efe8" stroke-opacity="0.7" stroke-width="5">%s</g></svg>'
    % (vb2, others))
print('done')
