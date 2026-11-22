"""(Cartels copy of package_premiere_nvidia.py) Build US_vs_Cartels_Premiere.zip (the Premiere Pro package, everything except the big 4K video files, which go to the same
gofile folder separately: Media/Video/Segments/ctsNN_4k.mp4).
Streams into the zip (low disk): VO.wav is the untouched edited VO (32-bit float, mono duplicated to L/R) padded with digital silence
to 1341.917 s = 32206 frames (no filter on the samples
style: pcm_s16le, no filter on the samples), beds are the sound designer's 24-bit stems as they are.
Usage: python3 tools/package_premiere_cartels.py OUT.zip"""
import glob, os, re, subprocess as sp, sys, zipfile
OUT = sys.argv[1]; R = 'US_vs_Cartels_Premiere/'
STORE = ('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.m4a', '.mov', '.webm', '.gif', '.mp3', '.zip')
z = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True)
def add(src, dst):
    z.write(src, R + dst, zipfile.ZIP_STORED if src.lower().endswith(STORE) else zipfile.ZIP_DEFLATED)
def text(dst, s): z.writestr(R + dst, s)

# XML + README
sp.run([sys.executable, 'tools/premiere_xml_cartels.py', '/dev/shm/US_vs_Cartels_Premiere.xml', '3840', '2160'], check=True)
add('/dev/shm/US_vs_Cartels_Premiere.xml', 'US_vs_Cartels_Premiere.xml')
add('project/cartels/premiere/README.txt', 'README.txt')

# Media/Audio — VO padded (samples untouched), beds as built, final mix reference
import struct
DATA = 32206 * 2000 * 8                       # f32 stereo, exactly 1341.9167 s (32206 frames @ 24 fps)
p = sp.Popen(['ffmpeg', '-v', 'error', '-i', 'project/cartels/media/vo_ct.wav', '-af', 'pan=stereo|c0=c0|c1=c0,apad=whole_len=64412000',
              '-c:a', 'pcm_f32le', '-f', 'f32le', '-'], stdout=sp.PIPE)
hdr = (b'RIFF' + struct.pack('<I', 4 + 26 + 12 + 8 + DATA) + b'WAVE' + b'fmt ' + struct.pack('<IHHIIHHH', 18, 3, 2, 48000, 48000 * 8, 8, 32, 0)
       + b'fact' + struct.pack('<II', 4, 32206 * 2000) + b'data' + struct.pack('<I', DATA))
n = 0
with z.open(R + 'Media/Audio/VO.wav', 'w', force_zip64=True) as f:
    f.write(hdr)
    while (b := p.stdout.read(1 << 20)): f.write(b); n += len(b)
assert n == DATA, (n, DATA)
assert p.wait() == 0
for src, dst in [('music_bed', 'Music_bed'), ('sfx', 'SFX'), ('ambience', 'Ambience')]:
    add(f'assets/audio/cartels/{src}.wav', f'Media/Audio/{dst}.wav')
add('project/cartels/media/ct_final_audio.m4a', 'Media/Audio/Final_mix_reference.m4a')
text('Media/Video/Segments/PUT cts01_4k.mp4 … cts14_4k.mp4 HERE.txt', 'Move the 14 files cts01_4k.mp4 … cts14_4k.mp4 (from the same gofile folder) into this folder.\n')
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
for f in ['lib/fx.css', 'lib/fx.js', 'lib/ct_motifs.css', 'lib/ct_motifs.js', 'lib/palette_cartels.css', 'transcript_ct.json',
          'references/palette_cartels.png', 'assets/audio/cartels/music_report.json', 'assets/audio/cartels/sfx_placements.json']:
    if os.path.isfile(f): add(f, 'Source/' + f)
for f in sorted(glob.glob('project/cartels/**/*', recursive=True)):
    if os.path.isfile(f) and '/media' not in f and '/premiere/' not in f: add(f, 'Source/' + f.replace('project/cartels/', 'project/'))
z.close()
n = len(zipfile.ZipFile(OUT).namelist())
print('files', n, 'shared assets', len(used), 'size', os.path.getsize(OUT))
