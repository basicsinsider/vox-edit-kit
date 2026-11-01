# assets/ivan/ivs06 — sources (segment ivs06, master 675.59–781.38)

## footage/ — BBC World Service, "Shadowmen" (`assets/ivan/footage/raw/bbc_shadowmen.mp4`), © BBC, fair use (commentary, short excerpts, credited on screen "Video: BBC World Service")
All trimmed with ffmpeg: h264 CRF 20, 24 fps, no audio. Crop `1408:792:256:130` (or `1380:776:280:154` for careful/driving/fear/redlights)
scaled to 1920×1080 — removes the BBC logo, the "AI Anonymisation" / "Actor's Voice" tags and the burned subtitles.
| file | BBC timecode (mm:ss.s of the file) | dur | what it shows | used for |
|---|---|---|---|---|
| scout.mp4 | 00:44.6 | 4.4 s | Ivan's own video: silhouette watching a military airfield at dusk | sc004 "helping Ukraine prepare attacks" |
| careful.mp4 | 47:25.5 | 3.0 s | Ivan (anonymised) from behind in a room, Marcin in the background | sc006 "very careful" |
| warsaw.mp4 | 25:32.0 | 5.6 s | Warsaw at night, Palace of Culture (crop 1056×594 at 864,100 — keeps out the burned "WARSAW POLAND"; shown as a print, native size) | sc010 |
| road_volunteers.mp4 | 25:15.2 | 5.5 s | night road from the volunteers' vehicle | sc013 |
| handler.mp4 | 54:53.6 | 4.2 s | Ivan's Ukrainian handler from behind (cap) | sc014 |
| mamon.mp4 | 28:31.0 | 4.2 s | Marcin Mamoń on a balcony reading a note | sc016 |
| driving.mp4 | 51:45.5 | 5.0 s | Ivan (anonymised) driving at night, hands on the wheel | sc020 |
| redlights.mp4 | 51:58.45 | 1.75 s | a car stopped by a figure on a night highway, hazard lights | sc021 "when he was stopped" |
| fear.mp4 | 32:37.0 | 6.0 s | Ivan's silhouette on the Bosphorus ferry ("Do you understand the word fear?") | sc025 |

## photos/
| file | subject | source | licence | author | date | size |
|---|---|---|---|---|---|---|
| dps_post_officer_car.jpg | traffic police officer and police car, Yekaterinburg | https://commons.wikimedia.org/wiki/File:Пост_ДПС_с_автоматчиком.jpg (1920 px thumb) | CC BY-SA 4.0 (credit on screen) | Иван Абатуров (Ivan Abaturov) | 2017-04-06 | 1920×1440 |
| lada_granta_side.jpg | white Lada Granta sedan, side view | https://commons.wikimedia.org/wiki/File:2013_Lada_Granta_219010_white_side.jpg (1920 px thumb) | CC0 | Throwawayacc222 | 2025-12 | 1920×744 |

## derived/ (made by `project/ivan/gen/ivs06_assets.py`)
| file | how |
|---|---|
| ee_night_warsaw_pad.jpg | `assets/maps/kit/eastern_europe_night.jpg` cropped to x 0–3251, y 1560–3840 and padded 886 px on the left with `world_night.jpg` (lon 14–20.5°E) resampled into the kit's pixel space, 80 px feathered seam. Formula: x = (lon−20)·147.768 + 886, y = (62−lat)·240 − 1560. Credit: AWS Terrain Tiles (PD), Natural Earth |
| ee_pad_borders.json | Natural Earth country outlines from `eastern_europe_overlay.svg` in the padded space (clamped to the canvas, points < 6 px apart dropped) |
| lada_cut.png | lada_granta_side.jpg cut out with a hand polygon (2 px feather) |
| lada_xray.png | same polygon; greyscale → inverted + edge-enhanced "X-ray" plate |

## facecam/
| file | how |
|---|---|
| fc_702.40.mp4 | `assets/facecam/ivan_facecam_master.mp4` −ss 702.40 −t 4.30 (re-encoded, frame-accurate) |
| fc_702.40_fg.webm / _bg.webm | `npx --yes hyperframes@0.8.217 remove-background fc_702.40.mp4 -o …_fg.webm -b …_bg.webm` (129 frames, 469 s CPU). Used in sc008 with data-media-start 0.07 (= master 702.47) |
