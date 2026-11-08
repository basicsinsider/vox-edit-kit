"""Write a Final Cut Pro 7 XML (xmeml v4) that Premiere Pro imports (File > Import): the Paraguay edit as two sequences.
  1. "Paraguay — final edit (4K)" 3840x2160 24p, 38924 frames:
       V2 = the rendered 4K master, split into one clip per scene (names = segment·scene·words) + a marker per scene
       V1 = clean face cam (aligned to the master; disabled — turn it on to re-frame/replace shots)
       A1/A2 = VO (bleeped, L/R) · A3/A4 = music bed · A5/A6 = SFX · A7/A8 = ambience   (stems sum to the delivered mix)
  2. "Paraguay — dialogue edit on raw take" 1920x1080 60p: the 104 EDL cuts on Krish's original file (frame-exact, 60 fps grid)
       V1 + A1/A2 from "2026-11-07 17-40-20.mp4" (put it in Media/Raw/).
All media paths point at /Paraguay_Premiere/Media/... — Premiere asks to relink once; pick any one file in the downloaded
Media folder and tick "Relink others automatically". Stereo stems are written as L/R pairs (the FCP7 convention Premiere reads).
Usage: python3 tools/premiere_xml_paraguay.py OUT.xml"""
import json, re, glob, sys, html
from urllib.parse import quote
OUT = sys.argv[1]
ROOT = '/Paraguay_Premiere/Media'
def url(rel): return 'file://localhost' + quote(f'{ROOT}/{rel}')
E = html.escape
MASTER_FR = 38924; FPS = 24

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

# --- scenes from the editors' EDIT_NOTES (scene id, master start, words) ---
scenes = []
for f in sorted(glob.glob('project/paraguay/EDIT_NOTES_pys??.md')):
    seg = re.search(r'(pys\d\d)', f).group(1)
    for l in open(f):
        cells = [c.strip().strip('*') for c in l.strip().strip('|').split('|')]
        for i, c in enumerate(cells[:-1]):
            m = re.fullmatch(r'(?:pys\d\d-)?(sc\d+[a-z]?)', c)
            t = re.match(r'([\d.]+)\s*[–-]\s*([\d.]+)', cells[i + 1]) if m else None
            if m and t:
                words = cells[i + 2] if i + 2 < len(cells) else ''
                scenes.append((float(t.group(1)), f'{seg} {m.group(1)}', words.strip('"“” ')))
                break
scenes.sort()
starts = []
for t, n, w in scenes:
    fr = round(t * FPS)
    if 0 <= fr < MASTER_FR and (not starts or fr > starts[-1][0]): starts.append((fr, n, w))
if not starts or starts[0][0] != 0: starts.insert(0, (0, 'pys01 sc001', ''))

# --- sequence 1: final edit ---
master = file_xml('file-master', 'Paraguay_4K_final.mp4', 'Video/Paraguay_4K_final.mp4', 24, MASTER_FR, 3840, 2160, 2)
v2 = []
for k, (fr, n, w) in enumerate(starts):
    end = starts[k + 1][0] if k + 1 < len(starts) else MASTER_FR
    v2.append(clip(f'{n} · {w[:60]}', 24, fr, end, fr, end, master if k == 0 else '<file id="file-master"/>'))
fc = file_xml('file-facecam', 'paraguay_facecam_master.mp4', 'Video/paraguay_facecam_master.mp4', 30, 48656, 1920, 1080)
v1 = [clip('Face cam (clean, aligned to the master — scale 200% for 4K)', 24, 0, MASTER_FR, 0, MASTER_FR, fc, enabled=False)]
stems = [('file-vo', 'VO_bleeped.wav', 'VO (bleeped)', 16), ('file-music', 'Music_bed.wav', 'Music bed', 24),
         ('file-sfx', 'SFX.wav', 'SFX', 24), ('file-amb', 'Ambience.wav', 'Ambience', 24)]
at = []
for fid, fn, label, depth in stems:
    fd = file_xml(fid, fn, f'Audio/{fn}', 24, MASTER_FR + 1, ach=2, adepth=depth)
    for ch in (1, 2):
        at.append(atrack([clip(f'{label} {"L" if ch == 1 else "R"}', 24, 0, MASTER_FR, 0, MASTER_FR, fd if ch == 1 else f'<file id="{fid}"/>', audio_ch=ch)], ch))
markers = ''.join(f'<marker><name>{E(n)}</name><comment>{E(w)}</comment><in>{fr}</in><out>-1</out></marker>' for fr, n, w in starts)
seq1 = sequence('sequence-1', 'Paraguay — final edit (4K)', 24, MASTER_FR, 3840, 2160, [vtrack(v1, False), vtrack(v2)], at, markers)

# --- sequence 2: dialogue edit on the raw take (60 fps grid, exact) ---
E2 = json.load(open('project/paraguay/edl_frames.json'))
raw = file_xml('file-raw', '2026-11-07 17-40-20.mp4', 'Raw/2026-11-07 17-40-20.mp4', 60, 129969, 1920, 1080, 2)
rv, ra1, ra2 = [], [], []
pos = 0
for k, s in enumerate(E2['segments']):
    n = s['f1'] - s['f0']; nm = f'EDL {k + 1:03d} · raw {s["raw_in"]:.2f}–{s["raw_out"]:.2f}'
    rv.append(clip(nm, 60, pos, pos + n, s['f0'], s['f1'], raw if k == 0 else '<file id="file-raw"/>'))
    ra1.append(clip(nm, 60, pos, pos + n, s['f0'], s['f1'], '<file id="file-raw"/>', audio_ch=1))
    ra2.append(clip(nm, 60, pos, pos + n, s['f0'], s['f1'], '<file id="file-raw"/>', audio_ch=2))
    pos += n
seq2 = sequence('sequence-2', 'Paraguay — dialogue edit on raw take (104 cuts)', 60, pos, 1920, 1080, [vtrack(rv)], [atrack(ra1, 1), atrack(ra2, 2)])

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><project><name>Paraguay (Searching Lessons)</name><children>'
       + seq1 + seq2 + '</children></project></xmeml>\n')
open(OUT, 'w').write(xml)
print('scenes', len(starts), 'edl clips', len(rv), 'seq2 frames', pos, '(', pos / 60, 's )', 'bytes', len(xml))
