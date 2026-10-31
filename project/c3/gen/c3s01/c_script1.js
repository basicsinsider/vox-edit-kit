  <script>
  (function () {
    const SEG = "c3s01", SEG_START = 0.00, SEG_END = 200.34, DURATION = +(SEG_END - SEG_START).toFixed(2);
    const T = (s) => +(s - 0.00).toFixed(3);   // TEXT cues (audited) — literal word start; text lands L earlier
    const S = (s) => +(s - 0.00).toFixed(3);   // STRUCTURAL cues (cuts, camera, objects)
    const L = 0.06;
    const tl = gsap.timeline({ paused: true });
    const $ = (id) => document.getElementById(SEG + "-" + id);
    const NS = "http://www.w3.org/2000/svg";
    const defs = $("defs");
    const E = FX.ease;
    const C = (e, d) => FX.choppy(e, d, 12);
    const BONE = "#f2ede3", INK = "#141b24", RED = "#e03f2c", CEL = "#9fc7b2", YEL = "#f2d33b", NAVY = "#1d5c9e";
    const US = __US__;
    const TW = __TW__;

    // ---------- shared filters ----------
    FX.tintDefs(defs, "c3s01-tink", "#1b2028", "#ece4d2");
    FX.tintDefs(defs, "c3s01-tnavy", "#10304f", "#e9eef0");
    FX.tintDefs(defs, "c3s01-tsep", "#1f1a14", "#d9c9a8");
    FX.tintDefs(defs, "c3s01-tcel", "#1c2a24", "#dcefe4");
    const PEN = FX.markupDefs(defs, "c3s01-pen", { boil: 4 });
    const MRK = FX.markupDefs(defs, "c3s01-mrk", { boil: 12 });
    defs.removeAttribute("viewBox");
    FX.roughDefs(defs, "c3s01-rough", { freq: 0.04, scale: 6 });
    FX.roughDefs(defs, "c3s01-rhl", { freq: 0.05, scale: 7 });
    const ch007 = FX.roughDefs(defs, "c3s01-ch007", { freq: 0.035, scale: 8, choke: 0 });
    const ch017 = FX.roughDefs(defs, "c3s01-ch017", { freq: 0.03, scale: 9, choke: 0 });

    // ---------- helpers ----------
    function gated(a, b, fn) { const on = FX.onFrame; FX.onFrame = (f) => on(FX.gate(S(a) - 0.1, S(b) + 0.1, f)); try { return fn(); } finally { FX.onFrame = on; } }
    const inited = {};
    // scene window: hidden (display none) outside [a, b]; may be called twice for a second window
    function scene(id, a, b) {
      const el = $(id);
      if (!inited[id]) { gsap.set(el, { autoAlpha: 0, display: "none" }); inited[id] = 1; }
      if (S(a) <= 0) gsap.set(el, { autoAlpha: 1, display: "block" });
      else tl.fromTo(el, { autoAlpha: 0, display: "none" }, { autoAlpha: 1, display: "block", duration: 0.001, immediateRender: false }, S(a));
      if (b < SEG_END) tl.set(el, { autoAlpha: 0, display: "none" }, S(b));
    }
    function ground(kind, t) {
      const v = kind === "paper" ? [0.32, 0.14, 0.26] : [1, 0.42, 0.36];
      tl.set([$("vig"), $("dust"), $("grain")], { opacity: (i) => v[i] }, t);
    }
    const show = (el, t) => tl.fromTo(typeof el === "string" ? $(el) : el, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t);
    const rise = (el, t, o) => { o = o || {}; const d = o.dur || 1.0; if (typeof el === "string") el = $(el);
      tl.fromTo(el, { opacity: 0, y: o.y == null ? 22 : o.y }, { opacity: 1, y: 0, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const pop = (el, t, d, from) => { d = d || 0.8; if (typeof el === "string") el = $(el);
      tl.fromTo(el, { opacity: 0, scale: from || 0.8 }, { opacity: 1, scale: 1, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const out = (el, t, d) => { if (typeof el === "string") el = $(el); tl.to(el, { opacity: 0, duration: d || 0.3, ease: C(E.in, d || 0.3) }, t); };
    const words = (id) => $(id).querySelectorAll(".q-w");
    // word-by-word: times are literal T(word) − L (audited)
    function wr(id, times, o) { const ws = words(id); times.forEach((t, i) => rise(ws[i], t, Object.assign({ dur: 0.7, y: 14 }, o || {}))); }
    const whipN = { n: 0 };
    function whip(a, b, t, o) {
      o = Object.assign({ dir: 1, vertical: false, flash: false, dur: 0.32 }, o);
      a = $(a); b = $(b);
      const k = ++whipN.n, ba = FX.whipDefs(defs, `${SEG}-wa${k}`), bb = FX.whipDefs(defs, `${SEG}-wb${k}`), h = o.dur / 2;
      tl.set(a, { filter: `url(#${SEG}-wa${k})` }, t - h - 0.01); tl.set(a, { filter: "none" }, t + 0.06);
      tl.set(b, { filter: `url(#${SEG}-wb${k})` }, t - 0.001); tl.set(b, { filter: "none" }, t + h + 0.02);
      FX.whip(tl, a, b, t, { dir: o.dir, vertical: o.vertical, dur: o.dur, blurA: ba, blurB: bb });
      if (o.flash) tl.fromTo($("flash"), { opacity: 0 }, { opacity: 0.85, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.in", immediateRender: false }, t - 0.08);
    }
    // paper slide: incoming scene slides over the outgoing one (PS)
    function slideIn(b, t, o) { o = Object.assign({ from: "bottom", dur: 0.5 }, o); const p = o.from === "bottom" ? { y: 1100 } : o.from === "right" ? { x: 1960 } : { x: -1960 };
      tl.fromTo($(b), p, { x: 0, y: 0, duration: o.dur, ease: C(E.out, o.dur), immediateRender: false }, t); }
    function ink(parent, d, t, dur, o) {
      o = o || {};
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d); p.setAttribute("fill", o.fill || "none");
      p.setAttribute("stroke", o.color || INK); p.setAttribute("stroke-width", o.width || 6);
      p.setAttribute("stroke-linecap", "round"); p.setAttribute("stroke-linejoin", "round");
      if (o.filter) p.setAttribute("filter", o.filter);
      if (o.opacity) p.setAttribute("opacity", o.opacity);
      if (o.blend) p.style.mixBlendMode = o.blend;
      parent.appendChild(p);
      const len = p.getTotalLength() || 1;
      p.setAttribute("stroke-dasharray", `${len} ${len}`); p.setAttribute("stroke-dashoffset", len);
      tl.fromTo(p, { attr: { "stroke-dashoffset": len } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: o.ease || C(E.out, dur), immediateRender: true }, t);
      p._len = len; return p;
    }
    function el(tag, attrs, parent) { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
    function div(parent, css, cls, html) { const d = document.createElement("div"); if (cls) d.className = cls; d.style.cssText = css; if (html) d.innerHTML = html; parent.appendChild(d); return d; }
    // numbers of a path "M..L..Z" → bbox
    function bbox(d) { const n = d.match(/-?\d+\.?\d*/g).map(Number); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      for (let i = 0; i < n.length - 1; i += 2) { x0 = Math.min(x0, n[i]); x1 = Math.max(x1, n[i]); y0 = Math.min(y0, n[i + 1]); y1 = Math.max(y1, n[i + 1]); }
      return { x0, y0, x1, y1, cx: (x0 + x1) / 2, cy: (y0 + y1) / 2, w: x1 - x0, h: y1 - y0 }; }
    // camera framing for a map plane with transform-origin 0 0: put map point (px,py) at screen (sx,sy) at scale s
    const frame = (px, py, s, sx, sy) => ({ x: (sx == null ? 960 : sx) - px * s, y: (sy == null ? 540 : sy) - py * s, scale: s });

    // ---------- global textures ----------
    FX.grain($("grain"), 301);
    FX.dust($("dust"), 302, 2);
    gsap.set([$("vig"), $("dust"), $("grain")], { opacity: (i) => [1, 0.42, 0.36][i] });

    /* ============ C3S001 · 0.00–2.32 · "how big it was" ============ */
    scene("sc001", 0, 2.32);
    gsap.set($("sc001-cam"), { scale: 1.6 });
    tl.fromTo($("sc001-cam"), { scale: 1.6 }, { scale: 1.0, duration: 2.32, ease: E.cam, immediateRender: false }, 0);
    wr("sc001-t", [T(1.52) - L, T(1.68) - L], { dur: 0.3 });
    tl.fromTo($("sc001-big"), { scale: 1.0 }, { scale: 1.15, duration: 0.3, ease: C(E.out, 0.3), transformOrigin: "0% 80%", immediateRender: false }, S(1.62));

    /* ============ C3S002 · 2.32–7.04 · IC → the world (cutting the curve) ============ */
    scene("sc002", 2.32, 7.04);
    FX.curveCut(tl, $("sc002-wrap"), $("sc002-a"), $("sc002-b"), S(2.32), 5.16, { from: 1, to: 2.6 });   // cut at 4.90 (peak velocity)
    gsap.set($("sc002-globe"), { scale: 0.62 });
    tl.fromTo($("sc002-globe"), { scale: 0.62, rotation: 0 }, { scale: 0.62, rotation: -3, duration: 2.2, ease: "none", immediateRender: false }, S(4.9));
    FX.focusHunt(tl, $("sc002-globe"), S(5.6), { dur: 0.8 });
    wr("sc002-ic", [T(4.56) - L], { dur: 0.3, y: 0 });
    out("sc002-ic", S(5.15), 0.3);
    wr("sc002-world", [T(5.28) - L, T(5.44) - L], { dur: 0.8 });

    /* ============ C3S003 · 7.04–10.08 · the podcast on an IBM 5154 ============ */
    scene("sc003", 7.04, 10.10);
    ground("night", S(7.04));
    (function () {
      tl.fromTo($("sc003-mon"), { x: 380 }, { x: 0, duration: 0.8, ease: E.cam, immediateRender: false }, S(7.04));
      // CRT power-on
      tl.fromTo($("sc003-scr"), { scaleY: 0.012, filter: "brightness(3)" }, { scaleY: 1, filter: "brightness(1)", duration: 0.25, ease: "power2.out", immediateRender: true }, S(7.10));
      // waveform bars (12 fps shimmer)
      const w = $("sc003-wave"), bars = [], r = FX.rng(301);
      for (let i = 0; i < 70; i++) { const h = 20 + r() * 150; bars.push(el("rect", { x: i * 12, y: 100 - h / 2, width: 7, height: h, fill: "#9fc3e3", opacity: 0.85 }, w)); }
      gated(7.0, 10.1, () => FX.onFrame((t) => { const f = Math.floor(t * 12); bars.forEach((b, i) => { const h = 16 + FX.noise2(i * 0.35, f * 0.4, 7) * 170; b.setAttribute("height", h.toFixed(0)); b.setAttribute("y", (100 - h / 2).toFixed(0)); }); }));
      tl.fromTo($("sc003-bar"), { scaleX: 0.06 }, { scaleX: 0.095, duration: 3, ease: "none", immediateRender: false }, S(7.1));
      const tc = $("sc003-tc"), st = { v: 1476 };
      tl.fromTo(st, { v: 1476 }, { v: 1479, duration: 3, ease: "none", immediateRender: false, onUpdate: () => { const v = Math.floor(st.v); tc.textContent = `0:${String(Math.floor(v / 60)).padStart(2, "0")}:${String(v % 60).padStart(2, "0")}`; } }, S(7.1));
      wr("sc003-pod", [T(7.04) - L, T(7.36) - L], { dur: 0.6 });
      rise("sc003-lives", T(9.44) - L, { dur: 0.4 });
      tl.fromTo($("sc003-cam"), { scale: 1 }, { scale: 1.06, duration: 2.5, ease: "none", immediateRender: false }, S(7.1));
      // push-through into the screen; its glow fills the frame
      tl.to($("sc003-cam"), { scale: 4.2, duration: 0.48, ease: E.in }, S(9.6));
      tl.fromTo($("sc003-glow"), { opacity: 0 }, { opacity: 1, duration: 0.42, ease: "power2.in", immediateRender: false }, S(9.66));
    })();

    /* ============ C3S004 · 10.08–15.68 · video cards → Silicon Valley ============ */
    scene("sc004", 10.08, 16.5);
    ground("paper", S(10.08));
    (function () {
      const box = $("sc004-cards"), cards = [];
      for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) {
        const v = div(box, `left:${210 + c * 520}px;top:${160 + r * 270}px;opacity:0`, "q-vc",
          `<div class="f"></div><div class="d"></div><svg viewBox="0 0 400 236"><path d="M178 84 L228 116 L178 148Z" fill="${INK}"/><rect x="34" y="196" width="332" height="8" fill="rgba(20,27,36,0.25)"/><rect x="34" y="196" width="${60 + ((r * 3 + c) * 37) % 240}" height="8" fill="${INK}"/></svg>`);
        cards.push(v);
      }
      // the paper flash from the screen fades into the paper ground
      tl.fromTo($("sc004"), { filter: "brightness(1.25)" }, { filter: "brightness(1)", duration: 0.4, ease: "power2.out", immediateRender: false }, S(10.08));
      cards.forEach((v, i) => tl.fromTo(v, { opacity: 0, scale: 1.12, rotation: (i % 3 - 1) * 2 }, { opacity: 1, scale: 1, rotation: (i % 2 ? 1 : -1) * 0.8, duration: 0.25, ease: C(E.out, 0.25), immediateRender: true }, S(10.58) + i / 12));
      rise("sc004-vid", T(10.64) - L);
      // "wouldn't exist": the cards empty out to dashed outlines
      cards.forEach((v, i) => { tl.to(v.querySelector(".f"), { opacity: 0, duration: 0.25, ease: C(E.in, 0.25) }, S(13.66) + (i % 3) / 12); tl.to(v.querySelector("svg"), { opacity: 0, duration: 0.25 }, S(13.66) + (i % 3) / 12); tl.fromTo(v.querySelector(".d"), { opacity: 0 }, { opacity: 1, duration: 0.25, immediateRender: false }, S(13.66) + (i % 3) / 12); });
      wr("sc004-ex", [T(13.68) - L, T(14.08) - L], { dur: 0.4 });
      // pen strike through "exist"
      const mk = $("sc004-mk");
      FX.markup.pen(tl, mk, S(14.22), { points: [[968, 1014], [1132, 1006]], dur: 0.3, width: 6, color: INK, filter: PEN });
      // the paper splits and slides apart: Silicon Valley underneath
      tl.to([$("sc004-L"), ...cards.filter((_, i) => i % 3 === 0)], { x: -980, duration: 0.6, ease: C(E.inOut, 0.6) }, S(14.66));
      tl.to([$("sc004-R"), ...cards.filter((_, i) => i % 3 === 2)], { x: 980, duration: 0.6, ease: C(E.inOut, 0.6) }, S(14.66));
      tl.to(cards.filter((_, i) => i % 3 === 1), { y: -1100, duration: 0.6, ease: C(E.inOut, 0.6) }, S(14.66));
      tl.to([$("sc004-vid"), $("sc004-ex"), mk], { opacity: 0, duration: 0.25 }, S(14.62));
      tl.fromTo($("sc004-cam"), { scale: 1.0 }, { scale: 1.08, duration: 2.0, ease: "none", immediateRender: false }, S(14.66));
      show("sc004-svb", T(14.72) - L);
      wr("sc004-sv", [T(14.72) - L, T(15.28) - L], { dur: 0.35, y: 10 });
    })();

    /* ============ C3S005 · 15.68–21.43 · periodic chart, Si circled ============ */
    scene("sc005", 15.68, 21.48);
    slideIn("sc005", S(15.68), { dur: 0.7 });
    (function () {
      const P = [["H", 1, 1], ["He", 18, 2]];
      const rows = [
        [[1, "Li"], [2, "Be"], [13, "B"], [14, "C"], [15, "N"], [16, "O"], [17, "F"], [18, "Ne"]],
        [[1, "Na"], [2, "Mg"], [13, "Al"], [14, "Si"], [15, "P"], [16, "S"], [17, "Cl"], [18, "Ar"]],
        "K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr".split(" ").map((s, i) => [i + 1, s]),
        "Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe".split(" ").map((s, i) => [i + 1, s]),
        "Cs Ba La Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn".split(" ").map((s, i) => [i + 1, s]),
        [[1, "Fr"], [2, "Ra"], [3, "Ac"]],
      ];
      const grid = $("sc005-grid"), cells = []; let si = null;
      const put = (col, row, sym, z) => { const c = div(grid, `left:${(col - 1) * 88.6}px;top:${row * 104}px`, "q-cell", `<span class="n t-label">${z}</span><span class="s t-serif">${sym}</span>`); cells.push(c); if (sym === "Si") si = c; };
      put(1, 0, "H", 1); put(18, 0, "He", 2);
      let z = 3;
      rows.forEach((r, ri) => r.forEach(([col, sym]) => { if (ri === 4 && sym === "Hf") z = 72; put(col, ri + 1, sym, z++); }));
      si.style.borderWidth = "3px";
      // video card from C3S004 shrinks into the corner on "enjoyed my videos"
      $("sc005-card").innerHTML = `<div class="f"></div><svg viewBox="0 0 400 236"><path d="M178 84 L228 116 L178 148Z" fill="${INK}"/><rect x="34" y="196" width="332" height="8" fill="rgba(20,27,36,0.25)"/><rect x="34" y="196" width="140" height="8" fill="${INK}"/></svg>`;
      tl.fromTo($("sc005-card"), { opacity: 0, scale: 1.4, x: -500, y: -300 }, { opacity: 1, scale: 0.6, x: 0, y: 0, duration: 1.0, ease: C(E.inOut, 1.0), immediateRender: true }, S(18.01));
      rise("sc005-enj", T(18.07) - L, { dur: 0.8 });
      out("sc005-card", S(19.6), 0.3); out("sc005-enj", S(19.6), 0.3);
      // camera push to Si (cam ease), then pen circle + text call-out
      tl.fromTo($("sc005-cam"), { scale: 1, x: 0, y: 0 }, { scale: 1.6, x: -260, y: -10, duration: 1.7, ease: E.cam, immediateRender: false }, S(18.5));
      tl.to(cells.filter((c) => c !== si), { opacity: 0.22, duration: 0.6, ease: C(E.out, 0.6) }, S(20.2));
      FX.markup.pen(tl, $("sc005-mk"), S(20.17), { points: [[1236, 330], [1306, 338], [1318, 410], [1262, 464], [1192, 440], [1184, 360], [1242, 322]], dur: 0.6, width: 7, color: INK, filter: PEN });
      FX.focusHunt(tl, $("sc005-cam"), S(20.8), { dur: 0.5, a: 3, b: 4 });
      wr("sc005-si", [T(20.23) - L], { dur: 0.5 });
      wr("sc005-th", [T(20.95) - L, T(21.11) - L], { dur: 0.3 });
    })();

    /* ============ C3S006 · 21.43–26.47 · IC → Silicon Valley ============ */
    whip("sc005", "sc006", S(21.37), { vertical: true, dir: -1 });
    scene("sc006", 21.37, 26.95);
    ground("night", S(21.37));
    (function () {
      tl.fromTo($("sc006-cam"), { scale: 1.0 }, { scale: 2.4, duration: 3.2, ease: E.cam, immediateRender: false }, S(21.45));
      // die → street grid: match-dissolve into the aerial, which keeps settling
      tl.fromTo($("sc006-aer"), { opacity: 0, scale: 1.35 }, { opacity: 1, scale: 1.35, duration: 0.4, ease: "none", immediateRender: false }, S(24.45));
      tl.to($("sc006-aer"), { scale: 1.0, duration: 1.9, ease: E.cam }, S(24.5));
      show(words("sc006-ic")[0], T(21.59) - L);
      wr("sc006-int", [T(22.47) - L, T(23.03) - L], { dur: 0.7 });
      out("sc006-ic", S(24.4), 0.3); out("sc006-int", S(24.4), 0.3);
      rise("sc006-sv", T(25.51) - L, { dur: 0.45, y: 16 });
    })();

    /* ============ C3S007 · 26.47–32.63 · legal pad ============ */
    scene("sc007", 26.32, 32.63);
    slideIn("sc007", S(26.32), { dur: 0.5 });
    ground("paper", S(26.4));
    (function () {
      const ws = words("sc007-arg");
      show(ws[0], T(26.79) - L); show(ws[1], T(27.27) - L);
      FX.chokeSettle(tl, ch007, $("sc007-arg"), T(26.79) - L, 7, 1.0, "none");
      wr("sc007-deb", [T(29.35) - L], { dur: 0.8 });
      const mk = $("sc007-mk");
      FX.markup.pen(tl, mk, S(29.6), { points: [[226, 600], [560, 594]], dur: 0.45, width: 5, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(30.0), { points: [[232, 616], [548, 612]], dur: 0.4, width: 4, color: INK, filter: PEN, seed: 7 });
      wr("sc007-agr", [T(31.59) - L, T(31.75) - L], { dur: 0.6 });
      FX.markup.pen(tl, mk, S(31.75), { points: [[620, 760], [650, 800], [720, 690]], dur: 0.35, width: 9, color: RED, filter: PEN, jitter: 2 });
      tl.fromTo($("sc007-cam"), { y: 0 }, { y: -30, duration: 5.6, ease: "none", immediateRender: false }, S(26.5));
      tl.to($("sc007-cam"), { y: -240, duration: 0.3, ease: E.in }, S(32.36));   // tilt continues into the map push (cut on action)
    })();

    /* ============ C3S008 · 32.63–37.19 · California law (contrast call-out) ============ */
    scene("sc008", 32.63, 37.3);
    ground("night", S(32.63));
    const CA = US.california, caB = bbox(CA);
    const F_US = frame(3196, 1762, 0.30), F_CA = frame(caB.cx, caB.cy, 0.66, 470, 560);
    (function () {
      const svg = $("sc008-svg");
      const fill = el("path", { d: CA, fill: RED, "fill-opacity": 0.6, opacity: 0 }, svg); fill.style.mixBlendMode = "overlay";
      el("path", { d: CA, fill: "none", stroke: BONE, "stroke-width": 4, opacity: 0.0, id: "c3s01-sc008-caline" }, svg);
      gsap.set($("sc008-cam"), F_US);
      tl.fromTo($("sc008-cam"), F_US, Object.assign({ duration: 3.1, ease: E.cam, immediateRender: false }, F_CA), S(33.5));
      // contrast call-out: hard cut at the push's peak velocity (35.11)
      FX.contrastCallout(tl, $("sc008-veil"), S(35.05), { w: 6392, h: 3524, d: CA, feather: 22, color: "rgba(96,100,106,1)", strength: 0.62 });
      tl.set(fill, { opacity: 1 }, S(35.05));
      tl.set($("sc008-caline"), { opacity: 0.7 }, S(35.05));
      FX.focusHunt(tl, $("sc008-map"), S(35.6), { dur: 0.8 });
      wr("sc008-t", [T(35.11) - L, T(35.83) - L], { dur: 0.6 });
    })();

    /* ============ C3S009 · 37.19–42.55 · vintage atlas: every state the same, CA the exception ============ */
    whip("sc008", "sc009", S(37.13), { dir: -1 });
    scene("sc009", 37.13, 43.0);
    ground("paper", S(37.13));
    (function () {
      const svg = $("sc009-svg");
      svg.insertAdjacentHTML("afterbegin", `<defs><pattern id="c3s01-hatch" width="34" height="34" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="34" height="34" fill="rgba(20,27,36,0.10)"/><line x1="0" y1="0" x2="0" y2="34" stroke="${INK}" stroke-width="9"/></pattern></defs>`);
      const st = Object.keys(US).filter((k) => k !== "california").map((k) => ({ k, b: bbox(US[k]) })).sort((a, b) => a.b.cx - b.b.cx);
      st.forEach((s, i) => {
        const p = el("path", { d: US[s.k], fill: "url(#c3s01-hatch)", stroke: INK, "stroke-width": 5, opacity: 0 }, svg);
        tl.fromTo(p, { opacity: 0 }, { opacity: 0.55, duration: 0.001, immediateRender: true }, S(40.95) + Math.floor((i / st.length) * 10) / 12);
      });
      const ca = el("path", { d: CA, fill: RED, "fill-opacity": 0.8, stroke: RED, "stroke-width": 8, filter: "url(#c3s01-rough)", opacity: 0 }, svg);
      ca.style.mixBlendMode = "multiply";
      tl.fromTo(ca, { opacity: 0 }, { opacity: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(37.6));
      tl.fromTo($("sc009-cam"), { scale: 1.15 }, { scale: 1.0, duration: 5.3, ease: E.cam, immediateRender: false }, S(37.19));
      rise("sc009-ex", T(38.79) - L);
      rise("sc009-us", T(41.43) - L, { dur: 0.6 });
    })();

    /* ============ C3S010 · 42.55–46.71 · non-compete struck out ============ */
    scene("sc010", 42.40, 47.05);
    slideIn("sc010", S(42.40), { dur: 0.5 });
    (function () {
      const body = $("sc010-body");
      [[180, "1."], [330, "2."], [480, "3."]].forEach(([y, n]) => {
        div(body, `left:110px;top:${y}px;font-size:34px;color:var(--ink);font-weight:700`, "q-abs t-serif", n);
        [0, 1, 2].forEach((k) => div(body, `left:${k ? 110 : 160}px;top:${y + 16 + k * 44}px;width:${k === 2 ? 640 : 1040 - (k ? 0 : 50)}px;height:12px;background:rgba(20,27,36,0.32);border-radius:3px`, "q-abs"));
      });
      [0, 1, 2].forEach((k) => div($("sc010-doc"), `left:110px;top:${716 + k * 44}px;width:${k === 2 ? 700 : 1040}px;height:12px;background:rgba(20,27,36,0.4);border-radius:3px`, "q-abs"));
      [880, 924, 968].forEach((y, k) => div(body, `left:110px;top:${y}px;width:${k === 2 ? 520 : 1040}px;height:12px;background:rgba(20,27,36,0.32);border-radius:3px`, "q-abs"));
      wr("sc010-ce", [T(43.43) - L, T(44.23) - L], { dur: 0.6 });
      // text call-out: everything dims, the frame punches in on clause 4
      tl.to($("sc010-dim"), { opacity: 0.25, duration: 0.9, ease: E.out }, S(44.6));
      tl.fromTo($("sc010-cam"), { scale: 1 }, { scale: 1.1, duration: 1.1, ease: E.cam, immediateRender: false }, S(44.6));
      tl.fromTo($("sc010-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: C("sine.inOut", 0.35), immediateRender: true }, S(44.81));
      const mk = $("sc010-mk");
      FX.markup.pen(tl, mk, S(45.62), { points: [[100, 700], [1160, 820]], dur: 0.22, width: 8, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(45.86), { points: [[1150, 696], [110, 826]], dur: 0.22, width: 8, color: INK, filter: PEN, seed: 9 });
      pop("sc010-ca", T(46.07) - L, 0.3, 0.9);
      tl.to($("sc010"), { x: -1960, duration: 0.45, ease: C(E.in, 0.45) }, S(46.58));
    })();

    /* ============ C3S011 · 46.71–50.55 · most important states enforce ============ */
    scene("sc011", 46.58, 50.6);
    slideIn("sc011", S(46.58), { from: "right", dur: 0.45 });
    ground("night", S(46.7));
    (function () {
      const svg = $("sc011-svg");
      const ca = el("path", { d: CA, fill: RED, "fill-opacity": 0.6 }, svg); ca.style.mixBlendMode = "overlay";
      gsap.set($("sc011-cam"), F_CA);
      tl.fromTo($("sc011-cam"), F_CA, Object.assign({ duration: 1.8, ease: E.cam, immediateRender: false }, frame(3196, 1700, 0.30)), S(46.9));
      tl.to(ca, { attr: { "fill-opacity": 0.18 }, duration: 0.6, ease: C(E.out, 0.6) }, S(47.5));
      rise("sc011-out", T(47.51) - L, { dur: 0.8 });
      ["new_york", "massachusetts", "texas", "illinois", "new_jersey"].forEach((k, i) => {
        const b = bbox(US[k]);
        const p = el("path", { d: US[k], fill: "rgba(242,237,227,0.16)", stroke: BONE, "stroke-width": 16, opacity: 0 }, svg);
        p.style.filter = "drop-shadow(0 0 18px rgba(242,237,227,0.7))";
        const g = el("g", { opacity: 0 }, svg);
        el("circle", { cx: b.cx + 14, cy: b.cy + 18, r: 34, fill: "rgba(0,0,0,0.45)" }, g);
        el("circle", { cx: b.cx, cy: b.cy, r: 34, fill: BONE, stroke: INK, "stroke-width": 8 }, g);
        const t = S(48.81) + i * 2 / 12;
        tl.fromTo(p, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t);
        tl.fromTo(g, { opacity: 0, scale: 1.6, transformOrigin: `${b.cx}px ${b.cy}px` }, { opacity: 1, scale: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, t);
      });
      wr("sc011-t", [T(48.87) - L, T(49.35) - L, T(49.91) - L], { dur: 0.5 });
      tl.fromTo($("sc011-cam"), { x: 1.2 }, { x: -38.8, duration: 1.8, ease: "none", immediateRender: false }, S(48.75));
    })();
