# Mirror sample (illustrated Belle Époque style)

A 5-second sample with no captions: **a young woman looking at herself in a mirror**. It copies the art style of the
reference reel https://www.instagram.com/reel/DclYUnjR3iq/ ("Marketing tales by 2511": the Michelin Guide story),
which the user supplied as a file.

- `mirror_sample.mp4`: the render (1920×1080, 30 fps, 5.0 s, silent).
- `index.html`: the HyperFrames composition. The whole scene is hand-drawn inline SVG. One GSAP proxy tween drives
  `draw(t)`, so every frame is a pure function of time and can be seeked. RNG is seeded (no `Math.random`).
- `reference_contact_sheet.jpg`: 1 frame every 2 s of the reference reel.
- Re-render: `npx hyperframes@0.8.217 render samples/mirror-belle-epoque -o samples/mirror-belle-epoque/mirror_sample.mp4 --quality delivery`

## Analysis of the reference reel

**Format:** 75.6 s, 1276×718 (16:9 horizontal), 30 fps, AAC stereo. Narration-led, with italic sans-serif captions
centred at the bottom. Ends on a red Michelin-flower pattern card and a "MARKETING TALES BY 2511" end card on black.

**Medium:** fully animated 2D illustration, most likely AI-generated (illustrated keyframes animated with an
image-to-video model). The characters really act: they chew, write in notebooks, turn their heads and gesture.
It is not stills with camera moves.

**Art style**
- Modern editorial / storybook illustration with a ligne-claire feel. Thin, even outlines in warm dark brown, never
  pure black. Skin outlines are a lighter rust-brown.
- Flat colour fills with one soft airbrushed shading layer per form. No hard cel shadows, no texture, almost no grain.
- Characters: Belle Époque France (1900s). Big handlebar moustaches, bowler hats, high starched collars,
  three-piece suits, chef whites with a red polka-dot neckerchief. Faces are caricatured but warm: peachy-orange skin,
  rosy cheeks, small eyes with clear lids, strong noses.
- Settings are richly detailed but simplified: walnut panelling, red velvet banquettes, gilt sconces, a marble
  fireplace, Persian rugs, Haussmann façades, Tuscan-like countryside with cypress trees, vintage cars.

**Composition and camera**
- Strongly centred, symmetrical, frontal framing (Wes Anderson-like). Medium shots of one character in the centre,
  plus inserts (hands, a plate, a stamp, an open book).
- Mostly locked-off camera, sometimes a slow push-in. The motion comes from the characters acting.
- **Hard cuts only, on a steady rhythm.** Measured cuts: 1.8, 3.6, 5.7, 7.6, 9.1, 11.0, 12.9, 14.5, 16.5 s and so on.
  The average shot is about 1.85 s, and there are no transitions.

**Lighting**
- Warm tungsten interiors: glowing lamp shades and sconces with soft halos, and a gentle amber wash over everything.
- Low contrast with lifted blacks: the darkest areas are brown-black, never crushed. Soft daylight in the exteriors.
- Light is suggested by soft gradients and glows, not by cast shadows.

**Colour palette** (sampled from frames)
- Grounds: walnut `#7a4a2a` / `#4e2a15`, bottle and sage green walls `#4a5a3c`, cream tablecloths `#efe4cf`.
- Accents: Michelin red / vermilion `#c43a2a` (guide covers, velvet, the neckerchief), mustard ochre `#d8a23a`
  (the inspector's jacket), navy `#23365a` (suits, cars), gold and brass `#cf9d45`.
- Skin `#f2a679` → `#df8d66`, lips `#c2463a`, dark-brown hair masses.
- Overall: warm, saturated mid-tones, slightly sepia, with red as the recurring accent.

**Captions** (left out of the sample, as asked): lowercase italic sans-serif in warm cream with a soft dark shadow,
one short phrase at a time.

## How the sample applies it
- Three hard-cut shots (1.9 s, 1.6 s, 1.5 s), matching the reel's rhythm:
  1. Wide, symmetrical boudoir: velvet curtains, sage damask wallpaper, two glowing sconces, a gilt oval mirror and a
     vanity covered in perfume bottles and pearls. She sits with her back to us and leans in toward the glass, eyes
     lowered. Slow push-in.
  2. Over-the-shoulder into the mirror: her eyes lift to meet her own gaze, her head tilts, she blinks.
  3. Close-up on the reflection: a quiet smile, slight squint, cheeks flush, the curl at her temple sways.
- Warm-brown non-scaling outlines (2.0 / 2.6 / 3.0 px for wide / medium / close, the same on-screen weight as the
  reel), flat fills with one soft shading layer, breathing lamp glows, drifting dust motes, a soft-light warm grade,
  lifted blacks and a gentle vignette.
- This sample follows the reference's look on purpose, so it does not use the kit's documentary palette or fonts
  (and it has no text at all).

## Differences from the reference
- The reel's characters were almost certainly made with generative image and video models. This session has none,
  so the scene is hand-built vector art. The motion is limited to rigged acting (eyes, lids, mouth, head tilt,
  leaning) rather than full-body animation.
- The sample is silent. The reel has narration; a soft music or room-tone bed can be added.
