/* NVIDIA documentary — the two recurring motifs, built once (window.NV). Depends only on gsap + lib/fx.js.
   Loaded by tools/build_index.py / build_master.py for compositions whose id starts with "nv" (after lib/fx.js).
   Deterministic (no Math.random / Date), no layout measuring (paths use pathLength="100"), seek-safe.
   Every `t` is a COMPOSITION-LOCAL second (pass T(master)/S(master) from your segment).
   Call NV.scoreboard / NV.line BEFORE FX.mount (their marker boil registers with FX.onFrame).
   Docs + snippets: project/nvidia/MOTIFS.md. CSS: lib/nv_motifs.css (classes nvm-*). */
(function () {
  const NV = {};
  const NS = "http://www.w3.org/2000/svg";
  const E = () => FX.ease;
  const C = (e, d) => FX.choppy(e, d, 12);
  const tok = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  function svgEl(parent, tag, attrs) {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  // two marker filters (userSpaceOnUse so straight strokes never vanish): -mkc for 0..100 cell svgs, -mkl for 1920x1080 svgs
  function markFilters(root, P, o) {
    const defs = svgEl(null, "svg", { width: 0, height: 0, "aria-hidden": "true" });
    defs.style.position = "absolute"; defs.style.left = "0"; defs.style.top = "0";
    root.appendChild(defs);
    const f = (id, x, y, w, h, s1, s2) => `
      <filter id="${id}" filterUnits="userSpaceOnUse" x="${x}" y="${y}" width="${w}" height="${h}" color-interpolation-filters="sRGB">
        <feTurbulence class="nvm-t1" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3" result="n1"/>
        <feDisplacementMap in="SourceGraphic" in2="n1" scale="${s1}" xChannelSelector="R" yChannelSelector="G" result="d1"/>
        <feTurbulence class="nvm-t2" type="fractalNoise" baseFrequency="0.3" numOctaves="1" seed="5" result="n2"/>
        <feDisplacementMap in="d1" in2="n2" scale="${s2}" xChannelSelector="R" yChannelSelector="G"/>
      </filter>`;
    defs.innerHTML = f(P + "-mkc", -30, -30, 160, 160, 5, 2.2) +
      f(P + "-mkl", -60, -60, 2040, 1200, 7, 2.4).replace('baseFrequency="0.035"', 'baseFrequency="0.018"').replace('baseFrequency="0.3"', 'baseFrequency="0.22"');
    const t1 = defs.querySelectorAll(".nvm-t1"), t2 = defs.querySelectorAll(".nvm-t2");
    const boil = o.boil || 12;
    const fn = (t) => { const k = Math.floor(t * boil) % 7; t1.forEach((n) => n.setAttribute("seed", 3 + k)); t2.forEach((n) => n.setAttribute("seed", 11 + k)); };
    FX.onFrame(o.gate ? FX.gate(o.gate[0], o.gate[1], fn) : fn);
    return { cell: `url(#${P}-mkc)`, line: `url(#${P}-mkl)` };
  }
  // a path drawn on with dashoffset (pathLength 100 -> no measuring)
  function strokeP(svg, d, color, width, filter) {
    const p = svgEl(svg, "path", { d, fill: "none", "stroke-width": width, "stroke-linecap": "round", "stroke-linejoin": "round",
      pathLength: 100, "stroke-dasharray": "100 100", "stroke-dashoffset": 0 });
    p.style.stroke = color;
    if (filter) p.setAttribute("filter", filter);
    return p;
  }
  function drawOn(tl, p, t, dur, ease) {
    gsap.set(p, { opacity: 0, attr: { "stroke-dashoffset": 100 } });
    tl.set(p, { opacity: 1 }, t);
    tl.fromTo(p, { attr: { "stroke-dashoffset": 100 } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: ease || C(E().out, dur), immediateRender: false }, t);
  }

  // ---------------- result glyphs (viewBox 0 0 100 100), hand-marker strokes ----------------
  const GLYPH = {
    x: { color: "var(--red)", label: "NOT WORKING", paths: ["M22 21 C38 37 57 58 79 81", "M78 19 C61 37 41 59 21 82"], durs: [0.24, 0.24] },
    check: { color: "var(--volt)", label: "WORKING", paths: ["M16 55 C24 61 32 70 40 81 C51 58 66 35 87 15"], durs: [0.45] },
    q: { color: "var(--yellow)", label: "?", paths: ["M29 33 C29 17 43 9 54 10 C68 11 76 21 74 34 C72 47 54 50 52 63 L51 69"], durs: [0.5] },
  };

  // =====================================================================================
  // MOTIF 1 — THE SCOREBOARD
  // =====================================================================================
  NV.JOBS = ["Keep the chips out of China", "Keep America’s lead in AI", "Keep China hooked on American chips", "The renting loophole"];
  NV.scoreboard = function (root, o) {
    o = Object.assign({ prefix: "nvsb", state: {}, row4Text: null, compact: false, tally: null, kicker: "The chip ban — scoreboard",
      colHead: "Result", gate: null, boil: 12, sw: 11 }, o);
    const P = o.prefix, state = Object.assign({ 1: null, 2: null, 3: null, 4: null }, o.state);
    root.classList.add("nvm-sb");
    if (o.compact) root.classList.add("nvm-compact");
    const jobs = NV.JOBS.slice(); if (o.row4Text) jobs[3] = o.row4Text;
    const wordsHtml = (s) => s.split(" ").map((w, i, a) => `<span class="nvm-w">${w}${i < a.length - 1 ? " " : ""}</span>`).join("");
    let h = `<div class="nvm-head" id="${P}-head"><div class="nvm-kick t-label" id="${P}-kick"><i class="nvm-kdot"></i>${o.kicker}</div>` +
      `<div class="nvm-colh t-label" id="${P}-colh">${o.colHead}</div><div class="nvm-rule" id="${P}-rule"></div></div>`;
    for (let n = 1; n <= 4; n++) {
      const txt = n < 4 || o.row4Text ? jobs[n - 1] : "";
      h += `<div class="nvm-row" id="${P}-r${n}"><div class="nvm-bg"></div><div class="nvm-dash"></div>` +
        `<div class="nvm-tab t-label" id="${P}-tab${n}"><div class="nvm-tabfill" style="position:absolute; inset:0; background:var(--ice-dark)"></div>` +
        `<span class="nvm-tabk" style="position:relative">Job</span><span class="nvm-tabn" style="position:relative">${n}</span></div>` +
        `<div class="nvm-job t-display" id="${P}-job${n}"><div id="${P}-jt${n}">${wordsHtml(txt)}</div></div>` +
        `<div class="nvm-res" id="${P}-res${n}"><div class="nvm-tint" id="${P}-tint${n}"></div><div class="nvm-glow" id="${P}-glow${n}"></div>` +
        `<div class="nvm-slot" id="${P}-slot${n}"></div><svg class="nvm-mark" id="${P}-mark${n}" viewBox="0 0 100 100"></svg>` +
        `<div class="nvm-rl t-label" id="${P}-rl${n}"></div></div></div>`;
    }
    if (o.tally !== null) h += `<div class="nvm-tally" id="${P}-tally"><span class="nvm-tk t-label">Score</span><span class="nvm-tv t-display" id="${P}-tv">${o.tally}</span></div>`;
    root.innerHTML = h;
    const F = markFilters(root, P, o);
    const $ = (id) => document.getElementById(P + "-" + id);
    const rows = [1, 2, 3, 4].map((n) => $("r" + n));
    const row4Empty = !o.row4Text;
    if (row4Empty) {   // the empty fourth row: a dashed slot, no fill, ghost tab
      const r = rows[3];
      gsap.set(r.querySelector(".nvm-bg"), { opacity: 0 });
      gsap.set(r.querySelector(".nvm-dash"), { opacity: 1 });
      gsap.set(r.querySelector(".nvm-tabfill"), { opacity: 0 });
      gsap.set([r.querySelector(".nvm-tabk"), r.querySelector(".nvm-tabn")], { color: tok("--ash") });
      gsap.set($("res4"), { opacity: 0 });
    }
    const sw = o.sw;
    function buildMark(n, kind) {
      const g = GLYPH[kind], svg = $("mark" + n);
      svg.innerHTML = "";
      const paths = g.paths.map((d) => strokeP(svg, d, g.color, sw, F.cell));
      let dot = null;
      if (kind === "q") { dot = svgEl(svg, "circle", { cx: 51, cy: 86, r: sw * 0.62 }); dot.style.fill = g.color; }
      $("tint" + n).className = "nvm-tint " + kind;
      $("glow" + n).className = "nvm-glow " + kind;
      const rl = $("rl" + n); rl.className = "nvm-rl t-label " + kind; rl.textContent = kind === "q" ? "" : g.label;
      return { paths, dot, svg };
    }
    // earlier results, shown already stamped
    for (let n = 1; n <= 4; n++) if (state[n]) { buildMark(n, state[n]); gsap.set($("tint" + n), { opacity: 1 }); gsap.set($("slot" + n), { opacity: 0 }); }
    let lastGlow = null;
    const api = { el: root, rows, prefix: P };

    api.revealRow = function (tl, n, t, ro) {
      ro = ro || {};
      const r = rows[n - 1], d = ro.dur || 0.9;
      gsap.set(r, { clipPath: "inset(-40% 100% -40% 0%)" });
      tl.fromTo(r, { clipPath: "inset(-40% 100% -40% 0%)" }, { clipPath: "inset(-40% 0% -40% 0%)", duration: d, ease: C(E().out, d), immediateRender: false }, t);
      tl.fromTo($("tab" + n), { x: -36 }, { x: 0, duration: d, ease: C(E().out, d), immediateRender: false }, t);
      if (ro.words) {   // job text word by word on spoken cues
        const ws = Array.from($("jt" + n).querySelectorAll(".nvm-w"));
        gsap.set(ws, { opacity: 0 });
        ro.words.forEach((c, i) => ws[i] && tl.fromTo(ws[i], { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: C(E().out, 0.5), immediateRender: false }, c));
      }
      return t + d;
    };
    api.intro = function (tl, t0, io) {
      io = io || {};
      const d = 0.8;
      gsap.set($("kick"), { clipPath: "inset(0% 100% 0% 0%)" });
      tl.fromTo($("kick"), { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: d, ease: C(E().out, d), immediateRender: false }, t0);
      gsap.set($("rule"), { scaleX: 0 });
      tl.fromTo($("rule"), { scaleX: 0 }, { scaleX: 1, duration: 1.2, ease: C(E().out, 1.2), immediateRender: false }, t0 + 0.1);
      gsap.set($("colh"), { opacity: 0 });
      tl.fromTo($("colh"), { opacity: 0 }, { opacity: 1, duration: 0.4, ease: C(E().out, 0.4), immediateRender: false }, t0 + 0.5);
      const times = io.rows || [0, 1, 2, 3].map((i) => t0 + 0.45 + i * 0.4);
      let end = t0 + d;
      for (let n = 1; n <= 4; n++) end = Math.max(end, api.revealRow(tl, n, times[n - 1], { words: io.words && io.words[n - 1] }));
      if (o.tally !== null && $("tally") && io.tally !== false) { gsap.set($("tally"), { opacity: 0 }); }
      return end;
    };
    api.markRow = function (tl, n, kind, t) {
      const g = GLYPH[kind], m = buildMark(n, kind);
      let tt = t;
      m.paths.forEach((p, i) => { drawOn(tl, p, tt, g.durs[i], C(E().out, g.durs[i])); tt += g.durs[i] + 0.04; });
      if (m.dot) {
        gsap.set(m.dot, { opacity: 0, scale: 0, transformOrigin: "51px 86px" });
        tl.fromTo(m.dot, { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.3, ease: C(E().out, 0.3), immediateRender: false }, tt);
        tt += 0.3;
      }
      // settle: the mark lands a touch big and eases into its cell
      tl.fromTo(m.svg, { scale: 1.22, rotation: kind === "x" ? -4 : 3 }, { scale: 1, rotation: 0, duration: 0.9, ease: C(E().out, 0.9), immediateRender: false }, t);
      gsap.set($("slot" + n), { opacity: state[n] ? 0 : 1 });
      tl.to($("slot" + n), { opacity: 0, duration: 0.15, ease: "none" }, t);
      gsap.set($("tint" + n), { opacity: 0 });
      tl.fromTo($("tint" + n), { opacity: 0 }, { opacity: 1, duration: 0.4, ease: C(E().out, 0.4), immediateRender: false }, t + 0.1);
      const rl = $("rl" + n);
      gsap.set(rl, { clipPath: "inset(0% 100% 0% 0%)" });
      tl.fromTo(rl, { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, t + 0.2);
      // one hero glow: the newest stamp; the previous one dims
      if (lastGlow) tl.to(lastGlow, { opacity: 0, duration: 0.4, ease: "none" }, t);
      const gl = $("glow" + n);
      gsap.set(gl, { opacity: 0 });
      tl.fromTo(gl, { opacity: 0 }, { opacity: 1, duration: 0.25, ease: "power1.out", immediateRender: false }, t);
      tl.to(gl, { opacity: 0.4, duration: 1.4, ease: "power1.inOut" }, t + 0.5);
      lastGlow = gl; state[n] = kind;
      return Math.max(tt, t + 0.9);
    };
    api.fillRow4 = function (tl, text, t) {
      const r = rows[3], jt = $("jt4");
      jt.innerHTML = wordsHtml(text || NV.JOBS[3]);
      const ws = Array.from(jt.querySelectorAll(".nvm-w")), cues = Array.isArray(t) ? t : null, t0 = cues ? cues[0] : t;
      tl.to(r.querySelector(".nvm-dash"), { opacity: 0, duration: 0.5, ease: "power1.out" }, t0);
      tl.fromTo(r.querySelector(".nvm-bg"), { opacity: 0 }, { opacity: 1, duration: 0.7, ease: C(E().out, 0.7), immediateRender: false }, t0);
      tl.fromTo(r.querySelector(".nvm-tabfill"), { opacity: 0, scaleY: 0 }, { opacity: 1, scaleY: 1, duration: 0.7, ease: C(E().out, 0.7), immediateRender: false }, t0);
      tl.to([r.querySelector(".nvm-tabk")], { color: tok("--ice-light"), duration: 0.3 }, t0);
      tl.to([r.querySelector(".nvm-tabn")], { color: tok("--bone"), duration: 0.3 }, t0);
      tl.fromTo($("res4"), { opacity: 0, x: -24 }, { opacity: 1, x: 0, duration: 0.7, ease: C(E().out, 0.7), immediateRender: false }, t0 + 0.2);
      gsap.set(ws, { opacity: 0 });
      ws.forEach((w, i) => { const c = cues ? cues[i] : t + 0.15 + i * 0.12; if (c != null) tl.fromTo(w, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: C(E().out, 0.5), immediateRender: false }, c); });
      return (cues ? cues[cues.length - 1] : t + ws.length * 0.12) + 0.6;
    };
    api.setTally = function (tl, text, t) {
      const ta = $("tally");
      if (!ta) return t;
      $("tv").textContent = text;
      gsap.set(ta, { opacity: 0 });
      tl.fromTo(ta, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, t);
      return t + 0.6;
    };
    api.hideTally = function (tl, t) { const ta = $("tally"); if (ta) tl.to(ta, { opacity: 0, duration: 0.4, ease: "power1.in" }, t); return t + 0.4; };
    // hide the whole board / bring it back (structural, e.g. before a whip)
    api.out = function (tl, t, d) { d = d || 0.5; tl.to(root, { opacity: 0, y: -20, duration: d, ease: E().in }, t); return t + d; };
    return api;
  };

  // =====================================================================================
  // MOTIF 2 — THE LINE  (paper ground with graph texture; full frame 1920x1080)
  // =====================================================================================
  NV.lineGeom = { AX: 400, Y0: 900, Y1: 180, X0: 486, STEP: 206, ZTOP: 132, CARD_H: 74, L0: 96, L1: 1824 };
  NV.line = function (root, o) {
    o = Object.assign({ prefix: "nvln", chips: [], lineAt: 0.62, gate: null, boil: 4, paper1: "assets/textures/paper_graph_01_hires.jpg",
      paper2: "assets/textures/paper_cream_02.jpg", paper2Opacity: 0.5, labels: { top: "Most powerful", bottom: "Weakest", tag: "THE LINE",
        cant: "Can’t sell to China", can: "Can sell" } }, o);
    const P = o.prefix, G = NV.lineGeom, L = Object.assign({}, NV.line.defaults, o.labels);
    const Y = (p) => G.Y0 - (G.Y0 - G.Y1) * p;
    root.classList.add("nvm-ln");
    root.innerHTML = `<div class="nvm-cam" id="${P}-cam">
        <div class="nvm-p1" style="background-image:url('${o.paper1}')"></div>
        <div class="nvm-p2" style="background-image:url('${o.paper2}'); opacity:${o.paper2Opacity}"></div>
        <div class="nvm-zone" id="${P}-zone"></div>
        <svg class="nvm-svg" id="${P}-axsvg" viewBox="0 0 1920 1080"></svg>
        <div class="nvm-axl t-label" id="${P}-top" style="left:${G.AX}px; top:${G.Y1 - 92}px">${L.top}</div>
        <div class="nvm-axl t-label" id="${P}-bot" style="left:${G.AX}px; top:${G.Y0 + 44}px">${L.bottom}</div>
        <div class="nvm-zl up t-label" id="${P}-zu">${L.cant}</div>
        <div id="${P}-ticks"></div><div id="${P}-chips"></div>
        <div class="nvm-lw" id="${P}-lw"><svg class="nvm-svg" id="${P}-lsvg" viewBox="0 0 1920 1080"></svg>
          <div class="nvm-tagw" id="${P}-tag"><span class="label-box">${L.tag}</span></div>
          <div class="nvm-zl dn t-label" id="${P}-zd">${L.can}</div></div>
      </div>`;
    const F = markFilters(root, P, o);
    const $ = (id) => document.getElementById(P + "-" + id);
    const INK = "var(--ink)";
    // axis: a pen line, bottom -> top, with an arrow head
    const ax = $("axsvg");
    const axis = strokeP(ax, `M${G.AX - 1} ${G.Y0 + 22} C${G.AX + 2} ${G.Y0 - 200} ${G.AX - 3} ${G.Y1 + 260} ${G.AX + 1} ${G.Y1 - 34}`, INK, 6, F.line);
    const head = strokeP(ax, `M${G.AX - 22} ${G.Y1 - 6} L${G.AX + 1} ${G.Y1 - 36} L${G.AX + 23} ${G.Y1 - 5}`, INK, 6, F.line);
    // ruler rungs every 10 % of power (a ranking board, not an empty axis)
    const rungs = svgEl(ax, "g", { opacity: 0.55 });
    for (let k = 1; k < 10; k++) { const ry = Y(k / 10); const r = svgEl(rungs, "path", { d: `M${G.AX - 10} ${ry} L${G.AX + 10} ${ry}`, "stroke-width": 3, "stroke-linecap": "round" }); r.style.stroke = "var(--ink)"; }
    // the line: hand-drawn ice marker, never perfectly straight
    let lineP = o.lineAt;
    const ly = Y(lineP), rr = FX.rng(31), pts = [];
    for (let x = G.L0; x <= G.L1; x += 64) pts.push([x, ly + (rr() - 0.5) * 5 + (x - G.L0) * -0.003]);
    pts[pts.length - 1][0] = G.L1;
    const lsvg = $("lsvg");
    const lineD = "M" + pts.map((q) => q[0].toFixed(1) + " " + q[1].toFixed(1)).join(" L");
    const lineEl = strokeP(lsvg, lineD, "var(--ice-dark)", 11, F.line);
    lineEl.style.mixBlendMode = "multiply";
    gsap.set($("tag"), { top: ly - 74 });
    gsap.set($("zd"), { top: ly + 22 });
    gsap.set($("zone"), { height: ly - G.ZTOP });
    let off = 0;   // current y offset of the line wrapper
    // chips
    const chips = {}, order = [];
    function makeChip(c) {
      const col = c.col != null ? c.col : order.length;
      order.push(c.id);
      const x = c.x != null ? c.x : G.X0 + col * G.STEP, y = Y(c.power);
      const card = document.createElement("div");
      card.className = "nvm-chip"; card.id = P + "-chip-" + c.id;
      card.style.left = x + "px"; card.style.top = (y - G.CARD_H / 2) + "px";
      card.innerHTML = `<svg viewBox="0 0 44 44"><g fill="none" stroke="var(--ink)" stroke-width="2.6" stroke-linecap="round">
          <rect x="8" y="8" width="28" height="28" rx="3"/><path d="M15 8V2M22 8V2M29 8V2M15 42v-6M22 42v-6M29 42v-6M8 15H2M8 22H2M8 29H2M42 15h-6M42 22h-6M42 29h-6"/></g>
          <rect x="15" y="15" width="14" height="14" fill="var(--ink)"/></svg>
        <span class="nvm-cn t-label">${c.name}</span><div class="nvm-dim"></div>
        <svg class="nvm-xs" viewBox="0 0 100 100" preserveAspectRatio="none" style="left:6px; top:6px; width:60px; height:62px"></svg>
        <div class="nvm-ban t-label">Banned</div>`;
      $("chips").appendChild(card);
      const tick = document.createElement("div");
      tick.className = "nvm-tick"; tick.style.left = G.AX + "px"; tick.style.top = y + "px";
      $("ticks").appendChild(tick);
      chips[c.id] = { c, card, tick, banned: false, added: true };
      return chips[c.id];
    }
    o.chips.forEach(makeChip);
    const api = { el: root, cam: $("cam"), Y, prefix: P, chip: (id) => chips[id] && chips[id].card, line: $("lw") };

    api.drawAxis = function (tl, t, ao) {
      ao = ao || {};
      const d = ao.dur || 1.0;
      drawOn(tl, axis, t, d, C(E().inOut, d));
      drawOn(tl, head, t + d - 0.05, 0.25, C(E().out, 0.25));
      gsap.set(rungs, { opacity: 0 });
      tl.fromTo(rungs, { opacity: 0 }, { opacity: 0.55, duration: d, ease: C(E().out, d), immediateRender: false }, t + 0.2);
      [["bot", ao.bottom != null ? ao.bottom : t + 0.1], ["top", ao.top != null ? ao.top : t + d]].forEach(([k, c]) => {
        gsap.set($(k), { opacity: 0 });
        tl.fromTo($(k), { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, c);
      });
      return t + d + 0.25;
    };
    api.drawLine = function (tl, t, lo) {
      lo = lo || {};
      const d = lo.dur || 1.1;
      drawOn(tl, lineEl, t, d, C(E().inOut, d));
      gsap.set($("tag"), { opacity: 0 });
      tl.fromTo($("tag"), { opacity: 0, scale: 0.7, transformOrigin: "0% 100%" }, { opacity: 1, scale: 1, duration: 0.7, ease: C(E().out, 0.7), immediateRender: false }, lo.tag != null ? lo.tag : t + 0.25);
      gsap.set($("zone"), { opacity: 0 });
      tl.fromTo($("zone"), { opacity: 0 }, { opacity: 1, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, lo.zone != null ? lo.zone : t + d * 0.7);
      [["zu", lo.cant != null ? lo.cant : t + d], ["zd", lo.can != null ? lo.can : t + d + 0.4]].forEach(([k, c]) => {
        gsap.set($(k), { opacity: 0 });
        tl.fromTo($(k), { opacity: 0, x: 18 }, { opacity: 1, x: 0, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, c);
      });
      return t + d + 0.6;
    };
    api.addChip = function (tl, id, t, co) {
      let ch = chips[id];
      if (!ch) ch = makeChip(Object.assign({ id }, co));
      const d = 0.8;
      gsap.set(ch.card, { opacity: 0 }); gsap.set(ch.tick, { scaleX: 0 });
      tl.fromTo(ch.card, { opacity: 0, y: -28, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: d, ease: C(E().out, d), immediateRender: false }, t);
      tl.fromTo(ch.tick, { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: C(E().out, 0.5), immediateRender: false }, t + 0.1);
      return t + d;
    };
    api.ban = function (tl, id, t) {
      const ch = chips[id];
      if (!ch) throw new Error("NV.line.ban: unknown chip " + id);
      ch.banned = true;
      const xs = ch.card.querySelector(".nvm-xs"), dim = ch.card.querySelector(".nvm-dim"), tag = ch.card.querySelector(".nvm-ban");
      const a = strokeP(xs, GLYPH.x.paths[0], "var(--red)", 13, F.cell), b = strokeP(xs, GLYPH.x.paths[1], "var(--red)", 13, F.cell);
      tl.fromTo(dim, { opacity: 0 }, { opacity: 0.5, duration: 0.4, ease: C(E().out, 0.4), immediateRender: false }, t);
      drawOn(tl, a, t + 0.05, 0.2); drawOn(tl, b, t + 0.29, 0.2);
      tl.fromTo(tag, { opacity: 0, scale: 1.6, rotation: -12 }, { opacity: 1, scale: 1, rotation: -5, duration: 0.6, ease: C(E().out, 0.6), immediateRender: false }, t + 0.35);
      tl.to(ch.tick, { backgroundColor: tok("--red"), duration: 0.2 }, t + 0.35);
      return t + 0.95;
    };
    api.moveLine = function (tl, newP, t, dur, mo) {
      mo = Object.assign({ autoBan: true }, mo);
      dur = dur || 1.4;
      const oldP = lineP, from = off, to = Y(newP) - ly;
      tl.fromTo($("lw"), { y: from }, { y: to, duration: dur, ease: C(E().inOut, dur), immediateRender: false }, t);
      tl.fromTo($("zone"), { height: Y(oldP) - G.ZTOP }, { height: Y(newP) - G.ZTOP, duration: dur, ease: C(E().inOut, dur), immediateRender: false }, t);
      off = to; lineP = newP;
      if (mo.autoBan) Object.values(chips).forEach((ch) => {
        if (ch.banned || ch.c.power <= newP || ch.c.power > oldP) return;   // only chips the line passes over
        const top = ch.c.power + (G.CARD_H / 2) / (G.Y0 - G.Y1);
        const frac = Math.min(1, Math.max(0, (oldP - Math.min(top, oldP)) / (oldP - newP)));
        api.ban(tl, ch.c.id, t + dur * (0.35 + 0.5 * frac));
      });
      return t + dur;
    };
    return api;
  };
  NV.line.defaults = { top: "Most powerful", bottom: "Weakest", tag: "THE LINE", cant: "Can’t sell to China", can: "Can sell" };

  window.NV = NV;
})();
