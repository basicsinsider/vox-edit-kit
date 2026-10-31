
    /* =================== C5S096 · 454.22–458.70 · very quickly they realize that their worst dreams are coming true =================== */
    scene("sc096", 454.22, 458.96);
    (function () {
      cam($("sc096-cam"), { scale: 1.0 }, { scale: 1.08 }, S(454.22), 4.74);
      [T(456.80), T(457.20)].forEach((c, i) => rise(words("sc096-wd")[i], c, { dur: 0.9, y: 12 }));
      [T(457.76), T(458.08)].forEach((c, i) => rise(words("sc096-ct")[i], c, { dur: 0.35, y: 8 }));
    })();
    paperSlide($("sc096-shot"), $("sc097-shot"), S(458.70));

    /* =================== C5S097 · 458.70–462.62 · do you remember that vote we talked about where every single year =================== */
    scene("sc097", 458.45, 462.62);
    ground("paper", S(458.70));
    (function () {
      const svg = $("sc097-svg"), dots = hemi(svg, 960, 900, "c5s03-d97-");
      chair(svg, 877, 690, 0.75, "c5s03-ch97", { plate: true });
      cam($("sc097-cam"), { scale: 1.0 }, { scale: 1.04 }, S(458.45), 3.7);
      tl.to($("sc097-cam"), { scale: 1.1, y: -20, duration: 0.45, ease: E.in }, S(462.17));
      rise(words("sc097-vote")[0], T(460.48), { dur: 1.0, y: 14 });
      // the vote, year after year: the semicircle fills clockwise three times (12 fps waves)
      [460.50, 461.05, 461.60].forEach((t0, k) => {
        dots.forEach((d, i) => tl.to(d.el, { attr: { fill: INK }, duration: 0.001 }, S(t0) + Math.floor(i / 10) / 24));
        if (k < 2) dots.forEach((d) => tl.to(d.el, { attr: { fill: GREY }, duration: 0.001 }, S(t0) + 0.5));
      });
    })();

    /* =================== C5S098 · 462.62–467.02 · the CCP or one of CCP's allies brings up this vote in the UN =================== */
    scene("sc098", 462.62, 467.02);
    ground("night", S(462.62));
    (function () {
      cam($("sc098-cam"), { scale: 1.02 }, { scale: 1.08 }, S(462.62), 4.4);
      pop($("sc098-ccpb"), T(462.72), 0.9);
      rise(words("sc098-al")[0], T(464.80), { dur: 0.9, y: 10 });
      [T(466.40), T(466.48)].forEach((c, i) => rise(words("sc098-un")[i], c, { dur: 0.4, y: 10 }));
    })();
    pushThrough($("sc098-shot"), $("sc099-shot"), S(467.02));

    /* =================== C5S099 · 467.02–473.18 · let's kick out Taiwan, let's give that Chinese seat to the CCP. That vote is coming up =================== */
    scene("sc099", 467.02, 473.44);
    ground("paper", S(467.02));
    (function () {
      const svg = $("sc099-svg");
      chair(svg, 762, 300, 1.8, "c5s03-ch99", { plate: true });
      svg.insertAdjacentHTML("beforeend", `<g id="c5s03-c99tw"><circle cx="960" cy="470" r="74" fill="url(#c5s03-ht-cel)" stroke="${INK}" stroke-width="6"/></g>
        <g id="c5s03-c99cn"><circle cx="960" cy="470" r="74" fill="url(#c5s03-ht-red)" stroke="${INK}" stroke-width="6"/></g>`);
      $("sc099-cam").insertAdjacentHTML("beforeend", `<div id="c5s03-sc099-ccp" class="k-abs t-label" style="left:1100px;top:330px;font-size:52px"><span class="k-redbox" id="c5s03-sc099-ccpb" style="opacity:0">CCP</span></div>`);
      cam($("sc099-cam"), { scale: 1.0 }, { scale: 1.05 }, S(467.02), 6.4);
      const tw = $("c99tw"), cn = $("c99cn");
      tl.fromTo(tw, { attr: { transform: "translate(0 0) rotate(0 960 470)" } }, { attr: { transform: "translate(-1300 40) rotate(-80 960 470)" }, duration: 1.0, ease: C(E.in, 1.0), immediateRender: true }, S(468.40));
      tl.fromTo(cn, { attr: { transform: "translate(1150 0) rotate(60 960 470)" } }, { attr: { transform: "translate(0 0) rotate(0 960 470)" }, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(470.80));
      [T(468.32), T(468.56), T(468.72)].forEach((c, i) => rise(words("sc099-kot")[i], c, { dur: 0.8, y: 10 }));
      [T(469.76), T(470.16)].forEach((c, i) => rise(words("sc099-cs")[i], c, { dur: 0.8, y: 10 }));
      pop($("sc099-ccpb"), T(470.80), 0.8);
      show($("sc099-cub"), T(472.32));
      [T(472.32), T(472.64)].forEach((c, i) => rise(words("sc099-cu")[i], c, { dur: 0.35, y: 8 }));
    })();
    paperSlide($("sc099-shot"), $("sc100-shot"), S(473.18));

    /* =================== C5S100–C5S101 · 473.18–484.78 · we are not against China coming into the UN … against kicking out Taiwan … none of the sides =================== */
    scene("sc100", 472.93, 484.94);
    (function () {
      const svg = $("sc100-svg"), camEl = $("sc100-cam");
      const tw = chair(svg, 440, 330, 1.7, "c5s03-ch100a", { fill: CEL });
      const cn = chair(svg, 1100, 330, 1.7, "c5s03-ch100b", { dash: true, fill: "rgba(0,0,0,0)" });
      cam(camEl, { scale: 1.0 }, { scale: 1.03 }, S(472.93), 5.45);
      [T(475.68), T(475.92)].forEach((c, i) => rise(words("sc100-na")[i], c, { dur: 0.8, y: 10 }));
      show($("sc100-nab"), T(475.68));
      tl.to(cn.cush, { attr: { fill: RED, "stroke-dasharray": "none" }, duration: 0.001 }, S(476.56));
      tl.to(cn.inner.querySelector("g"), { attr: { "stroke-dasharray": "none" }, duration: 0.001 }, S(476.56));
      tl.fromTo(cn.inner, { scale: 1.08 }, { scale: 1, svgOrigin: "110 130", duration: 0.6, ease: C(E.out, 0.6), immediateRender: false }, S(476.56));
      pop($("sc100-chb"), T(476.56), 0.7);
      [T(477.44), T(477.68), T(477.76)].forEach((c, i) => rise(words("sc100-iu")[i], c, { dur: 0.4, y: 8 }));
      // C5S101 — CA: punch in on Taiwan's seat mid-move
      tl.set([$("sc100-na"), $("sc100-iu")], { opacity: 0 }, S(478.38));
      tl.set(camEl, { scale: 1.16, x: 210, y: 30 }, S(478.38));
      tl.to(camEl, { scale: 1.2, x: 230, y: 34, duration: 2.6, ease: "none" }, S(478.38));
      tl.to(camEl, { scale: 0.96, x: 0, y: 0, duration: 2.4, ease: E.cam }, S(481.0));
      rise(words("sc101-ag")[0], T(478.88), { dur: 0.7, y: 10 });
      [T(479.52), T(480.00), T(480.24)].forEach((c, i) => rise(words("sc101-ag")[i + 1], c, { dur: 0.7, y: 10 }));
      show($("sc100-tw"), T(480.24));
      hide($("sc101-ag"), S(481.6), 0.4);
      const mk = $("sc100-svg"), f = gated(479.3, 484.9, () => markDefs(mk, "c5s03-mk100", "0 0 1920 1080", 4));
      const x1 = FX.markup.pen(tl, mk, S(479.56), { points: [[860, 250], [760, 380], [690, 470]], dur: 0.4, width: 9, color: RED, filter: f, seed: 1001, jitter: 6 });
      ink(mk, "M780 280 C 792 380, 786 480, 796 600", S(479.86), 0.3, { color: INK, width: 16, filter: f });
      FX.markup.out(tl, x1, S(480.05), 0.35);
      tl.to(tw.inner, { x: -8, duration: 0.08, yoyo: true, repeat: 3, ease: "none" }, S(479.95));
      [T(482.32), T(482.56), T(482.72), T(482.80)].forEach((c, i) => rise(words("sc101-nos")[i], c, { dur: 0.8, y: 12 }));
      // none of the sides asks for it: both seats turn away from each other (12 fps)
      tl.to(tw.inner, { x: -70, rotation: -9, svgOrigin: "110 232", duration: 0.9, ease: C(E.inOut, 0.9) }, S(483.0));
      tl.to(cn.inner, { x: 70, rotation: 9, svgOrigin: "110 232", duration: 0.9, ease: C(E.inOut, 0.9) }, S(483.0));
    })();
    whip($("sc100-shot"), $("sc102-shot"), S(484.72), { dir: 1 });

    /* =================== C5S102–C5S103 · 484.78–493.45 · Taiwan says keep CCP out. CCP says, give me the seat … No one is saying let's compromise =================== */
    scene("sc102", 484.72, 493.71);
    ground("night", S(484.72));
    (function () {
      const L = $("sc102-L"), R = $("sc102-R");
      cam(L, { x: -30 }, { x: -110 }, S(484.72), 5.5);
      cam(R, { x: 30 }, { x: 110 }, S(484.72), 5.5);
      cam($("sc102-Limg"), { scale: 1.0 }, { scale: 1.05 }, S(484.72), 8.7);
      cam($("sc102-Rimg"), { scale: 1.0 }, { scale: 1.05 }, S(484.72), 8.7);
      [T(484.72), T(485.28)].forEach((c, i) => rise(words("sc102-ts")[i], c, { dur: 0.8, y: 10 }));
      [T(485.68), T(486.00), T(486.64)].forEach((c, i) => rise(words("sc102-kc")[i], c, { dur: 0.8, y: 12 }));
      [T(487.23), T(487.87)].forEach((c, i) => rise(words("sc102-cs")[i], c, { dur: 0.8, y: 10 }));
      [T(488.19), T(488.43), T(488.59), T(488.67)].forEach((c, i) => rise(words("sc102-gm")[i], c, { dur: 0.7, y: 12 }));
      [T(489.15), T(489.47), T(489.87)].forEach((c, i) => rise(words("sc102-kt")[i], c, { dur: 0.7, y: 12 }));
      // C5S103 — the halves slide toward each other and stop short
      hide([$("sc102-ts"), $("sc102-kc"), $("sc102-cs"), $("sc102-gm"), $("sc102-kt")], S(490.22), 0.35);
      tl.to(L, { x: -55, duration: 1.1, ease: C(E.inOut, 1.1) }, S(490.30));
      tl.to(R, { x: 55, duration: 1.1, ease: C(E.inOut, 1.1) }, S(490.30));
      tl.to([L, R], { x: (i) => (i ? 52 : -52), duration: 0.12, ease: "none", yoyo: true, repeat: 1 }, S(491.40));
      pop($("sc103-cmpb"), T(491.55), 0.6);
      const mk = $("sc103-mk"), f = gated(491.5, 493.8, () => markDefs(mk, "c5s03-mk103", "0 0 1920 1080", 12));
      FX.markup.cross(tl, mk, S(491.90), { x: 960, y: 505, s: 70, dur: 0.16, color: BONE, width: 12, filter: f });
      [T(492.19), T(492.43), T(492.51)].forEach((c, i) => rise(words("sc103-bou")[i], c, { dur: 0.6, y: 10 }));
    })();
    paperSlide($("sc102-shot"), $("sc104-shot"), S(493.45));

    /* =================== C5S104 · 493.45–498.17 · both of them … say they are real China, the other party is the fake China =================== */
    scene("sc104", 493.20, 498.33);
    ground("paper", S(493.45));
    (function () {
      const camEl = $("sc104-cam");
      cam(camEl, { scale: 1.0 }, { scale: 1.02 }, S(493.2), 2.7);
      tl.to(camEl, { scale: 1.05, duration: 0.3, ease: C(E.out, 0.3) }, S(495.95));
      tl.to(camEl, { scale: 1.08, duration: 0.3, ease: C(E.out, 0.3) }, S(497.47));
      cam($("sc104-roc"), { y: 0 }, { y: -10 }, S(493.2), 5);
      const ch = gated(495.8, 498.2, () => FX.roughDefs(defs, "c5s03-ch104", { freq: 0.045, scale: 7, choke: 0 }));
      const stamp = (el, t) => {
        el.style.filter = "url(#c5s03-ch104)";
        tl.fromTo(el, { opacity: 0, scale: 1.35 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power2.in", immediateRender: true }, t);
        FX.chokeSettle(tl, ch, el, t, 8, 0.45, "none");
      };
      stamp($("sc104-r1"), T(495.95)); stamp($("sc104-r2"), T(495.95));
      ["sc104-r1", "sc104-r2"].forEach((id) => { show(words(id)[0], T(495.95)); show(words(id)[1], T(496.19)); });
      stamp($("sc104-f1"), T(497.47)); stamp($("sc104-f2"), T(497.47));
    })();
    whip($("sc104-shot"), $("sc105-shot"), S(498.17), { dir: 1, vertical: true });

    /* =================== C5S105 · 498.17–503.53 · Why would they get a UN seat? US is trying to walk between the two demands, making a compromise =================== */
    scene("sc105", 498.17, 503.53);
    ground("night", S(498.17));
    (function () {
      cam($("sc105-cam"), { scale: 1.0 }, { scale: 1.08 }, S(498.17), 4.9);
      tl.to($("sc105-cam"), { scale: 1.13, duration: 0.46, ease: E.in }, S(503.07));
      tl.fromTo($("sc105-lamp"), { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "steps(2)", immediateRender: true }, S(498.22));
      [T(498.83), T(499.15)].forEach((c, i) => rise(words("sc105-us")[i], c, { dur: 0.8, y: 10 }));
      hide($("sc105-us"), S(500.9), 0.4);
      [T(501.15), T(501.55)].forEach((c, i) => rise(words("sc105-wb")[i], c, { dur: 0.9, y: 12 }));
      [T(501.95), T(502.11)].forEach((c, i) => rise(words("sc105-td")[i], c, { dur: 0.6, y: 10 }));
      tl.fromTo([$("sc105-tl"), $("sc105-tr")], { opacity: 0, scaleX: 0 }, { opacity: 1, scaleX: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(502.0));
      rise(words("sc105-cmp")[0], T(502.99), { dur: 0.35, y: 8 });
    })();

    /* =================== C5S106 · 503.53–507.69 · And what is this Jeff Bezos quote? Where compromise is never a good solution =================== */
    scene("sc106", 503.53, 507.85);
    ground("paper", S(503.53));
    (function () {
      const page = $("sc106-page"), r = FX.rng(10601);
      ["sc106-n1", "sc106-n2"].forEach((id) => { let h = ""; for (let i = 0; i < 60; i++) h += `<div class="k-filler" style="width:${i % 9 === 8 ? 140 + r() * 80 : 330 + r() * 50}px"></div>`; $(id).innerHTML = h; });
      const s0 = 1.85;
      gsap.set(page, { x: 960 - 960 * s0, y: 540 - 340 * s0, scale: s0 });
      tl.fromTo(page, { x: 960 - 960 * s0, y: 540 - 340 * s0, scale: s0 }, { x: 960 - 960 * 1.9, y: 540 - 340 * 1.9, scale: 1.9, duration: 1.07, ease: "none", immediateRender: false }, S(503.53));
      tl.to(page, { x: 0, y: -30, scale: 1.0, duration: 1.2, ease: C(E.inOut, 1.2) }, S(504.60));
      tl.to(page, { x: -30, y: -60, scale: 1.03, duration: 1.9, ease: "none" }, S(505.80));
      [T(504.27), T(504.51)].forEach((c, i) => rise(words("sc106-col")[i], c, { dur: 0.5, y: 6 }));
      // pull-quote + pen underline per word, in sync with the spoken quote
      const pq = $("sc106-pq"), ws = pq.querySelectorAll(".k-w"), mk = $("sc106-mk");
      const f = gated(505.8, 507.9, () => markDefs(mk, "c5s03-mk106", "0 0 820 900", 4));
      const cues = [T(505.95), T(506.51), T(506.67), T(506.91), T(506.99), T(507.15)];
      ws.forEach((w, i) => {
        show(w, cues[i]);
        const x = w.offsetLeft, y = pq.offsetTop + w.offsetTop + w.offsetHeight - 4, wd = w.offsetWidth - 14;
        FX.markup.pen(tl, mk, cues[i] + 0.04, { points: [[x + 4, y + 2], [x + wd, y - 1]], dur: 0.22, width: 5, color: RED, filter: f, seed: 1060 + i, jitter: 3 });
      });
      ws.forEach((w) => (w.style.position = "relative"));
    })();
    whip($("sc106-shot"), $("sc107-shot"), S(507.69), { dir: -1 });

    /* =================== C5S107 · 507.69–513.77 · make both sides happy, when in reality both sides are just getting more pissed off =================== */
    scene("sc107", 507.69, 514.03);
    (function () {
      const svg = $("sc107-svg"), mk = $("sc107-mk");
      cam($("sc107-cam"), { scale: 1.0 }, { scale: 1.06 }, S(507.69), 6.3);
      const ring = (cx, col, id) => svg.insertAdjacentHTML("beforeend", `<circle id="${id}" cx="${cx}" cy="560" r="136" fill="none" stroke="${col}" stroke-width="8" opacity="0"/>`);
      ring(380, CEL, "c5s03-r107a"); ring(960, INK, "c5s03-r107b"); ring(1540, RED, "c5s03-r107c");
      const node = (id, rid, t) => { pop($(id), t, 0.8); tl.fromTo($(rid), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, t); };
      node("sc107-us", "r107b", S(507.75)); node("sc107-tw", "r107a", S(508.15)); node("sc107-cn", "r107c", S(508.30));
      show($("sc107-usl"), T(507.63)); show($("sc107-twl"), S(508.2)); show($("sc107-cnl"), S(508.35));
      const f = gated(508.4, 514.1, () => markDefs(mk, "c5s03-mk107", "0 0 1920 1080", 4));
      FX.markup.pen(tl, mk, S(508.57), { points: [[822, 548], [700, 530], [520, 552]], dur: 0.55, width: 6, color: INK, filter: f, seed: 1071 });
      FX.markup.pen(tl, mk, S(508.70), { points: [[1098, 552], [1240, 534], [1402, 556]], dur: 0.55, width: 6, color: INK, filter: f, seed: 1072 });
      [T(510.51), T(510.75)].forEach((c, i) => rise(words("sc107-bs")[i], c, { dur: 0.8, y: 10 }));
      pop($("sc107-h1"), T(510.99), 0.6); pop($("sc107-h2"), T(510.99), 0.6);
      FX.markup.pen(tl, mk, S(512.55), { points: [[290, 366], [460, 352]], dur: 0.2, width: 7, color: RED, filter: f, seed: 1073 });
      FX.markup.pen(tl, mk, S(512.62), { points: [[1450, 366], [1620, 350]], dur: 0.2, width: 7, color: RED, filter: f, seed: 1074 });
      // angry scribbles over both sides (permanent pen boil)
      const zig = (cx, cy, seed) => { const r = FX.rng(seed), p = []; for (let i = 0; i < 9; i++) p.push([cx - 120 + i * 30 + (r() - 0.5) * 16, cy + (i % 2 ? -46 : 46) + (r() - 0.5) * 20]); return p; };
      FX.markup.pen(tl, mk, S(512.85), { points: zig(380, 360, 1075).map(([x, y]) => [x, y - 110]), dur: 0.35, width: 6, color: INK, filter: f, seed: 1075, jitter: 6 });
      FX.markup.pen(tl, mk, S(512.90), { points: zig(1540, 360, 1076).map(([x, y]) => [x, y - 110]), dur: 0.35, width: 6, color: INK, filter: f, seed: 1076, jitter: 6 });
    })();
    paperSlide($("sc107-shot"), $("sc108-shot"), S(513.77));

    /* =================== C5S108 · 513.77–520.89 · US does kind of pick which side it favors more, and that side is the CCP =================== */
    scene("sc108", 513.52, 521.05);
    (function () {
      const svg = $("sc108-svg"), card = $("sc108-card");
      cam($("sc108-cam"), { scale: 1.0 }, { scale: 1.07 }, S(513.52), 7.4);
      svg.insertAdjacentHTML("beforeend", `<g id="c5s03-c108tw" opacity="0"><circle cx="445" cy="735" r="44" fill="url(#c5s03-ht-cel)" stroke="${INK}" stroke-width="5"/></g>
        <g id="c5s03-c108cn" opacity="0"><circle cx="960" cy="860" r="44" fill="url(#c5s03-ht-red)" stroke="${INK}" stroke-width="5"/></g>
        <g id="c5s03-c108us" opacity="0"><path d="M900 560 L1020 560 L1040 650 L880 650 Z" fill="${INK}"/><path d="M935 560 Q960 520 985 560" fill="none" stroke="${INK}" stroke-width="10"/>
          <text x="960" y="626" text-anchor="middle" class="t-label" font-size="40" fill="${PAPER}" style="letter-spacing:0.14em">US</text></g>`);
      tl.fromTo($("c108tw"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(514.30));
      tl.fromTo($("c108cn"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(514.42));
      tl.fromTo($("c108us"), { attr: { opacity: 0 }, y: -40 }, { attr: { opacity: 1 }, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, T(514.67));
      show($("sc108-pwbg"), T(515.95));
      [T(515.95), T(516.59), T(516.91)].forEach((c, i) => rise(words("sc108-pw")[i], c, { dur: 0.8, y: 10 }));
      // the US weight drops on the CCP pan; the scale tips (12 fps)
      tl.to($("c108us"), { y: 165, duration: 0.35, ease: C(E.in, 0.35) }, S(519.27));
      tl.to($("c108cn"), { y: 36, duration: 0.5, ease: C(E.out, 0.5) }, S(519.60));
      tl.to($("c108us"), { y: 201, duration: 0.5, ease: C(E.out, 0.5) }, S(519.60));
      tl.to($("c108tw"), { y: -40, duration: 0.5, ease: C(E.out, 0.5) }, S(519.60));
      tl.to(card, { rotation: 2.2, duration: 0.6, ease: C(E.out, 0.6) }, S(519.60));
      tl.fromTo($("sc108-ccp"), { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(519.79));
      [T(519.79), T(520.03)].forEach((c, i) => rise(words("sc108-ccp")[i], c, { dur: 0.5, y: 8 }));
    })();
    whip($("sc108-shot"), $("sc109-shot"), S(520.89), { dir: 1, flash: true });
