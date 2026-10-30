#!/bin/bash
# Cloud environment setup script (claude.ai/code -> environment -> Setup script). Keep under ~5 min.
set -e
apt-get update -qq && apt-get install -y -qq ffmpeg zsh fontconfig file >/dev/null &
command -v uv >/dev/null || (curl -LsSf https://astral.sh/uv/install.sh | sh) &
wait
echo "base tools ready; run 'bash setup.sh' in the repo for the rest"
