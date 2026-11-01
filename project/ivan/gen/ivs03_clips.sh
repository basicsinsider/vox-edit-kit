#!/bin/bash
# ivs03 footage: BBC "Shadowmen" short clips, cropped past the BBC logo (top-left) and burned subtitles (bottom), 24 fps, no audio.
set -e
cd "$(dirname "$0")/../../.."
SRC=assets/ivan/footage/raw/bbc_shadowmen.mp4
OUT=assets/ivan/ivs03/footage; mkdir -p $OUT
clip() { # name start dur cropx cropy (crop 1600x900 → 1920x1080)
  nice -n 15 ffmpeg -v error -y -ss $2 -i $SRC -t $3 -an -vf "crop=1600:900:$4:$5,scale=1920:1080:flags=lanczos,fps=24,format=yuv420p" \
    -c:v libx264 -preset medium -crf 20 -g 24 -movflags +faststart $OUT/$1.mp4
}
clip warsaw_night     626.0 4.5 240 60
clip foma_silhouette  3599.0 4.5 240 70
clip kremlin_hall     719.0 5.0 240 70
clip laptop_streetview 677.0 6.0 240 40
clip apartment_windows 689.5 4.0 240 70
clip foma_training    659.0 5.0 240 40
clip tram_stop_night  617.5 6.5 240 70
clip streetlight_man  759.5 7.5 240 70
clip kirillov_site    755.0 4.5 240 30
clip sarvarov_portrait 3533.0 4.0 160 60
clip sarvarov_car     3539.0 4.0 240 70
clip officers_hall    707.0 5.5 240 70
clip moscow_window    671.0 7.5 240 40
ls -la $OUT
