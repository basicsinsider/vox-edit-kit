#!/usr/bin/env bash
# One-shot environment setup for the Vox documentary edit kit.
# Works on Linux (cloud sessions, Debian/Ubuntu) and macOS. Safe to re-run.
#   bash setup.sh            # everything
#   bash setup.sh --no-reach # skip Agent Reach
set -euo pipefail
cd "$(dirname "$0")"
OS="$(uname -s)"
say() { printf '\n== %s\n' "$*"; }

say "System packages (ffmpeg, zsh, python3, curl)"
if [ "$OS" = "Linux" ]; then
  SUDO=""; [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null && SUDO="sudo"
  if command -v apt-get >/dev/null; then
    $SUDO apt-get update -qq || true
    $SUDO apt-get install -y -qq ffmpeg zsh python3 python3-venv curl unzip fontconfig file >/dev/null || \
      echo "!! apt install failed — install ffmpeg + zsh manually, or use the npm static ffmpeg fallback below"
  fi
fi
if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  say "Fallback: static ffmpeg/ffprobe from npm"
  mkdir -p "$HOME/.local/videotools" "$HOME/.local/bin"
  (cd "$HOME/.local/videotools" && npm init -y >/dev/null && npm i ffmpeg-static @ffprobe-installer/ffprobe >/dev/null)
  ln -sf "$HOME/.local/videotools/node_modules/ffmpeg-static/ffmpeg" "$HOME/.local/bin/ffmpeg"
  FP=$(find "$HOME/.local/videotools/node_modules/@ffprobe-installer" -name ffprobe -type f | grep -E "$( [ "$OS" = Darwin ] && echo darwin-$(uname -m | sed s/x86_64/x64/) || echo linux-$(uname -m | sed 's/x86_64/x64/;s/aarch64/arm64/'))" | head -1)
  ln -sf "$FP" "$HOME/.local/bin/ffprobe"
  export PATH="$HOME/.local/bin:$PATH"
fi
ffmpeg -version | head -1; ffprobe -version | head -1

say "Node.js (needs >= 22) + HyperFrames CLI"
node -v || { echo "!! Node.js missing — install Node 22+ (e.g. via nvm) and re-run"; exit 1; }
npx --yes hyperframes@0.8.217 --version
npx --yes hyperframes@0.8.217 browser ensure 2>/dev/null || npx --yes hyperframes@0.8.217 doctor || true
say "HyperFrames agent skills (/hyperframes, /hyperframes-core, /general-video, /media-use, ...)"
npx --yes hyperframes@0.8.217 skills update general-video || true
npx --yes hyperframes@0.8.217 skills update || true
say "Local speech-to-text model (Parakeet) for word timestamps"
npx --yes hyperframes@0.8.217 models install parakeet || echo "!! parakeet install failed — transcribe will fall back to whisper"

say "uv + Python environment (numpy, scipy, pillow) at .venv"
command -v uv >/dev/null || { curl -LsSf https://astral.sh/uv/install.sh | sh; export PATH="$HOME/.local/bin:$PATH"; }
uv venv --python 3.12 .venv >/dev/null 2>&1 || uv venv .venv
uv pip install --python .venv/bin/python numpy scipy pillow soundfile >/dev/null
.venv/bin/python -c "import numpy, scipy.signal, PIL; print('python env ok')"

say "Fonts (Cooper Hewitt, Haskoy, Crimson Pro) — bundled in assets/fonts; also installed system-wide"
if [ "$OS" = "Linux" ]; then mkdir -p "$HOME/.local/share/fonts" && cp assets/fonts/* "$HOME/.local/share/fonts/" && fc-cache -f >/dev/null 2>&1 || true; fi

if [ "${1:-}" != "--no-reach" ]; then
  say "Agent Reach (watch Instagram reels / read sites). Docs: https://github.com/Panniantong/Agent-Reach"
  uv tool install --force "https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip" >/dev/null || echo "!! Agent Reach install failed (network?) — references/reels already holds the studied reels"
  command -v agent-reach >/dev/null && agent-reach doctor --text | head -20 || true
fi

say "Done. Next: read CLAUDE.md, then MANUAL.md"
