"""US vs Cartels — fix round 1 (Frame.io review 2026-11-22): choose the VO timeline ops on master timeline v1
(project/cartels/media/vo_ct.wav = transcript_ct.json times = the delivered 720p) and write project/cartels/fix1_ops.json.
Copy of tools/nv_fix_cuts.py, extended:
  * PAUSES: every true silence run (10 ms RMS < -55 dBFS, >= 0.30 s) is shortened to a natural breath, by what precedes it
    (Parakeet punctuation): sentence end -> 0.36 s, comma -> 0.28 s, mid-phrase -> 0.22 s of silence left (perceived pause
    ≈ +0.1 s of word decay). Only removals of >= 3 frames. The deletion stays >= 60 ms inside the run after the word's decay
    and >= 80 ms before the next onset. Position on the 24 fps grid = minimum visual jump on the delivered 720p
    (frames of the delivered v1 720p decoded to work/fix1/v1_64.gray, 64x36 gray — the 720p itself has since been deleted).
  * MANUAL ops (review notes): #4 repeated "and he controls the routes," deleted silence-to-silence; #12 the over-long /s/ of
    "gets" (380 ms of sibilance in the RAW take — not an edit) shortened by 5 frames with a crossfade inside the fricative.
  * EXCLUDE: candidates the ASR window check (tools/ct_fix_check.py, Parakeet + Whisper, ±3 s with vs without) rejected.
Every op: t = first deleted v1 instant (k/24), del = n/24; the audio side crossfades 6 ms across each join (xfade taken from
the deleted span, so the length removed is exactly del). Picture: the same frames are deleted.
Usage: .venv/bin/python tools/ct_fix_cuts.py [--cands]   (--cands: also write work/fix1/cands.json for the check)"""
import json, sys, numpy as np, soundfile as sf
FPS = 24; SR = 48000
PREROLL = 108 / FPS   # cold open cts00 (Agent A, lead 2026-11-22): 4.5 s = 108 frames, its own audio cold_open_audio.wav
VO = 'project/cartels/media/vo_ct.wav'; FR = 'work/fix1/v1_64.gray'; V1_FRAMES = 32206
TH = -55.0; MINRUN = 0.30; M_PRE, M_POST = 0.06, 0.08; MIN_FR = 3
JUMP_MAX = 15.0   # a pause that sits entirely inside a fast picture move / whip / title transition is left alone (cutting
                  # 4–11 frames out of a 12-frame whip or a title-card reveal shows; 7 such pauses on v1)
TARGET = {'end': 0.36, 'comma': 0.28, 'none': 0.22}
# --- review-note ops (v1 seconds; t on the frame grid) ---
MANUAL = [
    dict(t=5535 / FPS, n=50, kind='repeat', note='#4 Sam 3:56 "cut out the repeat sentence": deletes the 1st "and he controls the routes," '
         '(from the 0.1 s dip after "Sinaloa" 230.60–230.70 → the silence before the 2nd "and" 232.59–232.88); keeps "…north of Sinaloa '
         'and he controls the routes into Sonora". (A first try from the silence AFTER the 1st "and" left "and and" — Parakeet check.)'),
    dict(t=14352 / FPS, n=7, kind='noise', note='#18 Sanket 9:59 "audio needs to be cleaned up here too": a 160 ms voiced mouth sound / '
         'aborted syllable (598.06–598.22, −36 dBFS, periodic, no word for Parakeet or Whisper) in the pause "…work with anybody. ⟨x⟩ As long as…"; '
         'removed with its decay (598.000–598.292), 0.39 s of pause left'),
    dict(t=5162 / FPS, n=5, kind='fricative', note='#12 Sanket 3:35 "gets said weirdly": raw take (no edit within 8 s) holds a 380 ms /s/ '
         '(215.00–215.38, ZCR 7 kHz); 5 frames of the steady hiss removed with a 10 ms crossfade → 170 ms /s/', xfade=0.010),
]
# --- candidates rejected by the ASR window check (v1 run start -> reason) ---
EXCLUDE = {}

def db10():
    x, sr = sf.read(VO, dtype='float32'); assert sr == SR
    h = SR // 100; n = len(x) // h
    return 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
def runs(D):
    s = D < TH; R = []; st = None
    for i, q in enumerate(list(s) + [False]):
        if q and st is None: st = i
        if not q and st is not None:
            if (i - st) / 100 >= MINRUN: R.append((st / 100, i / 100))
            st = None
    return R
W = json.load(open('transcript_ct.json'))
def around(a, b):
    p = [w for w in W if w['start'] < a + 0.05]; n = [w for w in W if w['start'] >= a + 0.05]
    return (p[-1]['text'] if p else ''), (n[0]['text'] if n else ''), ' '.join(w['text'] for w in p[-4:]) + ' | ' + ' '.join(w['text'] for w in n[:4])
def cls(prev): return 'end' if prev[-1:] in '.?!' else 'comma' if prev[-1:] in ',;:' else 'none'
F = np.fromfile(FR, np.uint8).reshape(-1, 36, 64).astype(np.float32); assert len(F) == V1_FRAMES, len(F)
def d(i, j): return float(np.abs(F[i] - F[j]).mean())
def best_pos(f_lo, f_hi, n):
    """delete frames [f, f+n) with f_lo <= f and f+n <= f_hi: minimise the jump between frame f-1 and frame f+n"""
    best = None
    for f in range(f_lo, f_hi - n + 1):
        seg = [d(k, k + 1) for k in range(f - 1, f + n)]; big = [k for k, j in enumerate(seg) if j > 12]
        if big:   # a shot change inside the deleted frames: cost = the two half-jumps around it
            c = f - 1 + big[0]; cost = d(f - 1, c) + d(c + 1, f + n)
        else: cost = d(f - 1, f + n)
        cost += 0.05 * abs((f + n / 2) - (f_lo + f_hi) / 2)   # tie-break: centre of the window
        if best is None or cost < best[0]: best = (cost, f)
    return best

def main():
    D = db10(); ops = []; cands = []
    man_spans = [(m['t'], m['t'] + m['n'] / FPS) for m in MANUAL]
    for m in MANUAL:
        f = round(m['t'] * FPS); p, nx, c = around(m['t'], m['t'] + m['n'] / FPS)
        ops.append(dict(t=round(f / FPS, 6), dele=m['n'] / FPS, frames=m['n'], kind=m['kind'], xfade=m.get('xfade', 0.006),
                        jump=round(d(f - 1, f + m['n']), 2), words=c, note=m['note']))
    for a, b in runs(D):
        if any(a < s1 and b > s0 for s0, s1 in man_spans): continue
        prev, nxt, c = around(a, b); k = cls(prev); T = TARGET[k]
        n = int(np.floor((b - a - T) * FPS + 1e-9))
        if n < MIN_FR: continue
        f_lo = int(np.ceil((a + M_PRE) * FPS)); f_hi = int(np.floor((b - M_POST) * FPS))
        n = min(n, f_hi - f_lo)
        if n < MIN_FR: continue
        key = round(a, 2)
        cost, f = best_pos(f_lo, f_hi, n)
        cand = dict(t=round(f / FPS, 6), dele=n / FPS, frames=n, kind='pause_' + k, xfade=0.006, run=[a, b], left=round(b - a - n / FPS, 3),
                    jump=round(cost, 2), words=c)
        cands.append(cand)
        if key in EXCLUDE: cand['excluded'] = EXCLUDE[key]; continue
        if cost > JUMP_MAX: cand['excluded'] = f'picture: pause inside a fast move/transition (jump {cost:.1f})'; continue
        ops.append(cand)
    ops.sort(key=lambda o: o['t'])
    for i in range(1, len(ops)): assert ops[i]['t'] >= ops[i - 1]['t'] + ops[i - 1]['dele'] + 1 / FPS, (ops[i - 1], ops[i])
    out = dict(doc='US vs Cartels fix round 1 — VO timeline ops on master v1 (Agent V, tools/ct_fix_cuts.py). v2 time = preroll + map(v1). '
               'del: v1 [t, t+del) removed from audio AND picture (whole frames, silence only except #12 fricative); '
               'ins: raw VO span src inserted at v1 t, picture frame held. Audio joins: crossfade xfade s taken from the removed span.',
               fps=FPS, preroll=PREROLL, v1_len=round(V1_FRAMES / FPS, 6), ops=[])
    for o in ops:
        e = dict(t=o['t'], **({'del': round(o['dele'], 6)}), frames=o['frames'], kind=o['kind'], xfade=o['xfade'], words=o['words'])
        for k in ('run', 'left', 'jump', 'note'):
            if k in o: e[k] = o[k]
        out['ops'].append(e)
    tot = sum(o['dele'] for o in ops); out['total_del'] = round(tot, 6); out['total_ins'] = 0.0
    out['v2_len_no_preroll'] = round(out['v1_len'] - tot, 6)
    json.dump(out, open('project/cartels/fix1_ops.json', 'w'), indent=1, ensure_ascii=False)
    if '--cands' in sys.argv: json.dump(cands, open('work/fix1/cands.json', 'w'), indent=1, ensure_ascii=False)
    from collections import Counter
    print(len(ops), 'ops', Counter(o['kind'] for o in ops), 'removed', round(tot, 3), 's; excluded', sum('excluded' in c for c in cands))
if __name__ == '__main__': main()
