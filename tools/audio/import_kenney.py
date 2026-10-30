#!/usr/bin/env python3
"""Convert selected CC0 Kenney.nl sounds (already extracted under assets/audio/_raw/) to
48 kHz / 24-bit WAV, peak -6 dBFS, into assets/audio/sfx/ with a 'kenney_' prefix.

Packs (CC0 1.0, no attribution required; credit 'Kenney.nl' appreciated):
  RPG Audio        https://kenney.nl/assets/rpg-audio
  Interface Sounds https://kenney.nl/assets/interface-sounds
  Impact Sounds    https://kenney.nl/assets/impact-sounds
Re-download: the zip is fetched from the 'Continue without donating' link on each page
(GET https://kenney.nl/download-link/<hex('assets/<slug>')> returns a signed URL).
Only audio is decoded (ffmpeg); nothing from the archives is executed.
"""
import glob
import os
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(__file__))
from dsp import AUDIO, Manifest, peak_norm, write, fade

FFMPEG = os.path.expanduser("~/.local/bin/ffmpeg")
RAW = os.path.join(AUDIO, "_raw")
LIC = "CC0 1.0 (public domain dedication) - Kenney.nl"
ATTR = "Optional: 'Sound effects by Kenney (kenney.nl), CC0'"

PICK = [  # (pack, file, out name, purpose)
    ("rpg-audio", "bookFlip1", "paper_page_flip_01", "Real recorded page turn (book flip) - newspaper/page reveal."),
    ("rpg-audio", "bookFlip2", "paper_page_flip_02", "Page turn variant."),
    ("rpg-audio", "bookFlip3", "paper_page_flip_03", "Page turn variant."),
    ("rpg-audio", "bookPlace1", "photo_place_01", "Book/object placed on a table - heavier alternative to photo_drop (stack of photos/papers)."),
    ("rpg-audio", "bookClose", "book_close", "Book closing - chapter end / archival document closes."),
    ("rpg-audio", "cloth1", "cloth_rustle_01", "Soft cloth/paper handling texture."),
    ("rpg-audio", "metalClick", "metal_click", "Small mechanical metal click (pin, latch, camera body)."),
    ("rpg-audio", "creak1", "gate_creak_01", "Wooden/iron creak (gate, old door, chair)."),
    ("rpg-audio", "creak3", "gate_creak_02", "Creak variant."),
    ("rpg-audio", "metalLatch", "metal_latch", "Mechanical latch - film canister / projector gate."),
    ("interface-sounds", "click_002", "ui_click_01", "Recorded soft UI click."),
    ("interface-sounds", "click_004", "ui_click_02", "Recorded soft UI click variant."),
    ("interface-sounds", "tick_002", "ui_tick_03", "Recorded tiny tick (labels / counters)."),
    ("interface-sounds", "tick_004", "ui_tick_04", "Recorded tiny tick variant."),
    ("interface-sounds", "drop_002", "ui_drop_pop_01", "Recorded water-drop-like pop (map pins, bullet points)."),
    ("interface-sounds", "drop_003", "ui_drop_pop_02", "Recorded pop variant."),
    ("interface-sounds", "scratch_002", "pen_scratch_01", "Short scratch - alternative pen tick/checkmark."),
    ("interface-sounds", "switch_002", "switch_click", "Toggle switch click (turning the oscillator/radio on)."),
    ("interface-sounds", "pluck_001", "ui_pluck_01", "Soft pluck (gentle label pop)."),
    ("impact-sounds", "impactSoft_medium_000", "impact_soft_body_01", "Soft body impact - layer under photo drops/stamps."),
    ("impact-sounds", "impactWood_light_002", "impact_wood_light_01", "Light wood knock (stamp, block landing on map)."),
    ("impact-sounds", "impactPlate_light_000", "impact_plate_light_01", "Light ceramic/plate tap."),
]

if __name__ == "__main__":
    man = Manifest("kenney")
    out_dir = os.path.join(AUDIO, "sfx")
    for pack, stem, out, purpose in PICK:
        src = glob.glob(os.path.join(RAW, f"kenney_{pack}", "**", stem + ".ogg"), recursive=True)
        if not src:
            print("missing", pack, stem)
            continue
        with tempfile.TemporaryDirectory() as td:
            tmp = os.path.join(td, "x.wav")
            subprocess.run([FFMPEG, "-v", "error", "-y", "-i", src[0], "-ar", "48000", "-c:a", "pcm_f32le", tmp], check=True)
            y, sr = sf.read(tmp)
        y = fade(y, 0.0, min(0.01, 0.15 * len(y) / sr))   # de-click the tail only
        y = peak_norm(y, -6.0)
        name = f"kenney_{out}"
        write(os.path.join(out_dir, name + ".wav"), y)
        man.add(f"sfx/{name}.wav", purpose,
                f"https://kenney.nl/assets/{pack} ({os.path.relpath(src[0], RAW)})", LIC, ATTR, tags="kenney cc0")
        print(f"{name:34s} {len(y)/sr:5.2f}s")
    man.save()
