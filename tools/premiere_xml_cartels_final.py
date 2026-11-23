"""Final (2026-11-23) Premiere Pro XML (FCP7 xmeml v4) for US vs Cartels = the delivered final 4K, as editable timeline:
  Sequence 1 "US vs Cartels — FINAL (3840x2160)", 24 fps, 31,563 frames (21:55.125) = master v2:
    V1  cts00_4k.mp4 (cold open, 0–4.5 s) + the 14 rendered segments ctsNN_4k.mp4 (rendered on the ORIGINAL v1 timeline), cut into
        one clip per scene AND at every fix-round-1 VO cut (project/cartels/fix1_ops.json: 159 deletions, picture removed at the same
        frames) → clip names "ctsNN scNNN · words"; a marker at every scene start.
    V2  Krish's 3D renders, conformed to the v1 frame grid (Media/Video/3D/R1_conformed_4k.mp4, R4_conformed_4k.mp4 — tools/ct_conform_3d.py),
        cut with the same ops, over V1 (the originals are in Assets/3D_renders_original/).
    A1/A2 VO (edited, unity, mono on L/R, starts after the cold open) · A3/A4 cold-open clip audio · A5/A6 music · A7/A8 SFX · A9/A10 ambience
        (sum at 0 dB = the mix BEFORE the owner-requested levelling ride; the delivered levelled mix is Media/Audio/Final_mix_levelled.m4a, A11/A12, muted).
  Sequence 2 "VO edit on the raw take (reference)": the EDL (project/cartels/edl_map.json) minus the fix-1 deletions, on the raw take, 60 fps grid.
Usage: python3 tools/premiere_xml_cartels_final.py OUT.xml"""
import json, re, sys, html, numpy as np
from urllib.parse import quote
OUT = sys.argv[1]; W, H = 3840, 2160
ROOT = '/US_vs_Cartels_Premiere/Media'
def url(rel): return 'file://localhost' + quote(f'{ROOT}/{rel}')
E = html.escape; FPS = 24
SJ = json.load(open('project/cartels/segments.json')); SEGS = SJ['segments']; V1F = 32206
OPS = json.load(open('project/cartels/fix1_ops.json')); PF = round(float(OPS['preroll']) * FPS)
keep = np.ones(V1F, np.int32)
for o in OPS['ops']:
    assert 'del' in o, o
    f = round(o['t'] * FPS); keep[f:f + round(o['del'] * FPS)] = 0
cum = np.concatenate([[0], np.cumsum(keep)]); V2F = PF + int(cum[-1])          # v2 frame of v1 frame g = PF + cum[g]
assert V2F == 31563, V2F
def v2(g): return PF + int(cum[g])
def kept_runs(a, b):
    """kept v1 sub-ranges of [a, b)"""
    out, s = [], None
    for g in range(a, b):
        if keep[g] and s is None: s = g
        if not keep[g] and s is not None: out.append((s, g)); s = None
    if s is not None: out.append((s, b))
    return out
RAW_LEN = 1486.154667

def rate(tb): return f'<rate><timebase>{tb}</timebase><ntsc>FALSE</ntsc></rate>'
FILES = {}
def file_xml(fid, name, rel, tb, dur, w=None, h=None, ach=None, adepth=16):
    if fid in FILES: return f'<file id="{fid}"/>'
    FILES[fid] = rel
    v = f'<video><samplecharacteristics>{rate(tb)}<width>{w}</width><height>{h}</height><anamorphic>FALSE</anamorphic><pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance></samplecharacteristics></video>' if w else ''
    a = f'<audio><samplecharacteristics><depth>{adepth}</depth><samplerate>48000</samplerate></samplecharacteristics><channelcount>{ach}</channelcount></audio>' if ach else ''
    return f'<file id="{fid}"><name>{E(name)}</name><pathurl>{url(rel)}</pathurl>{rate(tb)}<duration>{dur}</duration><media>{v}{a}</media></file>'
_n = [0]
def clip(name, tb, start, end, cin, cout, fdef, audio_ch=None, enabled=True):
    _n[0] += 1
    st = f'<sourcetrack><mediatype>audio</mediatype><trackindex>{audio_ch}</trackindex></sourcetrack>' if audio_ch else ''
    return (f'<clipitem id="clipitem-{_n[0]}"><name>{E(name)}</name><enabled>{"TRUE" if enabled else "FALSE"}</enabled>'
            f'<duration>{cout - cin}</duration>{rate(tb)}<start>{start}</start><end>{end}</end><in>{cin}</in><out>{cout}</out>{fdef}{st}</clipitem>')
def vtrack(items): return f'<track>{"".join(items)}<enabled>TRUE</enabled><locked>FALSE</locked></track>'
def atrack(items, ch, enabled=True): return f'<track>{"".join(items)}<enabled>{"TRUE" if enabled else "FALSE"}</enabled><locked>FALSE</locked><outputchannelindex>{ch}</outputchannelindex></track>'
def sequence(sid, name, tb, dur, vtracks, atracks, markers=''):
    fmt = f'<format><samplecharacteristics>{rate(tb)}<width>{W}</width><height>{H}</height><anamorphic>FALSE</anamorphic><pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance><colordepth>24</colordepth></samplecharacteristics></format>'
    afmt = '<format><samplecharacteristics><depth>16</depth><samplerate>48000</samplerate></samplecharacteristics></format><outputs><group><index>1</index><numchannels>2</numchannels><downmix>0</downmix><channel><index>1</index></channel><channel><index>2</index></channel></group></outputs>'
    return (f'<sequence id="{sid}"><name>{E(name)}</name><duration>{dur}</duration>{rate(tb)}<timecode>{rate(tb)}<string>00:00:00:00</string><frame>0</frame><displayformat>NDF</displayformat></timecode>'
            f'<media><video>{fmt}{"".join(vtracks)}</video><audio>{afmt}{"".join(atracks)}</audio></media>{markers}</sequence>')

# --- V1: cold open + segments split at scenes and at kept-run boundaries ---
v1 = [clip('cts00 · cold open (Luis Cárdenas fan clip)', 24, 0, PF, 0, PF, file_xml('file-cts00', 'cts00_4k.mp4', 'Video/Segments/cts00_4k.mp4', 24, PF, W, H))]
markers = [(0, 'cts00 cold open', 'crowd clip with its own sound')]
bounds = [round(s['start'] * FPS) for s in SEGS] + [V1F]
for k, s in enumerate(SEGS):
    seg = s['id']; seg0, seg1 = bounds[k], bounds[k + 1]; sc = []
    for l in open(f'project/cartels/EDIT_NOTES_{seg}.md'):
        cells = [c.strip().strip('*').strip('`') for c in l.strip().strip('|').split('|')]
        if len(cells) < 3: continue
        m = re.fullmatch(rf'(?:{seg}-)?(sc\d+[a-z]?)(?:\s*\(.*\))?', cells[0])
        t = re.match(r'([\d.]+)\s*[–-]\s*([\d.]+)', cells[1]) if m else None
        if m and t: sc.append((min(max(round(float(t.group(1)) * FPS), seg0), seg1), f'{seg} {m.group(1)}', cells[2].strip('"“” ')))
    sc.sort(); pts = []
    for fr, n, w in sc:
        if fr < seg1 and (not pts or fr > pts[-1][0]): pts.append((fr, n, w))
    if not pts or pts[0][0] != seg0: pts.insert(0, (seg0, f'{seg} start', ''))
    fn = f'{seg}_4k.mp4'; fd = file_xml(f'file-{seg}', fn, f'Video/Segments/{fn}', 24, seg1 - seg0, W, H)
    for j, (fr, n, w) in enumerate(pts):
        end = pts[j + 1][0] if j + 1 < len(pts) else seg1
        runs = kept_runs(fr, end)
        if runs: markers.append((v2(runs[0][0]), n, w))
        for a, b in runs:
            v1.append(clip(f'{n} · {w[:60]}', 24, v2(a), v2(a) + b - a, a - seg0, b - seg0, fd)); fd = f'<file id="file-{seg}"/>'
# --- V2: 3D renders ---
v2t = []
for fid, fn, g0, g1, label in [('file-r1', 'R1_conformed_4k.mp4', 762, 1061, 'Krish 3D R1 · army came for one man / El Chapo Isidro'),
                               ('file-r4', 'R4_conformed_4k.mp4', 2810, 4794, 'Krish 3D R4 · To answer that … shooting and killing')]:
    fd = file_xml(fid, fn, f'Video/3D/{fn}', 24, g1 - g0, W, H)
    for a, b in kept_runs(g0, g1):
        v2t.append(clip(label, 24, v2(a), v2(a) + b - a, a - g0, b - g0, fd)); fd = f'<file id="{fid}"/>'
# --- audio stems (all v2 length) ---
at = []
stems = [('file-vo', 'VO.wav', 'VO', 32, True), ('file-cold', 'Cold_open_clip_audio.wav', 'Cold open clip', 24, True),
         ('file-music', 'Music_bed.wav', 'Music bed', 24, True), ('file-sfx', 'SFX.wav', 'SFX', 24, True),
         ('file-amb', 'Ambience.wav', 'Ambience', 24, True), ('file-mix', 'Final_mix_levelled.m4a', 'FINAL MIX (levelled, delivered) — muted reference', 16, False)]
for fid, fn, label, depth, on in stems:
    fd = file_xml(fid, fn, f'Audio/{fn}', 24, V2F, ach=2, adepth=depth)
    for ch in (1, 2):
        at.append(atrack([clip(f'{label} {"L" if ch == 1 else "R"}', 24, 0, V2F, 0, V2F, fd if ch == 1 else f'<file id="{fid}"/>', audio_ch=ch, enabled=on)], ch, on))
mk = ''.join(f'<marker><name>{E(n)}</name><comment>{E(w)}</comment><in>{fr}</in><out>-1</out></marker>' for fr, n, w in sorted(markers))
seq1 = sequence('sequence-1', 'US vs Cartels — FINAL (3840x2160)', 24, V2F, [vtrack(v1), vtrack(v2t)], at, mk)
# --- sequence 2: raw-take VO edit minus the fix-1 deletions (60 fps grid) ---
EM = json.load(open('project/cartels/edl_map.json'))['segments']
dels = [(o['t'], o['t'] + o['del']) for o in OPS['ops']]
fd = file_xml('file-raw', 'us vs cartels.wav', 'Raw/us vs cartels.wav', 60, round(RAW_LEN * 60), ach=1, adepth=32)
r1, r2, pos = [], [], 0
for k, s in enumerate(EM):
    e0 = s['edit_in']; L = s['raw_out'] - s['raw_in']; pieces = [(e0, e0 + L)]
    for a, b in dels:
        nxt = []
        for x, y in pieces:
            if b <= x or a >= y: nxt.append((x, y)); continue
            if x < a: nxt.append((x, a))
            if b < y: nxt.append((b, y))
        pieces = nxt
    for x, y in pieces:
        i0, i1 = round((s['raw_in'] + x - e0) * 60), round((s['raw_in'] + y - e0) * 60)
        if i1 - i0 < 2: continue
        nm = f'EDL {k + 1:03d} · raw {s["raw_in"] + x - e0:.2f}–{s["raw_in"] + y - e0:.2f}'
        r1.append(clip(nm, 60, pos, pos + i1 - i0, i0, i1, fd, audio_ch=1)); fd = '<file id="file-raw"/>'
        r2.append(clip(nm, 60, pos, pos + i1 - i0, i0, i1, fd, audio_ch=1)); pos += i1 - i0
seq2 = sequence('sequence-2', f'US vs Cartels — VO edit on the raw take ({len(r1)} pieces, reference)', 60, pos, [vtrack([])], [atrack(r1, 1), atrack(r2, 2)])
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><project><name>US vs Cartels FINAL (Searching Lessons)</name><children>'
       + seq1 + seq2 + '</children></project></xmeml>\n')
open(OUT, 'w').write(xml); json.dump(FILES, open(OUT + '.media.json', 'w'), indent=1)
# self-check: V1 covers every v2 frame exactly once
cov = np.zeros(V2F, np.int32)
for m in re.finditer(r'<start>(\d+)</start><end>(\d+)</end>', seq1.split('<audio>')[0].split('</track>')[0]): cov[int(m.group(1)):int(m.group(2))] += 1
print('V1 clips', len(v1), 'coverage ok' if (cov == 1).all() else f'COVERAGE PROBLEM {np.unique(cov)}', '| V2 3D clips', len(v2t), '| markers', len(markers),
      '| seq2 pieces', len(r1), f'{pos / 60:.2f} s (VO v2 {(V2F - PF) / 24:.2f} s)', '| bytes', len(xml))
