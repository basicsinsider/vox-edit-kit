# nvs18 assets (segment editor, 2026-11-17)

## photos/
| file | subject | URL | licence | author | date | size |
|---|---|---|---|---|---|---|
| kwai_tsing_cranes_2024.jpg | Kwai Tsing Container Terminals, Hong Kong — red quay cranes under a big sky (600,000 hero) | https://commons.wikimedia.org/wiki/File:Kwai_Tsing_Container_Terminals_2024_05_part1.jpg | CC BY 4.0 | Qwer132477 | 2024-05-23 | 1920x1440 (Commons 1920 px thumb) |
| kwai_tsing_night_2008.jpg | Kwai Tsing Container Terminals at night (sc007 "why?") | https://commons.wikimedia.org/wiki/File:Kwai_Tsing_Container_Terminals_at_night.JPG | CC BY-SA 3.0 | eFilm | 2008-07-12 | 1920x1440 |
| kwai_tsing_day_2019.jpg | Kwai Tsing container yard + cranes, 2019 (spare, not used in the cut) | https://commons.wikimedia.org/wiki/File:Kwai_Tsing_Container_Terminals_in_Hong_Kong.jpg | CC BY-SA 4.0 | Rehman Abubakr | 2019-10-20 | 1920x1440 |

## derived/ (made by `project/nvidia/gen/nvs18_assets.py`)
| file | from | what |
|---|---|---|
| kwai_tsing_cranes_fg.png | kwai_tsing_cranes_2024.jpg | sky keyed out (bright/unsaturated, connected to the top) → cranes/hills/city as a foreground layer in front of the numerals |
| china_night_crop.jpg + china_crop.json | assets/maps/kit/china_night.jpg + china_overlay.svg + china.json | crop x 2350–5350, y 2400–4088 (lon 97.8–130.7°E, lat 33.6–18.5°N) scaled to 2560×1440; json = China / Taiwan / Hong Kong outlines and places in crop px (credit: AWS Terrain Tiles + Natural Earth, PD) |
| huawei_hq_bantian_1920.jpg, huawei_store_1920.jpg | shared/places huawei_hq_bantian_1.jpg (CC BY-SA 3.0, fading) / huawei_store_1.jpg (CC BY 4.0) | 1920 px copies for the layered panels |
