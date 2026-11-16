#!/bin/zsh
# Creates work/<name>/ : a private preview project for one editor (own index.html + .snap), sharing
# assets/lib/tools/vo via symlinks. Edit compositions in the MAIN compositions/ folder; the sandbox links it.
# Usage: tools/make_sandbox.sh seg03   then:  cd work/seg03 && python3 tools/build_index.py seg03 --root . && npx hyperframes snapshot ...
set -e
cd "${0:A:h}/.."
W=work/$1; mkdir -p $W
for d in assets lib tools compositions references project vo10.mp3 vo_intro.mp3 vo_c1.mp3 vo_c2.mp3 vo_c3.mp3 vo_c4.mp3 vo_c5.mp3 vo_c6.mp3 transcript.json transcript_intro.json transcript_c1.json transcript_c2.json transcript_c3.json transcript_c4.json transcript_c5.json transcript_c6.json vo_iv.mp3 transcript_iv.json vo_ivan_master.wav vo_py.mp3 transcript_py.json vo_pd.mp3 transcript_pd.json vo_nv.mp3 transcript_nv.json hyperframes.json package.json input; do ln -sfn ../../$d $W/$d; done
echo "sandbox: $W"
