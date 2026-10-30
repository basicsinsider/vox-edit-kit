#!/bin/zsh
# Builds a self-contained GitHub-ready repo of the editing kit next to this project:
#   ../vox-edit-kit  — a runnable HyperFrames project that regenerates the 11 approved samples,
#   plus the manual, effects library, tools, references, Taiwan planning docs and expected-output previews.
# Re-run after updating MANUAL.md / lib / tools. (Keeps an existing .git folder.)
set -e
export PATH=~/.local/bin:$PATH
SRC="${0:A:h}/.."
R="$SRC/../vox-edit-kit"
mkdir -p "$R"
cd "$SRC"
find "$R" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +

# --- docs ---
cp MANUAL.md EDITOR_BRIEF.md "$R/"
mkdir -p "$R/example-docs"
cp BRIEF.md EDIT_NOTES.md SEGMENTS.md DECISIONS.md ASSETS_NEEDED.md "$R/example-docs/"
cp -R analysis "$R/example-docs/"

# --- runnable project core ---
cp hyperframes.json package.json "$R/"
cp vo10.mp3 transcript.json transcript.txt "$R/"
cp -R lib "$R/"
rsync -a --exclude seg01 --exclude seg03 --exclude make_repo.sh tools/ "$R/tools/"
cp tools/make_repo.sh "$R/tools/" 2>/dev/null || true
mkdir -p "$R/compositions" "$R/templates/full-edit"
cp compositions/s[0-9]*.html "$R/compositions/"
cp compositions/seg0*.html compositions/seg0*.sfx.json compositions/seg0*.NOTES.md "$R/templates/full-edit/"
mkdir -p "$R/templates/full-edit/generators" && cp -R tools/seg01 tools/seg03 "$R/templates/full-edit/generators/"
cp -R references "$R/"

# --- assets: everything the 11 samples reference + the shared style assets ---
python3 - "$R" <<'EOF'
import re, glob, os, shutil, sys
R = sys.argv[1]
refs = set()
for f in glob.glob('compositions/s[0-9]*.html') + ['tools/s02_template.html', 'lib/fx.css']:
    for m in re.findall(r"""(?:\.\./)?(assets/[^"')\s>]+)""", open(f).read()):
        refs.add(m)
for r in sorted(refs):
    if os.path.exists(r):
        os.makedirs(os.path.join(R, os.path.dirname(r)), exist_ok=True)
        shutil.copy2(r, os.path.join(R, r))
print(len(refs), "sample asset files")
EOF
rsync -a assets/fonts "$R/assets/"
rsync -a --exclude '*_hires*' --exclude '*_withbg*' --exclude '_raw' --exclude 'grain_04*' assets/textures "$R/assets/"
rsync -a --exclude 'old' --exclude 'na_basemap.jpg' --exclude 'world_basemap.jpg' --exclude 'us_basemap.jpg' --exclude '*relief*' --exclude 'seg02_*' assets/maps "$R/assets/"
rsync -a assets/icons assets/logos assets/sfx "$R/assets/"
mkdir -p "$R/assets/audio" && cp assets/audio/*.md "$R/assets/audio/" && rsync -a assets/audio/sfx "$R/assets/audio/"
for d in archival archival/hoover archival/companies archival/terman archival/hp archival/footage archival/collage archival/brain_drain archival/newspapers archival/cutouts; do
  [ -f "assets/$d/SOURCES.md" ] && mkdir -p "$R/assets/$d" && cp "assets/$d/SOURCES.md" "$R/assets/$d/"
done

# --- expected output: 720p previews of the approved samples + a contact sheet each ---
mkdir -p "$R/expected"
for f in renders/samples/s*.mp4; do
  n=$(basename $f .mp4)
  ffmpeg -loglevel error -y -i $f -vf scale=1280:-2 -c:v libx264 -crf 28 -preset medium -c:a aac -b:a 128k "$R/expected/$n.720p.mp4"
  ffmpeg -loglevel error -y -i $f -vf "fps=1.2,scale=480:-1,tile=4x3:padding=4" -frames:v 1 "$R/expected/$n.sheet.jpg"
done

# --- repo hygiene ---
cat > "$R/.gitignore" <<'EOF'
node_modules/
renders/
work/
.snap/
.hyperframes/
.media/
compositions/_master/
kit/
*.wav.tmp
.DS_Store
EOF
python3 tools/build_index.py --root "$R" >/dev/null
echo "repo at $R ($(du -sh "$R" | cut -f1)); largest files:"
find "$R" -type f -not -path '*/.git/*' -size +40M -exec ls -la {} \; | awk '{print $5/1e6 " MB", $9}'
