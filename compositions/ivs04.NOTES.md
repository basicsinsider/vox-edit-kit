# ivs04 — NOTES (master 474.57–594.35, DUR 119.78) — "Ukraine reaches the aircraft" / Operation Spiderweb
Plan: `project/ivan/EDIT_NOTES_ivs04.md` (scene table, exact words, cue times). Assets + licences: `assets/ivan/ivs04/SOURCES.md`.
Generator for derived maps: `project/ivan/gen/ivs04_assets.py`. SFX markers: `compositions/ivs04.sfx.json` (45 markers, one HERO per scene).

## Checks
- Lint (0.8.217, sandbox `work/ivs04`): **0 errors in ivs04.html** (the run's 2 errors are intro02/intro03 missing face-cam files, not mine).
- `sync_audit.py --transcript transcript_iv.json`: 0 flagged; every text cue is a literal `T(word) − 0.06`, long lines word by word.
- Snapshots of every scene (start/middle/end, 9 batches of ≤ 8) looked at for words↔picture, grid, contrast, hold rule.
  Frame 0 fixed (see gotchas). Timeline = 119.78 s (`FX.mount(tl, DURATION)`).

## What I built (23 scenes)
| # | master | picture | effect / layout |
|---|---|---|---|
| sc01 | 474.57–482.49 | FACE wide → punch medium on "You see" | clean face cam, lower-third ink box (word by word) |
| sc02 | 482.49–488.65 | night map of Russia, distance rings radiate from Ukraine, airfields far out on the rings | map camera pull-out, rings drawn on (D11-style dark map) |
| sc03 | 488.65–493.04 | paper timeline: brass "June 2025" box, pen arrow "a few months before" | typeset timeline, pen markup (D05 idea) |
| sc04 | 493.04–496.96 | FACE close | "how vulnerable those airfields" |
| sc05 | 496.96–504.56 | satellite map: four airfields pulse with azure radio rings + drone triangles; push-through into Belaya → Esri z17 aerial, parked Tu-22M3s circled | radio waves (§10.6.7), push-through cut at peak velocity, focus hunt, Vox markup circles on satellite (D14) |
| sc06 | 504.56–510.32 | three phone screens (ours) playing real clips: "videos were circulating… going up in flames" | phone collage, staggered entrances, progress bars |
| sc07 | 510.32–513.60 | FACE medium, **cut-out**: a spider web draws itself on the wall behind Krish (spokes ash, threads oxblood) | remove-background sandwich (room plate → web → narrator → text) |
| sc08 | 513.60–519.60 | paper: SBU emblem + 18-month calendar grid filling at 12 fps, brass "18" | isotype calendar (ref 5 variation) |
| sc09 | 519.60–522.08 | FACE close (no text) | — |
| sc10 | 522.08–525.12 | desaturated atlas: drone route Ukraine → Ivanovo draws, red X strikes it | dashed route + markup cross |
| sc11 | 525.12–529.28 | paper: BBC/TSN truck + cabin footage in a print frame, four truck pictograms | paper slide in, push-through out |
| sc12 | 529.28–532.917 | wide atlas: ghost long routes from Ukraine, trucks drop next to all four airfields, short azure launch arcs | pins + arcs; light-flash whip into the insert |
| sc13 | 532.917–543.917 | **insert 3** full frame, thin vignette, 13 px credit "Video: Security Service of Ukraine (SBU)" | no SFX |
| sc14 | 543.917–548.28 | FACE wide | "a big hit" |
| sc15 | 548.28–552.20 | paper: Tu-95 / Tu-22M3 photo cards drop, ink / oxblood label boxes | card drop (ref 4 / D02 portraits idea) |
| sc16 | 552.20–559.39 | night map: bomber deep in Russia fires four missile arcs into Ukraine, Russia brightens, orbit ring | route arcs, region pulse |
| sc17 | 559.39–563.63 | FACE medium | "stopped building these models / decades earlier" |
| sc18 | 563.63–568.19 | SBU FPV: Tu-95 explodes, framed monitor on night, monitor shake | framed footage |
| sc19 | 568.19–571.39 | paper isotype: 41 bomber icons + counter in brass box | isotype (ref 5), `FX.text.count` |
| sc20 | 571.39–574.99 | FACE close | "how many were completely destroyed" |
| sc21 | 574.99–582.75 | paper callback: same 41 grid under an "American military intelligence" folder tab; 31 fade to ash outlines, 10 boxed, brass "10", stamp "lost forever" | isotype callback, pen box, stamp |
| sc22 | 582.75–590.11 | FACE wide → punch close at 586.83 | two lower thirds |
| sc23 | 590.11–594.35 | night map: one sky ring grows from Ukraine all the way to Belaya, Belaya pulses; camera keeps accelerating toward it | **last frame = motion** (ease-in push) for the hand-off |

Transitions used: whip (×6, incl. 2 light-flash), paper slide, push-through (×2), hard cuts on face-cam punches. Grounds never > 3 in a row.

**Face cam: 37.16 s of 108.78 s non-insert = 34.2 %** (8 shots, 2.5–7.9 s; framings wide 1.0 / medium 1.25 / close 1.55, never the
same twice in a row; slow 2.5 % push inside each shot; no grain/vignette on him — the texture overlays are set to 0 on face scenes).
First scene: face cam wide (fresh shot). Last scene: night map pushing toward Belaya with an ease-in (moving at the cut).

## Design decisions (Krish's §0 notes)
- Face-cam text = **lower-third ink box** (paper text on `--ink`, oxblood rule) at x 96, 96 px from the bottom — his wall is light grey and
  busy (posters), so text beside his head would sit on low contrast or over his shoulder; the ink box reads on anything.
- Map/footage text: Crimson italic `.clean` bone at x 96 over a bottom scrim (night) or ink over a paper scrim (atlas).
  Labels left-aligned to x 96 or to the photo/phone edge they belong to (sc06 text aligns to the first phone, sc18 to the monitor).
- One text idea at a time: each phrase fades (0.22 s) before the next.
- Colours: Russia/bombers oxblood (light shade on night), Ukraine/drones/SBU azure/sky, brass only for "June 2025", "18", "41", "10".
- No glow (`.halate`) used: no night scene has a hero title that needs it.

## Deviations / open issues for the lead
1. **`tools/build_index.py` does not discover `ivs*` compositions** (regex `(?:seg|intro|c\d+s)\d+`). I used a patched copy
   (`sed 's/(?:seg|intro|c\\d+s)/(?:seg|intro|ivs|c\\d+s)/'` → /tmp) and did not edit the shared tool. Please add `ivs` there
   (`build_master.py` is fine: it takes `--prefix ivs`).
2. `tools/make_sandbox.sh` does not link `vo_iv.mp3` / `transcript_iv.json`; I linked them by hand in `work/ivs04`.
3. ASR has no word for the name in "a few months before ___ was killed" (gap 492.00–492.40); no text there by design.
4. Insert clip: data-start 58.347 (local) = master 532.917, 11.0 s, muted; insert audio is the lead's mix.
5. Lip sync: face-cam `data-media-start` = master second (no offset added), per SEGMENTS §1. sc07 uses the cut-out pre-cut
   (media 0 = master 510.20, so `data-media-start="0.12"`).
6. Bystander clip in sc06 (phone 2) contains a cut to a second angle at ~3.5 s inside the phone — reads as a phone video; fine.

## Gotchas found (for MANUAL §4.2)
- A `scene()` helper that does `tl.fromTo(scene,{autoAlpha:0},{autoAlpha:1},0)` blacks out **frame 0** even with a `gsap.set` before
  it (seeking to 0 renders the from-state) — skip the fromTo for a scene that starts at 0.
- Scene wrappers must stay transparent: with `background` on the `.scene` div (not only the `.shot`), a paper slide hid the
  outgoing scene behind a flat paper colour (same as the c5s03 note — it bites with every slide/push).
- Commons SVG emblems: the thumb URL needs a `.png` suffix and only some widths exist (`1280px-Name.svg.png` worked, 960 did not).
- Esri z17 over an airbase (Belaya, ~340 tiles) shows individual parked bombers — good enough for markup circles at 1080p.

## Helpers worth promoting (in the composition script)
`face(id,a,b,framing)` + `FR` framings (face ≈ 860,300 in the master face cam), `fcBox(id,cues,{out})` lower-third with rule,
`dashed(svg,d,t,dur,o)` (dash-pattern route revealed through a mask stroke), `circD()` circle-as-path for drawn rings,
`planeGrid()` isotype of bomber pictograms (PLANE path), `TRUCK` pictogram.
