
    /* =================== C5S109 · 520.89–524.17 · Because while this vote is about to happen at the United Nations =================== */
    scene("sc109", 520.89, 524.11);
    ground("night", S(520.89));
    (function () {
      const P = 1200;
      gsap.set($("sc109-lf"), { z: -220, scale: (P + 220) / P });
      gsap.set($("sc109-ln"), { z: 140, scale: (P - 140) / P });
      tl.fromTo($("sc109-cam"), { z: -60, x: 60, rotationY: -2.2 }, { z: 170, x: -50, rotationY: 1.8, duration: 3.3, ease: E.cam, immediateRender: false }, S(520.89));
      [T(523.31), T(523.63)].forEach((c, i) => rise(words("sc109-un")[i], c, { dur: 0.45, y: 10 }));
    })();

    /* =================== C5S110 · 524.17–528.33 · Henry Kissinger is once again going to China, and this time officially =================== */
    scene("sc110", 524.11, 528.59);
    (function () {
      const camEl = $("sc110-cam");
      const at = (cx, cy, s) => ({ x: 960 - cx * s, y: 540 - cy * s, scale: s });
      tl.fromTo(camEl, at(1000, 660, 1.0), Object.assign(at(1010, 700, 1.12), { duration: 0.9, ease: E.cam, immediateRender: true }), S(524.11));
      tl.to(camEl, Object.assign(at(1040, 700, 1.32), { duration: 3.5, ease: "none" }), S(525.01));
      [T(524.11), T(524.43)].forEach((c, i) => rise(words("sc110-hk")[i], c, { dur: 0.7, y: 10 }));
      [T(525.39), T(525.55)].forEach((c, i) => rise(words("sc110-oa")[i], c, { dur: 0.8, y: 10 }));
      rise(words("sc110-ch")[0], T(526.27), { dur: 0.9, y: 12 });
      const ch = gated(527.2, 528.4, () => FX.roughDefs(defs, "c5s03-ch110", { freq: 0.045, scale: 7, choke: 0 }));
      const st = $("sc110-st"); st.style.filter = "url(#c5s03-ch110)";
      tl.fromTo(st, { opacity: 0, scale: 1.35 }, { opacity: 0.92, scale: 1, duration: 0.22, ease: "power2.in", immediateRender: true }, T(527.39));
      FX.chokeSettle(tl, ch, st, T(527.39), 8, 0.3, "none");
    })();
    paperSlide($("sc110-shot"), $("sc111-shot"), S(528.33));

    /* =================== C5S111 · 528.33–532.81 · this actually plays a big part into how the countries vote =================== */
    scene("sc111", 528.08, 532.97);
    ground("paper", S(528.33));
    (function () {
      const svg = $("sc111-svg"), dots = hemi(svg, 960, 950, "c5s03-d111-", { k: 1.12, r: 13 });
      cam($("sc111-cam"), { scale: 1.0, x: 0 }, { scale: 1.07, x: -40 }, S(528.08), 4.9);
      const sub = dots.filter((d, i) => FX.noise2(i * 0.37, 3.3, 111) > 0.42);
      gated(528.3, 533.0, () => FX.onFrame((t) => {
        const f = Math.floor(t * 12);
        sub.forEach((d, i) => { const h = FX.noise2(i * 1.7, f * 0.45, 1110); d.el.setAttribute("fill", h < 0.36 ? RED : h > 0.64 ? NAVY : GREY); });
      }));
      [T(531.47), T(532.03)].forEach((c, i) => rise(words("sc111-cv")[i], c, { dur: i ? 0.4 : 0.8, y: 10 }));
    })();
    whip($("sc111-shot"), $("sc112-shot"), S(532.81), { dir: -1, vertical: true });

    /* =================== C5S112 · 532.81–538.81 · the US ambassador to the UN is future president George H.W. Bush =================== */
    scene("sc112", 532.81, 538.81);
    ground("night", S(532.81));
    (function () {
      const camEl = $("sc112-cam");
      tl.fromTo(camEl, { scale: 1.0 }, { scale: 1.1, duration: 1.2, ease: E.cam, immediateRender: false }, S(532.81));
      FX.focusHunt(tl, camEl, S(534.02), { dur: 0.8 });
      tl.to(camEl, { scale: 1.14, duration: 4.4, ease: "none" }, S(534.01));
      tl.to(camEl, { scale: 1.2, duration: 0.4, ease: E.in }, S(538.41));
      [T(534.03), T(534.43), T(535.07), T(535.23), T(535.31)].forEach((c, i) => rise(words("sc112-amb")[i], c, { dur: 0.6, y: 8 }));
      [T(536.11), T(536.59)].forEach((c, i) => rise(words("sc112-fp")[i], c, { dur: 0.6, y: 8 }));
      [T(537.07), T(537.55), T(538.27)].forEach((c, i) => rise(words("sc112-gb")[i], c, { dur: i === 2 ? 0.35 : 0.7, y: 12 }));
    })();

    /* =================== C5S113 · 538.81–544.33 · trying his best to implement the strategy that the administration itself is saying publicly =================== */
    scene("sc113", 538.81, 544.59);
    ground("paper", S(538.81));
    (function () {
      const lines = $("sc113-lines"), r = FX.rng(11301);
      let h = `<div class="k-filler" style="left:110px;top:90px;width:520px;height:22px;filter:blur(3px)"></div><div class="k-filler" style="left:110px;top:140px;width:340px;height:16px;filter:blur(3px)"></div>`;
      for (let i = 0; i < 26; i++) {
        const y = 230 + i * 38; if (y === 572) { h += `<div class="k-filler" style="left:280px;top:${y}px;width:${620}px"></div>`; continue; }
        h += `<div class="k-filler" style="left:110px;top:${y}px;width:${i % 6 === 5 ? 380 + r() * 200 : 800 + r() * 60}px"></div>`;
      }
      lines.innerHTML = h;
      const key = $("sc113-key").querySelector("span:last-child");
      gsap.set(key, { filter: "blur(4px)", opacity: 0.55 });
      tl.to(key, { filter: "blur(0px)", opacity: 1, duration: 0.25, ease: "power1.out" }, T(543.55));
      tl.fromTo($("sc113-cam"), { scale: 1.0, y: 0 }, { scale: 1.3, y: -40, duration: 4.9, ease: E.cam, immediateRender: false }, S(538.81));
      tl.to($("sc113-cam"), { scale: 1.33, duration: 0.6, ease: "none" }, S(543.71));
      pop($("sc113-strb"), T(541.31), 0.8);
      tl.fromTo($("sc113-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: "sine.inOut", immediateRender: true }, S(543.57));
    })();
    paperSlide($("sc113-shot"), $("sc114-shot"), S(544.33));

    /* =================== C5S114 · 544.33–548.80 · bring in China to the United Nations, but they don't want to kick out Taiwan =================== */
    scene("sc114", 544.08, 548.96);
    (function () {
      const svg = $("sc114-svg");
      const tw = chair(svg, 330, 330, 1.5, "c5s03-ch114a", { fill: CEL });
      const cn = chair(svg, 1260, 330, 1.5, "c5s03-ch114b", { dash: true, fill: "rgba(0,0,0,0)" });
      $("sc114-un").style.filter = "brightness(0.25) sepia(0.3)";
      cam($("sc114-cam"), { scale: 1.0 }, { scale: 1.04 }, S(544.08), 4.9);
      tl.to(cn.cush, { attr: { fill: RED, "stroke-dasharray": "none" }, duration: 0.001 }, S(545.55));
      tl.to(cn.inner.querySelector("g"), { attr: { "stroke-dasharray": "none" }, duration: 0.001 }, S(545.55));
      tl.fromTo(cn.inner, { scale: 1.08 }, { scale: 1, svgOrigin: "110 130", duration: 0.6, ease: C(E.out, 0.6), immediateRender: false }, S(545.55));
      [T(545.07), T(545.31), T(545.55)].forEach((c, i) => rise(words("sc114-bic")[i], c, { dur: 0.7, y: 8 }));
      [T(547.15), T(547.55), T(547.71), T(547.87)].forEach((c, i) => rise(words("sc114-kot")[i], c, { dur: 0.5, y: 8 }));
      const f = gated(547.7, 549.0, () => markDefs(svg, "c5s03-mk114", "0 0 1920 1080", 4));
      FX.markup.pen(tl, svg, S(547.80), { points: [[440, 470], [485, 520], [580, 400]], dur: 0.3, width: 10, color: INK, filter: f, seed: 1141, jitter: 4 });
    })();
    whip($("sc114-shot"), $("sc115-shot"), S(548.80), { dir: 1 });

    /* =================== C5S115 · 548.80–554.00 · trying to guess some kind of compromise, and throughout the weekend before this vote =================== */
    scene("sc115", 548.80, 553.94);
    ground("night", S(548.80));
    (function () {
      const g = $("sc115-grid");
      let h = "";
      "SMTWTFS".split("").forEach((d, i) => (h += `<div class="k-cd h t-label" style="left:${i * 111}px;top:0px">${d}</div>`));
      const cell = (d) => { const k = d + 4; return [k % 7, Math.floor(k / 7)]; };
      [23, 24].forEach((d) => { const [c, rw] = cell(d); h += `<div class="k-hlbar" id="c5s03-sc115-h${d}" style="left:${c * 111 + 14}px;top:${50 + rw * 96 + 26}px;width:83px;height:50px"></div>`; });
      for (let d = 1; d <= 31; d++) { const [c, rw] = cell(d); h += `<div class="k-cd t-serif" style="left:${c * 111}px;top:${50 + rw * 96}px">${d}</div>`; }
      g.innerHTML = h;
      cam($("sc115-cam"), { scale: 1.0 }, { scale: 1.07 }, S(548.80), 4.8, E.cam);
      tl.to($("sc115-cam"), { scale: 1.12, duration: 0.4, ease: E.in }, S(553.54));
      rise(words("sc115-cmp")[0], T(550.58), { dur: 0.9, y: 10 });
      [T(552.10), T(552.26)].forEach((c, i) => rise(words("sc115-wk")[i], c, { dur: 0.8, y: 12 }));
      [23, 24].forEach((d, i) => tl.fromTo($("sc115-h" + d), { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "sine.inOut", immediateRender: true }, S(552.30) + i * 0.18));
      const mk = $("sc115-mk"), f = gated(552.8, 554.0, () => markDefs(mk, "c5s03-mk115", "0 0 880 820", 4));
      const [c25, r25] = cell(25);
      FX.markup.circle(tl, mk, S(552.90), { cx: 50 + c25 * 111 + 55, cy: 190 + 50 + r25 * 96 + 45, rx: 60, ry: 44, rot: -6, dur: 0.45, color: RED, width: 6, filter: f, seed: 1151 });
    })();

    /* =================== C5S116 · 554.00–557.84 · George Bush is … talking with all these other delegations =================== */
    scene("sc116", 553.94, 557.84);
    (function () {
      cam($("sc116-cam"), { scale: 1.0, x: 0 }, { scale: 1.07, x: -30 }, S(553.94), 3.9);
      FX.focalBlur(tl, $("sc116-blur"), [{ t: S(553.94), x: 1000, y: 520, r: 300 }, { t: S(554.3), x: 1420, y: 420, r: 320, dur: 2.6 }]);
      [T(553.94), T(554.50)].forEach((c, i) => rise(words("sc116-gb")[i], c, { dur: 0.7, y: 10 }));
      rise(words("sc116-del")[0], T(557.14), { dur: 0.35, y: 8 });
    })();
    pushThrough($("sc116-shot"), $("sc117-shot"), S(557.84));

    /* =================== C5S117 · 557.84–565.52 · telling them, hey, US policy is not abandoning Taiwan at all … let's not vote against abandoning Taiwan =================== */
    scene("sc117", 557.84, 565.68);
    ground("paper", S(557.84));
    (function () {
      const page = $("sc117-page"), r = FX.rng(11701);
      ["sc117-n1", "sc117-n2"].forEach((id) => { let h = ""; for (let i = 0; i < 80; i++) h += `<div class="k-filler" style="width:${i % 9 === 8 ? 140 + r() * 80 : 330 + r() * 50}px"></div>`; $(id).innerHTML = h; });
      let b = ""; for (let i = 0; i < 26; i++) b += `<div class="k-filler" style="position:relative;margin-bottom:15px;width:${i % 8 === 7 ? 300 : 760 + r() * 50}px"></div>`;
      $("sc117-body").innerHTML = b;
      const s0 = 2.3, cx = 570, cy = 340;
      gsap.set(page, { x: 960 - cx * s0, y: 540 - cy * s0, scale: s0 });
      tl.fromTo(page, { x: 960 - cx * s0, y: 540 - cy * s0, scale: s0 }, { x: 960 - cx * 2.36, y: 540 - cy * 2.36, scale: 2.36, duration: 0.16, ease: "none", immediateRender: false }, S(557.84));
      tl.to(page, { x: 0, y: 0, scale: 1.0, duration: 1.2, ease: C(E.inOut, 1.2) }, S(558.00));
      tl.to(page, { y: -330, duration: 5.4, ease: E.cam }, S(559.4));
      tl.to(page, { y: -350, duration: 0.8, ease: "none" }, S(564.8));
      show($("sc117-cap"), S(558.6));
      const mk = $("sc117-mk"), f = gated(558.4, 565.7, () => markDefs(mk, "c5s03-mk117", "0 0 820 1200", 4));
      const under = (pq, cues, seed) => pq.querySelectorAll(".k-w").forEach((w, i) => {
        show(w, cues[i]);
        const x = w.offsetLeft, y = pq.offsetTop + w.offsetTop + w.offsetHeight - 4, wd = w.offsetWidth - 12;
        FX.markup.pen(tl, mk, cues[i] + 0.04, { points: [[x + 4, y + 2], [x + Math.max(wd, 14), y - 1]], dur: 0.22, width: 5, color: RED, filter: f, seed: seed + i, jitter: 3 });
      });
      under($("sc117-pq"), [T(558.58), T(558.90), T(559.30), T(559.54), T(559.94), T(560.66), T(561.06), T(561.14)], 1170);
      $("sc117-q2").querySelectorAll(".k-w").forEach((w, i) => rise(w, [T(563.06), T(563.30), T(563.46), T(563.78), T(564.26), T(564.90)][i], { dur: i === 5 ? 0.3 : 0.5, y: 6 }));
    })();
    whip($("sc117-shot"), $("sc118-shot"), S(565.52), { dir: -1, vertical: true });

    /* =================== C5S118 · 565.52–572.08 · countries are having a very hard time believing that because he's just an ambassador =================== */
    scene("sc118", 565.52, 572.08);
    ground("night", S(565.52));
    (function () {
      cam($("sc118-cam"), { scale: 1.0 }, { scale: 1.07 }, S(565.52), 6.1);
      tl.to($("sc118-cam"), { scale: 1.12, duration: 0.45, ease: E.in }, S(571.63));
      [T(568.50), T(568.74), T(568.98)].forEach((c, i) => rise(words("sc118-htb")[i], c, { dur: 0.8, y: 12 }));
      const mk = $("sc118-mk"), f = gated(568.8, 572.1, () => markDefs(mk, "c5s03-mk118", "0 0 1920 1080", 4));
      const q = (x, y, s) => [[-30, -40], [-26, -70], [6, -82], [36, -64], [34, -32], [6, -12], [2, 22]].map(([a, b]) => [x + a * s, y + b * s]);
      FX.markup.pen(tl, mk, S(569.00), { points: q(700, 360, 1.6), dur: 0.5, width: 8, color: BONE, filter: f, seed: 1181, blend: "normal" });
      FX.markup.pen(tl, mk, S(569.55), { points: q(700, 435, 0.1).slice(5), dur: 0.08, width: 10, color: BONE, filter: f, seed: 1182, blend: "normal" });
      FX.markup.pen(tl, mk, S(569.30), { points: q(1210, 330, 1.4), dur: 0.5, width: 8, color: BONE, filter: f, seed: 1183, blend: "normal" });
      FX.markup.pen(tl, mk, S(569.85), { points: q(1210, 395, 0.1).slice(5), dur: 0.08, width: 10, color: BONE, filter: f, seed: 1184, blend: "normal" });
      pop($("sc118-chip"), S(570.45), 0.7);
      [T(570.58), T(570.74), T(570.90)].forEach((c, i) => rise(words("sc118-jaa")[i], c, { dur: 0.6, y: 8 }));
    })();

    /* =================== C5S119 · 572.08–577.44 · how much influence Kissinger has … the Kissinger is closer to the president =================== */
    scene("sc119", 572.08, 577.60);
    ground("paper", S(572.08));
    (function () {
      const svg = $("sc119-svg"), camEl = $("sc119-cam");
      svg.insertAdjacentHTML("beforeend", `<path d="M300 1502 L1620 1504" stroke="${INK}" stroke-width="4" opacity="0.7"/>
        <rect id="c5s03-k119b" x="520" y="1290" width="120" height="212" fill="url(#c5s03-ht-bone119)" stroke="${INK}" stroke-width="5"/>
        <rect id="c5s03-k119k" x="1190" y="1500" width="120" height="2" fill="${INK}" opacity="0.88"/>`);
      defs.insertAdjacentHTML("beforeend", `<pattern id="c5s03-ht-bone119" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="#d9d0bd"/><circle cx="7" cy="7" r="3" fill="${INK}" opacity="0.35"/></pattern>`);
      tl.fromTo(camEl, { y: -540 }, { y: -540, duration: 0.9, ease: "none", immediateRender: true }, S(572.08));
      tl.to(camEl, { y: 0, duration: 2.4, ease: E.cam }, S(573.0));
      show($("sc119-bul"), S(572.2));
      pop($("sc119-infb"), T(572.98), 0.8);
      const k = { h: 2 }, bar = $("k119k");
      tl.fromTo(k, { h: 2 }, { h: 1080, duration: 1.9, ease: C(E.out, 1.9), immediateRender: false, onUpdate: () => { bar.setAttribute("y", (1502 - k.h).toFixed(1)); bar.setAttribute("height", k.h.toFixed(1)); } }, S(573.05));
      tl.fromTo([$("sc119-ki"), $("sc119-kil")], { y: 0 }, { y: -1080, duration: 1.9, ease: C(E.out, 1.9), immediateRender: false }, S(573.05));
      rise(words("sc119-kil")[0], T(573.46), { dur: 0.6, y: 8 });
      [T(576.18), T(576.50), T(576.66), T(576.82)].forEach((c, i) => rise(words("sc119-ctp")[i], c, { dur: 0.6, y: 10 }));
      rise(words("sc119-nxl")[0], T(576.82), { dur: 0.35, y: 6 });
    })();
    whip($("sc119-shot"), $("sc120-shot"), S(577.44), { dir: 1 });

    /* =================== C5S120 · 577.44–580.40 · He's part of the administration. He's going to China =================== */
    scene("sc120", 577.44, 580.66);
    ground("night", S(577.44));
    (function () {
      cam($("sc120-cam"), { scale: 1.0 }, { scale: 1.08 }, S(577.44), 3.2);
      rise(words("sc120-adm")[0], T(578.10), { dur: 0.9, y: 10 });
      [T(579.38), T(579.70), T(579.86)].forEach((c, i) => rise(words("sc120-gtc")[i], c, { dur: i === 2 ? 0.35 : 0.5, y: 10 }));
    })();
    paperSlide($("sc120-shot"), $("sc121-shot"), S(580.40));

    /* =================== C5S121 · 580.40–583.76 · Who would you trust more? the actions or … this guy =================== */
    scene("sc121", 580.15, 583.76);
    ground("paper", S(580.40));
    (function () {
      cam($("sc121-cam"), { scale: 1.0 }, { scale: 1.03 }, S(580.15), 3.6);
      cam($("sc121-a"), { y: 10 }, { y: -10 }, S(580.15), 3.6);
      cam($("sc121-b"), { y: -8 }, { y: 12 }, S(580.15), 3.6);
      tl.to($("sc121-cam"), { scale: 1.08, duration: 0.4, ease: E.in }, S(583.36));
      rise(words("sc121-tr")[0], T(580.90), { dur: 0.9, y: 12 });
      rise(words("sc121-act")[0], T(582.02), { dur: 0.7, y: 8 });
      [T(583.30), T(583.46)].forEach((c, i) => rise(words("sc121-tg")[i], c, { dur: 0.3, y: 6 }));
    })();

    /* =================== C5S122 · 583.76–588.72 · telling you hey US is not abandoning … Taiwan =================== */
    scene("sc122", 583.76, 588.98);
    (function () {
      tl.fromTo($("sc122-clip"), { x: 260, y: 20, rotation: 3 }, { x: 0, y: 0, rotation: -3, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(583.76));
      cam($("sc122-cam"), { scale: 1.0 }, { scale: 1.06 }, S(583.76), 5.2);
      show($("sc122-natb"), T(584.90));
      [T(584.90), T(585.06)].forEach((c, i) => rise(words("sc122-nat")[i], c, { dur: 0.6, y: 8 }));
      const svg = $("sc122-svg"), f = gated(585.9, 589.0, () => markDefs(svg, "c5s03-mk122", "0 0 1920 1080", 4));
      const q = [[-60, -80], [-52, -140], [12, -164], [72, -128], [68, -64], [12, -24], [4, 44]].map(([a, b]) => [1340 + a, 420 + b]);
      FX.markup.pen(tl, svg, S(586.00), { points: q, dur: 0.7, width: 12, color: RED, filter: f, seed: 1221 });
      FX.markup.pen(tl, svg, S(586.78), { points: [[1342, 512], [1346, 520]], dur: 0.08, width: 16, color: RED, filter: f, seed: 1222 });
      tl.fromTo($("sc122-twb"), { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.35, ease: C(E.out, 0.35), immediateRender: true }, T(587.86));
    })();
    paperSlide($("sc122-shot"), $("sc123-shot"), S(588.72));

    /* =================== C5S123 · 588.72–592.48 · That's all to say that US allies are already kinda unsure =================== */
    scene("sc123", 588.47, 592.64);
    (function () {
      const svg = $("sc123-svg"), dots = hemi(svg, 960, 920, "c5s03-d123-");
      cam($("sc123-cam"), { scale: 1.0 }, { scale: 1.22 }, S(588.47), 3.6, E.cam);
      const al = dots.filter((d) => d.a < 0.85);
      const f = gated(589.7, 592.7, () => markDefs(svg, "c5s03-mk123", "0 0 1920 1080", 4));
      FX.markup.circle(tl, svg, S(589.80), { cx: 1430, cy: 800, rx: 200, ry: 150, rot: -20, dur: 0.6, color: INK, width: 7, filter: f, seed: 1231 });
      gated(589.9, 592.7, () => FX.onFrame((t) => {
        const fr = Math.floor(t * 12);
        al.forEach((d, i) => d.el.setAttribute("fill", t < S(590.1) ? GREY : FX.noise2(i * 1.3, fr * 0.5, 1232) > 0.5 ? NAVY : GREY));
      }));
      show($("sc123-usb"), T(589.78));
      [T(589.78), T(590.10)].forEach((c, i) => rise(words("sc123-us")[i], c, { dur: 0.7, y: 8 }));
      rise(words("sc123-un")[0], T(591.54), { dur: 0.6, y: 10 });
    })();
    whip($("sc123-shot"), $("sc124-shot"), S(592.48), { dir: -1, flash: true });

    /* =================== C5S124 · 592.48–598.03 · we don't exactly know how this vote is gonna play out (→ c6, still moving) =================== */
    scene("sc124", 592.48, SEG_END);
    ground("night", S(592.48));
    (function () {
      const img = $("sc124-img"), s = { b: 14 }, fl = () => (img.style.filter = `saturate(0.7) brightness(0.8) blur(${s.b.toFixed(2)}px)`);
      fl();
      cam($("sc124-cam"), { scale: 1.0 }, { scale: 1.2 }, S(592.48), 5.55);
      [[593.2, 9, 0.7], [594.0, 13, 0.5], [594.9, 7, 0.8], [595.9, 11, 0.5], [596.7, 7.5, 0.7], [597.5, 10, 0.53]].forEach(([t, v, d]) =>
        tl.to(s, { b: v, duration: d, ease: "sine.inOut", onUpdate: fl }, S(t)));
      [T(596.58), T(596.82)].forEach((c, i) => rise(words("sc124-tv")[i], c, { dur: 0.6, y: 10 }));
    })();

    // scenes outside their window: display none (set last — every measuring call above needed layout)
    SCENES.forEach((el) => { if (!el._first) gsap.set(el, { autoAlpha: 0, display: "none" }); });
