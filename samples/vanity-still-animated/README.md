# Vanity still, animated (5 s)

The user's illustration (`source.jpg`, 2752×1536) turned into a 5-second shot: `vanity_animated.mp4` (1920×1080, 30 fps, silent).

`animate.py` builds every frame from the single still:
- **Watermark:** the sparkle in the bottom right is found as a lighter-than-surroundings blob and inpainted (OpenCV Telea).
- **Blinks** at 1.35 s and 3.85 s are painted onto all three eyes at once (her profile and both eyes of the reflection).
- **Masked warps:** she breathes (her chest, the reflection and the side-mirror back view, all in sync), her head nods
  slowly, the reflection's fingers work the earring, and her hand presses lightly on her cheek.
- **Camera:** a slow 7.5 % push-in toward the space between her and the reflection, plus faint dust motes in the lamplight.

Re-render: `python -I animate.py source.jpg vanity_animated.mp4` (needs numpy, opencv-python-headless, ffmpeg).
Test stills: add `--frames-at 0,1.43`.
