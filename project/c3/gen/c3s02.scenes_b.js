    /* =================== C3S053 · 261.05–265.93 · It basically said that there's no such thing. China belongs to the CCP =================== */
    scene("sc053", 261.05, 265.93);
    (function () {
      tl.fromTo($("sc053-cam"), { scale: 1.0 }, { scale: 1.09, duration: 4.9, ease: "none", immediateRender: true }, S(261.05));
      gated(261.05, 265.95, () => FX.weave($("sc053-cam"), { amp: 0.7, flicker: 0.03, seed: 5301 }));
      [T(262.75), T(262.99), T(263.31)].forEach((c, i) => rise(words("sc053-nst")[i], c, { dur: 0.45, y: 10 }));
      hide($("sc053-nst"), S(263.70), 0.2);
      rise(words("sc053-ch")[0], T(263.87), { dur: 0.7, y: 14 });
      pop(words("sc053-ccp")[0], T(265.15), 0.25);
    })();
    whip($("sc053-shot"), $("sc054-shot"), S(265.87), { vertical: true, dir: -1 });

    /* =================== C3S054 · 265.93–272.73 · The CCP is the governing government of China … Taiwan is just nothing. Not a country =================== */
    scene("sc054", 265.87, 273.09);
    (function () {
      const J = M.ea, cam = $("sc054-cam"), svg = $("sc054-svg");
      svg.innerHTML = `<g id="c3s02-sc054-cn" opacity="0" filter="url(#c3s02-glow)"><path d="${J.china}" fill="url(#c3s02-ht-red)" fill-opacity="0.78" stroke="${RED}" stroke-width="7" stroke-linejoin="round"/></g>
        <path id="c3s02-sc054-two" d="${J.taiwan}" fill="none" stroke="${BONE}" stroke-width="4" stroke-dasharray="10 9" opacity="0"/>`;
      const tw = $("sc054-tw"); Object.assign(tw.style, { left: J.tw_box[0] + "px", top: J.tw_box[1] + "px", opacity: 0.88 });
      const a = camAt(0.62, 1900, 1750), b = camAt(1.15, 2150, 2620);
      tl.fromTo(cam, a, Object.assign({}, b, { duration: 6.4, ease: E.cam, immediateRender: true }), S(265.87));
      tl.fromTo($("sc054-cn"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(266.03));
      pop(words("sc054-ccp")[0], T(266.03), 0.5);
      rise(words("sc054-ch")[0], T(267.79), { dur: 0.9, y: 14 });
      hide([$("sc054-ccp"), $("sc054-ch")], S(270.30));
      // Taiwan's celadon drains away (motif: fill 0.88 → 0 at 12 fps), the dashed outline is all that's left
      tl.fromTo(tw, { opacity: 0.88 }, { opacity: 0, duration: 1.0, ease: C(E.inOut, 1.0), immediateRender: false }, S(270.59));
      tl.fromTo($("sc054-two"), { attr: { opacity: 0 } }, { attr: { opacity: 0.85 }, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(270.90));
      rise(words("sc054-no")[0], T(270.59), { dur: 0.8, y: 12 });
      rise(words("sc054-nac")[0], T(271.47), { dur: 0.3, y: 8 });
      show(words("sc054-nac")[1], T(271.79)); show(words("sc054-nac")[2], T(271.95));
    })();
    slideIn($("sc055-shot"), S(272.67));

    /* =================== C3S055 · 272.73–277.21 · from a Taiwanese point of view, this was something they did not expect =================== */
    scene("sc055", 272.67, 277.21);
    ground("paper", S(272.90));
    (function () {
      tl.fromTo($("sc055-col"), { y: 0 }, { y: -20, duration: 4.5, ease: "none", immediateRender: true }, S(272.67));
      FX.textCallout(tl, $("sc055-cam"), $("sc055-dim"), $("sc055-key"), S(274.00), { dim: 0.22, punch: 1.1, dur: 1.1, wipe: 0.8, delay: 0.35 });
      pop(words("sc055-tws")[0], T(273.23), 0.8);
      [T(276.19), T(276.43)].forEach((c, i) => rise(words("sc055-dne")[i], c, { dur: 0.25, y: 8 }));
      show(words("sc055-dne")[2], T(276.59));
    })();

    /* =================== C3S056 · 277.21–280.17 · they didn't know what was gonna happen next =================== */
    scene("sc056", 277.21, 280.53);
    ground("night", S(277.21));
    (function () {
      tl.fromTo($("sc056-cam"), { scale: 1.0 }, { scale: 1.08, duration: 3.3, ease: "none", immediateRender: true }, S(277.21));
      gated(277.21, 280.6, () => FX.weave($("sc056-wv"), { amp: 1.0, flicker: 0.04, seed: 5601 }));
      rise(words("sc056-nx")[0], T(279.55), { dur: 0.5, y: 12 });
    })();
    slideIn($("sc057-shot"), S(280.11), { from: "left" });

    /* =================== C3S057–058 · 280.17–291.29 · to truly understand … existential crisis … background about Taiwan and how the government there came to be =================== */
    scene("sc057", 280.11, 291.29);
    ground("paper", S(280.30));
    (function () {
      const svg = $("sc057-svg"), g = $("sc057-ticks"), Y = 620;
      let d = `M-600 ${Y} L1790 ${Y}`;
      for (let x = -560, k = 0; x <= 1780; x += 40, k++) { const h = k % 5 === 0 ? 30 : 12; d += ` M${x} ${Y - h} L${x} ${Y}`; }
      const axis = document.createElementNS(NS, "path"); axis.setAttribute("d", d); axis.setAttribute("stroke", INK); axis.setAttribute("stroke-width", "4"); axis.setAttribute("fill", "none"); g.appendChild(axis);
      const axb = FX.whipDefs(defs, "c3s02-ax057"); g.setAttribute("filter", "url(#c3s02-ax057)");
      const ab = { v: 0 };
      tl.fromTo(ab, { v: 0 }, { v: 22, duration: 0.5, ease: "power2.in", immediateRender: true, onUpdate: () => axb.setAttribute("stdDeviation", `${ab.v.toFixed(1)} 0`) }, S(286.43));
      tl.to(ab, { v: 0, duration: 0.7, ease: "power2.out", onUpdate: () => axb.setAttribute("stdDeviation", `${ab.v.toFixed(1)} 0`) }, S(286.93));
      // the 1971 page pins at the right end of the line
      const card = $("sc057-card");
      tl.fromTo(card, { opacity: 0, y: -260, rotation: 7 }, { opacity: 1, y: 0, rotation: 2, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(282.83));
      const pn = pin(svg, 1560, 312, RED, 13, "c3s02-sc057-pin");
      tl.fromTo(pn, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(283.55));
      ink(svg, `M1560 526 L1772 ${Y - 6}`, S(283.30), 0.5, { color: INK, width: 3 });
      svg.insertAdjacentHTML("beforeend", `<circle id="c3s02-sc057-dot" cx="1780" cy="${Y}" r="16" fill="${INK}" opacity="0"/><path id="c3s02-sc057-stop" d="M300 ${Y - 70} L300 ${Y + 30}" stroke="${INK}" stroke-width="7" opacity="0"/>`);
      [T(282.83), T(283.63)].forEach((c, i) => rise(words("sc057-ec")[i], c, { dur: 0.6, y: 12 }));
      hide($("sc057-ec"), S(284.70));
      // C3S058: the dot rewinds left fast, ticks blur, the camera tracks left; it stops at the government's origin
      show($("sc057-dot"), S(284.70));
      tl.fromTo($("sc057-dot"), { attr: { cx: 1780 } }, { attr: { cx: 300 }, duration: 1.3, ease: C(E.inOut, 1.3), immediateRender: false }, S(286.43));
      tl.fromTo($("sc057-cam"), { x: 0 }, { x: 260, duration: 1.6, ease: E.cam, immediateRender: true }, S(286.30));
      tl.fromTo($("sc057-stop"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(287.75));
      tl.fromTo($("sc058-pres"), { opacity: 0, scale: 0.85, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(289.07));
      $("sc058-pres").style.left = "40px"; $("sc058-pres").style.top = "40px";
      $("sc058-bk").style.left = "1000px"; $("sc058-tw").style.left = "1000px"; $("sc058-gov").style.left = "300px"; $("sc058-gov").style.top = "700px";
      rise(words("sc058-bk")[0], T(286.43), { dur: 0.7, y: 10 });
      rise(words("sc058-tw")[0], T(287.39), { dur: 0.8, y: 12 });
      pop(words("sc058-gov")[0], T(289.07), 0.7);
      tl.to($("sc057-cam"), { x: 280, scale: 1.03, duration: 3.4, ease: "none" }, S(287.90));
    })();
    whip($("sc057-shot"), $("sc059-shot"), S(291.23), { dir: 1, flash: true });

    /* =================== C3S059 · 291.29–294.01 · Our story starts in World War II =================== */
    scene("sc059", 291.23, 294.37);
    ground("night", S(291.25));
    (function () {
      gated(291.23, 294.4, () => FX.weave($("sc059-wv"), { amp: 1.4, flicker: 0.05, seed: 5901 }));
      tl.fromTo($("sc059-wv"), { scale: 1.0 }, { scale: 1.05, duration: 3.1, ease: "none", immediateRender: true }, S(291.23));
      [T(292.75), T(293.15)].forEach((c, i) => rise(words("sc059-ww")[i], c, { dur: 0.5, y: 14 }));
      show(words("sc059-ww")[2], T(293.47));
    })();
    slideIn($("sc060-shot"), S(293.95));

    /* =================== C3S060 · 294.01–298.97 · this is where current China, the CCP, has tried to change the story a bit =================== */
    scene("sc060", 293.95, 298.97);
    ground("paper", S(294.20));
    (function () {
      // book spread (typeset recreation: no title, no real book) — body text as rules
      const L = $("sc060-l"), R = $("sc060-r"), r = FX.rng(6000);
      const bars = (pg, y0, y1, x0, w0) => { let h = ""; for (let y = y0; y < y1; y += 26) h += `<div class="bl" style="top:${y}px;left:${x0}px;width:${(w0 - r() * (y % 130 === 0 ? 160 : 30)).toFixed(0)}px"></div>`; pg.insertAdjacentHTML("beforeend", h); };
      L.insertAdjacentHTML("beforeend", `<div class="bl" style="top:80px;left:60px;width:260px;height:16px;background:rgba(20,27,36,0.7)"></div>`);
      bars(L, 590, 940, 60, 420);
      R.insertAdjacentHTML("beforeend", `<div class="bl" style="top:74px;left:60px;width:380px;height:22px;background:rgba(20,27,36,0.75)"></div><div class="bl" style="top:112px;left:60px;width:300px;height:14px;background:rgba(20,27,36,0.6)"></div>`);
      bars(R, 170, 940, 60, 420);
      tl.fromTo($("sc060-cam"), { scale: 1.0 }, { scale: 1.08, duration: 5.0, ease: "none", immediateRender: true }, S(293.95));
      // the red pen (the CCP's side) strikes the heading and writes over it
      const mk = $("sc060-mk"), mf = gated(293.9, 299.1, () => FX.markupDefs(defs, "c3s02-mk060", { boil: 4 }));
      FX.markup.pen(tl, mk, S(297.31), { points: [[592, 92], [990, 84]], jitter: 4, seed: 6001, dur: 0.4, width: 7, color: RED, filter: mf });
      FX.markup.pen(tl, mk, S(297.40), { points: [[592, 124], [910, 118]], jitter: 4, seed: 6002, dur: 0.35, width: 7, color: RED, filter: mf });
      const hw = []; for (let i = 0; i <= 24; i++) { const x = 600 + i * 15; hw.push([x, 40 + Math.sin(i * 1.9) * 13 + (i % 3 === 0 ? -10 : 0)]); }
      FX.markup.pen(tl, mk, S(297.75), { points: hw, jitter: 3, seed: 6003, dur: 0.55, width: 5, color: RED, filter: mf, ease: "none" });
      pop(words("sc060-ccp")[0], T(295.87), 0.6);
      [T(297.31), T(297.63), T(297.79)].forEach((c, i) => rise(words("sc060-cs")[i], c, { dur: 0.5, y: 10 }));
    })();
    whip($("sc060-shot"), $("sc061-shot"), S(298.91), { dir: 1 });

    /* =================== C3S061 · 298.97–303.53 · where they claim that China fought with the United States. Which is true, by the way =================== */
    scene("sc061", 298.91, 303.53);
    ground("night", S(298.93));
    (function () {
      tl.fromTo($("sc061-cam"), { scale: 1.0 }, { scale: 1.06, duration: 4.6, ease: "none", immediateRender: true }, S(298.91));
      const w = words("sc061-txt");
      [T(300.11), T(300.51), T(300.99), T(301.15), T(301.63)].forEach((c, i) => rise(w[i], c, { dur: 0.6, y: 10 }));
      rise(w[5], T(302.51), { dur: 0.4, y: 10 });
      const mf = gated(298.9, 303.6, () => FX.markupDefs(defs, "c3s02-mk061", { boil: 4 }));
      FX.markup.pen(tl, $("sc061-mk"), S(302.57), { points: [[350, 600], [380, 640], [460, 548]], jitter: 2, seed: 6101, dur: 0.3, width: 9, color: BONE, filter: mf, blend: "normal" });
    })();

    /* =================== C3S062 · 303.53–310.65 · a lot of Chinese people … fought with the United States in World War II against Japan =================== */
    scene("sc062", 303.53, 311.01);
    (function () {
      tl.fromTo($("sc062-cam"), { x: 0 }, { x: -40, duration: 7.5, ease: "none", immediateRender: true }, S(303.53));
      tl.fromTo($("sc062-a"), { y: 30 }, { y: -20, duration: 7.5, ease: "none", immediateRender: true }, S(303.53));
      tl.fromTo($("sc062-b"), { y: -20 }, { y: 24, duration: 7.5, ease: "none", immediateRender: true }, S(303.53));
      tl.fromTo($("sc062-h"), { scale: 1.0 }, { scale: 1.05, duration: 7.5, ease: "none", immediateRender: true }, S(303.53));
      [T(304.27), T(304.67)].forEach((c, i) => rise(words("sc062-cp")[i], c, { dur: 0.8, y: 12 }));
      hide($("sc062-cp"), S(306.8));
      rise(words("sc062-aj")[0], T(309.39), { dur: 0.3, y: 8 });
      show(words("sc062-aj")[1], T(309.71));
    })();
    slideIn($("sc063-shot"), S(310.59));

    /* =================== C3S063 · 310.65–317.45 · But it wasn't the CCP that was fighting with the United States. In fact, CCP stay out of World War II =================== */
    scene("sc063", 310.59, 317.45);
    ground("paper", S(310.80));
    (function () {
      const svg = $("sc063-svg");
      pop($("sc063-us"), S(310.80), 0.8); pop($("sc063-cn"), S(310.88), 0.8);
      pop(words("sc063-ccp")[0], T(311.87), 0.4);
      // the link US ↔ CCP draws … and gets crossed out
      ink(svg, "M770 470 L1150 470", S(311.93), 0.6, { color: INK, width: 8 });
      ink(svg, "M800 446 L768 470 L800 494", S(312.40), 0.15, { color: INK, width: 8 });
      ink(svg, "M1120 446 L1152 470 L1120 494", S(312.40), 0.15, { color: INK, width: 8 });
      const mf = gated(310.5, 317.5, () => FX.markupDefs(defs, "c3s02-mk063", { boil: 4 }));
      FX.markup.cross(tl, svg, S(312.89), { x: 960, y: 470, s: 64, dur: 0.14, color: RED, width: 14, filter: mf });
      [T(313.95), T(314.27)].forEach((c, i) => rise(words("sc063-usl")[i], c, { dur: 0.7, y: 10 }));
      tl.fromTo($("sc063-cam"), { scale: 1.0 }, { scale: 1.05, duration: 6.5, ease: "none", immediateRender: true }, S(310.80));
      tl.to([$("sc063-cn"), $("sc063-ccp")], { x: 1000, duration: 0.42, ease: E.in }, S(317.05));   // CCP slides off (cut on action)
    })();

    /* =================== C3S064 · 317.45–324.28 · It was the ROC, the nationalists who were ruling China at the time … =================== */
    scene("sc064", 317.45, 324.32);
    ground("night", S(317.45));
    (function () {
      tl.fromTo($("sc064-cam"), { scale: 1.0, x: 30 }, { scale: 1.12, x: -40, duration: 6.9, ease: E.cam, immediateRender: true }, S(317.45));
      tl.fromTo($("sc064-far"), { x: -20, scale: 1.0 }, { x: 30, scale: 1.04, duration: 6.9, ease: "none", immediateRender: true }, S(317.45));
      const mf = gated(317.4, 324.4, () => FX.markupDefs(defs, "c3s02-mk064", { boil: 4 }));
      FX.markup.circle(tl, $("sc064-mk"), S(318.00), { cx: 330, cy: 560, rx: 250, ry: 470, rot: 2, dur: 0.9, color: CEL, width: 10, filter: mf, seed: 6401 });
      show($("sc064-box"), T(317.71));
      rise(words("sc064-roc")[0], T(317.71), { dur: 0.6, y: 10 });
      rise(words("sc064-roc")[1], T(317.95), { dur: 0.6, y: 10 });
      rise(words("sc064-nat")[0], T(318.91), { dur: 0.9, y: 12 });
    })();
    whip($("sc064-shot"), $("sc065-shot"), S(324.22), { vertical: true, dir: 1 });
