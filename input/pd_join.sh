#!/bin/bash
# Rebuild the podcast intro face cam (1080p, master-time aligned, 0-397 s) from its parts: bash input/pd_join.sh
set -e; cd "$(dirname "$0")/.."; mkdir -p assets/facecam
cat input/pd_parts/pd_facecam_intro.mp4.part-* > assets/facecam/pd_facecam_intro.mp4
(cd assets/facecam && sha256sum -c ../../input/pd_parts/SHA256SUMS)
