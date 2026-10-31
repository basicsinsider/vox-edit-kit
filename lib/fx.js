/* Taiwan-edit reusable effects. Everything is a pure function of timeline time (seek-safe). */
(function () {
  const FX = {};
  FX.FPS = 24;

  // ---------- deterministic randomness ----------
  FX.rng = function (seed) {
    let a = (seed >>> 0) || 1;
    return function () {
      a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };
  function hash2(x, y, s) {
    let h = (x * 374761393 + y * 668265263 + s * 2147483647) | 0;
    h = Math.imul(h ^ (h >>> 13), 1274126177);
    return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
  }
  FX.noise2 = function (x, y, s) {
    const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
    const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
    const a = hash2(xi, yi, s), b = hash2(xi + 1, yi, s), c = hash2(xi, yi + 1, s), d = hash2(xi + 1, yi + 1, s);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  };
  FX.noise1 = (x, s) => FX.noise2(x, 0.5, s);

  // ---------- 12fps "posterize time" ease ----------
  FX.choppy = function (ease, dur, fps) {
    const e = gsap.parseEase(ease || "power3.out");
    const n = Math.max(1, Math.round((dur || 1) * (fps || 12)));
    // ceil: the first step lands immediately (floor held the start value for 1/12 s, so text appeared after its word)
    return (t) => (t <= 0 ? 0 : t >= 1 ? 1 : e(Math.ceil(t * n) / n));
  };

  // ---------- per-frame driver ----------
  const frameFns = [];
  FX.onFrame = (fn) => frameFns.push(fn);
  // run a per-frame function only inside [a, b] (scene window, timeline seconds) — keeps long segments fast
  FX.gate = (a, b, fn) => (t) => { if (t >= a && t <= b) fn(t); };
  FX.mount = function (tl, dur) {
    const fns = frameFns.splice(0); // each composition owns the frame functions registered before its mount
    const proxy = { p: 0 };
    tl.to(proxy, {
      p: 1, duration: dur, ease: "none",
      onUpdate() {
        const t = Math.round(this.time() * FX.FPS) / FX.FPS;
        for (const fn of fns) fn(t);
      },
    }, 0);
  };

  // ---------- old-film gate weave + exposure flicker (point 14) ----------
  FX.weave = function (el, o) {
    o = Object.assign({ amp: 1.6, rot: 0.08, flicker: 0.035, seed: 7, from: 0, to: 1e9 }, o);
    FX.onFrame((t) => {
      if (t < o.from || t > o.to) return;
      const f = Math.floor(t * FX.FPS);
      const x = (FX.noise1(f * 0.45, o.seed) - 0.5) * 2 * o.amp + (hash2(f, 1, o.seed) - 0.5) * 0.6;
      const y = (FX.noise1(f * 0.45, o.seed + 11) - 0.5) * 2 * o.amp * 1.3 + (hash2(f, 2, o.seed) - 0.5) * 0.8;
      const r = (FX.noise1(f * 0.2, o.seed + 23) - 0.5) * 2 * o.rot;
      const b = 1 + (hash2(f, 3, o.seed) - 0.5) * 2 * o.flicker + (FX.noise1(f * 0.3, o.seed + 5) - 0.5) * o.flicker;
      el.style.translate = `${x.toFixed(2)}px ${y.toFixed(2)}px`;
      el.style.rotate = `${r.toFixed(3)}deg`;
      el.style.filter = `brightness(${b.toFixed(3)})`;
    });
  };

  // ---------- texture overlays: grain jitter / dust swap ----------
  FX.grain = function (el, seed) {
    FX.onFrame((t) => {
      const f = Math.floor(t * FX.FPS);
      el.style.backgroundPosition = `${Math.floor(hash2(f, 9, seed || 3) * 900)}px ${Math.floor(hash2(f, 10, seed || 3) * 900)}px`;
    });
  };
  FX.dust = function (el, seed, every) {
    every = every || 2;
    FX.onFrame((t) => {
      const f = Math.floor(t * FX.FPS / every);
      const sx = hash2(f, 4, seed || 5) > 0.5 ? -1 : 1, sy = hash2(f, 6, seed || 5) > 0.5 ? -1 : 1;
      el.style.transform = `scale(${sx * 1.05}, ${sy * 1.05}) translate(${(hash2(f, 7, seed || 5) - 0.5) * 120}px, ${(hash2(f, 8, seed || 5) - 0.5) * 80}px)`;
    });
  };

  // ---------- fractal-noise light streaks (point 8) ----------
  // Fractal noise squashed horizontally into thin vertical streaks, evolution animated, levels crushed.
  FX.streaks = function (canvas, o) {
    o = Object.assign({ seed: 17, speed: 0.55, xfreq: 0.11, gamma: 2.4, lo: 0.42, hi: 0.95, tint: [255, 214, 170], gain: 1, angle: 0 }, o);
    const W = (canvas.width = 384), H = (canvas.height = 216);
    const ctx = canvas.getContext("2d");
    const img = ctx.createImageData(W, H);
    FX.onFrame((t) => {
      const evo = t * o.speed;
      const d = img.data;
      for (let x = 0; x < W; x++) {
        let col = 0, amp = 0.55, fq = o.xfreq;
        for (let k = 0; k < 4; k++) { col += amp * FX.noise2(x * fq + k * 31.7, evo * (1 + k * 0.35), o.seed + k); amp *= 0.5; fq *= 2.03; }
        col /= 1.03;
        for (let y = 0; y < H; y++) {
          const ny = FX.noise2(x * o.xfreq * 0.5, y * 0.012 + evo * 0.6, o.seed + 99);
          let v = col * 0.82 + ny * 0.18;
          v = Math.min(1, Math.max(0, (v - o.lo) / (o.hi - o.lo)));
          v = Math.pow(v, o.gamma) * o.gain;
          const fall = 1 - Math.abs(y / H - 0.42) * 0.9;
          v *= Math.max(0, fall);
          const i = (y * W + x) * 4;
          d[i] = o.tint[0] * v; d[i + 1] = o.tint[1] * v; d[i + 2] = o.tint[2] * v; d[i + 3] = 255;
        }
      }
      ctx.putImageData(img, 0, 0);
    });
  };

  // ---------- iris shutter (point 9) ----------
  // Builds 6 blades in an <svg viewBox="0 0 1920 1080">. Returns {at(tl, tMid)} closing to black at tMid.
  FX.iris = function (svg, o) {
    o = Object.assign({ blades: 7, close: 0.16, hold: 2 / 24, open: 0.2, twist: 38 }, o);
    const NS = "http://www.w3.org/2000/svg";
    svg.setAttribute("viewBox", "0 0 1920 1080");
    svg.innerHTML = `<defs><linearGradient id="${svg.id}-g" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#2a2826"/><stop offset="0.04" stop-color="#121110"/><stop offset="1" stop-color="#070707"/></linearGradient></defs>`;
    const blades = [];
    for (let k = 0; k < o.blades; k++) {
      const g = document.createElementNS(NS, "g");
      const r = document.createElementNS(NS, "rect");
      r.setAttribute("x", -1800); r.setAttribute("width", 3600); r.setAttribute("height", 2600);
      r.setAttribute("fill", `url(#${svg.id}-g)`);
      r.setAttribute("stroke", "rgba(255,240,220,0.10)"); r.setAttribute("stroke-width", "2");
      g.appendChild(r); svg.appendChild(g); blades.push({ g, r });
    }
    const R_OPEN = 1250;
    const state = { r: R_OPEN };
    function draw() {
      const p = 1 - state.r / R_OPEN;
      blades.forEach((b, k) => {
        const ang = (360 / o.blades) * k + p * o.twist;
        b.r.setAttribute("y", state.r - 6);
        b.g.setAttribute("transform", `translate(960 540) rotate(${ang.toFixed(2)}) translate(${(p * 140).toFixed(1)} 0)`);
      });
      svg.style.opacity = state.r >= R_OPEN - 1 ? 0 : 1;
    }
    draw();
    return {
      at(tl, tMid) {
        tl.fromTo(state, { r: R_OPEN }, { r: 0, duration: o.close, ease: "power2.in", onUpdate: draw, immediateRender: false }, tMid - o.close - o.hold / 2);
        tl.fromTo(state, { r: 0 }, { r: R_OPEN, duration: o.open, ease: "power2.out", onUpdate: draw, immediateRender: false }, tMid + o.hold / 2);
      },
    };
  };

  // ---------- rough edges: boiling displacement + choker reveal (point 18) ----------
  FX.roughDefs = function (svg, id, o) {
    o = Object.assign({ freq: 0.035, scale: 5, choke: 0 }, o);
    svg.insertAdjacentHTML("beforeend", `
      <filter id="${id}" x="-10%" y="-30%" width="120%" height="160%">
        <feMorphology id="${id}-m" operator="erode" radius="${o.choke}" in="SourceGraphic" result="ch"/>
        <feTurbulence id="${id}-t" type="fractalNoise" baseFrequency="${o.freq}" numOctaves="3" seed="1" result="n"/>
        <feDisplacementMap in="ch" in2="n" scale="${o.scale}" xChannelSelector="R" yChannelSelector="G"/>
      </filter>`);
    const turb = svg.querySelector(`#${id}-t`);
    FX.onFrame((t) => turb.setAttribute("seed", 1 + (Math.floor(t * 12) % 9)));
    return svg.querySelector(`#${id}-m`);
  };
  FX.choke = function (tl, morph, t, from, dur) {
    const s = { r: from };
    tl.fromTo(s, { r: from }, {
      r: 0, duration: dur, ease: FX.choppy("power2.out", dur, 12), immediateRender: false,
      onUpdate: () => morph.setAttribute("radius", s.r.toFixed(2)),
    }, t);
    morph.setAttribute("radius", from);
  };

  // ---------- text animations (point 13) ----------
  FX.split = function (el, mode) {
    const text = el.textContent;
    el.textContent = "";
    const parts = mode === "words" ? text.split(/(\s+)/) : Array.from(text);
    return parts.filter((p) => p.length).map((p) => {
      const s = document.createElement("span");
      s.className = mode === "words" ? "word" : "char";
      s.textContent = p;
      el.appendChild(s);
      return s;
    });
  };
  FX.text = {
    // Vox "fill": letters pop on in the brand yellow, then settle to the reading colour.
    fill(tl, el, t, o) {
      o = Object.assign({ hot: "#f2cf3b", cool: null, per: 0.035, settle: 0.6, hold: 0.35 }, o);
      const chars = FX.split(el, "chars");
      const cool = o.cool || getComputedStyle(el).color;
      chars.forEach((c, i) => {
        tl.fromTo(c, { opacity: 0, color: o.hot }, { opacity: 1, duration: 0.001, immediateRender: true }, t + i * o.per);
        tl.to(c, { color: cool, duration: o.settle, ease: "power1.inOut" }, t + i * o.per + o.hold);
      });
      return t + chars.length * o.per + o.hold + o.settle;
    },
    // Letters appear in a seeded random order.
    random(tl, el, t, o) {
      o = Object.assign({ dur: 0.7, seed: 4 }, o);
      const chars = FX.split(el, "chars");
      const r = FX.rng(o.seed);
      const order = chars.map((c, i) => [r(), c]).sort((a, b) => a[0] - b[0]).map((x) => x[1]);
      order.forEach((c, i) => tl.fromTo(c, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t + Math.floor((i / order.length) * o.dur * 12) / 12));
      return t + o.dur;
    },
    // Slot-machine odometer: each letter spins through glyphs and lands.
    odometer(tl, el, t, o) {
      o = Object.assign({ glyphs: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", spins: 7, dur: 0.9, stagger: 0.045, seed: 9 }, o);
      const r = FX.rng(o.seed);
      const text = el.textContent;
      el.textContent = "";
      const cs = getComputedStyle(el);
      const lh = parseFloat(cs.fontSize) * 1.0;
      Array.from(text).forEach((ch, i) => {
        const reel = document.createElement("span");
        reel.className = "reel";
        reel.style.height = lh + "px";
        reel.style.lineHeight = lh + "px";
        const strip = document.createElement("span");
        strip.className = "reel-strip";
        const n = ch.trim() ? o.spins + Math.floor(r() * 4) : 0;
        const pool = /[0-9]/.test(ch) ? "0123456789" : o.glyphs;
        for (let k = 0; k < n; k++) { const s = document.createElement("span"); s.textContent = pool[Math.floor(r() * pool.length)]; strip.appendChild(s); }
        const fin = document.createElement("span"); fin.textContent = ch === " " ? " " : ch; strip.appendChild(fin);
        reel.appendChild(strip); el.appendChild(reel);
        // lock each reel to its final glyph's width so spinning glyphs never change the spacing
        const probe = document.createElement("span");
        probe.style.cssText = "display:inline-block;white-space:pre";
        probe.textContent = fin.textContent;
        el.appendChild(probe);
        reel.style.width = probe.getBoundingClientRect().width + "px";
        el.removeChild(probe);
        if (n) tl.fromTo(strip, { y: 0 }, { y: -n * lh, duration: o.dur, ease: FX.choppy("power3.out", o.dur, 24), immediateRender: true }, t + i * o.stagger);
      });
      tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t);
      return t + text.length * o.stagger + o.dur;
    },
    // Number counter with formatting, posterized to 12fps.
    count(tl, el, t, from, to, dur, fmt) {
      const s = { v: from };
      fmt = fmt || ((v) => Math.round(v).toLocaleString("en-US"));
      el.textContent = fmt(from);
      tl.fromTo(s, { v: from }, { v: to, duration: dur, ease: FX.choppy("power3.out", dur, 12), immediateRender: false, onUpdate: () => (el.textContent = fmt(s.v)) }, t);
      return t + dur;
    },
    // Words rise out of a soft blur (film title in).
    rise(tl, els, t, o) {
      o = Object.assign({ y: 26, stagger: 0.08, dur: 0.7, blur: 10 }, o);
      tl.fromTo(els, { opacity: 0, y: o.y, filter: `blur(${o.blur}px)` }, { opacity: 1, y: 0, filter: "blur(0.45px)", duration: o.dur, stagger: o.stagger, ease: "power3.out", immediateRender: true }, t);
      return t + o.dur + o.stagger * (els.length || 1);
    },
  };

  // ---------- "cutting the curve" match cut (point 15) ----------
  // a and b live in the same wrapper so they share the exact movement; cut at peak velocity (midpoint of inOut).
  FX.curveCut = function (tl, wrap, a, b, t0, dur, o) {
    o = Object.assign({ from: 1, to: 1.35, ease: "expo.inOut" }, o);
    tl.fromTo(wrap, { scale: o.from }, { scale: o.to, duration: dur, ease: FX.choppy(o.ease, dur, 12), immediateRender: false }, t0);
    const mid = t0 + dur / 2;
    tl.set(a, { opacity: 0 }, mid);
    tl.fromTo(b, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, mid);
    tl.fromTo(wrap, { filter: "blur(0px)" }, { filter: "blur(3px)", duration: 1 / 12, yoyo: true, repeat: 1, ease: "none", immediateRender: false }, mid - 1 / 12);
    return mid;
  };

  // ---------- tint (Vox / collage colour system) ----------
  FX.tintDefs = function (svg, id, dark, light) {
    const c = (h) => [1, 3, 5].map((i) => (parseInt(h.slice(i, i + 2), 16) / 255).toFixed(3));
    const d = c(dark), l = c(light);
    svg.insertAdjacentHTML("beforeend", `
      <filter id="${id}" color-interpolation-filters="sRGB">
        <feColorMatrix type="saturate" values="0"/>
        <feComponentTransfer>
          <feFuncR type="table" tableValues="${d[0]} ${l[0]}"/>
          <feFuncG type="table" tableValues="${d[1]} ${l[1]}"/>
          <feFuncB type="table" tableValues="${d[2]} ${l[2]}"/>
        </feComponentTransfer>
      </filter>`);
  };


  // ---------- Vox-style markups: hand-drawn circle / arrow / underline / box ----------
  // Drawn on with stroke-dashoffset (After Effects "trim paths"), then two stacked rough-edge passes
  // (a big wobble + a fine chalky edge) boiling at 12 fps. All coordinates are in a 1920x1080 svg overlay.
  FX.markupDefs = function (svg, id, o) {
    o = Object.assign({ boil: 12 }, o);   // pen/pencil: boil 4 (×/s); marker/chalk: 12
    svg.setAttribute("viewBox", "0 0 1920 1080");
    svg.insertAdjacentHTML("beforeend", `
      <filter id="${id}" x="-20%" y="-20%" width="140%" height="140%">
        <feTurbulence id="${id}-t1" type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="3" result="n1"/>
        <feDisplacementMap in="SourceGraphic" in2="n1" scale="7" xChannelSelector="R" yChannelSelector="G" result="d1"/>
        <feTurbulence id="${id}-t2" type="fractalNoise" baseFrequency="0.22" numOctaves="1" seed="5" result="n2"/>
        <feDisplacementMap in="d1" in2="n2" scale="2.4" xChannelSelector="R" yChannelSelector="G"/>
      </filter>`);
    const t1 = svg.querySelector(`#${id}-t1`), t2 = svg.querySelector(`#${id}-t2`);
    FX.onFrame((t) => { const f = Math.floor(t * o.boil) % 7; t1.setAttribute("seed", 3 + f); t2.setAttribute("seed", 11 + f); });
    return `url(#${id})`;
  };
  function strokePath(svg, d, o) {
    const NS = "http://www.w3.org/2000/svg";
    const p = document.createElementNS(NS, "path");
    p.setAttribute("d", d);
    p.setAttribute("fill", "none");
    p.setAttribute("stroke", o.color || "#e5482a");
    p.setAttribute("stroke-width", o.width || 7);
    p.setAttribute("stroke-linecap", "round");
    p.setAttribute("stroke-linejoin", "round");
    if (o.filter) p.setAttribute("filter", o.filter);
    svg.appendChild(p);
    const len = p.getTotalLength();
    p.setAttribute("stroke-dasharray", `${len} ${len}`);
    p.setAttribute("stroke-dashoffset", len);
    return { p, len };
  }
  function drawOn(tl, item, t, dur, ease) {
    tl.fromTo(item.p, { attr: { "stroke-dashoffset": item.len } }, { attr: { "stroke-dashoffset": 0 }, duration: dur, ease: ease || "power2.inOut", immediateRender: true }, t);
  }
  FX.markup = {
    // loose hand-drawn ellipse that overshoots its start (~1.1 turns)
    circle(tl, svg, t, o) {
      o = Object.assign({ cx: 960, cy: 540, rx: 200, ry: 90, rot: -6, turns: 1.12, dur: 0.6, seed: 2 }, o);
      const r = FX.rng(o.seed), pts = [], N = 64, a0 = -2.2 + r() * 0.4;
      for (let i = 0; i <= N; i++) {
        const k = i / N, a = a0 + k * Math.PI * 2 * o.turns, wob = 1 + (k - 0.5) * 0.08 + (r() - 0.5) * 0.015;
        const x = Math.cos(a) * o.rx * wob, y = Math.sin(a) * o.ry * wob, c = Math.cos(o.rot * Math.PI / 180), s = Math.sin(o.rot * Math.PI / 180);
        pts.push([o.cx + x * c - y * s, o.cy + x * s + y * c]);
      }
      const d = "M" + pts.map((q) => q[0].toFixed(1) + " " + q[1].toFixed(1)).join(" L");
      const it = strokePath(svg, d, o); drawOn(tl, it, t, o.dur, "power1.inOut"); return it.p;
    },
    // curved arrow from (x1,y1) to (x2,y2); bend = perpendicular offset of the control point
    arrow(tl, svg, t, o) {
      o = Object.assign({ x1: 0, y1: 0, x2: 100, y2: 100, bend: 80, head: 34, dur: 0.5 }, o);
      const mx = (o.x1 + o.x2) / 2, my = (o.y1 + o.y2) / 2, dx = o.x2 - o.x1, dy = o.y2 - o.y1, L = Math.hypot(dx, dy);
      const cx = mx - (dy / L) * o.bend, cy = my + (dx / L) * o.bend;
      const shaft = strokePath(svg, `M${o.x1} ${o.y1} Q${cx} ${cy} ${o.x2} ${o.y2}`, o);
      const ang = Math.atan2(o.y2 - cy, o.x2 - cx), h = o.head;
      const hx1 = o.x2 - h * Math.cos(ang - 0.5), hy1 = o.y2 - h * Math.sin(ang - 0.5);
      const hx2 = o.x2 - h * Math.cos(ang + 0.5), hy2 = o.y2 - h * Math.sin(ang + 0.5);
      const head = strokePath(svg, `M${hx1} ${hy1} L${o.x2} ${o.y2} L${hx2} ${hy2}`, o);
      drawOn(tl, shaft, t, o.dur, "power2.out"); drawOn(tl, head, t + o.dur * 0.85, 0.18, "power2.out");
      return [shaft.p, head.p];
    },
    underline(tl, svg, t, o) {
      o = Object.assign({ x1: 0, x2: 300, y: 0, dur: 0.35 }, o);
      const it = strokePath(svg, `M${o.x1} ${o.y + 3} C${o.x1 + (o.x2 - o.x1) * 0.3} ${o.y - 6} ${o.x1 + (o.x2 - o.x1) * 0.7} ${o.y + 8} ${o.x2} ${o.y - 2}`, o);
      drawOn(tl, it, t, o.dur, "power2.out"); return it.p;
    },
    box(tl, svg, t, o) {
      o = Object.assign({ x: 0, y: 0, w: 200, h: 100, dur: 0.7 }, o);
      const j = 6, d = `M${o.x - j} ${o.y + 2} L${o.x + o.w + j} ${o.y - 3} L${o.x + o.w - 2} ${o.y + o.h + j} L${o.x + 3} ${o.y + o.h - 2} L${o.x - 4} ${o.y - j}`;
      const it = strokePath(svg, d, o); drawOn(tl, it, t, o.dur, "power1.inOut"); return it.p;
    },
    // an "X marks the spot"
    cross(tl, svg, t, o) {
      o = Object.assign({ x: 0, y: 0, s: 26, dur: 0.14 }, o);
      const a = strokePath(svg, `M${o.x - o.s} ${o.y - o.s} L${o.x + o.s} ${o.y + o.s}`, o);
      const b = strokePath(svg, `M${o.x + o.s} ${o.y - o.s} L${o.x - o.s} ${o.y + o.s}`, o);
      drawOn(tl, a, t, o.dur, "power2.out"); drawOn(tl, b, t + o.dur + 0.04, o.dur, "power2.out");
      return [a.p, b.p];
    },
  };


  // ---------- easing (Krish's Vox easing reel, 2026-10-31) ----------
  // Vox moves: velocity jumps up almost at once, then decays over a LONG tail (1–2 s) -> soft, expensive-looking settle.
  // cubic-bezier evaluator so we need no GSAP plugin. Use with FX.choppy(FX.ease.out, dur, 12) for 12 fps steps.
  function bezier(x1, y1, x2, y2) {
    const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx, cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
    const X = (t) => ((ax * t + bx) * t + cx) * t, Y = (t) => ((ay * t + by) * t + cy) * t, dX = (t) => (3 * ax * t + 2 * bx) * t + cx;
    return (x) => { if (x <= 0) return 0; if (x >= 1) return 1; let t = x;
      for (let i = 0; i < 8; i++) { const d = X(t) - x, s = dX(t); if (Math.abs(d) < 1e-6 || !s) break; t -= d / s; }
      return Y(Math.min(1, Math.max(0, t))); };
  }
  FX.bezier = bezier;
  FX.ease = {
    out: bezier(0.12, 0.8, 0.12, 1),     // entrances / pops: spike then long tail (the curve in the reel)
    inOut: bezier(0.65, 0, 0.12, 1),     // moves A->B: gentle start, long soft landing
    in: bezier(0.55, 0, 0.9, 0.35),      // exits: slow start, accelerate away (pair with a cut-on-action)
    cam: bezier(0.45, 0, 0.2, 1),        // camera pushes / dollies (never posterized)
  };
  // Default durations: entrances 1.0–1.6 s, moves 1.2–2 s, exits 0.5–0.8 s. Short = only when the word is short.

  // ---------- whip transition (Krish's whip reel) ----------
  // Outgoing shot whips off with heavy directional motion blur; incoming whips in from the opposite side in the same
  // direction; swap at t (peak speed). ~0.24–0.36 s total. Needs an <svg> for the blur filter; each layer gets its own.
  FX.whipDefs = function (svg, id) {
    svg.insertAdjacentHTML("beforeend", `<filter id="${id}" x="-30%" y="-10%" width="160%" height="120%" color-interpolation-filters="sRGB"><feGaussianBlur id="${id}-b" stdDeviation="0 0"/></filter>`);
    return svg.querySelector(`#${id}-b`);
  };
  FX.whip = function (tl, a, b, t, o) {
    o = Object.assign({ dir: 1, dist: 700, dur: 0.32, blur: 90, vertical: false, blurA: null, blurB: null }, o);
    const h = o.dur / 2, ax = o.vertical ? "y" : "x";
    const set = (node, v) => node && node.setAttribute("stdDeviation", o.vertical ? `0 ${v}` : `${v} 0`);
    const sa = { v: 0 }, sb = { v: o.blur };
    // both shots overscale while they smear so the frame is always full (no black gap), and overlap for one frame
    tl.fromTo(a, { [ax]: 0, scale: 1 }, { [ax]: -o.dir * o.dist, scale: 1.18, duration: h, ease: "power3.in", immediateRender: false }, t - h);
    tl.fromTo(sa, { v: 0 }, { v: o.blur, duration: h, ease: "power2.in", immediateRender: false, onUpdate: () => set(o.blurA, sa.v) }, t - h);
    tl.set(a, { autoAlpha: 0 }, t + 1 / 24);
    tl.fromTo(b, { [ax]: o.dir * o.dist * 0.55, scale: 1.18, autoAlpha: 1 }, { [ax]: 0, scale: 1, duration: h, ease: "power3.out", immediateRender: false }, t);
    tl.fromTo(sb, { v: o.blur }, { v: 0, duration: h, ease: "power2.out", immediateRender: false, onUpdate: () => set(o.blurB, sb.v) }, t);
    return t;
  };

  // ---------- DSLR focus hunting (Krish's focus reel) ----------
  // Box-blur keyframes 0 -> 4 -> 6 -> 0 px, like a camera searching for focus. Use right after a fast zoom / big move.
  FX.focusHunt = function (tl, el, t, o) {
    o = Object.assign({ dur: 0.8, a: 4, b: 6, base: "" }, o);
    const s = { r: 0 }, f = () => (el.style.filter = `${o.base} blur(${s.r.toFixed(2)}px)`.trim());
    tl.fromTo(s, { r: 0 }, { r: o.a, duration: o.dur * 0.25, ease: "sine.inOut", immediateRender: false, onUpdate: f }, t);
    tl.to(s, { r: o.b, duration: o.dur * 0.25, ease: "sine.inOut", onUpdate: f }, t + o.dur * 0.25);
    tl.to(s, { r: 0, duration: o.dur * 0.5, ease: "sine.out", onUpdate: f }, t + o.dur * 0.5);
  };

  // ---------- rough reveal that SETTLES (Krish: the boil must not keep jittering after the reveal) ----------
  // Like FX.choke, then hands the element back to a clean filter one 12 fps step after the reveal ends.
  FX.chokeSettle = function (tl, morph, el, t, from, dur, cleanFilter) {
    FX.choke(tl, morph, t, from, dur);
    const rough = el.style.filter || getComputedStyle(el).filter;
    tl.set(el, { filter: rough }, t - 0.001);
    tl.set(el, { filter: cleanFilter || "none" }, t + dur + 1 / 12);
  };


  // ================= Chris Moran "How VOX Directs Your Attention" (Krish's markup reference, 2026-10-31) =================
  // Pen/pencil markup: freehand polyline with nudged points (never a perfect end-to-end line), ~5 px stroke, multiply,
  // roughened edge ≈ 0.7× stroke, boil 4×/s (pen) — FX.markupDefs(svg,id,{boil:4}) — drawn on ~1 s with a slight ease,
  // and drawn OUT by trimming the start (FX.markup.out).
  FX.markup.pen = function (tl, svg, t, o) {
    o = Object.assign({ points: [[0, 0], [300, 0]], jitter: 4, seed: 3, dur: 1.0, width: 5, color: "#1d3f73", ease: "sine.inOut" }, o);
    const r = FX.rng(o.seed), pts = [];
    for (let i = 0; i < o.points.length - 1; i++) {
      const [x1, y1] = o.points[i], [x2, y2] = o.points[i + 1], n = Math.max(2, Math.round(Math.hypot(x2 - x1, y2 - y1) / 40));
      for (let k = 0; k < n; k++) { const f = k / n; pts.push([x1 + (x2 - x1) * f + (r() - 0.5) * o.jitter * 0.4, y1 + (y2 - y1) * f + (r() - 0.5) * o.jitter]); }
    }
    pts.push(o.points[o.points.length - 1]);
    let d = `M${pts[0][0].toFixed(1)} ${pts[0][1].toFixed(1)}`;
    for (let i = 1; i < pts.length; i++) { const [px, py] = pts[i - 1], [x, y] = pts[i]; d += ` Q${px.toFixed(1)} ${py.toFixed(1)} ${((px + x) / 2).toFixed(1)} ${((py + y) / 2).toFixed(1)}`; }
    d += ` L${pts[pts.length - 1][0]} ${pts[pts.length - 1][1]}`;
    const NS = "http://www.w3.org/2000/svg", path = document.createElementNS(NS, "path");
    path.setAttribute("d", d); path.setAttribute("fill", "none"); path.setAttribute("stroke", o.color); path.setAttribute("stroke-width", o.width);
    path.setAttribute("stroke-linecap", "round"); path.style.mixBlendMode = o.blend || "multiply"; if (o.filter) path.setAttribute("filter", o.filter);
    svg.appendChild(path); const len = path.getTotalLength();
    path.setAttribute("stroke-dasharray", `${len} ${len}`); path.setAttribute("stroke-dashoffset", len);
    tl.fromTo(path, { attr: { "stroke-dashoffset": len } }, { attr: { "stroke-dashoffset": 0 }, duration: o.dur, ease: o.ease, immediateRender: true }, t);
    path._len = len; return path;
  };
  // animate any drawn markup OUT (trim the start: the line retracts toward its end)
  FX.markup.out = function (tl, path, t, dur) {
    const len = path._len || path.getTotalLength();
    tl.to(path, { attr: { "stroke-dashoffset": -len }, duration: dur || 0.5, ease: "sine.in" }, t);
  };

  // Contrast call-out: everything except the region gets a faded "lifted blacks" veil; the region stays full contrast.
  // Appears as a HARD CUT (no fade) at t — time t to the peak velocity of an ease-in camera push; pair with a
  // circuit-breaker "clunk" SFX. veil = a full-frame div inside the camera layer; shape = SVG path d / ellipse in its px space.
  FX.contrastCallout = function (tl, veil, t, o) {
    o = Object.assign({ w: 1920, h: 1080, d: null, ellipse: null, feather: 18, color: "rgba(239,231,213,1)", strength: 0.55, until: null }, o);
    const shape = o.d ? `<path d='${o.d}' fill='black'/>` : `<ellipse cx='${o.ellipse[0]}' cy='${o.ellipse[1]}' rx='${o.ellipse[2]}' ry='${o.ellipse[3]}' fill='black'/>`;
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='${o.w}' height='${o.h}' viewBox='0 0 ${o.w} ${o.h}'><defs><filter id='f' x='-20%' y='-20%' width='140%' height='140%'><feGaussianBlur stdDeviation='${o.feather}'/></filter></defs><rect width='100%' height='100%' fill='white'/><g filter='url(#f)'>${shape}</g></svg>`;
    const url = `url("data:image/svg+xml;utf8,${encodeURIComponent(svg)}")`;
    Object.assign(veil.style, { background: o.color, maskImage: url, webkitMaskImage: url, maskSize: "100% 100%", webkitMaskSize: "100% 100%", maskMode: "luminance", pointerEvents: "none" });
    tl.fromTo(veil, { opacity: 0 }, { opacity: o.strength, duration: 0.001, immediateRender: true }, t);
    if (o.until) tl.set(veil, { opacity: 0 }, o.until);
  };

  // Focal call-out (compound blur by a radial gradient): a blurred copy of the layer sits on top with a soft hole where
  // the eye should look; the hole travels across the map/document with long, extreme easing as the narrator moves on.
  // blurEl = blurred duplicate (e.g. filter: blur(9px)); keys = [{t, x, y, r}] in the element's px space.
  FX.focalBlur = function (tl, blurEl, keys, o) {
    o = Object.assign({ soft: 1.9, ease: FX.ease.cam }, o);
    const s = { x: keys[0].x, y: keys[0].y, r: keys[0].r || 260 };
    const apply = () => { const m = `radial-gradient(circle at ${s.x.toFixed(0)}px ${s.y.toFixed(0)}px, transparent ${s.r.toFixed(0)}px, #000 ${(s.r * o.soft).toFixed(0)}px)`; blurEl.style.maskImage = m; blurEl.style.webkitMaskImage = m; };
    apply();
    for (let i = 1; i < keys.length; i++) {
      const k = keys[i], dur = k.dur || 1.6;
      tl.to(s, { x: k.x, y: k.y, r: k.r || s.r, duration: dur, ease: o.ease, onUpdate: apply }, k.t);
    }
    return apply;
  };

  // Text contrast call-out (Google/Vox): the whole text block dims to ~20 % while the scene punches in ~10 %, then the key
  // words come back at full strength through a feathered left→right wipe, slightly after the zoom.
  // dimEl = the full text; keyEl = an identical copy on top containing only the key words visible (others transparent).
  FX.textCallout = function (tl, wrap, dimEl, keyEl, t, o) {
    o = Object.assign({ dim: 0.2, punch: 1.1, dur: 1.1, wipe: 0.7, delay: 0.35, feather: 55 }, o);
    tl.fromTo(dimEl, { opacity: 1 }, { opacity: o.dim, duration: o.dur, ease: FX.ease.out, immediateRender: false }, t);
    tl.fromTo(wrap, { scale: 1 }, { scale: o.punch, duration: o.dur, ease: FX.ease.cam, immediateRender: false }, t);
    const s = { p: -o.feather };
    const f = () => { const m = `linear-gradient(90deg, #000 ${s.p}%, transparent ${s.p + o.feather}%)`; keyEl.style.maskImage = m; keyEl.style.webkitMaskImage = m; };
    f();
    tl.to(s, { p: 100, duration: o.wipe, ease: FX.ease.inOut, onUpdate: f }, t + o.delay);
  };

  // Radio-wave / doppler rings emitting from a map point (flatten with a CSS rotateX on the svg for the 3D look).
  FX.radioWaves = function (svg, cx, cy, o) {
    o = Object.assign({ rings: 4, max: 260, period: 1.6, width: 6, color: "#f2ede3", from: 0, to: 1e9 }, o);
    const NS = "http://www.w3.org/2000/svg", cs = [];
    for (let i = 0; i < o.rings; i++) { const c = document.createElementNS(NS, "circle"); c.setAttribute("cx", cx); c.setAttribute("cy", cy); c.setAttribute("fill", "none"); c.setAttribute("stroke", o.color); svg.appendChild(c); cs.push(c); }
    FX.onFrame((t) => {
      cs.forEach((c, i) => {
        if (t < o.from || t > o.to) { c.setAttribute("opacity", 0); return; }
        const ph = (((t - o.from) / o.period + i / o.rings) % 1);
        c.setAttribute("r", (ph * o.max).toFixed(1));
        c.setAttribute("stroke-width", (o.width * (1 - ph) + 0.5).toFixed(2));   // sawtooth-in profile: thick → thin
        c.setAttribute("opacity", (1 - ph).toFixed(3));
      });
    });
  };

  window.FX = FX;
})();
