"""nvs10 derived assets: US night crop around Memphis + state/river overlay + Tennessee fill, Colossus aerial inset crop."""
import re
from PIL import Image
K = 'assets/maps/kit/'
OUT = 'assets/nvidia/nvs10/derived/'
X0, Y0, W, H = 2000, 600, 3600, 2500          # crop of us_night (6392x3524 px space)
Image.open(K + 'us_night.jpg').crop((X0, Y0, X0 + W, Y0 + H)).save(OUT + 'us_night_memphis.jpg', quality=88)
svg = open(K + 'us_overlay.svg').read()
def group(name):
    m = re.search(r'<g id="%s">(.*?)</g>' % name, svg, re.S)
    return m.group(1) if m else ''
tn = re.search(r'<path id="st-tennessee"[^>]*d="([^"]+)"', svg).group(1)
o = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" width="%d" height="%d">' % (X0, Y0, W, H, W, H) +
     '<g fill="none" stroke="#f0efe8" stroke-opacity="0.38" stroke-width="2.4">' + group('us_states') + '</g>' +
     '<g fill="none" stroke="#9fdcf0" stroke-opacity="0.55" stroke-width="3">' + group('rivers') + '</g>'
     '<g fill="none" stroke="#f0efe8" stroke-opacity="0.6" stroke-width="3">' + group('countries') + '</g></svg>')
o = re.sub(r'<circle[^>]*/>', '', o)
open(OUT + 'us_memphis_overlay.svg', 'w').write(o)
open(OUT + 'tennessee_fill.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" width="%d" height="%d"><path d="%s" fill="#2a9fc9" fill-opacity="0.38" stroke="#9fdcf0" stroke-width="5"/></svg>' % (X0, Y0, W, H, W, H, tn))
a = Image.open(K + 'aerial_memphis_xai_colossus_z16.jpg')
a.crop((1406 - 800, 1358 - 600, 1406 + 800, 1358 + 600)).save(OUT + 'colossus_aerial_inset.jpg', quality=88)
print('memphis in crop px', (-90.05 + 126) * 106.533 - X0, (50 - 35.15) * 133 - Y0)
