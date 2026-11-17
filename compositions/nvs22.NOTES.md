# nvs22 — NOTES (master 2182.542–2267.958, 85.417 s; no face cam)

Built 12 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs22.md`). Face cam 0 % (part 2 audio only). A new shot or clear
development every 2–5 s. First scene: fresh tilted night map of Malaysia (picks up nvs21's long-distance data-center line). Last scene:
B-roll footage (Grace Hopper server internals, slow push) — ends on footage, hard cut on action into nvs23.

Scenes: sc001 tilted SE-Asia night map (MALAYSIA lit, volt data-center pins KL + Johor, camera north to CHINA red, routes back south) →
sc002 push-through into the Johor aerial (Sedenak Tech Park data halls ringed in volt; park only, no operator) → sc003 GB300 NVL72 rack
hero (the one glow) → sc004 owner cards flip on their words (Malaysian flag / US flag / Howard Lutnick + ice "?") → sc005 case board
(isometric data park, OWNER / FOR RENT / CHINESE COMPANY tags, LOG IN laptop + login cable, plane arc) → sc006 three law books, ✓ stamps
on "Malaysian / Chinese / US law" → sc007 the real 7 Oct 2022 BIS rule (Federal Register p.1) with a hole cut in it on "loophole", ice
tape patch on "tried fixing it", patch drops on "smarter" → sc008 HGX H100 server, red China tags on the GPUs, volt box on "AI chips" →
sc009 RENT receipt prints, stacks rise, pen arrow up on "big business" → sc010 bars RENTED ABROAD ≈ INSIDE CHINA (COMPUTING POWER) →
sc011 B-roll data-centre pipe corridor → sc012 B-roll Grace Hopper server.

References: `ast_b15cdcc28a634241` (sc001: tilted map, one country lit with bright edge, square icon pins, labels),
`ast_91abea88b76c4b43` (sc005: dark iso card on graph paper, tags on strings, sketch cards around).
Effects: tilted 3D map camera + counter-scaled labels, route draw-on, push-through crossfade, focus hunt, pen circle/arrow/box markups,
card flips, iso drawing, luggage tags + strings, plane on a path, stamps, real-document cut-out hole + patch, 12 fps bars, receipt
print + stacks, whips (plain, light-flash), slides (x and y), hard cuts on action, footage B-roll.

Lutnick / Cantor–Bitdeer Johor story (RESEARCH §23, NYT 15 Nov 2026): NO real headline for it exists in `assets/nvidia/shared/news`
(stories go up to s15 Malaysia/suitcases) → his official PD portrait with name + "COMMERCE SECRETARY" tag and an ice "?" only, no claim
text. The renting-abroad estimate (2250 s) is UNVERIFIED → Sam's claim as bars, no source label. Johor aerial: park only, no operator.

Shared assets used: maps/kit southeast_asia_night (+ overlay → derived fills), aerial_johor_data_centers_z16 (derived desat; used in sc002
and blurred as sc004 ground); hardware gb300_nvl72_rack_render.jpg, hgx_h100_8gpu_server_open.jpg; people lutnick_cut.png; logos
flag_malaysia/flag_us/flag_china; icons datacenter, server_rack, plane, check; docs bis_rule_2022-10-07_p1.png (5th use in the video —
the story needs the actual chip-ban rule here; lead may swap); footage dc_cooling_pump_room_pipes.mp4 (CC BY 3.0 credit on screen),
server_grace_hopper_internals.mp4 (2nd use after nvs08; CC BY 3.0 credit). No new downloads; derived files in `assets/nvidia/nvs22/`
(+ SOURCES.md), generator `project/nvidia/gen/nvs22_assets.py`.

Deviations from the lead plan: sc003 (rack hero) added for "the most powerful AI chips in the world"; sc004 cards on a blurred aerial
with face-down backs from the scene start (no empty frame); sc006/sc007 boundary moved 2230.19 → 2230.80 so the US-law stamp holds
≥ 0.5 s (the page lands on "chip ban" 2230.83); sc008 (HGX server + tags) for "let Chinese companies rent AI chips"; the end
(2260.55–2267.96, "another huge reason… so close to American models") is two B-roll footage shots, as required (END on B-roll).

Checks: lint 0 errors for nvs22 (warnings: generic nested_media_start_basis_ambiguous for the two clips — values are composition-local;
composition_file_too_large); `sync_audit` → "0 cue(s) flagged" (every text cue −0.06 s); headless timeline dump `tl.duration()` =
85.417, 0 runtime errors over a full seek (0.25 s steps). Snapshots of every scene (start/middle/end) and every cut (±0.05 s) looked at.
SFX: `compositions/nvs22.sfx.json` (52 markers, all types in place_sound's vocabulary).

Gotchas (for MANUAL): (1) a tilted map plane (rotateX 22°) covers the frame if the plane div is oversize (2880×1680, offset −480/−300)
with the sea colour as its background; ease rotateX → 0 during a push-through so the flat aerial takes over cleanly. (2) Vertical
FX.whip leaves a dark band at the frame edge for ~2 frames (blur filter region + 700 px travel) — horizontal whips don't; I used
horizontal ones. (3) Dimming a card with opacity shows the busy ground through it — dim with `filter: brightness()` instead.
(4) Scenes whose objects arrive on later words show an empty ground right after a whip/slide — give them something on frame 1
(face-down cards, books/page already sliding in).
