    /* =================== C3S092 · 479.00–484.28 · Now this is where I want to explain the situation that the Taiwanese government is in =================== */
    scene("sc092", 478.94, 484.28);
    ground("night", S(478.94));
    (function () {
      const set = $("sc092-set"), scr = $("sc092-screen");
      tl.fromTo(set, { scale: 0.97 }, { scale: 1.02, duration: 4.9, ease: "none", immediateRender: true }, S(478.94));
      tl.fromTo(scr, { scaleY: 0.012 }, { scaleY: 1, duration: 0.18, ease: "power2.out", immediateRender: true }, S(479.05));
      tl.fromTo($("sc092-cflash"), { opacity: 0.9 }, { opacity: 0, duration: 0.4, ease: "power2.out", immediateRender: true }, S(479.05));
      gated(478.9, 484.3, () => FX.weave(scr, { amp: 0.6, rot: 0.02, flicker: 0.05, seed: 92 }));
      rise($("sc092-si"), T(481.10), { dur: 0.9, y: 12 });
      [T(482.14), T(483.02)].forEach((c, i) => rise(words("sc092-tg")[i], c, { dur: 0.6, y: 8 }));
      // push-through into the screen
      tl.to(set, { scale: 3.4, duration: 0.45, ease: E.in }, S(483.83));
      out([$("sc092-si"), $("sc092-tg")], S(483.83), 0.25);
    })();

    /* =================== C3S093 · 484.28–490.84 · even though it has majority recognition, in reality it's not majority recognition =================== */
    // isotype grid shared with C3S099: 120 country squares, 71 ROC (celadon) + 48 PRC (red) + 1 open — shapes only
    const GRID = { x0: 900, y0: 200, pitch: 74, size: 58, cols: 12 };
    const KEEP = new Set([3, 10, 17, 25, 30, 38, 44, 52, 57, 63, 66, 70]);   // ROC squares that stay solid 'in reality'
    function gridSquares(svg, prefix) {
      const sq = [];
      for (let i = 0; i < 120; i++) {
        const x = GRID.x0 + (i % GRID.cols) * GRID.pitch, y = GRID.y0 + Math.floor(i / GRID.cols) * GRID.pitch;
        svg.insertAdjacentHTML("beforeend", `<rect id="${prefix}${i}" x="${x}" y="${y}" width="${GRID.size}" height="${GRID.size}" rx="4" fill="${i < 71 ? CEL : i < 119 ? RED : "none"}" fill-opacity="0" stroke="${INK}" stroke-opacity="0.22" stroke-width="2"/>`);
        sq.push({ el: document.getElementById(prefix + i), x: x + GRID.size / 2, y: y + GRID.size / 2, roc: i < 71, hollow: i < 71 && !KEEP.has(i) });
      }
      return sq;
    }
    scene("sc093", 484.28, 490.84);
    ground("paper", S(484.28));
    (function () {
      const sq = gridSquares($("sc093-svg"), "c3s03-g93-");
      sq.forEach((s, i) => { if (i < 119) tl.fromTo(s.el, { attr: { "fill-opacity": 0, "stroke-opacity": 0.22 } }, { attr: { "fill-opacity": 1, "stroke-opacity": 0.6 }, duration: 0.001, immediateRender: true }, S(486.06) + Math.floor(i / 6) / 12); });
      sq.filter((s) => s.hollow).forEach((s, j) => tl.to(s.el, { attr: { "fill-opacity": 0, stroke: CEL, "stroke-opacity": 1, "stroke-width": 5 }, duration: 0.001 }, S(488.94) + Math.floor(j / 6) / 12));
      tl.fromTo($("sc093-cam"), { scale: 1.0 }, { scale: 1.04, duration: 6.2, ease: "none", immediateRender: true }, S(484.28));
      tl.to($("sc093-cam"), { scale: 1.1, duration: 0.34, ease: E.in }, S(490.50));
      [T(486.06), T(486.86)].forEach((c, i) => rise(words("sc093-mr")[i], c, { dur: 0.8, y: 10 }));
      [T(487.82), T(487.98)].forEach((c, i) => rise(words("sc093-ir")[i], c, { dur: 0.7, y: 10 }));
      pop($("sc093-not"), T(488.94), 0.6);
    })();

    /* =================== C3S094 · 490.84–497.63 · A lot of countries say hey Taiwan is the government of China because the United States is saying that =================== */
    scene("sc094", 490.84, 497.77);
    ground("night", S(490.84));
    (function () {
      const svg = $("sc094-svg"), cam = $("sc094-cam");
      worldOutlines(svg, 0.2, 4);
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc094-fl" fill="none" stroke="${CEL}" stroke-width="6" stroke-opacity="0.75" filter="url(#c3s03-glowS)"></g><g id="c3s03-sc094-dots"></g>`);
      const [ux, uy] = wll(-98, 39), x0 = ux + 120;
      svg.insertAdjacentHTML("beforeend", `<rect id="c3s03-sc094-us" x="${ux - 120}" y="${uy - 90}" width="240" height="180" fill="${NAVY}" stroke="${SKY}" stroke-width="6" opacity="0"/>`);
      const dests = REC.r1969.filter((k) => k !== "united_states_of_america").map((k) => centerD(MAPS.world.d[k])).sort((a, b) => a[0] - b[0]);
      dests.forEach((c, i) => {
        $("sc094-dots").insertAdjacentHTML("beforeend", `<circle id="c3s03-d94-${i}" cx="${c[0].toFixed(0)}" cy="${c[1].toFixed(0)}" r="16" fill="${BONE}" opacity="0"/>`);
        attrOn($("d94-" + i), S(492.06) + Math.floor(i / 6) / 12, 0.9);
        const dx = c[0] - x0;
        ink($("sc094-fl"), `M${x0.toFixed(0)} ${uy.toFixed(0)} C${(x0 + dx * 0.45).toFixed(0)} ${uy.toFixed(0)} ${(c[0] - dx * 0.45).toFixed(0)} ${c[1].toFixed(0)} ${c[0].toFixed(0)} ${c[1].toFixed(0)}`, S(495.26) + i * 0.012, 0.8, { color: CEL, width: 6, ease: C(E.out, 0.8) });
      });
      tl.fromTo($("sc094-us"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.25, ease: C("none", 0.25), immediateRender: true }, S(495.20));
      tl.fromTo(cam, wat(12, 15, 0.47), Object.assign(wat(10, 15, 0.42), { duration: 6.9, ease: E.cam, immediateRender: true }), S(490.84));
      [T(491.90), T(492.06), T(492.14), T(492.30)].forEach((c, i) => rise(words("sc094-alc")[i], c, { dur: 0.6, y: 10 }));
      out($("sc094-alc"), S(494.90), 0.3);
      [T(495.26), T(495.58), T(495.74), T(496.14)].forEach((c, i) => rise(words("sc094-bus")[i], c, { dur: 0.6, y: 8 }));
    })();

    /* =================== C3S095 · 497.63–504.67 · Taiwan realizes … US was truly the foremost power after World War II =================== */
    scene("sc095", 497.38, 504.69);
    ground("paper", S(497.45));
    slideIn($("sc095-shot"), S(497.57));
    (function () {
      const H = [640, 430, 300, 260], L = [520, 820, 1120, 1420];
      H.forEach((h, i) => {
        const bar = $("sc095-b" + i), fl = $("sc095-f" + i), t0 = S(500.60) + i * 0.15;
        gsap.set(fl, { left: L[i] + 85 - 86, top: 900 - h - 178 });
        gsap.set(bar, { scaleY: 0 });
        tl.fromTo(bar, { scaleY: 0 }, { scaleY: 1, duration: 1.1, ease: C(E.out, 1.1), immediateRender: false }, t0);
        tl.fromTo(fl, { opacity: 0, y: h }, { opacity: 1, y: 0, duration: 1.1, ease: C(E.out, 1.1), immediateRender: true }, t0);
      });
      const cam = $("sc095-cam");
      tl.fromTo(cam, { scale: 1.0, y: 0 }, { scale: 1.02, y: 0, duration: 4.5, ease: "none", immediateRender: true }, S(497.38));
      tl.to(cam, { scale: 1.12, y: 110, duration: 1.7, ease: E.cam }, S(502.05));
      tl.to(cam, { scale: 1.13, y: 116, duration: 0.85, ease: "none" }, S(503.75));
      [T(498.45), T(499.01)].forEach((c, i) => rise(words("sc095-tr")[i], c, { dur: 0.8, y: 10 }));
      show($("sc095-fpb"), T(502.05));
      [T(502.05), T(502.69)].forEach((c, i) => rise(words("sc095-fp")[i], c, { dur: 0.6, y: 8 }));
    })();
    whip($("sc095-shot"), $("sc096-shot"), S(504.61), { dir: 1, vertical: true });

    /* =================== C3S096 · 504.67–508.83 · Doesn't matter what the USSR says. We had a bigger military, =================== */
    scene("sc096", 504.61, 508.77);
    ground("night", S(504.61));
    (function () {
      const cam = $("sc096-cam");
      gated(504.5, 508.8, () => FX.weave(cam, { amp: 1.1, flicker: 0.04, seed: 96 }));
      tl.fromTo($("sc096-a"), { scale: 1.0 }, { scale: 1.06, duration: 3.1, ease: "none", immediateRender: true }, S(504.61));
      tl.to($("sc096-a"), { filter: "brightness(0.3)", duration: 0.6, ease: C("none", 0.6) }, S(506.00));
      tl.set($("sc096-a"), { opacity: 0 }, S(507.65));                                   // hard cut on action (march → ships)
      tl.fromTo($("sc096-b"), { opacity: 0, scale: 1.0 }, { opacity: 1, scale: 1.0, duration: 0.001, immediateRender: true }, S(507.65));
      tl.to($("sc096-b"), { scale: 1.06, duration: 1.15, ease: "none" }, S(507.66));
      rise($("sc096-ussr"), T(505.41), { dur: 0.8, y: 10 });
      out($("sc096-ussr"), S(507.40), 0.25);
      [T(507.65), T(508.05)].forEach((c, i) => rise(words("sc096-bm")[i], c, { dur: 0.6, y: 10 }));
    })();

    /* =================== C3S097 · 508.83–513.23 · bigger economy, especially if you … factor in the whole Western bloc =================== */
    scene("sc097", 508.77, 513.25);
    ground("paper", S(508.77));
    (function () {
      const svg = $("sc097-svg"), acam = $("sc097-acam");
      const west = ["united_states_of_america", "canada", "united_kingdom", "france", "italy", "belgium", "netherlands", "luxembourg", "norway", "denmark", "portugal",
        "iceland", "greece", "turkey", "spain", "japan", "australia", "new_zealand", "south_korea", "philippines", "germany"];
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc097-g"></g>`);
      const ps = pathsFill($("sc097-g"), "world", west, `fill="url(#c3s03-ht-navy)" fill-opacity="0.85" stroke="${NAVY}" stroke-width="5" opacity="0"`, "c3s03-w97-")
        .sort((a, b) => centerD(a.getAttribute("d"))[0] - centerD(b.getAttribute("d"))[0]);
      ps.forEach((p, i) => attrOn(p, S(511.75) + Math.floor(i / 2) / 12));
      const aat = (lon, lat, z) => { const [x, y] = wll(lon, lat); return { x: 850 - x * z, y: 450 - y * z, scale: z }; };
      tl.fromTo(acam, aat(10, 22, 0.4), Object.assign(aat(5, 24, 0.37), { duration: 4.5, ease: "none", immediateRender: true }), S(508.77));
      const cam = $("sc097-cam");
      tl.fromTo(cam, { scale: 1.06 }, { scale: 1.06, duration: 1.5, ease: "none", immediateRender: true }, S(508.77));
      tl.to(cam, { scale: 1.0, duration: 1.4, ease: E.cam }, S(510.30));
      tl.to(cam, { scale: 0.98, duration: 1.5, ease: "none" }, S(511.70));
      tl.fromTo($("sc097-card"), { y: 160, rotation: -6, opacity: 0 }, { y: 0, rotation: -2, opacity: 1, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(508.77));
      tl.to($("sc097-card"), { x: -1700, rotation: -10, duration: 0.6, ease: E.in }, S(510.30));
      [T(508.77), T(509.17)].forEach((c, i) => rise(words("sc097-be")[i], c, { dur: 0.7, y: 10 }));
      out($("sc097-be"), S(510.30), 0.3);
      show($("sc097-wbb"), T(512.05));
      [T(512.05), T(512.45)].forEach((c, i) => rise(words("sc097-wb")[i], c, { dur: 0.45, y: 8 }));
    })();
    whip($("sc097-shot"), $("sc098-shot"), S(513.17), { dir: -1, flash: true });

    /* =================== C3S098 · 513.23–521.07 · So it was the power … when the US said something … vast majority … said the same thing =================== */
    scene("sc098", 513.17, 521.21);
    ground("night", S(513.17));
    (function () {
      const svg = $("sc098-svg"), cam = $("sc098-cam");
      worldOutlines(svg, 0.22, 4);
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc098-g" filter="url(#c3s03-glowS)"></g><g id="c3s03-sc098-us" filter="url(#c3s03-glow)"></g><g id="c3s03-sc098-rw"></g>`);
      pathsFill($("sc098-us"), "world", ["united_states_of_america"], `fill="url(#c3s03-ht-navy)" stroke="${SKY}" stroke-width="7"`, "c3s03-w98u-");
      const [ux, uy] = wll(-98, 39);
      const dests = REC.r1969.filter((k) => k !== "united_states_of_america");
      const ps = pathsFill($("sc098-g"), "world", dests, `fill="url(#c3s03-ht-sky)" stroke="${SKY}" stroke-width="4" stroke-opacity="0.8" opacity="0"`, "c3s03-w98-");
      const dist = ps.map((p) => { const c = centerD(p.getAttribute("d")); return Math.hypot(c[0] - ux, c[1] - uy); }), dmax = Math.max(...dist);
      ps.forEach((p, i) => attrOn(p, S(518.21) + Math.round((dist[i] / dmax) * 1.75 * 12) / 12));
      gated(516.3, 521.3, () => FX.radioWaves($("sc098-rw"), ux, uy, { rings: 4, max: 2600, period: 1.9, width: 26, color: SKY, from: S(516.45), to: S(521.3) }));
      tl.fromTo(cam, wat(-35, 18, 0.44), Object.assign(wat(-30, 20, 0.49), { duration: 7.9, ease: E.cam, immediateRender: true }), S(513.17));
      [T(514.37), T(514.69)].forEach((c, i) => rise(words("sc098-pw")[i], c, { dur: 0.9, y: 14 }));
      out($("sc098-pw"), S(516.25), 0.35);
      [T(520.29), T(520.53)].forEach((c, i) => rise(words("sc098-st")[i], c, { dur: 0.35, y: 8 }));
    })();

    /* =================== C3S099 · 521.07–527.23 · But that creates an issue. And that issue is if the US pulls your recognition, =================== */
    scene("sc099", 520.82, 527.23);
    ground("paper", S(520.90));
    slideIn($("sc099-shot"), S(521.01), { dist: -2000, rot: -2 });
    (function () {
      const svg = $("sc099-svg");
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc099-str"></g>`);
      const sq = gridSquares(svg, "c3s03-g99-");
      sq.forEach((s, i) => { if (i < 119) { s.el.setAttribute("fill-opacity", s.hollow ? 0 : 1); s.el.setAttribute("stroke-opacity", 0.6); }
        if (s.hollow) { s.el.setAttribute("stroke", CEL); s.el.setAttribute("stroke-opacity", 1); s.el.setAttribute("stroke-width", 5); } });
      // the US: navy-ringed flag disc on the left, strings to every 'hollow' square
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc099-us"><circle cx="500" cy="540" r="92" fill="${NAVY}" stroke="${INK}" stroke-width="4"/>
        <clipPath id="c3s03-c99"><circle cx="500" cy="540" r="80"/></clipPath><image href="assets/c3/flags/flag_us_48star_1912_1959.png" x="348" y="460" width="304" height="160" clip-path="url(#c3s03-c99)"/></g>`);
      const strs = [];
      sq.filter((s) => s.hollow).forEach((s, j) => {
        const p = ink($("sc099-str"), `M590 540 L${s.x - 29} ${s.y}`, S(521.40) + j * 0.012, 0.5, { color: INK, width: 2, opacity: 0.5 });
        strs.push({ p, s });
      });
      tl.set(strs.map((o) => o.p), { attr: { "stroke-dasharray": "none" } }, S(522.60));
      // the yank
      tl.to($("sc099-us"), { x: -330, duration: 0.3, ease: C(E.out, 0.3) }, S(524.51));
      strs.forEach(({ p, s }) => tl.to(p, { attr: { d: `M260 540 L${s.x - 29 - 22} ${s.y}` }, duration: 0.3, ease: C(E.out, 0.3) }, S(524.51)));
      tl.to(strs.map((o) => o.s.el), { x: -22, duration: 0.3, ease: C(E.out, 0.3) }, S(524.51));
      // recognition goes: the hollow squares fade to grey outlines
      strs.forEach(({ p, s }, j) => {
        const t = S(525.79) + Math.floor(j / 8) / 12;
        tl.to(s.el, { attr: { stroke: INK, "stroke-opacity": 0.25, "stroke-width": 2 }, duration: 0.001 }, t);
        tl.to(p, { attr: { opacity: 0 }, duration: 0.001 }, t);
      });
      tl.fromTo($("sc099-cam"), { scale: 1.0 }, { scale: 1.05, duration: 6.0, ease: "none", immediateRender: true }, S(520.82));
      tl.to($("sc099-cam"), { scale: 1.12, duration: 0.36, ease: E.in }, S(526.87));
      rise($("sc099-is"), T(522.13), { dur: 0.8, y: 12 });
      out($("sc099-is"), S(524.20), 0.25);
      pop($("sc099-pu"), T(524.45), 0.6);
      rise($("sc099-re"), T(525.73), { dur: 0.5, y: 8 });
    })();

    /* =================== C3S100 · 527.23–535.23 · just one country saying … a lot of countries that will start following suit =================== */
    scene("sc100", 527.23, 535.25);
    ground("night", S(527.23));
    (function () {
      const world = $("sc100-world"), flags = ["us48", "japan", "france", "italy", "belgium", "thailand", "peru", "colombia"], SP = 130;
      world.innerHTML = flags.map((f, i) => `<div class="k-dom" id="c3s03-dom${i}" style="left:${i * SP - 455}px"><div class="tp"></div><div class="fa"><div class="fl">${FL[f]}</div><div class="sh"></div></div><div class="ed"></div></div>`).join("");
      const doms = flags.map((f, i) => $("dom" + i));
      gsap.set(world, { rotationX: -14, rotationY: 50 });
      tl.fromTo(world, { x: 120, rotationY: 54 }, { x: -140, rotationY: 47, duration: 8.0, ease: "none", immediateRender: true }, S(527.23));
      // the first (US) tips onto the second and rests there
      tl.fromTo(doms[0], { rotationZ: 0 }, { rotationZ: 17, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(528.91));
      tl.fromTo(doms[1], { rotationZ: 0 }, { rotationZ: 2.5, duration: 0.16, ease: "sine.out", yoyo: true, repeat: 1, immediateRender: false }, S(529.30));
      // …and the whole row follows suit (12 fps)
      doms.forEach((d, i) => tl.to(d, { rotationZ: i === doms.length - 1 ? 84 : 66, duration: 0.24, ease: C("power2.in", 0.24) }, S(534.03) + i * 0.05));
      [T(528.85), T(529.09)].forEach((c, i) => rise(words("sc100-oc")[i], c, { dur: 0.7, y: 10 }));
      out($("sc100-oc"), S(531.60), 0.3);
      [T(533.97), T(534.53)].forEach((c, i) => rise(words("sc100-fs")[i], c, { dur: 0.35, y: 8 }));
    })();
    whip($("sc100-shot"), $("sc101-shot"), S(535.17), { dir: 1 });

    /* =================== C3S101 · 535.23–541.47 · not a big issue … remember one thing, it's the United States of America =================== */
    scene("sc101", 535.17, 541.47);
    ground("paper", S(535.17));
    (function () {
      const cam = $("sc101-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.06, duration: 5.95, ease: "none", immediateRender: true }, S(535.17));
      tl.to(cam, { scale: 1.14, duration: 0.35, ease: E.in }, S(541.12));
      [T(538.13), T(538.53), T(538.77)].forEach((c, i) => rise(words("sc101-rot")[i], c, { dur: 0.6, y: 10 }));
      tl.fromTo($("sc101-usab"), { opacity: 0, scale: 1.15 }, { opacity: 1, scale: 1, duration: 0.12, ease: "power2.in", immediateRender: true }, T(539.73));
      [T(539.73), T(540.21), T(540.61), T(540.77)].forEach((c, i) => tl.fromTo(words("sc101-usa")[i], { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: 0.12, ease: "power2.in", immediateRender: true }, c));
    })();

    /* =================== C3S102 · 541.47–544.35 · They're not gonna talk to the communist ever =================== */
    scene("sc102", 541.47, 544.49);
    ground("night", S(541.47));
    (function () {
      tl.fromTo($("sc102-cam"), { scale: 1.0 }, { scale: 1.08, duration: 3.0, ease: "none", immediateRender: true }, S(541.47));
      tl.set($("sc102-fr"), { opacity: 1 }, S(543.50));                                  // freeze on the last dial position
      tl.to($("sc102-pl"), { filter: "brightness(0.42) saturate(0.35)", duration: 0.5, ease: C("none", 0.5) }, S(543.55));
      [T(541.73), T(541.89), T(542.13)].forEach((c, i) => rise(words("sc102-ngt")[i], c, { dur: 0.4, y: 8 }));
      out($("sc102-ngt"), S(543.30), 0.2);
      rise($("sc102-ever"), T(543.49), { dur: 0.3, y: 10 });
    })();

    /* =================== C3S103 · 544.35–550.59 · That's the belief assumption that Taiwan is gonna operate under for a very, very long time =================== */
    scene("sc103", 544.10, 550.61);
    ground("paper", S(544.18));
    slideIn($("sc103-shot"), S(544.29), { from: "y", dist: 1200, rot: 0 });
    (function () {
      const cam = $("sc103-cam"), mk = $("sc103-mk");
      typeOn($("sc103-be"), T(544.93), 1 / 24);
      const f = gated(544.0, 550.7, () => FX.markupDefs(mk, "c3s03-mk103", { boil: 4 }));
      mk.setAttribute("viewBox", "0 0 4000 1080");
      FX.markup.pen(tl, mk, S(545.38), { points: [[388, 446], [560, 440], [742, 432]], dur: 0.22, width: 6, color: "#1d3f73", filter: f, seed: 103 });
      rise($("sc103-as"), T(545.57), { dur: 0.5, y: 6 });
      rise($("sc103-tabl"), T(546.45), { dur: 0.6, y: 6 });
      // dashed arrow of time, revealed through a drawn mask
      mk.insertAdjacentHTML("beforeend", `<mask id="c3s03-m103" maskUnits="userSpaceOnUse" x="0" y="0" width="4000" height="1080"><path id="c3s03-m103p" d="M1250 540 L3950 540" stroke="#fff" stroke-width="30" fill="none"/></mask>
        <path d="M1250 540 L3950 540" stroke="${INK}" stroke-width="7" stroke-dasharray="30 20" fill="none" mask="url(#c3s03-m103)"/>`);
      const mp = $("m103p"), L = 2700; mp.setAttribute("stroke-dasharray", `${L} ${L}`); mp.setAttribute("stroke-dashoffset", L);
      tl.fromTo(mp, { attr: { "stroke-dashoffset": L } }, { attr: { "stroke-dashoffset": 0 }, duration: 1.8, ease: "none", immediateRender: true }, S(548.69));
      tl.fromTo(cam, { x: 0 }, { x: -30, duration: 4.3, ease: "none", immediateRender: true }, S(544.10));
      tl.to(cam, { x: -930, duration: 2.0, ease: E.inOut }, S(548.40));
      [T(548.69), T(549.01), T(549.33), T(549.89)].forEach((c, i) => rise($("sc103-v" + (i + 1)), c, { dur: i === 3 ? 0.15 : 0.3, y: 8 }));
    })();
    whip($("sc103-shot"), $("sc104-shot"), S(550.53), { dir: 1, flash: true });

