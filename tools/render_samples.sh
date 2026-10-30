#!/bin/zsh
# Renders each sample on its own, then replaces the AAC voiceover with the original MP3 frames
# (stream copy, bit-identical to the raw file) — unless the sample carries SFX, in which case the
# rendered mix is kept (VO at unity gain, never processed).
# Usage: tools/render_samples.sh s01 s02 ...   (default: all samples in tools/build_index.py)
set -e
export PATH=~/.local/bin:$PATH
cd "${0:A:h}/.."
ids=("$@")
if [ ${#ids[@]} -eq 0 ]; then ids=(s01 s02 s03 s04 s05 s06 s07 s08 s09 s10); fi
mkdir -p renders/samples
for id in $ids; do
  file=$(ls compositions/${id}-*.html 2>/dev/null | head -1) || true
  [ -z "$file" ] && { echo "skip $id (no composition)"; continue; }
  name=$(basename $file .html)
  python3 tools/build_index.py $id >/dev/null
  npx hyperframes render -o renders/samples/_${name}.mp4 >/dev/null 2>&1
  # media-start / duration of the sample's VO, read from its <audio> tag
  ms=$(grep -o 'data-media-start="[0-9.]*"' $file | head -1 | grep -o '[0-9.]*')
  du=$(grep -o "id=\"${id}-vo\"[^>]*data-duration=\"[0-9.]*\"" $file | grep -o 'data-duration="[0-9.]*"' | grep -o '[0-9.]*')
  if grep -q "${id}-sfx" $file; then
    mv renders/samples/_${name}.mp4 renders/samples/${name}.mp4
  else
    ffmpeg -hide_banner -loglevel error -y -ss $ms -t $du -i vo10.mp3 -c copy renders/samples/_${name}_vo.mp3
    ffmpeg -hide_banner -loglevel error -y -i renders/samples/_${name}.mp4 -i renders/samples/_${name}_vo.mp3 \
      -map 0:v -map 1:a -c copy -t $du renders/samples/${name}.mp4
    rm renders/samples/_${name}_vo.mp3
    rm renders/samples/_${name}.mp4
  fi
  echo "rendered $name"
done
