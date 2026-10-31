    const SEG = "c5s03", SEG_START = 399.67, SEG_END = 598.03, DURATION = +(SEG_END - SEG_START).toFixed(2);
    const T = (s) => +(s - 399.67).toFixed(3);   // TEXT cues (audited) — literal word start − 0.06 (LOCAL c5 seconds)
    const S = (s) => +(s - 399.67).toFixed(3);   // STRUCTURAL cues (cuts, camera, objects)
    const tl = gsap.timeline({ paused: true });
    const $ = (id) => document.getElementById(SEG + "-" + id);
    const NS = "http://www.w3.org/2000/svg";
    const defs = $("defs");
    const E = FX.ease;
    const C = (e, d) => FX.choppy(e, d, 12);
    const BONE = "#f2ede3", INK = "#141b24", RED = "#e03f2c", CEL = "#9fc7b2", NAVY = "#1d5c9e", SKY = "#9fc3e3", YEL = "#f2d33b", PAPER = "#ebe4d6", GREY = "#9a958c";
    const SCENES = [];

    function gated(a, b, fn) { const on = FX.onFrame; FX.onFrame = (f) => on(FX.gate(S(a) - 0.1, S(b) + 0.1, f)); try { return fn(); } finally { FX.onFrame = on; } }
    // scene window [a, b] in LOCAL seconds; display:none outside (set at the very end, after every measuring call)
    function scene(id, a, b) {
      const el = $(id); SCENES.push(el);
      if (a <= SEG_START + 0.001) gsap.set(el, { autoAlpha: 1, display: "block" });
      else tl.fromTo(el, { autoAlpha: 0, display: "none" }, { autoAlpha: 1, display: "block", duration: 0.001, immediateRender: false }, S(a));
      if (b < SEG_END) tl.set(el, { autoAlpha: 0, display: "none" }, S(b));
      el._first = a <= SEG_START + 0.001;
    }
    function ground(kind, t) {
      const v = kind === "paper" ? [0.32, 0.14, 0.26] : [1, 0.42, 0.36];
      tl.set([$("vig"), $("dust"), $("grain")], { opacity: (i) => v[i] }, t);
    }
    const show = (el, t) => tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t);
    const hide = (el, t, d) => tl.to(el, { opacity: 0, duration: d || 0.4, ease: "power1.in" }, t);
    const rise = (el, t, o) => { o = o || {}; const d = o.dur || 1.0;
      tl.fromTo(el, { opacity: 0, y: o.y == null ? 22 : o.y }, { opacity: 1, y: 0, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const pop = (el, t, d) => { d = d || 0.8; tl.fromTo(el, { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: d, ease: C(E.out, d), immediateRender: true }, t); };
    const words = (id) => $(id).querySelectorAll(".k-w");
    const cam = (el, from, to, t, d, ease) => tl.fromTo(el, from, Object.assign({ duration: d, ease: ease || "none", immediateRender: false }, to), t);
    const whipN = { n: 0 };
    function whip(a, b, t, o) {
      o = Object.assign({ dir: 1, vertical: false, flash: false, dur: 0.32 }, o);
      const k = ++whipN.n, ba = FX.whipDefs(defs, `${SEG}-wa${k}`), bb = FX.whipDefs(defs, `${SEG}-wb${k}`), h = o.dur / 2;
      tl.set(a, { filter: `url(#${SEG}-wa${k})` }, t - h - 0.01); tl.set(a, { filter: "none" }, t + 0.06);
      tl.set(b, { filter: `url(#${SEG}-wb${k})` }, t - 0.001); tl.set(b, { filter: "none" }, t + h + 0.02);
      FX.whip(tl, a, b, t, { dir: o.dir, vertical: o.vertical, dur: o.dur, blurA: ba, blurB: bb });
      if (o.flash) tl.fromTo($("flash"), { opacity: 0 }, { opacity: 0.85, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.in", immediateRender: false }, t - 0.08);
    }
    // PS = paper slide with a torn leading edge: the incoming shot slides in over the outgoing one (scene b starts at t-0.25)
    const TORN = (() => { const r = FX.rng(777), p = []; for (let i = 0; i <= 24; i++) p.push(`${(r() * 34).toFixed(1)}px ${(i / 24 * 100).toFixed(2)}%`); return `polygon(${p.join(",")}, 100% 100%, 100% 0%)`; })();
    function paperSlide(a, b, t, o) {
      o = Object.assign({ d: 0.5 }, o);
      tl.set(b, { clipPath: TORN, boxShadow: "-30px 0 50px rgba(0,0,0,0.45)" }, t - o.d / 2 - 0.001);
      tl.fromTo(b, { x: 1960 }, { x: 0, duration: o.d, ease: C(E.inOut, o.d), immediateRender: false }, t - o.d / 2);
      tl.to(a, { x: -260, duration: o.d, ease: E.in }, t - o.d / 2);
      tl.set(b, { clipPath: "none", boxShadow: "none" }, t + o.d / 2 + 0.01);
    }
    // PT = push-through: the outgoing shot accelerates into the frame, the incoming lands from an over-scale
    function pushThrough(a, b, t) {
      tl.to(a, { scale: 1.7, filter: "blur(6px)", duration: 0.32, ease: E.in }, t - 0.32);
      tl.fromTo(b, { scale: 1.3, filter: "blur(8px)" }, { scale: 1, filter: "blur(0px)", duration: 0.5, ease: E.cam, immediateRender: false }, t);
      tl.set(b, { filter: "none" }, t + 0.52);
    }
    function ink(parent, d, t, dur, o) {
      o = o || {};
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d); p.setAttribute("fill", "none");
      p.setAttribute("stroke", o.color || INK); p.setAttribute("stroke-width", o.width || 6);
      p.setAttribute("stroke-linecap", o.cap || "round"); p.setAttribute("stroke-linejoin", "round");
      if (o.filter) p.setAttribute("filter", o.filter);
      if (o.opacity) p.setAttribute("opacity", o.opacity);
      if (o.blend) p.style.mixBlendMode = o.blend;
      parent.appendChild(p);
      const len = p.getTotalLength() || 1;
      p.setAttribute("stroke-dasharray", `${len} ${len}`); p.setAttribute("stroke-dashoffset", len);
      tl.fromTo(p, { attr: { "stroke-dashoffset": len } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: o.ease || C(E.out, dur), immediateRender: true }, t);
      p._len = len; return p;
    }
    function svgEl(parent, tag, attrs) { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); parent.appendChild(e); return e; }
    function markDefs(svg, id, vb, boil) { const f = FX.markupDefs(svg, id, { boil: boil || 4 }); svg.setAttribute("viewBox", vb); return f; }
    // UN hemicycle of member dots (c4 spec: 5 rows [r, n] = 300/14 … 580/26, r 14, grey) → [{x,y,a,el}] sorted clockwise
    function hemi(svg, cx, cy, pre, o) {
      o = Object.assign({ k: 1, r: 14 }, o);
      const rows = [[300, 14], [370, 17], [440, 20], [510, 23], [580, 26]], dots = [];
      rows.forEach(([r, n]) => { for (let k = 0; k < n; k++) { const a = Math.PI - k / (n - 1) * Math.PI; dots.push({ a, x: cx + Math.cos(a) * r * o.k, y: cy - Math.sin(a) * r * o.k }); } });
      dots.sort((p, q) => q.a - p.a);
      svg.insertAdjacentHTML("beforeend", `<path d="M${cx - 640 * o.k} ${cy + 30} L${cx + 640 * o.k} ${cy + 32}" stroke="${INK}" stroke-width="3" opacity="0.55"/>`);
      dots.forEach((d, i) => { d.el = svgEl(svg, "circle", { id: `${pre}${i}`, cx: d.x.toFixed(1), cy: d.y.toFixed(1), r: o.r * o.k, fill: GREY }); });
      return dots;
    }
    // the shared 'CHINA' chair icon (c4 motif) — ink chair, cushion element returned for colouring
    function chair(svg, x, y, sc, id, o) {
      o = o || {};
      const g = svgEl(svg, "g", { id, transform: `translate(${x} ${y}) scale(${sc})` });
      const inner = svgEl(g, "g", {});
      inner.innerHTML = `<g fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" ${o.dash ? 'stroke-dasharray="14 12"' : ""}>
          <path d="M58 20 L58 128 M162 20 L162 128 M50 20 L170 20 M58 70 L162 70"/>
          <path d="M54 150 L46 232 M166 150 L174 232 M74 150 L72 212 M146 150 L148 212"/></g>
        <path class="cush" d="M40 128 L180 128 L172 150 L48 150 Z" fill="${o.fill || "#e2dccd"}" stroke="${INK}" stroke-width="7" stroke-linejoin="round" ${o.dash ? 'stroke-dasharray="14 12"' : ""}/>` +
        (o.plate ? `<rect x="52" y="160" width="116" height="38" fill="${INK}"/><text x="110" y="188" text-anchor="middle" fill="${PAPER}" font-size="26" class="t-label" style="letter-spacing:0.14em">CHINA</text>` : "");
      return { g, inner, cush: inner.querySelector(".cush") };
    }

    // shared filters
    FX.tintDefs(defs, "c5s03-tint-ink", "#1d1f22", "#e9e1cf");
    FX.tintDefs(defs, "c5s03-tint-night", "#0e1013", "#c4bcae");
    FX.tintDefs(defs, "c5s03-tint-bone", "#2f2b27", "#efe7d6");
    FX.tintDefs(defs, "c5s03-tint-redp", "#7d1c11", "#efe3d0");
    defs.insertAdjacentHTML("beforeend", `
      <pattern id="c5s03-ht-red" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="22" height="22" fill="${RED}" opacity="0.55"/><circle cx="11" cy="11" r="6.2" fill="${RED}"/></pattern>
      <pattern id="c5s03-ht-cel" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="${CEL}" opacity="0.75"/><circle cx="7" cy="7" r="3.4" fill="#6f9c86" opacity="0.6"/></pattern>`);
    FX.grain($("grain"), 8401);
    FX.dust($("dust"), 8402, 2);

    /* =================== C5S084 · 399.67–405.11 · Of course, this does not really mean that US is not supporting Taiwan anymore =================== */
    scene("sc084", 399.67, 405.11);
    ground("night", 0);
    (function () {
      // lands from c5s02's light-flash whip (smear up, seed 8400): flash decays, panels drift up
      const sh = $("sc084-shot"), bb = FX.whipDefs(defs, "c5s03-win0");
      gsap.set($("flash"), { opacity: 0.85 });
      tl.fromTo($("flash"), { opacity: 0.85 }, { opacity: 0, duration: 0.2, ease: "power2.out", immediateRender: true }, 0);
      gsap.set(sh, { y: 380, scale: 1.18, filter: "url(#c5s03-win0)" });
      const sb = { v: 90 };
      tl.fromTo(sh, { y: 380, scale: 1.18 }, { y: 0, scale: 1, duration: 0.18, ease: "power3.out", immediateRender: true }, 0);
      tl.fromTo(sb, { v: 90 }, { v: 0, duration: 0.18, ease: "power2.out", immediateRender: true, onUpdate: () => bb.setAttribute("stdDeviation", `0 ${sb.v.toFixed(1)}`) }, 0);
      tl.set(sh, { filter: "none" }, 0.2);
      cam($("sc084-map"), { y: 70 }, { y: -60 }, 0, 5.44);
      cam($("sc084-ike"), { y: 110 }, { y: -30 }, 0, 5.44);
      cam($("sc084-badge"), { y: 160, rotation: 9 }, { y: -40, rotation: 5 }, 0, 5.44);
      cam($("sc084-tw"), { y: 140 }, { y: -20 }, 0, 5.44);
      cam($("sc084-bg"), { y: 40 }, { y: -40 }, 0, 5.44);
      cam($("sc084-cam"), { scale: 1.0 }, { scale: 1.04 }, 0, 5.0);
      tl.to($("sc084-cam"), { scale: 1.1, duration: 0.45, ease: E.in }, S(404.66));      // CA: push accelerates into the cut
      pop($("sc084-notb"), T(400.65), 0.9);
      [T(402.49), T(402.81)].forEach((c, i) => rise(words("sc084-sup")[i], c, { dur: 1.0, y: 14 }));
      tl.fromTo($("sc084-tw"), { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, T(402.81));
    })();

    /* =================== C5S085 · 405.11–411.11 · every time US wants anything, China wants give up support of Taiwan =================== */
    scene("sc085", 405.11, 411.40);
    (function () {
      const svg = $("sc085-svg");
      cam($("sc085-cam"), { scale: 1.0 }, { scale: 1.06 }, S(405.11), 6.3);
      tl.fromTo($("sc085-cam"), { y: 30 }, { y: 0, duration: 0.6, ease: E.cam, immediateRender: false }, S(405.11));   // CA: still settling from the push
      // anchors: US west coast (right), China (left), Taiwan (celadon dot)
      svg.insertAdjacentHTML("beforeend", `<circle id="c5s03-f-us" cx="1760" cy="500" r="14" fill="${BONE}" opacity="0"/><circle id="c5s03-f-cn" cx="250" cy="470" r="14" fill="${RED}" opacity="0"/>
        <circle id="c5s03-f-tw" cx="300" cy="700" r="13" fill="${CEL}" opacity="0"/>`);
      ["f-us", "f-cn", "f-tw"].forEach((k, i) => tl.fromTo($(k), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(405.3) + i / 12));
      tl.fromTo([$("sc085-us"), $("sc085-cn")], { opacity: 0 }, { opacity: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(405.35));
      // the existing link: US support of Taiwan (two halves so it can snap in the middle)
      const sA = ink(svg, "M1760 520 C 1500 860, 1080 900, 940 860", S(405.9), 0.7, { color: CEL, width: 12, cap: "butt", ease: C(E.inOut, 0.7) });
      const sB = ink(svg, "M300 700 C 520 820, 760 860, 940 860", S(406.0), 0.7, { color: CEL, width: 12, cap: "butt", ease: C(E.inOut, 0.7) });
      // flow 1: US → China "anything" (neutral bone)
      ink(svg, "M1760 480 C 1350 210, 700 200, 270 450", S(407.40), 1.1, { color: BONE, width: 44, cap: "butt", opacity: 0.8, ease: C(E.inOut, 1.1) });
      rise(words("sc085-any")[0], T(407.93), { dur: 0.9, y: 14 });
      // flow 2: China → US, red
      ink(svg, "M270 500 C 700 690, 1250 690, 1760 520", S(408.60), 1.0, { color: RED, width: 44, cap: "butt", opacity: 0.9, ease: C(E.inOut, 1.0) });
      [T(409.61), T(409.93)].forEach((c, i) => rise(words("sc085-give")[i], c, { dur: 0.7, y: 10 }));
      // the celadon strand snaps on "give up" — both halves retract from the break
      [sA, sB].forEach((p, i) => tl.to(p, { attr: { "stroke-dashoffset": p._len }, y: 26, duration: 0.42, ease: C(E.in, 0.42) }, S(409.70) + i * 0.04));
      const sp = svgEl(svg, "g", { opacity: 0 });
      sp.innerHTML = `<path d="M925 835 L905 810 M955 835 L975 808 M940 885 L940 912" stroke="${BONE}" stroke-width="5" stroke-linecap="round"/>`;
      tl.fromTo(sp, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(409.72));
      tl.set(sp, { attr: { opacity: 0 } }, S(409.98));
      show($("sc085-sotb"), T(410.09));
      [T(410.09), T(410.41), T(410.57)].forEach((c, i) => rise(words("sc085-sot")[i], c, { dur: 0.35, y: 8 }));
    })();
    paperSlide($("sc085-shot"), $("sc086-shot"), S(411.11));

    /* =================== C5S086 · 411.11–415.43 · That's what China is always asking for. And that's exactly why Taiwan is worried =================== */
    scene("sc086", 410.86, 415.53);
    ground("paper", S(411.11));
    (function () {
      const rows = $("sc086-rows"), r = FX.rng(8601);
      for (let i = 0; i < 7; i++) {
        let f = ""; let x = 90;
        while (x < 560) { const w = 60 + r() * 120; f += `<div class="k-filler" style="left:${x}px;top:${52}px;width:${Math.min(w, 600 - x)}px"></div>`; x += w + 18; }
        rows.insertAdjacentHTML("beforeend", `<div class="k-row" style="top:${70 + i * 140}px"><div class="n t-serif">${i + 1}.</div>${f}<div class="k-hlbar hl" id="c5s03-sc086-hl${i}"></div><div class="tw t-serif" style="position:absolute">Taiwan</div></div>`);
      }
      cam($("sc086-cam"), { y: 0, scale: 1.02 }, { y: -150, scale: 1.06 }, S(410.86), 4.7, E.cam);
      [T(412.01), T(412.49)].forEach((c, i) => rise(words("sc086-aa")[i], c, { dur: 0.9, y: 12 }));
      [0, 2, 4].forEach((k, i) => tl.fromTo($("sc086-hl" + k), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "sine.inOut", immediateRender: true }, S(412.05) + i * 0.5));
      // the repeated item is only legible once he says "Taiwan" (focus pull) — the strokes mark it again and again before that
      const tws = $("sc086-rows").querySelectorAll(".tw");
      gsap.set(tws, { filter: "blur(5px)", opacity: 0.6 });
      tl.to(tws, { filter: "blur(0px)", opacity: 1, duration: 0.2, ease: "power1.out" }, T(414.01));
      tl.fromTo($("sc086-worb"), { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.35, ease: C(E.out, 0.35), immediateRender: true }, T(414.73));
    })();
    whip($("sc086-shot"), $("sc087-shot"), S(415.43), { dir: -1 });

    /* =================== C5S087 · 415.43–418.79 · Oh, by the way, one important thing I completely forgot to mention so far =================== */
    scene("sc087", 415.43, 418.95);
    ground("night", S(415.43));
    (function () {
      cam($("sc087-cam"), { scale: 1.0 }, { scale: 1.07 }, S(415.43), 3.5, E.cam);
      const scr = $("sc087-scr");
      tl.fromTo(scr, { scaleY: 0.012 }, { scaleY: 1, duration: 0.2, ease: "power3.out", immediateRender: true }, S(415.50));
      tl.fromTo($("sc087-pw"), { opacity: 1 }, { opacity: 0, duration: 0.3, ease: "power2.out", immediateRender: true }, S(415.55));
      tl.fromTo($("sc087-trk"), { y: -60 }, { y: 450, duration: 0.42, ease: "none", repeat: 7, immediateRender: true }, S(415.6));
      tl.fromTo($("sc087-ff"), { opacity: 1 }, { opacity: 0.15, duration: 0.25, ease: "steps(1)", repeat: 12, yoyo: true, immediateRender: true }, S(415.6));
      [T(417.37), T(417.77), T(417.93)].forEach((c, i) => rise(words("sc087-fm")[i], c, { dur: 0.7, y: 10 }));
    })();
    whip($("sc087-shot"), $("sc088-shot"), S(418.79), { dir: 1, flash: true });

    /* =================== C5S088 · 418.79–423.19 · which is also kind of tells you why Taiwanese got so freaked out over this =================== */
    scene("sc088", 418.79, 423.19);
    ground("paper", S(418.79));
    (function () {
      const bars = $("sc088-bars"), r = FX.rng(8801);
      let h = `<div style="position:absolute;left:60px;right:60px;top:40px;height:4px;background:rgba(20,27,36,0.8)"></div><div style="position:absolute;left:60px;right:60px;top:52px;height:2px;background:rgba(20,27,36,0.8)"></div>`;
      h += `<div class="bar" style="left:70px;top:90px;width:1040px;height:86px"></div><div class="bar" style="left:70px;top:196px;width:760px;height:86px"></div>`;
      bars.innerHTML = h;
      let b = "";
      for (let col = 0; col < 2; col++) for (let i = 0; i < 26; i++) {
        const y = (col === 0 ? 880 : 330) + i * 26; if (col === 1 && i === 11) continue;
        if (y > 1450) continue;
        b += `<div class="k-filler" style="left:${col === 0 ? -680 : 0}px;top:${y - 330}px;width:${col === 0 ? 300 + r() * 340 : 300 + r() * 100}px;height:9px"></div>`;
      }
      $("sc088-body").innerHTML = b;
      $("sc088-body").insertAdjacentHTML("beforeend", `<div class="k-filler" style="left:160px;top:${11 * 26 + 2}px;width:240px;height:9px"></div>`);
      cam($("sc088-cam"), { scale: 1.0, x: 0, y: 0 }, { scale: 1.75, x: -470, y: -430 }, S(418.79), 3.8, E.cam);
      tl.to($("sc088-cam"), { scale: 1.82, x: -500, y: -455, duration: 0.6, ease: "none" }, S(422.59));
      tl.fromTo($("sc088-photo").querySelector(".k-ht"), { backgroundSize: "160px auto" }, { backgroundSize: "260px auto", duration: 4.4, ease: "none", immediateRender: true }, S(418.79));
      const kw = $("sc088-key").querySelector("span:last-child");
      gsap.set(kw, { filter: "blur(4px)", opacity: 0.5 });
      tl.to(kw, { filter: "blur(0px)", opacity: 1, duration: 0.2, ease: "power1.out" }, T(420.81));
      tl.fromTo($("sc088-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "sine.inOut", immediateRender: true }, S(420.81));
      [T(421.93), T(422.25)].forEach((c, i) => rise(words("sc088-fo")[i], c, { dur: 0.7, y: 10 }));
    })();

    /* =================== C5S089–C5S090 · 423.19–430.86 · two times Mao Zedong's China tried invading Taiwan … islands … the mainland =================== */
    scene("sc089", 423.19, 431.11);
    ground("night", S(423.19));
    (function () {
      const camEl = $("sc089-cam"), svg = $("sc089-svg");
      const at = (cx, cy, s) => ({ x: 960 - cx * s, y: 540 - cy * s, scale: s });
      gsap.set(camEl, at(2010, 2060, 0.52));
      tl.fromTo(camEl, at(2010, 2060, 0.52), Object.assign(at(1930, 2010, 0.565), { duration: 4.1, ease: "none", immediateRender: false }), S(423.19));
      const f = gated(423.1, 431.2, () => markDefs(svg, "c5s03-mk089", "0 0 3840 4096", 4));
      const a1 = FX.markup.arrow(tl, svg, S(423.81), { x1: 760, y1: 1880, x2: 2430, y2: 2330, bend: -220, head: 90, dur: 1.0, color: RED, width: 24, filter: f });
      const a2 = FX.markup.arrow(tl, svg, S(424.40), { x1: 1640, y1: 600, x2: 2900, y2: 1330, bend: -200, head: 90, dur: 1.0, color: RED, width: 24, filter: f });
      pop($("sc089-twob"), T(423.77), 0.8);
      rise(words("sc089-times")[0], T(423.93), { dur: 0.8, y: 10 });
      [T(424.33), T(424.73), T(425.53)].forEach((c, i) => rise(words("sc089-mao")[i], c, { dur: 0.8, y: 10 }));
      rise(words("sc089-inv")[0], T(426.17), { dur: 0.8, y: 10 });
      // C5S090 — zoom to Kinmen; contrast call-out cut at the push's peak velocity
      hide([$("sc089-two"), $("sc089-times"), $("sc089-mao"), $("sc089-inv")], S(427.27), 0.4);
      tl.to([...a1, ...a2], { attr: { opacity: 0.25 }, duration: 0.5, ease: "power1.in" }, S(427.27));
      tl.to(camEl, Object.assign(at(950, 1830, 1.25), { duration: 1.3, ease: C(E.inOut, 1.3) }), S(427.30));
      FX.contrastCallout(tl, $("sc089-veil"), S(427.95), { w: 3840, h: 4096, ellipse: [905, 1868, 150, 115], feather: 34, color: "rgba(150,150,146,1)", strength: 0.55 });
      FX.focusHunt(tl, camEl, S(428.62), { dur: 0.8 });
      FX.markup.circle(tl, svg, S(428.60), { cx: 905, cy: 1868, rx: 140, ry: 100, rot: -8, dur: 0.6, color: BONE, width: 9, filter: f, seed: 901 });
      svg.insertAdjacentHTML("beforeend", `<text id="c5s03-sc090-kin" x="1060" y="1990" class="t-label" font-size="27" fill="${BONE}" opacity="0" style="letter-spacing:0.18em">KINMEN</text>`);
      tl.fromTo($("sc090-kin"), { attr: { opacity: 0 } }, { attr: { opacity: 0.95 }, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(428.75));
      gated(428.5, 431.0, () => FX.radioWaves(svg, 790, 1840, { rings: 3, max: 170, period: 1.0, width: 10, color: RED, from: S(428.65), to: S(430.95) }));
      tl.fromTo($("sc090-inset"), { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(428.95));
      tl.fromTo($("sc090-im"), { scale: 1.0 }, { scale: 1.15, duration: 2.0, ease: "none", immediateRender: false }, S(428.95));
      [T(428.57), T(428.65)].forEach((c, i) => rise(words("sc090-isl")[i], c, { dur: 0.8, y: 10 }));
      [T(430.16), T(430.24)].forEach((c, i) => rise(words("sc090-ml")[i], c, { dur: 0.35, y: 8 }));
      tl.to(camEl, Object.assign(at(930, 1845, 1.3), { duration: 2.3, ease: "none" }), S(428.6));
    })();
    paperSlide($("sc089-shot"), $("sc091-shot"), S(430.86));

    /* =================== C5S091 · 430.86–434.06 · and you know if he succeeds, he would probably keep moving forward =================== */
    scene("sc091", 430.61, 434.22);
    ground("paper", S(430.86));
    (function () {
      const svg = $("sc091-svg");
      cam($("sc091-cam"), { x: 0, y: -430 }, { x: -110, y: -560 }, S(430.61), 3.6, E.cam);
      svg.insertAdjacentHTML("beforeend", `<defs><mask id="c5s03-m091" maskUnits="userSpaceOnUse" x="0" y="0" width="1400" height="1849"><path id="c5s03-m091p" d="M372 1060 C 470 1010, 560 1020, 640 1090 S 760 1200, 812 1196" fill="none" stroke="white" stroke-width="30" stroke-linecap="round"/></mask></defs>
        <path d="M372 1060 C 470 1010, 560 1020, 640 1090 S 760 1200, 812 1196" fill="none" stroke="${RED}" stroke-width="11" stroke-dasharray="26 16" stroke-linecap="round" mask="url(#c5s03-m091)"/>`);
      const mp = $("m091p"), len = mp.getTotalLength();
      mp.setAttribute("stroke-dasharray", `${len} ${len}`);
      tl.fromTo(mp, { attr: { "stroke-dashoffset": len } }, { attr: { "stroke-dashoffset": 0 }, duration: 1.2, ease: C(E.inOut, 1.2), immediateRender: true }, S(431.90));
      const head = svgEl(svg, "path", { d: "M780 1168 L 822 1197 L 778 1222", fill: "none", stroke: RED, "stroke-width": 11, "stroke-linecap": "round", "stroke-linejoin": "round", opacity: 0 });
      tl.fromTo(head, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(433.10));
      show($("sc091-kbg"), T(433.04));
      [T(433.04), T(433.20), T(433.52)].forEach((c, i) => rise(words("sc091-kmf")[i], c, { dur: 0.5, y: 10 }));
    })();
    whip($("sc091-shot"), $("sc092-shot"), S(434.06), { dir: 1, vertical: true });

    /* =================== C5S092–C5S093 · 434.06–445.50 · US sent a aircraft carrier through the Taiwan Strait … don't mess with Taiwan =================== */
    scene("sc092", 434.06, 445.50);
    ground("night", S(434.06));
    (function () {
      const wrap = $("sc092-wrap"), a = $("sc092-a"), b = $("sc092-b"), svg = $("sc092-svg");
      const P = [1950, 1900], M = 1.43;
      gsap.set(b, { x: 960 - P[0] * M, y: 540 - P[1] * M, scale: M, opacity: 0 });
      cam(a, { scale: 1.0 }, { scale: 1.1 }, S(434.06), 4.84);
      FX.curveCut(tl, wrap, a, b, S(438.90), 1.4, { from: 1, to: 0.37 });
      tl.to(wrap, { scale: 0.345, duration: 5.1, ease: "none" }, S(440.30));
      [T(438.40), T(439.04)].forEach((c, i) => rise(words("sc092-ac")[i], c, { dur: 0.6, y: 10 }));
      hide($("sc092-ac"), S(440.0), 0.4);
      tl.set($("sc092-cr1"), { opacity: 0 }, S(439.6)); tl.set($("sc092-cr2"), { opacity: 1 }, S(439.6));
      [T(439.76), T(440.48)].forEach((c, i) => rise(words("sc092-ts")[i], c, { dur: 0.5, y: 10 }));
      // the carrier = a bone dot; its route north through the Strait in yellow marker (D14)
      const f = gated(439.5, 445.6, () => markDefs(svg, "c5s03-mk092", "0 0 3840 4096", 12));
      const route = ink(svg, "M1950 1900 C 2120 1520, 2260 1160, 2560 640", S(441.40), 1.4, { color: YEL, width: 34, filter: f, ease: C(E.inOut, 1.4), opacity: 0.92 });
      const dot = svgEl(svg, "circle", { cx: P[0], cy: P[1], r: 24, fill: BONE, opacity: 0 });
      const halo = svgEl(svg, "circle", { cx: P[0], cy: P[1], r: 24, fill: "none", stroke: BONE, "stroke-width": 6, opacity: 0 });
      tl.fromTo(dot, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(439.6));
      tl.fromTo(halo, { attr: { r: 24, opacity: 0.9 } }, { attr: { r: 90, opacity: 0 }, duration: 0.9, ease: "power2.out", repeat: 2, immediateRender: false }, S(439.7));
      const st = { p: 0 };
      tl.fromTo(st, { p: 0 }, { p: 1, duration: 1.4, ease: C(E.inOut, 1.4), immediateRender: false, onUpdate: () => { const q = route.getPointAtLength(st.p * route._len); dot.setAttribute("cx", q.x.toFixed(1)); dot.setAttribute("cy", q.y.toFixed(1)); } }, S(441.40));
      hide($("sc092-ts"), S(442.6), 0.4);
      tl.fromTo([$("sc092-tw"), $("sc092-twg")], { opacity: 0 }, { opacity: 1, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(443.80));
      [T(443.04), T(443.36), T(443.60), T(443.76)].forEach((c, i) => rise(words("sc093-dm")[i], c, { dur: 0.8, y: 12 }));
    })();

    /* =================== C5S094 · 445.50–450.38 · So now that US is talking with China … =================== */
    scene("sc094", 445.50, 450.54);
    ground("paper", S(445.50));
    (function () {
      cam($("sc094-cam"), { scale: 1.07, y: 18 }, { scale: 1.0, y: 0 }, S(445.50), 1.4, E.cam);
      tl.to($("sc094-cam"), { scale: 1.05, duration: 3.5, ease: "none" }, S(446.9));
      [T(446.64), T(447.04), T(447.20)].forEach((c, i) => rise(words("sc094-twc")[i], c, { dur: 0.9, y: 10 }));
    })();
    whip($("sc094-shot"), $("sc095-shot"), S(450.38), { dir: -1, vertical: true });

    /* =================== C5S095 · 450.38–454.22 · Taiwan is getting a little worried, not sure what the future holds =================== */
    scene("sc095", 450.38, 454.38);
    ground("night", S(450.38));
    (function () {
      cam($("sc095-cam"), { scale: 1.0 }, { scale: 1.07 }, S(450.38), 4.0);
      cam($("sc095-fog1"), { x: -900, y: -260 }, { x: -300, y: -240 }, S(450.38), 4.0);
      cam($("sc095-fog2"), { x: 500, y: -500, rotation: 90 }, { x: -100, y: -470, rotation: 90 }, S(450.38), 4.0);
      FX.focusHunt(tl, $("sc095-cam"), S(450.60), { dur: 0.8 });
      rise(words("sc095-wor")[0], T(451.44), { dur: 0.9, y: 10 });
      [T(452.80), T(452.96)].forEach((c, i) => rise(words("sc095-fut")[i], c, { dur: 0.8, y: 12 }));
    })();
    whip($("sc095-shot"), $("sc096-shot"), S(454.22), { dir: 1, flash: true });
