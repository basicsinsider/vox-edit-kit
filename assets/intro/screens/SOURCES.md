# Screens — intro (asset gatherer B)
Each: `<name>.png` = frame with the screen made transparent (alpha, 1.2 px feather), `<name>_withbg.jpg` = original photo,
`<name>_screen.json` = screen bbox + shape in the same format as assets/textures/tv_frame_01_screen.json (plus source/licence).
- tatung_tv20cge_frame (1040x595, crop of 1280x1280) — Tatung "Audiocolor" TV-20CGE colour TV in a wood console (Taiwanese
  maker, 1970s), museum display, straight-on. https://commons.wikimedia.org/wiki/File:Tatung_TV-20CGE_20131120.jpg —
  CC BY-SA 3.0 (credit on screen). Screen = superellipse n=4. Crochet cover on top = very Taiwanese-home.
- sony_trinitron_kv1320_frame (1280x966) — Sony Trinitron KV-1320UB (early 1970s), 3/4 view on dark studio ground.
  https://commons.wikimedia.org/wiki/File:Trinitron_KV-1320UB_front.jpg — CC BY 4.0. Screen = 4-point quad (perspective);
  corner-pin footage to `screen_shape.points_xy`.
- ibm_5154_monitor_frame (3840x2160) — IBM 5154 Enhanced Color Display (PC/XT era, 1984), straight-on.
  https://commons.wikimedia.org/wiki/File:IBM_5154_-_PC_DOS_Prompt.jpg — CC0. Screen = superellipse n=4.
- tektronix_475a_scope_frame (1920x1013) — Tektronix 475A oscilloscope (1970s), straight-on, white ground.
  https://commons.wikimedia.org/wiki/File:Tektronix_Oscilloscope_475A.jpg — CC BY-SA 4.0. Screen = superellipse n=10.
Also downloaded but not keyed (angled/less clean; Commons, at /tmp only): Tatung TV-14EAD (CC BY-SA 3.0), IBM PC 5150 with
rotary phone (CC0, "Ibm computer pc 5150 (6049156797).jpg"), DEC VT100 (CC BY 2.0).
