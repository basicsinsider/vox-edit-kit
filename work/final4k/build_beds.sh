#!/bin/bash
# fix round 1: v2 build + scan + act_levels (logs in /dev/shm/sound_v2/*$1*)
cd /home/user/vox-edit-kit
L=/dev/shm/sound_v2
TMPDIR=/dev/shm nice .venv/bin/python tools/audio/place_sound.py --vo work/fix1/vo_v2_master.wav --transcript work/fix1/transcript_v2.json --len 1315.125 \
  --markers 'work/final4k/sfx/cts*.sfx.json' --cues project/cartels/music_cuesheet_v2.json --out assets/audio/cartels_v2 > $L/build$1.log 2>&1 || { echo BUILD FAILED; tail $L/build$1.log; exit 1; }
nice .venv/bin/python tools/audio/vo_music_scan.py --vo work/fix1/vo_v2_master.wav --beds assets/audio/cartels_v2 > $L/scan$1.txt 2>&1; echo "scan exit $?" >> $L/scan$1.txt
nice .venv/bin/python tools/audio/act_levels.py --vo work/fix1/vo_v2_master.wav --beds assets/audio/cartels_v2 --cues project/cartels/music_cuesheet_v2.json --len 1315.125 > $L/act$1.txt 2>&1
echo DONE
