#!/usr/bin/env bash
# Ivan project: rebuild assets/facecam/ivan_facecam_master.mp4 (face cam aligned to the 949 s master) from 95 MB parts.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/facecam
cat input/ivan_parts/ivan_facecam_master.mp4.part-* > assets/facecam/ivan_facecam_master.mp4
(cd assets/facecam && sha256sum -c ../../input/ivan_parts/SHA256SUMS)
