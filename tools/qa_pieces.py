#!/usr/bin/env python3
"""QA for rendered podcast pieces: frame count vs sections.json, black/near-black frames, frozen runs, and a contact sheet with
the spoken words under each frame (MANUAL §9 / §10.1.3).  usage: qa_pieces.py renders/pieces/pd04.mp4 [...]  -> work/qa/<id>_sheet.jpg"""
import json, os, subprocess, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
S = {s['id']: s for s in json.load(open('project/podcast/sections.json'))['sections']}
T = json.load(open('transcript_pd.json')); os.makedirs('work/qa', exist_ok=True)
F = ImageFont.truetype('assets/fonts/CooperHewitt-Semibold.otf', 15)
for p in sys.argv[1:]:
    sid = os.path.basename(p).split('.')[0]; s = S[sid]; N = round(s['dur'] * 30)
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', 'scale=96:54', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, 54, 96).astype(np.int16); n = len(fr)
    mean = fr.reshape(n, -1).mean(1); black = np.where(mean < 6)[0]
    diff = np.abs(np.diff(fr, axis=0)).reshape(n - 1, -1).mean(1); still = diff < 0.15
    runs = []; k = 0
    while k < len(still):
        if still[k]:
            j = k
            while j < len(still) and still[j]: j += 1
            if j - k >= 45: runs.append((round(k / 30, 2), round(j / 30, 2)))
            k = j
        else: k += 1
    print(f"{sid}: frames {n} (slot {N}) {'OK' if n == N else '!! MISMATCH'} | black frames {len(black)} {list(black[:8])} | frozen ≥1.5 s: {runs}")
    times = np.linspace(0.2, s['dur'] - 0.1, 12); W, H = 480, 270; sheet = Image.new('RGB', (W * 4, (H + 44) * 3), (16, 16, 16)); d = ImageDraw.Draw(sheet)
    for i, t in enumerate(times):
        img = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', p, '-frames:v', '1', '-vf', f'scale={W}:{H}', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        from io import BytesIO
        im = Image.open(BytesIO(img)).convert('RGB'); x, y = (i % 4) * W, (i // 4) * (H + 44); sheet.paste(im, (x, y))
        m = s['start'] + t; words = ' '.join(w['text'] for w in T if m - 2.0 <= w['start'] <= m + 0.3)
        d.text((x + 4, y + H + 2), f"{m:.1f}s  …{words[-62:]}", font=F, fill=(240, 230, 120))
    sheet.save(f'work/qa/{sid}_sheet.jpg', quality=82)
