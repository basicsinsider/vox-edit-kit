    /* =================== C3S065–066 · 324.28–335.08 · as soon as the war ended, ROC was one of the big four … maintain a post-war order =================== */
    scene("sc065", 324.22, 335.08);
    ground("paper", S(324.40));
    (function () {
      const svg = $("sc065-svg"), XS = [470, 770, 1070, 1370], BW = 190, BASE = 960, TOP = 450;
      svg.innerHTML = `<path d="M330 ${BASE} L1610 ${BASE}" stroke="${INK}" stroke-width="4"/>`;
      XS.forEach((x, i) => svg.insertAdjacentHTML("beforeend", `<rect id="c3s02-sc065-b${i}" x="${x - BW / 2}" y="${TOP}" width="${BW}" height="${BASE - TOP}" fill="${INK}" opacity="0.88"/>`));
      // the 1945 'war ends' paper (The Sun, Sydney) drops in, then slides off
      tl.fromTo($("sc065-card"), { opacity: 0, y: 500, rotation: 6 }, { opacity: 1, y: 0, rotation: -2, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(325.30));
      [T(325.50), T(325.90)].forEach((c, i) => rise(words("sc065-we")[i], c, { dur: 0.7, y: 10 }));
      tl.to($("sc065-card"), { x: -1500, rotation: -10, duration: 0.6, ease: C(E.in, 0.6) }, S(327.10));
      hide($("sc065-we"), S(327.10));
      // four equal pillars rise at 12 fps, flags on top (US 48-star, UK, USSR, ROC); the ROC pillar turns celadon
      XS.forEach((x, i) => {
        const b = $("sc065-b" + i);
        gsap.set(b, { attr: { y: BASE, height: 0 } });
        tl.fromTo(b, { attr: { y: BASE, height: 0 } }, { attr: { y: TOP, height: BASE - TOP }, duration: 1.2, ease: C(E.out, 1.2), immediateRender: false }, S(327.60) + i * 0.1);
        const f = $("sc065-f" + i); f.style.left = (x - 86) + "px"; f.style.top = (TOP - 172) + "px";
        pop(f, S(329.00) + i / 12, 0.6);
      });
      tl.to($("sc065-b3"), { attr: { fill: CEL, opacity: 1 }, duration: 0.4, ease: C(E.out, 0.4) }, S(329.02));
      [T(329.02), T(329.42)].forEach((c, i) => rise(words("sc065-bf")[i], c, { dur: 0.6, y: 12 }));
      hide($("sc065-bf"), S(330.80));
      // C3S066: FDR lowers over the US pillar — the plan was his
      const fdr = $("sc066-fdr"); fdr.style.left = (XS[0] - 115) + "px"; fdr.style.top = "70px";
      tl.fromTo(fdr, { opacity: 0, y: -360 }, { opacity: 1, y: 0, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(331.18));
      const us = $("sc066-us"); us.style.left = (XS[0] + 135) + "px"; us.style.top = "160px";
      tl.set(us, { opacity: 1 }, T(331.18));
      [T(331.18), T(331.58)].forEach((c, i) => rise(words("sc066-us")[i], c, { dur: 0.6, y: 8 }));
      $("sc066-pwo").style.left = "1480px"; $("sc066-pwo").style.top = "170px";
      rise(words("sc066-pwo")[0], T(333.90), { dur: 0.3, y: 8 });
      show(words("sc066-pwo")[1], T(334.54));
      tl.fromTo($("sc066-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "sine.inOut", immediateRender: true }, S(333.95));
      tl.fromTo($("sc065-cam"), { scale: 1.0 }, { scale: 1.08, duration: 4.5, ease: "none", immediateRender: true }, S(330.52));
    })();
    whip($("sc065-shot"), $("sc067-shot"), S(335.02), { dir: 1, flash: true });

    /* =================== C3S067–068 · 335.08–346.20 · the four policemen of the world … the United States, the UK, the Soviet Union, and the Republic of China, ROC =================== */
    scene("sc067", 335.02, 346.56);
    ground("night", S(335.04));
    (function () {
      const W = M.world, P = (lon, lat) => [(lon - W.lon0) * W.deg, (W.lat0 - lat) * W.deg];
      const cam = $("sc067-cam"), svg = $("sc067-svg");
      const fit = (s, lon, lat) => { const [cx, cy] = P(lon, lat), c = camAt(s, cx, cy);
        c.x = Math.min(0, Math.max(1920 - W.size[0] * s, c.x)); c.y = Math.min(0, Math.max(1080 - W.size[1] * s, c.y)); return c; };
      const a = fit(0.62, -30, 34), b = fit(0.5, 26, 34);
      tl.fromTo(cam, a, Object.assign(fit(0.6, -26, 34), { duration: 4.4, ease: "none", immediateRender: true }), S(335.02));
      tl.to(cam, Object.assign({}, b, { duration: 4.0, ease: E.cam }), S(339.45));
      tl.to(cam, { x: b.x - 20, duration: 2.7, ease: "none" }, S(343.45));
      // a thin bone ring orbits the world
      const [ox, oy] = P(-10, 30);
      svg.insertAdjacentHTML("beforeend", `<ellipse id="c3s02-sc067-ring" cx="${ox}" cy="${oy}" rx="2300" ry="760" fill="none" stroke="${BONE}" stroke-width="4" stroke-dasharray="60 34" opacity="0.4"/>`);
      tl.fromTo($("sc067-ring"), { attr: { "stroke-dashoffset": 0 } }, { attr: { "stroke-dashoffset": -1400 }, duration: 5.0, ease: "none", immediateRender: true }, S(335.02));
      tl.to($("sc067-ring"), { attr: { opacity: 0 }, duration: 0.6 }, S(339.0));
      [T(335.74), T(336.06)].forEach((c, i) => rise(words("sc067-fp")[i], c, { dur: 0.9, y: 16 }));
      hide($("sc067-fp"), S(337.70), 0.4);
      // four pins + labels (labels live in map space so they ride the camera)
      const four = [[-77.0, 38.9, BONE, 338.86, [T(338.86), T(339.26)]], [-0.13, 51.5, BONE, 340.78, [T(340.78)]], [37.6, 55.75, BONE, 341.98, [T(341.98), T(342.54)]],
        [118.8, 32.06, CEL, 343.82, [T(343.82), T(344.30), T(344.46), T(345.02)]]];
      const pts = [];
      four.forEach(([lon, lat, col, t, cues], i) => {
        const [x, y] = P(lon, lat); pts.push([x, y]);
        const g = pin(svg, x, y, col, 22, `c3s02-sc067-p${i}`);
        tl.fromTo(g, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(t));
        tl.fromTo(g, { y: -40 }, { y: 0, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(t));
        const lab = $("sc067-l" + i); cam.appendChild(lab);
        Object.assign(lab.style, { left: (x + 40) + "px", top: (y - 70) + "px", fontSize: "56px" });
        if (i === 1) lab.style.left = (x - 140) + "px"; if (i === 3) { lab.style.left = (x - 600) + "px"; lab.style.top = (y + 20) + "px"; lab.style.textAlign = "right"; lab.style.width = "560px"; }
        tl.set(lab, { opacity: 1 }, S(t) - 0.07);
        const ws = lab.querySelectorAll(".k-w");
        cues.forEach((c, k) => rise(ws[k], c, { dur: k === 3 ? 0.4 : 0.6, y: 8 }));
      });
      // dashed arcs tie the four together
      for (let i = 0; i < 3; i++) {
        const [x1, y1] = pts[i], [x2, y2] = pts[i + 1], mx = (x1 + x2) / 2, my = Math.min(y1, y2) - 220;
        ink(svg, `M${x1} ${y1 - 58} Q${mx} ${my} ${x2} ${y2 - 58}`, S(344.90) + i * 0.1, 0.5, { color: BONE, width: 5, opacity: 0.7 });
      }
    })();
    slideIn($("sc069-shot"), S(346.14), { from: "up" });

    /* =================== C3S069 · 346.20–352.84 · the ROC, China was also one of the founding members that had signed the UN Charter =================== */
    scene("sc069", 346.14, 352.84);
    ground("paper", S(346.40));
    (function () {
      tl.fromTo($("sc069-cam"), { scale: 1.0 }, { scale: 1.08, duration: 6.7, ease: "none", immediateRender: true }, S(346.14));
      tl.fromTo($("sc069-photo"), { y: -60, rotation: -8, opacity: 0 }, { y: 0, rotation: -3.5, opacity: 1, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(346.70));
      tl.fromTo($("sc069-clip"), { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(347.62));
      [T(349.82), T(350.30)].forEach((c, i) => rise(words("sc069-fm")[i], c, { dur: 0.8, y: 12 }));
      tl.fromTo($("sc069-box"), { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power2.in", immediateRender: true }, T(351.66));
      show(words("sc069-unc")[0], T(351.66));
      show(words("sc069-unc")[1], T(352.14));
    })();

    /* =================== C3S070 · 352.84–359.00 · It had a veto, it had a permanent seat on the UN Security Council =================== */
    scene("sc070", 352.84, 359.00);
    ground("night", S(352.84));
    (function () {
      const cam = $("sc070-cam");
      tl.fromTo(cam, camAt(0.62, 1168, 870), Object.assign(camAt(1.45, 1860, 700), { duration: 2.1, ease: E.cam, immediateRender: true }), S(352.95));
      FX.focusHunt(tl, $("sc070-img"), S(355.60), { dur: 0.8, base: "grayscale(1) sepia(0.2) contrast(1.05) brightness(0.92)" });
      tl.to(cam, Object.assign(camAt(1.2, 1760, 760), { duration: 3.9, ease: E.inOut }), S(355.10));
      const mf = gated(352.8, 359.1, () => FX.markupDefs(defs, "c3s02-mk070", { boil: 4 }));
      FX.markup.circle(tl, $("sc070-mk"), S(355.02), { cx: 1895, cy: 650, rx: 165, ry: 205, rot: -4, dur: 0.7, color: CEL, width: 12, filter: mf, seed: 7001 });
      rise(words("sc070-veto")[0], T(353.26), { dur: 0.8, y: 10 });
      [T(354.38), T(355.02)].forEach((c, i) => rise(words("sc070-ps")[i], c, { dur: 0.7, y: 10 }));
      [T(356.70), T(357.42)].forEach((c, i) => rise(words("sc070-sc")[i], c, { dur: 0.8, y: 16 }));
    })();
    whip($("sc070-shot"), $("sc071-shot"), S(358.94), { dir: -1 });

    /* =================== C3S071 · 359.00–365.40 · as soon as World War II ends, the civil war kicks off in China … =================== */
    scene("sc071", 358.94, 365.76);
    (function () {
      gated(358.94, 365.8, () => FX.weave($("sc071-wv"), { amp: 1.6, flicker: 0.06, seed: 7101 }));
      tl.fromTo($("sc071-wv"), { scale: 1.0 }, { scale: 1.06, duration: 6.8, ease: "none", immediateRender: true }, S(358.94));
      [T(361.66), T(362.06)].forEach((c, i) => rise(words("sc071-cw")[i], c, { dur: 0.8, y: 16 }));
      hide($("sc071-cw"), S(364.40), 0.5);
    })();
    slideIn($("sc072-shot"), S(365.34), { from: "left" });

    /* =================== C3S072 · 365.40–372.76 · it restarts in China, where the ROC, who are the nationalists, are fighting against the communists, which is the CCP =================== */
    scene("sc072", 365.34, 372.80);
    ground("paper", S(365.55));
    (function () {
      tl.fromTo($("sc072-cam"), { scale: 1.0 }, { scale: 1.06, duration: 7.4, ease: "none", immediateRender: true }, S(365.34));
      rise(words("sc072-rs")[0], T(365.58), { dur: 0.8, y: 10 });
      tl.fromTo($("sc072-l"), { opacity: 0, x: -260 }, { opacity: 1, x: 0, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(367.34));
      pop(words("sc072-roc")[0], T(367.34), 0.6);
      rise(words("sc072-nat")[0], T(368.38), { dur: 0.8, y: 10 });
      tl.fromTo($("sc072-r"), { opacity: 0, x: 260 }, { opacity: 1, x: 0, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(370.38));
      rise(words("sc072-com")[0], T(370.38), { dur: 0.8, y: 10 });
      pop(words("sc072-ccp")[0], T(371.66), 0.4);
    })();
    whip($("sc072-shot"), $("sc073-shot"), S(372.70), { vertical: true, dir: -1 });

    /* =================== C3S073–074 · 372.76–383.45 · over the next four years … the communists win the civil war, and the ROC … flee to the island of Taiwan =================== */
    scene("sc073", 372.70, 383.81);
    ground("night", S(372.72));
    (function () {
      const J = M.ea, cam = $("sc073-cam"), svg = $("sc073-svg"), HM = 2 * J.size[1];
      svg.innerHTML = `<defs><mask id="c3s02-burn" maskUnits="userSpaceOnUse" x="0" y="0" width="${J.size[0]}" height="${J.size[1]}"><image id="c3s02-sc073-bm" href="assets/c3/derived/c3s02/burn_mask.png" x="0" y="${-HM / 2 - 300}" width="${J.size[0]}" height="${HM}" preserveAspectRatio="none"/></mask></defs>
        <g mask="url(#c3s02-burn)"><g filter="url(#c3s02-glow)"><path d="${J.china}" fill="url(#c3s02-ht-red)" fill-opacity="0.8" stroke="${RED}" stroke-width="7" stroke-linejoin="round"/></g></g>
        <path d="${J.taiwan}" fill="none" stroke="${BONE}" stroke-width="4" stroke-dasharray="10 9" opacity="0.7"/>`;
      const fit = (s, cx, cy) => { const c = camAt(s, cx, cy); c.x = Math.min(0, Math.max(1920 - J.size[0] * s, c.x)); c.y = Math.min(0, Math.max(1080 - J.size[1] * s, c.y)); return c; };
      tl.fromTo(cam, fit(0.66, 2000, 1500), Object.assign(fit(0.56, 1900, 1750), { duration: 5.2, ease: E.cam, immediateRender: true }), S(372.70));
      // ink burns south in four steps (one per year), 12 fps
      const bm = $("sc073-bm"), edges = [700, 1500, 2400, 3500];
      edges.forEach((e, i) => tl.to(bm, { attr: { y: e - HM / 2 }, duration: 0.55, ease: C(E.out, 0.55) }, S(374.00) + i * 0.95));
      const n = $("sc073-n"); gsap.set(n, { opacity: 0 });
      show(n, T(373.50)); FX.text.count(tl, n, T(373.50), 1, 4, 0.45, (v) => String(Math.round(v)));
      rise(words("sc073-yr")[0], T(373.74), { dur: 0.6, y: 8 });
      hide([n, $("sc073-yr")], S(377.20));
      rise(words("sc073-win")[0], T(377.50), { dur: 0.6, y: 12 });
      hide($("sc073-win"), S(378.60));
      // C3S074: fast push into the strait, dissolve to the satellite plate, the flight route, Taiwan turns celadon
      const lonx = (lon) => (lon - 100) * 127.95 * J.sc, laty = (lat) => ((48 - lat) * 150 - J.oy) * J.sc;
      tl.to(cam, Object.assign(camAt(3.2, lonx(120.4), laty(24.9)), { duration: 1.1, ease: E.in }), S(378.00));
      const K = M.strait, Z = 256 * Math.pow(2, K.z);
      const mx = (lon) => (lon + 180) / 360 * Z - K.X0, my = (lat) => { const r = lat * Math.PI / 180; return (1 - Math.log(Math.tan(r) + 1 / Math.cos(r)) / Math.PI) / 2 * Z - K.Y0; };
      const sc = $("sc074-cam"), s2 = $("sc074-svg");
      const f = $("sc074-fill"); Object.assign(f.style, { left: K.tw_box[0] + "px", top: K.tw_box[1] + "px" });
      const sfit = (s, lon, lat) => { const c = camAt(s, mx(lon), my(lat)); c.x = Math.min(0, Math.max(1920 - K.size[0] * s, c.x)); c.y = Math.min(0, Math.max(1080 - K.size[1] * s, c.y)); return c; };
      const s0 = sfit(0.93, 120.4, 24.9), s1 = sfit(0.86, 120.6, 25.0), s2c = sfit(0.62, 120.9, 23.75);
      tl.fromTo(sc, Object.assign({ opacity: 0 }, s0), Object.assign({ opacity: 1 }, s0, { duration: 0.35, ease: "power1.inOut", immediateRender: true }), S(378.75));
      tl.to(sc, Object.assign({}, s1, { duration: 2.2, ease: E.cam }), S(379.10));
      tl.to(sc, Object.assign({}, s2c, { duration: 1.9, ease: E.cam }), S(381.30));
      tl.to(sc, { scale: s2c.scale * 0.985, x: s2c.x + 12, y: s2c.y + 8, duration: 0.6, ease: "none" }, S(383.20));
      FX.focusHunt(tl, $("sc074-map"), S(379.10), { dur: 0.8, base: "brightness(1.1) contrast(1.05)" });
      tl.set($("sc073-cr"), { opacity: 0 }, S(378.90)); tl.set($("sc074-cr"), { opacity: 1 }, S(378.90));
      const mf = gated(378.6, 383.9, () => FX.markupDefs(defs, "c3s02-mk074", { boil: 12 }));
      const x0 = mx(119.45), y0 = my(25.95), x1 = mx(121.55), y1 = my(25.05);
      FX.markup.pen(tl, s2, S(380.94), { points: [[x0, y0], [(x0 + x1) / 2, Math.min(y0, y1) - 40], [x1 - 30, y1 - 10]], jitter: 6, seed: 7401, dur: 1.2, width: 16, color: YEL, filter: mf, blend: "normal", ease: C(E.inOut, 1.2) });
      FX.markup.pen(tl, s2, S(382.10), { points: [[x1 - 70, y1 - 46], [x1 - 28, y1 - 10], [x1 - 78, y1 + 16]], jitter: 2, seed: 7402, dur: 0.18, width: 16, color: YEL, filter: mf, blend: "normal" });
      tl.fromTo(f, { opacity: 0 }, { opacity: 0.9, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(382.30));
      rise(words("sc074-fl")[0], T(380.94), { dur: 0.7, y: 10 });
      rise(words("sc074-tw")[0], T(382.30), { dur: 0.5, y: 14 });
    })();
    slideIn($("sc075-shot"), S(383.39));

    /* =================== C3S075 · 383.45–388.49 · they have arrived at this island, which is Taiwan. It's called Taiwan at that point too =================== */
    scene("sc075", 383.39, 388.49);
    ground("paper", S(383.60));
    (function () {
      const cam = $("sc075-cam");
      tl.fromTo($("sc075-ph"), { y: -40, rotation: -7 }, { y: 0, rotation: -3, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(383.70));
      rise(words("sc075-ar")[0], T(384.19), { dur: 0.8, y: 12 });
      tl.fromTo(cam, { x: 0 }, { x: -60, duration: 1.6, ease: "none", immediateRender: true }, S(383.39));
      tl.to(cam, { x: -1080, duration: 1.6, ease: E.cam }, S(385.10));
      tl.to(cam, { x: -1140, duration: 1.8, ease: "none" }, S(386.70));
      rise(words("sc075-tw")[0], T(386.83), { dur: 0.5, y: 10 });
      const mf = gated(383.3, 388.6, () => FX.markupDefs(defs, "c3s02-mk075", { boil: 4 }));
      FX.markup.pen(tl, $("sc075-mk"), S(386.89), { points: [[1815, 920], [1990, 914], [2140, 922]], jitter: 4, seed: 7501, dur: 0.4, width: 6, color: INK, filter: mf });
    })();

    /* =================== C3S076 · 388.49–396.89 · they are not Taiwanese … the government that's coming to the island … the government of Taiwan =================== */
    scene("sc076", 388.49, 396.89);
    ground("night", S(388.49));
    (function () {
      tl.fromTo($("sc076-cam"), { scale: 1.0 }, { scale: 1.07, duration: 8.4, ease: "none", immediateRender: true }, S(388.49));
      gated(388.49, 392.7, () => FX.weave($("sc076-w1"), { amp: 1.1, flicker: 0.04, seed: 7601 }));
      gated(392.5, 396.95, () => FX.weave($("sc076-w2"), { amp: 0.7, flicker: 0.025, seed: 7602 }));
      tl.set($("sc076-w2"), { opacity: 1 }, S(392.59)); tl.set($("sc076-w1"), { opacity: 0 }, S(392.60));
      [T(389.15), T(389.31)].forEach((c, i) => rise(words("sc076-nt")[i], c, { dur: 0.8, y: 12 }));
      hide($("sc076-nt"), S(391.90));
      rise(words("sc076-gov")[0], T(392.59), { dur: 0.9, y: 14 });
    })();
    whip($("sc076-shot"), $("sc077-shot"), S(396.83), { dir: 1, flash: true });

    /* =================== C3S077 · 396.89–404.17 · temporary problems, temporary inconvenience, but they're still the government of Taiwan =================== */
    scene("sc077", 396.83, 404.17);
    ground("paper", S(396.90));
    (function () {
      tl.fromTo($("sc077-cam"), { scale: 1.0 }, { scale: 1.07, duration: 7.3, ease: "none", immediateRender: true }, S(396.83));
      typeOn($("sc077-t1"), T(398.51));
      typeOn($("sc077-t2"), T(399.47));
      typeOn($("sc077-t3"), T(401.15));
      // strike 'problems' (fixed coordinates, checked on the snapshot)
      const x1 = 1238, x2 = 1500, y = 352;
      const mf = gated(396.8, 404.2, () => FX.markupDefs(defs, "c3s02-mk077", { boil: 4 }));
      FX.markup.pen(tl, $("sc077-mk"), S(400.80), { points: [[x1, y + 4], [x2, y - 4]], jitter: 3, seed: 7701, dur: 0.3, width: 7, color: INK, filter: mf });
      rise(words("sc077-st")[0], T(402.59), { dur: 0.6, y: 14 });
      FX.markup.pen(tl, $("sc077-mk"), S(402.95), { points: [[965, 870], [1100, 864], [1250, 872]], jitter: 4, seed: 7702, dur: 0.3, width: 7, color: INK, filter: mf });
      // hand-off to c3s03: whip right — outgoing smears off to the right by 404.17
      const wb = FX.whipDefs(defs, "c3s02-w077"), sh = $("sc077-shot"), v = { b: 0 };
      tl.set(sh, { filter: "url(#c3s02-w077)" }, S(404.00));
      tl.fromTo(sh, { x: 0, scale: 1 }, { x: 700, scale: 1.18, duration: 0.16, ease: "power3.in", immediateRender: false }, S(404.01));
      tl.fromTo(v, { b: 0 }, { b: 90, duration: 0.16, ease: "power2.in", immediateRender: false, onUpdate: () => wb.setAttribute("stdDeviation", `${v.b.toFixed(1)} 0`) }, S(404.01));
    })();
