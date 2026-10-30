"""Checks that on-screen cues land on the spoken words.

Every cue in a composition is written as T(<voiceover seconds>) (see MANUAL.md, "Sync rule").
For each cue this prints the nearest transcript word and the offset (cue - word start).
Rule of thumb: text should land 0-120 ms BEFORE its word (offset between -0.12 and 0.00).
Cues more than 0.25 s away from any word start are flagged so you can check them by ear.

Usage: python3 tools/sync_audit.py compositions/*.html [--transcript transcript.json]
"""
import json, re, sys, pathlib

args = [a for a in sys.argv[1:] if not a.startswith("--")]
tp = "transcript.json"
if "--transcript" in sys.argv:
    tp = sys.argv[sys.argv.index("--transcript") + 1]
words = json.load(open(tp))
words = words if isinstance(words, list) else words["words"]
starts = [(w["start"], w["text"]) for w in words]

bad = 0
for f in args:
    src = pathlib.Path(f).read_text()
    cues = sorted({float(m) for m in re.findall(r"T\((\d+(?:\.\d+)?)\)", src)})
    if not cues:
        continue
    print(f"\n== {f}")
    for c in cues:
        ws, wt = min(starts, key=lambda s: abs(s[0] - c))
        off = c - ws
        flag = "" if -0.25 <= off <= 0.12 else "  <-- check"
        bad += bool(flag)
        print(f"  cue {c:8.2f}  word '{wt}' @ {ws:7.2f}  offset {off:+.2f}s{flag}")
print(f"\n{bad} cue(s) flagged")
