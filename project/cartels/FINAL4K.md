# US vs Cartels — final 4K (2026-11-23): Krish's 3D renders + 4K master
Request (Krish): "Go back to the Google Doc… each part highlighted needs to be replaced in the edit with its corresponding 3D render (Drive link
in the comments)… create the final 4K render." Clarified: R4 ("with voiceover so you know exactly") covers "To answer that, we have to start with
the guy from last night…" → "…in charge of shooting and killing"; the other links are individual/shorter clips.

| render (Drive) | doc passage | used on v1 | how it was timed |
|---|---|---|---|
| R1 1JrhyW2L… (1080p 24 fps, 18 s, silent) | "All of this was happening because the Mexican army had come for one man… not related." | 31.750–44.208 (R1 4.45–16.91 s) | picture cues: Isidro's face on "El Chapo Isidro" (36.24), the El Chapo mugshot on "the famous El Chapo" (41.0); v1 = R1 t + 27.3; lanczos 2× to 4K |
| R2 1mm54Xtb… (board, 10.5 s) | "To answer that…" | inside R4 | R2 = R4's first 10 s |
| R3 1O425yI8… (+ folder 12KNa5DS…, 9 shots) | "Fausto Isidro was born in 1982…" | inside R4 | the same shots as R4 10–22 s / the folder = R4's individual shots |
| R4 16ZlZQ93… (4K 29.97 fps, 82.8 s, our v1 VO on it) | "To answer that…" → "…shooting and killing" | 117.083–199.750 | its audio matched vo_ct.wav sample-exactly (FFT xcorr): offsets 117.0857 / 117.3021 / 117.2281 / 117.3147 s in 4 pieces (3 pauses nudged by the animator) → re-timed frame by frame so the picture stays on the words |
The doc's green highlight continues ("That war is where he makes his name… big bosses"); R4 ends at "killing" → our edit resumes at 199.75 ("This war…").
Tools: `tools/ct_conform_3d.py` (→ 4K 24 fps clips on the v1 frame grid), `tools/ct_fix_assemble.py --replace FILE:G0 --only/--join --preset --crf`.
Sound: 41 SFX cued to the replaced visuals were removed (`work/final4k/sfx/`, kept: the two cut-in swells); music, ambience, VO unchanged;
beds rebuilt (`work/final4k/build_beds.sh`), levelled mix as fix 1 (`tools/ct_fix_mix.py`): −15.0 LUFS-I, LRA 3.7, peak −1.6 dBFS, ALL LIMITS MET.
Picture: 4K pieces rendered by 14 Sonnet helpers ("Cartels final 4K ctsNN", HELPER4K2_PROMPT.md, CRF 20, pushed to render4k/ctsNN — local 4K
render measured 0.65 fps, unusable), cts00 rendered locally (`tools/render_local4k.sh`); `work/final4k/collect_assemble.sh` fetches each into a
throwaway bare repo in /dev/shm, checks SHA-256, builds its v2 part (x264 faster CRF 19, no B-frames) with the 3D frames spliced in.
