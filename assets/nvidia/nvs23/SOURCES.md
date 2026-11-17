# nvs23 — derived assets (all made from files already in the repo; nothing downloaded)
Generator: `python3 project/nvidia/gen/nvs23_assets.py` (run from the repo root).

| file | subject | made from | licence | size |
|---|---|---|---|---|
| derived/cn_china_fill.svg, cn_china_wall.svg | China fill (red 0.45) and the "data wall" border (red-light + red glow band) in the `china_*` kit pixel space (6383×4368) | `assets/maps/kit/china_overlay.svg` #c-china | Natural Earth (PD) | vector |
| derived/wn_crop.jpg | world night relief crop 85–135°E × 36°N–2°S; x = (lon−85)·45.5111, y = (36−lat)·45.5111 | `assets/maps/kit/world_night.jpg` | AWS Terrain Tiles + Natural Earth (PD) | 2276×1729 |
| derived/ws_crop.jpg | Blue Marble desaturated crop 88–132°E × 34°N–3°S; x = (lon−88)·60, y = (34−lat)·60 | `assets/maps/kit/world_satdesat_21600.jpg` | NASA Blue Marble NG (PD) | 2640×2220 |
| derived/{wn,ws}_china_fill.svg, _china_stroke.svg, _taiwan.svg, _malaysia.svg | country fills/strokes in the two crop pixel spaces | `assets/maps/kit/world_overlay.svg` #c-china #c-taiwan #c-malaysia | Natural Earth (PD) | vector |
| derived/fc_last_2400_53.jpg | last face-cam frame (master 2400.53 s) — freeze under the end fade | `assets/facecam/nvidia_facecam_master.mp4` | own footage (Searching Lessons) | 1920×1080 |

Shared assets used (logged in their own folders): news/s15_tomshw_suitcases.jpg, news/s01_npr_resign.jpg, hardware/huawei_atlas900_superpod_1.jpg,
places/kuala_lumpur_skyline.jpg, maps/kit/aerial_johor_data_centers_z16.jpg, maps/kit/china_night.jpg, logos (flag_china, flag_malaysia, huawei,
huawei_wordmark, deepseek_wordmark, bytedance, alibaba_wordmark, tsmc, nvidia_wordmark), icons (person, hard_drive, lock, plane, suitcase,
datacenter, chip).
