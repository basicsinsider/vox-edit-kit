#!/bin/bash
# window ASR in GLOBAL raw time (prints global times). usage: gwin.sh A B [engine]
export PATH=~/.local/bin:$PATH
d=work/asr/nv/g_$1; mkdir -p $d
ffmpeg -v error -y -ss $1 -to $2 -i project/nvidia/media/raw_audio.wav -ac 1 -ar 16000 $d/w.wav
(cd $d && npx --yes hyperframes@0.8.217 transcribe w.wav --engine ${3:-parakeet} --dir . >/dev/null 2>&1)
python3 -c "
import json;d=json.load(open('$d/transcript.json'));d=d['words'] if isinstance(d,dict) else d
print('[$1]', ' '.join(f\"{x['text']}@{$1+x['start']:.2f}-{$1+x['end']:.2f}\" for x in d))"
