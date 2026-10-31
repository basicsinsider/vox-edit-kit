    /* =================== C4S013–C4S014 · 70.72–82.56 · new countries being born in Africa … fight over … your camp =================== */
    scene("sc013", 70.72, 82.85);
    ground("night", S(70.72));
    (function () {
      const svg = $("sc013-svg"), cam = $("sc013-cam"), K = 45.5111;
      const ll = (lon, lat) => [(lon + 60) * K, (42 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      const order = ["sudan", "morocco", "tunisia", "ghana", "guinea", "cameroon", "senegal", "togo", "madagascar", "dem_rep_congo", "somalia", "benin",
        "niger", "burkina_faso", "c_te_d_ivoire", "chad", "central_african_rep", "congo", "gabon", "mali", "nigeria", "mauritania", "sierra_leone",
        "tanzania", "rwanda", "burundi", "algeria", "uganda", "kenya", "malawi", "zambia", "gambia"];
      svg.insertAdjacentHTML("beforeend", `<g id="c4s01-af-g"></g>`);
      const g = $("af-g");
      order.forEach((k, i) => {
        const d = MAPS.africa.d[k]; if (!d) return;
        g.insertAdjacentHTML("beforeend", `<path id="c4s01-af-${k}" d="${d}" fill="${BONE}" fill-opacity="0.2" stroke="${BONE}" stroke-width="6" stroke-opacity="0.85" opacity="0"/>`);
        const p = document.getElementById("c4s01-af-" + k);
        tl.fromTo(p, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(70.95) + Math.floor(i * 0.9) / 12);
        tl.fromTo(p, { attr: { "fill-opacity": 0.55 } }, { attr: { "fill-opacity": 0.2 }, duration: 0.5, ease: C(E.out, 0.5), immediateRender: false }, S(70.95) + Math.floor(i * 0.9) / 12);
      });
      // C4S013 framing: the whole continent, slow push; C4S014: push into one new country (DR Congo), veil hard-cuts at the push's peak
      tl.fromTo(cam, at(17.5, 1, 0.31), Object.assign(at(18.5, 0, 0.335), { duration: 3.12, ease: "none", immediateRender: true }), S(70.72));
      tl.to(cam, Object.assign(at(23.5, -3, 0.5), { duration: 0.42, ease: E.in }), S(73.84));
      tl.to(cam, Object.assign(at(23.5, -3, 0.53), { duration: 2.6, ease: "none" }), S(74.26));
      tl.to(cam, Object.assign(at(23.5, -3, 0.45), { duration: 1.6, ease: E.cam }), S(77.0));     // pull back to show both sides
      tl.to(cam, Object.assign(at(23.5, -3, 0.44), { duration: 3.9, ease: "none" }), S(78.6));
      FX.focusHunt(tl, cam, S(74.30), { dur: 0.7 });
      const [qx, qy] = ll(23.5, -3);
      FX.contrastCallout(tl, $("sc014-veil"), S(74.10), { w: 7055, h: 3731, d: MAPS.africa.d.dem_rep_congo, feather: 14, color: "rgba(20,22,26,1)", strength: 0.72 });
      tl.to(document.getElementById("c4s01-af-dem_rep_congo"), { attr: { "fill-opacity": 0.45, "stroke-width": 9 }, duration: 0.001 }, S(74.10));
      [T(71.06), T(71.38)].forEach((c, i) => rise(words("sc013-nc")[i], c, { dur: 0.8, y: 10 }));
      rise($("sc013-af"), T(73.22), { dur: 0.25, y: 10 });
      tl.to([$("sc013-af"), $("sc013-nc")], { opacity: 0, duration: 0.25 }, S(74.05));
      // C4S014: a celadon rope to Taiwan, a red rope to the CCP — they tug alternately (12 fps)
      const cn = $("sc014-cnsvg"), dcn = MAPS.eurasia.d.china;
      const nums = dcn.match(/-?\d+(\.\d+)?/g).map(Number); let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
      for (let i = 0; i < nums.length; i += 2) { x0 = Math.min(x0, nums[i]); x1 = Math.max(x1, nums[i]); y0 = Math.min(y0, nums[i + 1]); y1 = Math.max(y1, nums[i + 1]); }
      const sc = 280 / Math.max(x1 - x0, y1 - y0);
      cn.innerHTML = `<g transform="translate(${(150 - (x0 + x1) / 2 * sc).toFixed(1)} ${(150 - (y0 + y1) / 2 * sc).toFixed(1)}) scale(${sc.toFixed(4)})"><path d="${dcn}" fill="url(#c4s01-ht-red)" stroke="${RED}" stroke-width="${(3 / sc).toFixed(1)}"/></g>`;
      tl.fromTo($("sc014-tw"), { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(76.10));
      tl.fromTo($("sc014-cn"), { opacity: 0, x: 40 }, { opacity: 1, x: 0, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(77.08));
      rise($("sc014-twl"), T(76.18), { dur: 0.8, y: 10 });
      pop($("sc014-ccpb"), T(77.14), 0.8);
      const rope = $("sc014-rope");
      rope.innerHTML = `<path id="c4s01-r-tw" fill="none" stroke="${CEL}" stroke-width="9" stroke-linecap="round"/><path id="c4s01-r-cn" fill="none" stroke="${RED}" stroke-width="9" stroke-linecap="round"/>`;
      const rt = document.getElementById("c4s01-r-tw"), rc = document.getElementById("c4s01-r-cn");
      const st = { a: 0, b: 0, s1: 90, s2: 90, x: 0 };
      const draw = () => {
        const cx = 960 + st.x;
        rt.setAttribute("d", `M330 520 Q${(330 + cx) / 2} ${540 + st.s1} ${cx - 20} 548`);
        rc.setAttribute("d", `M${cx + 20} 548 Q${(cx + 1590) / 2} ${540 + st.s2} 1590 520`);
        const lt = rt.getTotalLength(), lc = rc.getTotalLength();
        rt.setAttribute("stroke-opacity", st.a > 0.01 ? 1 : 0); rc.setAttribute("stroke-opacity", st.b > 0.01 ? 1 : 0);
        rt.setAttribute("stroke-dasharray", `${lt} ${lt}`); rt.setAttribute("stroke-dashoffset", (lt * (1 - st.a)).toFixed(1));
        rc.setAttribute("stroke-dasharray", `${lc} ${lc}`); rc.setAttribute("stroke-dashoffset", (lc * (1 - st.b)).toFixed(1));
      };
      tl.fromTo(st, { a: 0 }, { a: 1, duration: 0.8, ease: C(E.out, 0.8), onUpdate: draw, immediateRender: false }, S(76.30));
      tl.fromTo(st, { b: 0 }, { b: 1, duration: 0.8, ease: C(E.out, 0.8), onUpdate: draw, immediateRender: false }, S(77.26));
      // tug of war: the ropes tighten alternately, the knot slides a little each way (ends centred, holds from 81.5)
      const tug = [[78.00, 10, 90, -40], [78.55, 90, 12, 34], [79.10, 14, 90, -30], [79.65, 90, 10, 28], [80.20, 12, 90, -22], [80.75, 60, 60, 0]];
      tug.forEach(([t, s1, s2, x]) => tl.to(st, { s1, s2, x, duration: 0.5, ease: C(E.inOut, 0.5), onUpdate: draw }, S(t)));
      draw();
      [T(77.94), T(78.26)].forEach((c, i) => rise(words("sc014-fo")[i], c, { dur: 0.6, y: 12 }));
      [T(81.70), T(82.02)].forEach((c, i) => rise(words("sc014-yc")[i], c, { dur: i ? 0.15 : 0.3, y: 8 }));
    })();

    /* =================== C4S015 · 82.56–88.64 · Taiwan … they send in aid, diplomat missions … whatever they can =================== */
    scene("sc015", 82.40, 88.64);
    ground("paper", S(82.56));
    (function () {
      tl.fromTo($("sc015-shot"), { x: 1990, rotation: 2 }, { x: 0, rotation: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(82.40));   // PS: paper slides in from the right
      tl.fromTo($("sc015-cam"), { scale: 1.0 }, { scale: 1.03, duration: 3.0, ease: "none", immediateRender: true }, S(82.56));
      tl.to($("sc015-cam"), { scale: 1.12, duration: 1.4, ease: E.cam }, S(86.20));
      tl.to($("sc015-cam"), { scale: 1.14, duration: 1.0, ease: "none" }, S(87.60));
      tl.to($("sc015-cam"), { scale: 1.3, x: -120, duration: 0.3, ease: E.in }, S(88.38));       // CA
      typeOn($("sc015-ty0"), T(82.90));
      typeOn($("sc015-ty1"), T(84.82));
      typeOn($("sc015-ty2"), T(85.94));
      typeOn($("sc015-ty3"), T(86.50));
      typeOn($("sc015-ty4"), T(87.70));
      typeOn($("sc015-ty5"), T(88.02), 1 / 30);
      typeOn($("sc015-ty6"), T(88.26), 1 / 30);
      // the paper-clipped card: a pencil route Taiwan → Africa on an atlas crop (missions abroad)
      tl.fromTo($("sc015-clip"), { opacity: 0, x: 120, y: 60, rotation: 12 }, { opacity: 1, x: 0, y: 0, rotation: 5, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(86.00));
      tl.fromTo($("sc015-pc"), { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(86.75));
      const r = $("sc015-route"), f = gated(86.4, 88.8, () => FX.markupDefs(r, "c4s01-mk015", { boil: 4 })); r.setAttribute("viewBox", "0 0 532 372");
      FX.markup.pen(tl, r, S(86.55), { points: [[515, 62], [400, 70], [260, 110], [110, 160], [67, 175]], dur: 0.9, width: 4, color: INK, filter: f, seed: 151, jitter: 3 });
      FX.markup.pen(tl, r, S(86.95), { points: [[400, 70], [300, 140], [200, 230], [130, 240]], dur: 0.8, width: 4, color: INK, filter: f, seed: 152, jitter: 3 });
      r.insertAdjacentHTML("beforeend", `<circle id="c4s01-sc015-tw" cx="515" cy="62" r="9" fill="${CEL}" stroke="${INK}" stroke-width="2.5"/>`);
    })();

    /* =================== C4S016 · 88.64–92.80 · to convince these countries to come on the Taiwanese side, ROC side =================== */
    scene("sc016", 88.64, 92.72);
    (function () {
      const svg = $("sc016-svg"), cam = $("sc016-cam"), K = 45.5111, z = 0.34;
      const ll = (lon, lat) => [(lon + 60) * K, (42 - lat) * K];
      const [cx, cy] = ll(14, 2);
      tl.fromTo(cam, { x: 960 - cx * 0.36, y: 540 - cy * 0.36, scale: 0.36 }, { x: 960 - cx * z, y: 540 - cy * z, scale: z, duration: 4.2, ease: E.cam, immediateRender: true }, S(88.64));
      const scr = (lon, lat) => { const [x, y] = ll(lon, lat); return [960 + (x - cx) * z, 540 + (y - cy) * z]; };
      const toMap = (X, Y) => [cx + (X - 960) / z, cy + (Y - 540) / z];
      const sides = [["c_te_d_ivoire", -5.5, 7.6], ["liberia", -9.4, 6.4], ["togo", 1.0, 8.6], ["gabon", 11.7, -0.6], ["malawi", 34.0, -13.3], ["madagascar", 46.8, -19.2], ["rwanda", 29.9, -2.0], ["niger", 9.0, 17.0]];
      svg.insertAdjacentHTML("beforeend", `<g id="c4s01-sc016-g" filter="url(#c4s01-wc)"></g><g id="c4s01-sc016-l"></g>`);
      const g = $("sc016-g"), lg = $("sc016-l");
      const [lx, ly] = toMap(1290, 905);
      sides.forEach(([k, lon, lat], i) => {
        const d = MAPS.africa.d[k]; if (!d) return;
        g.insertAdjacentHTML("beforeend", `<path id="c4s01-c16-${k}" d="${d}" fill="url(#c4s01-ht-cel)" stroke="${INK}" stroke-width="4" opacity="0"/>`);
        tl.fromTo(document.getElementById("c4s01-c16-" + k), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(89.00) + i / 6);
        const [x, y] = ll(lon, lat);
        ink(lg, `M${x.toFixed(0)} ${y.toFixed(0)} L${lx.toFixed(0)} ${ly.toFixed(0)}`, S(91.20) + i / 24, 0.45, { color: INK, width: 5 });
      });
      rise($("sc016-conv"), T(88.90), { dur: 0.9, y: 12 });
      [T(91.94), T(92.42)].forEach((c, i) => rise(words("sc016-roc")[i], c, { dur: i ? 0.15 : 0.25, y: 8 }));
      tl.fromTo($("sc016-rocu"), { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(92.05));
    })();
    whip($("sc016-shot"), $("sc017-shot"), S(92.72), { dir: 1 });

    /* =================== C4S017 · 92.80–96.96 · CCP does the same thing. Unfortunately, CCP is just a lot bigger =================== */
    scene("sc017", 92.72, 96.96);
    ground("night", S(92.72));
    (function () {
      const svg = $("sc017-svg"), cam = $("sc017-cam"), K = 45.5111;
      const ll = (lon, lat) => [(lon - 2) * K, (62 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      svg.insertAdjacentHTML("beforeend", `<defs><filter id="c4s01-glowr" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
        <g id="c4s01-sc017-cn" filter="url(#c4s01-glowr)"></g><g id="c4s01-sc017-tw"></g>`);
      pathsFill($("sc017-cn"), "eurasia", ["china"], `fill="url(#c4s01-ht-red)" fill-opacity="0.78" stroke="${RED}" stroke-width="8"`, "c4s01-cn17-");
      pathsFill($("sc017-tw"), "eurasia", ["taiwan"], `fill="${CEL}" stroke="${CEL}" stroke-width="10"`, "c4s01-tw17-");
      tl.fromTo($("sc017-cn"), { attr: { opacity: 0.0 } }, { attr: { opacity: 1 }, duration: 0.4, ease: C("none", 0.4), immediateRender: true }, S(92.78));
      tl.fromTo($("sc017-tw"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(95.10));
      tl.fromTo(cam, at(103, 35, 0.66), Object.assign(at(103, 34.5, 0.63), { duration: 2.6, ease: "none", immediateRender: true }), S(92.72));
      tl.to(cam, Object.assign(at(96, 33, 0.47), { duration: 1.1, ease: E.cam }), S(95.32));   // pull back: China at full size beside tiny Taiwan (lands 96.42)
      tl.to(cam, Object.assign(at(95.5, 33, 0.46), { duration: 0.6, ease: "none" }), S(96.42));
      FX.focusHunt(tl, cam, S(96.10), { dur: 0.6 });
      // "does the same thing": dashed red arrows out west (toward Africa)
      [[[95, 30], [55, 14]], [[92, 38], [52, 30]]].forEach(([a, b], i) => {
        const [x1, y1] = ll(a[0], a[1]), [x2, y2] = ll(b[0], b[1]);
        const p = ink(svg, `M${x1.toFixed(0)} ${y1.toFixed(0)} Q${((x1 + x2) / 2).toFixed(0)} ${((y1 + y2) / 2 - 300).toFixed(0)} ${x2.toFixed(0)} ${y2.toFixed(0)}`, S(93.55) + i * 0.15, 1.0, { color: RED, width: 14, ease: "sine.inOut" });
        p.setAttribute("opacity", "0.9");
      });
      pop($("sc017-ccpb"), T(92.74), 0.8);
      [T(93.54), T(93.70)].forEach((c, i) => rise(words("sc017-st")[i], c, { dur: 0.7, y: 10 }));
      tl.to($("sc017-st"), { opacity: 0, duration: 0.3 }, S(95.6));
      rise($("sc017-big"), T(96.42), { dur: 0.3, y: 10 });
      tl.to(cam, Object.assign(at(95.0, 33, 0.5), { duration: 0.2, ease: E.in }), S(96.80));     // CA into the bars
    })();

    /* =================== C4S018 · 96.96–101.36 · more access to … land and people, their resources are bigger than Taiwan =================== */
    scene("sc018", 96.96, 101.36);
    ground("paper", S(96.96));
    (function () {
      const rows = $("sc018-rows"), names = ["land", "people", "resources"], R = [1150, 1240, 1080], Cw = [120, 150, 100], cues = [T(98.82), T(99.22), T(99.78)];
      names.forEach((n, i) => {
        rows.insertAdjacentHTML("beforeend", `<div class="k-row" id="c4s01-sc018-r${i}" style="top:${300 + i * 190}px"><div class="lb t-label">${n}</div><div class="b r" style="width:${R[i]}px"><div class="ht"></div></div><div class="b c" style="width:${Cw[i]}px"><div class="ht"></div></div></div>`);
        const r = $("sc018-r" + i);
        rise(r.querySelector(".lb"), cues[i], { dur: 0.6, y: 8 });
        tl.fromTo(r.querySelector(".r"), { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, cues[i] + 0.04);
        tl.fromTo(r.querySelector(".c"), { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, cues[i] + 0.04);
      });
      [T(97.38), T(97.46), T(97.70)].forEach((c, i) => show(words("sc018-title")[i], c));
      show($("sc018-sw"), S(100.82));
      rise($("sc018-key"), T(100.82), { dur: 0.35, y: 8 });
      tl.fromTo($("sc018-shot"), { scale: 1.0 }, { scale: 1.03, duration: 4.4, ease: "none", immediateRender: false, transformOrigin: "40% 50%" }, S(96.96));
    })();
    whip($("sc018-shot"), $("sc019-shot"), S(101.36), { dir: 1, vertical: true });

    /* =================== C4S019–C4S020 · 101.36–113.60 · slowly, CCP is winning … African countries going towards the CCP =================== */
    scene("sc019", 101.36, 113.60);
    (function () {
      const svg = $("sc019-svg"), px = 960, py = 270, L = 430;
      // C4S019 — ink balance scale (our drawing): post, beam, two pans (celadon = Taiwan, red = CCP)
      svg.insertAdjacentHTML("beforeend", `<g fill="none" stroke="${INK}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M${px} ${py} L${px} 700"/><path d="M${px - 170} 720 Q${px} 660 ${px + 170} 720 Z" fill="#d9cfb9"/><circle cx="${px}" cy="${py - 26}" r="18" fill="${INK}"/></g>
        <g id="c4s01-bm"><path d="M${px - L} ${py} L${px + L} ${py}" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><circle cx="${px}" cy="${py}" r="16" fill="${PAPER}" stroke="${INK}" stroke-width="6"/></g>
        <g id="c4s01-panL"></g><g id="c4s01-panR"></g>`);
      const pan = (col, pat) => `<g fill="none" stroke="${INK}" stroke-width="5"><path d="M0 0 L-120 230 M0 0 L120 230"/></g><path d="M-150 230 Q0 330 150 230 Z" fill="url(#${pat})" stroke="${INK}" stroke-width="7"/><circle cx="0" cy="0" r="9" fill="${INK}"/>`;
      $("panL").innerHTML = pan(CEL, "c4s01-ht-cel"); $("panR").innerHTML = pan(RED, "c4s01-ht-red");
      const st = { a: -3 };
      const draw = () => {
        const r = st.a * Math.PI / 180, dx = L * Math.cos(r), dy = L * Math.sin(r);
        $("bm").setAttribute("transform", `rotate(${st.a.toFixed(2)} ${px} ${py})`);
        $("panL").setAttribute("transform", `translate(${(px - dx).toFixed(1)} ${(py - dy).toFixed(1)})`);
        $("panR").setAttribute("transform", `translate(${(px + dx).toFixed(1)} ${(py + dy).toFixed(1)})`);
      };
      draw();
      tl.fromTo(st, { a: -3 }, { a: 16, duration: 2.2, ease: C(E.inOut, 2.2), onUpdate: draw, immediateRender: false }, S(101.55));   // slowly tips to red (lands 103.75)
      pop($("sc019-ccpb"), T(102.18), 0.8);
      tl.fromTo($("sc019-ccp"), { y: 0 }, { y: 120, duration: 1.4, ease: C(E.inOut, 1.4), immediateRender: false }, S(102.3));
      rise($("sc019-win"), T(103.14), { dur: 0.6, y: 12 });
      // tilt down onto the GA hemicycle on the same sheet
      tl.fromTo($("sc019-sheet"), { y: 0 }, { y: -1080, duration: 1.1, ease: E.cam, immediateRender: false }, S(104.00));
      tl.to($("sc019-sheet"), { scale: 1.03, duration: 8.4, ease: "none", transformOrigin: "50% 75%" }, S(105.1));
      // C4S020 — hemicycle of member states (shapes only); the African wedge flips red, the celadon side shrinks
      const cx = 960, cy = 1990, rows = [[300, 14], [370, 17], [440, 20], [510, 23], [580, 26]], dots = [];
      rows.forEach(([r, n]) => { for (let k = 0; k < n; k++) { const a = Math.PI - k / (n - 1) * Math.PI; dots.push({ a, x: cx + Math.cos(a) * r, y: cy - Math.sin(a) * r }); } });
      dots.sort((p, q) => q.a - p.a);
      dots.forEach((d, i) => { svg.insertAdjacentHTML("beforeend", `<circle id="c4s01-gd${i}" cx="${d.x.toFixed(1)}" cy="${d.y.toFixed(1)}" r="14" fill="#9a958c"/>`); d.el = document.getElementById("c4s01-gd" + i); });
      svg.insertAdjacentHTML("beforeend", `<path d="M${cx - 640} ${cy + 30} L${cx + 640} ${cy + 30}" stroke="${INK}" stroke-width="3" opacity="0.6"/>
        <path id="c4s01-celarc" d="M${cx + 655} ${cy} A655 655 0 0 0 ${cx + 655 * Math.cos(1.75)} ${cy - 655 * Math.sin(1.75)}" fill="none" stroke="${CEL}" stroke-width="16" stroke-linecap="round"/>`);
      const n = dots.length;
      // start: right side (a < 1.75 rad) celadon = votes with Taiwan
      dots.forEach((d) => { if (d.a < 1.75) d.el.setAttribute("fill", CEL); });
      const wedge = dots.filter((d) => d.a > 2.15);                     // the African block (left), flips red 105.6–107.9
      wedge.forEach((d, i) => tl.to(d.el, { attr: { fill: RED }, duration: 0.001 }, S(105.60) + Math.floor(i / 3) / 12));
      const swing = dots.filter((d) => d.a >= 1.35 && d.a <= 2.15).sort((p, q) => q.a - p.a);   // more follow, celadon side shrinks 108.3–112.4
      swing.forEach((d, i) => tl.to(d.el, { attr: { fill: RED }, duration: 0.001 }, S(108.30) + Math.floor(i / 2) / 12));
      const arc = document.getElementById("c4s01-celarc"), al = arc.getTotalLength();
      arc.setAttribute("stroke-dasharray", `${al} ${al}`);
      tl.fromTo(arc, { attr: { "stroke-dashoffset": 0 } }, { attr: { "stroke-dashoffset": al * 0.23 }, duration: 3.0, ease: C(E.inOut, 3.0), immediateRender: true }, S(108.30));
      [T(104.26), T(104.34), T(104.66), T(104.90), T(105.46)].forEach((c, i) => show(words("sc020-title")[i], c));
      tl.fromTo($("sc020-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: "sine.inOut", immediateRender: true }, S(105.02));
      pop($("sc020-ccpb"), T(107.54), 0.8);
      $("sc020-chair").innerHTML = CHAIR;
      tl.fromTo($("sc020-chair"), { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(110.30));
      [T(110.34), T(111.22)].forEach((c, i) => rise(words("sc020-cs")[i], c, { dur: 0.6, y: 8 }));
      tl.fromTo($("sc020-twr"), { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.25, ease: C(E.out, 0.25), immediateRender: true }, T(113.06));
    })();
    whip($("sc019-shot"), $("sc021-shot"), S(113.60), { dir: -1, vertical: true });

    /* =================== C4S021 · 113.60–120.00 · Even then, not a big issue. The US is with Taiwan, and it should all be good =================== */
    scene("sc021", 113.60, 120.45);
    ground("night", S(113.60));
    (function () {
      gated(113.5, 120.5, () => FX.weave($("sc021-weave"), { amp: 0.6, flicker: 0.025, seed: 2101 }));
      tl.fromTo($("sc021-cam"), { scale: 1.0 }, { scale: 1.06, duration: 6.4, ease: "none", immediateRender: true }, S(113.60));
      [T(114.26), T(114.58), T(114.66), T(114.90)].forEach((c, i) => show(words("sc021-nbi")[i], c));
      tl.to($("sc021-nbi"), { opacity: 0, duration: 0.4 }, S(116.9));
      [T(115.54), T(115.70), T(116.18), T(116.42), T(116.66)].forEach((c, i) => show(words("sc021-us")[i], c));
      tl.fromTo($("sc021-twu"), { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(116.78));
    })();

    /* =================== C4S022 · 120.00–127.44 · the diplomatic front, diplomatic war … between the ROC and the CCP in the 70s =================== */
    scene("sc022", 119.80, 127.44);
    (function () {
      const shot = $("sc022-shot");
      const m = "url('assets/textures/watercolour_edge_mask_01.png') top / 100% 60px no-repeat, linear-gradient(#000, #000) 0 58px / 100% 100% no-repeat";
      tl.set(shot, { maskImage: m, webkitMaskImage: m }, S(119.79));
      tl.fromTo(shot, { y: 1140 }, { y: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: false }, S(119.80));   // PS: torn-edge paper slides up over the photo
      tl.set(shot, { maskImage: "none", webkitMaskImage: "none" }, S(120.32));
      ground("paper", S(120.0));
      [T(122.74), T(123.30)].forEach((c, i) => rise(words("sc022-dw")[i], c, { dur: 0.7, y: 10 }));
      tl.fromTo($("sc022-rocr"), { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, T(124.90));
      pop($("sc022-ccpb"), T(125.78), 0.7);
      tl.fromTo($("sc022-tab"), { x: 420 }, { x: 0, duration: 0.42, ease: C(E.out, 0.42), immediateRender: true }, S(126.40));
      [T(126.50), T(126.66)].forEach((c, i) => show(words("sc022-tab")[i], c));
      tl.to($("sc022-tab"), { x: -40, duration: 0.5, ease: "none" }, S(126.94));
    })();

    /* =================== C4S023 · 127.44–134.51 · a big event, almost a seismic event that changes. The equation tremendously =================== */
    scene("sc023", 127.44, 134.51);
    ground("night", S(127.44));
    (function () {
      const svg = $("sc023-tr"); let g = `<g stroke="${BONE}" stroke-width="1.5" opacity="0.16">`;
      for (let i = 1; i < 10; i++) g += `<path d="M${i * 70.4} 0 L${i * 70.4} 574"/>`;
      for (let j = 1; j < 8; j++) g += `<path d="M0 ${j * 71.75} L704 ${j * 71.75}"/>`;
      g += `</g><path id="c4s01-trace" fill="none" stroke="#e9f2ea" stroke-width="3.2" stroke-linejoin="round" style="filter:drop-shadow(0 0 6px rgba(200,235,215,0.8))"/>`;
      svg.innerHTML = g;
      const tr = document.getElementById("c4s01-trace"), TE = S(130.16), W = 2.4;
      gated(127.3, 134.6, () => FX.onFrame((t) => {
        let d = "";
        for (let x = 0; x <= 704; x += 4) {
          const tw = t - (1 - x / 704) * W;                         // when this sample was written (right edge = now)
          let v = (FX.noise1(tw * 22, 23) - 0.5) * 26 + Math.sin(tw * 31) * 4;
          if (tw > TE) { const k = tw - TE; v += Math.sin(k * 46) * 230 * Math.exp(-k * 1.6) * (0.6 + 0.4 * FX.noise1(k * 9, 5)); }
          d += (x ? "L" : "M") + x + " " + Math.max(14, Math.min(560, 287 + v)).toFixed(1);
        }
        tr.setAttribute("d", d);
      }));
      // the frame shakes 4 px for 0.5 s on "seismic"
      const cam = $("sc023-cam");
      gated(130.1, 130.75, () => FX.onFrame((t) => { const k = t - TE; const a = k >= 0 && k <= 0.5 ? 4 * (1 - k / 0.5) : 0;
        cam.style.translate = `${((FX.noise1(t * 40, 3) - 0.5) * 2 * a).toFixed(1)}px ${((FX.noise1(t * 40, 9) - 0.5) * 2 * a).toFixed(1)}px`; }));
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.07, duration: 7.1, ease: "none", immediateRender: true }, S(127.44));
      [T(128.58), T(128.82)].forEach((c, i) => rise(words("sc023-be")[i], c, { dur: 0.7, y: 10 }));
      tl.fromTo($("sc023-sei"), { opacity: 0, scale: 1.12 }, { opacity: 1, scale: 1, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, T(130.10));
      tl.to([$("sc023-sei"), $("sc023-be")], { opacity: 0, duration: 0.35 }, S(132.20));
      [T(132.61), T(132.77)].forEach((c, i) => rise(words("sc023-eq")[i], c, { dur: 0.7, y: 10 }));
    })();
    whip($("sc023-shot"), $("sc024-shot"), S(134.51), { dir: 1, flash: true });

    /* =================== C4S024 · 134.51–139.71 · let me explain how the Taiwanese economy is at this point =================== */
    scene("sc024", 134.51, 139.71);
    (function () {
      gated(134.4, 139.8, () => FX.weave($("sc024-weave"), { amp: 0.6, flicker: 0.025, seed: 2401 }));
      tl.fromTo($("sc024-cam"), { scale: 1.0 }, { scale: 1.06, duration: 5.2, ease: "none", immediateRender: true }, S(134.51));
      tl.to($("sc024-cam"), { scale: 1.12, x: -60, duration: 0.3, ease: E.in }, S(139.41));      // CA
      [T(137.25), T(138.13)].forEach((c, i) => rise(words("sc024-te")[i], c, { dur: 0.8, y: 10 }));
    })();
