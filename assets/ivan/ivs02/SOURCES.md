# assets/ivan/ivs02 — sources (segment ivs02, master 144.02–296.18)

All files looked at before use (contact sheets / snapshots). Fair-use items are short excerpts, transformed (cropped,
re-graded, overlaid with our graphics) and credited on screen (13 px, bottom-right).

## footage/ (h264 1920×1080, 24 fps, no audio, CRF 20)
BBC World Service, "Shadowmen — Russians working with Ukraine" (BBC Investigations, 2025), © BBC, fair use (Krish approved
short clips). Source file `assets/ivan/footage/raw/bbc_shadowmen.mp4` (1920×1080, 25 fps). Every clip is cropped so the BBC
logo, the "AI Anonymisation" / "Actor's Voice" tags and the burned subtitles are out of frame (crop 1536×864 @ 240,120, or
1500×844 @ 410,120 for the three Ivan-interview clips) and scaled back to 1920×1080. On-screen credit "Video: BBC World Service".

| file | BBC timecode (mm:ss.s) | length | what it shows | used in |
|---|---|---|---|---|
| bbc_marcin_walk.mp4 | 01:13.0–01:19.5 | 6.5 s | Marcin Mamoń walking in a street (after the BBC's own name caption) | sc002 |
| bbc_marcin_phone.mp4 | 04:46.0–04:52.0 | 6.0 s | Mamoń, silhouette, reading his phone | sc004 |
| bbc_phone_bomb.mp4 | 04:06.0–04:11.0 | 5.0 s | phone in Ivan's hand showing his video of a home-made explosive device | sc005 |
| bbc_airfield_night.mp4 | 00:50.0–00:57.0 | 7.0 s | Ivan's own night video: silhouette, airfield lights on the horizon | sc006, sc025 |
| bbc_marcin_profile.mp4 | 05:01.0–05:05.9 | 4.9 s | Mamoń in profile against a window | sc008 |
| bbc_field_meet.mp4 | 03:25.0–03:29.0 | 4.0 s | Mamoń and Ivan sitting in a field "somewhere outside Russia" (backs/anonymised) | sc010 |
| bbc_astana.mp4 | 16:59.6–17:03.4 | 3.8 s | Astana skyline (Bayterek), Kazakhstan, car passing | sc020 |
| bbc_phone_footage.mp4 | 15:45.5–15:48.9 | 3.4 s | Ivan's hands holding a phone showing his footage | sc021 |
| bbc_hooded_night.mp4 | 12:42.0–12:48.0 | 6.0 s | hooded figure by a lit wall at night | sc028 |
| bbc_cctv.mp4 | 17:03.1–17:06.05, slowed ×1.45 | 4.3 s | CCTV camera cluster (two shots) | sc029 |
| bbc_cache_dig.mp4 | 00:21.0–00:27.0 | 6.0 s | Ivan's own video: digging up a cache (canisters) at night | sc031 |
| bbc_home.mp4 | 04:38.8–04:44.4 | 5.6 s | quiet home: window, kitchen stove, hand picks up a phone | sc032 |

The Guardian, anti-war protest footage (St Petersburg, Feb 2022), © Guardian News & Media, fair use; source
`assets/ivan/footage/raw/src_protest.mp4` 01:31.1–01:36.3 (5.2 s), cropped 1500×844 @ 20,0 (Guardian logo + burned subtitles
out of frame). Credit "Video: The Guardian".

| file | what | used in |
|---|---|---|
| guardian_arrests.mp4 | police detaining protesters, riot police | sc034 |

## photos/
| file | subject | source | licence | author | date | size |
|---|---|---|---|---|---|---|
| moscow_nemtsov_march_2015.jpg | Moscow opposition march in memory of Boris Nemtsov (Kremlin tower, flags) | https://commons.wikimedia.org/wiki/File:Moscow_march_for_Nemtsov_2015-03-01_5064.jpg (1920 px thumb) | CC BY 4.0 | putnik (Wikimedia Commons, own work) | 2015-03-01 | 1920×1079 |

## derived/
| file | made from | how |
|---|---|---|
| kazan_aviation_plant_esri_z15.jpg | Esri World Imagery z15 tiles, lon 49.06–49.20 E, lat 55.83–55.89 N (Kazan aircraft plant + Borisoglebskoye airfield, Tatarstan) | `MK_CACHE=/tmp/ivs02/tiles tools/map_tiles.py fetch esri 15 …` + PIL mosaic (154 tiles, 3584×2816, web mercator; tile x0 20849, y0 10221; plant 49.13 E 55.86 N ≈ px 1772,1404). Credit "Imagery: Esri, Maxar, Earthstar Geographics". Kept at native size (> 1920 px) because sc026 shows it 1:1 after the push. |
| still_9/18/27/845/855.jpg | BBC Shadowmen frames at 00:09, 00:18, 00:27, 14:05, 14:15 (Ivan's own videos) | ffmpeg single frames, same crop, 1280×720 | 
| still_air.jpg | frame 3.0 s of bbc_airfield_night.mp4 | 1280×720 |
| mamon_circle.jpg | frame 5.6 s of bbc_marcin_walk.mp4 | crop 900×900, 400×400 |
| ee_paths.json | `assets/maps/kit/eastern_europe_overlay.svg` (Natural Earth, PD) | simplified/clamped Russia, Ukraine, Crimea, Belarus, Poland, Kazakhstan outlines in the eastern_europe kit pixel space — `project/ivan/gen/ivs02_paths.py` |

## facecam/
| file | made from | how |
|---|---|---|
| fc_239.9_fg.webm | `assets/facecam/ivan_facecam_master.mp4` master 239.9–243.9 s | ffmpeg pre-cut (deleted after use) → `npx --yes hyperframes@0.8.217 remove-background … -o fc_239.9_fg.webm --device cpu` (120 frames, 417 s on CPU). Narrator cut-out (transparent WebM, 30 fps) for sc023. |
