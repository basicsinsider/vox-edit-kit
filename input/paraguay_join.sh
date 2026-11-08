#!/usr/bin/env bash
# Paraguay project: rebuild assets/facecam/paraguay_facecam_master.mp4 (face cam aligned to the 1621.87 s master) from 95 MB parts.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/facecam
cat input/paraguay_parts/paraguay_facecam_master.mp4.part-* > assets/facecam/paraguay_facecam_master.mp4
(cd assets/facecam && sha256sum -c ../../input/paraguay_parts/SHA256SUMS)
