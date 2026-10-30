#!/usr/bin/env bash
# Reassembles the input files from parts/ (they were split byte-for-byte to fit GitHub's 100 MB limit)
# and verifies they are identical to the originals. Run from anywhere: bash input/join.sh
set -euo pipefail
cd "$(dirname "$0")"
cat parts/"Face Cam.mp4.part-"*   > "Face Cam.mp4"
cat parts/"Full Audio.mp3.part-"* > "Full Audio.mp3"
if command -v sha256sum >/dev/null; then sha256sum -c SHA256SUMS; else shasum -a 256 -c SHA256SUMS; fi
echo "OK — input/Face Cam.mp4 and input/Full Audio.mp3 are ready (byte-identical to the originals)."
