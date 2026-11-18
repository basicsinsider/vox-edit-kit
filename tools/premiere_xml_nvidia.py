"""Write a Final Cut Pro 7 XML (xmeml v4) that Premiere Pro imports (File > Import): the NVIDIA edit as two sequences.
  1. "NVIDIA — final edit (4K)" 3840x2160 24p, 57648 frames:
       V2 = the 23 rendered 4K segment files (Media/Video/Segments/nvsNN_4k.mp4), cut into one clip per scene
            (names = segment·scene·words) + a sequence marker per scene. No master render: the timeline IS the edit.
       V1 = clean 4K face cam (Media/Video/nvidia_facecam_master_4k.mp4, aligned to the edit, black in part 2; disabled —
            turn it on to re-frame/replace face-cam shots)
       A1/A2 = VO · A3/A4 = music bed · A5/A6 = SFX · A7/A8 = ambience   (stems sum to the delivered mix)
  2. "NVIDIA — dialogue edit on raw takes" 3840x2160 60p: the EDL cuts on Krish's original files (frame-exact, 60 fps grid)
       V1 + A1/A2 from Media/Raw/"part 1.mp4", "part 2.wav" (audio only, mono), "part 3.mp4".
All media paths point at /NVIDIA_Premiere/Media/... — Premiere asks to relink once; pick any one file in the downloaded
Media folder and tick "Relink others automatically". Stereo stems are written as L/R pairs (the FCP7 convention Premiere reads).
Usage: python3 tools/premiere_xml_nvidia.py OUT.xml"""
import json, re, glob, sys, html
from urllib.parse import quote
OUT = sys.argv[1]
ROOT = '/NVIDIA_Premiere/Media'
def url(rel): return 'file://localhost' + quote(f'{ROOT}/{rel}')
E = html.escape
SEGS = json.load(open('project/nvidia/segments.json'))['segments']
MASTER_FR = sum(s['frames'] for s in SEGS); FPS = 24          # 57648
VO_LEN = 2400.6167                                           # face cam master length (s) = VO length
FC_FR30 = round(VO_LEN * 30)

def rate(tb): return f'<rate><timebase>{tb}</timebase><ntsc>FALSE</ntsc></rate>'
FILES = {}
def file_xml(fid, name, rel, tb, dur, w=None, h=None, ach=None, adepth=16):
    if fid in FILES: return f'<file id="{fid}"/>'
    FILES[fid] = 1
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

# --- scenes from the editors' EDIT_NOTES (scene id, master start, words), per segment ---
v2, starts = [], []
seg0 = 0
for s in SEGS:
    seg = s['seg']; seg1 = seg0 + s['frames']
    sc = []
    for l in open(f'project/nvidia/EDIT_NOTES_{seg}.md'):
        cells = [c.strip().strip('*').strip('`') for c in l.strip().strip('|').split('|')]
        if len(cells) < 3: continue
        m = re.fullmatch(rf'(?:{seg}-)?(sc\d+[a-z]?)', cells[0])
        t = re.match(r'([\d.]+)\s*[–-]\s*([\d.]+)', cells[1]) if m else None
        if m and t: sc.append((min(max(round(float(t.group(1)) * FPS), seg0), seg1), f'{seg} {m.group(1)}', cells[2].strip('"“” ')))
    sc.sort()
    pts = []
    for fr, n, w in sc:
        if fr < seg1 and (not pts or fr > pts[-1][0]): pts.append((fr, n, w))
    if not pts or pts[0][0] != seg0: pts.insert(0, (seg0, f'{seg} start', ''))
    fid = f'file-{seg}'
    for k, (fr, n, w) in enumerate(pts):
        end = pts[k + 1][0] if k + 1 < len(pts) else seg1
        fd = file_xml(fid, f'{seg}_4k.mp4', f'Video/Segments/{seg}_4k.mp4', 24, s['frames'] + 1, 3840, 2160)
        v2.append(clip(f'{n} · {w[:60]}', 24, fr, end, fr - seg0, end - seg0, fd))
    starts += pts
    seg0 = seg1
assert seg0 == MASTER_FR

# --- sequence 1: final edit ---
fc = file_xml('file-facecam', 'nvidia_facecam_master_4k.mp4', 'Video/nvidia_facecam_master_4k.mp4', 30, FC_FR30, 3840, 2160)
FC_END = int(VO_LEN * 24)
v1 = [clip('Face cam (clean 4K, aligned to the edit; black = part 2, audio only)', 24, 0, FC_END, 0, FC_END, fc, enabled=False)]
stems = [('file-vo', 'VO.wav', 'VO', 16), ('file-music', 'Music_bed.wav', 'Music bed', 24),
         ('file-sfx', 'SFX.wav', 'SFX', 24), ('file-amb', 'Ambience.wav', 'Ambience', 24)]
at = []
for fid, fn, label, depth in stems:
    dur = MASTER_FR                       # VO.wav is padded with digital silence to 2402.0 s (as in the delivered mix)
    fd = file_xml(fid, fn, f'Audio/{fn}', 24, dur + 1, ach=2, adepth=depth)
    for ch in (1, 2):
        at.append(atrack([clip(f'{label} {"L" if ch == 1 else "R"}', 24, 0, dur, 0, dur, fd if ch == 1 else f'<file id="{fid}"/>', audio_ch=ch)], ch))
markers = ''.join(f'<marker><name>{E(n)}</name><comment>{E(w)}</comment><in>{fr}</in><out>-1</out></marker>' for fr, n, w in starts)
seq1 = sequence('sequence-1', 'NVIDIA — final edit (4K)', 24, MASTER_FR, 3840, 2160, [vtrack(v1, False), vtrack(v2)], at, markers)

# --- sequence 2: dialogue edit on the raw takes (60 fps grid, exact) ---
EF = json.load(open('project/nvidia/edl_frames.json'))
P = {p['part']: p for p in json.load(open('project/nvidia/parts.json'))}
off = {k: round(v['offset'] * 60) for k, v in P.items()}
RAW = {1: ('part 1.mp4', True, 2, 16), 2: ('part 2.wav', False, 1, 32), 3: ('part 3.mp4', True, 2, 16)}
rv, ra1, ra2 = [], [], []
pos = 0
for k, s in enumerate(EF['segments']):
    p = 1 if s['f0'] < off[2] else 2 if s['f0'] < off[3] else 3
    fn, vid, ach, depth = RAW[p]; fid = f'file-raw{p}'
    fd = file_xml(fid, fn, f'Raw/{fn}', 60, P[p]['frames'], *((3840, 2160) if vid else (None, None)), ach=ach, adepth=depth)
    i0, i1 = s['f0'] - off[p], s['f1'] - off[p]
    n = i1 - i0; nm = f'EDL {k + 1:03d} · part {p} · {i0 / 60:.2f}–{i1 / 60:.2f}'
    if vid: rv.append(clip(nm, 60, pos, pos + n, i0, i1, fd)); fd = f'<file id="{fid}"/>'
    ra1.append(clip(nm, 60, pos, pos + n, i0, i1, fd, audio_ch=1)); fd = f'<file id="{fid}"/>'
    ra2.append(clip(nm, 60, pos, pos + n, i0, i1, fd, audio_ch=2 if ach == 2 else 1))
    pos += n
seq2 = sequence('sequence-2', f'NVIDIA — dialogue edit on raw takes ({len(ra1)} cuts)', 60, pos, 3840, 2160, [vtrack(rv)], [atrack(ra1, 1), atrack(ra2, 2)])

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><project><name>NVIDIA (Searching Lessons)</name><children>'
       + seq1 + seq2 + '</children></project></xmeml>\n')
open(OUT, 'w').write(xml)
print('scenes', len(starts), 'v2 clips', len(v2), 'edl clips', len(ra1), 'seq2 frames', pos, '(', pos / 60, 's )', 'bytes', len(xml))
