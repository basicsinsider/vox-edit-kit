#!/bin/bash
# Re-transcribe a short raw window with Parakeet (short context = tighter word times). usage: asr_win.sh A B
export PATH=~/.local/bin:$PATH
d=work/asr/win_$1; mkdir -p $d
ffmpeg -v error -y -ss $1 -to $2 -i work/asr/raw16k.wav $d/w.wav
(cd $d && npx --yes hyperframes@0.8.217 transcribe w.wav --engine parakeet --dir . >/dev/null 2>&1)
python3 -c "
import json;d=json.load(open('$d/transcript.json'));d=d['words'] if isinstance(d,dict) else d
print(' '.join(f\"{x['text']}@{$1+x['start']:.2f}-{$1+x['end']:.2f}\" for x in d))"
