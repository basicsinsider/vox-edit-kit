"""FINAL (2026-11-23) Premiere Pro package for US vs Cartels = the delivered final 4K (fix round 1 + Krish's 3D renders), as an editable
timeline (tools/premiere_xml_cartels_final.py). Everything except the 15 big 4K segment files (cts00_4k.mp4 … cts14_4k.mp4, uploaded to the
same gofile folder separately) goes into the zip, streamed (low disk). VO.wav = work/fix1/vo_v2_master.wav (the edited VO after the fix-1 cuts,
samples untouched, 4.5 s of digital silence for the cold open first), mono duplicated to L/R (pan, unity), 32-bit float, padded to 31,563 frames.
Usage: python3 tools/package_premiere_cartels_final.py OUT.zip"""
import glob, os, re, subprocess as sp, sys, zipfile, struct
OUT = sys.argv[1]; R = 'US_vs_Cartels_Premiere/'
STORE = ('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.m4a', '.mov', '.webm', '.gif', '.mp3', '.zip')
z = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True)
def add(src, dst):
    z.write(src, R + dst, zipfile.ZIP_STORED if src.lower().endswith(STORE) else zipfile.ZIP_DEFLATED)
def text(dst, s): z.writestr(R + dst, s)
sp.run([sys.executable, 'tools/premiere_xml_cartels_final.py', '/dev/shm/US_vs_Cartels_Premiere.xml'], check=True)
add('/dev/shm/US_vs_Cartels_Premiere.xml', 'US_vs_Cartels_Premiere.xml')
add('project/cartels/premiere/README_FINAL.txt', 'README.txt')
NS = 31563 * 2000; DATA = NS * 8
p = sp.Popen(['ffmpeg', '-v', 'error', '-i', 'work/fix1/vo_v2_master.wav', '-af', f'pan=stereo|c0=c0|c1=c0,apad=whole_len={NS}',
              '-c:a', 'pcm_f32le', '-f', 'f32le', '-'], stdout=sp.PIPE)
hdr = (b'RIFF' + struct.pack('<I', 4 + 26 + 12 + 8 + DATA) + b'WAVE' + b'fmt ' + struct.pack('<IHHIIHHH', 18, 3, 2, 48000, 48000 * 8, 8, 32, 0)
       + b'fact' + struct.pack('<II', 4, NS) + b'data' + struct.pack('<I', DATA))
n = 0
with z.open(R + 'Media/Audio/VO.wav', 'w', force_zip64=True) as f:
    f.write(hdr)
    while (b := p.stdout.read(1 << 20)): f.write(b); n += len(b)
assert n == DATA and p.wait() == 0, (n, DATA)
for src, dst in [('music_bed', 'Music_bed'), ('sfx', 'SFX'), ('ambience', 'Ambience'), ('cold_open', 'Cold_open_clip_audio')]:
    add(f'assets/audio/cartels_v2/{src}.wav', f'Media/Audio/{dst}.wav')
add('work/final4k/ct_final4k_audio.m4a', 'Media/Audio/Final_mix_levelled.m4a')
add('/dev/shm/r3d/R1_v1.mp4', 'Media/Video/3D/R1_conformed_4k.mp4')
add('/dev/shm/r3d/R4_v1.mp4', 'Media/Video/3D/R4_conformed_4k.mp4')
for k, nm in [('R1', 'R1_army_came_for_one_man'), ('R2', 'R2_evidence_board'), ('R3', 'R3_birth_to_map_with_vo'), ('R4', 'R4_to_answer_that_to_killing_with_vo')]:
    add(f'/dev/shm/r3d_orig/{k}.mp4', f'Assets/3D_renders_original/{nm}.mp4')
text('Media/Video/Segments/PUT cts00_4k.mp4 … cts14_4k.mp4 HERE.txt', 'Move the 15 files cts00_4k.mp4 … cts14_4k.mp4 (from the same gofile folder) into this folder.\n')
add('input/vo_raw.wav', 'Media/Raw/us vs cartels.wav')

# Assets — the whole NVIDIA library + every shared file the compositions use, with the SOURCES files of their folders
used = set()
for f in glob.glob('compositions/cts??.html') + ['lib/ct_motifs.js', 'lib/ct_motifs.css', 'lib/palette_cartels.css', 'lib/fx.css', 'lib/fx.js']:
    for m in re.findall(r"(assets/[^\"'()\s]+?\.(?:jpe?g|png|svg|webp|mp4|webm|otf|ttf|gif))", open(f, errors='ignore').read()):
        if os.path.isfile(m) and not m.startswith(('assets/cartels/', 'assets/cartels/')): used.add(m)
for f in sorted(glob.glob('assets/cartels/**/*', recursive=True)):
    if os.path.isfile(f): add(f, 'Assets/' + f[len('assets/'):])
dirs = set()
for f in sorted(used | set(glob.glob('assets/fonts/*'))):
    add(f, 'Assets/' + f[len('assets/'):]); dirs.add(os.path.dirname(f))
for d in sorted(dirs):
    for s in glob.glob(f'{d}/SOURCES*.md') + glob.glob(f'{os.path.dirname(d)}/SOURCES*.md') + glob.glob(f'{d}/LICEN*') + glob.glob(f'{d}/OFL*'):
        if R + 'Assets/' + s[len('assets/'):] not in z.namelist(): add(s, 'Assets/' + s[len('assets/'):])

# Source — compositions, motif/palette code, plans, notes, EDL, transcript, sound plan, cue sheet
for f in sorted(glob.glob('compositions/cts*')): add(f, 'Source/' + f)
for f in ['project/cartels/fix1_ops.json', 'tools/ct_conform_3d.py', 'tools/ct_final4k_stream.py', 'work/fix1/transcript_v2.json']: add(f, 'Source/extra/' + os.path.basename(f))
for f in ['lib/fx.css', 'lib/fx.js', 'lib/ct_motifs.css', 'lib/ct_motifs.js', 'lib/palette_cartels.css', 'transcript_ct.json',
          'references/palette_cartels.png', 'assets/audio/cartels_v2/music_report.json', 'assets/audio/cartels_v2/sfx_placements.json']:
    if os.path.isfile(f): add(f, 'Source/' + f)
for f in sorted(glob.glob('project/cartels/**/*', recursive=True)):
    if os.path.isfile(f) and '/media' not in f and '/premiere/' not in f: add(f, 'Source/' + f.replace('project/cartels/', 'project/'))
z.close()
n = len(zipfile.ZipFile(OUT).namelist())
print('files', n, 'shared assets', len(used), 'size', os.path.getsize(OUT))
