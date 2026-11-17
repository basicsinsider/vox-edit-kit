"""nvs21 derived maps: a Pacific-centred night plate (world_night, 110E -> 95W, 62N -> 2N, 45.5111 px/deg)
and a US-west detail layer (us_night, 126W -> 95W, 50N -> 25N, native) placed in the same pixel space.
Plate px: X = ((lon % 360) - 110) * 45.5111 ; Y = (62 - lat) * 45.5111
US layer: native us_night crop; CSS box in plate px: left (234-110)*k, top (62-50)*k, width 31*k, height 25*k."""
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
K = 45.5111
KIT = "assets/maps/kit/"
OUT = "assets/nvidia/nvs21/derived/"
w = Image.open(KIT + "world_night.jpg")
x0 = int(round((180 + 110) * K)); x1 = int(round((180 + 180) * K))
y0 = int(round((90 - 62) * K)); y1 = int(round((90 - 2) * K))
left = w.crop((x0, y0, x1, y1))                                  # 110E .. 180
right = w.crop((0, y0, int(round((180 - 95) * K)), y1))           # 180 .. 95W
plate = Image.new("RGB", (left.width + right.width, left.height))
plate.paste(left, (0, 0)); plate.paste(right, (left.width, 0))
plate.save(OUT + "pacific_us_night_plate.jpg", quality=88)
print("plate", plate.size)
u = Image.open(KIT + "us_night.jpg")
ux0 = 0; ux1 = int(round((126 - 95) * 106.533)); uy0 = 0; uy1 = int(round((50 - 25) * 133))
us = u.crop((ux0, uy0, ux1, uy1))
us.save(OUT + "us_west_night.jpg", quality=88)
print("us", us.size)
