"""US vs Cartels fix round 1 — ASR window check of EVERY op in project/cartels/fix1_ops.json (NVIDIA lesson: an RMS gate alone
is not enough). For each op: the v1 window [t-W, t+del+W] WITHOUT the op and the same window WITH only that op applied
(tools/ct_fix_remap.render_vo). All windows are concatenated with 1.5 s of digital silence between them into two files
(/dev/shm/fx/chk_{without,with}.wav) → one Parakeet run and one Whisper run each → words assigned back to their window →
the normalised word sequences compared per op. Any difference is printed (and saved to work/fix1/check_<engine>.json);
a real loss (fragment, clipped consonant, whispered word) is then excluded in tools/ct_fix_cuts.py EXCLUDE.
Long concatenations make Parakeet drop whole phrases now and then (seen on both files, not at the joins): every window flagged by
`compare` is re-checked ALONE with `single` (each window its own file, both engines) before a verdict.
Usage: .venv/bin/python tools/ct_fix_check.py build | asr parakeet|whisper | compare parakeet|whisper | single parakeet|whisper T1 T2 …
       [--ops other.json]"""
import json, os, re, sys, subprocess as sp, numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ct_fix_remap import load_ops, render_vo, SR
WIN = 3.0; GAP = 1.5; NEAR = 1.2; D = '/dev/shm/fx'
OPSF = sys.argv[sys.argv.index('--ops') + 1] if '--ops' in sys.argv else 'project/cartels/fix1_ops.json'
def norm(s): return re.sub(r"[^a-z0-9']", '', s.lower().replace('-', ''))

def build():
    J, ops = load_ops(OPSF); x = sf.read('project/cartels/media/vo_ct.wav', dtype='float32')[0]; raw = None
    gap = np.zeros(round(GAP * SR), np.float32); A, B, idx = [gap], [gap], []; pa = pb = GAP
    for i, o in enumerate(ops):
        L = o.get('del', 0); t0 = max(0, o['t'] - WIN); t1 = min(len(x) / SR, o['t'] + L + WIN)
        w = x[round(t0 * SR):round(t1 * SR)]
        if 'ins' in o and raw is None: raw = sf.read('input/vo_raw.wav', dtype='float32')[0]
        v = render_vo(w, [o], raw=raw, t0=t0)
        idx.append(dict(i=i, t=o['t'], a0=pa, a1=pa + len(w) / SR, b0=pb, b1=pb + len(v) / SR))
        A += [w, gap]; B += [v, gap]; pa += (len(w) + len(gap)) / SR; pb += (len(v) + len(gap)) / SR
    os.makedirs(D, exist_ok=True)
    for name, parts in (('without', A), ('with', B)):
        y = np.concatenate(parts); sf.write(f'{D}/chk_{name}.wav', y, SR, subtype='FLOAT')
        sp.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{D}/chk_{name}.wav', '-ar', '16000', '-c:a', 'pcm_s16le', f'{D}/chk_{name}16.wav'], check=True)
        os.remove(f'{D}/chk_{name}.wav'); print(name, round(len(y) / SR, 1), 's')
    json.dump(idx, open('work/fix1/check_index.json', 'w'), indent=0)

def asr(engine):
    for name in ('without', 'with'):
        od = f'work/fix1/chk_{engine}_{name}'; os.makedirs(od, exist_ok=True)
        r = sp.run(['nice', 'npx', '--yes', 'hyperframes@0.8.217', 'transcribe', f'{D}/chk_{name}16.wav', '--engine', engine, '-d', od, '--json'],
                   capture_output=True, text=True)
        print(engine, name, r.returncode, r.stdout.strip()[:200])

def words_in(T, a, b):
    return [w for w in T if a <= (w['start'] + w['end']) / 2 < b]

def compare(engine):
    idx = json.load(open('work/fix1/check_index.json')); J, ops = load_ops(OPSF)
    def ld(name):
        T = json.load(open(f'work/fix1/chk_{engine}_{name}/transcript.json')); return T['words'] if isinstance(T, dict) else T
    TA, TB = ld('without'), ld('with'); bad = []
    for e in idx:
        o = ops[e['i']]; c = max(0.0, o['t'] - WIN); ca = e['a0'] + o['t'] - c; L = o.get('del', 0); cb = e['b0'] + o['t'] - c
        # compare only the words within NEAR s of the join (window edges make ASR vary on its own)
        a = words_in(TA, max(e['a0'], ca - NEAR), min(e['a1'], ca + L + NEAR)); b = words_in(TB, max(e['b0'], cb - NEAR), min(e['b1'], cb + NEAR + o.get('ins', 0)))
        na = [norm(w['text']) for w in a]; nb = [norm(w['text']) for w in b]
        if na != nb:
            bad.append(dict(t=o['t'], kind=o['kind'], frames=o.get('frames'), words=o.get('words'),
                            without=' '.join(w['text'] for w in a), with_=' '.join(w['text'] for w in b)))
    json.dump(bad, open(f'work/fix1/check_{engine}.json', 'w'), indent=1, ensure_ascii=False)
    for b in bad: print(f"{b['t']:9.3f} {b['kind']:12s} {b['frames']}\n   without: {b['without']}\n   with:    {b['with_']}")
    print(engine, len(bad), 'of', len(idx), 'windows differ')

def single(engine, ts):
    J, ops = load_ops(OPSF); x = sf.read('project/cartels/media/vo_ct.wav', dtype='float32')[0]; res = []
    for T in ts:
        o = [o for o in ops if abs(o['t'] - T) < 0.01][0]; L = o.get('del', 0)
        t0 = max(0, o['t'] - WIN); t1 = min(len(x) / SR, o['t'] + L + WIN); w = x[round(t0 * SR):round(t1 * SR)]
        out = {}
        for name, y in (('without', w), ('with', render_vo(w, [o], t0=t0))):
            d = f'{D}/single/{engine}_{T:.3f}_{name}'; os.makedirs(d, exist_ok=True)
            sf.write(f'{d}/a.wav', np.concatenate([np.zeros(SR // 2, np.float32), y, np.zeros(SR // 2, np.float32)]), SR, subtype='FLOAT')
            sp.run(['nice', 'npx', '--yes', 'hyperframes@0.8.217', 'transcribe', f'{d}/a.wav', '--engine', engine, '-d', d, '--json'], capture_output=True)
            Tr = json.load(open(f'{d}/transcript.json')); Tr = Tr['words'] if isinstance(Tr, dict) else Tr
            out[name] = ' '.join(t['text'] for t in Tr)
        same = [norm(a) for a in out['without'].split()] == [norm(b) for b in out['with'].split()]
        print(f"{T:9.3f} {o['kind']:12s} {'SAME' if same else 'DIFF'}\n   without: {out['without']}\n   with:    {out['with']}", flush=True)
        res.append(dict(t=T, engine=engine, same=same, **out))
    f = f'work/fix1/single_{engine}.json'; old = json.load(open(f)) if os.path.exists(f) else []
    json.dump(old + res, open(f, 'w'), indent=1, ensure_ascii=False)

if __name__ == '__main__':
    if sys.argv[1] == 'single': single(sys.argv[2], [float(a) for a in sys.argv[3:] if not a.startswith('--') and a != OPSF]); sys.exit()
    {'build': build, 'asr': lambda: asr(sys.argv[2]), 'compare': lambda: compare(sys.argv[2])}[sys.argv[1]]()
