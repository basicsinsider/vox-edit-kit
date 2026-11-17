# assets/nvidia/nvs14 — sources (nvs14 editor, 2026-11-17)
Regenerate: `.venv/bin/python assets/nvidia/nvs14/gen_nvs14_assets.py` (from the repo root). No new downloads: every file is derived
from the map kit or the shared news folder.

| file | subject | source | licence | author | date | size |
|---|---|---|---|---|---|---|
| derived/pacific_us_night.jpg | Pacific-centred crop of the kit world night relief, 70°E–320°E (=40°W) × 82°N–40°S, 22.756 px/deg: x = (lon(+360 if <0) − 70)·22.756, y = (82 − lat)·22.756 — shows all of China and the whole US | assets/maps/kit/world_night.jpg | PD (AWS Terrain Tiles + Natural Earth) | map kit | 2026-11-17 | 5689x2776 |
| derived/pu_china.svg, derived/pu_usa.svg | China / USA outlines in that pixel space (CSS masks for the fills) | assets/maps/kit/world_overlay.svg (`#c-china`, `#c-united_states_of_america`) | PD (Natural Earth) | map kit | 2026-11-17 | 5689x2776 |
| derived/sherwood_head.jpg | crop y 990–1470 of shared/news/s11_sherwood_gpus.jpg: headline "The trillion-dollar mystery surrounding DeepSeek's Nvidia GPUs" + standfirst "There's a cloud of suspicion hanging over the type and number of Nvidia GPUs DeepSeek used to train its R1 models." | https://www.sherwood.news/tech/the-trillion-dollar-mystery-surrounding-deepseeks-nvidia-gpus/ | © Sherwood News — fair use (MANUAL §10.9), credited on screen | Sherwood News | 2025-01-29 | 1800x480 |
| derived/sherwood_photo.jpg | crop x 300–1500, y 30–930 of the same screenshot: the article's lead photo (NVIDIA + DeepSeek logos on screens) | same article | © VCG/Getty Images — fair use, credited on screen | VCG/Getty Images | 2025-01-29 | 1200x900 |

Chart data (sc012, no file): the US/China staircase points were read off the pixels of Epoch AI's published chart
"Chinese AI models have lagged the US frontier by 7 months on average since 2023" (https://epoch.ai/data-insights/us-vs-china-eci,
CC BY, PNG fetched by the previous nvs14 attempt into `work/nvs14-agent/dl/epoch_chart.png`): dot centres → date/ECI through the
chart's own axis ticks (2024/2025/2026 and ECI 100/150). Credited on screen "Data: Epoch AI · Epoch Capabilities Index (ECI) · CC BY".
