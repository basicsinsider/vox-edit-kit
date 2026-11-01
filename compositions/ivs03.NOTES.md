# ivs03 — NOTES (segment editor, 2026-11-01)

Master 296.18–474.57 (178.39 s), composition id `ivs03`, 34 scenes (`ivs03-sc001…sc034`), plan in `project/ivan/EDIT_NOTES_ivs03.md`
(a few cuts moved by 0.1–0.35 s after the hold-rule audit; the scene table in the script is the truth).
Checks: lint 0 errors in ivs03 (the sandbox lint's 4 errors belong to ivs06 / intro02 / intro03), `sync_audit` 0 flagged (every text cue
= word start − 0.06 s), timeline dump: duration 178.39, no runtime errors, no key animation ending < 0.5 s before its transition
(only text exit-fades). Snapshots of every scene (mid + end) looked at; Krish's §0 notes checked frame by frame.

## What's on screen
| scenes | look |
|---|---|
| sc001 face W | "wasn't the only Russian" lower-third |
| sc002–003 | BBC Warsaw night (Palace of Culture) "Warsaw" → hard cut → Foma silhouette, FOMA (halate hero) |
| sc005 paper | two-column split IVAN | FOMA: grey men, Foma's grey-man network draws on and turns azure on "for Ukraine" (new layout) |
| sc006 | Kremlin St George Hall (Channel One via BBC) "powerful people in Russia" |
| sc008 cork | **investigator's wall** (ref 9 → red string): 36 index cards (= "three dozen") pinned stop-motion from Foma's card, red strings, brass "three dozen people" label-box, divider + "inside Russia"/"from abroad" with the halves dimming in turn |
| sc009 paper | redacted case file: black bars wipe off word by word to reveal RUSSIAN MILITARY FACILITIES / SENIOR OFFICERS |
| sc010 | BBC laptop street view of a Moscow residential building "where some of them actually lived" |
| sc012 paper | D06-style node chain: Ukrainian intelligence (azure) → Foma → his people → that person (oxblood), pen arrows |
| sc013–014 | BBC Foma training; night tram stop with surveillance HUD (REC, running timecode, focus box tracking a figure, "a Russian military officer") |
| sc016 night | prison-bar shadows slide over a wall, brass "25" hero, "at least … years in prison" |
| sc019 | BBC hooded man by a streetlight "looking over their shoulders" |
| sc021 paper | Kirillov case card (mil.ru portrait, CC BY 4.0), "that December" / "Igor Kirillov" + oxblood rule, focus hunt |
| sc022 | BBC: blast-damaged entrance on Ryazansky Prospekt "killed by a bomb" |
| sc023 paper | anonymous grey man in an azure ring "Ukrainian intelligence officer", CONFIRMED stamp, "behind the attack" |
| sc024 | **insert 2** full frame (`insert2.mp4`, muted), thin vignette, light grain, credit "Video: The Guardian"; light-flash whip in, whip out |
| sc026 paper | desk calendar DECEMBER, year odometer 2024 → 2025 + brass highlighter |
| sc027–028 | BBC Sarvarov portrait (shifted right on a matched grey ground, ink name "Fanil Sarvarov") → drone view of the wrecked car "beneath his car" |
| sc029 cork | wall callback: Sarvarov card, red strings from "his volunteers", azure string to a GUR card "Ukrainian intelligence services" |
| sc033 | generals in a Kremlin hall "senior military officers" → "direct the war" |
| sc034 | long-lens Moscow apartment block + crosshair HUD; focus box hunts and locks (oxblood-light) on a lit window, accelerating push into the segment cut; "back home in Moscow" → "watching them" |

Transitions: whips (horizontal, vertical, light-flash) alternating with hard cuts / cuts on action (push-in at the end of the outgoing
shot) and two paper slides; never the same twice in a row. Effects used: whips ×3 kinds, cut on action, paper slide, cork board + red
string, isotype/network draw-on, redaction wipe, node diagram + pen arrows (FX.markup.arrow, PEN boil), surveillance HUD, odometer,
highlighter, halate hero (FOMA, 25), focus hunt (×3), stop-motion pinning, slow pushes. Textures (grain/dust/vignette) on every
non-face scene; **none on the face cam**.

## Face cam — 12 shots, 54.79 s of 160.39 s non-insert = **34.2 %**
sc001 W 5.60 · sc004 C 2.11 · sc007 M 5.52 · sc011 W 5.67 · sc015 C 4.43 · sc017 M 4.84 · sc018 W 4.56 · sc020 M 4.48 · sc025 W 2.14 ·
sc030 M 5.28 · sc031 W 6.24 · sc032 C 3.92. Framing changes at every cut (W 1.0 / M 1.25 / C 1.55 around his face at 1070,330, 2–4 %
push inside). Text only on W/M shots (on C he fills the frame), lower-left on a soft dark radial scrim. Every face `<video>` uses
`assets/facecam/ivan_facecam_master.mp4` with `data-media-start` = master second — no offset added (lead does lip sync). No
remove-background shot was made (time; optional per SEGMENTS §5).

## Hand-off
- First frame: face cam W, static slow push (fresh shot). Last frame: push-in (power2.in, scale → 1.6) on a locked window of the Moscow
  block, still accelerating at 474.57 — ivs04 can cut on action.

## Deviations / decisions (Krish asleep)
- Words on screen are exactly the narrator's ("wasn't the only Russian", "where some of them actually lived" = 6 words, kept whole).
  No text on the aside "I'm pretty sure…"; "two and two together" shown.
- Dropped a planned "MOSCOW" kicker on sc022: it could not hold 0.5 s before the slide and the BBC shot can't be extended (next cut in the source).
- BBC clips are desaturated (saturate 0.35) to keep the four-colour palette (the tram-stop scene is teal in the source). Insert 2 is real colour.
- Watermarks of the original broadcasters inside the BBC film ("Popular Politics" on the Kirillov site shot, Guardian logo in the insert) are left as they are (never strip watermarks). The half-cropped "Channel One Russia" bug was cropped fully out of kremlin_hall/officers_hall instead (half a logo looked like a glitch).

## Assets
`assets/ivan/ivs03/` (25 MB): 12 BBC clips (footage/SOURCES.md, generator `project/ivan/gen/ivs03_clips.sh` + re-cuts listed there),
Kirillov portrait (Commons, CC BY 4.0, mil.ru) and a Sarvarov still (BBC). Existing: insert2, face cam, cork_01 (CC BY credited on screen).

## For the lead (tools / MANUAL §4.2 candidates)
- `tools/build_index.py`'s composition regex is `(?:seg|intro|c\d+s)\d+` — it does NOT find `ivs*` compositions (index gets duration −0.5).
  I used a sandbox-local copy with `ivs|` added (`work/ivs03/bi_local.py`); please add `ivs` to the shared tool. `tools/make_sandbox.sh`
  also doesn't link `vo_iv.mp3` / `transcript_iv.json` (I linked them by hand in the sandbox).
- BBC "Shadowmen" shots are short: almost every 4–7 s trim contained a cut. Run `ffmpeg -i clip.mp4 -vf "select='gt(scene,0.25)',showinfo" -f null -`
  on every trimmed clip and set `data-media-start`/scene length inside one shot.
- Shifting a portrait video sideways to make room for a name: put the video and a ground of its exact background colour inside one wrapper
  and apply the colour filter to the wrapper (not the video), so the seam is invisible (sc027).
- Hold-rule audit harness (puppeteer + HF's chrome-headless-shell, dumps `getChildren`): `/tmp`-only script, same method as MANUAL §4.2 (c2s02).
- Nothing for the lead to render-fix that I know of; please check lip sync on the 12 face-cam shots after the first render.
