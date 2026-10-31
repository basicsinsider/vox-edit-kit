#!/bin/zsh
# Creates work/<name>/ : a private preview project for one editor (own index.html + .snap), sharing
# assets/lib/tools/vo via symlinks. Edit compositions in the MAIN compositions/ folder; the sandbox links it.
# Usage: tools/make_sandbox.sh seg03   then:  cd work/seg03 && python3 tools/build_index.py seg03 --root . && npx hyperframes snapshot ...
set -e
cd "${0:A:h}/.."
W=work/$1; mkdir -p $W
for d in assets lib tools compositions references vo10.mp3 vo_intro.mp3 transcript.json transcript_intro.json hyperframes.json package.json; do ln -sfn ../../$d $W/$d; done
echo "sandbox: $W"
