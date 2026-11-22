"""US vs Cartels — fix round 1: apply project/cartels/fix1_ops.json (Agent V) to the audio side. Copy of tools/nv_fix_remap.py.
  work/fix1/vo_v2.wav              VO on the new timeline WITHOUT preroll (48 kHz mono float32; samples copied untouched except
                                   the joins: each `del` crossfades `xfade` s (equal power) across the join, the crossfade audio taken
                                   from the removed span so exactly `del` s go; each `ins` = raw VO src span with 6 ms fades, butt-joined)
  work/fix1/vo_v2_master.wav       (preroll > 0) the same VO with P s of digital silence in front = master v2 time (for place_sound)
  work/fix1/transcript_v2.json     word times remapped on MASTER v2 (with preroll: matches vo_v2_master.wav and the picture)
  work/fix1/transcript_v2_vo.json  word times remapped without preroll (matches vo_v2.wav)
  work/fix1/sfx/ctsNN.sfx.json     editors' SFX markers remapped (with preroll: master v2 seconds); cts00 (already v2) copied
  work/fix1/music_cuesheet_v2.json cue sheet: layers start/end/auto, stingers, marker_edits, ducks/bleeps remapped (with preroll), length = v2
  work/fix1/map.json               v1/v2 lengths, preroll, the ops
Map: v2 = preroll + map(v1); map shifts every time after a `del` by -del (a time inside a deleted span lands on its start), after an
`ins` by +ins (a time exactly at the insert point moves after it). Picture and audio use the same spans in this round.
Usage: .venv/bin/python tools/ct_fix_remap.py [--preroll P]   (default: fix1_ops.json "preroll")
Library: from ct_fix_remap import load_ops, mapper, render_vo"""
import json, glob, os, sys, numpy as np, soundfile as sf
FPS = 24; SR = 48000
OPS = 'project/cartels/fix1_ops.json'; VO1 = 'project/cartels/media/vo_ct.wav'; RAW = 'input/vo_raw.wav'
V1_LEN = 32206 / FPS   # master timeline v1 = the delivered 720p, 32206 frames (segments.json says 1341.912; the VO wav is 1341.870 s)

def load_ops(path=OPS):
    J = json.load(open(path)); ops = sorted(J['ops'], key=lambda o: o['t'])
    for o in ops:
        L = o.get('del', o.get('ins')); fr = L * FPS
        assert abs(fr - round(fr)) < 1e-4, ('not whole frames', o)
        assert abs(o['t'] * FPS - round(o['t'] * FPS)) < 1e-4, ('t not on the frame grid', o)
        if 'ins' in o:
            a, b = map(float, o['src'].split('-')); assert abs((b - a) - o['ins']) < 1e-6, ('src length != ins', o)
    return J, ops

def mapper(ops, preroll=0.0):
    def M(t):
        s = 0.0
        for o in ops:
            if 'del' in o:
                if t >= o['t'] + o['del']: s -= o['del']
                elif t > o['t']: return preroll + o['t'] + s
            else:
                if t >= o['t']: s += o['ins']
        return preroll + t + s
    return M

def _xcut(parts, x, a, b, nx):
    """append x[:a] handled by caller; returns crossfade block between x[a:a+nx] (out) and x[b:b+nx] (in)"""
    th = np.linspace(0, np.pi / 2, nx, dtype=np.float64)
    return (x[a:a + nx] * np.cos(th) + x[b:b + nx] * np.sin(th)).astype(np.float32)

def render_vo(x, ops, raw=None, t0=0.0):
    """x = v1 VO samples starting at v1 time t0 (float32 mono). Returns the v2 samples. Ops outside x are ignored."""
    out = []; pos = 0; n = len(x)
    for o in ops:
        a = round((o['t'] - t0) * SR)
        if a < 0 or a > n: continue
        if 'del' in o:
            b = a + round(o['del'] * SR); nx = max(1, round(o.get('xfade', 0.006) * SR))
            if b + nx > n: continue
            out.append(x[pos:a]); out.append(_xcut(out, x, a, b, nx)); pos = b + nx
        else:
            if raw is None: raw = sf.read(RAW, dtype='float32')[0]
            s0, s1 = map(float, o['src'].split('-')); seg = raw[round(s0 * SR):round(s0 * SR) + round(o['ins'] * SR)].copy()
            fd = round(0.006 * SR); r = np.linspace(0, 1, fd, dtype=np.float32)
            seg[:fd] *= r; seg[-fd:] *= r[::-1]
            pre = x[pos:a].copy(); post_fade = min(fd, n - a)
            if len(pre) >= fd: pre[-fd:] *= r[::-1]
            out.append(pre); out.append(seg)
            nxt = x[a:a + post_fade].copy() * r[:post_fade]; out.append(nxt); pos = a + post_fade
    out.append(x[pos:])
    return np.concatenate(out)

def main():
    J, ops = load_ops()
    P = float(sys.argv[sys.argv.index('--preroll') + 1]) if '--preroll' in sys.argv else float(J.get('preroll', 0))
    assert abs(P * FPS - round(P * FPS)) < 1e-6, 'preroll must be whole frames'
    M0 = mapper(ops, 0.0); MP = mapper(ops, P)
    dl = sum(o.get('del', 0) for o in ops); il = sum(o.get('ins', 0) for o in ops)
    NEW = round(round((V1_LEN - dl + il) * FPS) / FPS, 6); NEW_P = round(P + NEW, 6)   # whole frames
    os.makedirs('work/fix1/sfx', exist_ok=True)
    x, sr = sf.read(VO1, dtype='float32'); assert sr == SR and x.ndim == 1
    y = render_vo(x, ops)
    exp = len(x) - sum(round(o['del'] * SR) for o in ops if 'del' in o) + sum(round(o['ins'] * SR) for o in ops if 'ins' in o)
    assert len(y) == exp, (len(y), exp)
    sf.write('work/fix1/vo_v2.wav', y, SR, subtype='FLOAT')
    print(f'VO {len(x) / SR:.3f} -> {len(y) / SR:.3f} s (removed {dl:.3f}, inserted {il:.3f}); master v1 {V1_LEN} -> v2 {NEW} (+preroll {P} = {NEW_P})')
    if P:   # master-timeline VO for place_sound / measuring: P s of digital silence + vo_v2 (samples otherwise identical)
        sf.write('work/fix1/vo_v2_master.wav', np.concatenate([np.zeros(round(P * SR), np.float32), y]), SR, subtype='FLOAT')
    for name, Mx in (('transcript_v2.json', MP), ('transcript_v2_vo.json', M0)):
        W = json.load(open('transcript_ct.json'))
        for w in W: w['start'] = round(Mx(w['start']), 3); w['end'] = round(max(Mx(w['end']), Mx(w['start'])), 3)
        json.dump(W, open('work/fix1/' + name, 'w'), ensure_ascii=False)
    n = 0
    for f in sorted(glob.glob('compositions/cts[0-9][0-9].sfx.json')):
        m = json.load(open(f))
        if os.path.basename(f).startswith('cts00'):   # the cold open's markers are already on v2 time (Agent A): copied as they are
            json.dump(m, open('work/fix1/sfx/' + os.path.basename(f), 'w'), indent=1, ensure_ascii=False); continue
        for e in m:
            e['t'] = round(MP(e['t']), 4); n += 1
            if e.get('dur'): pass   # durations kept (a sustained sfx over a 0.1–0.4 s cut is harmless)
        json.dump(m, open('work/fix1/sfx/' + os.path.basename(f), 'w'), indent=1, ensure_ascii=False)
    cs = json.load(open('project/cartels/music_cuesheet.json'))
    cs['length'] = NEW_P
    cs['doc'] = cs.get('doc', '') + f' | REMAPPED to master v2 by tools/ct_fix_remap.py (fix round 1, preroll {P} s): edit the v1 sheet + rerun.'
    for L in cs['layers']:
        L['start'] = round(MP(L['start']), 4); L['end'] = round(MP(L['end']), 4)
        if 'auto' in L: L['auto'] = [[round(MP(t), 4), v] for t, v in L['auto']]
    for key in ('stingers', 'marker_edits', 'ducks', 'bleeps'):
        for d in cs.get(key, []):
            for k in ('t', 'start', 'end'):
                if k in d: d[k] = round(MP(d[k]), 4)
    json.dump(cs, open('work/fix1/music_cuesheet_v2.json', 'w'), indent=1, ensure_ascii=False)
    json.dump({'v1_len': V1_LEN, 'preroll': P, 'new_len_no_preroll': NEW, 'new_len': NEW_P, 'new_frames': round(NEW_P * FPS, 6),
               'vo_v2_len': len(y) / SR, 'total_del': round(dl, 6), 'total_ins': round(il, 6), 'ops': ops},
              open('work/fix1/map.json', 'w'), indent=1, ensure_ascii=False)
    print('markers', n, 'layers', len(cs['layers']), 'stingers', len(cs.get('stingers', [])), f'new master {NEW_P} s =', round(NEW_P * FPS, 3), 'frames')

if __name__ == '__main__': main()
