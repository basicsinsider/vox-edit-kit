#!/bin/zsh
# Packages the reusable editing kit (manual + style library + tools + references + templates + textures)
# into ./kit/vox-doc-kit. Re-run after any manual/library change so the shared copy stays current.
set -e
cd "${0:A:h}/.."
K=kit/vox-doc-kit
rm -rf $K && mkdir -p $K
cp MANUAL.md $K/
cp -R lib tools references $K/
mkdir -p $K/templates $K/assets
cp compositions/s*.html $K/templates/
cp tools/s02_template.html $K/templates/ 2>/dev/null || true
cp -R assets/textures $K/assets/ && rm -rf $K/assets/textures/_raw
cp -R assets/fonts $K/assets/
mkdir -p $K/assets/maps && cp assets/maps/{us_overlay.json,us_basemap_desat.jpg,burn_a.png,burn_b.png,SOURCES.md,project_to_svg.py} $K/assets/maps/
cp -R assets/maps/clouds $K/assets/maps/
[ -f assets/audio/LIBRARY.md ] && { mkdir -p $K/assets/audio; cp assets/audio/*.md $K/assets/audio/; }
[ -d tools/audio ] && cp -R tools/audio $K/tools/
cat > $K/START_HERE.md <<'EOF'
# Start here
1. Copy this folder next to (or into) a new HyperFrames project created with
   `npx hyperframes init <name> --resolution landscape --audio <your.mp3> --non-interactive --skill general-video`.
2. Copy `lib/`, `tools/`, `assets/` into the project; templates/ are working examples of every effect.
3. Read MANUAL.md top to bottom, then follow §8 (pipeline). Look at references/style-images and references/reels.
Fonts: Cooper Hewitt, Haskoy, Crimson Pro (assets/fonts — the user's licensed copies).
Textures: Texturelabs (free for commercial use; do not redistribute publicly as-is).
EOF
echo "kit at $K ($(du -sh $K | cut -f1))"
