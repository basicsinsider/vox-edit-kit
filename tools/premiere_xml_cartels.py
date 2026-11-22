"""Write a Final Cut Pro 7 XML (xmeml v4) that Premiere Pro imports (File > Import): the US vs Cartels edit as two sequences.
(Adapted from tools/premiere_xml_nvidia.py; no face cam in this video.)
  1. "US vs Cartels — final edit" W x H 24p, 32206 frames (1341.917 s):
       V1 = the 14 rendered segment files (Media/Video/Segments/ctsNN.mp4), cut into one clip per scene (names = segment·scene·words)
            + a sequence marker per scene. No master render needed: the timeline IS the edit.
       A1/A2 = VO · A3/A4 = music bed · A5/A6 = SFX · A7/A8 = ambience   (stems sum to the delivered mix at 0 dB)
  2. "US vs Cartels — VO edit on the raw take (reference)": the EDL as audio clips on Krish's original "us vs cartels.wav"
       (Media/Raw/), on a 60 fps grid (cut points rounded to 1/60 s — the exact cuts are in Media/Audio/VO.wav).
All media paths point at /US_vs_Cartels_Premiere/Media/... — Premiere asks to relink once; pick any one file in the downloaded
Media folder and tick "Relink others automatically". Stereo stems are written as L/R pairs (the FCP7 convention Premiere reads).
Usage: python3 tools/premiere_xml_cartels.py OUT.xml [W H]   (W H = the segment files' size, default 1280 720)"""
import json, re, sys, html
from urllib.parse import quote
OUT = sys.argv[1]
W, H = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (1280, 720)
ROOT = '/US_vs_Cartels_Premiere/Media'
def url(rel): return 'file://localhost' + quote(f'{ROOT}/{rel}')
E = html.escape
FPS = 24
SJ = json.load(open('project/cartels/segments.json'))
SEGS = SJ['segments']
MASTER_FR = round(SJ['length'] * FPS)                       # 32206
RAW_LEN = 1486.154667                                       # input/vo_raw.wav (48 kHz mono f32)

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
def vtrack(items, enabled=True): return f'<track>{"".join(items)}<enabled>{"TRUE" if enabled else "FALSE"}</enabled><locked>FALSE</locked></track>'
def atrack(items, ch): return f'<track>{"".join(items)}<enabled>TRUE</enabled><locked>FALSE</locked><outputchannelindex>{ch}</outputchannelindex></track>'
def sequence(sid, name, tb, dur, w, h, vtracks, atracks, markers=''):
    fmt = f'<format><samplecharacteristics>{rate(tb)}<width>{w}</width><height>{h}</height><anamorphic>FALSE</anamorphic><pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance><colordepth>24</colordepth></samplecharacteristics></format>'
    afmt = '<format><samplecharacteristics><depth>16</depth><samplerate>48000</samplerate></samplecharacteristics></format><outputs><group><index>1</index><numchannels>2</numchannels><downmix>0</downmix><channel><index>1</index></channel><channel><index>2</index></channel></group></outputs>'
    return (f'<sequence id="{sid}"><name>{E(name)}</name><duration>{dur}</duration>{rate(tb)}<timecode>{rate(tb)}<string>00:00:00:00</string><frame>0</frame><displayformat>NDF</displayformat></timecode>'
            f'<media><video>{fmt}{"".join(vtracks)}</video><audio>{afmt}{"".join(atracks)}</audio></media>{markers}</sequence>')

# --- scenes from the editors' EDIT_NOTES_ctsNN.md (scene id, master start, words) ---
v1, starts = [], []
bounds = [round(s['start'] * FPS) for s in SEGS] + [MASTER_FR]
for k, s in enumerate(SEGS):
    seg = s['id']; seg0, seg1 = bounds[k], bounds[k + 1]
    sc = []
    for l in open(f'project/cartels/EDIT_NOTES_{seg}.md'):
        cells = [c.strip().strip('*').strip('`') for c in l.strip().strip('|').split('|')]
        if len(cells) < 3: continue
        m = re.fullmatch(rf'(?:{seg}-)?(sc\d+[a-z]?)(?:\s*\(.*\))?', cells[0])
        t = re.match(r'([\d.]+)\s*[–-]\s*([\d.]+)', cells[1]) if m else None
        if m and t: sc.append((min(max(round(float(t.group(1)) * FPS), seg0), seg1), f'{seg} {m.group(1)}', cells[2].strip('"“” ')))
    sc.sort()
    pts = []
    for fr, n, w in sc:
        if fr < seg1 and (not pts or fr > pts[-1][0]): pts.append((fr, n, w))
    if not pts or pts[0][0] != seg0: pts.insert(0, (seg0, f'{seg} start', ''))
    fid = f'file-{seg}'
    for j, (fr, n, w) in enumerate(pts):
        end = pts[j + 1][0] if j + 1 < len(pts) else seg1
        fd = file_xml(fid, f'{seg}.mp4', f'Video/Segments/{seg}.mp4', 24, seg1 - seg0 + 1, W, H)
        v1.append(clip(f'{n} · {w[:60]}', 24, fr, end, fr - seg0, end - seg0, fd))
    starts += pts

# --- sequence 1: final edit ---
stems = [('file-vo', 'VO.wav', 'VO', 16), ('file-music', 'Music_bed.wav', 'Music bed', 24),
         ('file-sfx', 'SFX.wav', 'SFX', 24), ('file-amb', 'Ambience.wav', 'Ambience', 24)]
at = []
for fid, fn, label, depth in stems:
    fd = file_xml(fid, fn, f'Audio/{fn}', 24, MASTER_FR + 1, ach=2, adepth=depth)
    for ch in (1, 2):
        at.append(atrack([clip(f'{label} {"L" if ch == 1 else "R"}', 24, 0, MASTER_FR, 0, MASTER_FR, fd if ch == 1 else f'<file id="{fid}"/>', audio_ch=ch)], ch))
markers = ''.join(f'<marker><name>{E(n)}</name><comment>{E(w)}</comment><in>{fr}</in><out>-1</out></marker>' for fr, n, w in starts)
seq1 = sequence('sequence-1', f'US vs Cartels — final edit ({W}x{H})', 24, MASTER_FR, W, H, [vtrack(v1)], at, markers)

# --- sequence 2: the VO edit on the raw take (audio only, 60 fps grid, reference) ---
EM = json.load(open('project/cartels/edl_map.json'))
RAW_FR = round(RAW_LEN * 60)
fd = file_xml('file-raw', 'us vs cartels.wav', 'Raw/us vs cartels.wav', 60, RAW_FR, ach=1, adepth=32)
ra1, ra2, pos = [], [], 0
for k, s in enumerate(EM['segments']):
    i0, i1 = round(s['raw_in'] * 60), round(s['raw_out'] * 60)
    n = i1 - i0; nm = f'EDL {k + 1:03d} · raw {s["raw_in"]:.2f}–{s["raw_out"]:.2f}'
    ra1.append(clip(nm, 60, pos, pos + n, i0, i1, fd, audio_ch=1)); fd = '<file id="file-raw"/>'
    ra2.append(clip(nm, 60, pos, pos + n, i0, i1, fd, audio_ch=1))
    pos += n
seq2 = sequence('sequence-2', f'US vs Cartels — VO edit on the raw take ({len(ra1)} pieces, reference)', 60, pos, W, H, [vtrack([])], [atrack(ra1, 1), atrack(ra2, 2)])

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><project><name>US vs Cartels (Searching Lessons)</name><children>'
       + seq1 + seq2 + '</children></project></xmeml>\n')
open(OUT, 'w').write(xml)
json.dump(FILES, open(OUT + '.media.json', 'w'), indent=1)
print('scenes', len(starts), 'v1 clips', len(v1), 'edl clips', len(ra1), 'seq2 frames', pos, f'({pos / 60:.2f} s)', 'bytes', len(xml))
