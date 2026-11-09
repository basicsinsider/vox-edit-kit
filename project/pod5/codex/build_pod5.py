#!/usr/bin/env python3
"""Rebuild isolated picture-preview and frame-aligned render wrappers for pod5."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
SCENES = [('pod5opening',0,8),('pod5fab',8,9.6),('pod5export',17.6,19.12),('pod5umc',36.72,18.75),('pod5foundry',55.47,40.72),('pod5board',96.19,33.55),('pod5advisor',129.74,62.59),('pod5dialogue',192.33,67.87),('pod5reversal',260.2,38.8)]
GROUPS = [SCENES[:5]+[('pod5board',96.19,33.56)], [('pod5advisor',0,62.58),('pod5dialogue',62.58,67.87),('pod5reversal',130.45,38.8)]]
assert all(abs(a[1]+a[2]-b[1])<1e-7 for a,b in zip(SCENES,SCENES[1:]))
def make(name, scenes, duration, voice=False):
 d=ROOT/'work'/name;(d/'compositions').mkdir(parents=True,exist_ok=True)
 for item in ('assets','lib','input'):
  p=d/item
  if not p.exists(): p.symlink_to('../../'+item,target_is_directory=True)
 for n,_,_ in scenes:
  p=d/'compositions'/f'{n}.html'
  if not p.exists():p.symlink_to(f'../../../compositions/{n}.html')
 hosts='\n'.join(f'<div id="{n}" data-composition-id="{n}" data-composition-src="compositions/{n}.html" data-start="{t}" data-duration="{length}" data-track-index="1" data-width="1920" data-height="1080"></div>' for n,t,length in scenes)
 audio='<audio id="pod5-voice" src="input/BB_podcast_v2_first5min.mp4" data-start="0" data-duration="299" data-volume="1"></audio>' if voice else ''
 html='''<!doctype html><html><head><meta charset="utf-8"><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><link rel="stylesheet" href="lib/fx.css"><link rel="stylesheet" href="lib/palette.css"><script src="lib/fx.js"></script></head><body><div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="'''+str(duration)+'''" data-fps="24">'''+hosts+audio+'''</div><script>window.__timelines.main=gsap.timeline({paused:true});</script></body></html>'''
 (d/'index.html').write_text(html)
make('pod5master',SCENES,299,True)
make('pod5render01',GROUPS[0],129.75)
make('pod5render02',GROUPS[1],169.25)
print('Built master and two 24 fps frame-aligned render wrappers')
