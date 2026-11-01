# assets/ivan/ivs04 — sources (segment ivs04, master 474.57–594.35)
All files looked at before use (contact sheets / stills). Derived files are made by `project/ivan/gen/ivs04_assets.py` or the ffmpeg
commands below. Fair-use footage = documentary commentary, short excerpts, transformed (framed, cropped, graded), credited on screen.

## photos/
| file | subject | source / URL | licence | author | size |
|---|---|---|---|---|---|
| tu95_voronezh_2014.jpg | two Tu-95 bombers overhead, Voronezh air show 2014 | https://commons.wikimedia.org/wiki/File:Tu-95_at_an_Air_show_in_Voronezh_2014.jpg (1920 px thumb) | CC BY-SA 4.0 (credit on screen) | Роман Дергунов (Roman Dergunov) | 1920×1424 |
| tu22m3_kazan_2024.jpg | Tu-22M3 (monument), Kazan, 17 Jul 2024 | https://commons.wikimedia.org/wiki/File:Kazan_Tu-22M3_2024-07-17_2192.jpg (1920 px thumb) | CC BY-SA 3.0 (credit on screen) | see file page (Commons API answered 429) | 1920×1280 |
| sbu_emblem.png | emblem of the Security Service of Ukraine | https://commons.wikimedia.org/wiki/File:Security_Service_of_Ukraine_Emblem.svg (1280 px PNG render) | CC0 / PD (state symbol) | — | 1280×1280 |

## footage/ (h264, 24 fps, no audio, keyframe every 1 s)
| file | what | source + timecode | licence | size |
|---|---|---|---|---|
| sbu_phone_burn.mp4 | SBU FPV: bomber burning on an apron, black smoke (9:16 crop) | `assets/ivan/footage/raw/src_fast.mp4` (SBU Spiderweb compilation) 4:16.0–4:22.0, crop 607×1080+800+0 → 540×960 | © Security Service of Ukraine (SBU), fair use | 6.0 s |
| sbu_phone_smoke.mp4 | SBU FPV: smoke columns over the airfield (9:16 crop) | src_fast.mp4 3:37.0–3:43.0, crop 607×1080+700+0 | © SBU, fair use | 6.0 s |
| bbc_phone_smoke.mp4 (+ _poster.jpg) | bystander video of smoke + fire over an airfield (as shown in the BBC film; 9:16 crop without BBC logo / subtitles) | `bbc_shadowmen.mp4` 36:21.5–36:26.1, crop 500×890+870+50 | © BBC World Service (bystander video), fair use | 4.6 s |
| bbc_truck.mp4 | the Spiderweb cargo truck on the road + the cabin (TSN Ukraine graphic as used by BBC), cropped above the burned subtitles | `bbc_shadowmen.mp4` 36:48.5–36:53.1, crop 1500×844+210+56 → 1920×1080 | © BBC World Service / TSN Ukraine, fair use | 4.6 s |
| sbu_tu95_explosion.mp4 | SBU FPV: Tu-95 explodes on the apron (Olenya) | src_fast.mp4 0:31.5–0:36.5 | © SBU, fair use | 5.0 s |

## facecam/
| file | what | source |
|---|---|---|
| fc_510.2_fg.webm / fc_510.2_bg.webm | narrator cut-out + room plate for sc07 (spider web drawn between them) | `assets/facecam/ivan_facecam_master.mp4` master 510.20–513.70 (`ffmpeg -ss 510.20 -t 3.5`), `npx hyperframes@0.8.217 remove-background` (105 frames, 176 s). Media time 0 = master 510.20. |

## derived/
| file | what | source |
|---|---|---|
| russia_night.jpg / russia_atlas.jpg / russia_satdesat.jpg | Russia crop lon 18–112°E, lat 30–78°N, 4278×2185, x=(lon−18)·45.5111, y=(78−lat)·45.5111 (`russia_map.json`) | map kit `world_night.jpg`, `world_atlas.jpg`, `world_satdesat_21600.jpg` (AWS Terrain Tiles PD / Natural Earth PD / NASA Blue Marble PD) |
| russia_fill_ru.png / russia_fill_ua.png / russia_edge_ua.png | Russia (oxblood) / Ukraine (sky) fills in that pixel space | `world_overlay.svg` (Natural Earth) rasterised |
| ee_fill_ru.png / ee_fill_ua.png | Russia / Ukraine fills in the eastern_europe kit pixel space (6206×4800) | `eastern_europe_overlay.svg` (Natural Earth) |
| belaya_esri_z17.jpg | Belaya air base (Irkutsk oblast) apron with parked Tu-22M3s, Esri World Imagery z17, 2326×2327 (crop of a 4352×5120 mosaic of lon 103.5504–103.5942, lat 52.8990–52.9308). Bomber centres in crop px: (665,637) (775,781) (918,984) (1060,1189) | Esri World Imagery (Esri, Maxar, Earthstar Geographics) — credit on screen |
