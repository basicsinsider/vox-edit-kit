"""nvs07 derived map overlays (pacific kit pixel space 6380x2420): borders, China fill, US fill."""
import re, os
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/../../.."
src = open(ROOT + "/assets/maps/kit/pacific_overlay.svg").read()
out = ROOT + "/assets/nvidia/nvs07/derived/"
def path(cid):
    return re.search(r'<path[^>]*id="%s"[^>]*d="([^"]+)"' % cid, src).group(1)
g = re.search(r'<g id="countries">(.*?)</g>', src, re.S).group(1)
head = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6380 2420" width="6380" height="2420">'
open(out + "pacific_borders.svg", "w").write(head + '<g fill="none" stroke="#f0efe8" stroke-width="2.4" stroke-opacity="0.5" stroke-linejoin="round">' + re.sub(r'\s(id|data-name)="[^"]*"', "", g) + "</g></svg>")
open(out + "pacific_china_fill.svg", "w").write(head + '<path fill-rule="evenodd" fill="#dc2f3c" fill-opacity="0.5" stroke="#f6a4a9" stroke-width="4" stroke-linejoin="round" d="%s"/></svg>' % path("c-china"))
open(out + "pacific_us_fill.svg", "w").write(head + '<path fill-rule="evenodd" fill="#2a9fc9" fill-opacity="0.38" stroke="#9fdcf0" stroke-width="4" stroke-linejoin="round" d="%s"/></svg>' % path("c-united_states_of_america"))
for f in os.listdir(out): print(f, os.path.getsize(out + f))
