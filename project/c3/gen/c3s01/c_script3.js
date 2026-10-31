
    /* ============ C3S026 · 120.58–124.98 · 1965, Terman steps down ============ */
    whip("sc025", "sc026", S(120.52), { dir: 1, flash: true });
    scene("sc026", 120.52, 124.98);
    ground("night", S(120.52));
    (function () {
      gated(120.4, 125.0, () => FX.streaks($("sc026-streaks"), { seed: 2601, speed: 0.45, gain: 0.9 }));
      // odometer measures glyph widths: build it while the scene is displayed (MANUAL 4.2)
      const sc = $("sc026"); sc.style.display = "block";
      FX.text.odometer(tl, $("sc026-yr"), T(122.34) - L, { dur: 0.55, stagger: 0.04, seed: 26 });
      sc.style.display = "none";
      tl.fromTo($("sc026-card"), { x: 500, opacity: 0 }, { x: 0, opacity: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(120.6));
      pop("sc026-tn", T(123.46) - L, 0.5, 0.9);
      tl.to([$("sc026-card"), $("sc026-tn")], { y: 380, opacity: 0.3, duration: 0.43, ease: C(E.inOut, 0.43) }, S(124.02));
      wr("sc026-sd", [T(124.02) - L, T(124.42) - L], { dur: 0.45 });
      tl.fromTo($("sc026-cam"), { scale: 1 }, { scale: 1.04, duration: 4.4, ease: "none", immediateRender: false }, S(120.58));
    })();

    /* ============ C3S027 · 124.98–129.62 · everything he built (D07 collage) ============ */
    scene("sc027", 124.98, 129.7);
    ground("paper", S(124.98));
    (function () {
      ["a", "b", "c", "d"].forEach((k, i) => tl.fromTo($("sc027-" + k), { y: i % 2 ? -700 : 900, opacity: 1 }, { y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(124.98) + i * 0.1));
      const mk = $("sc027-mk");
      [[640, 160], [1250, 140], [870, 610], [1700, 200]].forEach(([x, y], i) => FX.markup.pen(tl, mk, S(125.76) + i * 0.15, { points: [[x - 34, y], [x - 8, y + 34], [x + 40, y - 40]], dur: 0.22, width: 10, color: RED, filter: PEN, jitter: 2, seed: 30 + i }));
      rise("sc027-ev", T(125.78) - L, { dur: 0.9 });
      show($("sc027-hb").firstElementChild, T(128.66) - L);
      wr("sc027-hb", [T(128.66) - L, T(128.82) - L], { dur: 0.35, y: 6 });
      tl.fromTo($("sc027-cam"), { x: 0 }, { x: -40, duration: 4.6, ease: "none", immediateRender: false }, S(124.98));
    })();

    /* ============ C3S028 · 129.62–136.90 · 1961 USGS quad: important companies ============ */
    whip("sc027", "sc028", S(129.56), { dir: -1 });
    scene("sc028", 129.56, 136.90);
    ground("night", S(129.56));
    (function () {
      tl.fromTo($("sc028-cam"), frame(950, 1700, 0.6), Object.assign({ duration: 7.3, ease: E.cam, immediateRender: true }, frame(1000, 1750, 0.68)), S(129.56));
      pop("sc028-65", T(129.94) - L, 0.6, 0.9);
      rise("sc028-gr", T(133.30) - L, { dur: 0.9 });
      const mk = $("sc028-mk");
      [[1602, 2108, 130], [1798, 1972, 110], [1700, 2050, 380]].forEach(([x, y, r], i) => FX.markup.circle(tl, mk, S(135.70) + i * 0.12, { cx: x, cy: y, rx: r, ry: r * 0.8, width: 14, color: RED, filter: MRK, dur: 0.35, seed: 280 + i }));
      wr("sc028-ic", [T(135.78) - L, T(136.18) - L], { dur: 0.4 });
    })();

    /* ============ C3S029 · 136.90–142.17 · nowhere close: a behemoth ============ */
    scene("sc029", 136.90, 142.2);
    ground("paper", S(136.90));
    (function () {
      tl.fromTo($("sc029-b1"), { scaleY: 0 }, { scaleY: 1, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(136.95));
      rise("sc029-l1", S(137.1), { dur: 0.6 });
      tl.fromTo($("sc029-th"), { opacity: 0, scaleX: 0, transformOrigin: "0 50%" }, { opacity: 1, scaleX: 1, duration: 0.6, ease: C(E.inOut, 0.6), immediateRender: true }, S(137.6));
      tl.fromTo($("sc029-b2"), { scaleY: 0 }, { scaleY: 1, duration: 1.5, ease: C(E.inOut, 1.5), immediateRender: true }, S(138.09));
      tl.fromTo($("sc029-cam"), { y: 0 }, { y: 120, duration: 1.8, ease: E.cam, immediateRender: false }, S(138.3));
      wr("sc029-nc", [T(138.09) - L, T(138.49) - L], { dur: 0.7 });
      pop("sc029-bh", T(140.73) - L, 0.6, 0.85);
      tl.to($("sc029-cam"), { y: 140, duration: 2.0, ease: "none" }, S(140.1));
    })();

    /* ============ C3S030 · 142.17–146.65 · Hoover gets some credit ============ */
    whip("sc029", "sc030", S(142.11), { dir: 1, flash: true });
    scene("sc030", 142.11, 147.2);
    ground("night", S(142.11));
    (function () {
      tl.fromTo($("sc030-cam"), { scale: 1 }, { scale: 1.06, duration: 4.5, ease: "none", immediateRender: false }, S(142.17));
      rise("sc030-h", T(142.41) - L, { dur: 1.2 });
      rise("sc030-c", T(143.69) - L, { dur: 0.9 });
    })();

    /* ============ C3S031 · 146.65–154.81 · Stanford could not charge tuition ============ */
    scene("sc031", 146.55, 154.85);
    slideIn("sc031", S(146.55), { dur: 0.5 });
    ground("paper", S(146.6));
    (function () {
      wr("sc031-cnl", [T(148.65) - L, T(148.81) - L, T(149.05) - L], { dur: 0.7 });
      wr("sc031-ct", [T(149.93) - L, T(150.41) - L], { dur: 0.6 });
      tl.fromTo($("sc031-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: C("sine.inOut", 0.4), immediateRender: true }, S(150.5));
      // the tuition bar tries to fill and can't
      tl.fromTo($("sc031-bar"), { scaleX: 0 }, { scaleX: 0.12, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(150.95));
      tl.to($("sc031-bar"), { scaleX: 0, duration: 0.4, ease: C(E.in, 0.4) }, S(151.5));
      const mk = $("sc031-mk");
      FX.markup.pen(tl, mk, S(151.95), { points: [[950, 572], [1790, 664]], dur: 0.22, width: 9, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(152.2), { points: [[1780, 568], [960, 666]], dur: 0.22, width: 9, color: INK, filter: PEN, seed: 4 });
      rise("sc031-imp", T(152.49) - L, { dur: 0.8 });
      FX.markup.pen(tl, mk, S(152.6), { points: [[900, 905], [1050, 895], [1200, 908], [1420, 896]], dur: 0.5, width: 6, color: INK, filter: PEN, seed: 12 });
      tl.fromTo($("sc031-cam"), { x: 0 }, { x: -24, duration: 8, ease: "none", immediateRender: false }, S(146.65));
    })();

    /* ============ C3S032 · 154.81–159.13 · Hoover Institution (2.5D) ============ */
    whip("sc031", "sc032", S(154.75), { vertical: true, dir: 1 });
    scene("sc032", 154.75, 159.13);
    ground("night", S(154.75));
    (function () {
      gated(154.7, 159.2, () => FX.streaks($("sc032-streaks"), { seed: 3201, speed: 0.3, gain: 0.7 }));
      tl.fromTo($("sc032-l0"), { scale: 1.0, y: 0 }, { scale: 1.04, y: 10, duration: 4.4, ease: E.cam, immediateRender: true }, S(154.75));
      tl.fromTo($("sc032-ttl"), { scale: 1.0 }, { scale: 1.06, duration: 4.4, ease: E.cam, immediateRender: false }, S(154.75));
      tl.fromTo($("sc032-l1"), { scale: 1.0, y: 0, x: 0 }, { scale: 1.14, y: -50, x: -30, duration: 4.4, ease: E.cam, immediateRender: true }, S(154.75));
      rise("sc032-hi", T(155.93) - L, { dur: 0.8 });
      rise("sc032-gp", T(157.05) - L, { dur: 0.8 });
      rise("sc032-ttl", T(158.17) - L, { dur: 0.45, y: 14 });
    })();

    /* ============ C3S033 · 159.13–165.45 · "the best… very good, very good at least" ============ */
    scene("sc033", 159.13, 165.5);
    ground("paper", S(159.13));
    (function () {
      tl.fromTo($("sc033-ph"), { x: 600, rotation: 4 }, { x: 0, rotation: -1.5, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(159.13));
      wr("sc033-td", [T(159.93) - L, T(160.09) - L, T(160.25) - L], { dur: 0.5 });
      // pen writes "best" (left-to-right wipe), strikes it, writes "very good"
      tl.fromTo($("sc033-best"), { opacity: 1, clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.45, ease: "sine.inOut", immediateRender: true }, T(161.77) - L);
      FX.markup.pen(tl, $("sc033-mk"), S(163.45), { points: [[590, 840], [860, 826]], dur: 0.2, width: 9, color: INK, filter: PEN });
      const ws = words("sc033-vg");
      [T(163.53) - L, T(163.85) - L].forEach((t, i) => tl.fromTo(ws[i], { opacity: 1, clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.35, ease: "sine.inOut", immediateRender: true }, t));
      tl.fromTo($("sc033-cam"), { scale: 1 }, { scale: 1.05, duration: 6.3, ease: "none", immediateRender: false }, S(159.13));
    })();

    /* ============ C3S034 · 165.45–168.57 · their videos (projector) ============ */
    whip("sc033", "sc034", S(165.39), { dir: 1, flash: true });
    scene("sc034", 165.39, 169.1);
    ground("night", S(165.39));
    (function () {
      tl.fromTo($("sc034-scr"), { scaleY: 0.25 }, { scaleY: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(165.39));
      tl.fromTo([$("sc034-beam"), $("sc034-img")], { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(165.62));
      tl.to($("sc034-beam"), { opacity: 0.6, duration: 1 / 24, yoyo: true, repeat: 1 }, S(165.7));
      gated(165.3, 169.1, () => FX.weave($("sc034-weave"), { amp: 1.8, flicker: 0.06, seed: 34 }));
      wr("sc034-tv", [T(165.77) - L, T(166.01) - L], { dur: 0.5 });
      rise("sc034-hi", T(167.61) - L, { dur: 0.5 });
      tl.fromTo($("sc034-cam"), { scale: 1 }, { scale: 1.04, duration: 3.1, ease: "none", immediateRender: false }, S(165.45));
    })();

    /* ============ C3S035 · 168.57–174.17 · the recipe card ============ */
    scene("sc035", 168.45, 174.25);
    slideIn("sc035", S(168.45), { dur: 0.55 });
    ground("paper", S(168.5));
    (function () {
      show("sc035-hd", T(169.13) - L);
      [["i1", T(170.49) - L], ["i2", T(171.21) - L], ["i3", T(171.85) - L], ["i3b", T(172.41) - L], ["i4", T(172.97) - L], ["i5", T(173.53) - L], ["i6", T(173.69) - L], ["i7", T(173.85) - L]].forEach(([k, t]) => show($("sc035-" + k), t));
      [["p1", 170.49], ["p2", 171.21], ["p3", 171.85]].forEach(([k, t]) => tl.fromTo($("sc035-" + k), { opacity: 0, scale: 1.15 }, { opacity: 1, scale: 1, duration: 1 / 12, immediateRender: true }, S(t) - 0.02));
      const mk = $("sc035-mk");
      FX.markup.pen(tl, mk, S(173.5), { points: [[640, 470], [760, 470]], dur: 0.2, width: 6, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(173.5) + 0.2, { points: [[740, 455], [762, 470], [740, 486]], dur: 0.1, width: 6, color: INK, filter: PEN, jitter: 1 });
      FX.markup.pen(tl, mk, S(173.85), { points: [[900, 640], [1020, 640]], dur: 0.2, width: 6, color: INK, filter: PEN, seed: 6 });
      FX.markup.pen(tl, mk, S(173.85) + 0.2, { points: [[1000, 625], [1022, 640], [1000, 656]], dur: 0.1, width: 6, color: INK, filter: PEN, jitter: 1 });
      tl.fromTo($("sc035-card"), { y: 0 }, { y: -40, duration: 5.4, ease: "none", immediateRender: false }, S(168.6));
      // the card flips over → blueprint (cont.)
      tl.to($("sc035-card"), { rotationY: 90, transformPerspective: 2200, duration: 0.24, ease: E.in }, S(173.98));
    })();

    /* ============ C3S036 · 174.17–179.37 · Silicon Valley, built by someone (blueprint) ============ */
    scene("sc036", 174.22, 179.45);
    (function () {
      tl.fromTo($("sc036-cam"), { rotationY: -90, transformPerspective: 2200, scale: 1 }, { rotationY: 0, transformPerspective: 2200, scale: 1, duration: 0.35, ease: E.out, immediateRender: false }, S(174.22));
      tl.to($("sc036-cam"), { scale: 1.05, duration: 4.7, ease: "none" }, S(174.6));
      const svg = $("sc036-svg"), BL = "rgba(234,241,246,0.85)";
      ink(svg, "M180 360 C 420 330, 520 520, 760 560 S 1120 470, 1260 600 S 1500 760, 1760 720", S(174.5), 1.5, { color: BL, width: 4, ease: C(E.inOut, 1.5) });
      ink(svg, "M180 600 C 420 590, 600 760, 860 800 S 1000 940, 1080 1000", S(174.8), 1.2, { color: BL, width: 3, ease: C(E.inOut, 1.2) });
      ink(svg, "M180 330 L180 300 M180 315 L760 315 M760 300 L760 330", S(175.6), 0.6, { color: BL, width: 3 });
      ink(svg, "M110 360 L110 600 M95 360 L125 360 M95 600 L125 600", S(175.9), 0.5, { color: BL, width: 3 });
      wr("sc036-sv", [T(175.61) - L, T(176.17) - L], { dur: 0.6 });
      rise("sc036-bb", T(176.89) - L, { dur: 0.6 });
      wr("sc036-so", [T(177.53) - L, T(177.77) - L], { dur: 0.5 });
      pop("sc036-tc", S(177.75), 0.5, 0.7);
    })();

    /* ============ C3S037 · 179.37–182.01 · a Taiwan connection (Pacific — motif master for c3s02 C3S046) ============ */
    whip("sc036", "sc037", S(179.31), { dir: 1, flash: true });
    scene("sc037", 179.31, 182.01);
    ground("night", S(179.31));
    const PAC = { stanford: [6064.5, 993.2], taiwan: [930, 1560], arcCtrl: [3500, 420] };
    (function () {
      const svg = $("sc037-svg");
      const tw = el("path", { d: TW.taiwan, fill: CEL, "fill-opacity": 0.85, stroke: CEL, "stroke-width": 6, opacity: 0 }, svg);
      tw.style.filter = "drop-shadow(0 0 6px rgba(159,199,178,0.8))";
      const [sx, sy] = PAC.stanford, [tx, ty] = PAC.taiwan;
      const pin = el("g", { opacity: 0 }, svg);
      el("circle", { cx: sx, cy: sy, r: 70, fill: "none", stroke: RED, "stroke-width": 8, opacity: 0.6 }, pin);
      el("circle", { cx: sx, cy: sy, r: 34, fill: RED, stroke: BONE, "stroke-width": 8 }, pin);
      tl.fromTo($("sc037-cam"), frame(3497, 1280, 0.40), Object.assign({ duration: 2.9, ease: E.cam, immediateRender: true }, frame(3497, 1300, 0.32)), S(179.31));
      tl.fromTo(pin, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(179.6));
      tl.fromTo(tw, { opacity: 0 }, { opacity: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(180.43));
      rise("sc037-tw", T(180.49) - L, { dur: 0.4 });
      ink(svg, `M${sx} ${sy} Q${PAC.arcCtrl[0]} ${PAC.arcCtrl[1]} ${tx + 30} ${ty - 30}`, S(181.07), 0.43, { color: BONE, width: 10, ease: C("sine.inOut", 0.43) });
      rise("sc037-cn", T(181.13) - L, { dur: 0.35 });
    })();

    /* ============ C3S038 · 182.01–185.61 · Terman teaching in the 30s ============ */
    scene("sc038", 182.01, 185.65);
    ground("paper", S(182.01));
    (function () {
      tl.fromTo($("sc038-ph"), { x: -700, rotation: -8 }, { x: 0, rotation: -2, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(182.01));
      pop("sc038-tn", T(182.25) - L, 0.6, 0.9);
      tl.fromTo($("sc038-tag"), { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: C("power3.in", 0.2), immediateRender: true }, T(184.01) - L);
      wr("sc038-bw", [T(184.57) - L, T(184.89) - L, T(185.05) - L], { dur: 0.35 });
      tl.fromTo($("sc038-cam"), { scale: 1 }, { scale: 1.05, duration: 3.6, ease: "none", immediateRender: false }, S(182.01));
    })();

    /* ============ C3S039 · 185.61–189.85 · Pan Wen-Yuan (burn reveal, celadon edge) ============ */
    whip("sc038", "sc039", S(185.55), { dir: -1 });
    scene("sc039", 185.55, 189.85);
    ground("night", S(185.55));
    (function () {
      gated(185.5, 189.9, () => FX.streaks($("sc039-streaks"), { seed: 3901, speed: 0.35, gain: 0.7, tint: [190, 230, 210] }));
      const s = $("sc039-svg");
      s.innerHTML = `<defs>
        <filter id="c3s01-b39" filterUnits="userSpaceOnUse" x="0" y="0" width="520" height="646" color-interpolation-filters="sRGB">
          <feImage href="assets/maps/burn_b.png" x="0" y="0" width="520" height="646" preserveAspectRatio="none" result="n"/>
          <feColorMatrix id="c3s01-b39m" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -12 0 0 0 13" result="t"/>
          <feComposite in="SourceGraphic" in2="t" operator="in"/></filter>
        <filter id="c3s01-c39" filterUnits="userSpaceOnUse" x="0" y="0" width="520" height="646" color-interpolation-filters="sRGB">
          <feImage href="assets/maps/burn_b.png" x="0" y="0" width="520" height="646" preserveAspectRatio="none" result="n"/>
          <feColorMatrix id="c3s01-c39a" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -12 0 0 0 13" result="e"/>
          <feColorMatrix id="c3s01-c39b" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -12 0 0 0 15.2" result="l"/>
          <feComposite in="l" in2="e" operator="arithmetic" k1="0" k2="1" k3="-1" k4="0" result="ring"/>
          <feFlood flood-color="#9fc7b2" result="fl"/><feComposite in="fl" in2="ring" operator="in" result="r2"/>
          <feGaussianBlur in="r2" stdDeviation="3" result="gl"/>
          <feMerge><feMergeNode in="gl"/><feMergeNode in="r2"/></feMerge></filter></defs>
        <g filter="url(#c3s01-b39)"><rect x="0" y="0" width="520" height="646" fill="#e9e1cf"/><image href="assets/c3/photos/pan_wen_yuan_enwiki.jpg" x="24" y="24" width="472" height="587" preserveAspectRatio="xMidYMid slice" filter="url(#c3s01-tcel)"/>
          <rect x="24" y="24" width="472" height="587" fill="url(#c3s01-ht39)" opacity="0.18"/></g>
        <rect x="0" y="0" width="520" height="646" fill="#fff" filter="url(#c3s01-c39)"/>`;
      s.insertAdjacentHTML("afterbegin", `<defs><pattern id="c3s01-ht39" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><circle cx="2.5" cy="2.5" r="1.1" fill="#1c2a24"/></pattern></defs>`);
      const M = (o) => "0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -12 0 0 0 " + o.toFixed(3);
      const b = { v: 13 }, get = (id) => document.getElementById("c3s01-" + id);
      tl.fromTo(b, { v: 13 }, { v: -2.4, duration: 2.0, ease: C("power1.inOut", 2.0), immediateRender: true, onUpdate: () => { get("b39m").setAttribute("values", M(b.v)); get("c39a").setAttribute("values", M(b.v)); get("c39b").setAttribute("values", M(b.v + 2.2)); } }, S(186.1));
      tl.fromTo($("sc039-cam"), { scale: 1.0 }, { scale: 1.05, duration: 4.3, ease: "none", immediateRender: false }, S(185.55));
      FX.focusHunt(tl, $("sc039-plate"), S(188.2), { dur: 0.6, a: 3, b: 4 });
      rise("sc039-st", T(187.69) - L, { dur: 0.5 });
      wr("sc039-pan", [T(188.09) - L, T(188.57) - L, T(188.89) - L], { dur: 0.4, y: 16 });
    })();

    /* ============ C3S040 · 189.85–193.37 · Pan + Terman (diagram motif master; C3S042 below) ============ */
    scene("sc040", 189.85, 193.40);
    ground("paper", S(189.85));
    (function () {
      pop("sc040-pan", S(189.87), 0.6, 0.7);
      pop("sc040-ter", S(190.0), 0.6, 0.7);
      show("sc040-pl", S(189.95)); show("sc040-tl", S(190.1));
      wr("sc040-bs", [T(190.49) - L, T(190.97) - L], { dur: 0.6 });
      wr("sc040-vc", [T(191.93) - L, T(192.09) - L], { dur: 0.45 });
      const svg = $("sc040-svg");
      ink(svg, "M700 402 L1222 402", S(191.93), 0.6, { width: 6, filter: PEN, ease: C(E.inOut, 0.6) });
      ink(svg, "M700 420 L1222 420", S(192.0), 0.6, { width: 6, filter: PEN, ease: C(E.inOut, 0.6) });
      gsap.set($("sc040-hew"), { opacity: 0 }); gsap.set($("sc040-bh"), { opacity: 1 });
      // push-through into the drawn line
      tl.fromTo($("sc040-cam"), { scale: 1 }, { scale: 3.6, duration: 0.42, ease: E.in, immediateRender: false }, S(192.98));
    })();

    /* ============ C3S041 · 193.37–197.13 · co-wrote papers (typeset pages, bylines only) ============ */
    scene("sc041", 193.37, 197.5);
    ground("night", S(193.37));
    (function () {
      const box = $("sc041-pages");
      const PG = [[720, 160, -7], [980, 120, 4], [1240, 170, -2]];
      PG.forEach(([x, y, r], i) => {
        const p = div(box, `left:${x}px;top:${y}px;width:560px;height:760px;background:#ece3cf;box-shadow:0 26px 50px rgba(0,0,0,0.55);transform:rotate(${r}deg);padding:50px 46px`, "q-abs",
          `<div class="t-serif" style="font-size:20px;color:#4a5260;letter-spacing:0.16em;border-bottom:2px solid #4a5260;padding-bottom:10px">PROCEEDINGS</div>
           <div style="height:16px;margin:30px 20px 0;background:rgba(20,27,36,0.55)"></div><div style="height:16px;margin:12px 80px 0;background:rgba(20,27,36,0.55)"></div>
           <div class="t-label" style="font-size:19px;color:#141b24;text-align:center;margin-top:22px;position:relative"><span style="position:relative;z-index:1">F. E. Terman and W. Y. Pan</span>${i === 2 ? '<span id="c3s01-sc041-hl" class="q-hl" style="left:228px;top:-3px;width:118px;height:26px;filter:url(#c3s01-rhl)"></span>' : ""}</div>
           <div style="display:flex;gap:22px;margin-top:30px">${[0, 1].map(() => `<div style="flex:1">${Array.from({ length: 16 }, (_, k) => `<div style="height:8px;margin-top:14px;background:rgba(20,27,36,0.28);width:${k % 6 === 5 ? 60 : 100}%"></div>`).join("")}</div>`).join("")}</div>`);
        p.style.opacity = 0;
        tl.fromTo(p, { opacity: 0, y: 300, rotation: r + 8 }, { opacity: 1, y: 0, rotation: r, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(193.37) + i * 2 / 12);
      });
      tl.fromTo($("sc041-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: C("sine.inOut", 0.35), immediateRender: true }, S(194.7));
      wr("sc041-cw", [T(193.77) - L, T(194.09) - L], { dur: 0.45 });
      rise("sc041-pp", T(194.73) - L, { dur: 0.7 });
      tl.fromTo($("sc041-cam"), { scale: 1, x: 0, y: 0 }, { scale: 1.35, x: -260, y: 60, duration: 2.6, ease: E.cam, immediateRender: false }, S(194.2));
    })();

    /* ============ C3S042 · 197.13–200.34 · + Bill Hewlett; light-flash whip hand-off to c3s02 ============ */
    scene("sc040", 197.0, SEG_END + 1);
    tl.set($("sc040"), { zIndex: 3 }, S(196.99));
    slideIn("sc040", S(197.0), { dur: 0.45 });
    ground("paper", S(197.1));
    (function () {
      tl.set([$("sc040-bs"), $("sc040-vc")], { opacity: 0 }, S(197.0));
      tl.fromTo($("sc040-cam"), { scale: 1.12 }, { scale: 0.96, duration: 2.6, ease: E.cam, immediateRender: false }, S(197.0));
      pop("sc040-hew", S(198.95), 0.6, 0.7);
      show($("sc040-bh").firstElementChild, T(198.97) - L);
      wr("sc040-bh", [T(198.97) - L, T(199.37) - L], { dur: 0.35, y: 6 });
      ink($("sc040-svg"), "M900 742 L640 512", S(199.2), 0.45, { width: 6, filter: PEN, ease: C(E.inOut, 0.45) });
      // FW: smear left + brightness ramp to bone (#f2ede3) at 200.34 (c3s02 opens on the bone frame)
      const wb = FX.whipDefs(defs, "c3s01-wend");
      tl.set($("sc040"), { filter: "url(#c3s01-wend)" }, S(200.27));
      const sb = { v: 0 };
      tl.fromTo(sb, { v: 0 }, { v: 90, duration: 0.07, ease: "power2.in", immediateRender: false, onUpdate: () => wb.setAttribute("stdDeviation", `${sb.v} 0`) }, S(200.27));
      tl.fromTo($("sc040"), { x: 0, scale: 1 }, { x: -700, scale: 1.18, duration: 0.07, ease: "power3.in", immediateRender: false }, S(200.27));
      tl.fromTo($("flash"), { opacity: 0 }, { opacity: 1, duration: 0.07, ease: "power2.in", immediateRender: false }, S(200.27));
    })();

    FX.mount(tl, DURATION);
    window.__timelines = window.__timelines || {};
    window.__timelines[SEG] = tl;
  })();
  </script>
</template>
</body>
</html>
