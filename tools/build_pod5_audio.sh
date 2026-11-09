#!/bin/bash
# Rebuild podcast beds; source dialogue is read only, never rewritten or gained.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p work/pod5tmp
export TMPDIR="$ROOT/work/pod5tmp"
.venv/bin/python tools/audio/place_sound.py --vo input/BB_podcast_v2_first5min.mp4 --transcript project/pod5/codex/transcript_pod5.json --len 299 --markers 'compositions/pod5*.sfx.json' --cues project/pod5/codex/music_cuesheet.json --out assets/audio/pod5_codex
# Restraint adjustment established by the short-window scan; applied only to effects.
ffmpeg -v error -i assets/audio/pod5_codex/sfx.wav -af volume=-8dB -c:a pcm_s24le -y assets/audio/pod5_codex/sfx_quiet.wav
mv assets/audio/pod5_codex/sfx_quiet.wav assets/audio/pod5_codex/sfx.wav
