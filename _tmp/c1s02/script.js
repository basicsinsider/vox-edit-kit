  (function () {
    const SEG = "c1s02", SEG_START = 208.43, SEG_END = 402.83, DURATION = +(SEG_END - SEG_START).toFixed(2);
    const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues, LOCAL c1 seconds (audited)
    const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
    const L = 0.06;                                  // text lands 60 ms before its word
    const tl = gsap.timeline({ paused: true });
    const $ = (id) => document.getElementById(SEG + "-" + id);
    const NS = "http://www.w3.org/2000/svg";
    const C = (e, d) => FX.choppy(e, d, 12);
    const defs = $("defs");
    const INK = "#141b24", NAVY = "#1d5c9e", SKY = "#9fc3e3", RED = "#e03f2c", BONE = "#f2ede3", YEL = "#f2d33b";

    // ---------- shared filters ----------
    FX.tintDefs(defs, "c1s02-tintbg", "#2b2825", "#9c907e");
    FX.tintDefs(defs, "c1s02-tint", "#1d1a17", "#f0e6d3");
    FX.tintDefs(defs, "c1s02-tintp", "#3a342c", "#efe7d6");
    FX.roughDefs(defs, "c1s02-rough", { freq: 0.045, scale: 6 });   // torn card edges (permanent boil allowed)
    const choke36 = FX.roughDefs(defs, "c1s02-choke36", { freq: 0.04, scale: 8, choke: 0 });
    const blurs = {};
    ["035","036","037","038","039","040","040a","040b","041","042","043","044","045","047","048","049","050","051","052","053","054","055","056","057","058","059","060","060a","060b","061","062","063","064","065","066","067","068","069","070"].forEach((k) => { blurs[k] = FX.whipDefs(defs, "c1s02-wb" + k); });

    // ---------- helpers ----------
    const scenes = [];
    function scene(k, a, b) {
      const el = $("sc" + k); scenes.push([el, a]);
      if (S(a) <= 0) gsap.set(el, { autoAlpha: 1 });
      else { tl.set(el, { display: "block" }, S(a) - 0.002); tl.fromTo(el, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.001, immediateRender: false }, S(a)); }
      if (b < SEG_END) { tl.set(el, { autoAlpha: 0 }, S(b)); tl.set(el, { display: "none" }, S(b) + 0.002); }
    }
    function E(x) { return typeof x === "string" ? $(x) : x; }
    function rise(el, t, o) {
      o = o || {}; el = E(el);
      tl.fromTo(el, { opacity: 0, y: o.y == null ? 18 : o.y }, { opacity: 1, y: 0, duration: o.dur || 0.9, ease: C(FX.ease.out, o.dur || 0.9), immediateRender: true }, t);
    }
    function pop(el, t, o) {
      o = o || {}; el = E(el);
      tl.fromTo(el, { opacity: 0, scale: o.from || 0.6 }, { opacity: 1, scale: 1, duration: o.dur || 1.0, ease: C(FX.ease.out, o.dur || 1.0), immediateRender: true }, t);
    }
    function out(el, t, d) { el = E(el); tl.to(el, { opacity: 0, duration: d || 0.3, ease: C(FX.ease.in, d || 0.3) }, t); }
    function slideIn(el, t, o) {   // card / paper slides in (stop-motion 12 fps, long tail)
      o = o || {}; el = E(el);
      tl.fromTo(el, { opacity: 1, x: o.x || 0, y: o.y || 0, rotation: o.r0 == null ? 0 : o.r0 }, { opacity: 1, x: 0, y: 0, rotation: o.r == null ? 0 : o.r, duration: o.dur || 1.0, ease: C(FX.ease.out, o.dur || 1.0), immediateRender: true }, t);
    }
    function ground(kind, t) {
      const v = kind === "paper" ? [0.32, 0.14, 0.24] : [1, 0.42, 0.36];
      if (t <= 0) gsap.set(["#c1s02-vig", "#c1s02-dust", "#c1s02-grain"], { opacity: (i) => v[i] });
      else tl.set(["#c1s02-vig", "#c1s02-dust", "#c1s02-grain"], { opacity: (i) => v[i] }, t);
    }
    // whip between two layers, blur filter only on while it runs
    function whipEl(a, b, ka, kb, t, o) {
      o = Object.assign({ dir: 1, vertical: false }, o);
      tl.set(a, { filter: "url(#c1s02-wb" + ka + ")" }, t - 0.17);
      tl.set(b, { filter: "url(#c1s02-wb" + kb + ")", visibility: "visible" }, t - 0.001);
      FX.whip(tl, a, b, t, Object.assign({ blurA: blurs[ka], blurB: blurs[kb] }, o));
      tl.set(b, { filter: "none" }, t + 0.2);
    }
    function whip(ka, kb, t, o) { whipEl($("sc" + ka), $("sc" + kb), ka, kb, t, o); }
    function flash(t) {
      tl.fromTo("#c1s02-flash", { opacity: 0 }, { opacity: 0.85, duration: 0.08, ease: "power2.in", immediateRender: false }, t - 0.08);
      tl.to("#c1s02-flash", { opacity: 0, duration: 0.22, ease: "power2.out" }, t);
    }
    // paper slide: outgoing scene slides off left (above), revealing the next scene underneath
    function slideOut(k, t) {
      const a = $("sc" + k);
      tl.set(a, { zIndex: 6, boxShadow: "30px 0 40px rgba(0,0,0,0.45)" }, t - 0.4);
      tl.fromTo(a, { x: 0 }, { x: -2050, duration: 0.4, ease: C(FX.ease.in, 0.4), immediateRender: false }, t - 0.4);
    }
    // paper slide: incoming scene slides over from the right
    function slideOver(k, t) {
      const b = $("sc" + k);
      tl.set(b, { zIndex: 6 }, t - 0.001);
      tl.fromTo(b, { x: 1980 }, { x: 0, duration: 0.42, ease: C(FX.ease.out, 0.42), immediateRender: false }, t);
      tl.set(b, { zIndex: 0 }, t + 0.5);
    }
    function svgEl(tag, attrs, parent) { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
    function ink(parent, d, t, dur, o) {
      o = o || {};
      const p = svgEl("path", { d, fill: "none", stroke: o.color || INK, "stroke-width": o.width || 6, "stroke-linecap": "round", "stroke-linejoin": "round" }, parent);
      if (o.filter) p.setAttribute("filter", o.filter);
      if (o.opacity) p.setAttribute("opacity", o.opacity);
      if (o.blend) p.style.mixBlendMode = o.blend;
      const len = p.getTotalLength() || 1;
      p.setAttribute("stroke-dasharray", len + " " + len); p.setAttribute("stroke-dashoffset", len);
      tl.fromTo(p, { attr: { "stroke-dashoffset": len } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: o.ease || C(FX.ease.inOut, dur), immediateRender: true }, t);
      return p;
    }
    function gated(a, b, fn) { const o = FX.onFrame; FX.onFrame = (f) => o(FX.gate(S(a) - 0.1, S(b) + 0.1, f)); try { fn(); } finally { FX.onFrame = o; } }
    function camTo(el, from, to, t, dur, ease) { tl.fromTo(E(el), from, Object.assign({ duration: dur, ease: ease || "none", immediateRender: t <= 0.01 }, to), t); }

    // ---------- global textures ----------
    FX.grain($("grain"), 3501);
    FX.dust($("dust"), 3502, 2);

    /* ============ C1S035 · 208.43–212.83 · exam sheet (GRID) ============ */
    scene("035", 208.43, 212.83);
    ground("paper", 0);
    (function () {
      // incoming half of the c1s01 W↓ whip: smears in from the top, lands sharp by 208.70
      const sc = $("sc035");
      gsap.set(sc, { filter: "url(#c1s02-wb035)" });
      const sb = { v: 90 };
      tl.fromTo(sc, { y: -400, scale: 1.18 }, { y: 0, scale: 1, duration: 0.27, ease: "power3.out", immediateRender: true }, 0);
      tl.fromTo(sb, { v: 90 }, { v: 0, duration: 0.27, ease: "power2.out", immediateRender: true, onUpdate: () => blurs["035"].setAttribute("stdDeviation", "0 " + sb.v.toFixed(1)) }, 0);
      tl.set(sc, { filter: "none" }, S(208.72));
      camTo("sc035-cam", { scale: 1.0 }, { scale: 1.07 }, 0, 4.4);
      tl.to("#c1s02-sc035-cam", { scale: 1.16, duration: 0.5, ease: FX.ease.in }, S(212.33));   // cut on action
      rise("sc035-hoover", T(208.83) - L, { dur: 1.0 });
      rise("sc035-w1", T(209.63) - L);
      rise("sc035-w2", T(210.11) - L);
      rise("sc035-w3", T(210.35) - L);
      rise("sc035-w4", T(210.59) - L);
      rise("sc035-stan", T(212.11) - L, { dur: 0.6 });
      // pen crosses in the grade boxes, one per subject
      const svg = $("sc035-svg"), f = FX.markupDefs(svg, "c1s02-mk35", { boil: 4 });
      svg.setAttribute("viewBox", "0 0 840 920");
      [0, 1, 2, 3, 4].forEach((i) => {
        const cx = 714, cy = 337 + i * 100, s = 22, t0 = S(209.60) + i * 0.24;
        ink(svg, `M${cx - s} ${cy - s} L${cx + s + 3} ${cy + s}`, t0, 0.1, { width: 5, filter: f, blend: "multiply" });
        ink(svg, `M${cx + s} ${cy - s - 2} L${cx - s} ${cy + s + 2}`, t0 + 0.11, 0.1, { width: 5, filter: f, blend: "multiply" });
      });
    })();

    /* ============ C1S036 · 212.83–216.59 · Quaker → admitted (NIGHT) ============ */
    scene("036", 212.83, 216.66);
    ground("night", S(212.83));
    (function () {
      camTo("sc036-cam", { x: 30, scale: 1.12 }, { x: -50, scale: 1.07 }, S(212.83), 3.8);
      rise("sc036-q", T(213.47) - L, { dur: 1.1, y: 26 });
      tl.fromTo("#c1s02-sc036-card", { opacity: 0, x: 500, rotation: 12 }, { opacity: 1, x: 0, rotation: 4, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(214.30));
      const st = $("sc036-stamp");
      st.style.filter = "url(#c1s02-choke36)";
      tl.fromTo(st, { opacity: 0, scale: 1.7 }, { opacity: 0.92, scale: 1, duration: 0.2, ease: C("power2.in", 0.2), immediateRender: true }, T(215.15) - L);
      FX.chokeSettle(tl, choke36, st, T(215.15) - L, 4, 0.45, "none");
      tl.fromTo("#c1s02-sc036-card", { x: 0 }, { x: -10, duration: 1 / 12, yoyo: true, repeat: 1, ease: "none", immediateRender: false }, S(215.30));
    })();

    /* ============ C1S037 · 216.59–220.40 · back then vs now (PAPER) ============ */
    whip("036", "037", S(216.59), { dir: 1 });
    scene("037", 216.59, 220.9);
    ground("paper", S(216.59));
    (function () {
      camTo("sc037-cam", { scale: 1 }, { scale: 1.035 }, S(216.59), 3.9);
      slideIn("sc037-p1", S(216.62), { x: -260, r0: -8, r: -3, dur: 1.0 });
      gsap.set("#c1s02-sc037-p2", { opacity: 0 });
      slideIn("sc037-p2", S(218.62), { x: 300, r0: 9, r: 2.5, dur: 1.0 });
      tl.fromTo("#c1s02-sc037-cr", { opacity: 0 }, { opacity: 1, duration: 0.3, immediateRender: true }, S(218.7));
      rise("sc037-w1", T(217.07) - L);
      rise("sc037-w2", T(217.23) - L);
      tl.fromTo("#c1s02-sc037-now", { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: true }, T(219.63) - L);
      const mk = $("sc037-mk"), f = FX.markupDefs(mk, "c1s02-mk37", { boil: 4 });
      FX.markup.pen(tl, mk, S(218.72), { points: [[830, 760], [960, 690], [1080, 760]], color: INK, width: 6, dur: 0.6, filter: f, seed: 37 });
      FX.markup.pen(tl, mk, S(218.72) + 0.55, { points: [[1050, 735], [1082, 762], [1046, 784]], color: INK, width: 6, dur: 0.2, filter: f, seed: 38 });
      FX.markup.circle(tl, mk, S(219.42), { cx: 1420, cy: 900, rx: 170, ry: 92, color: RED, width: 7, dur: 0.42, filter: f, seed: 371 });
    })();

    /* ============ C1S038 · 220.40–224.08 · he met his wife (PAPER) ============ */
    slideOver("038", S(220.40));
    scene("038", 220.40, 224.25);
    (function () {
      gsap.set("#c1s02-sc038-h", { x: -40 });
      tl.fromTo("#c1s02-sc038-h", { x: -40, rotation: -4 }, { x: 20, rotation: -2, duration: 1.4, ease: C(FX.ease.inOut, 1.4), immediateRender: false }, S(222.9));
      tl.fromTo("#c1s02-sc038-l", { opacity: 1, x: 420, y: 60, rotation: 12 }, { opacity: 1, x: -20, y: 0, rotation: 3.5, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(222.90));
      rise("sc038-w1", T(221.52) - L);
      rise("sc038-w2", T(221.76) - L);
      rise("sc038-w3", T(223.36) - L, { dur: 0.5 });
      rise("sc038-w4", T(223.52) - L, { dur: 0.5 });
      const mk = $("sc038-mk"), f = FX.markupDefs(mk, "c1s02-mk38", { boil: 4 });
      // pen loop joining the two cards
      FX.markup.pen(tl, mk, S(223.12), { points: [[850, 500], [930, 440], [990, 470], [960, 540], [905, 520], [940, 455], [1060, 470]], color: RED, width: 6, dur: 0.45, filter: f, seed: 381 });
    })();

    /* ============ C1S039 · 224.08–229.60 · Hoover 1928 newsreel (NIGHT) ============ */
    whip("038", "039", S(224.20), { dir: 1 });
    scene("039", 224.20, 229.60);
    ground("night", S(224.20));
    (function () {
      gated(224.0, 229.7, () => FX.weave($("sc039-weave"), { amp: 1.8, flicker: 0.05, seed: 391 }));
      camTo("sc039-cam", { scale: 1.0 }, { scale: 1.05 }, S(224.20), 4.9);
      tl.to("#c1s02-sc039-cam", { scale: 1.16, duration: 0.5, ease: FX.ease.in }, S(229.10));
      tl.fromTo("#c1s02-sc039-v1", { opacity: 1 }, { opacity: 0, duration: 0.001, immediateRender: false }, S(227.0));
      rise("sc039-w1", T(227.12) - L);
      rise("sc039-w2", T(227.52) - L);
    })();

    /* ============ C1S040 · 229.60–233.68 · Commerce → White House (NIGHT) ============ */
    scene("040", 229.60, 233.75);
    (function () {
      camTo("sc040-acam", { scale: 1.16 }, { scale: 1.02 }, S(229.60), 3.0, FX.ease.cam);
      rise("sc040-w1", T(229.76) - L, { dur: 0.6 });
      rise("sc040-w2", T(229.84) - L, { dur: 0.6 });
      tl.fromTo("#c1s02-sc040-plate", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(230.45));
      rise("sc040-w3", T(230.64) - L, { y: 8 });
      rise("sc040-w4", T(231.28) - L, { y: 8 });
      rise("sc040-w5", T(231.52) - L, { y: 8 });
      whipEl($("sc040-a"), $("sc040-b"), "040a", "040b", S(232.62), { dir: 1 });
      camTo("sc040-bcam", { scale: 1.0 }, { scale: 1.45 }, S(232.62), 1.1, FX.ease.cam);
      const mk = $("sc040-mk"), f = FX.markupDefs(mk, "c1s02-mk40", { boil: 4 });
      FX.markup.circle(tl, mk, S(232.78), { cx: 1003, cy: 334, rx: 120, ry: 62, color: BONE, width: 5, dur: 0.38, filter: f, seed: 401 });
      rise("sc040-w6", T(233.04) - L, { dur: 0.35, y: 10 });
      rise("sc040-w7", T(233.28) - L, { dur: 0.3, y: 10 });
    })();

    /* ============ C1S041 · 233.68–240.48 · board of trustees (PAPER, D06) ============ */
    flash(S(233.68));
    whip("040", "041", S(233.68), { dir: 1 });
    scene("041", 233.68, 240.48);
    ground("paper", S(233.68));
    (function () {
      const box = $("sc041-seats"), cx = 960, cy = 800, seats = [];
      const rows = [[340, 9], [230, 6]];
      rows.forEach(([r, n]) => { for (let i = 0; i < n; i++) { const a = Math.PI - (i / (n - 1)) * Math.PI; seats.push({ a, x: cx + Math.cos(a) * r, y: cy - Math.sin(a) * r }); } });
      seats.sort((p, q) => q.a - p.a || p.y - q.y);
      const ds = seats.map((p) => { const d = document.createElement("div"); d.className = "c2-seat"; d.style.left = (p.x - 28) + "px"; d.style.top = (p.y - 28) + "px"; box.appendChild(d); return d; });
      ds.forEach((d, i) => tl.fromTo(d, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(FX.ease.out, 0.25), immediateRender: true }, S(234.0) + Math.floor(i / 2) / 12));
      ds.forEach((d, i) => tl.to(d, { backgroundColor: INK, duration: 0.001 }, S(235.50) + Math.floor(i / 2) / 12));
      // Hoover's seat = the top of the outer arc: it swells into his portrait
      const top = ds[seats.findIndex((p) => Math.abs(p.a - Math.PI / 2) < 0.01)];
      tl.to(top, { opacity: 0, duration: 0.2 }, S(237.0));
      gsap.set("#c1s02-sc041-hoov", { left: 860, top: 360 });
      pop("sc041-hoov", S(237.0), { from: 0.28, dur: 1.2 });
      rise("sc041-w1", T(235.52) - L);
      rise("sc041-w2", T(236.40) - L);
      rise("sc041-w3", T(236.72) - L);
      rise("sc041-w4", T(236.88) - L);
      rise("sc041-w5", T(239.60) - L, { dur: 0.5 });
      rise("sc041-w6", T(240.00) - L, { dur: 0.3 });
      rise("sc041-w7", T(240.16) - L, { dur: 0.3 });
      $("sc041-hlb").style.filter = "url(#c1s02-rough)";
      tl.fromTo("#c1s02-sc041-hlb", { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: C("sine.inOut", 0.4), immediateRender: true }, S(239.56));
      camTo("sc041-cam", { scale: 1 }, { scale: 1.04 }, S(233.68), 6.3);
      tl.to("#c1s02-sc041-cam", { scale: 1.14, duration: 0.45, ease: FX.ease.in }, S(240.03));
    })();

    /* ============ C1S042 · 240.48–245.28 · the ledger (GRID) ============ */
    scene("042", 240.48, 245.45);
    (function () {
      camTo("sc042-cam", { y: 40, scale: 1.05 }, { y: -170, scale: 1.0 }, S(240.48), 4.8, FX.ease.cam);
      const svg = $("sc042-mk"), f = FX.markupDefs(svg, "c1s02-mk42", { boil: 4 });
      svg.setAttribute("viewBox", "0 0 980 1004");
      [0, 1, 2, 3, 4].forEach((i) => {
        const x = 880, y = 300 + i * 92, t0 = S(241.58) + i * 0.24;
        ink(svg, `M${x - 18} ${y} L${x - 4} ${y + 18} L${x + 26} ${y - 26}`, t0, 0.16, { color: NAVY, width: 6, filter: f, blend: "multiply" });
      });
      rise("sc042-w1", T(241.60) - L);
      rise("sc042-w2", T(241.76) - L);
      rise("sc042-w3", T(241.92) - L);
      rise("sc042-w4", T(244.24) - L, { dur: 0.6 });
      rise("sc042-w5", T(244.64) - L, { dur: 0.5 });
    })();

    /* ============ C1S043 · 245.28–250.64 · money flows, trusted people (NIGHT, D11) ============ */
    whip("042", "043", S(245.36), { dir: -1 });
    scene("043", 245.36, 250.80);
    ground("night", S(245.36));
    (function () {
      // map: Stanford (crop px 356,709) placed at screen (725,540)
      camTo("sc043-cam", { x: 725 - 356 * 1.0 + 30, y: 540 - 709 * 1.0, scale: 1.0 }, { x: 725 - 356 * 1.0 - 30, y: 540 - 709 * 1.0 }, S(245.36), 5.3);
      const map = $("sc043-map");
      const ca = "/*CA*/";
      const g = svgEl("g", { transform: "matrix(0.4272,0,0,0.34219,182.04,136.53)" }, map);
      const caFill = svgEl("path", { d: ca, fill: RED, "fill-opacity": 0.16, stroke: RED, "stroke-width": 7, "stroke-opacity": 0.85 }, g);
      caFill.style.filter = "drop-shadow(0 0 10px rgba(224,63,44,0.8))";
      tl.fromTo(g, { opacity: 0 }, { opacity: 1, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(245.45));
      pop("sc043-box", S(245.70), { from: 0.8, dur: 0.9 });
      const svg = $("sc043-svg");
      // incoming money: bone ribbons from the left converge into the Stanford box
      [[120, 32], [330, 24], [930, 28]].forEach(([y0, w], i) => {
        ink(svg, `M-20 ${y0} C 300 ${y0} 420 ${430 + i * 110} 640 ${430 + i * 110}`, S(246.30) + i * 0.15, 1.2, { color: BONE, width: w, opacity: 0.4 });
      });
      // out to the people he trusted (vermilion)
      [290, 540, 790].forEach((y, i) => {
        ink(svg, `M810 ${450 + i * 90} C 1100 ${450 + i * 90} 1150 ${y} 1420 ${y}`, S(248.0) + i * 0.15, 0.9, { color: RED, width: 18, opacity: 0.75 });
      });
      pop("sc043-c1", S(248.98), { from: 0.5, dur: 0.8 });
      pop("sc043-c2", S(249.10), { from: 0.5, dur: 0.8 });
      pop("sc043-c3", S(249.22), { from: 0.5, dur: 0.8 });
      rise("sc043-w1", T(246.32) - L);
      rise("sc043-w2", T(246.48) - L);
      rise("sc043-w3", T(248.00) - L);
      rise("sc043-w4", T(248.32) - L);
      rise("sc043-w5", T(248.56) - L);
      rise("sc043-w6", T(249.04) - L, { y: 8 });
      rise("sc043-w7", T(249.20) - L, { y: 8 });
    })();

    /* ============ C1S044 · 250.64–255.92 · 1925 (NIGHT) ============ */
    whip("043", "044", S(250.72), { dir: 1, vertical: true });
    scene("044", 250.72, 255.92);
    (function () {
      camTo("sc044-cam", { scale: 1.0 }, { scale: 1.07 }, S(250.72), 4.7);
      tl.to("#c1s02-sc044-cam", { scale: 1.16, duration: 0.5, ease: FX.ease.in }, S(255.42));
      FX.text.odometer(tl, $("sc044-yr"), T(251.44) - L, { dur: 0.9, stagger: 0.05, seed: 44 });
      rise("sc044-w1", T(254.08) - L);
      rise("sc044-w2", T(254.56) - L);
      rise("sc044-w3", T(255.20) - L, { dur: 0.6 });
      tl.fromTo("#c1s02-sc044-obj", { opacity: 0 }, { opacity: 0.85, duration: 0.5, immediateRender: true }, S(254.15));
    })();

    /* ============ C1S045–046 · 255.92–270.08 · painting → print (§10.7) ============ */
    scene("045", 255.92, 270.08);
    (function () {
      // body copy = the narrator's own words (no invented claims), 22 px Crimson Pro, typeset columns
      const body = "His argument for this was pretty simple, and that's the argument we're gonna see Terman make very soon. ";
      const cols = $("sc045-cols");
      [[330, 180, 520, 1240], [1580, 180, 500, 1240], [870, 1240, 660, 300]].forEach(([x, y, w, h], i) => {
        const d = document.createElement("div"); d.className = "c2-col t-serif"; d.style.cssText = `left:${x}px;top:${y}px;width:${w}px;height:${h}px;overflow:hidden`;
        d.textContent = body.repeat(14); cols.appendChild(d);
      });
      [[880, 180, 1200], [1545, 180, 1240]].forEach(([x, y, h]) => { const r = document.createElement("div"); r.className = "c2-colrule"; r.style.cssText = `left:${x}px;top:${y}px;height:${h}px`; cols.appendChild(r); });
      // pull-quote, word by word with a pen underline per word
      const q = $("sc045-quote");
      const words = [["I", T(263.12)], ["don't", T(263.20)], ["want", T(263.36)], ["all", T(263.52)], ["these", T(263.76)], ["young", T(263.92)], ["Californians", T(264.24)], ["going", T(264.88)], ["east", T(265.20)], ["just", T(265.68)], ["for", T(265.84)], ["business", T(266.08)], ["training", T(266.40)], ["and", T(266.72)], ["not", T(266.88)], ["coming", T(267.12)], ["back.", T(267.44)]];
      q.innerHTML = "“";
      words.forEach(([w, t], i) => {
        const s = document.createElement("span"); s.className = "c2-w"; s.textContent = w;
        if (w === "east") s.style.color = NAVY;
        const u = document.createElement("i"); u.className = "c2-ul"; u.style.filter = "url(#c1s02-rough)"; if (w === "east") u.style.background = NAVY;
        s.appendChild(u); q.appendChild(s); q.appendChild(document.createTextNode(i < words.length - 1 ? " " : "”"));
        tl.fromTo(s, { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.3, ease: C(FX.ease.out, 0.3), immediateRender: true }, t - L);
        tl.fromTo(u, { scaleX: 0 }, { scaleX: 1, duration: 0.22, ease: C("sine.inOut", 0.22), immediateRender: true }, t - L + 0.04);
      });
      // camera: phase A = painting full frame (frame 520 px wide → ×3.69), push to ×3.85; phase B = pull back + pan, tilt −3°
      const cam = $("sc045-cam");
      gsap.set(cam, { x: 960 - 3.69 * 1200, y: 540 - 3.69 * 337, scale: 3.69, rotation: 0 });
      tl.fromTo(cam, { x: 960 - 3.69 * 1200, y: 540 - 3.69 * 337, scale: 3.69, rotation: 0 }, { x: 960 - 3.85 * 1200, y: 540 - 3.85 * 337, scale: 3.85, duration: 6.08, ease: "none", immediateRender: false }, S(255.92));
      tl.to(cam, { x: -150.6, y: -14.6, scale: 0.9, rotation: -3, duration: 1.25, ease: FX.ease.cam }, S(262.00));
      tl.to(cam, { x: -190, y: -40, scale: 0.94, duration: 6.85, ease: "none" }, S(263.25));
      tl.fromTo("#c1s02-sc045-print", { opacity: 0 }, { opacity: 1, duration: 1.0, ease: C(FX.ease.inOut, 1.0), immediateRender: true }, S(262.05));
      tl.fromTo("#c1s02-sc045-paint", { filter: "saturate(1) contrast(1)" }, { filter: "saturate(0.15) contrast(1.15)", duration: 1.0, ease: "none", immediateRender: true }, S(262.05));
      tl.set("#c1s02-sc045", { backgroundColor: "#e6dcc6" }, S(262.4));
      ground("paper", S(262.6));
      // phase-A overlays
      rise("sc045-w1", T(256.32) - L);
      rise("sc045-w2", T(257.52) - L);
      rise("sc045-w3", T(257.76) - L);
      tl.fromTo("#c1s02-sc045-tc", { opacity: 0, x: 300, rotation: 14 }, { opacity: 1, x: 0, rotation: 4, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(260.30));
      rise("sc045-w4", T(260.48) - L, { y: 8, dur: 0.6 });
      tl.to("#c1s02-sc045-ov", { opacity: 0, duration: 0.3, ease: C(FX.ease.in, 0.3) }, S(261.65));
      tl.to("#c1s02-sc045-cr", { opacity: 0, duration: 0.3 }, S(261.65));
      // phase-A ground
      ground("night", S(255.92));
    })();

    /* ============ C1S047 · 270.08–277.60 · around the world, first in the West (NIGHT, D13) ============ */
    scene("047", 270.08, 277.70);
    ground("night", S(270.08));
    (function () {
      const sx = 616.9, sy = 560.7;
      gsap.set("#c1s02-sc047-cam", { x: 0, y: 60, scale: 0.5 });
      tl.fromTo("#c1s02-sc047-cam", { x: 0, y: 60, scale: 0.5 }, { x: 790 - 0.82 * sx, y: 560 - 0.82 * sy, scale: 0.82, duration: 7.5, ease: FX.ease.cam, immediateRender: false }, S(270.08));
      const svg = $("sc047-svg");
      const gS = svgEl("g", {}, svg), gE = svgEl("g", { opacity: 0.55 }, svg);
      gated(270.0, 277.8, () => {
        FX.radioWaves(gS, sx, sy, { rings: 4, max: 340, period: 1.6, width: 10, color: RED, from: S(270.30), to: S(277.8) });
        [[1918.9, 409.6, 272.80], [3410, 579.6, 273.10], [2747, 821.6, 273.35], [2291, 618.5, 273.55], [3136.6, 719.5, 273.80], [1423, 1210.7, 274.00]].forEach(([x, y, t], i) => {
          FX.radioWaves(gE, x, y, { rings: 3, max: 150, period: 1.4 + i * 0.07, width: 5, color: BONE, from: S(t), to: S(277.8) });
          const d = svgEl("circle", { cx: x, cy: y, r: 9, fill: BONE }, gE); pop(d, S(t), { from: 0.2, dur: 0.6 });
        });
      });
      const dot = svgEl("circle", { cx: sx, cy: sy, r: 16, fill: RED }, svg);
      dot.style.transformOrigin = sx + "px " + sy + "px"; dot.style.transformBox = "view-box";
      pop(dot, S(270.25), { from: 0.2, dur: 0.8 });
      tl.fromTo(dot, { scale: 1 }, { scale: 2.0, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: false }, S(275.70));
      tl.fromTo(gE, { opacity: 0.55 }, { opacity: 0.25, duration: 0.8, immediateRender: false }, S(275.70));
      rise("sc047-w1", T(273.36) - L);
      rise("sc047-w2", T(273.52) - L);
      rise("sc047-w3", T(273.84) - L);
      rise("sc047-w4", T(273.92) - L);
      out("sc047-l1", S(275.3), 0.35);
      rise("sc047-w5", T(275.76) - L);
      rise("sc047-w6", T(276.96) - L, { dur: 0.5, y: 8 });
      rise("sc047-w7", T(277.04) - L, { dur: 0.5, y: 8 });
    })();

    /* ============ C1S048 · 277.60–283.91 · the father of Silicon Valley (NIGHT) ============ */
    flash(S(277.68));
    whip("047", "048", S(277.68), { dir: 1 });
    scene("048", 277.68, 283.91);
    (function () {
      gated(277.5, 284.0, () => FX.streaks($("sc048-streaks"), { seed: 4801, speed: 0.4, gain: 0.9 }));
      camTo("sc048-cam", { scale: 1.0 }, { scale: 1.06 }, S(277.68), 5.8);
      tl.to("#c1s02-sc048-cam", { scale: 1.2, duration: 0.45, ease: FX.ease.in }, S(283.46));
      rise("sc048-w1", T(279.03) - L);
      rise("sc048-w2", T(279.27) - L);
      rise("sc048-w3", T(279.51) - L);
      rise("sc048-w4", T(279.91) - L, { y: 8 });
      rise("sc048-w5", T(279.99) - L, { y: 8 });
      rise("sc048-w6", T(280.23) - L, { y: 8 });
      FX.text.random(tl, $("sc048-sil"), T(280.39) - L, { dur: 0.5, seed: 481 });
      FX.text.random(tl, $("sc048-val"), T(281.11) - L, { dur: 0.5, seed: 482 });
    })();

    /* ============ C1S049 · 283.91–287.43 · Frederick Terman, born 1900 (PAPER) ============ */
    scene("049", 283.91, 287.43);
    ground("paper", S(283.91));
    (function () {
      tl.fromTo("#c1s02-sc049-p1", { x: -30 }, { x: 40, duration: 3.6, ease: "none", immediateRender: true }, S(283.91));
      tl.fromTo("#c1s02-sc049-p2", { x: 40 }, { x: -50, duration: 3.6, ease: "none", immediateRender: true }, S(283.91));
      tl.fromTo("#c1s02-sc049-t", { y: 120, rotation: -6, opacity: 1 }, { y: 0, rotation: -1.5, duration: 1.1, ease: C(FX.ease.out, 1.1), immediateRender: true }, S(283.91));
      rise("sc049-w1", T(284.63) - L);
      rise("sc049-w2", T(285.19) - L);
      rise("sc049-w3", T(286.07) - L);
      FX.text.odometer(tl, $("sc049-yr"), T(286.47) - L, { dur: 0.5, stagger: 0.04, seed: 49 });
    })();

    /* ============ C1S050 · 287.43–296.47 · 1900 → 2000 (GRID) ============ */
    scene("050", 287.43, 296.50);
    (function () {
      // match cut: the 1900 sits exactly where C1S049 left it, then glides to centre
      tl.fromTo("#c1s02-sc050-grp", { x: 0, y: 0, scale: 1 }, { x: -540, y: -240, scale: 1.5, duration: 1.4, ease: C(FX.ease.inOut, 1.4), immediateRender: true }, S(287.55));
      camTo("sc050-cam", { scale: 1 }, { scale: 1.04 }, S(287.43), 9.0);
      rise("sc050-w1", T(287.59) - L);
      rise("sc050-w2", T(287.91) - L);
      tl.fromTo("#c1s02-sc050-d1 .reel-strip", { y: 0 }, { y: -150, duration: 0.6, ease: C("power3.out", 0.6), immediateRender: true }, T(289.51) - L);
      tl.fromTo("#c1s02-sc050-d2 .reel-strip", { y: 0 }, { y: -150, duration: 0.6, ease: C("power3.out", 0.6), immediateRender: true }, T(289.51) - L + 0.05);
      rise("sc050-w3", T(292.07) - L);
      const mk = $("sc050-mk"), f = FX.markupDefs(mk, "c1s02-mk50", { boil: 4 });
      FX.markup.pen(tl, mk, S(292.05), { points: [[900, 760], [930, 795], [990, 720]], color: RED, width: 7, dur: 0.3, filter: f, seed: 501 });
      FX.markup.circle(tl, mk, S(292.60), { cx: 1000, cy: 455, rx: 140, ry: 125, color: RED, width: 7, dur: 0.5, filter: f, seed: 502 });
      slideOut("050", S(296.47));
    })();

    /* ============ C1S051 · 296.47–299.83 · a very successful family (NIGHT) ============ */
    scene("051", 296.07, 299.83);
    ground("night", S(296.27));
    (function () {
      camTo("sc051-cam", { scale: 1.08 }, { scale: 1.0 }, S(296.07), 3.8, FX.ease.cam);
      pop("sc051-o1", S(296.55), { from: 0.8, dur: 1.0 });
      pop("sc051-o2", S(296.85), { from: 0.8, dur: 1.0 });
      rise("sc051-w1", T(298.55) - L);
      rise("sc051-w2", T(299.27) - L, { dur: 0.5 });
      tl.to(["#c1s02-sc051-o1", "#c1s02-sc051-o2"], { scale: 1.12, duration: 0.4, ease: FX.ease.in }, S(299.43));
    })();

    /* ============ C1S052 · 299.83–303.59 · Lewis Terman (PAPER) ============ */
    scene("052", 299.83, 303.59);
    ground("paper", S(299.83));
    (function () {
      slideIn("sc052-l", S(299.83), { x: -200, r0: -9, r: -3, dur: 1.0 });
      slideIn("sc052-b", S(300.30), { x: 300, r0: 10, r: 3, dur: 1.0 });
      rise("sc052-w1", T(299.83) - L, { dur: 0.6 });
      rise("sc052-w2", T(300.07) - L, { dur: 0.6 });
      rise("sc052-w3", T(300.39) - L);
      rise("sc052-w4", T(300.79) - L);
      rise("sc052-w5", T(301.99) - L);
      rise("sc052-w6", T(302.55) - L, { dur: 0.6 });
      // push-through into the book
      tl.fromTo("#c1s02-sc052-cam", { scale: 1 }, { scale: 2.6, duration: 0.55, ease: FX.ease.in, immediateRender: false }, S(303.04));
    })();

    /* ============ C1S053 · 303.59–306.07 · the IQ test (PAPER) ============ */
    scene("053", 303.59, 306.07);
    (function () {
      tl.fromTo("#c1s02-sc053-cam", { scale: 1.5 }, { scale: 1.0, duration: 0.7, ease: FX.ease.cam, immediateRender: true }, S(303.59));
      tl.fromTo("#c1s02-sc053-leaf", { rotationY: 0 }, { rotationY: -178, duration: 0.5, ease: C(FX.ease.inOut, 0.5), immediateRender: true }, S(304.45));
      $("sc053-hl").style.filter = "url(#c1s02-rough)";
      tl.fromTo("#c1s02-sc053-hl", { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: C("sine.inOut", 0.35), immediateRender: true }, S(305.05));
      rise("sc053-w1", T(304.39) - L, { dur: 0.7 });
      rise("sc053-w2", T(305.11) - L, { dur: 0.6 });
      rise("sc053-w3", T(305.75) - L, { dur: 0.3 });
    })();

    /* ============ C1S054 · 306.07–308.71 · on a 1950s TV (NIGHT) ============ */
    scene("054", 306.07, 308.79);
    ground("night", S(306.07));
    (function () {
      tl.fromTo("#c1s02-sc054-scr", { scaleY: 0.012, scaleX: 0.9 }, { scaleY: 1, scaleX: 1, duration: 0.22, ease: "power2.out", immediateRender: true }, S(306.12));
      tl.fromTo("#c1s02-sc054-glow", { opacity: 0.9 }, { opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: true }, S(306.18));
      camTo("sc054-cam", { scale: 1.0 }, { scale: 1.14 }, S(306.07), 2.7, FX.ease.cam);
      rise("sc054-w1", T(306.95) - L, { dur: 0.6 });
      rise("sc054-w2", T(307.11) - L, { dur: 0.6 });
      rise("sc054-w3", T(307.19) - L, { dur: 0.6 });
    })();

    /* ============ C1S055 · 308.71–313.19 · very powerful (PAPER, D15) ============ */
    whip("054", "055", S(308.79), { dir: -1 });
    scene("055", 308.79, 313.19);
    ground("paper", S(308.79));
    (function () {
      pop("sc055-c1", S(308.95), { from: 0.5, dur: 1.0 });
      pop("sc055-c2", S(309.25), { from: 0.5, dur: 1.0 });
      const mk = $("sc055-mk"), f = FX.markupDefs(mk, "c1s02-mk55", { boil: 4 });
      FX.markup.pen(tl, mk, S(309.6), { points: [[760, 470], [960, 400], [1160, 470]], color: INK, width: 5, dur: 0.7, filter: f, seed: 551 });
      FX.markup.pen(tl, mk, S(310.25), { points: [[1128, 452], [1162, 472], [1140, 506]], color: INK, width: 5, dur: 0.2, filter: f, seed: 552 });
      FX.markup.pen(tl, mk, S(309.9), { points: [[1160, 600], [960, 670], [760, 600]], color: INK, width: 5, dur: 0.7, filter: f, seed: 553 });
      FX.markup.pen(tl, mk, S(310.55), { points: [[792, 582], [758, 602], [784, 634]], color: INK, width: 5, dur: 0.2, filter: f, seed: 554 });
      // the double ring around the family (on 'powerful')
      FX.markup.circle(tl, mk, S(311.20), { cx: 960, cy: 530, rx: 560, ry: 250, rot: -3, color: RED, width: 7, dur: 0.6, filter: f, seed: 555 });
      FX.markup.circle(tl, mk, S(311.45), { cx: 960, cy: 532, rx: 590, ry: 275, rot: -2, color: RED, width: 4, dur: 0.55, filter: f, seed: 556 });
      rise("sc055-w1", T(310.95) - L);
      rise("sc055-w2", T(311.27) - L);
      camTo("sc055-cam", { scale: 1.0 }, { scale: 1.03 }, S(308.79), 3.9);
      tl.to("#c1s02-sc055-cam", { scale: 1.16, duration: 0.5, ease: FX.ease.in }, S(312.69));
    })();

    /* ============ C1S056 · 313.19–318.79 · by 24 … undergrad degree in Stanford (NIGHT, 2.5D) ============ */
    scene("056", 313.19, 318.87);
    ground("night", S(313.19));
    (function () {
      const P = 1200;
      gsap.set("#c1s02-sc056-L0", { z: -500, scale: (P + 500) / P });
      gsap.set("#c1s02-sc056-L1", { z: 0, scale: 1 });
      tl.fromTo("#c1s02-sc056-cam", { x: 60, z: -40, rotationY: 2.5 }, { x: -430, y: -20, z: 330, rotationY: -2, duration: 3.0, ease: FX.ease.cam, immediateRender: true }, S(313.19));
      tl.to("#c1s02-sc056-cam", { x: -470, z: 360, duration: 2.6, ease: "none" }, S(316.19));
      FX.focusHunt(tl, $("sc056-L1"), S(316.05), { dur: 0.8 });
      const mk = $("sc056-mk"), f = FX.markupDefs(mk, "c1s02-mk56", { boil: 4 });
      FX.markup.circle(tl, mk, S(316.9), { cx: 1779, cy: 505, rx: 70, ry: 86, color: BONE, width: 5, dur: 0.5, filter: f, seed: 561, blend: "normal" });
      tl.fromTo("#c1s02-sc056-n", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(313.43) - L);
      FX.text.count(tl, $("sc056-n"), T(313.43) - L, 0, 24, 0.8);
      rise("sc056-w1", T(316.07) - L);
      rise("sc056-w2", T(316.71) - L);
      rise("sc056-w3", T(317.91) - L, { dur: 0.5 });
    })();

    /* ============ C1S057 · 318.79–325.43 · East to MIT and back (PAPER, R10) ============ */
    flash(S(318.87));
    whip("056", "057", S(318.87), { dir: 1 });
    scene("057", 318.87, 325.43);
    ground("paper", S(318.87));
    (function () {
      const cam = $("sc057-cam");
      // Palo Alto (382,1813) → wide (whole route) → back to California + book
      gsap.set(cam, { x: 700 - 0.9 * 382, y: 620 - 0.9 * 1813, scale: 0.9 });
      tl.fromTo(cam, { x: 700 - 0.9 * 382, y: 620 - 0.9 * 1813, scale: 0.9 }, { x: 960 - 0.47 * 1900, y: 560 - 0.47 * 1600, scale: 0.47, duration: 1.6, ease: FX.ease.cam, immediateRender: false }, S(318.87));
      tl.to(cam, { x: 960 - 0.5 * 1900, y: 560 - 0.5 * 1600, scale: 0.5, duration: 2.2, ease: "none" }, S(320.47));
      tl.to(cam, { x: 520 - 0.62 * 1300, y: 560 - 0.62 * 1650, scale: 0.62, duration: 1.4, ease: FX.ease.cam }, S(322.70));
      tl.to(cam, { x: 500 - 0.64 * 1300, y: 560 - 0.64 * 1650, scale: 0.64, duration: 1.4, ease: "none" }, S(324.10));
      const svg = $("sc057-svg"), f = FX.markupDefs(svg, "c1s02-mk57", { boil: 12 });
      svg.setAttribute("viewBox", "0 0 3840 2827");
      const pts = [[382, 1813], [450, 1735], [497, 1677], [912, 1488], [1920, 1488], [2414, 1473], [2900, 1500], [3365, 1551], [3402, 1434]];
      const cr = (P, off) => { let d = `M${P[0][0]} ${P[0][1] + off}`; for (let i = 0; i < P.length - 1; i++) { const p0 = P[Math.max(0, i - 1)], p1 = P[i], p2 = P[i + 1], p3 = P[Math.min(P.length - 1, i + 2)];
        d += ` C${(p1[0] + (p2[0] - p0[0]) / 6).toFixed(1)} ${(p1[1] + (p2[1] - p0[1]) / 6 + off).toFixed(1)} ${(p2[0] - (p3[0] - p1[0]) / 6).toFixed(1)} ${(p2[1] - (p3[1] - p1[1]) / 6 + off).toFixed(1)} ${p2[0]} ${p2[1] + off}`; } return d; };
      const there = ink(svg, cr(pts, 0), S(319.30), 2.4, { color: YEL, width: 30, filter: f, blend: "multiply", ease: C(FX.ease.inOut, 2.4) });
      const back = ink(svg, cr(pts.slice().reverse(), 46), S(322.45), 1.25, { color: YEL, width: 22, filter: f, blend: "multiply", opacity: 0.85, ease: C(FX.ease.inOut, 1.25) });
      // pins: MIT navy (East), Stanford vermilion
      const pin = (x, y, c, t) => { const g = svgEl("g", { transform: `translate(${x} ${y})` }, svg); svgEl("circle", { cx: 0, cy: 0, r: 30, fill: c, stroke: BONE, "stroke-width": 6 }, g); g.style.transformBox = "fill-box"; g.style.transformOrigin = "50% 50%"; pop(g, t, { from: 0.2, dur: 0.6 }); return g; };
      pin(3402, 1434, NAVY, S(321.77));
      pin(382, 1813, RED, S(322.97));
      tl.fromTo("#c1s02-sc057-east", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: true }, T(319.35) - L);
      tl.to("#c1s02-sc057-east", { opacity: 0, duration: 0.3 }, S(321.5));
      tl.fromTo("#c1s02-sc057-mit", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: true }, T(321.83) - L);
      rise("sc057-w1", T(320.07) - L);
      out("sc057-l1", S(322.25), 0.25);
      rise("sc057-w2", T(322.47) - L);
      rise("sc057-w3", T(322.71) - L);
      tl.fromTo("#c1s02-sc057-book", { opacity: 1, x: 640, rotation: 14 }, { opacity: 1, x: 0, rotation: 4, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(323.70));
      gsap.set("#c1s02-sc057-book", { opacity: 0 });
      rise("sc057-w4", T(324.07) - L, { dur: 0.6, y: 8 });
      rise("sc057-w5", T(324.55) - L, { dur: 0.6, y: 8 });
    })();

    /* ============ C1S058 · 325.43–332.15 · first ten years … breaking his heart (GRID) ============ */
    scene("058", 325.43, 332.23);
    (function () {
      const svg = $("sc058-svg");
      ink(svg, "M260 300 L260 890 L1700 890", S(325.50), 0.8, { color: INK, width: 4 });
      tl.fromTo("#c1s02-sc058-band", { scaleX: 0 }, { scaleX: 1, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(325.95));
      // the 'staying West' line: steady, then falls through his first ten years (shapes only, no values)
      const L1 = "M260 470 C 340 455 420 480 500 462 S 600 470 640 476 C 760 500 820 560 900 600 S 1040 690 1110 720";
      const L2 = "M1110 720 C 1160 742 1210 770 1260 792 S 1400 820 1520 834";
      const p1 = ink(svg, L1, S(326.0), 3.2, { color: RED, width: 8, ease: C("sine.inOut", 3.2) });
      const g2 = svgEl("g", {}, svg);
      const p2 = ink(g2, L2, S(329.2), 1.2, { color: RED, width: 8, ease: C("sine.out", 1.2) });
      // crack on 'breaking'
      const mk = svgEl("g", {}, svg), f = FX.markupDefs(svg, "c1s02-mk58", { boil: 4 });
      svg.setAttribute("viewBox", "0 0 1920 1080");
      ink(mk, "M1090 650 L1124 690 L1098 712 L1132 744 L1106 780", S(330.85), 0.22, { color: INK, width: 5, filter: f });
      tl.fromTo(g2, { y: 0, x: 0 }, { y: 26, x: 10, duration: 0.3, ease: C(FX.ease.out, 0.3), immediateRender: false }, S(330.95));
      rise("sc058-w1", T(325.99) - L, { y: 8 });
      rise("sc058-w2", T(326.31) - L, { y: 8 });
      rise("sc058-w3", T(326.71) - L, { y: 8 });
      rise("sc058-w4", T(327.59) - L);
      rise("sc058-w5", T(328.23) - L);
      rise("sc058-w6", T(330.87) - L, { dur: 0.6 });
      rise("sc058-w7", T(331.43) - L, { dur: 0.5 });
      rise("sc058-w8", T(331.59) - L, { dur: 0.4 });
      camTo("sc058-cam", { scale: 1 }, { scale: 1.04 }, S(325.43), 6.8);
    })();

    /* ============ C1S059 · 332.15–338.47 · Hoover becomes the president (NIGHT) ============ */
    whip("058", "059", S(332.23), { dir: -1 });
    scene("059", 332.23, 338.47);
    ground("night", S(332.23));
    (function () {
      gated(332.1, 338.6, () => FX.weave($("sc059-weave"), { amp: 1.6, flicker: 0.05, seed: 591 }));
      camTo("sc059-cam", { scale: 1.0 }, { scale: 1.06 }, S(332.23), 5.75);
      tl.to("#c1s02-sc059-cam", { scale: 1.2, duration: 0.5, ease: FX.ease.in }, S(337.97));
      tl.fromTo("#c1s02-sc059-v1", { opacity: 1 }, { opacity: 0, duration: 0.001, immediateRender: false }, S(335.30));
      rise("sc059-w1", T(333.11) - L);
      rise("sc059-w2", T(337.35) - L, { dur: 0.6 });
    })();

    /* ============ C1S060 · 338.47–344.84 · the Great Depression (NIGHT) ============ */
    scene("060", 338.47, 345.30);
    (function () {
      camTo("sc060-acam", { scale: 1.15 }, { scale: 1.02 }, S(338.47), 2.4, FX.ease.cam);
      rise("sc060-w1", T(338.95) - L, { dur: 1.0 });
      rise("sc060-w2", T(339.35) - L, { dur: 1.0 });
      whipEl($("sc060-a"), $("sc060-b"), "060a", "060b", S(340.75), { dir: 1 });
      camTo("sc060-bcam", { scale: 1.0 }, { scale: 1.08 }, S(340.75), 2.7);
      rise("sc060-w3", T(341.00) - L, { dur: 0.8 });
      // "that's a different topic": the photo shrinks to a print and is flicked out of frame
      tl.to("#c1s02-sc060-bph", { scale: 0.62, rotation: -5, duration: 0.9, ease: C(FX.ease.inOut, 0.9) }, S(343.30));
      tl.to(["#c1s02-sc060-bs", "#c1s02-sc060-w3", "#c1s02-sc060-bcr"], { opacity: 0, duration: 0.3 }, S(343.30));
      tl.to("#c1s02-sc060-bph", { x: -1700, y: -120, rotation: -24, duration: 0.45, ease: C(FX.ease.in, 0.45) }, S(344.62));
    })();

    /* ============ C1S061 · 344.84–349.40 · Terman, ten years (PAPER) ============ */
    slideOver("061", S(344.84));
    scene("061", 344.84, 349.40);
    ground("paper", S(345.0));
    (function () {
      rise("sc061-w1", T(345.32) - L);
      const svg = $("sc061-mk"), f = FX.markupDefs(svg, "c1s02-mk61", { boil: 4 });
      for (let i = 0; i < 10; i++) {
        const grp = Math.floor(i / 5), k = i % 5, x0 = 1000 + grp * 330, t0 = S(347.42) + i * 0.1;
        const d = k < 4 ? `M${x0 + k * 52} 400 L${x0 + k * 52 + 4} 600` : `M${x0 - 26} 560 L${x0 + 200} 430`;
        ink(svg, d, t0, 0.09, { color: INK, width: 9, filter: f, blend: "multiply" });
      }
      rise("sc061-w2", T(347.48) - L);
      rise("sc061-w3", T(347.72) - L);
      camTo("sc061-cam", { scale: 1 }, { scale: 1.03 }, S(344.84), 4.1);
      tl.to("#c1s02-sc061-cam", { scale: 1.14, duration: 0.45, ease: FX.ease.in }, S(348.95));
    })();

    /* ============ C1S062 · 349.40–357.32 · best students go back east; STOP (PAPER, R5) ============ */
    scene("062", 349.40, 357.50);
    (function () {
      const grid = $("sc062-grid"), ic = [];
      const best = [2, 5, 9, 12, 14, 19, 22];
      for (let r = 0; r < 3; r++) for (let c = 0; c < 8; c++) {
        const i = r * 8 + c, d = document.createElement("div"); d.className = "c2-ico";
        d.style.left = (200 + c * 70) + "px"; d.style.top = (420 + r * 90) + "px";
        d.innerHTML = '<img src="assets/icons/graduate_ink.svg" alt="" /><img class="v" src="assets/icons/graduate_vermilion.svg" alt="" style="opacity:0" /><img class="n" src="assets/icons/graduate_navy.svg" alt="" style="opacity:0" />';
        grid.appendChild(d); ic.push(d);
      }
      ic.forEach((d, i) => tl.fromTo(d, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(349.45) + Math.floor(i / 3) / 12));
      best.forEach((i, k) => tl.to(ic[i].querySelector(".v"), { opacity: 1, duration: 0.001 }, S(349.72) + k / 12));
      const svg = $("sc062-svg");
      ink(svg, "M780 520 C 1000 500 1200 560 1420 620", S(352.20), 0.9, { color: INK, width: 4, opacity: 0.5 });
      best.forEach((i, k) => {
        const tx = 1440 + (k % 4) * 70 - (200 + (i % 8) * 70), ty = 640 + Math.floor(k / 4) * 80 - (420 + Math.floor(i / 8) * 90);
        tl.to(ic[i], { x: tx, y: ty, duration: 1.6, ease: C(FX.ease.inOut, 1.6) }, S(352.28) + k * 0.08);
        tl.to(ic[i].querySelector(".n"), { opacity: 1, duration: 0.001 }, S(353.6) + k * 0.08);
      });
      rise("sc062-w1", T(349.72) - L);
      rise("sc062-w2", T(350.20) - L);
      rise("sc062-w3", T(352.28) - L);
      rise("sc062-w4", T(353.72) - L);
      rise("sc062-w5", T(353.96) - L);
      tl.fromTo("#c1s02-sc062-stop", { opacity: 0, scale: 1.6, rotation: -8 }, { opacity: 1, scale: 1, rotation: -4, duration: 0.14, ease: C("power2.in", 0.14), immediateRender: true }, T(356.68) - L);
      tl.fromTo("#c1s02-sc062-cam", { x: 0 }, { x: -10, duration: 1 / 12, yoyo: true, repeat: 1, ease: "none", immediateRender: false }, S(356.78));
      camTo("sc062-cam", { scale: 1 }, { scale: 1.0 }, S(349.40), 0.01);
    })();

    /* ============ C1S063 · 357.32–361.72 · 1938 (NIGHT) ============ */
    whip("062", "063", S(357.42), { dir: 1, vertical: true });
    scene("063", 357.42, 361.72);
    ground("night", S(357.42));
    (function () {
      gated(357.3, 361.8, () => FX.streaks($("sc063-streaks"), { seed: 6301, speed: 0.5, gain: 0.85, tint: [235, 210, 180], xfreq: 0.14 }));
      camTo("sc063-cam", { scale: 1.0 }, { scale: 1.07 }, S(357.42), 4.3);
      tl.to("#c1s02-sc063-cam", { scale: 1.2, duration: 0.45, ease: FX.ease.in }, S(361.27));
      FX.text.odometer(tl, $("sc063-yr"), T(357.88) - L, { dur: 0.9, stagger: 0.05, seed: 63 });
      rise("sc063-w1", T(359.64) - L, { y: 8 });
      rise("sc063-w2", T(360.12) - L, { y: 8 });
      rise("sc063-w3", T(360.44) - L, { y: 8 });
    })();

    /* ============ C1S064 · 361.72–369.96 · two students (NIGHT, s09) ============ */
    scene("064", 361.72, 369.96);
    (function () {
      tl.fromTo("#c1s02-sc064-p1", { x: 0, rotation: -2 }, { x: 60, rotation: -2, duration: 8.3, ease: "none", immediateRender: true }, S(361.72));
      tl.fromTo("#c1s02-sc064-p2", { x: 0, rotation: 3 }, { x: -80, rotation: 3, duration: 8.3, ease: "none", immediateRender: true }, S(361.72));
      tl.fromTo("#c1s02-sc064-p3", { x: 0, rotation: -1 }, { x: 120, rotation: -1, duration: 8.3, ease: "none", immediateRender: true }, S(361.72));
      tl.fromTo("#c1s02-sc064-h", { opacity: 0, y: 120, rotation: -12 }, { opacity: 1, y: 0, rotation: -3.5, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(362.25));
      tl.fromTo("#c1s02-sc064-p", { opacity: 0, y: 120, rotation: 11 }, { opacity: 1, y: 0, rotation: 3, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(362.55));
      rise("sc064-w1", T(362.36) - L, { y: 8 });
      rise("sc064-w2", T(362.68) - L, { y: 8 });
      rise("sc064-w3", T(364.28) - L);
      rise("sc064-w4", T(364.60) - L);
      const mk = $("sc064-mk"), f = FX.markupDefs(mk, "c1s02-mk64", { boil: 4 });
      FX.markup.pen(tl, mk, S(367.30), { points: [[1610, 470], [1700, 455], [1770, 462]], color: SKY, width: 7, dur: 0.45, filter: f, seed: 641, blend: "normal" });
      FX.markup.pen(tl, mk, S(367.72), { points: [[1745, 440], [1772, 462], [1746, 486]], color: SKY, width: 7, dur: 0.15, filter: f, seed: 642, blend: "normal" });
      FX.markup.pen(tl, mk, S(367.95), { points: [[1805, 380], [1802, 470], [1808, 550]], color: BONE, width: 12, dur: 0.2, filter: f, seed: 643, blend: "normal" });
      rise("sc064-w5", T(367.96) - L, { y: 8, dur: 0.6 });
      tl.fromTo(["#c1s02-sc064-h", "#c1s02-sc064-p"], { scale: 1 }, { scale: 1.03, duration: 6.0, ease: "none", immediateRender: false }, S(363.6));
    })();

    /* ============ C1S065 · 369.96–377.16 · their names (PAPER) ============ */
    scene("065", 369.96, 377.16);
    ground("paper", S(369.96));
    (function () {
      tl.fromTo("#c1s02-sc065-t1", { x: -500, rotation: -12 }, { x: 0, rotation: -3, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(370.0));
      tl.fromTo("#c1s02-sc065-t2", { x: 600, rotation: 12 }, { x: 0, rotation: 2.5, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(370.75));
      // blinking type cursors waiting for the names (12 fps blink)
      ["#c1s02-sc065-c1", "#c1s02-sc065-c2"].forEach((c, k) => { for (let i = 0; i < 12; i++) tl.set(c, { opacity: i % 2 ? 0 : 1 }, S(371.6) + k * 0.25 + i * 0.45); tl.set(c, { opacity: 0 }, S(377.0)); });
      rise("sc065-w1", T(370.84) - L);
      rise("sc065-w2", T(371.00) - L);
      rise("sc065-w3", T(372.36) - L, { y: 8 });
      rise("sc065-w4", T(372.68) - L, { y: 8 });
      out("sc065-l2", S(375.8), 0.3);
      rise("sc065-w5", T(376.12) - L, { y: 8, dur: 0.6 });
      rise("sc065-w6", T(376.68) - L, { y: 8, dur: 0.4 });
      camTo("sc065-cam", { scale: 1 }, { scale: 1.03 }, S(369.96), 6.8);
      tl.to("#c1s02-sc065-cam", { scale: 1.16, duration: 0.45, ease: FX.ease.in }, S(376.71));
    })();

    /* ============ C1S066 · 377.16–381.08 · Bill Hewlett and David Packard (NIGHT, s09 reveal) ============ */
    scene("066", 377.16, 381.08);
    ground("night", S(377.16));
    (function () {
      tl.fromTo("#c1s02-sc066-p1", { x: 0, rotation: -2 }, { x: 40, rotation: -2, duration: 4.0, ease: "none", immediateRender: true }, S(377.16));
      tl.fromTo("#c1s02-sc066-p2", { x: 0, rotation: 3 }, { x: -50, rotation: 3, duration: 4.0, ease: "none", immediateRender: true }, S(377.16));
      tl.fromTo("#c1s02-sc066-p3", { x: 0, rotation: -1 }, { x: 70, rotation: -1, duration: 4.0, ease: "none", immediateRender: true }, S(377.16));
      tl.fromTo(["#c1s02-sc066-h", "#c1s02-sc066-p"], { scale: 1.06 }, { scale: 1.0, duration: 1.2, ease: FX.ease.cam, immediateRender: true }, S(377.16));
      tl.fromTo("#c1s02-sc066-hs", { opacity: 0.94 }, { opacity: 0, duration: 0.5, ease: C("power2.out", 0.5), immediateRender: true }, T(378.28) - L);
      tl.fromTo("#c1s02-sc066-ps", { opacity: 0.94 }, { opacity: 0, duration: 0.5, ease: C("power2.out", 0.5), immediateRender: true }, T(379.48) - L);
      rise("sc066-w1", T(378.28) - L, { dur: 0.5, y: 8 });
      rise("sc066-w2", T(378.60) - L, { dur: 0.7 });
      rise("sc066-w3", T(379.48) - L, { dur: 0.5, y: 8 });
      rise("sc066-w4", T(379.96) - L, { dur: 0.7 });
    })();

    /* ============ C1S067 · 381.08–385.64 · the famous company HP (PAPER) ============ */
    scene("067", 381.08, 385.72);
    ground("paper", S(381.08));
    (function () {
      const hn = FX.split($("sc067-hn"), "chars"), pn = FX.split($("sc067-pn"), "chars");
      tl.fromTo("#c1s02-sc067-hn", { x: 0, y: 0 }, { x: 60, y: -380, duration: 1.3, ease: C(FX.ease.inOut, 1.3), immediateRender: true }, S(381.25));
      tl.fromTo("#c1s02-sc067-pn", { x: 0, y: 0 }, { x: -60, y: -380, duration: 1.3, ease: C(FX.ease.inOut, 1.3), immediateRender: true }, S(381.35));
      // every letter but H and P drops away (12 fps), then H + P meet
      hn.slice(1).concat(pn.slice(1)).forEach((c, i) => tl.to(c, { y: 140, opacity: 0, duration: 0.4, ease: C(FX.ease.in, 0.4) }, S(383.40) + (i % 6) / 24));
      tl.to(hn[0], { x: 470, duration: 0.5, ease: C(FX.ease.inOut, 0.5) }, S(383.70));
      tl.to(pn[0], { x: -320, duration: 0.5, ease: C(FX.ease.inOut, 0.5) }, S(383.70));
      tl.to([hn[0], pn[0]], { opacity: 0, duration: 0.001 }, T(384.20) - L);
      tl.fromTo("#c1s02-sc067-hp", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: true }, T(384.20) - L);
      rise("sc067-w1", T(382.60) - L);
      rise("sc067-w2", T(383.16) - L, { y: 8 });
      rise("sc067-w3", T(383.64) - L, { y: 8 });
      camTo("sc067-cam", { scale: 1 }, { scale: 1.03 }, S(381.08), 4.6);
    })();

    /* ============ C1S068 · 385.64–390.52 · Packard at General Electric (NIGHT) ============ */
    whip("067", "068", S(385.72), { dir: -1 });
    scene("068", 385.72, 390.52);
    ground("night", S(385.72));
    (function () {
      camTo("sc068-cam", { scale: 1.0 }, { scale: 1.06 }, S(385.72), 4.8);
      tl.fromTo("#c1s02-sc068-pk", { opacity: 1, x: 500, rotation: 14 }, { opacity: 1, x: 0, rotation: 3, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(386.70));
      gsap.set("#c1s02-sc068-pk", { opacity: 0 });
      rise("sc068-w1", T(386.92) - L, { y: 8 });
      rise("sc068-w2", T(387.80) - L);
      rise("sc068-w3", T(388.12) - L);
      rise("sc068-w4", T(389.24) - L);
      rise("sc068-w5", T(389.72) - L, { dur: 0.6 });
      pop("sc068-logo", S(389.20), { from: 0.7, dur: 0.8 });
      tl.to(["#c1s02-sc068-cam", "#c1s02-sc068-pk"], { scale: 1.14, duration: 0.45, ease: FX.ease.in }, S(390.07));
    })();

    /* ============ C1S069 · 390.52–395.56 · $100 a month; Hewlett going (PAPER) ============ */
    scene("069", 390.52, 395.60);
    ground("paper", S(390.52));
    (function () {
      tl.fromTo("#c1s02-sc069-env", { y: 260, rotation: -9 }, { y: 0, rotation: -2, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(390.52));
      tl.fromTo("#c1s02-sc069-amt", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(391.16) - L);
      FX.text.count(tl, $("sc069-n"), T(391.16) - L, 0, 100, 0.7, (v) => "$" + Math.round(v));
      rise("sc069-w1", T(391.96) - L);
      rise("sc069-w2", T(392.20) - L);
      tl.fromTo("#c1s02-sc069-h", { opacity: 1, x: 500, rotation: 14 }, { opacity: 1, x: 0, rotation: 3, duration: 0.9, ease: C(FX.ease.out, 0.9), immediateRender: true }, S(393.05));
      gsap.set("#c1s02-sc069-h", { opacity: 0 });
      rise("sc069-w3", T(393.24) - L);
      tl.fromTo("#c1s02-sc069-ticket", { opacity: 1, x: 300, y: 80, rotation: 6 }, { opacity: 1, x: 0, y: 0, rotation: -7, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(394.25));
      gsap.set("#c1s02-sc069-ticket", { opacity: 0 });
      rise("sc069-w4", T(395.08) - L, { dur: 0.5 });
      camTo("sc069-cam", { scale: 1 }, { scale: 1.03 }, S(390.52), 5.0);
      slideOut("069", S(395.60));
    })();

    /* ============ C1S070 · 395.56–402.83 · Terman's plan — cork board (NIGHT, R9) ============ */
    scene("070", 395.18, 402.83);
    ground("night", S(395.40));
    (function () {
      // slow push, still moving at 402.83 (cut on action into c1s03's map push)
      tl.fromTo("#c1s02-sc070-cam", { scale: 1.0 }, { scale: 1.09, duration: 7.7, ease: "none", immediateRender: true }, S(395.18));
      tl.fromTo("#c1s02-sc070-lamp", { opacity: 0.6 }, { opacity: 1, duration: 1 / 24, immediateRender: true }, S(395.60));
      rise("sc070-w1", T(396.28) - L, { y: 6, dur: 0.6 });
      rise("sc070-w2", T(397.88) - L);
      out("sc070-w2", S(399.6), 0.3);
      rise("sc070-w3", T(399.95) - L);
      out("sc070-w3", S(401.05), 0.3);
      rise("sc070-w4", T(401.39) - L);
      tl.fromTo("#c1s02-sc070-q", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(398.9));
      rise("sc070-w5", T(402.35) - L, { dur: 0.35, y: 6 });
      // red string (vermilion), sagging, drawn pin to pin
      const svg = $("sc070-svg");
      const str = (x1, y1, x2, y2, t, d) => { const mx = (x1 + x2) / 2, my = Math.max(y1, y2) + 60; ink(svg, `M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}`, t, d, { color: RED, width: 4 }); };
      str(930, 123, 560, 531, S(399.95), 0.55);
      str(930, 123, 1040, 611, S(400.25), 0.5);
      str(560, 531, 1550, 341, S(401.39), 0.5);
      str(1040, 611, 1550, 341, S(401.62), 0.5);
    })();

    // ---------- scenes start display:none (after odometers measured their reels) ----------
    scenes.forEach(([el, a]) => { if (S(a) > 0) gsap.set(el, { display: "none" }); });

    FX.mount(tl, DURATION);
    window.__timelines = window.__timelines || {};
    window.__timelines[SEG] = tl;
  })();
