"""Builds master.html: every compositions/segNN.html mounted at its voiceover start, one continuous
voiceover track, plus the sound designer's tracks (assets/audio/timeline.json, optional).

Segment contract (see SEGMENTS.md): the segment root div carries
  data-composition-id="segNN" data-vo-start="<VO seconds>" data-duration="<seconds>"
and the segment contains NO voiceover <audio> of its own.

assets/audio/timeline.json (written by the sound designer):
  [{"id": "mus-01", "src": "assets/audio/music/x.wav", "start": 0.0, "duration": 95.2,
    "media_start": 0.0, "volume": 0.18}, ...]
Usage: python3 tools/build_master.py [--out master.html] [--prefix seg] [--vo vo10.mp3] [--len 600] [--timeline assets/audio/timeline.json]
  e.g. intro: --prefix intro --vo vo_intro.mp3 --len 275.06 --timeline assets/audio/intro/timeline.json --out intro.html
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "master.html"
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
PREFIX, VO, VO_LEN = arg("--prefix", "seg"), arg("--vo", "vo10.mp3"), float(arg("--len", "600"))
TL = arg("--timeline", "assets/audio/timeline.json")

segs = []
for f in sorted((ROOT / "compositions").glob(f"{PREFIX}*.html")):
    src = f.read_text()
    m = re.search(rf'data-composition-id="({PREFIX}\d+)"[^>]*', src)
    if not m:
        continue
    tag = m.group(0)
    vs = re.search(r'data-vo-start="([\d.]+)"', tag)
    du = re.search(r'data-duration="([\d.]+)"', tag)
    if not (vs and du):
        sys.exit(f"{f.name}: root needs data-vo-start and data-duration")
    # strip the editor's temporary voiceover slice; the master plays one continuous VO
    clean = re.sub(r'<audio[^>]*class="temp-vo"[^>]*>\s*</audio>', "", src)
    gen = ROOT / "compositions/_master"
    gen.mkdir(exist_ok=True)
    (gen / f.name).write_text(clean)
    segs.append((m.group(1), f"compositions/_master/{f.name}", float(vs.group(1)), float(du.group(1))))

segs.sort(key=lambda s: s[2])
hosts = "\n".join(
    f'      <div id="{sid}-host" data-composition-id="{sid}" data-composition-src="{src}" data-start="{st:.3f}" '
    f'data-duration="{du:.3f}" data-track-index="1" data-width="1920" data-height="1080"></div>'
    for sid, src, st, du in segs)

tracks = []
tl = ROOT / TL
if tl.exists():
    for i, t in enumerate(json.loads(tl.read_text())):
        tracks.append(
            f'      <audio id="{t["id"]}" src="{t["src"]}" data-start="{t["start"]:.3f}" data-duration="{t["duration"]:.3f}" '
            f'data-media-start="{t.get("media_start", 0):.3f}" data-volume="{t.get("volume", 0.2)}" data-track-index="{6 + (i % 6)}"></audio>')

total = max([VO_LEN] + [s[2] + s[3] for s in segs])
import os as _os
PALETTE = _os.environ.get('PALETTE') or ('lib/palette_ivan.css' if any(a.startswith('iv') for a in sys.argv[1:]) else 'lib/palette_paraguay.css' if any(a.startswith('py') for a in sys.argv[1:]) else 'lib/palette_podcast.css' if any(a.startswith('pd') for a in sys.argv[1:]) else 'lib/palette_nvidia.css' if any(a.startswith('nv') for a in sys.argv[1:]) else 'lib/palette.css')  # per-video palette (Ivan = iv*)
NV_MOTIFS = ('\n    <link rel="stylesheet" href="lib/nv_motifs.css" />\n    <script src="lib/nv_motifs.js"></script>'
             if any(a.startswith('nv') for a in sys.argv[1:]) else '')  # NVIDIA motifs (MOTIFS.md) for nv* compositions
html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link rel="stylesheet" href="lib/fx.css" />
    <link rel="stylesheet" href="{PALETTE}" />
    <script src="lib/fx.js"></script>{NV_MOTIFS}
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="1920" data-height="1080" data-fps="24">
{hosts}
      <audio id="vo-main" src="{VO}" data-start="0" data-duration="{VO_LEN}" data-media-start="0" data-volume="1" data-track-index="5"></audio>
{chr(10).join(tracks)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
(ROOT / out).write_text(html)
gaps = [(a[2] + a[3], b[2]) for a, b in zip(segs, segs[1:]) if b[2] - (a[2] + a[3]) > 0.05]
print(f"wrote {out}: {len(segs)} segments, {len(tracks)} audio tracks, {total:.2f}s; gaps: {gaps or 'none'}")
