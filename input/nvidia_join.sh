#!/usr/bin/env bash
# NVIDIA project: rebuild assets/facecam/nvidia_facecam_master.mp4 (face cam aligned to the 2400.62 s master) from 95 MB parts.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/facecam
cat input/nvidia_parts/nvidia_facecam_master.mp4.part-* > assets/facecam/nvidia_facecam_master.mp4
(cd assets/facecam && sha256sum -c ../../input/nvidia_parts/SHA256SUMS)
