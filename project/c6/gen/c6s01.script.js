  (function () {
    const SEG = "c6s01", SEG_START = 0.00, SEG_END = 201.96, DURATION = +(SEG_END - SEG_START).toFixed(2);
    const T = (s) => +(s - 0).toFixed(3);   // TEXT cues (audited) — literal word start − 0.06, LOCAL c6 seconds
    const S = (s) => +(s - 0).toFixed(3);   // STRUCTURAL cues (cuts, camera, objects)
    const tl = gsap.timeline({ paused: true });
    const $ = (id) => document.getElementById(SEG + "-" + id);
    const NS = "http://www.w3.org/2000/svg";
    const defs = $("defs");
    const E = FX.ease;
    const C = (e, d) => FX.choppy(e, d, 12);
    const BONE = "#f2ede3", INK = "#141b24", RED = "#e03f2c", CEL = "#9fc7b2", NAVY = "#1d5c9e", SKY = "#9fc3e3", YEL = "#f2d33b", PAPER = "#ebe4d6", GREY = "#9a958c";
    const PATHS = /*@PATHS@*/null;

    function gated(a, b, fn) { const on = FX.onFrame; FX.onFrame = (f) => on(FX.gate(S(a) - 0.1, S(b) + 0.1, f)); try { return fn(); } finally { FX.onFrame = on; } }
    // scene window: visible in [a, b]; display:none is applied to every scene at the very end (layout needed while building)
    const SCENES = [];
    function scene(id, a, b) {
      const el = $(id); SCENES.push(el);
      tl.fromTo(el, { autoAlpha: 0, display: "none" }, { autoAlpha: 1, display: "block", duration: 0.001, immediateRender: false }, S(a));
      if (b < SEG_END) tl.set(el, { autoAlpha: 0, display: "none" }, S(b));
    }
    function ground(kind, t) {
      const v = kind === "paper" ? [0.32, 0.14, 0.26] : [1, 0.42, 0.36];
      tl.set([$("vig"), $("dust"), $("grain")], { opacity: (i) => v[i] }, t);
    }
    const show = (el, t) => tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t);
    const rise = (el, t, o) => { o = o || {}; const d = o.dur || 0.9;
      tl.fromTo(el, { opacity: 0, y: o.y == null ? 18 : o.y }, { opacity: 1, y: 0, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const pop = (el, t, d, s0) => { d = d || 0.8; tl.fromTo(el, { opacity: 0, scale: s0 || 0.85 }, { opacity: 1, scale: 1, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const words = (id) => $(id).querySelectorAll(".k-w");
    const ul = (el, t, d) => { d = d || 0.5; tl.fromTo(el, { scaleX: 0 }, { scaleX: 1, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const whipN = { n: 0 };
    function whip(a, b, t, o) {
      o = Object.assign({ dir: 1, vertical: false, flash: false, dur: 0.32 }, o);
      const k = ++whipN.n, ba = FX.whipDefs(defs, `${SEG}-wa${k}`), bb = FX.whipDefs(defs, `${SEG}-wb${k}`), h = o.dur / 2;
      tl.set(a, { filter: `url(#${SEG}-wa${k})` }, t - h - 0.01); tl.set(a, { filter: "none" }, t + 0.06);
      tl.set(b, { filter: `url(#${SEG}-wb${k})` }, t - 0.001); tl.set(b, { filter: "none" }, t + h + 0.02);
      FX.whip(tl, a, b, t, { dir: o.dir, vertical: o.vertical, dur: o.dur, blurA: ba, blurB: bb });
      if (o.flash) tl.fromTo($("flash"), { opacity: 0 }, { opacity: 0.85, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.in", immediateRender: false }, t - 0.08);
    }
    // plain draw-on stroke (pathLength=1, so no layout is needed); o.filter for a pen look
    function ink(parent, d, t, dur, o) {
      o = o || {};
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d); p.setAttribute("fill", o.fill || "none"); p.setAttribute("pathLength", "1");
      p.setAttribute("stroke", o.color || INK); p.setAttribute("stroke-width", o.width || 6);
      p.setAttribute("stroke-linecap", "round"); p.setAttribute("stroke-linejoin", "round");
      if (o.filter) p.setAttribute("filter", o.filter);
      if (o.opacity != null) p.setAttribute("opacity", o.opacity);
      parent.appendChild(p);
      p.setAttribute("stroke-dasharray", "1 1"); p.setAttribute("stroke-dashoffset", 1);
      if (t != null) tl.fromTo(p, { attr: { "stroke-dashoffset": 1 } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: o.ease || C(E.out, dur), immediateRender: true }, t);
      return p;
    }
    function pin(svg, x, y, color, r, id) {
      svg.insertAdjacentHTML("beforeend", `<g id="${id}" opacity="0"><ellipse cx="${x + r * 0.6}" cy="${y + r * 0.5}" rx="${r * 0.9}" ry="${r * 0.35}" fill="rgba(0,0,0,0.45)"/><path d="M${x} ${y} L${x} ${y - r * 2.6}" stroke="#ddd" stroke-width="${r * 0.25}"/><circle cx="${x}" cy="${y - r * 2.6}" r="${r}" fill="${color}" stroke="${INK}" stroke-width="${r * 0.18}"/><circle cx="${x - r * 0.3}" cy="${y - r * 2.9}" r="${r * 0.28}" fill="rgba(255,255,255,0.6)"/></g>`);
      return document.getElementById(id);
    }
    function typeOn(el, t, per) {
      const chars = FX.split(el, "chars"); per = per || 1 / 24;
      tl.set(el, { opacity: 1 }, t);
      chars.forEach((c, i) => tl.fromTo(c, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t + i * per));
      return t + chars.length * per;
    }
    // word box (offset layout inside an un-transformed parent) → [x, y, w, h] relative to `rel`
    function box(el, rel) { let x = 0, y = 0, n = el; while (n && n !== rel) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; } return [x, y, el.offsetWidth, el.offsetHeight]; }

    // shared filters
    FX.tintDefs(defs, "c6s01-tint-ink", "#1d1f22", "#e9e1cf");
    FX.tintDefs(defs, "c6s01-tint-night", "#0e1013", "#bdb6a8");
    FX.grain($("grain"), 601);
    FX.dust($("dust"), 602, 2);

    /* ===== D06 hemicycle (motif master, C6S007–008 / C6S027): 114 voting dots in the real 1971 'important question'
       proportions (55 for = US side, 59 against = Beijing side) + 15 abstentions as a grey block. No numbers printed. ===== */
    function hemicycle(svg, pre) {
      const cx = 960, cy = 860, radii = [300, 352, 404, 456, 508, 560], sum = radii.reduce((a, b) => a + b, 0);
      let ns = radii.map((r) => Math.round(114 * r / sum)); ns[ns.length - 1] += 114 - ns.reduce((a, b) => a + b, 0);
      const dots = [];
      radii.forEach((r, i) => { const n = ns[i]; for (let k = 0; k < n; k++) { const a = (178 - k * (176 / (n - 1))) * Math.PI / 180; dots.push({ a, r, x: cx + r * Math.cos(a), y: cy - r * Math.sin(a) }); } });
      dots.sort((p, q) => q.a - p.a || p.r - q.r);
      const ma = (dots[56].a + dots[57].a) / 2;
      let html = `<path d="M${(cx + 250 * Math.cos(ma)).toFixed(1)} ${(cy - 250 * Math.sin(ma)).toFixed(1)} L${(cx + 610 * Math.cos(ma) + 3).toFixed(1)} ${(cy - 610 * Math.sin(ma)).toFixed(1)}" stroke="${INK}" stroke-width="4" stroke-dasharray="14 10" fill="none" id="${pre}-maj" opacity="0"/>`;
      dots.forEach((d, i) => { html += `<circle id="${pre}-d${i}" cx="${d.x.toFixed(1)}" cy="${d.y.toFixed(1)}" r="12" fill="#ddd4c2" stroke="${INK}" stroke-width="2.2" stroke-opacity="0.55"/>`; });
      for (let i = 0; i < 15; i++) html += `<circle id="${pre}-a${i}" cx="${(900 + (i % 5) * 30).toFixed(1)}" cy="${(760 + Math.floor(i / 5) * 30).toFixed(1)}" r="11" fill="#ddd4c2" stroke="${INK}" stroke-width="2" stroke-opacity="0.45"/>`;
      svg.insertAdjacentHTML("beforeend", html);
      return { dots: dots.map((d, i) => Object.assign(d, { el: document.getElementById(`${pre}-d${i}`) })), abst: Array.from({ length: 15 }, (_, i) => document.getElementById(`${pre}-a${i}`)), maj: document.getElementById(`${pre}-maj`), ma };
    }
    // fill a list of dots at 12 fps over dur seconds
    function fillDots(list, t, dur, color) {
      const steps = Math.max(1, Math.round(dur * 12));
      list.forEach((d, i) => tl.fromTo(d.el || d, { attr: { fill: "#ddd4c2" } }, { attr: { fill: color }, duration: 0.001, immediateRender: false }, t + Math.floor(i / list.length * steps) / 12));
    }

    /* =================== C6S001 · 0.00–2.48 · Taiwan doesn't know this, too. So =================== */
    scene("sc001", 0, 2.56);
    gsap.set($("sc001"), { autoAlpha: 1, display: "block" });
    ground("night", 0);
    (function () {
      tl.fromTo($("sc001-cam"), { scale: 1.0 }, { scale: 1.06, duration: 2.6, ease: "none", immediateRender: true }, 0);
      // reversed focus hunt: sharp → soft (not knowing)
      // c5 hand-off: c5s03 ends on the vote board at ~7–10 px blur with the push still moving → open at 9 px and
      // rack to sharp by 0.45 s (one continuous focus hunt across the cut), then the planned sharp → soft.
      const s = { r: 9 }, f = () => ($("sc001-cam").style.filter = `blur(${s.r.toFixed(2)}px)`);
      f();
      tl.fromTo(s, { r: 9 }, { r: 0, duration: 0.45, ease: "power2.out", immediateRender: true, onUpdate: f }, 0);
      tl.to(s, { r: 3, duration: 0.5, ease: "sine.inOut", onUpdate: f }, S(0.5));
      tl.to(s, { r: 1.5, duration: 0.3, ease: "sine.inOut", onUpdate: f }, S(1.0));
      tl.to(s, { r: 5, duration: 0.7, ease: "sine.inOut", onUpdate: f }, S(1.3));
    })();
    whip($("sc001-shot"), $("sc002-shot"), S(2.48), { dir: -1 });

    /* =================== C6S002 · 2.48–8.64 · George Bush tries another hail mary … he has done this before =================== */
    scene("sc002", 2.48, 8.66);
    ground("paper", S(2.48));
    (function () {
      const cam = $("sc002-cam");
      tl.fromTo(cam, { x: 0 }, { x: -40, duration: 5.8, ease: "none", immediateRender: true }, S(2.48));
      // football field (typographic: yard lines) inside the field panel
      const fs = $("sc002-fsvg");
      let h = `<rect width="1000" height="430" fill="#5f6b5c" opacity="0.35"/>`;
      for (let i = 0; i <= 10; i++) h += `<path d="M${50 + i * 90} 30 L${46 + i * 90} 400" stroke="${PAPER}" stroke-width="${i % 5 ? 3 : 6}" opacity="0.8"/>`;
      fs.innerHTML = h;
      tl.fromTo($("sc002-bush"), { x: -700, rotation: -8 }, { x: 0, rotation: -2.5, duration: 1.1, ease: C(E.out, 1.1), immediateRender: true }, S(2.40));
      tl.fromTo($("sc002-field"), { y: -600, rotation: 6 }, { y: 0, rotation: 2, duration: 1.2, ease: C(E.out, 1.2), immediateRender: true }, S(2.55));
      // name label-box, rough reveal that settles
      const ch = gated(2.3, 3.4, () => FX.roughDefs(defs, "c6s01-ch002", { freq: 0.05, scale: 6, choke: 0 }));
      $("sc002-nameb").style.filter = "url(#c6s01-ch002)";
      show($("sc002-nameb"), T(2.42));
      FX.chokeSettle(tl, ch, $("sc002-nameb"), T(2.42), 5, 0.5, "none");
      // Hail Mary + the long pass (pen arc)
      [T(4.10), T(4.50)].forEach((c, i) => rise(words("sc002-hm")[i], c, { dur: 0.7, y: 12 }));
      const mk = $("sc002-mk"), pf = gated(4.0, 8.7, () => FX.markupDefs(mk, "c6s01-mk002", { boil: 4 }));
      FX.markup.pen(tl, mk, S(4.16), { points: [[830, 520], [1050, 330], [1330, 250], [1560, 300], [1690, 420]], dur: 0.8, width: 6, color: INK, filter: pf, seed: 21, jitter: 5 });
      FX.markup.pen(tl, mk, S(4.92), { points: [[1650, 380], [1692, 424], [1700, 362]], dur: 0.14, width: 6, color: INK, filter: pf, seed: 22, jitter: 2 });
      // 'done this before': three resolution pages fan out (12 fps)
      const st = $("sc002-stack");
      [[-9, -40, 20], [-2, 10, -10], [6, 70, -30]].forEach(([r, x, y], i) => {
        st.insertAdjacentHTML("beforeend", `<div class="k-page" id="c6s01-sc002-pg${i}" style="left:120px; top:0; width:300px; height:388px; box-shadow:0 14px 30px rgba(20,27,36,0.35)"><img src="assets/c4/documents/un_draft_A-L630_1971_expel.jpg" alt="" style="position:absolute;inset:0;width:100%;height:100%;filter:sepia(0.35);mix-blend-mode:multiply"/></div>`);
        const pg = $("sc002-pg" + i);
        tl.fromTo(pg, { opacity: 0, x: 0, y: 140, rotation: 0 }, { opacity: 1, x: x * 2.2, y: y, rotation: r, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(6.0) + i * 0.17);
      });
      [T(5.94), T(6.10), T(6.26)].forEach((c, i) => rise(words("sc002-dtb")[i], c, { dur: 0.5, y: 8 }));
      // PT: push into the top page of the stack
      gsap.set(cam, { transformOrigin: "1330px 760px" });
      tl.to(cam, { scale: 2.8, duration: 0.42, ease: E.in }, S(8.22));
    })();

    /* =================== C6S003 · 8.64–13.69 · pass a resolution before the main resolution =================== */
    scene("sc003", 8.64, 13.71);
    ground("night", S(8.64));
    (function () {
      const cam = $("sc003-cam");
      tl.fromTo(cam, { scale: 1.12 }, { scale: 1.0, duration: 1.0, ease: E.cam, immediateRender: true }, S(8.64));
      tl.to(cam, { scale: 1.06, duration: 3.9, ease: "none" }, S(9.64));
      tl.fromTo($("sc003-small"), { x: 900, rotation: 14 }, { x: 0, rotation: 4, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(11.30));
      rise($("sc003-res"), T(11.38), { dur: 0.6, y: 8 });
      rise($("sc003-bef"), T(11.86), { dur: 0.7 });
      show($("sc003-mb"), T(12.26));
      [T(12.26), T(12.74)].forEach((c, i) => show(words("sc003-main-l")[i], c));
      // CA: the small page lifts toward camera as we cut
      tl.to($("sc003-small"), { scale: 1.25, y: -70, rotation: 1, duration: 0.6, ease: E.in }, S(13.15));
    })();

    /* =================== C6S004 · 13.69–21.13 · this Taiwan question is an important question … just a majority =================== */
    scene("sc004", 13.69, 21.20);
    ground("paper", S(13.69));
    (function () {
      const cam = $("sc004-cam");
      tl.fromTo(cam, { scale: 1.04, y: 10 }, { scale: 1.0, y: 0, duration: 1.2, ease: E.cam, immediateRender: true }, S(13.69));
      tl.fromTo($("sc004-dim"), { opacity: 0 }, { opacity: 1, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(13.75));
      [T(15.15), T(15.71)].forEach((c, i) => rise(words("sc004-tq")[i], c, { dur: 0.5, y: 8 }));
      ul($("sc004-tqu"), S(15.80), 0.5);
      show($("sc004-iq"), T(16.27));
      const iw = words("sc004-iq");
      [T(16.27), T(16.67), T(16.99), T(17.55)].forEach((c, i) => rise(iw[i], c, { dur: 0.35, y: 6 }));
      // highlighter on the body-size words 'important question' (one stroke, near-constant speed)
      const line = $("sc004-iq"), a = box(iw[2], cam), b = box(iw[3], cam);
      Object.assign($("sc004-hl").style, { left: a[0] - 8 + "px", top: a[1] + a[3] * 0.52 + "px", width: b[0] + b[2] - a[0] + 16 + "px", height: a[3] * 0.42 + "px" });
      tl.fromTo($("sc004-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.75, ease: C("sine.inOut", 0.75), immediateRender: true }, S(17.62));
      // text contrast call-out: the rest of the page dims while the frame punches in, key words stay at full strength
      const dimT = [$("sc004-dim"), $("sc004-line"), iw[0], iw[1]];
      tl.to(dimT, { opacity: 0.2, duration: 1.0, ease: E.out }, S(18.41));
      tl.to(cam, { scale: 1.1, duration: 1.2, ease: E.cam }, S(18.41));
      rise($("sc004-maj"), T(20.51), { dur: 0.3, y: 6 });
      const mk = $("sc004-mk"), pf = gated(20.4, 21.3, () => FX.markupDefs(mk, "c6s01-mk004", { boil: 4 }));
      FX.markup.cross(tl, mk, S(20.62), { x: 1440, y: 920, s: 60, dur: 0.1, color: INK, width: 7, filter: pf });
    })();
    whip($("sc004-shot"), $("sc005-shot"), S(21.13), { dir: -1, vertical: true });

    /* =================== C6S005 · 21.13–25.29 · You need two thirds to decide any kind of resolution =================== */
    scene("sc005", 21.13, 25.31);
    ground("paper", S(21.13));
    (function () {
      const cam = $("sc005-cam"), svg = $("sc005-svg");
      // dashed 2/3 threshold rises with the count
      svg.innerHTML = `<path id="c6s01-sc005-axis" d="M700 902 L1760 900" stroke="${INK}" stroke-width="4"/><g id="c6s01-sc005-thr"><path d="M680 502 L1780 498" stroke="${INK}" stroke-width="5" stroke-dasharray="18 12"/></g>`;
      const bars = $("sc005-bars"), H = [0.42, 0.55, 0.62, 0.74, 0.86];
      H.forEach((v, i) => {
        bars.insertAdjacentHTML("beforeend", `<div class="k-bar" id="c6s01-sc005-b${i}" style="left:${780 + i * 190}px; bottom:180px; height:${(v * 600).toFixed(0)}px; background:${v > 0.667 ? "#2b3440" : "#8f8a80"}"><div class="wc"></div></div>`);
        tl.fromTo($("sc005-b" + i), { scaleY: 0 }, { scaleY: 1, duration: 1.1, ease: C(E.out, 1.1), immediateRender: true }, S(21.70) + i * 0.08);
      });
      tl.fromTo($("sc005-thr"), { y: 400 }, { y: 0, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(21.42));
      pop($("sc005-23b"), T(21.39), 0.7, 0.8);
      [T(21.39)].forEach((c) => rise($("sc005-tt"), c, { dur: 0.6, y: 8 }));
      rise($("sc005-res"), T(23.95), { dur: 0.6, y: 8 });
      // CA: punch-in on the dashed line
      gsap.set(cam, { transformOrigin: "1230px 500px" });
      tl.to(cam, { scale: 1.3, duration: 0.4, ease: E.in }, S(24.95));
    })();

    /* =================== C6S006 · 25.29–29.77 · people are first voting … important question or not =================== */
    scene("sc006", 25.29, 29.85);
    ground("night", S(25.29));
    (function () {
      const cam = $("sc006-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.12, duration: 1.8, ease: E.cam, immediateRender: true }, S(25.29));
      tl.to(cam, { scale: 1.15, duration: 2.6, ease: "none" }, S(27.09));
      FX.focusHunt(tl, cam, S(27.2), { dur: 0.8 });
      gated(25.2, 29.9, () => FX.weave($("sc006-weave"), { amp: 0.4, flicker: 0.03, seed: 61 }));
      [T(25.87), T(26.11)].forEach((c, i) => rise(words("sc006-fv")[i], c, { dur: 0.6, y: 8 }));
      [T(28.43), T(28.91)].forEach((c, i) => rise(words("sc006-iq")[i], c, { dur: 0.6, y: 10 }));
    })();
    whip($("sc006-shot"), $("sc007-shot"), S(29.77), { dir: 1, flash: true });

    /* =================== C6S007–C6S008 · 29.77–38.09 · US does not have a majority · China has more than enough votes =================== */
    scene("sc007", 29.77, 38.15);
    ground("paper", S(29.77));
    (function () {
      const cam = $("sc007-cam"), H7 = hemicycle($("sc007-svg"), "c6s01-h7");
      tl.fromTo(cam, { x: -30 }, { x: 40, duration: 8.2, ease: "none", immediateRender: true }, S(29.77));
      [T(29.95), T(30.11), T(30.35)].forEach((c, i) => rise(words("sc007-ttl")[i], c, { dur: 0.6, y: 10 }));
      tl.fromTo(H7.maj, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(30.0));
      fillDots(H7.dots.slice(0, 55), S(30.05), 1.6, NAVY);
      fillDots(H7.abst, S(31.0), 0.5, GREY);
      rise($("sc007-us"), T(32.43), { dur: 0.6, y: 8 });
      [T(33.23), T(33.79)].forEach((c, i) => rise(words("sc007-nm")[i], c, { dur: 0.5, y: 8 }));
      // C6S008: the Beijing side fills from the right, past the majority line
      pop($("sc007-cnb"), T(35.23), 0.7, 0.85);
      fillDots(H7.dots.slice(55).reverse(), S(35.27), 1.2, RED);
      tl.to([$("sc007-ttl"), $("sc007-nm")], { opacity: 0.25, duration: 0.5, ease: E.out }, S(35.2));
      [T(35.79), T(36.03), T(36.19), T(36.43)].forEach((c, i) => rise(words("sc007-mte")[i], c, { dur: 0.5, y: 8 }));
      // camera starts a fast tilt up into the whip
      tl.to(cam, { y: 120, duration: 0.25, ease: E.in }, S(37.88));
    })();
    whip($("sc007-shot"), $("sc009-shot"), S(38.09), { dir: 1, vertical: true });

    /* =================== C6S009 · 38.09–41.69 · as soon as that vote comes to the floor in just a few minutes =================== */
    scene("sc009", 38.09, 41.71);
    ground("night", S(38.09));
    (function () {
      const cam = $("sc009-cam");
      tl.fromTo(cam, { y: 0, scale: 1.05 }, { y: -70, scale: 1.1, duration: 3.7, ease: "none", immediateRender: true }, S(38.09));
      const mk = $("sc009-mk"), pf = gated(38.2, 41.8, () => FX.markupDefs(mk, "c6s01-mk009", { boil: 4 }));
      FX.markup.circle(tl, mk, S(38.6), { cx: 1600, cy: 300, rx: 140, ry: 140, rot: 0, turns: 1.08, dur: 0.8, color: BONE, width: 6, filter: pf, seed: 91 });
      mk.insertAdjacentHTML("beforeend", `<g filter="${pf}" stroke="${BONE}" stroke-linecap="round" fill="none">${Array.from({ length: 12 }, (_, i) => { const a = i * Math.PI / 6; return `<path d="M${(1600 + 110 * Math.cos(a)).toFixed(1)} ${(300 + 110 * Math.sin(a)).toFixed(1)} L${(1600 + 124 * Math.cos(a)).toFixed(1)} ${(300 + 124 * Math.sin(a) + 1).toFixed(1)}" stroke-width="5"/>`; }).join("")}<path id="c6s01-sc009-hand" d="M1600 300 L1602 196" stroke-width="7"/><path d="M1600 300 L1660 318" stroke-width="7"/></g>`);
      const hand = $("sc009-hand"), ang = { a: 0 };
      const setH = () => { const r = (ang.a - 90) * Math.PI / 180; hand.setAttribute("d", `M1600 300 L${(1600 + 104 * Math.cos(r) + 1).toFixed(1)} ${(300 + 104 * Math.sin(r)).toFixed(1)}`); };
      setH();
      tl.to(ang, { a: 120, duration: 2.8, ease: C("none", 2.8), onUpdate: setH }, S(38.7));
      [T(40.11), T(40.19)].forEach((c, i) => rise(words("sc009-fl")[i], c, { dur: 0.5, y: 8 }));
      [T(40.91), T(40.99), T(41.23)].forEach((c, i) => rise(words("sc009-fm")[i], c, { dur: 0.4, y: 8 }));
    })();

    /* =================== C6S010 · 41.69–45.45 · Taiwan is getting kicked out. China is officially in the United Nations =================== */
    scene("sc010", 41.69, 45.52);
    ground("night", S(41.69));
    (function () {
      const cam = $("sc010-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.55, duration: 1.52, ease: "power2.in", immediateRender: true }, S(41.69));
      tl.to(cam, { scale: 1.75, duration: 2.3, ease: E.cam }, S(43.21));
      FX.contrastCallout(tl, $("sc010-veil"), S(43.21), { ellipse: [800, 568, 150, 46], feather: 22, color: "rgba(12,14,18,1)", strength: 0.75 });
      show($("sc010-tw"), T(41.63));
      [T(42.43), T(42.83)].forEach((c, i) => rise(words("sc010-ko")[i], c, { dur: 0.5, y: 8 }));
      tl.to($("sc010-chip"), { y: 760, rotation: 50, duration: 0.6, ease: C(E.in, 0.6) }, S(42.50));
      tl.to($("sc010-tw"), { opacity: 0.35, duration: 0.4 }, S(42.9));
      tl.fromTo($("sc010-cn"), { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, T(43.15));
      [T(43.63), T(44.03), T(44.19), T(44.35), T(44.75)].forEach((c, i) => rise(words("sc010-oi")[i], c, { dur: 0.35, y: 6 }));
    })();
    whip($("sc010-shot"), $("sc011-shot"), S(45.45), { dir: 1 });

    /* =================== C6S011 · 45.45–49.53 · everyone can see … and Taiwan can see what's about to happen =================== */
    scene("sc011", 45.45, 49.55);
    ground("paper", S(45.45));
    (function () {
      const cam = $("sc011-cam"), wrap = $("sc011-seats");
      const names = ["AFGHANISTAN","ALBANIA","ALGERIA","ARGENTINA","AUSTRALIA","AUSTRIA","BAHRAIN","BARBADOS","BELGIUM","BHUTAN","BOLIVIA","BOTSWANA","BRAZIL","BULGARIA","BURMA","BURUNDI","BYELORUSSIAN SSR","CAMEROON","CANADA","CENTRAL AFRICAN REP.","CEYLON","CHAD","CHILE","CHINA","COLOMBIA","CONGO","COSTA RICA","CUBA","CYPRUS","CZECHOSLOVAKIA","DAHOMEY","DENMARK","DOMINICAN REP.","ECUADOR","EGYPT","EL SALVADOR","EQUATORIAL GUINEA","ETHIOPIA","FIJI","FINLAND","FRANCE","GABON","GAMBIA","GHANA","GREECE","GUATEMALA","GUINEA","GUYANA","HAITI","HONDURAS","HUNGARY","ICELAND","INDIA","INDONESIA","IRAN","IRAQ","IRELAND","ISRAEL","ITALY","IVORY COAST","JAMAICA","JAPAN","JORDAN","KENYA","KHMER REPUBLIC","KUWAIT","LAOS","LEBANON","LESOTHO","LIBERIA","LIBYA","LUXEMBOURG","MADAGASCAR","MALAWI","MALAYSIA","MALDIVES","MALI","MALTA","MAURITANIA","MAURITIUS","MEXICO","MONGOLIA","MOROCCO","NEPAL","NETHERLANDS","NEW ZEALAND","NICARAGUA","NIGER","NIGERIA","NORWAY","OMAN","PAKISTAN","PANAMA","PARAGUAY","PERU","PHILIPPINES","POLAND","PORTUGAL","QATAR","ROMANIA","RWANDA","SAUDI ARABIA","SENEGAL","SIERRA LEONE","SINGAPORE","SOMALIA","SOUTH AFRICA","SPAIN","SUDAN","SWAZILAND","SWEDEN","SYRIA","THAILAND","TOGO","TUNISIA","TURKEY","UGANDA","UKRAINIAN SSR","USSR","UNITED KINGDOM","TANZANIA","UNITED STATES","URUGUAY","VENEZUELA","YEMEN","YUGOSLAVIA","ZAMBIA"];
      const rows = 8, per = 13, x0 = 100, y0 = 200, dx = 142, dy = 92;
      const rocR = 5, rocC = 6;                                // the CHINA (ROC) seat: row 5, centre
      const roc = [x0 + rocC * dx + 20 + 66, y0 + rocR * dy - 108 + 20];
      let k = 0; const seats = [];
      for (let r = 0; r < rows; r++) for (let c = 0; c < per; c++) {
        const isRoc = r === rocR && c === rocC;
        const nm = isRoc ? "CHINA" : names[(k++ * 7) % names.length];
        const x = x0 + c * dx + (r % 2 ? 20 : 0), y = y0 + r * dy - (36 - (c - 6) * (c - 6)) * 3;
        wrap.insertAdjacentHTML("beforeend", `<div class="k-seat t-label${isRoc ? " roc" : ""}" id="c6s01-st${r}_${c}" style="left:${x}px; top:${y}px">${nm === "CHINA" && !isRoc ? "CHILE" : nm}</div>`);
        if (!isRoc) seats.push({ el: document.getElementById(`c6s01-st${r}_${c}`), x: x + 66, y: y + 20 });
      }
      $("sc011-tw").style.left = roc[0] - 60 + "px"; $("sc011-tw").style.top = roc[1] + 34 + "px";
      gsap.set(cam, { transformOrigin: `${roc[0]}px ${roc[1]}px` });
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.12, duration: 3.6, ease: "none", immediateRender: true }, S(45.45));
      rise($("sc011-ev"), T(45.71), { dur: 0.7, y: 10 });
      // every card turns toward the CHINA (ROC) seat, 12 fps stagger by distance
      seats.forEach((s) => {
        const ang = Math.atan2(roc[1] - s.y, roc[0] - s.x) * 180 / Math.PI + 90, d = Math.hypot(roc[0] - s.x, roc[1] - s.y);
        const rot = Math.max(-70, Math.min(70, ((ang + 540) % 360) - 180));
        tl.fromTo(s.el, { rotation: 0 }, { rotation: rot * 0.5, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(45.78) + Math.floor(d / 120) / 12);
      });
      show($("sc011-twr"), T(47.63));
      ul($("sc011-twu"), S(47.75), 0.4);
      const mk = $("sc011-mk"), pf = gated(48.2, 49.6, () => FX.markupDefs(mk, "c6s01-mk011", { boil: 4 }));
      [[300, 260], [1620, 240], [260, 860], [1660, 880]].forEach(([x, y], i) => {
        const tx = roc[0] + (x < 960 ? -95 : 95), ty = roc[1] + (y < 540 ? -40 : 50);
        FX.markup.arrow(tl, mk, S(48.30) + i * 0.06, { x1: x, y1: y, x2: tx, y2: ty, bend: i % 2 ? 60 : -60, head: 26, dur: 0.45, color: INK, width: 6, filter: pf });
      });
      tl.to(cam, { scale: 3.4, duration: 0.42, ease: E.in }, S(49.12));
    })();

    /* =================== C6S012 · 49.53–54.49 · Taiwan just walks up to the front, officially just withdraws (2.5D) =================== */
    scene("sc012", 49.53, 54.51);
    ground("night", S(49.53));
    (function () {
      const cam = $("sc012-cam");
      tl.fromTo(cam, { z: -80, x: 40, rotationY: 1.5 }, { z: 120, x: -60, rotationY: -1.5, duration: 3.5, ease: E.cam, immediateRender: true }, S(49.53));
      tl.to(cam, { z: 170, x: -90, duration: 1.6, ease: "none" }, S(53.03));
      FX.focusHunt(tl, $("sc012-stage"), S(53.0), { dur: 0.8 });
      [T(50.59), T(50.91), T(51.07), T(51.23), T(51.31)].forEach((c, i) => rise(words("sc012-wf")[i], c, { dur: 0.5, y: 8 }));
      tl.fromTo($("sc012-wd"), { opacity: 0, scale: 1.06 }, { opacity: 1, scale: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, T(52.67));
      [T(53.23), T(53.39), T(53.55), T(53.87)].forEach((c, i) => rise(words("sc012-un")[i], c, { dur: 0.35, y: 6 }));
    })();

    /* =================== C6S013 · 54.49–58.41 · after they withdraw, I think people are crying =================== */
    scene("sc013", 54.49, 58.47);
    ground("night", S(54.49));
    (function () {
      gated(54.4, 58.5, () => FX.weave($("sc013-weave"), { amp: 1.4, flicker: 0.05, seed: 131 }));
      tl.fromTo($("sc013-weave"), { scale: 1.0 }, { scale: 1.04, duration: 3.95, ease: "none", immediateRender: true }, S(54.49));
      rise($("sc013-wd"), T(55.39), { dur: 0.6, y: 8 });
      rise($("sc013-cr"), T(57.63), { dur: 0.5, y: 10 });
    })();
    whip($("sc013-shot"), $("sc014-shot"), S(58.41), { dir: -1 });

    /* =================== C6S014 · 58.41–65.21 · some of the people from the Taiwanese delegation are crying … the future =================== */
    scene("sc014", 58.41, 65.23);
    ground("paper", S(58.41));
    (function () {
      const cam = $("sc014-cam");
      tl.fromTo(cam, { scale: 1.07 }, { scale: 0.98, duration: 7.0, ease: "none", immediateRender: true }, S(58.41));
      ["sc014-c1", "sc014-c2", "sc014-c3"].forEach((id, i) => tl.fromTo($(id), { opacity: 0, scale: 1.15, y: -30 }, { opacity: 1, scale: 1, y: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(58.55) + i * 0.42));
      [T(61.63), T(62.19)].forEach((c, i) => rise(words("sc014-td")[i], c, { dur: 0.6, y: 8 }));
      rise($("sc014-cr"), T(62.67), { dur: 0.6, y: 10 });
      [T(64.51), T(64.59)].forEach((c, i) => rise(words("sc014-fu")[i], c, { dur: 0.4, y: 8 }));
      // the faces blur into fog (reverse focus pull) — the unknown future
      tl.to([$("sc014-c1"), $("sc014-c2"), $("sc014-c3")], { filter: "blur(6px)", opacity: 0.75, duration: 0.4, ease: E.out }, S(64.3));
    })();

    /* =================== C6S015 · 65.21–72.64 · George H. W. Bush just sitting there with his head in his hands =================== */
    scene("sc015", 65.21, 73.25);
    ground("night", S(65.21));
    (function () {
      const cam = $("sc015-cam");
      gsap.set(cam, { transformOrigin: "600px 420px" });
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.08, duration: 3.0, ease: "none", immediateRender: true }, S(65.21));
      tl.to(cam, { scale: 1.2, duration: 0.4, ease: E.in }, S(68.2));
      tl.to(cam, { scale: 1.28, duration: 4.0, ease: E.cam }, S(68.6));
      FX.contrastCallout(tl, $("sc015-veil"), S(68.6), { ellipse: [600, 430, 320, 400], feather: 40, color: "rgba(12,14,18,1)", strength: 0.62 });
      show($("sc015-nmb"), T(66.75));
      [T(66.75), T(67.15), T(67.55)].forEach((c, i) => show(words("sc015-nm")[i], c));
      const mk = $("sc015-mk"), pf = gated(68.7, 73.3, () => FX.markupDefs(mk, "c6s01-mk015", { boil: 4 }));
      FX.markup.circle(tl, mk, S(68.83), { cx: 590, cy: 360, rx: 200, ry: 220, rot: -8, turns: 1.1, dur: 0.75, color: BONE, width: 7, filter: pf, seed: 151 });
      [T(68.83), T(69.15), T(69.23), T(69.39)].forEach((c, i) => rise(words("sc015-hh")[i], c, { dur: 0.5, y: 8 }));
      [T(71.55), T(71.95)].forEach((c, i) => rise(words("sc015-wo")[i], c, { dur: 0.4, y: 6 }));
      FX.markup.pen(tl, mk, S(71.62), { points: [[1180, 960], [1500, 990], [1800, 950]], dur: 0.45, width: 6, color: BONE, filter: pf, seed: 152, jitter: 4, blend: "normal" });
      FX.markup.pen(tl, mk, S(72.02), { points: [[1760, 920], [1802, 950], [1760, 985]], dur: 0.14, width: 6, color: BONE, filter: pf, seed: 153, jitter: 2, blend: "normal" });
    })();

    /* =================== C6S016 · 72.64–76.48 · One of the most famous pictures, probably in Taiwan, they still remember =================== */
    scene("sc016", 72.64, 76.55);
    (function () {
      // PS: the printed page slides down over the photo (the photo lands as itself, in print)
      tl.fromTo($("sc016-shot"), { y: -1080 }, { y: 0, duration: 0.55, ease: C(E.out, 0.55), immediateRender: true }, S(72.64));
      ground("paper", S(72.95));
      const cols = $("sc016-cols");
      let h = "";
      for (let c = 0; c < 2; c++) for (let i = 0; i < 46; i++) { const x = c ? 1600 : 120, w = 320 - ((i * 37) % 70); h += `<div class="k-ln" style="left:${x}px; top:${230 + i * 38}px; width:${w}px; height:8px"></div>`; }
      for (let i = 0; i < 22; i++) h += `<div class="k-ln" style="left:560px; top:${1180 + i * 38}px; width:${1000 - ((i * 53) % 160)}px; height:8px"></div>`;
      cols.innerHTML = h;
      const cam = $("sc016-cam");
      tl.fromTo(cam, { x: -1075, y: -834, scale: 1.92 }, { x: -1075, y: -824, scale: 1.92, duration: 0.4, ease: "none", immediateRender: true }, S(72.64));
      tl.to(cam, { x: 365, y: 70, scale: 0.62, duration: 1.3, ease: E.cam }, S(73.04));
      tl.to(cam, { y: 30, scale: 0.6, x: 384, duration: 2.2, ease: "none" }, S(74.34));
      [T(72.90), T(73.06), T(73.38)].forEach((c, i) => rise(words("sc016-mf")[i], c, { dur: 0.5, y: 8 }));
      show($("sc016-twr"), T(74.26));
      ul($("sc016-twu"), S(74.36), 0.45);
      [T(74.82), T(75.06)].forEach((c, i) => rise(words("sc016-sr")[i], c, { dur: 0.5, y: 8 }));
    })();
    whip($("sc016-shot"), $("sc017-shot"), S(76.48), { dir: -1, vertical: true });

    /* =================== C6S017 · 76.48–80.00 · a lot of African countries, especially Tanzania =================== */
    scene("sc017", 76.48, 80.02);
    ground("night", S(76.48));
    (function () {
      const cam = $("sc017-cam"), svg = $("sc017-svg"), A = PATHS.africa.d;
      Object.keys(A).forEach((k) => ink(svg, A[k], null, 0, { color: BONE, width: 4, opacity: 0.75 }));
      const outl = Array.from(svg.querySelectorAll("path"));
      tl.fromTo(outl, { attr: { "stroke-dashoffset": 1 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(77.06));
      tl.fromTo(cam, { x: -97, y: -87, scale: 0.405 }, { x: -540, y: -330, scale: 0.6, duration: 2.12, ease: E.in, immediateRender: true }, S(76.48));
      tl.to(cam, { x: -3352 + 400, y: -1800 + 200, scale: 1.18, duration: 1.6, ease: "power1.out" }, S(78.60));
      FX.contrastCallout(tl, $("sc017-veil"), S(78.60), { w: 5400, h: 3024, d: A.tanzania, feather: 26, color: "rgba(12,14,18,1)", strength: 0.66 });
      svg.insertAdjacentHTML("beforeend", `<path d="${A.tanzania}" fill="none" stroke="${BONE}" stroke-width="7" id="c6s01-sc017-tzo" opacity="0"/>`);
      show($("sc017-tzo"), S(78.60));
      const p = pin($("sc017-pin"), 3240, 1830, BONE, 26, "c6s01-sc017-pinA");
      tl.fromTo(p, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(78.70));
      tl.fromTo(p, { y: -60 }, { y: 0, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(78.70));
      [T(77.06), T(77.54)].forEach((c, i) => rise(words("sc017-ac")[i], c, { dur: 0.5, y: 8 }));
      pop($("sc017-tzb"), T(78.66), 0.6, 0.85);
    })();

    /* =================== C6S018 · 80.00–84.16 · dancing, basically trying to rub it into the Taiwanese delegation that they lost =================== */
    scene("sc018", 80.00, 84.23);
    ground("night", S(80.00));
    (function () {
      tl.fromTo($("sc018-cam"), { scale: 1.0 }, { scale: 1.08, duration: 4.2, ease: "none", immediateRender: true }, S(80.0));
      gated(79.9, 84.3, () => FX.weave($("sc018-weave"), { amp: 0.6, flicker: 0.03, seed: 181 }));
      rise($("sc018-da"), T(79.94), { dur: 0.7, y: 10 });
      [T(81.06), T(81.30), T(81.38)].forEach((c, i) => rise(words("sc018-rb")[i], c, { dur: 0.45, y: 6 }));
      rise($("sc018-lo"), T(83.46), { dur: 0.4, y: 8 });
    })();
    whip($("sc018-shot"), $("sc019-shot"), S(84.16), { dir: 1 });

    /* =================== C6S019 · 84.16–88.64 · this is happening all before the main vote … withdrawn and they're dancing =================== */
    scene("sc019", 84.16, 88.66);
    ground("paper", S(84.16));
    (function () {
      const cam = $("sc019-cam"), svg = $("sc019-svg");
      const ax = ink(svg, "M200 652 C900 646 1600 656 2400 650", S(84.25), 0.7, { color: INK, width: 5 });
      [500, 1100, 1800].forEach((x, i) => svg.insertAdjacentHTML("beforeend", `<path d="M${x} 630 L${x + 2} 674" stroke="${INK}" stroke-width="4" opacity="0.7"/>`));
      svg.insertAdjacentHTML("beforeend", `<circle id="c6s01-sc019-dot" cx="0" cy="651" r="17" fill="${INK}"/>`);
      const dot = $("sc019-dot");
      tl.fromTo(dot, { attr: { cx: 220 } }, { attr: { cx: 1100 }, duration: 3.5, ease: C("sine.inOut", 3.5), immediateRender: true }, S(84.4));
      tl.fromTo(cam, { x: 0 }, { x: -260, duration: 4.6, ease: "none", immediateRender: true }, S(84.16));
      // positions
      Object.assign($("sc019-wd").style, { left: "380px", top: "540px" });
      Object.assign($("sc019-ck").style, { left: "460px", top: "330px" });
      Object.assign($("sc019-th").style, { left: "960px", top: "290px" });
      Object.assign($("sc019-dn").style, { left: "990px", top: "700px" });
      Object.assign($("sc019-mvb").style, { left: "1560px", top: "430px", width: "520px", height: "170px" });
      Object.assign($("sc019-mv").style, { left: "1590px", top: "460px", fontSize: "76px" });
      Object.assign($("sc019-bf").style, { left: "1330px", top: "700px" });
      rise($("sc019-bf"), T(85.22), { dur: 0.6, y: 8 });
      [T(85.46), T(85.62), T(85.86)].forEach((c, i) => rise(words("sc019-mv")[i], c, { dur: 0.5, y: 8 }));
      tl.to([$("sc019-mv"), $("sc019-mvb")], { opacity: 0.45, duration: 0.6 }, S(86.6));
      show($("sc019-wd"), T(87.46));
      ul($("sc019-wdu"), S(87.52), 0.35);
      tl.fromTo($("sc019-ck"), { opacity: 0, scale: 1.7 }, { opacity: 1, scale: 1, duration: 0.35, ease: C(E.out, 0.35), immediateRender: true }, S(87.52));
      rise($("sc019-dn"), T(88.18), { dur: 0.3, y: 6 });
      tl.fromTo($("sc019-th"), { opacity: 0, scale: 1.2 }, { opacity: 1, scale: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(88.20));
    })();

    /* =================== C6S020 · 88.64–92.24 · this becomes such a big deal that Tanzania tries to walk this back =================== */
    scene("sc020", 88.64, 92.85);
    ground("night", S(88.64));
    (function () {
      const cam = $("sc020-cam");
      tl.fromTo(cam, { y: 0, scale: 1.0 }, { y: -50, scale: 1.05, duration: 4.2, ease: "none", immediateRender: true }, S(88.64));
      tl.fromTo($("sc020-p1"), { opacity: 0, scale: 1.3, rotation: -14 }, { opacity: 1, scale: 1, rotation: -6, duration: 0.42, ease: C(E.out, 0.42), immediateRender: true }, S(88.70));
      tl.fromTo($("sc020-p2"), { opacity: 0, scale: 1.3, rotation: 12 }, { opacity: 1, scale: 1, rotation: 4, duration: 0.42, ease: C(E.out, 0.42), immediateRender: true }, S(89.56));
      [T(89.54), T(89.70)].forEach((c, i) => rise(words("sc020-bd")[i], c, { dur: 0.5, y: 8 }));
      pop($("sc020-tzb"), T(90.10), 0.6, 0.85);
      [T(91.30), T(91.54), T(91.70)].forEach((c, i) => rise(words("sc020-wb")[i], c, { dur: 0.45, y: 8 }));
    })();

    /* =================== C6S021 · 92.24–96.88 · we weren't celebrating that they're crying or they're getting kicked out =================== */
    scene("sc021", 92.24, 96.95);
    (function () {
      // PS: the typed statement card slides over the newspaper pile
      tl.fromTo($("sc021-shot"), { x: 1920 }, { x: 0, duration: 0.55, ease: C(E.out, 0.55), immediateRender: true }, S(92.24));
      ground("paper", S(92.5));
      tl.fromTo($("sc021-cam"), { scale: 1.0 }, { scale: 1.05, duration: 4.6, ease: "none", immediateRender: true }, S(92.24));
      const w1 = words("sc021-l1");
      [T(93.46), T(93.54), T(93.78)].forEach((c, i) => typeOn(w1[i], c, 1 / 24));
      typeOn(words("sc021-l2")[0], T(94.74), 1 / 24);
      const w3 = words("sc021-l3");
      [T(95.54), T(95.78)].forEach((c, i) => typeOn(w3[i], c, 1 / 24));
      rise($("sc021-att"), S(96.10), { dur: 0.4, y: 6 });
    })();
    whip($("sc021-shot"), $("sc022-shot"), S(96.88), { dir: 1, vertical: true });

    /* =================== C6S022 · 96.88–102.08 · We weren't dancing, we were just standing up … a very, very big deal =================== */
    scene("sc022", 96.88, 102.15);
    ground("night", S(96.88));
    (function () {
      tl.fromTo($("sc022-cam"), { scale: 1.04 }, { scale: 1.1, duration: 5.2, ease: "none", immediateRender: true }, S(96.88));
      FX.focalBlur(tl, $("sc022-blur"), [{ x: 700, y: 520, r: 300 }, { t: S(97.3), x: 1000, y: 480, r: 340, dur: 1.6 }, { t: S(99.6), x: 880, y: 540, r: 380, dur: 1.4 }]);
      [T(96.98), T(97.22)].forEach((c, i) => rise(words("sc022-wd")[i], c, { dur: 0.6, y: 10 }));
      const mk = $("sc022-mk"), pf = gated(98.0, 102.2, () => FX.markupDefs(mk, "c6s01-mk022", { boil: 4 }));
      FX.markup.circle(tl, mk, S(98.10), { cx: 980, cy: 500, rx: 330, ry: 290, rot: -10, turns: 1.1, dur: 0.75, color: BONE, width: 6, filter: pf, seed: 221 });
      [T(98.10), T(98.34)].forEach((c, i) => rise(words("sc022-su")[i], c, { dur: 0.5, y: 8 }));
      // three headline strips (real 1971 front page) whip in
      const strips = $("sc022-strips");
      [[-940, -768, 144, 270, -2, 800], [-945, -915, 130, 440, 1.5, 765], [-1060, -1150, 150, 600, -1, 765]].forEach(([ox, oy, hh, top, r, ww], i) => {
        strips.insertAdjacentHTML("beforeend", `<div class="k-card" id="c6s01-sc022-s${i}" style="left:${300 + i * 90}px; top:${top}px; width:${ww}px; height:${hh}px; transform:rotate(${r}deg); background:#e8e0cc"><img src="assets/c6/derived/c6s01/kansan_1971-10-26_1800.jpg" alt="" style="position:absolute; left:${ox}px; top:${oy}px; width:1800px; height:2254px; object-fit:fill; filter:sepia(0.35) contrast(1.1)"/></div>`);
        tl.fromTo($("sc022-s" + i), { x: -1500, opacity: 1 }, { x: 0, duration: 0.45, ease: C(E.out, 0.45), immediateRender: true }, S(100.66) + i * 0.08);
      });
      [T(100.98), T(101.22), T(101.46), T(101.62)].forEach((c, i) => rise(words("sc022-vb")[i], c, { dur: 0.3, y: 6 }));
    })();
    whip($("sc022-shot"), $("sc023-shot"), S(102.08), { dir: -1, flash: true });

    /* =================== C6S023–C6S024 · 102.08–116.64 · painting-to-print: this quote … we lost the vote because of the visit … to China =================== */
    scene("sc023", 102.08, 116.70);
    ground("paper", S(102.08));
    (function () {
      const cam = $("sc023-cam"), page = $("sc023-page");
      const cols = $("sc023-cols");
      let h = "";
      for (let i = 0; i < 52; i++) h += `<div class="k-ln" style="left:300px; top:${300 + i * 36}px; width:${560 - ((i * 41) % 90)}px; height:8px"></div>`;
      for (let i = 0; i < 52; i++) h += `<div class="k-ln" style="left:2640px; top:${300 + i * 36}px; width:${300 - ((i * 29) % 60)}px; height:8px"></div>`;
      h += `<div class="k-ln" style="left:300px; top:180px; width:2560px; height:6px; background:var(--ink)"></div>`;
      for (let i = 0; i < 14; i++) h += `<div class="k-ln" style="left:2100px; top:${300 + i * 36}px; width:${440 - ((i * 37) % 80)}px; height:8px"></div>`;
      cols.innerHTML = h;
      // full-frame colour picture → pull-back + upward pan reveals it printed in a column
      tl.fromTo(cam, { x: -2002, y: -902, scale: 1.975 }, { x: -1990, y: -890, scale: 1.96, duration: 3.1, ease: "none", immediateRender: true }, S(102.08));
      tl.to(cam, { x: 30, y: 60, scale: 0.62, duration: 1.3, ease: E.cam }, S(105.18));
      tl.to(cam, { x: -165, y: -210, scale: 0.75, duration: 3.2, ease: E.inOut }, S(106.6));
      tl.to(cam, { x: -390, y: -765, scale: 0.9, duration: 1.4, ease: E.inOut }, S(109.95));
      tl.to(cam, { x: -553, y: -862, scale: 0.85, duration: 3.6, ease: E.inOut }, S(112.7));
      [T(103.86), T(104.02)].forEach((c, i) => rise(words("sc023-tq")[i], c, { dur: 0.6, y: 10 }));
      tl.to($("sc023-tq"), { opacity: 0, duration: 0.4, ease: E.in }, S(105.1));
      [T(104.58), T(105.06), T(105.70)].forEach((c, i) => show(words("sc023-cap")[i], c));
      rise($("sc023-later"), T(106.50), { dur: 0.7, y: 10 });
      rise($("sc023-com"), T(108.34), { dur: 0.7, y: 10 });
      // C6S024 pull-quote: words land as spoken, each pen-underlined on its word (§10.7)
      const mk = $("sc023-mk"), pf = gated(111.3, 116.8, () => FX.markupDefs(mk, "c6s01-mk023", { boil: 4 }));
      mk.setAttribute("viewBox", "0 0 3000 2400");
      const pw = words("sc023-pq");
      [T(111.46), T(111.70), T(112.10), T(112.26), T(112.74), T(113.06), T(113.38), T(113.54)].forEach((c, i) => {
        show(pw[i], c);
        const b = box(pw[i], page);
        FX.markup.pen(tl, mk, c + 0.04, { points: [[b[0] + 2, b[1] + b[3] - 4], [b[0] + b[2] * 0.5, b[1] + b[3] - 1], [b[0] + b[2] - 20, b[1] + b[3] - 5]], dur: 0.3, width: 6, color: INK, filter: pf, seed: 230 + i, jitter: 3 });
      });
      tl.fromTo($("sc023-inset"), { opacity: 0, scale: 1.12 }, { opacity: 1, scale: 1, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(114.0));
      show($("sc023-kis"), T(114.02));
      [T(115.86), T(116.02)].forEach((c, i) => rise(words("sc023-tc")[i], c, { dur: 0.3, y: 6 }));
      rise($("sc023-att"), S(114.6), { dur: 0.6, y: 6 });
    })();
    whip($("sc023-shot"), $("sc025-shot"), S(116.64), { dir: -1 });

    /* =================== C6S025 · 116.64–124.56 · cutting my legs out from under me … the US is with Taiwan =================== */
    scene("sc025", 116.64, 124.58);
    ground("night", S(116.64));
    (function () {
      const cam = $("sc025-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.07, duration: 8.0, ease: "none", immediateRender: true }, S(116.64));
      [T(118.82), T(119.22), T(119.38), T(119.78)].forEach((c, i) => rise(words("sc025-cl")[i], c, { dur: 0.5, y: 8 }));
      const mk = $("sc025-mk"), pf = gated(119.2, 120.4, () => FX.markupDefs(mk, "c6s01-mk025", { boil: 4 }));
      FX.markup.pen(tl, mk, S(119.38), { points: [[30, 706], [300, 698], [620, 708], [940, 696]], dur: 0.35, width: 7, color: BONE, filter: pf, seed: 251, jitter: 6, blend: "normal" });
      tl.to($("sc025-lb"), { y: 760, rotation: 7, duration: 0.7, ease: C(E.in, 0.7) }, S(119.75));
      const uw = words("sc025-us");
      [T(122.90), T(123.14), T(123.62), T(123.78)].forEach((c, i) => rise(uw[i], c, { dur: 0.4, y: 6 }));
      ul($("sc025-twu"), S(123.85), 0.35);
    })();

    /* =================== C6S026 · 124.56–129.59 · while the administration is visiting China … if it wasn't for that visit =================== */
    scene("sc026", 124.56, 129.66);
    ground("night", S(124.56));
    (function () {
      const cam = $("sc026-cam");
      gsap.set(cam, { transformOrigin: "826px 640px" });
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.03, duration: 1.04, ease: "none", immediateRender: true }, S(124.56));
      tl.to(cam, { scale: 1.42, duration: 0.5, ease: E.cam }, S(125.60));
      tl.to(cam, { scale: 1.5, duration: 3.6, ease: "none" }, S(126.10));
      FX.focusHunt(tl, cam, S(126.10), { dur: 0.8 });
      [T(124.74), T(124.98)].forEach((c, i) => rise(words("sc026-ad")[i], c, { dur: 0.6, y: 8 }));
      [T(125.70), T(127.06)].forEach((c, i) => rise(words("sc026-vc")[i], c, { dur: 0.6, y: 10 }));
      const mk = $("sc026-mk"), pf = gated(128.6, 129.7, () => FX.markupDefs(mk, "c6s01-mk026", { boil: 4 }));
      FX.markup.circle(tl, mk, S(128.74), { cx: 826, cy: 640, rx: 150, ry: 120, rot: -6, turns: 1.1, dur: 0.6, color: BONE, width: 5, filter: pf, seed: 261 });
      [T(128.74), T(128.90)].forEach((c, i) => rise(words("sc026-tv")[i], c, { dur: 0.4, y: 6 }));
    })();
    whip($("sc026-shot"), $("sc027-shot"), S(129.59), { dir: -1, vertical: true });

    /* =================== C6S027 · 129.59–134.87 · We might have won that vote … Taiwan was out of the United Nations =================== */
    scene("sc027", 129.59, 134.89);
    ground("paper", S(129.59));
    (function () {
      const cam = $("sc027-cam"), H = hemicycle($("sc027-svg"), "c6s01-h27");
      // state carried over from C6S007–008 (filled), the camera from the other side
      H.dots.forEach((d, i) => d.el.setAttribute("fill", i < 55 ? NAVY : RED));
      H.abst.forEach((d) => d.setAttribute("fill", GREY));
      H.maj.setAttribute("opacity", 1);
      tl.fromTo(cam, { rotation: -3, x: 30 }, { rotation: 3, x: -30, duration: 5.3, ease: "none", immediateRender: true }, S(129.59));
      [T(129.69), T(129.85), T(129.93)].forEach((c, i) => rise(words("sc027-mw")[i], c, { dur: 0.5, y: 8 }));
      // 'might have won': three ghost navy rings creep toward the line
      [55, 56, 57].forEach((k, i) => {
        const d = H.dots[k];
        $("sc027-svg").insertAdjacentHTML("beforeend", `<circle id="c6s01-h27-g${i}" cx="${d.x.toFixed(1)}" cy="${d.y.toFixed(1)}" r="16" fill="none" stroke="${NAVY}" stroke-width="4" stroke-dasharray="5 4" opacity="0"/>`);
        tl.fromTo($("h27-g" + i), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(130.0) + i / 12 * 2);
        tl.to($("h27-g" + i), { attr: { opacity: 0 }, duration: 0.3 }, S(131.9));
      });
      // Taiwan's celadon dot drops out of the Assembly; navy dims (two accents: celadon + red)
      const tw = H.dots[22];
      tl.set(tw.el, { attr: { fill: CEL, r: 19, stroke: INK, "stroke-width": 4, "stroke-opacity": 1 } }, S(132.33));
      tl.to(H.dots.filter((d, i) => i < 55 && i !== 22).map((d) => d.el), { attr: { "fill-opacity": 0.3 }, duration: 0.3 }, S(132.33));
      Object.assign($("sc027-tw").style, { left: tw.x - 120 + "px", top: tw.y - 100 + "px" });
      show($("sc027-tw"), T(132.33));
      ul($("sc027-twu"), S(132.40), 0.35);
      Object.assign($("sc027-out").style, { left: tw.x + 40 + "px", top: tw.y + 20 + "px" });
      rise($("sc027-out"), T(132.89), { dur: 0.4, y: 8 });
      tl.to(tw.el, { attr: { cy: tw.y + 900 }, duration: 0.9, ease: C(E.in, 0.9) }, S(132.95));
      tl.to($("sc027-tw"), { opacity: 0, duration: 0.3 }, S(133.6));
      [T(134.01), T(134.33)].forEach((c, i) => rise(words("sc027-un")[i], c, { dur: 0.3, y: 6 }));
      // PT: push after the falling dot
      gsap.set(cam, { transformOrigin: `${tw.x}px 1080px` });
      tl.to(cam, { scale: 2.6, y: -400, duration: 0.45, ease: E.in }, S(134.44));
    })();

    /* =================== C6S028 · 134.87–137.75 · and then it has a cascading or like a domino effect =================== */
    scene("sc028", 134.87, 137.77);
    ground("night", S(134.87));
    (function () {
      const row = $("sc028-row"), cam = $("sc028-cam");
      const pipsets = [[[0.3, 0.25], [0.7, 0.25], [0.5, 0.75]], [[0.3, 0.2], [0.7, 0.4], [0.3, 0.65], [0.7, 0.85]], [[0.5, 0.25], [0.3, 0.65], [0.7, 0.85]], [[0.3, 0.25], [0.7, 0.25], [0.3, 0.75], [0.7, 0.75], [0.5, 0.65]]];
      for (let i = 0; i < 11; i++) {
        const x = 180 + i * 150, y = 420 + i * 14, sc = 1 - i * 0.03;
        const pips = pipsets[i % 4].map(([px, py]) => `<i style="left:${(px * 96 - 8).toFixed(0)}px; top:${(py * 188 - 8).toFixed(0)}px"></i>`).join("");
        row.insertAdjacentHTML("beforeend", `<div class="k-dom${i === 0 ? " tw" : ""}" id="c6s01-dm${i}" style="left:${x}px; top:${y}px">${pips}</div>`);
        gsap.set($("dm" + i), { scale: sc });
        tl.fromTo($("dm" + i), { rotation: 0 }, { rotation: 74, duration: 0.42, ease: C(E.in, 0.42), immediateRender: true }, S(135.62) + i * 0.165);
      }
      tl.fromTo(cam, { x: 0, scale: 1.05 }, { x: -620, scale: 1.12, duration: 2.95, ease: "power1.inOut", immediateRender: true }, S(134.87));
      rise($("sc028-cas"), T(135.61), { dur: 0.6, y: 8 });
      [T(136.65), T(137.13)].forEach((c, i) => tl.fromTo(words("sc028-de")[i], { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, c));
    })();

    /* =================== C6S029 · 137.75–142.47 · Slowly allies are now switching their recognition from Taiwan to the CCP =================== */
    scene("sc029", 137.75, 142.54);
    ground("night", S(137.75));
    (function () {
      const cam = $("sc029-cam"), svg = $("sc029-svg"), W = PATHS.world;
      const groups = { w: ["canada", "mexico", "peru", "brazil", "argentina"], e: ["italy", "belgium", "germany", "greece", "turkey", "lebanon", "iran"], a: ["thailand", "malaysia", "philippines", "japan", "australia", "new_zealand"] };
      let h = "<defs>";
      ["w", "e", "a"].forEach((g, i) => ["r", "c"].forEach((kind) => {
        h += `<filter id="c6s01-bn${g}${kind}" filterUnits="userSpaceOnUse" x="0" y="0" width="6144" height="3072" color-interpolation-filters="sRGB"><feImage href="assets/maps/burn_${i % 2 ? "b" : "a"}.png" preserveAspectRatio="none" result="n"/><feColorMatrix id="c6s01-bm${g}${kind}" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 -12" result="t"/><feComposite in="SourceGraphic" in2="t" operator="in"/></filter>`;
      }));
      h += "</defs>";
      ["w", "e", "a"].forEach((g) => {
        const d = groups[g].map((k) => W.d[k]).join("");
        h += `<path d="${d}" fill="#1a0e0a" stroke="#2a1510" stroke-width="10" filter="url(#c6s01-bn${g}c)"/>`;
        h += `<path d="${d}" fill="${RED}" fill-opacity="0.6" stroke="${RED}" stroke-width="3" filter="url(#c6s01-bn${g}r)"/>`;
      });
      h += `<path d="${W.d.taiwan}" fill="${CEL}" stroke="${CEL}" stroke-width="6"/><circle cx="5137" cy="1131" r="34" fill="none" stroke="${CEL}" stroke-width="7"/>`;
      svg.innerHTML = h;
      const burn = (g, t, dur) => ["c", "r"].forEach((kind) => {
        const m = $(`bm${g}${kind}`), s = { k: -12 }, lead = kind === "c" ? 0.25 : 0;
        const f = () => m.setAttribute("values", `0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 ${s.k.toFixed(2)}`);
        tl.fromTo(s, { k: -12 }, { k: kind === "c" ? 1.5 : 0.6, duration: dur, ease: C("sine.inOut", dur), immediateRender: true, onUpdate: f }, t - lead);
      });
      burn("w", S(138.55), 1.2); burn("e", S(139.45), 1.2); burn("a", S(140.40), 1.2);
      tl.fromTo(cam, { x: -423, y: -254, scale: 0.62 }, { x: -1799, y: -254, scale: 0.62, duration: 4.9, ease: E.inOut, immediateRender: true }, S(137.75));
      rise($("sc029-al"), T(138.49), { dur: 0.6, y: 8 });
      [T(139.37), T(140.01)].forEach((c, i) => rise(words("sc029-sr")[i], c, { dur: 0.6, y: 10 }));
      svg.insertAdjacentHTML("beforeend", `<text id="c6s01-sc029-twl" x="5200" y="1260" fill="${CEL}" font-size="64" class="t-label" style="letter-spacing:0.18em" opacity="0">TAIWAN</text>`);
      tl.fromTo($("sc029-twl"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, T(140.81));
      pop($("sc029-ccpb"), T(141.61), 0.35, 0.85);
    })();
    whip($("sc029-shot"), $("sc030-shot"), S(142.47), { dir: -1 });

    /* =================== C6S030 · 142.47–149.75 · the biggest hit is from Japan, the biggest trade partner … close allies =================== */
    scene("sc030", 142.47, 149.77);
    ground("paper", S(142.47));
    (function () {
      const ch = $("sc030-chart"), cam = $("sc030-cam");
      const flags = {
        jp: `<svg viewBox="0 0 120 120"><rect width="120" height="120" fill="#ece6d8"/><circle cx="60" cy="60" r="27" fill="#6b6660"/></svg>`,
        us: `<svg viewBox="0 0 120 120"><rect width="120" height="120" fill="#ece6d8"/>${Array.from({ length: 7 }, (_, i) => `<rect y="${i * 17.2}" width="120" height="8.6" fill="#7d7870"/>`).join("")}<rect width="56" height="52" fill="#3e4148"/></svg>`,
        de: `<svg viewBox="0 0 120 120"><rect width="120" height="40" fill="#2a2c30"/><rect y="40" width="120" height="40" fill="#77726b"/><rect y="80" width="120" height="40" fill="#b5aea2"/></svg>`,
      };
      [["jp", 420, 560], ["us", 700, 420], ["de", 980, 290]].forEach(([k, x, hgt], i) => {
        ch.insertAdjacentHTML("beforeend", `<div class="k-bar" id="c6s01-sc030-b${k}" style="left:${x}px; bottom:230px; height:${hgt}px; background:${i ? "#8f8a80" : "#2b3440"}"><div class="wc"></div></div><div class="k-disc" id="c6s01-sc030-d${k}" style="left:${x + 4}px; top:${850 - hgt - 160}px">${flags[k]}</div>`);
        tl.fromTo($("sc030-b" + k), { scaleY: 0 }, { scaleY: 1, duration: 1.1, ease: C(E.out, 1.1), immediateRender: true }, S(143.80) + i * 0.1);
        tl.fromTo($("sc030-d" + k), { y: hgt + 160, opacity: 0 }, { y: 0, opacity: 1, duration: 1.1, ease: C(E.out, 1.1), immediateRender: true }, S(143.80) + i * 0.1);
      });
      ch.insertAdjacentHTML("beforeend", `<div class="k-abs t-display" id="c6s01-sc030-jpl" style="left:420px; top:870px; font-size:52px"><span class="k-inkbox" id="c6s01-sc030-jpb" style="opacity:0">JAPAN</span></div>`);
      ch.insertAdjacentHTML("beforeend", `<div class="k-disc" id="c6s01-sc030-tw" style="left:1560px; top:430px; width:150px; height:150px; background:${CEL}; opacity:0"></div>`);
      [T(143.77), T(144.09)].forEach((c, i) => rise(words("sc030-bh")[i], c, { dur: 0.5, y: 8 }));
      pop($("sc030-jpb"), T(144.81), 0.6, 0.85);
      [T(145.77), T(145.93), T(146.33), T(146.65)].forEach((c, i) => rise(words("sc030-ttl")[i], c, { dur: 0.5, y: 8 }));
      pop($("sc030-tw"), S(148.20), 0.5, 0.7);
      [T(148.41), T(148.65)].forEach((c, i) => rise(words("sc030-ca")[i], c, { dur: 0.5, y: 8 }));
      const mk = $("sc030-mk"), pf = gated(148.2, 149.8, () => FX.markupDefs(mk, "c6s01-mk030", { boil: 4 }));
      FX.markup.pen(tl, mk, S(148.35), { points: [[565, 200], [900, 230], [1250, 330], [1555, 488]], dur: 0.7, width: 6, color: INK, filter: pf, seed: 301, jitter: 6 });
      gsap.set(cam, { transformOrigin: "485px 225px" });
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.05, duration: 6.85, ease: "none", immediateRender: true }, S(142.47));
      tl.to(cam, { scale: 4.2, duration: 0.42, ease: E.in }, S(149.33));
    })();

    /* =================== C6S031 · 149.75–156.47 · So Japan switching recognition from Taiwan to China was definitely a big hit =================== */
    scene("sc031", 149.75, 156.49);
    ground("night", S(149.75));
    (function () {
      const cam = $("sc031-cam"), svg = $("sc031-svg"), EA = PATHS.east_asia.d;
      svg.innerHTML = `<path d="${EA.japan}" fill="${BONE}" fill-opacity="0.18" stroke="${BONE}" stroke-width="3" stroke-opacity="0.8"/>
        <path id="c6s01-sc031-tw" d="${EA.taiwan}" fill="${CEL}" fill-opacity="0" stroke="${CEL}" stroke-width="4"/>
        <path id="c6s01-sc031-cnf" d="${EA.china}" fill="${RED}" fill-opacity="0" stroke="${RED}" stroke-opacity="0" stroke-width="4"/>`;
      // map is 3199 px wide → scale ≥ 0.64 so it always covers 1920 (same framing centre as planned: map ≈ (1600,1290) → (1603,1276))
      tl.fromTo(cam, { x: -64, y: -286, scale: 0.64 }, { x: -72, y: -292, scale: 0.645, duration: 1.0, ease: "none", immediateRender: true }, S(149.75));
      tl.to(cam, { x: -114, y: -315, scale: 0.67, duration: 5.6, ease: E.inOut }, S(150.75));
      tl.to($("sc031-tw"), { attr: { "fill-opacity": 0.85 }, duration: 0.5, ease: C(E.out, 0.5) }, S(150.25));
      const l1 = ink(svg, "M2470 960 Q1950 1300 1400 1760", S(150.30), 0.7, { color: CEL, width: 10 });
      tl.to(l1, { attr: { "stroke-dashoffset": -1 }, duration: 0.5, ease: E.in }, S(152.30));
      tl.to($("sc031-tw"), { attr: { "fill-opacity": 0.25 }, duration: 0.5 }, S(152.4));
      tl.to($("sc031-cnf"), { attr: { "fill-opacity": 0.22, "stroke-opacity": 1 }, duration: 0.6, ease: C(E.out, 0.6) }, S(153.95));
      ink(svg, "M2470 900 Q1800 560 1080 640", S(153.99), 0.7, { color: RED, width: 10 });
      FX.focalBlur(tl, $("sc031-blur"), [{ x: 2540, y: 922, r: 520 }, { t: S(151.4), x: 1700, y: 1450, r: 700, dur: 1.5 }, { t: S(153.6), x: 1500, y: 900, r: 900, dur: 1.6 }]);
      show($("sc031-jp"), T(150.17));
      [T(150.81), T(151.29)].forEach((c, i) => rise(words("sc031-sr")[i], c, { dur: 0.6, y: 10 }));
      show($("sc031-cn"), T(153.93));
      [T(155.37), T(155.77)].forEach((c, i) => rise(words("sc031-bh")[i], c, { dur: 0.4, y: 10 }));
      // CRT: the picture collapses to a line — it becomes the TV of the next shot
      tl.to($("sc031-shot"), { scaleY: 0.012, filter: "brightness(2.2)", duration: 0.17, ease: "power2.in" }, S(156.30));
    })();

    /* =================== C6S032 · 156.47–161.11 · Back in Taiwan, everyone's seeing this, especially the dancing scene =================== */
    scene("sc032", 156.47, 161.13);
    ground("night", S(156.47));
    (function () {
      const cam = $("sc032-cam");
      tl.fromTo($("sc032-scr"), { scaleY: 0.012 }, { scaleY: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(156.50));
      tl.fromTo($("sc032-pw"), { opacity: 1 }, { opacity: 0, duration: 0.45, ease: "power1.out", immediateRender: true }, S(156.55));
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.1, duration: 4.2, ease: "none", immediateRender: true }, S(156.47));
      tl.to(cam, { scale: 4.0, duration: 0.42, ease: E.in }, S(160.69));
      [T(156.41), T(156.73), T(156.89)].forEach((c, i) => rise(words("sc032-bt")[i], c, { dur: 0.5, y: 8 }));
      ul($("sc032-btu"), S(157.0), 0.5);
      [T(158.81), T(158.97), T(159.37)].forEach((c, i) => rise(words("sc032-ds")[i], c, { dur: 0.6, y: 10 }));
      rise($("sc032-fa"), T(160.25), { dur: 0.4, y: 6 });
    })();

    /* =================== C6S033 · 161.11–164.71 · And they just cannot keep in the anger and the grief =================== */
    scene("sc033", 161.11, 164.78);
    ground("paper", S(161.11));
    (function () {
      [["sc033-a", -30, 0], ["sc033-b", 40, 0.15], ["sc033-c", -60, 0.3]].forEach(([id, dx, d]) => {
        tl.fromTo($(id), { opacity: 0, y: 90 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(161.15) + d);
        tl.fromTo($(id), { x: 0 }, { x: dx, duration: 3.6, ease: "none", immediateRender: true }, S(161.11));
      });
      rise($("sc033-an"), T(163.29), { dur: 0.6, y: 12 });
      rise($("sc033-gr"), T(164.09), { dur: 0.4, y: 10 });
    })();
    whip($("sc033-shot"), $("sc034-shot"), S(164.71), { dir: 1 });

    /* =================== C6S034 · 164.71–172.07 · comments from the economic minister … the technological revolution Taiwan is about to have =================== */
    scene("sc034", 164.71, 172.09);
    ground("night", S(164.71));
    (function () {
      tl.fromTo($("sc034-cam"), { scale: 1.0 }, { scale: 1.06, duration: 7.4, ease: "none", immediateRender: true }, S(164.71));
      gated(164.7, 172.1, () => FX.streaks($("sc034-st"), { seed: 341, speed: 0.5, tint: [255, 226, 190], gain: 1.1 }));
      tl.fromTo($("sc034-st"), { opacity: 0 }, { opacity: 0.6, duration: 1.0, ease: E.out, immediateRender: true }, S(169.0));
      const ch = gated(166.3, 167.4, () => FX.roughDefs(defs, "c6s01-ch034", { freq: 0.05, scale: 6, choke: 0 }));
      $("sc034-emb").style.filter = "url(#c6s01-ch034)";
      show($("sc034-emb"), T(166.41));
      [T(166.41), T(166.97)].forEach((c, i) => show(words("sc034-em")[i], c));
      FX.chokeSettle(tl, ch, $("sc034-emb"), T(166.41), 5, 0.5, "none");
      [T(168.97), T(170.01)].forEach((c, i) => rise(words("sc034-tr")[i], c, { dur: 0.7, y: 10 }));
      show($("sc034-twr"), T(170.81));
      ul($("sc034-twu"), S(170.9), 0.45);
    })();

    /* =================== C6S035 · 172.07–175.67 · he was just like, wow, they couldn't believe that this happened =================== */
    scene("sc035", 172.07, 175.74);
    ground("paper", S(172.07));
    (function () {
      tl.fromTo($("sc035-cam"), { scale: 1.0, x: 0 }, { scale: 1.03, x: -20, duration: 3.7, ease: "none", immediateRender: true }, S(172.07));
      rise($("sc035-wow"), T(173.21), { dur: 0.6, y: 10 });
      FX.text.random(tl, $("sc035-cb1"), T(174.09), { dur: 0.3, seed: 351 });
      FX.text.random(tl, $("sc035-cb2"), T(174.41), { dur: 0.3, seed: 352 });
      rise($("sc035-att"), S(174.85), { dur: 0.3, y: 6 });
    })();
    whip($("sc035-shot"), $("sc036-shot"), S(175.67), { dir: -1, vertical: true });

    /* =================== C6S036 · 175.67–180.95 · They fought a war with the United States. They were on the winning side =================== */
    scene("sc036", 175.67, 180.97);
    ground("night", S(175.67));
    (function () {
      gated(175.6, 181.0, () => FX.weave($("sc036-weave"), { amp: 0.9, flicker: 0.04, seed: 361 }));
      tl.fromTo($("sc036-cam"), { scale: 1.0 }, { scale: 1.16, duration: 5.4, ease: "power1.in", immediateRender: true }, S(175.67));
      [T(175.77), T(176.17), T(176.33), T(176.65), T(176.81), T(176.97), T(177.37)].forEach((c, i) => rise(words("sc036-fw")[i], c, { dur: 0.45, y: 6 }));
      [T(178.33), T(178.73)].forEach((c, i) => rise(words("sc036-ws")[i], c, { dur: 0.6, y: 10 }));
      const mk = $("sc036-mk"), pf = gated(178.2, 181.0, () => FX.markupDefs(mk, "c6s01-mk036", { boil: 4 }));
      const wb = box($("sc036-ws"), $("sc036-shot")), wy = wb[1] + wb[3] - 4;   // under "winning side" (svg at shot level, not in the push)
      FX.markup.pen(tl, mk, S(178.80), { points: [[wb[0] + 4, wy], [wb[0] + wb[2] * 0.5, wy + 5], [wb[0] + wb[2] - 10, wy - 2]], dur: 0.6, width: 7, color: BONE, filter: pf, seed: 362, jitter: 6, blend: "normal" });
    })();

    /* =================== C6S037 · 180.95–183.11 · left out hanging =================== */
    scene("sc037", 180.95, 183.18);
    ground("night", S(180.95));
    (function () {
      const svg = $("sc037-svg");
      svg.innerHTML = `<g transform="translate(780 260) scale(1.6)"><g fill="none" stroke="${BONE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" opacity="0.9">
          <path d="M58 20 L58 128 M162 20 L162 128 M50 20 L170 20 M58 70 L162 70"/><path d="M40 128 L180 128 L172 150 L48 150 Z" fill="rgba(242,237,227,0.08)"/>
          <path d="M54 150 L46 232 M166 150 L174 232 M74 150 L72 212 M146 150 L148 212"/></g>
        <g id="c6s01-sc037-plate"><rect x="52" y="160" width="116" height="38" fill="${BONE}"/><text x="110" y="188" text-anchor="middle" fill="${INK}" font-size="26" class="t-label" style="letter-spacing:0.14em">CHINA</text></g></g>`;
      tl.fromTo($("sc037-cam"), { x: 0 }, { x: 40, duration: 2.3, ease: "none", immediateRender: true }, S(180.95));
      tl.fromTo($("sc037-plate"), { y: 0, opacity: 1 }, { y: -320, opacity: 0, duration: 1.0, ease: C(E.in, 1.0), immediateRender: true }, S(181.0));
      tl.fromTo($("sc037-vig"), { opacity: 0.4 }, { opacity: 1, duration: 2.1, ease: "none", immediateRender: true }, S(180.95));
      [T(180.89), T(181.21), T(181.53)].forEach((c, i) => rise(words("sc037-lh")[i], c, { dur: 0.6, y: 10 }));
    })();
    whip($("sc037-shot"), $("sc038-shot"), S(183.11), { dir: 1, vertical: true, flash: true });

    /* =================== C6S038 · 183.11–188.63 · by the night of the UN vote … the shock dissipates a bit =================== */
    scene("sc038", 183.11, 188.65);
    ground("night", S(183.11));
    (function () {
      tl.fromTo($("sc038-cam"), { y: -40, scale: 1.08 }, { y: 60, scale: 1.12, duration: 5.6, ease: "none", immediateRender: true }, S(183.11));
      gated(183.0, 188.7, () => FX.streaks($("sc038-st"), { seed: 381, speed: 0.4, tint: [170, 200, 255], gain: 0.9 }));
      [T(183.77), T(184.01), T(184.33), T(184.49), T(184.65), T(185.21)].forEach((c, i) => rise(words("sc038-nt")[i], c, { dur: 0.5, y: 6 }));
      tl.fromTo($("sc038-sh"), { opacity: 0, y: 14, filter: "blur(6px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, T(186.89));
      tl.to($("sc038-sh"), { opacity: 0, scale: 1.16, filter: "blur(16px)", duration: 0.65, ease: E.in }, S(187.43));
    })();

    /* =================== C6S039 · 188.63–193.56 · This is when the leader, Chiang Kai-shek =================== */
    scene("sc039", 188.63, 193.63);
    ground("paper", S(188.63));
    (function () {
      const cam = $("sc039-cam");
      tl.fromTo($("sc039-card"), { opacity: 0, y: 70, rotation: 2 }, { opacity: 1, y: 0, rotation: -2, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(188.66));
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.05, duration: 4.9, ease: "none", immediateRender: true }, S(188.63));
      FX.focusHunt(tl, $("sc039-card"), S(190.4), { dur: 0.8, base: "drop-shadow(0 24px 34px rgba(20,27,36,0.35))" });
      [T(189.05), T(189.21)].forEach((c, i) => rise(words("sc039-tl")[i], c, { dur: 0.5, y: 8 }));
      show($("sc039-nmb"), T(189.77));
      [T(189.77), T(190.25)].forEach((c, i) => show(words("sc039-nm")[i], c));
      // torn edge (static, deterministic)
      const r = FX.rng(3901), pts = [];
      for (let i = 0; i <= 20; i++) pts.push(`${(i * 5).toFixed(1)}% ${(r() * 1.6).toFixed(2)}%`);
      for (let i = 0; i <= 26; i++) pts.push(`${(100 - r() * 1.3).toFixed(2)}% ${(i * 100 / 26).toFixed(1)}%`);
      for (let i = 20; i >= 0; i--) pts.push(`${(i * 5).toFixed(1)}% ${(100 - r() * 1.6).toFixed(2)}%`);
      for (let i = 26; i >= 0; i--) pts.push(`${(r() * 1.3).toFixed(2)}% ${(i * 100 / 26).toFixed(1)}%`);
      $("sc039-paper").style.clipPath = `polygon(${pts.join(",")})`;
    })();
    whip($("sc039-shot"), $("sc040-shot"), S(193.56), { dir: -1 });

    /* =================== C6S040 · 193.56–196.76 · Puts out a statement that's still very famous in Taiwan =================== */
    scene("sc040", 193.56, 196.78);
    ground("night", S(193.56));
    (function () {
      const pl = $("sc040-plane");
      tl.fromTo(pl, { x: -153, y: 90, scale: 0.42, rotationX: 32, rotationZ: -4 }, { x: -153, y: 70, scale: 0.5, rotationX: 28, rotationZ: 2, duration: 3.3, ease: "none", immediateRender: true }, S(193.56));
      tl.fromTo($("sc040-cel"), { opacity: 0 }, { opacity: 0.86, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(193.70));
      gated(193.5, 196.8, () => FX.radioWaves($("sc040-svg"), 1268, 224, { rings: 4, max: 1300, period: 1.5, width: 14, color: BONE, from: S(194.02), to: S(196.9) }));
      $("sc040-svg").insertAdjacentHTML("beforeend", `<circle cx="1268" cy="224" r="22" fill="${BONE}"/>`);
      rise($("sc040-st"), T(193.98), { dur: 0.6, y: 8 });
      [T(194.86), T(195.02)].forEach((c, i) => rise(words("sc040-vf")[i], c, { dur: 0.6, y: 10 }));
      show($("sc040-twr"), T(195.50));
      ul($("sc040-twu"), S(195.6), 0.4);
    })();

    /* =================== C6S041 · 196.76–201.96 · stay dignified and strengthen ourselves. Keep on fighting. (scroll) =================== */
    scene("sc041", 196.76, SEG_END);
    ground("paper", S(196.76));
    (function () {
      const cam = $("sc041-cam");
      tl.fromTo($("sc041-scroll"), { scaleX: 0.02 }, { scaleX: 1, duration: 1.3, ease: C(E.out, 1.3), immediateRender: true }, S(196.80));
      tl.fromTo($("sc041-rod"), { x: 0 }, { x: 1420, duration: 1.3, ease: C(E.out, 1.3), immediateRender: true }, S(196.80));
      tl.fromTo(cam, { scale: 1.07 }, { scale: 1.0, duration: 5.0, ease: E.cam, immediateRender: true }, S(196.76));
      const mk = $("sc041-mk"), pf = gated(198.1, 201.9, () => FX.markupDefs(mk, "c6s01-mk041", { boil: 4 }));
      const lw = words("sc041-l1");
      [T(198.22), T(198.70), T(199.34), T(199.50), T(200.14)].forEach((c, i) => {
        rise(lw[i], c, { dur: 0.4, y: 8 });
        const b = box(lw[i], cam), y = b[1] + b[3] - 2;
        FX.markup.pen(tl, mk, c + 0.05, { points: [[b[0] + 4, y], [b[0] + b[2] * 0.5, y + 4], [b[0] + b[2] - 22, y - 2]], dur: 0.32, width: 6, color: INK, filter: pf, seed: 411 + i, jitter: 3 });
      });
      const ch = gated(200.7, 201.6, () => FX.roughDefs(defs, "c6s01-ch041", { freq: 0.05, scale: 7, choke: 0 }));
      $("sc041-l2").style.filter = "url(#c6s01-ch041)";
      [T(200.86), T(201.10), T(201.26)].forEach((c, i) => show(words("sc041-l2")[i], c));
      FX.chokeSettle(tl, ch, $("sc041-l2"), T(200.86), 6, 0.42, "none");
      // whip ↑ first half (c6s02 lands the second half from below): smear upward, blur 40 px, overscale 1.08
      const bl = FX.whipDefs(defs, "c6s01-wout"), sb = { v: 0 };
      tl.set($("sc041-shot"), { filter: "url(#c6s01-wout)" }, S(201.79));
      tl.fromTo($("sc041-shot"), { y: 0, scale: 1 }, { y: -380, scale: 1.08, duration: 0.16, ease: "power3.in", immediateRender: false }, S(201.80));
      tl.fromTo(sb, { v: 0 }, { v: 40, duration: 0.16, ease: "power2.in", immediateRender: false, onUpdate: () => bl.setAttribute("stdDeviation", `0 ${sb.v.toFixed(1)}`) }, S(201.80));
    })();

    // layout is no longer needed: hide every scene outside its window (initial state), then mount
    SCENES.forEach((el, i) => { if (i) gsap.set(el, { autoAlpha: 0, display: "none" }); });
    FX.mount(tl, DURATION);
    window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
  })();
