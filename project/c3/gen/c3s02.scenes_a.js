    /* =================== C3S043 · 200.34–205.94 · And a little bit later … I mean a few decades later, after Silicon Valley =================== */
    scene("sc043", 200.34, 205.94);
    ground("night", 0);
    (function () {
      // hand-off: c3s01's light-flash whip lands here — frame 0 = bone flash, smear decays over 0.2 s
      gsap.set($("flash"), { opacity: 1 });
      tl.fromTo($("flash"), { opacity: 1 }, { opacity: 0, duration: 0.22, ease: "power2.out", immediateRender: true }, 0);
      const shot = $("sc043-shot"), wb = FX.whipDefs(defs, "c3s02-w043"), sb = { v: 90 };
      tl.set(shot, { filter: "url(#c3s02-w043)" }, 0); tl.set(shot, { filter: "none" }, 0.24);
      tl.fromTo(sb, { v: 90 }, { v: 0, duration: 0.22, ease: "power2.out", immediateRender: true, onUpdate: () => wb.setAttribute("stdDeviation", `${sb.v.toFixed(1)} 0`) }, 0);
      tl.fromTo(shot, { x: 380, scale: 1.18 }, { x: 0, scale: 1, duration: 0.22, ease: "power3.out", immediateRender: true }, 0);
      // the decade axis: minor tick = a year, tall tick = a decade (no year labels — he says none)
      const ax = $("sc043-axis"), Y = 640;
      let d = `M-200 ${Y} L12000 ${Y}`;
      for (let x = 0, k = 0; x <= 11600; x += 48, k++) { const h = k % 10 === 0 ? 46 : 14; d += ` M${x} ${Y - h} L${x} ${Y + (k % 10 === 0 ? 20 : 0)}`; }
      ax.innerHTML = `<path d="${d}" stroke="${BONE}" stroke-width="3" fill="none" opacity="0.85"/>`;
      for (let x = 0; x <= 11600; x += 480) ax.insertAdjacentHTML("beforeend", `<circle cx="${x}" cy="${Y - 70}" r="4" fill="${BONE}" opacity="0.5"/>`);
      const axb = FX.whipDefs(defs, "c3s02-ax043"); ax.setAttribute("filter", "url(#c3s02-ax043)");
      const ab = { v: 40 };
      tl.fromTo(ab, { v: 40 }, { v: 0, duration: 3.2, ease: E.out, immediateRender: true, onUpdate: () => axb.setAttribute("stdDeviation", `${ab.v.toFixed(1)} 0`) }, S(200.40));
      tl.fromTo(ax, { x: 0 }, { x: -9600, duration: 3.76, ease: E.out, immediateRender: true }, S(200.34));   // races, stops @204.10
      tl.to(ax, { x: -9660, duration: 1.84, ease: "none" }, S(204.10));                                   // still drifting at the cut (CA)
      $("sc043-dot").innerHTML = `<circle cx="960" cy="${Y}" r="44" fill="none" stroke="${CEL}" stroke-width="3" opacity="0.45"/><circle cx="960" cy="${Y}" r="17" fill="${CEL}" stroke="${INK}" stroke-width="3"/>`;
      gated(200.34, 205.94, () => FX.streaks($("sc043-str"), { seed: 4300, speed: 0.9, tint: [190, 220, 205], gain: 1.1 }));
      tl.fromTo($("sc043-str"), { opacity: 0.6 }, { opacity: 0.18, duration: 3.6, ease: E.out, immediateRender: true }, S(200.6));
      [T(203.32), T(203.40), T(203.64), T(204.04)].forEach((c, i) => rise(words("sc043-txt")[i], c, { dur: 0.7, y: 14 }));
    })();

    /* =================== C3S044 · 205.94–213.14 · after graduating … one of the most important people in Taiwan =================== */
    scene("sc044", 205.94, 213.50);
    (function () {
      const J = M.tw_night, cam = $("sc044-cam");
      $("sc044-sea").style.background = `rgb(${J.corner.join(",")})`;
      tl.fromTo(cam, camAt(0.5, 811, 1100), Object.assign(camAt(0.6, 830, 830), { duration: 4.9, ease: E.cam, immediateRender: true }), S(208.0));
      FX.focusHunt(tl, $("sc044-cam"), S(212.95 - 0.95), { dur: 0.8 });
      // dissertation title page (typeset recreation, no seal) slides onto the desk, then away
      const th = $("sc044-thesis");
      tl.fromTo(th, { y: 760, rotation: 6 }, { y: 0, rotation: -2.5, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(205.94));
      rise(words("sc044-grad")[0], T(206.20), { dur: 0.8, y: 12 });
      hide($("sc044-grad"), S(207.9));
      tl.to(th, { x: -1500, y: -120, rotation: -14, duration: 0.6, ease: C(E.in, 0.6) }, S(207.95));
      tl.to($("sc044-desk"), { opacity: 0, duration: 0.6, ease: "power1.inOut" }, S(208.0));
      // Pan Wen-Yuan: circle pinned off the Hsinchu coast, leader to the city
      const svg = $("sc044-svg"), hs = J.hsinchu, px = hs[0] - 330, py = hs[1] - 40;
      const pc = document.createElement("div"); pc.className = "k-abs"; pc.style.cssText = `left:${px - 140}px;top:${py - 140}px;width:280px;height:280px;opacity:0`;
      pc.innerHTML = PANSIL(280); cam.appendChild(pc);
      svg.insertAdjacentHTML("beforeend", `<circle id="c3s02-sc044-hd" cx="${hs[0]}" cy="${hs[1]}" r="9" fill="${BONE}" stroke="${INK}" stroke-width="3" opacity="0"/>`);
      pop(pc, S(210.44), 0.8);
      show($("sc044-hd"), S(210.44));
      ink(svg, `M${px + 140} ${py + 10} L${hs[0] - 10} ${hs[1]}`, S(210.70), 0.5, { color: BONE, width: 4 });
      [T(210.44), T(210.76), T(211.40)].forEach((c, i) => rise(words("sc044-mip")[i], c, { dur: 0.8, y: 14 }));
      // celadon fill (motif: watercolour edge + halftone + 6 px glow)
      tl.fromTo($("sc044-fill"), { opacity: 0 }, { opacity: 0.9, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(212.28));
      tl.fromTo($("sc044-ht"), { opacity: 0 }, { opacity: 0.5, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(212.28));
      rise(words("sc044-tw")[0], T(212.28), { dur: 0.3, y: 8 });
      gsap.set($("sc044-cr"), { opacity: 0 }); show($("sc044-cr"), S(208.3));
    })();
    slideIn($("sc045-shot"), S(213.08));

    /* =================== C3S045 · 213.14–216.90 · Which is not a country at this point … but it will become a country =================== */
    scene("sc045", 213.08, 216.92);
    ground("paper", S(213.30));
    (function () {
      tl.fromTo($("sc045-cam"), { scale: 1.0, x: 0 }, { scale: 1.05, x: -20, duration: 3.8, ease: "none", immediateRender: true }, S(213.08));
      const mf = gated(213.0, 217.0, () => FX.markupDefs(defs, "c3s02-mk045", { boil: 4 }));
      FX.markup.circle(tl, $("sc045-mk"), S(213.80), { cx: 482, cy: 470, rx: 225, ry: 370, rot: 8, dur: 0.8, color: INK, width: 8, filter: mf, seed: 4501 });
      [T(213.48), T(213.64), T(213.80)].forEach((c, i) => rise(words("sc045-nac")[i], c, { dur: 0.6, y: 12 }));
      FX.markup.arrow(tl, $("sc045-amk"), S(215.80), { x1: 1080, y1: 700, x2: 1280, y2: 880, bend: -60, head: 30, dur: 0.35, color: INK, width: 7, filter: mf });
      rise(words("sc045-wb")[0], T(215.80), { dur: 0.3, y: 8 });
      show(words("sc045-wb")[1], T(216.04));
    })();
    whip($("sc045-shot"), $("sc046-shot"), S(216.84), { dir: -1 });

    /* =================== C3S046 · 216.90–223.46 · He becomes an important person in Taiwan … happening in Silicon Valley right now =================== */
    scene("sc046", 216.84, 223.46);
    ground("night", S(216.86));
    (function () {
      const J = M.pac, cam = $("sc046-cam"), svg = $("sc046-svg"), tw = J.taipei, sv = J.sv;
      // ghost map: soft top/bottom edges so the band floats on the night ground
      const mimg = "linear-gradient(180deg, transparent 0%, #000 14%, #000 86%, transparent 100%)";
      $("sc046-map").style.webkitMaskImage = mimg; $("sc046-map").style.maskImage = mimg;
      const f = $("sc046-fill"); Object.assign(f.style, { left: J.tw_box[0] + "px", top: J.tw_box[1] + "px" });
      const a = camAt(0.9, tw[0] + 260, tw[1]); a.x = Math.min(-40, a.x); const b = camAt(0.335, (tw[0] + sv[0]) / 2, (tw[1] + sv[1]) / 2 + 10);
      b.x = Math.min(0, Math.max(1920 - 5896 * 0.335, b.x));
      tl.fromTo(cam, a, Object.assign({}, a, { x: a.x - 30, duration: 2.4, ease: "none", immediateRender: true }), S(216.84));
      tl.to(cam, Object.assign({}, b, { duration: 2.4, ease: E.cam }), S(219.24));
      tl.to(cam, { x: b.x - 12, duration: 1.8, ease: "none" }, S(221.64));
      // Pan's small circle on Taiwan
      const pc = document.createElement("div"); pc.className = "k-abs"; pc.style.cssText = `left:${tw[0] + 50}px;top:${tw[1] - 230}px;width:150px;height:150px;opacity:0`;
      pc.innerHTML = PANSIL(150); cam.appendChild(pc);
      svg.insertAdjacentHTML("beforeend", `<path d="M${tw[0] + 60} ${tw[1] - 100} L${tw[0] + 8} ${tw[1] - 6}" stroke="${BONE}" stroke-width="4" opacity="0.8"/>`);
      pop(pc, S(217.10), 0.8);
      // labels (screen space, placed from the camera at that moment)
      const lt = $("sc046-twl"); lt.style.left = (a.x - 30 + tw[0] * 0.9 + 70) + "px"; lt.style.top = (a.y + tw[1] * 0.9 + 40) + "px";
      tl.set(lt, { opacity: 1 }, T(218.44)); rise(words("sc046-twl")[0], T(218.44), { dur: 0.6, y: 10 });
      hide(lt, S(219.20), 0.25);
      const ls = $("sc046-svl"); ls.style.left = (b.x - 12 + sv[0] * 0.335 - 420) + "px"; ls.style.top = (b.y + sv[1] * 0.335 + 50) + "px";
      tl.set(ls, { opacity: 1 }, T(221.88));
      rise(words("sc046-svl")[0], T(221.88), { dur: 0.6, y: 10 }); rise(words("sc046-svl")[1], T(222.44), { dur: 0.4, y: 8 });
      // Silicon Valley emits (vermilion rings), the signal arcs across the Pacific and reaches Taiwan
      svg.insertAdjacentHTML("beforeend", `<circle cx="${sv[0]}" cy="${sv[1]}" r="20" fill="${RED}" stroke="${INK}" stroke-width="4" id="c3s02-sc046-svd" opacity="0"/>`);
      show($("sc046-svd"), S(221.70));
      gated(221.6, 223.6, () => FX.radioWaves(svg, sv[0], sv[1], { rings: 4, max: 560, period: 1.3, width: 16, color: RED, from: S(221.88), to: S(223.6) }));
      const mx = (tw[0] + sv[0]) / 2, my = Math.min(tw[1], sv[1]) - 520;
      ink(svg, `M${sv[0]} ${sv[1]} Q${mx} ${my} ${tw[0] + 10} ${tw[1] - 10}`, S(221.94), 0.9, { color: BONE, width: 9, ease: C(E.inOut, 0.9), opacity: 0.85 });
      svg.insertAdjacentHTML("beforeend", `<circle cx="${tw[0]}" cy="${tw[1]}" r="60" fill="none" stroke="${CEL}" stroke-width="10" id="c3s02-sc046-twr" opacity="0"/>`);
      tl.fromTo($("sc046-twr"), { attr: { opacity: 0, r: 30 } }, { attr: { opacity: 1, r: 80 }, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(222.84));
    })();

    /* =================== C3S047 · 223.46–228.34 · But he's gonna go back and look and see what made it so =================== */
    scene("sc047", 223.46, 228.34);
    ground("paper", S(223.46));
    (function () {
      // the recipe index card (C3S035 motif, rebuilt here: c3s01 owns the master)
      const rows = [["a great university", "quad_chip.jpg"], ["company", "hp_chip.jpg"], ["industrial park", "park_chip.jpg"], ["people in and out", null]];
      let h = `<div class="k-recipe">`;
      for (let y = 150; y < 760; y += 110) h += `<div class="rl" style="top:${y}px"></div>`;
      h += `<div class="ml"></div><div class="hd t-label">Recipe</div>`;
      rows.forEach((r, i) => {
        h += `<div class="ln t-serif" style="top:${170 + i * 110}px">${r[0]}</div>`;
        if (r[1]) h += `<div class="chip" style="left:${830 + (i % 2) * 40}px;top:${158 + i * 110}px;transform:rotate(${i % 2 ? 3 : -3}deg)"><img src="assets/c3/derived/c3s02/${r[1]}" alt="" /></div>`;
      });
      h += `<svg viewBox="0 0 1200 760"><g fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"><path d="M860 540 L960 540 M940 524 L962 540 L940 556"/><path d="M1080 570 L980 570 M1000 554 L978 570 L1000 586"/></g></svg></div>`;
      $("sc047-cards").innerHTML = h; $("sc047-blur").innerHTML = h;
      const cam = $("sc047-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.15, duration: 1.4, ease: E.cam, immediateRender: true }, S(223.46));
      tl.to(cam, { scale: 1.18, duration: 3.4, ease: "none" }, S(224.86));
      FX.focusHunt(tl, $("sc047-cards"), S(224.90), { dur: 0.8 });
      FX.focalBlur(tl, $("sc047-blur"), [
        { t: S(223.46), x: 760, y: 395, r: 200 },
        { t: S(225.64), x: 830, y: 505, r: 190, dur: 0.9 },
        { t: S(226.55), x: 830, y: 615, r: 190, dur: 0.6 },
        { t: S(227.15), x: 860, y: 725, r: 210, dur: 0.6 },
      ]);
      [T(224.28), T(224.44)].forEach((c, i) => rise(words("sc047-gb")[i], c, { dur: 0.7, y: 12 }));
      [T(226.28), T(226.76), T(227.24)].forEach((c, i) => rise(words("sc047-wm")[i], c, { dur: 0.5, y: 10 }));
      show(words("sc047-wm")[3], T(227.56));
    })();
    whip($("sc047-shot"), $("sc048-shot"), S(228.28), { vertical: true, dir: -1 });

    /* =================== C3S048 · 228.34–235.94 · before we get into that story, let's look at exactly the situation Taiwan is in =================== */
    scene("sc048", 228.28, 235.94);
    ground("night", S(228.30));
    (function () {
      const cam = $("sc048-cam");
      $("sc048-sea").style.background = `rgb(${M.tw_sat.corner.join(",")})`;
      const fe = "linear-gradient(90deg, transparent 0%, #000 6%, #000 94%, transparent 100%)"; $("sc048-map").style.webkitMaskImage = fe; $("sc048-map").style.maskImage = fe;
      tl.fromTo(cam, camAt(0.42, 960, 1250), Object.assign(camAt(0.56, 960, 1380), { duration: 7.66, ease: E.cam, immediateRender: true }), S(228.28));
      // clouds drift in from the north-west, a shadow under the big one
      const cl = [["sc048-c1", -700, -200, 1700, 0.9, 380, 260], ["sc048-sh1", -640, -120, 1700, 1, 380, 260], ["sc048-c2", -900, 900, 1500, 0.8, 300, 160], ["sc048-c3", 1300, -500, 1400, 0.7, -160, 220]];
      cl.forEach(([id, x, y, w, o, dx, dy]) => {
        const el = $(id); Object.assign(el.style, { left: x + "px", top: y + "px", width: w + "px" });
        const base = id === "sc048-sh1" ? 0.35 : o;
        tl.fromTo(el, { x: 0, y: 0, opacity: 0 }, { x: dx, y: dy, opacity: base, duration: 7.66, ease: "none", immediateRender: true }, S(228.28));
      });
      tl.fromTo($("sc048-dark"), { opacity: 0 }, { opacity: 1, duration: 1.4, ease: E.inOut, immediateRender: true }, S(233.64));
      rise(words("sc048-bf")[0], T(230.84), { dur: 0.9, y: 10 });
      hide($("sc048-bf"), S(233.30));
      [T(233.64), T(233.96)].forEach((c, i) => rise(words("sc048-sit")[i], c, { dur: 0.7, y: 12 }));
      rise(words("sc048-tw")[0], T(234.60), { dur: 0.6, y: 16 });
    })();

    /* =================== C3S049 · 235.94–240.50 · Now, of course, everyone wants Silicon Valley, but why did Taiwan want it? =================== */
    scene("sc049", 235.94, 240.50);
    ground("paper", S(235.94));
    (function () {
      const A = M.atlas, k = 1840 / A.size[0] * A.deg, P = (lon, lat) => [(lon - A.lon0) * k, (A.lat0 - lat) * k];
      const svg = $("sc049-svg");
      const spots = [[-77, 38.9], [-99.1, 19.4], [-47.9, -15.8], [-58.4, -34.6], [-0.1, 51.5], [2.35, 48.9], [13.4, 52.5], [37.6, 55.8], [34.8, 32.1], [3.4, 6.5], [36.8, -1.3], [77.6, 13.0], [103.8, 1.35], [127.0, 37.6], [139.7, 35.7], [151.2, -33.9]];
      spots.forEach(([lon, lat], i) => { const [x, y] = P(lon, lat); const g = pin(svg, x, y, PAPER, 9, `c3s02-sc049-p${i}`);
        tl.fromTo(g, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(236.68) + i / 12); });
      const [tx, ty] = P(121.0, 23.7);
      svg.insertAdjacentHTML("beforeend", `<circle cx="${tx}" cy="${ty}" r="7" fill="${CEL}" stroke="${INK}" stroke-width="2"/>`);
      const mf = gated(235.9, 240.6, () => FX.markupDefs(defs, "c3s02-mk049", { boil: 4 }));
      FX.markup.circle(tl, svg, S(239.48), { cx: tx, cy: ty, rx: 46, ry: 38, rot: -10, dur: 0.5, color: INK, width: 5, filter: mf, seed: 4901 });
      const cam = $("sc049-cam");
      tl.fromTo(cam, { scale: 1, x: 0, y: 0 }, { scale: 1.06, x: -40, y: -20, duration: 3.06, ease: "none", immediateRender: true }, S(235.94));
      tl.to(cam, Object.assign(camAt(1.9, 40 + tx, 205 + ty), { duration: 1.5, ease: E.in }), S(239.0));   // push to Taiwan, into the flash
      [T(236.68), T(237.08), T(237.40), T(238.12)].forEach((c, i) => rise(words("sc049-l1")[i], c, { dur: 0.6, y: 12 }));
      rise(words("sc049-l2")[0], T(239.00), { dur: 0.4, y: 10 });
      rise(words("sc049-l2")[1], T(239.48), { dur: 0.4, y: 10 });
      show(words("sc049-l2")[2], T(239.48));
    })();
    whip($("sc049-shot"), $("sc050-shot"), S(240.44), { dir: 1, flash: true });

    /* =================== C3S050 · 240.50–244.74 · And why were they so desperate? This is when we come back to Taiwan =================== */
    scene("sc050", 240.44, 245.10);
    ground("night", S(240.46));
    (function () {
      tl.fromTo($("sc050-cam"), { scale: 1.0 }, { scale: 1.07, duration: 4.66, ease: "none", immediateRender: true }, S(240.44));
      gated(240.44, 245.1, () => FX.weave($("sc050-wv"), { amp: 0.8, flicker: 0.03, seed: 5001 }));
      rise(words("sc050-des")[0], T(241.56), { dur: 1.0, y: 18 });
      hide($("sc050-des"), S(243.30));
      rise(words("sc050-btt")[0], T(243.72), { dur: 0.3, y: 8 });
      show(words("sc050-btt")[1], T(243.88)); show(words("sc050-btt")[2], T(244.12));
    })();
    slideIn($("sc051-shot"), S(244.68), { from: "up" });

    /* =================== C3S051 · 244.74–253.94 · while the Silicon Valley is on the up and up, Taiwan is … facing … existential crises =================== */
    scene("sc051", 244.68, 253.98);
    ground("paper", S(244.90));
    (function () {
      const svg = $("sc051-svg");
      svg.innerHTML = `<defs><pattern id="c3s02-hatch" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="16" height="16" fill="${INK}" opacity="0.05"/><line x1="0" y1="0" x2="0" y2="16" stroke="${INK}" stroke-width="3" opacity="0.18"/></pattern></defs>
        <path d="M150 120 L150 940 L2150 940" fill="none" stroke="${INK}" stroke-width="4" opacity="0.7"/>
        <rect id="c3s02-sc051-band" x="1290" y="110" width="520" height="830" fill="url(#c3s02-hatch)" opacity="0"/>`;
      ink(svg, "M300 560 C500 552 650 540 800 515 C1000 480 1150 420 1350 330 C1550 240 1750 190 1950 150", S(246.76), 1.3, { color: NAVY, width: 8 });
      ink(svg, "M300 640 C520 636 760 630 980 632 C1120 634 1200 650 1300 700 C1420 760 1540 830 1700 862", S(248.84), 1.2, { color: INK, width: 8 });
      svg.insertAdjacentHTML("beforeend", `<circle id="c3s02-sc051-dot" cx="1700" cy="862" r="17" fill="${CEL}" stroke="${INK}" stroke-width="4" opacity="0"/>`);
      pop($("sc051-dot"), S(250.0), 0.6);
      tl.fromTo($("sc051-band"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(250.12));
      tl.fromTo($("sc051-cam"), { x: 0 }, { x: -140, duration: 8.6, ease: E.cam, immediateRender: true }, S(244.90));
      [T(245.32), T(245.96)].forEach((c, i) => rise(words("sc051-sv")[i], c, { dur: 0.6, y: 8 }));
      [T(246.76), T(247.08), T(247.24)].forEach((c, i) => rise(words("sc051-uu")[i], c, { dur: 0.6, y: 10 }));
      rise(words("sc051-tw")[0], T(247.80), { dur: 0.6, y: 8 });
      [T(250.12), T(251.00)].forEach((c, i) => rise(words("sc051-ec")[i], c, { dur: 0.8, y: 12 }));
    })();
    whip($("sc051-shot"), $("sc052-shot"), S(253.88), { dir: 1 });

    /* =================== C3S052 · 253.94–261.05 · the UN had just kicked out Taiwan, the Republic of China, as a country =================== */
    scene("sc052", 253.88, 261.05);
    ground("night", S(253.90));
    (function () {
      const cam = $("sc052-cam");
      tl.fromTo(cam, camAt(0.42, 1500, 1350), Object.assign(camAt(0.78, 2230, 820), { duration: 2.6, ease: E.cam, immediateRender: true }), S(254.30));
      tl.to(cam, Object.assign(camAt(0.84, 2200, 860), { duration: 4.1, ease: "none" }), S(256.90));
      tl.fromTo($("sc052-ht"), { opacity: 0.12 }, { opacity: 0.3, duration: 2.6, ease: E.cam, immediateRender: true }, S(254.30));
      FX.focusHunt(tl, $("sc052-stage"), S(256.95), { dur: 0.8 });
      const mf = gated(253.8, 261.2, () => FX.markupDefs(defs, "c3s02-mk052", { boil: 12 }));
      FX.markup.box(tl, $("sc052-mk"), S(257.16), { x: 1470, y: 590, w: 1500, h: 300, dur: 0.7, color: INK, width: 12, filter: mf });
      [T(257.16), T(257.56)].forEach((c, i) => rise(words("sc052-ko")[i], c, { dur: 0.7, y: 12 }));
      [T(258.44), T(258.92), T(259.08)].forEach((c, i) => rise(words("sc052-roc")[i], c, { dur: 0.6, y: 8 }));
    })();
