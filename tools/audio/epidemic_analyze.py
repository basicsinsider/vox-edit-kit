#!/usr/bin/env python3
"""'Listen' to the downloaded Epidemic tracks by measurement (MANUAL §10.3): per stem integrated loudness, true peak,
a 1 s short-term loudness curve (EBU R128 S, 3 s window) and the sections it implies (quiet / steady / build / peak / drop),
plus a key estimate (Krumhansl chroma) and BPM-derived bar length for the full mix.

  .venv/bin/python tools/audio/epidemic_analyze.py [track_dir ...]   (default: every dir in assets/audio/epidemic except sfx)
  -> assets/audio/epidemic/ANALYSIS.json  (machine-readable, used by the bed builder)
  -> assets/audio/epidemic/ANALYSIS.md    (human-readable: stems table + section timeline per track)

Memory-safe: ffmpeg streams every file (one at a time); only the full mix is decoded (mono, 11 kHz, first 240 s) for key.
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
from scipy.signal import stft

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EPI = os.path.join(ROOT, "assets/audio/epidemic")
FFMPEG = "ffmpeg"
BPM = {}  # filled from LOG.md table (| name | ... | bpm |) if present, else None

MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NOTES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def r128(path):
    """Integrated LUFS, true peak and a 1 s short-term loudness curve, streamed by ffmpeg."""
    p = subprocess.run([FFMPEG, "-nostats", "-v", "info", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    st, last = [], -1
    for line in p.stderr.splitlines():
        m = re.search(r"t:\s*([\d.]+).*?S:\s*(-?[\d.]+|-inf)", line)
        if m:
            t = float(m.group(1))
            if int(t) > last:
                last = int(t)
                s = m.group(2)
                st.append(-70.0 if s == "-inf" else max(-70.0, float(s)))
    if len(st) > 3:                      # S needs a full 3 s window: hold the first valid value over the warm-up
        st[:3] = [st[3]] * 3
    tail = p.stderr[p.stderr.rfind("Summary"):]
    i = re.search(r"I:\s*(-?[\d.]+) LUFS", tail)
    tp = re.search(r"Peak:\s*(-?[\d.]+|-inf) dBFS", tail)
    return (float(i.group(1)) if i else -70.0), (float(tp.group(1)) if tp and tp.group(1) != "-inf" else -70.0), st


def key_of(path):
    raw = subprocess.run([FFMPEG, "-v", "quiet", "-t", "240", "-i", path, "-ac", "1", "-ar", "11025", "-f", "f32le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    f, _, Z = stft(x, 11025, nperseg=4096, noverlap=2048)
    M = np.abs(Z) ** 2
    ok = (f > 55) & (f < 2000)
    pc = np.round(12 * np.log2(f[ok] / 261.63)).astype(int) % 12
    c = np.array([M[ok][pc == i].sum() for i in range(12)])
    c /= c.sum()
    res = []
    for i in range(12):
        res.append((float(np.corrcoef(c, np.roll(MAJ, i))[0, 1]), NOTES[i] + " major"))
        res.append((float(np.corrcoef(c, np.roll(MIN, i))[0, 1]), NOTES[i] + " minor"))
    res.sort(reverse=True)
    return res[0][1], round(res[0][0], 2), res[1][1]


def sections(st, full_lufs):
    """Label 1 s short-term loudness into contiguous sections relative to the track's own integrated loudness."""
    a = np.array(st, float)
    if len(a) == 0:
        return []
    k = 4
    sm = np.convolve(np.pad(a, (k, k), mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="valid")
    lab = []
    for i, v in enumerate(sm):
        d = v - full_lufs
        slope = sm[min(len(sm) - 1, i + 3)] - sm[max(0, i - 3)]
        if d < -12:
            L = "silent/tail"
        elif d < -4:
            L = "quiet"
        elif slope > 2.5:
            L = "build"
        elif slope < -2.5:
            L = "drop"
        elif d > 1.5:
            L = "peak"
        else:
            L = "steady"
        lab.append(L)
    out, s = [], 0
    for i in range(1, len(lab) + 1):
        if i == len(lab) or lab[i] != lab[s]:
            out.append({"from": s, "to": i, "label": lab[s], "S_mean": round(float(a[s:i].mean()), 1)})
            s = i
    # merge sections shorter than 3 s into the previous one
    merged = []
    for sec in out:
        if merged and sec["to"] - sec["from"] < 3:
            merged[-1]["to"] = sec["to"]
        else:
            merged.append(sec)
    return merged


def main():
    dirs = sys.argv[1:] or sorted(os.path.join(EPI, d) for d in os.listdir(EPI)
                                   if os.path.isdir(os.path.join(EPI, d)) and d != "sfx")
    out_json = os.path.join(EPI, "ANALYSIS.json")
    data = json.load(open(out_json)) if os.path.exists(out_json) else {}
    for d in dirs:
        name = os.path.basename(d.rstrip("/"))
        wavs = sorted(f for f in os.listdir(d) if f.endswith(".wav"))
        if not wavs:
            continue
        tr = {"stems": {}}
        for w in wavs:
            stem = w[len(name) + 1:-4]
            I, tp, st = r128(os.path.join(d, w))
            tr["stems"][stem] = {"file": f"{name}/{w}", "lufs": I, "true_peak": tp, "dur_s": len(st), "short_term_1s": st}
            print(f"{name:22s} {stem:12s} I={I:6.1f} LUFS TP={tp:5.1f} dur={len(st)} s", flush=True)
        full = tr["stems"].get("full")
        if full:
            k, conf, alt = key_of(os.path.join(d, f"{name}_full.wav"))
            tr["key"], tr["key_conf"], tr["key_alt"] = k, conf, alt
            tr["sections"] = sections(full["short_term_1s"], full["lufs"])
            # per-stem activity: seconds where each stem is within 10 LU of its own loudness
            for stem, s in tr["stems"].items():
                a = np.array(s["short_term_1s"])
                s["active_pct"] = round(float((a > s["lufs"] - 10).mean() * 100), 0) if len(a) else 0
        data[name] = tr
        json.dump(data, open(out_json, "w"), indent=1)
    write_md(data)


def write_md(data):
    L = ["# Epidemic tracks — measured analysis (`tools/audio/epidemic_analyze.py`)", "",
         "Loudness = EBU R128 integrated (ffmpeg). Sections from the full mix's 1 s short-term loudness (3 s window), labelled",
         "relative to the track's own integrated loudness: quiet (< −4 LU), build/drop (±2.5 LU over 6 s), peak (> +1.5 LU).\nProfile = full-mix short-term loudness every 5 s, in LU relative to the track's LUFS-I (0 = average, + louder).",
         "Use the sections to put a cue's builds/peaks on story beats (offset into the file = `media_start`).", ""]
    for name, tr in data.items():
        L.append(f"## {name}  — key ≈ {tr.get('key','?')} (r={tr.get('key_conf','?')}, alt {tr.get('key_alt','?')})")
        L.append("")
        L.append("| stem | LUFS-I | true peak | active % |")
        L.append("|---|---|---|---|")
        for stem, s in tr["stems"].items():
            L.append(f"| {stem} | {s['lufs']} | {s['true_peak']} | {s.get('active_pct','')} |")
        L.append("")
        if tr.get("sections"):
            L.append("Sections (s): " + " · ".join(f"{x['from']}–{x['to']} {x['label']} ({x['S_mean']})" for x in tr["sections"]))
            L.append("")
            a = tr["stems"]["full"]["short_term_1s"]; I = tr["stems"]["full"]["lufs"]
            L.append("Profile (5 s steps, LU re I): " + " ".join(f"{t}:{a[t]-I:+.0f}" for t in range(0, len(a), 5)))
            L.append("")
    open(os.path.join(EPI, "ANALYSIS.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
