"""Builds index.html as a sample reel: each sample sub-composition back to back with a short black gap.
Usage: python3 tools/build_index.py [sample ids...]   (default: every sample listed below)"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
import sys as _s
if "--root" in _s.argv:
    _i = _s.argv.index("--root"); ROOT = pathlib.Path(_s.argv[_i + 1]).resolve(); del _s.argv[_i:_i + 2]
GAP = 0.5
SAMPLES = [  # id, file, duration
    ("s01", "compositions/s01-trillion.html", 6.8),
    ("s02", "compositions/s02-map.html", 10.0),
    ("s03", "compositions/s03-gdp.html", 9.6),
    ("s04", "compositions/s04-tv.html", 10.2),
    ("s05", "compositions/s05-brain-drain.html", 8.0),
    ("s06", "compositions/s06-newspaper.html", 8.4),
    ("s07", "compositions/s07-hoover-1891.html", 10.0),
    ("s08", "compositions/s08-collage.html", 9.6),
    ("s09", "compositions/s09-vox-cutout.html", 6.2),
    ("s10", "compositions/s10-garage-25d.html", 7.0),
    ("s11", "compositions/s11-markup.html", 7.9),
]

want = set(sys.argv[1:])
import re as _re, glob as _glob
for _f in sorted(_glob.glob(str(ROOT / "compositions/*.html"))):
    _src = open(_f).read()
    _m = _re.search(r'data-composition-id="((?:seg|intro|ivs|pys|c\d+s)\d+)"[^>]*data-duration="([\d.]+)"', _src)
    if _m:
        SAMPLES.append((_m.group(1), "compositions/" + _f.split("/")[-1], float(_m.group(2))))
items = [s for s in SAMPLES if (not want or s[0] in want) and (ROOT / s[1]).exists()]
t = 0.0
hosts, plan = [], []
for sid, src, dur in items:
    hosts.append(f'''    <div id="{sid}-host" data-composition-id="{sid}" data-composition-src="{src}"
      data-start="{t:.3f}" data-duration="{dur}" data-track-index="1" data-width="1920" data-height="1080"></div>''')
    plan.append({"id": sid, "start": round(t, 3), "duration": dur})
    t += dur + GAP
total = round(t - GAP, 3)

import os as _os
PALETTE = _os.environ.get('PALETTE') or ('lib/palette_ivan.css' if any(a.startswith('iv') for a in sys.argv[1:]) else 'lib/palette_paraguay.css' if any(a.startswith('py') for a in sys.argv[1:]) else 'lib/palette_podcast.css' if any(a.startswith('pd') for a in sys.argv[1:]) else 'lib/palette.css')  # per-video palette (Ivan = iv*)
html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link rel="stylesheet" href="lib/fx.css" />
    <link rel="stylesheet" href="{PALETTE}" />
    <script src="lib/fx.js"></script>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080" data-fps="24">
{chr(10).join(hosts)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
(ROOT / "index.html").write_text(html)
(ROOT / "reel_plan.json").write_text(json.dumps(plan, indent=1))
print(json.dumps(plan), "total", total)
