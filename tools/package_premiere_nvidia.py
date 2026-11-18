"""Build NVIDIA_Premiere.zip (the Premiere Pro package, everything except the big 4K video files, which go to the same
gofile folder separately: Media/Video/nvidia_facecam_master_4k.mp4 + Media/Video/Segments/nvsNN_4k.mp4).
Streams into the zip (low disk): VO.wav is the untouched edited VO padded with digital silence to 2402.0 s (ffmpeg -c copy
style: pcm_s16le, no filter on the samples), beds are the sound designer's 24-bit stems as they are.
Usage: python3 tools/package_premiere_nvidia.py OUT.zip"""
import glob, os, re, subprocess as sp, sys, zipfile
OUT = sys.argv[1]; R = 'NVIDIA_Premiere/'
STORE = ('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.m4a', '.mov', '.webm', '.gif', '.mp3', '.zip')
z = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True)
def add(src, dst):
    z.write(src, R + dst, zipfile.ZIP_STORED if src.lower().endswith(STORE) else zipfile.ZIP_DEFLATED)
def text(dst, s): z.writestr(R + dst, s)

# XML + README
sp.run([sys.executable, 'tools/premiere_xml_nvidia.py', '/tmp/NVIDIA_Premiere.xml'], check=True)
add('/tmp/NVIDIA_Premiere.xml', 'NVIDIA_Premiere.xml')
add('project/nvidia/premiere/README.txt', 'README.txt')

# Media/Audio — VO padded (samples untouched), beds as built, final mix reference
import struct
DATA = round(2402.0 * 48000) * 4                       # s16 stereo, exactly 2402.0 s
p = sp.Popen(['ffmpeg', '-v', 'error', '-i', 'project/nvidia/media/vo_nv.wav', '-af', 'apad=whole_dur=2402.0',
              '-c:a', 'pcm_s16le', '-f', 's16le', '-'], stdout=sp.PIPE)
hdr = b'RIFF' + struct.pack('<I', 36 + DATA) + b'WAVEfmt ' + struct.pack('<IHHIIHH', 16, 1, 2, 48000, 48000 * 4, 4, 16) + b'data' + struct.pack('<I', DATA)
n = 0
with z.open(R + 'Media/Audio/VO.wav', 'w', force_zip64=True) as f:
    f.write(hdr)
    while (b := p.stdout.read(1 << 20)): f.write(b); n += len(b)
assert n == DATA, (n, DATA)
assert p.wait() == 0
for src, dst in [('music_bed', 'Music_bed'), ('sfx', 'SFX'), ('ambience', 'Ambience')]:
    add(f'assets/audio/nvidia/{src}.wav', f'Media/Audio/{dst}.wav')
add('project/nvidia/media/nv_final_audio.m4a', 'Media/Audio/Final_mix_reference.m4a')
text('Media/Video/PUT nvidia_facecam_master_4k.mp4 HERE.txt', 'Move nvidia_facecam_master_4k.mp4 (from the same gofile folder) into this folder.\n')
text('Media/Video/Segments/PUT nvs01_4k.mp4 … nvs23_4k.mp4 HERE.txt', 'Move the 23 files nvs01_4k.mp4 … nvs23_4k.mp4 (from the same gofile folder) into this folder.\n')
text('Media/Raw/PUT YOUR RAW TAKES HERE.txt', 'Optional, only for sequence 2: copy your original "part 1.mp4", "part 2.wav", "part 3.mp4" here (names exactly).\n')

# Assets — the whole NVIDIA library + every shared file the compositions use, with the SOURCES files of their folders
used = set()
for f in glob.glob('compositions/nvs??.html') + ['lib/nv_motifs.js', 'lib/nv_motifs.css', 'lib/palette_nvidia.css', 'lib/fx.css', 'lib/fx.js']:
    for m in re.findall(r"(assets/[^\"'()\s]+?\.(?:jpe?g|png|svg|webp|mp4|webm|otf|ttf|gif))", open(f, errors='ignore').read()):
        if os.path.isfile(m) and not m.startswith(('assets/nvidia/', 'assets/facecam/')): used.add(m)
for f in sorted(glob.glob('assets/nvidia/**/*', recursive=True)):
    if os.path.isfile(f): add(f, 'Assets/' + f[len('assets/'):])
dirs = set()
for f in sorted(used | set(glob.glob('assets/fonts/*'))):
    add(f, 'Assets/' + f[len('assets/'):]); dirs.add(os.path.dirname(f))
for d in sorted(dirs):
    for s in glob.glob(f'{d}/SOURCES*.md') + glob.glob(f'{os.path.dirname(d)}/SOURCES*.md') + glob.glob(f'{d}/LICEN*') + glob.glob(f'{d}/OFL*'):
        if R + 'Assets/' + s[len('assets/'):] not in z.namelist(): add(s, 'Assets/' + s[len('assets/'):])

# Source — compositions, motif/palette code, plans, notes, EDL, transcript, sound plan, cue sheet
for f in sorted(glob.glob('compositions/nvs*')): add(f, 'Source/' + f)
for f in ['lib/fx.css', 'lib/fx.js', 'lib/nv_motifs.css', 'lib/nv_motifs.js', 'lib/palette_nvidia.css', 'transcript_nv.json',
          'references/palette_nvidia.png', 'assets/audio/nvidia/music_report.json', 'assets/audio/nvidia/sfx_placements.json']:
    if os.path.isfile(f): add(f, 'Source/' + f)
for f in sorted(glob.glob('project/nvidia/**/*', recursive=True)):
    if os.path.isfile(f) and '/media' not in f and '/premiere/' not in f: add(f, 'Source/' + f.replace('project/nvidia/', 'project/'))
z.close()
n = len(zipfile.ZipFile(OUT).namelist())
print('files', n, 'shared assets', len(used), 'size', os.path.getsize(OUT))
