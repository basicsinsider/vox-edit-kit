"""Write a Final Cut Pro 7 XML (xmeml v4) that Premiere Pro imports (File > Import) for the podcast edit "TSMC vs UMC".
Same approach as tools/premiere_xml_paraguay.py, but built from this edit's real structure (EDL + sections + sound islands):

  1. "TSMC vs UMC — final edit" 1920x1080 30p, 172561 frames (95:52.03):
       V1 = your raw take (podcast.mp4, 4K) cut by the EDL: one clip per kept piece (229), frame-exact; every second clip is
            the punch-in (scale 54 % = 108 % of the 50 % fit) exactly as in the review
       V2 = the 44 rendered graphic pieces (pd01-pd44, 1080p30) at their master frames (the intro is pd01-pd03)
       A1/A2 = the cut voice (Voice_edited.wav, the camera audio cut only — never processed), on both channels at unity
       A3/A4 music · A5/A6 SFX · A7/A8 ambience = one clip per sound island (39), L/R pairs, 0 dB
       markers: one per section (title + why it is there)
  2. "TSMC vs UMC — dialogue edit on raw take (229 cuts)" 3840x2160 30p: V1 + A1/A2 from podcast.mp4 only, no punch-ins.

Media paths point at /TSMC_vs_UMC_Premiere/Media/... — Premiere asks to relink once; pick any one file inside the downloaded
Media folder and keep "Relink others automatically" ticked. Usage: python3 tools/premiere_xml_podcast.py OUT.xml"""
import json, sys, html, soundfile as sf
from urllib.parse import quote
OUT = sys.argv[1]
PKG = 'renders/premiere/TSMC_vs_UMC_Premiere'
ROOT = '/TSMC_vs_UMC_Premiere/Media'
FPS = 30
E = html.escape
def url(rel): return 'file://localhost' + quote(f'{ROOT}/{rel}')
def rate(tb=FPS): return f'<rate><timebase>{tb}</timebase><ntsc>FALSE</ntsc></rate>'

S = json.load(open('project/podcast/sections.json')); MASTER = round(S['length'] * FPS)
EDL = json.load(open('project/podcast/edl_frames.json'))['segments']
PUNCH = json.load(open('project/podcast/punch_plan.json'))
MAN = json.load(open('assets/audio/podcast/pd_beds_manifest.json'))['islands']
RAW_FR, RAW_W, RAW_H = 176997, 3840, 2160              # podcast.mp4 (ffprobe: hevc 3840x2160 30/1, 176997 frames)

FILES = set()
def fileref(fid, name, rel, dur, w=None, h=None, ach=None, sr=48000, depth=16):
    if fid in FILES: return f'<file id="{fid}"/>'
    FILES.add(fid)
    v = (f'<video><samplecharacteristics>{rate()}<width>{w}</width><height>{h}</height><anamorphic>FALSE</anamorphic>'
         f'<pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance></samplecharacteristics></video>') if w else ''
    a = (f'<audio><samplecharacteristics><depth>{depth}</depth><samplerate>{sr}</samplerate></samplecharacteristics>'
         f'<channelcount>{ach}</channelcount></audio>') if ach else ''
    return f'<file id="{fid}"><name>{E(name)}</name><pathurl>{url(rel)}</pathurl>{rate()}<duration>{dur}</duration><media>{v}{a}</media></file>'

def motion(scale):
    return ('<filter><effect><name>Basic Motion</name><effectid>basic</effectid><effectcategory>motion</effectcategory>'
            '<effecttype>motion</effecttype><mediatype>video</mediatype><parameter authoringApp="PremierePro"><parameterid>scale</parameterid>'
            f'<name>Scale</name><valuemin>0</valuemin><valuemax>1000</valuemax><value>{scale:g}</value></parameter></effect></filter>')

_n = [0]
def clip(name, start, end, cin, cout, fdef, ch=None, extra='', enabled=True):
    _n[0] += 1
    st = f'<sourcetrack><mediatype>audio</mediatype><trackindex>{ch}</trackindex></sourcetrack>' if ch else ''
    return (f'<clipitem id="clipitem-{_n[0]}"><name>{E(name)}</name><enabled>{"TRUE" if enabled else "FALSE"}</enabled>'
            f'<duration>{cout - cin}</duration>{rate()}<start>{start}</start><end>{end}</end><in>{cin}</in><out>{cout}</out>'
            f'{fdef}{st}{extra}</clipitem>')
def vtrack(items, on=True): return f'<track>{"".join(items)}<enabled>{"TRUE" if on else "FALSE"}</enabled><locked>FALSE</locked></track>'
def atrack(items, ch): return f'<track>{"".join(items)}<enabled>TRUE</enabled><locked>FALSE</locked><outputchannelindex>{ch}</outputchannelindex></track>'
def sequence(sid, name, dur, w, h, vt, at, markers=''):
    fmt = (f'<format><samplecharacteristics>{rate()}<width>{w}</width><height>{h}</height><anamorphic>FALSE</anamorphic>'
           f'<pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance><colordepth>24</colordepth></samplecharacteristics></format>')
    afmt = ('<format><samplecharacteristics><depth>16</depth><samplerate>48000</samplerate></samplecharacteristics></format><outputs><group>'
            '<index>1</index><numchannels>2</numchannels><downmix>0</downmix><channel><index>1</index></channel><channel><index>2</index></channel></group></outputs>')
    return (f'<sequence id="{sid}"><name>{E(name)}</name><duration>{dur}</duration>{rate()}<timecode>{rate()}<string>00:00:00:00</string>'
            f'<frame>0</frame><displayformat>NDF</displayformat></timecode><media><video>{fmt}{"".join(vt)}</video><audio>{afmt}{"".join(at)}</audio></media>{markers}</sequence>')

# ---------------- sequence 1: final edit ----------------
assert sum(s['f1'] - s['f0'] for s in EDL) == MASTER, 'EDL length != master'
v1, pos = [], 0
for k, s in enumerate(EDL):
    n = s['f1'] - s['f0']; z = PUNCH[k]['zoom'] if k < len(PUNCH) else 1.0
    assert PUNCH[k]['master_f0'] == pos
    f = fileref('file-raw', 'podcast.mp4', 'Raw/podcast.mp4', RAW_FR, RAW_W, RAW_H, 2, 44100)
    v1.append(clip(f'A-roll {k + 1:03d}{" · punch-in" if z > 1 else ""} · raw {s["raw_in"]:.2f}-{s["raw_out"]:.2f}',
                   pos, pos + n, s['f0'], s['f1'], f, extra=motion(50 * z)))
    pos += n
v2, markers = [], []
for s in S['sections']:
    f0, f1 = round(s['start'] * FPS), round(s['end'] * FPS); n = f1 - f0
    fr = fileref(f'file-{s["id"]}', f'{s["id"]}.mp4', f'Sections/{s["id"]}.mp4', n, 1920, 1080)
    v2.append(clip(f'{s["id"]} · {s["title"][:70]}', f0, f1, 0, n, fr))
    markers.append(f'<marker><name>{E(s["id"] + " · " + s["title"][:60])}</name><comment>{E(s["why"])}</comment><in>{f0}</in><out>-1</out></marker>')
vo_dur = round(sf.info('project/podcast/media/vo_pd.wav').duration * FPS)
fvo = fileref('file-vo', 'Voice_edited.wav', 'Audio/Voice_edited.wav', vo_dur, ach=1, sr=44100)
at = [atrack([clip('Voice (cut only, unity)', 0, MASTER, 0, MASTER, fvo, ch=1)], 1),
      atrack([clip('Voice (cut only, unity)', 0, MASTER, 0, MASTER, '<file id="file-vo"/>', ch=1)], 2)]
for stem in ('Music', 'SFX', 'Ambience'):
    tl, tr = [], []
    for isl in MAN:
        rel = f'Audio/Islands/{isl["id"]}_{stem}.wav'; info = sf.info(f'{PKG}/Media/{rel}')
        n = round(info.duration * FPS); a = round(isl['start'] * FPS); fid = f'file-{isl["id"]}-{stem}'
        fd = fileref(fid, f'{isl["id"]}_{stem}.wav', rel, n, ach=2, sr=info.samplerate)
        nm = f'{stem} · {isl["id"]} ({", ".join(isl["sections"])})'
        tl.append(clip(nm + ' L', a, a + n, 0, n, fd, ch=1)); tr.append(clip(nm + ' R', a, a + n, 0, n, f'<file id="{fid}"/>', ch=2))
    at += [atrack(tl, 1), atrack(tr, 2)]
seq1 = sequence('sequence-1', 'TSMC vs UMC — final edit', MASTER, 1920, 1080, [vtrack(v1), vtrack(v2)], at, ''.join(markers))

# ---------------- sequence 2: dialogue edit on the raw take ----------------
rv, ra1, ra2, pos = [], [], [], 0
for k, s in enumerate(EDL):
    n = s['f1'] - s['f0']; nm = f'EDL {k + 1:03d} · raw {s["raw_in"]:.2f}-{s["raw_out"]:.2f}'
    rv.append(clip(nm, pos, pos + n, s['f0'], s['f1'], '<file id="file-raw"/>'))
    ra1.append(clip(nm, pos, pos + n, s['f0'], s['f1'], '<file id="file-raw"/>', ch=1))
    ra2.append(clip(nm, pos, pos + n, s['f0'], s['f1'], '<file id="file-raw"/>', ch=2))
    pos += n
seq2 = sequence('sequence-2', f'TSMC vs UMC — dialogue edit on raw take ({len(EDL)} cuts)', pos, RAW_W, RAW_H, [vtrack(rv)], [atrack(ra1, 1), atrack(ra2, 2)])

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><project><name>TSMC vs UMC (Searching Lessons)</name><children>'
       + seq1 + seq2 + '</children></project></xmeml>\n')
open(OUT, 'w').write(xml)
print('seq1: V1', len(v1), 'A-roll clips · V2', len(v2), 'sections · islands', len(MAN), '· frames', MASTER, '| seq2 clips', len(rv), '| bytes', len(xml))
