
    /* ============ C3S012 · 50.55–54.23 · Field's code on a lamp-lit desk ============ */
    whip("sc011", "sc012", S(50.49), { dir: 1 });
    scene("sc012", 50.49, 54.23);
    (function () {
      tl.fromTo($("sc012-lamp"), { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(50.6));
      tl.to($("sc012-lamp"), { opacity: 0.6, duration: 1 / 24, yoyo: true, repeat: 1 }, S(50.68));
      tl.fromTo($("sc012-cam"), { scale: 1.0 }, { scale: 1.1, duration: 3.74, ease: "none", immediateRender: false }, S(50.49));
      tl.fromTo($("sc012-cover"), { rotationY: 0, transformPerspective: 2200 }, { rotationY: -168, transformPerspective: 2200, duration: 0.7, ease: C(E.inOut, 0.7), immediateRender: true }, S(53.3));
      wr("sc012-t", [T(53.11) - L, T(53.51) - L], { dur: 0.6 });
    })();

    /* ============ C3S013 · 54.23–59.35 · David Dudley Field, a legal code for New York ============ */
    scene("sc013", 54.23, 59.35);
    ground("paper", S(54.23));
    (function () {
      tl.fromTo([$("sc013-field"), $("sc013-ht")], { x: 380, opacity: 0.0 }, { x: 0, opacity: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(54.23));
      tl.set($("sc013-ht"), { opacity: 0.35 }, S(55.2));
      const nm = $("sc013-name").firstElementChild;
      show(nm, T(55.19) - L);
      wr("sc013-name", [T(55.19) - L, T(55.67) - L, T(56.39) - L], { dur: 0.5, y: 8 });
      tl.fromTo($("sc013-p1"), { x: -900, rotation: -12 }, { x: 0, rotation: -4, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(57.29));
      wr("sc013-lc", [T(57.35) - L, T(57.75) - L], { dur: 0.6 });
      tl.fromTo($("sc013-p2"), { y: -800, rotation: 9 }, { y: 0, rotation: 3, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(58.07));
      pop("sc013-ny", T(58.15) - L, 0.5, 0.85);
      tl.fromTo($("sc013-cam"), { x: 0 }, { x: -40, duration: 5.1, ease: "none", immediateRender: false }, S(54.23));
    })();

    /* ============ C3S014 · 59.35–63.03 · New York never adopted it ============ */
    scene("sc014", 59.35, 63.1);
    (function () {
      tl.fromTo($("sc014-card"), { y: -900, rotation: -6 }, { y: 0, rotation: 4, duration: 0.55, ease: C(E.out, 0.55), immediateRender: true }, S(59.35));
      pop("sc014-ny", S(59.6), 0.5, 0.85);
      wr("sc014-t", [T(60.15) - L, T(60.71) - L], { dur: 0.5 });
      const mk = $("sc014-mk");
      FX.markup.pen(tl, mk, S(60.71), { points: [[40, 60], [480, 660]], dur: 0.22, width: 12, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(60.97), { points: [[470, 50], [50, 670]], dur: 0.22, width: 12, color: INK, filter: PEN, seed: 5 });
      tl.to($("sc014-card"), { x: -1500, rotation: -8, duration: 0.5, ease: C(E.in, 0.5) }, S(62.23));
      tl.fromTo($("sc014-map"), { x: 0 }, { x: 60, duration: 3.6, ease: "none", immediateRender: false }, S(59.35));
    })();

    /* ============ C3S015 · 63.03–68.63 · copied whole to California ============ */
    whip("sc014", "sc015", S(62.97), { dir: 1 });
    scene("sc015", 62.97, 68.7);
    (function () {
      const svg = $("sc015-svg");
      const ny = [3365, 1551], ca = [400, 1810];
      el("circle", { cx: ny[0], cy: ny[1], r: 26, fill: INK }, svg);
      const route = ink(svg, `M${ny[0]} ${ny[1]} C 2700 1300, 1600 1250, 900 1560 S 520 1760 ${ca[0]} ${ca[1]}`, S(63.27), 1.6, { width: 46, color: YEL, ease: C("sine.inOut", 1.6), filter: MRK, blend: "multiply", opacity: 0.85 });
      const cap = el("circle", { cx: ca[0], cy: ca[1], r: 34, fill: RED, opacity: 0 }, svg);
      tl.fromTo(cap, { opacity: 0, attr: { r: 60 } }, { opacity: 1, attr: { r: 34 }, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(64.85));
      tl.fromTo($("sc015-trk"), { x: -420, y: 40 }, { x: 380, y: -40, duration: 2.4, ease: E.cam, immediateRender: false }, S(63.03));
      pop("sc015-ca", T(63.27) - L, 0.5, 0.9);
      // the code card arrives in California; a photocopy bar sweeps it and an identical copy slides out
      tl.fromTo($("sc015-c1"), { opacity: 0, y: -60, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(65.4));
      tl.fromTo($("sc015-scan"), { opacity: 0, top: -40 }, { opacity: 1, top: 460, duration: 0.5, ease: "none", immediateRender: true }, S(66.33));
      tl.to($("sc015-scan"), { opacity: 0, duration: 0.1 }, S(66.83));
      tl.fromTo($("sc015-c2"), { opacity: 0, x: 0, y: 0, rotation: -3 }, { opacity: 1, x: -400, y: 70, rotation: 4, duration: 0.9, ease: C(E.inOut, 0.9), immediateRender: true }, S(66.85));
      wr("sc015-cp", [T(66.39) - L, T(66.87) - L], { dur: 0.6 });
    })();

    /* ============ C3S016 · 68.63–75.27 · Cal. Civil Code §1673 ============ */
    whip("sc015", "sc016", S(68.57), { dir: 1, flash: true });
    scene("sc016", 68.57, 75.27);
    ground("night", S(68.57));
    (function () {
      const P0 = { x: 0, y: 0, scale: 1 }, P1 = frame(974, 548, 1.7), P2 = frame(974, 548, 1.82);
      tl.fromTo($("sc016-cam"), P0, Object.assign({ duration: 2.3, ease: E.in, immediateRender: false }, { x: P1.x * 0.6, y: P1.y * 0.6, scale: 1.42 }), S(68.7));
      tl.to($("sc016-cam"), Object.assign({ duration: 1.0, ease: E.out }, P1), S(71.0));
      FX.focusHunt(tl, $("sc016-page"), S(71.05), { dur: 0.8 });
      tl.to($("sc016-cam"), Object.assign({ duration: 3.3, ease: "none" }, P2), S(72.0));
      FX.contrastCallout(tl, $("sc016-veil"), S(72.4), { w: 777, h: 1206, d: "M70 584 L732 584 L732 690 L70 690 Z", feather: 14, color: "rgba(18,16,13,1)", strength: 0.6 });
      tl.fromTo($("sc016-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: C("sine.inOut", 0.45), immediateRender: true }, S(73.77));
      wr("sc016-t", [T(69.91) - L, T(70.15) - L, T(70.23) - L, T(70.39) - L], { dur: 0.5 });
    })();

    /* ============ C3S017 · 75.27–82.10 · a contract is illegal ============ */
    scene("sc017", 75.27, 82.95);
    ground("paper", S(75.27));
    (function () {
      const ln = $("sc017-lines");
      for (let i = 0; i < 9; i++) div(ln, `left:130px;top:${330 + i * 78}px;width:${i % 4 === 3 ? 640 : 1140}px;height:11px;background:rgba(20,27,36,0.3);border-radius:3px`, "q-abs");
      tl.fromTo($("sc017-form"), { x: 700, rotation: 3 }, { x: 0, rotation: -0.8, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, S(75.27));
      rise("sc017-h", T(75.75) - L, { dur: 0.5 });
      // ILLEGAL stamp: lands, choke-settles, camera knocks
      tl.fromTo($("sc017-st"), { opacity: 0, scale: 1.7 }, { opacity: 0.92, scale: 1, duration: 0.18, ease: C("power3.in", 0.18), immediateRender: true }, T(76.47) - L - 0.12);
      FX.chokeSettle(tl, ch017, $("sc017-st"), T(76.47) - L, 5, 0.6, "none");
      tl.fromTo($("sc017-cam"), { x: 0 }, { x: 10, duration: 1 / 12, yoyo: true, repeat: 1, ease: "none", immediateRender: false }, S(76.42));
      tl.fromTo($("sc017-cam"), { y: 0 }, { y: -720, duration: 1.1, ease: E.cam, immediateRender: false }, S(77.4));
      const ws = words("sc017-ty");
      [T(78.74) - L, T(78.98) - L, T(79.78) - L, T(80.26) - L, T(80.42) - L, T(80.66) - L, T(81.06) - L].forEach((t, i) => show(ws[i], t));
      tl.to($("sc017-cam"), { y: -860, duration: 0.6, ease: E.in }, S(82.0));
    })();

    /* ============ C3S018 · 82.10–86.90 · the Silicon Valley TV show ============ */
    scene("sc018", 82.10, 86.90);
    ground("night", S(82.10));
    (function () {
      tl.fromTo($("sc018-tv"), { y: 420 }, { y: 0, duration: 0.8, ease: E.cam, immediateRender: false }, S(82.10));
      tl.fromTo($("sc018-tv"), { scale: 1 }, { scale: 1.05, duration: 4, ease: "none", immediateRender: false, transformOrigin: "40% 45%" }, S(82.9));
      gsap.set($("sc018-scr"), { scaleY: 0.012, opacity: 0 });
      tl.fromTo($("sc018-scr"), { scaleY: 0.012, opacity: 1, filter: "brightness(4)" }, { scaleY: 1, opacity: 1, filter: "brightness(1)", duration: 0.25, ease: "power2.out", immediateRender: false }, S(83.94));
      wr("sc018-tvs", [T(84.74) - L, T(85.06) - L], { dur: 0.6 });
      rise("sc018-ep", T(85.46) - L, { dur: 0.6 });
      // CRT off: collapse to a line, then a dot
      tl.to($("sc018-scr"), { scaleY: 0.01, filter: "brightness(3)", duration: 0.12, ease: "power2.in" }, S(86.6));
      tl.to($("sc018-scr"), { scaleX: 0.01, duration: 0.1, ease: "power2.in" }, S(86.72));
      tl.to($("sc018-scr"), { opacity: 0, duration: 0.06 }, S(86.82));
    })();

    /* ============ C3S019 · 86.90–90.74 · the cork board of what we already covered ============ */
    scene("sc019", 86.90, 90.80);
    (function () {
      tl.fromTo($("sc019"), { filter: "brightness(0)" }, { filter: "brightness(1)", duration: 0.3, ease: "power1.out", immediateRender: false }, S(86.90));
      tl.set($("sc019"), { filter: "none" }, S(87.25));
      const box = $("sc019-cards");
      const C19 = [
        ["assets/archival/collage/terman_frederick_1955.jpg", 170, 110, 320, 312, -4],
        ["assets/archival/hp/hewlett_and_packard_together_1960.jpg", 560, 80, 380, 307, 3],
        ["assets/archival/hp/layers/garage.png", 1280, 100, 380, 318, -2],
        ["assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg", 230, 560, 440, 290, 2],
        ["assets/intro/photos/silicon_valley_aerial.jpg", 1240, 560, 440, 293, -3],
      ];
      const pins = [];
      C19.forEach(([src, x, y, w, h, r], i) => {
        const c = div(box, `left:${x}px;top:${y}px;width:${w}px;height:${h}px;transform:rotate(${r}deg);background:#e4dccb;border:12px solid #f1ebdd;opacity:0`, "q-card", `<img src="${src}" alt="" style="object-fit:${i === 2 ? "contain" : "cover"};filter:grayscale(1) sepia(0.25) contrast(1.05)" />`);
        const p = div(box, `left:${x + w / 2 - 13}px;top:${y - 6}px;opacity:0`, "q-pin");
        const t = S(86.95) + i * 2 / 12;
        tl.fromTo(c, { opacity: 0, scale: 1.12 }, { opacity: 1, scale: 1, duration: 1 / 12, ease: "none", immediateRender: true }, t);
        tl.fromTo(p, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, t + 1 / 12);
        pins.push([x + w / 2, y + 7]);
      });
      pop("sc019-note", T(88.90) - L, 0.5, 0.9);
      const s = $("sc019-str");
      const order = [0, 1, 2, 4, 3, 0];
      for (let i = 0; i < order.length - 1; i++) {
        const [x1, y1] = pins[order[i]], [x2, y2] = pins[order[i + 1]];
        ink(s, `M${x1} ${y1} Q${(x1 + x2) / 2} ${Math.max(y1, y2) + 70} ${x2} ${y2}`, S(88.9) + i * 0.16, 0.3, { width: 4, color: RED, ease: "none" });
      }
      wr("sc019-t", [T(89.70) - L, T(90.02) - L, T(90.18) - L], { dur: 0.4 });
      tl.fromTo($("sc019-cam"), { scale: 1 }, { scale: 1.15, duration: 3.9, ease: "none", immediateRender: false }, S(86.9));
    })();

    /* ============ C3S020 · 90.74–94.66 · Fairchild, 1960 ============ */
    whip("sc019", "sc020", S(90.68), { vertical: true, dir: 1 });
    scene("sc020", 90.68, 94.66);
    (function () {
      gated(90.6, 94.7, () => FX.streaks($("sc020-streaks"), { seed: 2001, speed: 0.4, gain: 0.8 }));
      tl.fromTo($("sc020-card"), { scale: 1.0, x: -30, rotationY: -4, transformPerspective: 1400 }, { scale: 1.1, x: 30, rotationY: 2, transformPerspective: 1400, duration: 4.0, ease: E.cam, immediateRender: true }, S(90.68));
      rise("sc020-f", T(90.74) - L, { dur: 1.0 });
      show($("sc020-law").firstElementChild, T(93.38) - L);
      $("sc020-law").firstElementChild.style.opacity = 0;
      wr("sc020-law", [T(93.38) - L, T(93.78) - L], { dur: 0.4, y: 6 });
    })();

    /* ============ C3S021–022 · 94.66–105.54 · the Fairchild family tree ============ */
    scene("sc021", 94.66, 105.6);
    ground("paper", S(94.66));
    (function () {
      const svg = $("sc021-svg"), nodes = $("sc021-nodes"), r = FX.rng(2101);
      const FC = [960, 240], Y1 = 560, X1 = [300, 630, 960, 1290, 1620];
      ink(svg, `M${FC[0]} ${FC[1]} L${FC[0]} 400`, S(94.7), 0.4, { width: 6 });
      ink(svg, `M${X1[0]} 400 L${X1[4]} 400`, S(95.0), 0.6, { width: 6, ease: C(E.inOut, 0.6) });
      const node = (x, y, t, big) => { const n = div(nodes, `left:${x}px;top:${y}px` + (big ? ";width:44px;height:44px;margin:-22px 0 0 -22px" : ""), "q-node"); tl.fromTo(n, { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 1 / 12, ease: "none", immediateRender: true }, t); return n; };
      X1.forEach((x, i) => { ink(svg, `M${x} 400 L${x} ${Y1 - 30}`, S(96.98) + i * 0.08, 0.6, { width: 6 }); if (x !== 1290) node(x, Y1, S(97.6) + i / 12, true); });
      // later generations sprout from every node at 12 fps ("a lot of things are born")
      let t0 = S(104.0), k = 0;
      const gen = (px, py, depth) => {
        if (depth > 3) return;
        const n = depth === 1 ? 3 : 2, y = py + 300;
        for (let j = 0; j < n; j++) {
          const span = depth === 1 ? 260 : depth === 2 ? 120 : 56;
          const x = px + (j - (n - 1) / 2) * span + (r() - 0.5) * 20;
          const t = t0 + Math.min(9, Math.floor(k++ / 7)) / 12;
          const p = el("path", { d: `M${px} ${py + 24} C${px} ${py + 150} ${x} ${y - 150} ${x} ${y - 18}`, fill: "none", stroke: INK, "stroke-width": 4, opacity: 0 }, svg);
          tl.fromTo(p, { opacity: 0 }, { opacity: 0.85, duration: 0.001, immediateRender: true }, t);
          node(x, y, t + 1 / 12);
          gen(x, y, depth + 1);
        }
      };
      X1.forEach((x) => gen(x, Y1, 1));
      show("sc021-fc", S(94.7));
      wr("sc021-dl", [T(96.98) - L, T(97.22) - L, T(97.30) - L], { dur: 0.6 });
      pop("sc021-intel", S(98.84), 0.6, 0.6);
      rise("sc021-born", T(104.02) - L, { dur: 0.8 });
      const cam = $("sc021-cam");
      tl.fromTo(cam, { y: 0, scale: 1 }, { y: -120, scale: 1, duration: 2.2, ease: E.cam, immediateRender: false }, S(96.9));
      tl.to(cam, { y: -192, scale: 0.6, duration: 1.8, ease: E.cam }, S(101.94));
      tl.to(cam, { y: -210, scale: 0.57, duration: 1.2, ease: "none" }, S(104.3));
    })();

    /* ============ C3S023–024 · 105.54–114.66 · "wasn't that big a deal" → "a bigger role" ============ */
    whip("sc021", "sc023", S(105.48), { vertical: true, dir: -1 });
    scene("sc023", 105.48, 115.2);
    ground("night", S(105.48));
    (function () {
      const g = $("sc023-ghost"), b = bbox(CA);
      g.setAttribute("viewBox", `${b.x0} ${b.y0} ${b.w} ${b.h}`);
      el("path", { d: CA, fill: "rgba(242,237,227,0.04)", stroke: BONE, "stroke-width": 6, opacity: 0.16 }, g);
      const svg = $("sc023-svg");
      ink(svg, "M200 860 L2440 860", S(105.6), 0.8, { color: BONE, width: 3, opacity: 0.7, ease: C(E.inOut, 0.8) });
      ink(svg, "M200 860 L200 120", S(105.6), 0.8, { color: BONE, width: 3, opacity: 0.7, ease: C(E.inOut, 0.8) });
      for (let i = 1; i < 6; i++) el("path", { d: `M200 ${860 - i * 130} L2440 ${860 - i * 130}`, stroke: BONE, "stroke-width": 1, "stroke-dasharray": "6 14", opacity: 0.18 }, svg);
      ink(svg, "M200 836 C 500 838, 760 834, 1000 830", S(106.0), 2.6, { color: RED, width: 9, ease: "none" });
      ink(svg, "M210 890 L210 910 L990 910 L990 890", S(108.6), 0.3, { color: BONE, width: 3, opacity: 0.85, ease: C(E.out, 0.3) });
      rise("sc023-beg", T(108.66) - L, { dur: 0.4 });
      rise("sc023-arg", T(106.42) - L, { dur: 0.8 });
      wr("sc023-deal", [T(107.22) - L, T(107.46) - L, T(107.62) - L, T(107.86) - L, T(107.94) - L], { dur: 0.4 });
      // C3S024: the line takes off; camera tracks right
      out("sc023-arg", S(109.1), 0.4); out("sc023-deal", S(109.1), 0.4); out("sc023-beg", S(109.1), 0.4);
      ink(svg, "M1000 830 C 1260 826, 1460 760, 1600 520 S 1820 170 1900 150", S(109.94), 1.0, { color: RED, width: 9, ease: C(E.in, 1.0) });
      tl.fromTo($("sc023-cam"), { x: 0 }, { x: -620, duration: 1.8, ease: E.cam, immediateRender: false }, S(109.3));
      wr("sc023-br", [T(110.18) - L, T(110.42) - L], { dur: 0.6 });
      // big company block → people leave for smaller companies
      const bl = $("sc023-blocks");
      div(bl, "left:1960px;top:520px;width:250px;height:250px;border:4px solid #f2ede3;background:rgba(242,237,227,0.06)", "q-abs");
      const smalls = [[2330, 470], [2330, 620], [2330, 770]];
      smalls.forEach(([x, y]) => div(bl, `left:${x}px;top:${y}px;width:120px;height:110px;border:3px solid rgba(242,237,227,0.8)`, "q-abs"));
      const PER = '<svg viewBox="0 0 30 40" width="30" height="40"><circle cx="15" cy="8" r="7" fill="#f2ede3"/><path d="M3 40 V27 Q3 17 15 17 Q27 17 27 27 V40Z" fill="#f2ede3"/></svg>';
      const ppl = [];
      for (let i = 0; i < 9; i++) ppl.push(div(bl, `left:${1990 + (i % 3) * 70}px;top:${560 + Math.floor(i / 3) * 65}px;width:30px;height:40px`, "q-abs", PER));
      [0, 4, 8].forEach((pi, j) => {
        const p = ppl[pi], sx = 1990 + (pi % 3) * 70, sy = 560 + Math.floor(pi / 3) * 65, [tx, ty] = [smalls[j][0] + 45, smalls[j][1] + 38];
        const st = { u: 0 }, t = S(112.3) + j * 0.22;
        tl.fromTo(st, { u: 0 }, { u: 1, duration: 0.6, ease: C(E.inOut, 0.6), immediateRender: true, onUpdate: () => { const x = sx + (tx - sx) * st.u, y = sy + (ty - sy) * st.u - Math.sin(Math.PI * st.u) * 120; p.style.transform = `translate(${(x - sx).toFixed(1)}px, ${(y - sy).toFixed(1)}px)`; } }, t);
      });
      rise("sc023-lv", T(112.34) - L, { dur: 0.6 });
      tl.fromTo($("sc023-cam"), { y: 0 }, { y: -20, duration: 3.5, ease: "none", immediateRender: false }, S(111.1));
    })();

    /* ============ C3S025 · 114.66–120.58 · online vs "I think it did" ============ */
    scene("sc025", 114.55, 120.6);
    slideIn("sc025", S(114.55), { dur: 0.5 });
    ground("paper", S(114.6));
    (function () {
      tl.fromTo($("sc025-s1"), { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 1 / 12, immediateRender: true }, S(115.3));
      wr("sc025-s1", [T(115.86) - L, T(116.02) - L, T(116.18) - L, T(116.26) - L], { dur: 0.3, y: 6 });
      tl.fromTo($("sc025-s2"), { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 1 / 12, immediateRender: true }, S(116.9));
      tl.fromTo($("sc025-s3"), { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 1 / 12, immediateRender: true }, S(117.3));
      pop("sc025-on", T(117.94) - L, 0.5, 0.9);
      wr("sc025-me", [T(118.82) - L, T(118.98) - L, T(119.14) - L, T(119.30) - L], { dur: 0.35, y: 8 });
      const mk = $("sc025-mk");
      FX.markup.pen(tl, mk, S(119.3), { points: [[1000, 548], [1820, 540]], dur: 0.4, width: 7, color: INK, filter: PEN });
      FX.markup.pen(tl, mk, S(119.66), { points: [[1010, 568], [1800, 562]], dur: 0.3, width: 6, color: INK, filter: PEN, seed: 8 });
      tl.to([$("sc025-s1"), $("sc025-s2"), $("sc025-s3"), $("sc025-on")], { opacity: 0.35, duration: 0.6, ease: E.out }, S(118.7));
      tl.fromTo($("sc025-cam"), { x: 0, y: 0 }, { x: -20, y: -10, duration: 5.9, ease: "none", immediateRender: false }, S(114.66));
    })();
