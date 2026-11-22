/* US vs Cartels — recurring motifs, built once (window.CT). Depends only on gsap + lib/fx.js (+ palette_cartels.css tokens).
   Loaded by tools/build_index.py / build_master.py for compositions whose id starts with "ct" (after lib/fx.js).
   Deterministic (no Math.random / Date — FX.rng only), NO layout measuring (paths use pathLength="100", positions are
   fixed geometry), seek-safe (fromTo + immediateRender:false; hidden states set with gsap.set outside the timeline).
   Every `t` is a COMPOSITION-LOCAL second (pass T(master) for text cues / S(master) for structure from your segment).
   Call the constructors BEFORE FX.mount (boiling filters register with FX.onFrame; pass gate:[a,b] = your scene window).
   Docs + snippets: project/cartels/MOTIFS.md. CSS: lib/ct_motifs.css (classes ctm-*). Demo: compositions/ctmotif.html.

   CT.deal(root, o)     THE DEAL — America finds | Mexico arrests, split by "the line"
   CT.file(root, o)     TARGET FILE — manila dossier: photo, name, alias, typed rows, rubber stamp
   CT.dateTag(root, o)  place · date stamp for footage
   CT.credit(root, text, o)  on-screen source credit (bottom-left, 22 px) */
(function () {
  const CT = window.CT || {};
  const NS = "http://www.w3.org/2000/svg";
  const E = () => FX.ease;
  const C = (e, d) => FX.choppy(e, d, 12);
  const FALLBACK = { "--ink": "#1d1a16", "--sepia-light": "#ece2cf", "--ember-dark": "#8a3311", "--steel-dark": "#2f4a63",
    "--olive-dark": "#50512a", "--ash-dark": "#3b3631" };
  const tok = (n) => (getComputedStyle(document.documentElement).getPropertyValue(n).trim() || FALLBACK[n] || "#808080");
  const hex = (h) => { h = h.replace("#", ""); if (h.length === 3) h = h.split("").map((c) => c + c).join(""); return [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16)); };
  const mixHex = (a, b, k) => { const A = hex(a), B = hex(b); return "#" + A.map((v, i) => Math.round(v + (B[i] - v) * k).toString(16).padStart(2, "0")).join(""); };
  const esc = (s) => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  function svgEl(parent, tag, attrs) {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  // stroke drawn on with dashoffset; pathLength 100 → no getTotalLength
  function strokeP(svg, d, color, width, filter) {
    const p = svgEl(svg, "path", { d, fill: "none", "stroke-width": width, "stroke-linecap": "round", "stroke-linejoin": "round",
      pathLength: 100, "stroke-dasharray": "100 100", "stroke-dashoffset": 0 });
    p.style.stroke = color;
    if (filter) p.setAttribute("filter", filter);
    return p;
  }
  function hideStroke(p) { gsap.set(p, { opacity: 0, attr: { "stroke-dashoffset": 100 } }); }
  function drawOn(tl, p, t, dur, ease) {
    hideStroke(p);
    tl.fromTo(p, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: false }, t);
    tl.fromTo(p, { attr: { "stroke-dashoffset": 100 } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: ease || C(E().out, dur), immediateRender: false }, t);
  }
  const circ = (cx, cy, r) => `M${cx} ${cy - r} A${r} ${r} 0 1 1 ${cx - 0.01} ${cy - r}`;
  const ell = (cx, cy, rx, ry) => `M${cx - rx} ${cy} A${rx} ${ry} 0 1 1 ${cx + rx} ${cy} A${rx} ${ry} 0 1 1 ${cx - rx} ${cy}`;

  // Per-instance filter bank (all ids prefixed). Boiling turbulences carry class ctm-bt and step at `boil` per second, gated.
  function defsFor(root, P, o) {
    const defs = svgEl(null, "svg", { width: 0, height: 0, "aria-hidden": "true", class: "ctm-defs" });
    root.appendChild(defs);
    const boilT = [];
    const api = {
      el: defs,
      // rough reveal for HTML panels (erode = choke + displaced edge); returns the morphology node
      rough(id, scale) {
        defs.insertAdjacentHTML("beforeend", `<filter id="${P}-${id}" x="-6%" y="-6%" width="112%" height="112%" color-interpolation-filters="sRGB">
          <feMorphology id="${P}-${id}-m" operator="erode" radius="0" in="SourceGraphic" result="ch"/>
          <feTurbulence class="ctm-bt" type="fractalNoise" baseFrequency="0.028" numOctaves="3" seed="2" result="n"/>
          <feDisplacementMap in="ch" in2="n" scale="${scale || 16}" xChannelSelector="R" yChannelSelector="G"/></filter>`);
        boilT.push(...defs.querySelectorAll(`#${P}-${id} .ctm-bt`));
        return document.getElementById(`${P}-${id}-m`);
      },
      // marker line filter in a 1920x1080 user space (straight strokes never vanish)
      marker(id, s1, s2) {
        defs.insertAdjacentHTML("beforeend", `<filter id="${P}-${id}" filterUnits="userSpaceOnUse" x="-60" y="-60" width="2040" height="1200" color-interpolation-filters="sRGB">
          <feTurbulence class="ctm-bt" type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="3" result="n1"/>
          <feDisplacementMap in="SourceGraphic" in2="n1" scale="${s1}" xChannelSelector="R" yChannelSelector="G" result="d1"/>
          <feTurbulence class="ctm-bt" type="fractalNoise" baseFrequency="0.24" numOctaves="1" seed="5" result="n2"/>
          <feDisplacementMap in="d1" in2="n2" scale="${s2}" xChannelSelector="R" yChannelSelector="G"/></filter>`);
        boilT.push(...defs.querySelectorAll(`#${P}-${id} .ctm-bt`));
        return `url(#${P}-${id})`;
      },
      // rubber-stamp ink: speckled holes + uneven inking + slightly ragged edge (static, deterministic)
      ink(id) {
        defs.insertAdjacentHTML("beforeend", `<filter id="${P}-${id}" x="-4%" y="-8%" width="108%" height="116%" color-interpolation-filters="sRGB">
          <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="11" result="ed"/>
          <feDisplacementMap in="SourceGraphic" in2="ed" scale="5" xChannelSelector="R" yChannelSelector="G" result="rg"/>
          <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="2" seed="4" result="sp"/>
          <feColorMatrix in="sp" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -4.2 0 0 0 3.0" result="spa"/>
          <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="8" result="pt"/>
          <feColorMatrix in="pt" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -2.6 0 0 0 2.2" result="pta"/>
          <feComposite in="spa" in2="pta" operator="arithmetic" k1="1" k2="0" k3="0" k4="0" result="holes"/>
          <feComposite in="rg" in2="holes" operator="in"/></filter>`);
        return `url(#${P}-${id})`;
      },
      // photo duotone: blacks → dark, whites → light
      duo(id, dark, light) {
        const c = (h) => hex(h).map((v) => (v / 255).toFixed(3));
        const d = c(dark), l = c(light);
        defs.insertAdjacentHTML("beforeend", `<filter id="${P}-${id}" color-interpolation-filters="sRGB">
          <feColorMatrix type="saturate" values="0"/>
          <feComponentTransfer><feFuncR type="gamma" amplitude="1" exponent="0.9" offset="0"/><feFuncG type="gamma" amplitude="1" exponent="0.9" offset="0"/><feFuncB type="gamma" amplitude="1" exponent="0.9" offset="0"/></feComponentTransfer>
          <feComponentTransfer><feFuncR type="table" tableValues="${d[0]} ${l[0]}"/><feFuncG type="table" tableValues="${d[1]} ${l[1]}"/><feFuncB type="table" tableValues="${d[2]} ${l[2]}"/></feComponentTransfer></filter>`);
        return `url(#${P}-${id})`;
      },
      startBoil() {
        if (!boilT.length) return;
        const rate = o.boil || 8;
        const fn = (t) => { const k = Math.floor(t * rate) % 7; boilT.forEach((n, i) => n.setAttribute("seed", 3 + ((k + i * 3) % 9))); };
        FX.onFrame(o.gate ? FX.gate(o.gate[0], o.gate[1], fn) : fn);
      },
    };
    return api;
  }
  // a rough reveal that settles (MANUAL §10.1.2): rough filter on during the reveal, erode radius → 0, clean after
  function roughReveal(tl, el, morph, filterUrl, t, dur, from) {
    const s = { r: from };
    gsap.set(el, { filter: "none" });
    tl.fromTo(el, { filter: filterUrl }, { filter: filterUrl, duration: 0.001, immediateRender: false }, t - 0.001);
    tl.fromTo(s, { r: from }, { r: 0, duration: dur, ease: C("power2.out", dur), immediateRender: false,
      onUpdate: () => morph.setAttribute("radius", s.r.toFixed(2)) }, t);
    tl.fromTo(el, { filter: filterUrl }, { filter: "none", duration: 0.001, immediateRender: false }, t + dur + 1 / 12);
  }
  // deterministic shake (stamp impact)
  function shake(tl, el, t, amp, seed) {
    const r = FX.rng(seed || 5), n = 6;
    for (let i = 0; i < n; i++) {
      const k = 1 - i / n, last = i === n - 1;
      tl.to(el, { x: last ? 0 : (r() - 0.5) * 2 * amp * k, y: last ? 0 : (r() - 0.5) * 1.4 * amp * k, rotation: last ? 0 : (r() - 0.5) * 0.5 * k,
        duration: 1 / 24, ease: "none" }, t + i / 24);
    }
    return t + n / 24;
  }

  // =====================================================================================
  // ICONS (viewBox 0 0 200 200), hand-drawn on as strokes
  // =====================================================================================
  CT.ICONS = {
    // surveillance eye inside a reticle (drone / ISR) — "America finds". spin = reticle (turns on focus), core = the eye
    find: {
      spin: [circ(100, 100, 74), "M100 6 L100 40", "M100 160 L100 194", "M6 100 L40 100", "M160 100 L194 100",
        "M62 38 L50 38 L50 50", "M138 38 L150 38 L150 50", "M62 162 L50 162 L50 150", "M138 162 L150 162 L150 150"],
      core: ["M44 100 C66 66 134 66 156 100 C134 134 66 134 44 100"],
      dot: [100, 100, 17],
    },
    // handcuffs — "Mexico arrests"
    arrest: {
      spin: [],
      core: [circ(56, 132, 38), circ(144, 132, 38), circ(56, 132, 24), circ(144, 132, 24),
        "M44 96 L44 78 L68 78 L68 96", "M132 96 L132 78 L156 78 L156 96",
        ell(77, 66, 11, 7), ell(100, 60, 11, 7), ell(123, 66, 11, 7)],
      dot: null,
    },
  };
  function drawIcon(svg, kind, color, width) {
    const ic = CT.ICONS[kind], g = svgEl(svg, "g", {}), spin = svgEl(g, "g", {}), core = svgEl(g, "g", {}), parts = [];
    ic.spin.forEach((d) => parts.push(strokeP(spin, d, color, width)));
    ic.core.forEach((d) => parts.push(strokeP(core, d, color, width)));
    let dot = null;
    if (ic.dot) { dot = svgEl(core, "circle", { cx: ic.dot[0], cy: ic.dot[1], r: ic.dot[2] }); dot.style.fill = color; }
    return { g, spin, core, parts, dot };
  }

  // =====================================================================================
  // MOTIF 1 — THE DEAL
  // =====================================================================================
  CT.deal = function (root, o) {
    o = Object.assign({ prefix: "ctdeal", ground: "night", compact: false, kicker: "The deal", lineLabel: null, labels: {},
      bandTop: null, gate: null, boil: 8 }, o);
    const P = o.prefix, L = Object.assign({}, CT.deal.defaults, o.labels);
    const paperG = o.ground === "paper";
    const G = o.compact ? { top: o.bandTop != null ? o.bandTop : 1080 - 140 - 300, h: 300 } : { top: 206, h: 744 };
    G.mid = G.top + G.h / 2;
    root.classList.add("ctm-deal");
    if (o.compact) root.classList.add("ctm-compact");
    root.classList.add(paperG ? "ctm-on-paper" : "ctm-on-night");
    let ground = "";
    if (o.ground === "night") ground = `<div class="ctm-gnight"></div><div class="ctm-gtex" style="background-image:url('assets/textures/halftone_02_norm.jpg')"></div>`;
    else if (paperG) ground = `<div class="ctm-gpaper"></div><div class="ctm-gp1" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div><div class="ctm-gp2" style="background-image:url('assets/textures/paper_stained_01_hires.jpg')"></div>`;
    const panel = (k, side, cls, left) => `
      <div class="ctm-pan ${cls}" id="${P}-p${k}" style="left:${left}px; top:${G.top}px; height:${G.h}px">
        <div class="ctm-pfill"></div><div class="ctm-ppat"></div>
        <div class="ctm-ptex" style="background-image:url('assets/textures/halftone_01_norm.jpg')"></div>
        ${k === "a" ? `<div class="ctm-wash" id="${P}-wash"></div>` : ""}
        <div class="ctm-bar"></div>
        <div class="ctm-ico"><svg id="${P}-i${k}" viewBox="0 0 200 200"></svg></div>
        <div class="ctm-txt"><div class="ctm-who t-label" id="${P}-w${k}">${esc(L[side + "Who"])}</div>
          <div class="ctm-verb t-display" id="${P}-v${k}">${esc(L[side + "Verb"])}</div></div>
        <div class="ctm-dim" id="${P}-d${k}"></div>
      </div>`;
    root.innerHTML = `${ground}
      <div class="ctm-shk" id="${P}-shk">
        ${o.kicker ? `<div class="ctm-kick t-label" id="${P}-kick" style="top:${G.top - (o.compact ? 58 : 96)}px"><i></i>${esc(o.kicker)}<i></i></div>` : ""}
        ${panel("f", "find", "ctm-steel", 96)}
        ${panel("a", "arrest", "ctm-olive", 1008)}
        <svg class="ctm-lsvg" id="${P}-lsvg" viewBox="0 0 1920 1080"></svg>
        ${o.lineLabel ? `<div class="ctm-llab t-label" id="${P}-llab" style="top:${G.top + G.h + (o.compact ? 18 : 30)}px"><span>${esc(o.lineLabel)}</span></div>` : ""}
        <div class="ctm-drone" id="${P}-drone"><svg viewBox="0 0 200 200" id="${P}-dsvg"></svg></div>
        <div class="ctm-sdim" id="${P}-sdim"></div>
        <div class="ctm-stw" id="${P}-stw" style="top:${G.mid - (o.compact ? 70 : 100)}px"><div class="ctm-stamp t-display" id="${P}-st"><span id="${P}-stt"></span></div></div>
      </div>`;
    const D = defsFor(root, P, o);
    const $ = (id) => document.getElementById(P + "-" + id);
    const mF = D.rough("rf", 18), mA = D.rough("ra", 18);
    const lineF = D.marker("ln", 6, 2.2), lineX = D.marker("lnx", 22, 4);
    const inkF = D.ink("ink");
    D.startBoil();
    $("st").style.filter = inkF;
    const pf = $("pf"), pa = $("pa");
    gsap.set([pf, pa], { transformOrigin: "50% 50%" });

    // icons
    const icW = o.compact ? 9 : 7;
    const icF = drawIcon($("if"), "find", "var(--steel-light)", icW);
    const icA = drawIcon($("ia"), "arrest", "var(--olive-light)", icW);
    // the line (hand-drawn, never perfectly straight)
    const lsvg = $("lsvg"), r = FX.rng(19), y0 = G.top - (o.compact ? 14 : 22), y1 = G.top + G.h + (o.compact ? 26 : 40);
    const pts = [];
    for (let y = y0; y <= y1; y += 48) pts.push([960 + (r() - 0.5) * 3.2 + (y - y0) * 0.0025, y]);
    pts[pts.length - 1][1] = y1;
    const lineCol = paperG ? "var(--ink)" : "var(--bone)";
    const lineEl = strokeP(lsvg, "M" + pts.map((q) => q[0].toFixed(1) + " " + q[1].toFixed(1)).join(" L"), lineCol, o.compact ? 5 : 6, lineF);
    // cross: trail (quadratic) + drone marker
    // full: from the reticle's right edge, over the line, to beside the cuffs; compact: across the band's middle
    const X = o.compact ? { x0: 700, y0: G.mid - 10, cx: 960, cy: G.mid - 100, x1: 1220, y1: G.mid - 10 }
                        : { x0: 720, y0: G.top + 236, cx: 960, cy: G.top + 150, x1: 1200, y1: G.top + 236 };
    const trail = strokeP(lsvg, `M${X.x0} ${X.y0} Q${X.cx} ${X.cy} ${X.x1} ${X.y1}`, "var(--steel-light)", o.compact ? 4 : 5, lineF);
    trail.setAttribute("stroke-dasharray", "100 100");
    hideStroke(trail);
    const yAtLine = (X.y0 + 2 * X.cy + X.y1) / 4;   // quadratic at t = 0.5 (x0/x1 symmetric about 960 only approximately)
    const ck = o.compact ? 0.7 : 1;
    const cracks = [[-34, -22, -58, -20], [30, -30, 44, -56], [36, 16, 64, 24], [-28, 26, -40, 56], [8, -40, -6, -70]].map((c) =>
      strokeP(lsvg, `M960 ${yAtLine} L${960 + c[0] * ck} ${yAtLine + c[1] * ck} L${960 + c[2] * ck} ${yAtLine + c[3] * ck}`, lineCol, o.compact ? 3.5 : 5, lineF));
    cracks.forEach(hideStroke);
    const dr = drawIcon($("dsvg"), "find", "var(--steel-light)", 12);
    gsap.set($("drone"), { opacity: 0 });
    gsap.set($("sdim"), { opacity: 0 });
    gsap.set($("stw"), { opacity: 0 });

    const api = { el: root, prefix: P, panels: { find: pf, arrest: pa }, line: lineEl };
    let focused = null;

    // build: kicker, line, panels choke in from the line outward, icons draw on, labels + verbs land.
    // bo.find / bo.arrest = text cues (T()) — each panel's VERB lands exactly on its cue; the panel starts 0.5 s earlier.
    api.build = function (tl, t, bo) {
      bo = bo || {};
      const tf = bo.find != null ? bo.find - 0.5 : t + 0.25, ta = bo.arrest != null ? bo.arrest - 0.5 : t + 0.55;
      const k = $("kick");
      if (k) { gsap.set(k, { clipPath: "inset(0% 50% 0% 50%)" });
        tl.fromTo(k, { clipPath: "inset(0% 50% 0% 50%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.9, ease: C(E().out, 0.9), immediateRender: false }, t); }
      drawOn(tl, lineEl, t + 0.05, 1.0, C(E().inOut, 1.0));
      const lb = $("llab");
      if (lb) { gsap.set(lb, { opacity: 0 }); tl.fromTo(lb, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, t + 0.8); }
      [[pf, mF, "rf", tf, "inset(0% 0% 0% 100%)", 46, icF, "f"], [pa, mA, "ra", ta, "inset(0% 100% 0% 0%)", -46, icA, "a"]].forEach(([el, m, fid, ts, clip, dx, ic, s]) => {
        const d = 1.2;
        gsap.set(el, { clipPath: clip });
        tl.fromTo(el, { clipPath: clip, x: dx }, { clipPath: "inset(0% 0% 0% 0%)", x: 0, duration: d, ease: C(E().out, d), immediateRender: false }, ts);
        roughReveal(tl, el, m, `url(#${P}-${fid})`, ts, d * 0.75, 7);
        ic.parts.forEach((p, i) => drawOn(tl, p, ts + 0.35 + i * 0.05, 0.6, C(E().out, 0.6)));
        if (ic.dot) { gsap.set(ic.dot, { opacity: 0 }); tl.fromTo(ic.dot, { opacity: 0, scale: 0, svgOrigin: "100 100" }, { opacity: 1, scale: 1, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, ts + 0.6); }
        const w = $("w" + s), v = $("v" + s);
        gsap.set([w, v], { opacity: 0 });
        tl.fromTo(w, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.7, ease: C(E().out, 0.7), immediateRender: false }, ts + 0.4);
        tl.fromTo(v, { opacity: 0, y: 34 }, { opacity: 1, y: 0, duration: 1.0, ease: C(E().out, 1.0), immediateRender: false }, ts + 0.5);
      });
      return Math.max(tf, ta) + 1.5;
    };

    // focus: punch the chosen half, dim + shrink the other. which = 'find' | 'arrest' | null (both back to normal)
    api.focus = function (tl, t, which) {
      const d = 1.2;
      const on = which === "find" ? pf : which === "arrest" ? pa : null;
      [[pf, $("df"), "find"], [pa, $("da"), "arrest"]].forEach(([el, dim, k]) => {
        const sel = !which || k === which;
        tl.to(dim, { opacity: sel ? 0 : 0.62, duration: 0.6, ease: C(E().out, 0.6) }, t);
        tl.to(el, { scale: !which ? 1 : sel ? 1.035 : 0.965, duration: d, ease: C(E().out, d) }, t);
      });
      if (which === "find") {   // the reticle turns and the eye's pupil pulses
        tl.fromTo(icF.spin, { rotation: 0, svgOrigin: "100 100" }, { rotation: 90, duration: 1.1, ease: C(E().out, 1.1), immediateRender: false }, t);
        if (icF.dot) tl.fromTo(icF.dot, { scale: 1, svgOrigin: "100 100" }, { scale: 1.5, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, t + 0.15);
      } else if (which === "arrest") {   // the cuffs snap shut
        tl.fromTo(icA.g, { rotation: -10, scale: 1.12, svgOrigin: "100 120" }, { rotation: 0, scale: 1, duration: 0.8, ease: C(E().out, 0.8), immediateRender: false }, t);
      }
      focused = which; void on;
      return t + d;
    };

    // cross: a steel drone marker crosses the line into the olive half; the line cracks and boils; a steel wash floods in
    api.cross = function (tl, t, co) {
      co = co || {};
      const dur = co.dur || 1.6, drone = $("drone"), half = 0.5;
      const pos = (u) => { const a = (1 - u) * (1 - u), b = 2 * u * (1 - u), c = u * u; return [a * X.x0 + b * X.cx + c * X.x1, a * X.y0 + b * X.cy + c * X.y1]; };
      const s = { u: 0 }, size = o.compact ? 84 : 120;
      const place = () => { const [x, y] = pos(s.u); gsap.set(drone, { x: x - size / 2, y: y - size / 2 }); };
      gsap.set(drone, { width: size, height: size }); place();
      tl.fromTo(drone, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: C(E().out, 0.4), immediateRender: false }, t);
      tl.fromTo(s, { u: 0 }, { u: 1, duration: dur, ease: C(E().inOut, dur), immediateRender: false, onUpdate: place }, t + 0.15);
      tl.fromTo(dr.g, { rotation: 0, svgOrigin: "100 100" }, { rotation: 180, duration: dur + 0.6, ease: C(E().out, dur + 0.6), immediateRender: false }, t);
      drawOn(tl, trail, t + 0.15, dur, C(E().inOut, dur));
      const tc = t + 0.15 + dur * half;   // inOut ease is symmetric → the marker is on the line at the time midpoint
      gsap.set(lineEl, { attr: { filter: lineF } });
      tl.fromTo(lineEl, { attr: { filter: lineF } }, { attr: { filter: lineX }, duration: 0.001, immediateRender: false }, tc - 0.08);
      tl.fromTo(lineEl, { attr: { filter: lineX } }, { attr: { filter: lineF }, duration: 0.001, immediateRender: false }, tc + 1.1);
      cracks.forEach((c, i) => drawOn(tl, c, tc + i * 0.04, 0.22, C(E().out, 0.22)));
      const w = $("wash");
      gsap.set(w, { clipPath: "inset(0% 100% 0% 0%)", opacity: 0 });
      tl.fromTo(w, { clipPath: "inset(0% 100% 0% 0%)", opacity: 0 }, { clipPath: "inset(0% 0% 0% 0%)", opacity: 1, duration: 1.4, ease: C(E().out, 1.4), immediateRender: false }, tc);
      return tc + 1.4;
    };

    // rubber stamp over the whole board (e.g. "OFFICIALLY"); so.color = palette token name (default bone on night, ink on paper)
    api.stamp = function (tl, t, text, so) {
      so = so || {};
      const st = $("st"), w = $("stw");
      $("stt").textContent = text || "OFFICIALLY";
      st.style.color = `var(${so.color || (paperG ? "--ink" : "--bone")})`;
      const rot = so.rotation != null ? so.rotation : -7;
      tl.fromTo($("sdim"), { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "power1.out", immediateRender: false }, t - 0.1);
      tl.fromTo(w, { opacity: 0, scale: 1.8, rotation: rot - 9 }, { opacity: 1, scale: 1, rotation: rot, duration: 0.125, ease: "power2.in", immediateRender: false }, t);
      tl.fromTo(w, { scale: 1 }, { scale: 1.02, duration: 0.6, ease: "power1.out", immediateRender: false }, t + 0.125);
      shake(tl, $("shk"), t + 0.125, o.compact ? 6 : 10, 23);
      return t + 0.9;
    };
    api.unstamp = function (tl, t) {
      tl.to($("stw"), { opacity: 0, duration: 0.3, ease: "power1.in" }, t);
      tl.to($("sdim"), { opacity: 0, duration: 0.4, ease: "power1.in" }, t);
      return t + 0.4;
    };

    // out: panels fold back into the line, everything else fades (the ground stays — it is the scene's)
    api.out = function (tl, t, d) {
      d = d || 0.6;
      tl.to(pf, { clipPath: "inset(0% 0% 0% 100%)", x: 30, duration: d, ease: E().in }, t);
      tl.to(pa, { clipPath: "inset(0% 100% 0% 0%)", x: -30, duration: d, ease: E().in }, t);
      const rest = [lineEl, trail, $("drone"), $("stw"), $("sdim"), $("kick"), $("llab")].concat(cracks).filter(Boolean);
      tl.to(rest, { opacity: 0, duration: d * 0.8, ease: E().in }, t + d * 0.2);
      return t + d;
    };
    return api;
  };
  CT.deal.defaults = { findWho: "America", findVerb: "Finds", arrestWho: "Mexico", arrestVerb: "Arrests" };

  // =====================================================================================
  // MOTIF 2 — TARGET FILE (manila dossier on sand paper)
  // =====================================================================================
  CT.STAMPS = {
    wanted: { text: "WANTED", cls: "k-wanted" },
    captured: { text: "CAPTURED", cls: "k-captured" },
    killed: { text: "KILLED", cls: "k-killed" },
    run: { text: "ON THE RUN", cls: "k-run" },
  };
  CT.STAMPS.ontherun = CT.STAMPS.run; CT.STAMPS["on the run"] = CT.STAMPS.run;
  CT.fileGeom = { W: 1240, H: 760 };
  CT.file = function (root, o) {
    o = Object.assign({ prefix: "ctfile", ground: "paper", photo: null, photoPos: "50% 30%", name: "", alias: null, rows: [],
      accent: "ember", tilt: -1.4, scale: 1.06, x: 960, y: 548, kicker: "Target file", tag: null, stampAt: null, gate: null }, o);
    const P = o.prefix, Gm = CT.fileGeom, acc = ["ember", "steel", "olive"].indexOf(o.accent) >= 0 ? o.accent : "ember";
    root.classList.add("ctm-fileroot", "ctm-acc-" + acc);
    let ground = "";
    if (o.ground === "paper") ground = `<div class="ctm-gpaper"></div><div class="ctm-gp1" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>` +
      `<div class="ctm-gp2" style="background-image:url('assets/textures/paper_stained_01_hires.jpg')"></div><div class="ctm-gdesk"></div>`;
    const rows = o.rows.map((rw) => (Array.isArray(rw) ? { label: rw[0], value: rw[1] } : rw));
    const rowsHtml = rows.map((rw, i) => `<div class="ctm-row" id="${P}-row${i}"><span class="ctm-rl t-label" id="${P}-rl${i}">${esc(rw.label)}</span>` +
      `<span class="ctm-rv t-label" id="${P}-rv${i}">${Array.from(String(rw.value)).map((ch) => `<span class="ctm-ch">${esc(ch)}</span>`).join("")}<span class="ctm-caret" id="${P}-cr${i}"></span></span></div>`).join("");
    const photo = o.photo
      ? `<div class="ctm-pimg"><img src="${o.photo}" style="object-position:${o.photoPos}" id="${P}-img"/><div class="ctm-pht" style="background-image:url('assets/textures/halftone_01_norm.jpg')"></div></div>`
      : `<div class="ctm-pimg ctm-nophoto"><svg viewBox="0 0 200 240"><circle cx="100" cy="92" r="40"/><path d="M28 240 C28 172 62 146 100 146 C138 146 172 172 172 240 Z"/></svg><div class="ctm-npl t-label">No photo</div></div>`;
    const name = esc(o.name);
    root.innerHTML = `${ground}
      <div class="ctm-fcam" id="${P}-cam"><div class="ctm-shk" id="${P}-shk">
        <div class="ctm-file" id="${P}-file" style="left:${o.x - Gm.W / 2}px; top:${o.y - Gm.H / 2}px">
          <div class="ctm-folder"><div class="ctm-ftex" style="background-image:url('assets/textures/paper_fiber_01.jpg')"></div></div>
          <div class="ctm-tab"><div class="ctm-ftex" style="background-image:url('assets/textures/paper_fiber_01.jpg')"></div><i></i></div>
          <div class="ctm-sheet" id="${P}-sheet">
            <div class="ctm-stex" style="background-image:url('assets/textures/paper_cream_02.jpg')"></div>
            <div class="ctm-hbar"><div class="ctm-ptex" style="background-image:url('assets/textures/halftone_01_norm.jpg')"></div></div>
            <div class="ctm-head" id="${P}-head"><span class="t-label ctm-kk">${esc(o.kicker || "")}</span>${o.tag ? `<span class="t-label ctm-tg">${esc(o.tag)}</span>` : ""}</div>
            <div class="ctm-photo" id="${P}-ph">${photo}</div>
            <svg class="ctm-clip" id="${P}-clip" viewBox="0 0 60 170"><path class="a" d="M20 44 V128 a11 11 0 0 0 22 0 V34 a17 17 0 0 0 -34 0 V134 a23 23 0 0 0 46 0 V56"/><path class="b" d="M20 44 V128 a11 11 0 0 0 22 0 V34 a17 17 0 0 0 -34 0 V134 a23 23 0 0 0 46 0 V56"/></svg>
            <div class="ctm-info">
              <div class="ctm-name t-display" id="${P}-name">${name}</div>
              ${o.alias ? `<div class="ctm-alias t-serif-i" id="${P}-alias">“${esc(o.alias)}”</div>` : ""}
              <div class="ctm-rule" id="${P}-rule"></div>
              <div class="ctm-rows">${rowsHtml}</div>
            </div>
            <div class="ctm-fstw" id="${P}-stw"><div class="ctm-fstamp t-display" id="${P}-st"><span id="${P}-stt"></span></div></div>
          </div>
        </div>
      </div></div>`;
    const D = defsFor(root, P, o);
    const $ = (id) => document.getElementById(P + "-" + id);
    const inkF = D.ink("ink");
    if (o.photo) {
      const dark = mixHex(tok("--ink"), tok("--" + acc + "-dark"), 0.8);
      $("img").style.filter = D.duo("duo", dark, tok("--sepia-light"));
    }
    $("st").style.filter = inkF;
    const file = $("file"), cam = $("cam");
    gsap.set(file, { rotation: o.tilt, scale: o.scale, transformOrigin: "50% 50%" });
    gsap.set($("ph"), { rotation: 2.4, transformOrigin: "50% 50%" });
    gsap.set($("clip"), { rotation: -6, transformOrigin: "50% 50%" });
    gsap.set(cam, { transformOrigin: "0px 0px" });
    gsap.set($("stw"), { opacity: 0 });
    if (o.stampAt) gsap.set($("stw"), { left: o.stampAt[0], top: o.stampAt[1], right: "auto" });
    const api = { el: root, prefix: P, file, cam, sheet: $("sheet") };

    api.open = function (tl, t, oo) {
      oo = oo || {};
      const d = 1.3;
      gsap.set(file, { opacity: 0 });
      tl.fromTo(file, { opacity: 0, y: 190, rotation: o.tilt - 4 }, { opacity: 1, y: 0, rotation: o.tilt, duration: d, ease: C(E().out, d), immediateRender: false }, t);
      tl.fromTo($("sheet"), { y: 70 }, { y: 0, duration: 1.2, ease: C(E().out, 1.2), immediateRender: false }, t + 0.3);
      const h = $("head");
      gsap.set(h, { clipPath: "inset(0% 100% 0% 0%)" });
      tl.fromTo(h, { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.8, ease: C(E().out, 0.8), immediateRender: false }, t + 0.5);
      const nm = $("name"), tn = oo.name != null ? oo.name : t + 0.6;
      gsap.set(nm, { clipPath: "inset(-10% 100% -10% 0%)" });
      tl.fromTo(nm, { clipPath: "inset(-10% 100% -10% 0%)", x: -16 }, { clipPath: "inset(-10% 0% -10% 0%)", x: 0, duration: 0.8, ease: C(E().out, 0.8), immediateRender: false }, tn);
      const al = $("alias");
      if (al) { const ta = oo.alias != null ? oo.alias : tn + 0.45; gsap.set(al, { opacity: 0 });
        tl.fromTo(al, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.8, ease: C(E().out, 0.8), immediateRender: false }, ta); }
      gsap.set($("rule"), { scaleX: 0 });
      tl.fromTo($("rule"), { scaleX: 0 }, { scaleX: 1, duration: 1.0, ease: C(E().out, 1.0), immediateRender: false }, tn + 0.3);
      return Math.max(t + d, tn + 1.3);
    };
    api.photo = function (tl, t) {
      const ph = $("ph"), cl = $("clip");
      gsap.set([ph, cl], { opacity: 0 });
      tl.fromTo(ph, { opacity: 0, y: -50, rotation: -5, scale: 1.1 }, { opacity: 1, y: 0, rotation: 2.4, scale: 1, duration: 1.0, ease: C(E().out, 1.0), immediateRender: false }, t);
      tl.fromTo(cl, { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.5, ease: C(E().out, 0.5), immediateRender: false }, t + 0.55);
      return t + 1.05;
    };
    // typewriter: label wipes in, then the value types char by char on 12 fps steps (ro.cps chars per second, default 24)
    api.row = function (tl, t, i, ro) {
      ro = ro || {};
      const row = $("row" + i);
      if (!row) throw new Error("CT.file.row: no row " + i);
      const chars = Array.from($("rv" + i).querySelectorAll(".ctm-ch")), caret = $("cr" + i), rl = $("rl" + i);
      const per = Math.max(1, Math.round((ro.cps || 24) / 12));
      gsap.set(rl, { clipPath: "inset(0% 100% 0% 0%)" });
      tl.fromTo(rl, { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.4, ease: C(E().out, 0.4), immediateRender: false }, t);
      gsap.set(chars, { display: "none" });
      gsap.set(caret, { display: "none" });
      const t0 = t + (ro.lead != null ? ro.lead : 0.15);
      tl.fromTo(caret, { display: "none" }, { display: "inline-block", duration: 0.001, immediateRender: false }, t0 - 0.08);
      chars.forEach((c, k) => tl.fromTo(c, { display: "none" }, { display: "inline", duration: 0.001, immediateRender: false }, t0 + Math.floor(k / per) / 12));
      const end = t0 + Math.floor((chars.length - 1) / per) / 12;
      tl.fromTo(caret, { display: "inline-block" }, { display: "none", duration: 0.001, immediateRender: false }, end + 0.4);
      return end + 0.1;
    };
    // the rubber stamp slams on (kind: wanted | captured | killed | run), small shake of the whole file
    api.stamp = function (tl, t, kind, text) {
      const k = CT.STAMPS[String(kind || "wanted").toLowerCase()] || CT.STAMPS.wanted;
      const st = $("st"), w = $("stw");
      $("stt").textContent = text || k.text;
      st.className = "ctm-fstamp t-display " + k.cls;
      tl.fromTo(w, { opacity: 0, scale: 1.9, rotation: -19 }, { opacity: 1, scale: 1, rotation: -10, duration: 0.125, ease: "power2.in", immediateRender: false }, t);
      shake(tl, $("shk"), t + 0.125, 9, 41);
      return t + 0.4;
    };
    // camera push toward a point of the frame (px, default the stamp area); smooth, never posterized
    api.pushIn = function (tl, t, scale, po) {
      po = po || {};
      const s = scale || 1.12, d = po.dur || 1.8, fx = po.x != null ? po.x : o.x + 260, fy = po.y != null ? po.y : o.y + 200;
      tl.to(cam, { scale: s, x: fx * (1 - s), y: fy * (1 - s), duration: d, ease: E().cam }, t);
      return t + d;
    };
    api.out = function (tl, t, d) {
      d = d || 0.7;
      tl.to(file, { y: 220, opacity: 0, rotation: o.tilt + 3, duration: d, ease: E().in }, t);
      return t + d;
    };
    return api;
  };

  // =====================================================================================
  // DATE / PLACE TAG for footage, and the SOURCE CREDIT
  // =====================================================================================
  CT.dateTag = function (root, o) {
    o = Object.assign({ prefix: "ctdate", place: "", date: "", pos: "tl", theme: "night", accent: null }, o);
    const P = o.prefix;
    root.classList.add("ctm-date", "ctm-pos-" + o.pos, o.theme === "paper" ? "ctm-on-paper" : "ctm-on-night");
    root.innerHTML = `<div class="ctm-dscrim"></div><div class="ctm-drule" id="${P}-rule"><i ${o.accent ? `style="background:var(--${o.accent})"` : ""}></i></div>` +
      `<div class="ctm-dtxt t-label" id="${P}-txt"><b>${esc(o.place)}</b>${o.place && o.date ? `<span class="ctm-dsep">·</span>` : ""}<span class="ctm-dd">${esc(o.date)}</span></div>`;
    const $ = (id) => document.getElementById(P + "-" + id);
    const api = { el: root, prefix: P };
    api.in = function (tl, t) {
      const ru = $("rule"), tx = $("txt"), sc = root.querySelector(".ctm-dscrim");
      gsap.set(ru, { scaleX: 0 }); gsap.set(tx, { clipPath: "inset(-20% 100% -20% 0%)" }); gsap.set(sc, { opacity: 0 });
      tl.fromTo(sc, { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.out", immediateRender: false }, t);
      tl.fromTo(ru, { scaleX: 0 }, { scaleX: 1, duration: 0.8, ease: C(E().out, 0.8), immediateRender: false }, t);
      tl.fromTo(tx, { clipPath: "inset(-20% 100% -20% 0%)", x: -26 }, { clipPath: "inset(-20% 0% -20% 0%)", x: 0, duration: 1.0, ease: C(E().out, 1.0), immediateRender: false }, t + 0.08);
      return t + 1.1;
    };
    api.out = function (tl, t, d) { d = d || 0.5; tl.to(root, { opacity: 0, x: -20, duration: d, ease: E().in }, t); return t + d; };
    return api;
  };
  CT.credit = function (root, text, o) {
    o = Object.assign({ theme: "night", pos: "bl" }, o);
    root.classList.add("ctm-credit", "ctm-pos-" + o.pos, o.theme === "paper" ? "ctm-on-paper" : "ctm-on-night");
    root.innerHTML = `<span class="t-label">${esc(text)}</span>`;
    const api = { el: root };
    api.in = function (tl, t) { gsap.set(root, { opacity: 0 }); tl.fromTo(root, { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.out", immediateRender: false }, t); return t + 0.5; };
    api.out = function (tl, t) { tl.to(root, { opacity: 0, duration: 0.4, ease: "power1.in" }, t); return t + 0.4; };
    return api;
  };

  window.CT = CT;
})();
