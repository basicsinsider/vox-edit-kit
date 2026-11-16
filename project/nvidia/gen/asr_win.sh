#!/bin/bash
# Re-transcribe a short raw window with Parakeet. usage: asr_win.sh PART A B   (times local to the part)
export PATH=~/.local/bin:$PATH
d=work/asr/nv/win_$1_$2; mkdir -p $d
ffmpeg -v error -y -ss $2 -to $3 -i work/asr/nv/p$1/raw16k.wav $d/w.wav
(cd $d && npx --yes hyperframes@0.8.217 transcribe w.wav --engine parakeet --dir . >/dev/null 2>&1)
python3 -c "
import json;d=json.load(open('$d/transcript.json'));d=d['words'] if isinstance(d,dict) else d
print('p$1', ' '.join(f\"{x['text']}@{$2+x['start']:.2f}-{$2+x['end']:.2f}\" for x in d))"
