    // ---------- shared geometry helpers ----------
    const WK = 17.0667;
    const wll = (lon, lat) => [(lon + 180) * WK, (90 - lat) * WK];
    const wat = (lon, lat, z) => { const [x, y] = wll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
    // centre of the largest sub-path of an SVG path string (numeric, works while scenes are display:none)
    function centerD(d) {
      let best = null, ba = -1;
      d.split("M").filter(Boolean).forEach((sp) => {
        const n = sp.match(/-?\d+(?:\.\d+)?/g).map(Number); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        for (let i = 0; i + 1 < n.length; i += 2) { x0 = Math.min(x0, n[i]); x1 = Math.max(x1, n[i]); y0 = Math.min(y0, n[i + 1]); y1 = Math.max(y1, n[i + 1]); }
        const a = (x1 - x0) * (y1 - y0); if (a > ba) { ba = a; best = [(x0 + x1) / 2, (y0 + y1) / 2]; }
      });
      return best;
    }
    function worldOutlines(svg, op, w) {
      const g = document.createElementNS(NS, "g");
      g.setAttribute("fill", "none"); g.setAttribute("stroke", BONE); g.setAttribute("stroke-opacity", op); g.setAttribute("stroke-width", w); g.setAttribute("stroke-linejoin", "round");
      g.innerHTML = Object.values(MAPS.world.d).map((d) => `<path d="${d}"/>`).join("");
      svg.appendChild(g); return g;
    }
    const attrOn = (el, t, v) => tl.fromTo(el, { attr: { opacity: 0 } }, { attr: { opacity: v == null ? 1 : v }, duration: 0.001, immediateRender: true }, t);
    // seat horseshoe (motif shared with c4s01 C4S002: 11 seats, 5 permanent ink + 6 rotating; China = centre-top permanent seat)
    function horseshoe(svg, chinaCel) {
      const cx = 960, cy = 520, R = 290, RS = 392;
      const P = (r, a) => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)];
      const arc = (r, a0, a1) => { const p0 = P(r, a0), p1 = P(r, a1); return `M${p0[0].toFixed(1)} ${p0[1].toFixed(1)} A${r} ${r} 0 1 1 ${p1[0].toFixed(1)} ${p1[1].toFixed(1)}`; };
      svg.innerHTML = `<path d="${arc(R, 205, -25)}" fill="none" stroke="${INK}" stroke-width="64" opacity="0.9"/>
        <path d="${arc(R, 205, -25)}" fill="none" stroke="#ddd3bf" stroke-width="50"/>
        <path d="${arc(R - 60, 200, -20)}" fill="none" stroke="${INK}" stroke-width="2" stroke-dasharray="6 10" opacity="0.4"/>`;
      const seats = [];
      [134, 112, 90, 68, 46].forEach((a) => seats.push({ a, perm: true }));
      [156, 178, 200, 24, 2, -20].forEach((a) => seats.push({ a, perm: false }));
      seats.forEach((s, k) => {
        const [x, y] = P(RS, s.a); s.x = x; s.y = y;
        const china = s.a === 90 && s.perm;
        svg.insertAdjacentHTML("beforeend", `<circle id="${svg.id}-s${k}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="36" fill="${china && chinaCel ? CEL : (s.perm ? INK : PAPER)}" stroke="${INK}" stroke-width="${china ? 9 : 6}"/>`);
        s.el = document.getElementById(`${svg.id}-s${k}`); s.china = china;
      });
      return seats;
    }

    /* =================== C3S078 · 404.17–409.21 · And guess what? The world says the same thing. Majority of the world … =================== */
    scene("sc078", 404.17, 409.40);
    ground("night", 0);
    (function () {
      const svg = $("sc078-svg"), cam = $("sc078-cam"), shot = $("sc078-shot");
      worldOutlines(svg, 0.22, 4);
      svg.insertAdjacentHTML("beforeend", `<g id="c3s03-sc078-g" filter="url(#c3s03-glowS)"></g>`);
      const g = $("sc078-g");
      const att = 'fill="url(#c3s03-ht-celS)" stroke="' + CEL + '" stroke-width="5" opacity="0"';
      const w1 = REC.r1950.slice().sort((a, b) => centerD(MAPS.world.d[a])[0] - centerD(MAPS.world.d[b])[0]);
      const w2 = REC.r1969.filter((k) => !REC.r1950.includes(k)).sort((a, b) => centerD(MAPS.world.d[a])[0] - centerD(MAPS.world.d[b])[0]);
      const tw = pathsFill(g, "world", ["taiwan"], 'fill="' + CEL + '" stroke="' + CEL + '" stroke-width="8"', "c3s03-w78t-");
      const p1 = pathsFill(g, "world", w1, att, "c3s03-w78a-"), p2 = pathsFill(g, "world", w2, att, "c3s03-w78b-");
      p1.forEach((p, i) => attrOn(p, S(405.29) + Math.floor(i / 3) / 12));     // 12 fps, west → east
      p2.forEach((p, i) => attrOn(p, S(407.21) + Math.floor(i / 3) / 12));
      // hand-off from c3s02: incoming half of the whip (smeared in from the left), lands sharp by 404.34
      const wb = FX.whipDefs(defs, "c3s03-win");
      gsap.set(shot, { filter: "url(#c3s03-win)" }); tl.set(shot, { filter: "none" }, 0.2);
      tl.fromTo(shot, { x: -385, scale: 1.18 }, { x: 0, scale: 1, duration: 0.17, ease: "power3.out", immediateRender: true }, 0);
      const sb = { v: 90 }; wb.setAttribute("stdDeviation", "90 0");
      tl.fromTo(sb, { v: 90 }, { v: 0, duration: 0.17, ease: "power2.out", immediateRender: true, onUpdate: () => wb.setAttribute("stdDeviation", `${sb.v.toFixed(1)} 0`) }, 0);
      tl.fromTo(cam, wat(4, 15, 0.42), Object.assign(wat(10, 18, 0.46), { duration: 5.3, ease: "none", immediateRender: true }), 0);
      [T(405.07), T(405.23)].forEach((c, i) => rise(words("sc078-tw")[i], c, { dur: 0.8, y: 12 }));
      out($("sc078-tw"), S(406.85));
      rise(words("sc078-maj")[0], T(407.15), { dur: 0.9, y: 12 });
    })();

    /* =================== C3S079 · 409.21–412.33 · The United States is with the ROC, it's with the nationalists =================== */
    scene("sc079", 409.02, 412.33);
    ground("paper", S(409.12));
    slideIn($("sc079-shot"), S(409.20));
    (function () {
      const cam = $("sc079-cam");
      tl.fromTo(cam, { scale: 1.0, x: 0 }, { scale: 1.04, x: -20, duration: 2.9, ease: "none", immediateRender: true }, S(409.02));
      tl.to(cam, { scale: 1.13, duration: 0.4, ease: E.in }, S(411.93));                // CA: push accelerates into the cut
      tl.fromTo($("sc079-ph"), { y: 10 }, { y: -12, duration: 3.3, ease: "none", immediateRender: true }, S(409.02));
      tl.fromTo($("sc079-us"), { opacity: 0, y: 40, rotation: -9 }, { opacity: 1, y: 0, rotation: -5, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(409.31));
      tl.fromTo($("sc079-roc"), { opacity: 0, y: 40, rotation: 8 }, { opacity: 1, y: 0, rotation: 4, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(410.45));
      [T(409.31), T(409.63)].forEach((c, i) => rise(words("sc079-usw")[i], c, { dur: 0.8, y: 12 }));
      pop($("sc079-rocb"), T(410.51), 0.8);
    })();

    /* =================== C3S080 · 412.33–417.85 · it recognizes the ROC as the government of China, as all of China =================== */
    scene("sc080", 412.33, 417.87);
    ground("night", S(412.33));
    (function () {
      const svg = $("sc080-svg"), cam = $("sc080-cam"), K = 45;
      const ll = (lon, lat) => [(lon - 70) * K, (56 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      const [tx, ty] = ll(121, 23.7);
      svg.innerHTML = `<defs><clipPath id="c3s03-sc080-clip"><circle id="c3s03-sc080-cc" cx="${tx}" cy="${ty}" r="0"/></clipPath></defs>
        <g fill="none" stroke="${BONE}" stroke-opacity="0.35" stroke-width="3"><path d="${MAPS.asia.d.china}"/><path d="${MAPS.asia.d.mongolia}"/></g>
        <g id="c3s03-sc080-cn" clip-path="url(#c3s03-sc080-clip)" filter="url(#c3s03-glow)"><path d="${MAPS.asia.d.china}" fill="url(#c3s03-ht-cel)" fill-opacity="0.8" stroke="${CEL}" stroke-width="8"/></g>
        <g id="c3s03-sc080-tw" opacity="0" filter="url(#c3s03-glow)"><path d="${MAPS.asia.d.taiwan}" fill="${CEL}" fill-opacity="0.9" stroke="${CEL}" stroke-width="6"/></g>`;
      tl.fromTo(cam, at(119, 25.5, 1.25), Object.assign(at(105, 35.5, 0.64), { duration: 4.2, ease: E.cam, immediateRender: true }), S(412.33));
      tl.to(cam, Object.assign(at(105, 35.5, 0.62), { duration: 1.4, ease: "none" }), S(416.53));
      tl.fromTo($("sc080-tw"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.5, ease: C("none", 0.5), immediateRender: true }, S(413.15));
      const cc = $("sc080-cc"), st = { r: 0 };
      tl.fromTo(st, { r: 0 }, { r: 2600, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true, onUpdate: () => cc.setAttribute("r", st.r.toFixed(0)) }, S(416.67));
      rise($("sc080-rec"), T(413.15), { dur: 0.9, y: 12 });
      out($("sc080-rec"), S(415.9));
      [T(416.67), T(416.91), T(417.15)].forEach((c, i) => rise(words("sc080-all")[i], c, { dur: 0.35, y: 10 }));
    })();
    whip($("sc080-shot"), $("sc081-shot"), S(417.79), { dir: 1, flash: true });

    /* =================== C3S081 · 417.85–423.45 · Same thing with all the US allies … including Japan after the war =================== */
    scene("sc081", 417.79, 423.45);
    (function () {
      const names = ["Australia", "Belgium", "Canada", "France", "Greece", "Italy", "Japan", "Luxembourg", "New Zealand", "Philippines", "Portugal", "South Korea", "Spain", "Thailand", "Turkey"];
      const list = $("sc081-list");
      list.innerHTML = names.map((n, i) => `<div class="k-row" id="c3s03-sc081-r${i}" style="top:${i * 76}px; filter:blur(6px); opacity:0.7"><div class="n t-label">${n}</div><div class="b" style="width:${150 + (i * 37) % 90}px"></div><div class="r"></div></div>`).join("");
      const jp = $("sc081-r6");
      tl.fromTo(list, { y: 330 }, { y: 120, duration: 4.1, ease: "none", immediateRender: true }, S(417.79));
      tl.to(list, { y: 540 - 6 * 76 - 35, duration: 0.6, ease: C(E.out, 0.6) }, S(421.89));
      tl.to(list, { y: 540 - 6 * 76 - 60, duration: 0.95, ease: "none" }, S(422.50));
      // focus pull: JAPAN racks into focus, the rest falls further out
      tl.fromTo(jp, { filter: "blur(6px)", opacity: 0.7, scale: 1 }, { filter: "blur(0px)", opacity: 1, scale: 1.3, duration: 0.45, ease: C(E.out, 0.45), immediateRender: false, transformOrigin: "0% 50%" }, T(421.95));
      tl.to(names.map((n, i) => i).filter((i) => i !== 6).map((i) => $("sc081-r" + i)), { filter: "blur(10px)", opacity: 0.4, duration: 0.45, ease: "sine.out" }, S(421.95));
      [T(418.99), T(419.39)].forEach((c, i) => rise(words("sc081-hd")[i], c, { dur: 0.8, y: 10 }));
    })();

    /* =================== C3S082 · 423.45–428.33 · even though Japan just fought the United States and Taiwan before =================== */
    scene("sc082", 423.45, 428.47);
    (function () {
      gated(423.4, 428.5, () => FX.weave($("sc082-weave"), { amp: 1.3, flicker: 0.04, seed: 82 }));
      tl.fromTo($("sc082-shot"), { scale: 1.0 }, { scale: 1.05, duration: 5.0, ease: "none", immediateRender: true }, S(423.45));
      rise(words("sc082-txt")[0], T(424.03), { dur: 0.8, y: 12 });
      rise(words("sc082-txt")[1], T(424.75), { dur: 0.8, y: 12 });
    })();

    /* =================== C3S083 · 428.33–433.05 · It recognizes Taiwan as the true government of China =================== */
    scene("sc083", 428.08, 433.13);
    ground("paper", S(428.15));
    slideIn($("sc083-shot"), S(428.27));
    (function () {
      tl.fromTo($("sc083-cam"), { scale: 1.0 }, { scale: 1.05, duration: 4.7, ease: "none", immediateRender: true }, S(428.27));
      pop($("sc083-jp"), S(428.40), 0.7);
      pop($("sc083-tw"), S(429.47), 0.8);
      rise($("sc083-twl"), T(429.47), { dur: 0.7, y: 10 });
      const mk = $("sc083-mk"), f = gated(428.0, 433.2, () => FX.markupDefs(mk, "c3s03-mk083", { boil: 4 }));
      FX.markup.pen(tl, mk, S(429.70), { points: [[690, 360], [960, 300], [1230, 370]], dur: 0.8, width: 7, color: INK, filter: f, seed: 83 });
      FX.markup.pen(tl, mk, S(430.45), { points: [[1196, 334], [1232, 370], [1190, 398]], dur: 0.25, width: 7, color: INK, filter: f, seed: 84 });
      [T(430.91), T(431.39)].forEach((c, i) => rise(words("sc083-tg")[i], c, { dur: 0.5, y: 8 }));
      gsap.set($("sc083-hl"), { scaleX: 0 });
      tl.fromTo($("sc083-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.85, ease: "sine.inOut", immediateRender: false }, S(431.02));
    })();
    whip($("sc083-shot"), $("sc084-shot"), S(432.99), { dir: 1, vertical: true });

    /* =================== C3S084 · 433.05–438.44 · The United Nations also recognizes the ROC as the true government of China =================== */
    scene("sc084", 432.99, 438.44);
    ground("night", S(433.0));
    (function () {
      const cam = $("sc084-cam");
      gated(432.9, 438.5, () => FX.weave($("sc084-wv"), { amp: 1.0, flicker: 0.035, seed: 84 }));
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.06, duration: 5.05, ease: "none", immediateRender: true }, S(432.99));
      tl.to(cam, { scale: 1.16, duration: 0.4, ease: E.in }, S(438.04));
      [T(433.23), T(433.71)].forEach((c, i) => rise(words("sc084-un")[i], c, { dur: 0.9, y: 14 }));
      out($("sc084-un"), S(435.25), 0.35);
      const mk = $("sc084-mk"), f = gated(435.4, 438.5, () => FX.markupDefs(mk, "c3s03-mk084", { boil: 12 }));
      FX.markup.circle(tl, mk, S(435.63), { cx: 990, cy: 470, rx: 250, ry: 300, rot: -8, dur: 0.7, color: BONE, width: 8, filter: f, seed: 184 });
      rise($("sc084-roc"), T(435.63), { dur: 0.8, y: 10 });
    })();

    /* =================== C3S085 · 438.44–443.24 · They have the permanent seat, they have a seat as China and the UN =================== */
    scene("sc085", 438.44, 443.26);
    ground("paper", S(438.44));
    (function () {
      const seats = horseshoe($("sc085-svg"), false), ch = seats.find((s) => s.china);
      const cam = $("sc085-cam");
      tl.fromTo(cam, { scale: 1.1 }, { scale: 1.0, duration: 1.3, ease: E.cam, immediateRender: true }, S(438.44));
      tl.to(cam, { scale: 1.04, duration: 3.5, ease: "none" }, S(439.74));
      tl.fromTo(ch.el, { attr: { fill: INK } }, { attr: { fill: CEL }, duration: 0.25, ease: C("none", 0.25), immediateRender: true }, S(439.50));
      tl.fromTo(ch.el, { attr: { r: 36 } }, { attr: { r: 46 }, duration: 0.25, ease: C("power2.out", 0.25), yoyo: true, repeat: 1, immediateRender: false }, S(439.50));
      [T(438.94), T(439.50)].forEach((c, i) => rise(words("sc085-ps")[i], c, { dur: 0.8, y: 12 }));
      [T(441.10), T(441.42)].forEach((c, i) => rise(words("sc085-ac")[i], c, { dur: 0.7, y: 10 }));
    })();
    whip($("sc085-shot"), $("sc086-shot"), S(443.18), { dir: -1, flash: true });

    /* =================== C3S086 · 443.24–451.96 · But there is a problem … the Soviet Union recognizing the CCP … communists =================== */
    scene("sc086", 443.18, 451.96);
    ground("night", S(443.2));
    (function () {
      const cam = $("sc086-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.03, duration: 2.3, ease: "none", immediateRender: true }, S(443.18));
      tl.to(cam, { scale: 1.12, duration: 0.48, ease: E.in }, S(445.50));        // ease-in push; the veil hard-cuts at its peak speed
      tl.to(cam, { scale: 1.18, duration: 5.6, ease: "none" }, S(445.98));
      tl.to(cam, { scale: 1.3, duration: 0.36, ease: E.in }, S(451.60));
      FX.contrastCallout(tl, $("sc086-veil"), S(445.88), { ellipse: [830, 360, 560, 300], feather: 40, color: "rgba(18,17,16,1)", strength: 0.62 });
      rise($("sc086-pr"), T(444.54), { dur: 0.9, y: 12 });
      out($("sc086-pr"), S(445.62), 0.25);
      [T(445.82), T(446.30)].forEach((c, i) => rise(words("sc086-su")[i], c, { dur: 0.8, y: 10 }));
      pop($("sc086-ccpb"), T(447.58), 0.8);
    })();

    /* =================== C3S087 · 451.96–455.40 · They are just brothers. You know, they're gonna recognize each other. On top of that, =================== */
    scene("sc087", 451.96, 455.42);
    ground("paper", S(451.96));
    (function () {
      tl.fromTo($("sc087-cam"), { scale: 1.04 }, { scale: 1.17, duration: 3.45, ease: E.cam, immediateRender: true }, S(451.96));
      rise($("sc087-br"), T(452.30), { dur: 0.9, y: 12 });
    })();
    whip($("sc087-shot"), $("sc088-shot"), S(455.34), { dir: 1 });

    /* =================== C3S088 · 455.40–462.20 · slowly the whole Soviet bloc, the Warsaw Pact, starts recognizing CCP as China =================== */
    scene("sc088", 455.34, 462.34);
    ground("night", S(455.34));
    (function () {
      const svg = $("sc088-svg"), cam = $("sc088-cam"), K = 45.5111;
      const ll = (lon, lat) => [(lon - 2) * K, (62 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      svg.insertAdjacentHTML("beforeend", `<defs><clipPath id="c3s03-gdr"><path d="${EUR.gdr_clip}"/></clipPath></defs>
        <g id="c3s03-sc088-su" filter="url(#c3s03-glow)"></g><g id="c3s03-sc088-sat" filter="url(#c3s03-glow)"></g><g id="c3s03-sc088-cn" opacity="0" filter="url(#c3s03-glow)"></g><g id="c3s03-sc088-pen"></g>`);
      const att = `fill="url(#c3s03-ht-red)" fill-opacity="0.8" stroke="${RED}" stroke-width="6" opacity="0"`;
      const ussr = ["russia", "ukraine", "belarus", "lithuania", "latvia", "estonia", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan"];
      const sat = ["poland", "czechia", "slovakia", "hungary", "romania", "bulgaria", "albania"];
      const pu = pathsFill($("sc088-su"), "eurasia", ussr, att, "c3s03-e88-");
      const ps = pathsFill($("sc088-sat"), "eurasia", sat, att, "c3s03-e88-");
      $("sc088-sat").insertAdjacentHTML("beforeend", `<path id="c3s03-e88-gdr" d="${EUR.d.germany}" clip-path="url(#c3s03-gdr)" ${att}/>`);
      ps.splice(0, 0, $("e88-gdr") || document.getElementById("c3s03-e88-gdr"));
      pathsFill($("sc088-cn"), "eurasia", ["china"], `fill="url(#c3s03-ht-red)" fill-opacity="0.8" stroke="${RED}" stroke-width="7"`, "c3s03-e88c-");
      pu.forEach((p, i) => attrOn(p, S(455.50) + Math.floor(i / 2) / 12));
      ps.forEach((p, i) => attrOn(p, S(456.95) + i / 12));
      tl.fromTo($("sc088-cn"), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.5, ease: C("none", 0.5), immediateRender: true }, S(460.62));
      // camera: Europe → push (veil on the curve) → pan east to China
      tl.fromTo(cam, at(26, 47, 0.82), Object.assign(at(28, 47, 0.8), { duration: 1.6, ease: "none", immediateRender: true }), S(455.34));
      tl.to(cam, Object.assign(at(22, 49, 1.0), { duration: 0.6, ease: E.in }), S(456.95));
      tl.to(cam, Object.assign(at(23, 49, 1.02), { duration: 1.15, ease: "none" }), S(457.55));
      tl.to(cam, Object.assign(at(78, 38.5, 0.53), { duration: 1.7, ease: E.cam }), S(458.70));
      tl.to(cam, Object.assign(at(80, 38.5, 0.52), { duration: 1.8, ease: "none" }), S(460.40));
      FX.contrastCallout(tl, $("sc088-veil"), S(457.48), { w: 6190, h: 2139, ellipse: [870, 640, 560, 420], feather: 60, color: "rgba(18,17,16,1)", strength: 0.6, until: S(458.75) });
      FX.focusHunt(tl, cam, S(457.58), { dur: 0.7 });
      const [x1, y1] = ll(52, 54), [x2, y2] = ll(100, 37), qx = (x1 + x2) / 2, qy = y1 - 420;
      ink($("sc088-pen"), `M${x1.toFixed(0)} ${y1.toFixed(0)} Q${qx.toFixed(0)} ${qy.toFixed(0)} ${x2.toFixed(0)} ${y2.toFixed(0)}`, S(459.85), 0.75, { color: BONE, width: 16, ease: "sine.inOut" });
      const ang = Math.atan2(y2 - qy, x2 - qx), h = 90;
      ink($("sc088-pen"), `M${(x2 - h * Math.cos(ang - 0.5)).toFixed(0)} ${(y2 - h * Math.sin(ang - 0.5)).toFixed(0)} L${x2.toFixed(0)} ${y2.toFixed(0)} L${(x2 - h * Math.cos(ang + 0.5)).toFixed(0)} ${(y2 - h * Math.sin(ang + 0.5)).toFixed(0)}`, S(460.55), 0.2, { color: BONE, width: 16 });
      [T(456.38), T(456.86)].forEach((c, i) => rise(words("sc088-sb")[i], c, { dur: 0.6, y: 10 }));
      out($("sc088-sb"), S(457.30), 0.2);
      [T(457.42), T(458.22)].forEach((c, i) => rise(words("sc088-wp")[i], c, { dur: 0.8, y: 12 }));
      out($("sc088-wp"), S(459.70), 0.35);
      pop($("sc088-ccpb"), T(460.62), 0.6);
    })();

    /* =================== C3S089 · 462.20–468.28 · But that's not a big issue … because Taiwan has the seat of China in the UN =================== */
    scene("sc089", 461.95, 468.28);
    ground("paper", S(462.05));
    slideIn($("sc089-shot"), S(462.14), { from: "y", dist: 1200, rot: 0 });
    (function () {
      const seats = horseshoe($("sc089-svg"), true), ch = seats.find((s) => s.china);
      const cam = $("sc089-cam");
      tl.fromTo(cam, { scale: 1.0, y: 0 }, { scale: 1.03, y: 0, duration: 3.3, ease: "none", immediateRender: true }, S(461.95));
      tl.to(cam, { scale: 1.9, y: 300, duration: 1.6, ease: E.cam }, S(465.30));
      tl.to(cam, { scale: 1.98, y: 306, duration: 0.98, ease: "none" }, S(466.90));
      tl.to(cam, { scale: 2.35, y: 330, duration: 0.4, ease: E.in }, S(467.88));
      FX.focusHunt(tl, cam, S(466.85), { dur: 0.6 });
      tl.fromTo(ch.el, { attr: { r: 36 } }, { attr: { r: 44 }, duration: 0.25, ease: C("power2.out", 0.25), yoyo: true, repeat: 1, immediateRender: false }, S(466.20));
      [T(462.54), T(462.62), T(462.70), T(462.94)].forEach((c, i) => rise(words("sc089-nb")[i], c, { dur: 0.5, y: 10 }));
      out($("sc089-nb"), S(465.20), 0.3);
      [T(466.14), T(466.62), T(466.86)].forEach((c, i) => rise(words("sc089-sc")[i], c, { dur: 0.4, y: 8 }));
      gsap.set($("sc089-hl"), { scaleX: 0 });
      tl.fromTo($("sc089-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.8, ease: "sine.inOut", immediateRender: false }, S(466.20));
    })();

    /* =================== C3S090 · 468.28–473.08 · it doesn't matter if the Soviet Union is recognizing because Taiwan has the United States =================== */
    scene("sc090", 468.28, 473.10);
    ground("night", S(468.28));
    (function () {
      const svg = $("sc090-svg");
      svg.innerHTML = `<path id="c3s03-sc090-ls" d="M1380 452 Q1240 640 1070 700" fill="none" stroke="${RED}" stroke-width="4" stroke-dasharray="14 12" opacity="0"/>
        <path d="M660 452 Q760 640 850 700" fill="none" stroke="${BONE}" stroke-width="3" stroke-dasharray="10 12" opacity="0.3"/>`;
      ["us", "su", "tw"].forEach((k, i) => tl.fromTo($("sc090-" + k), { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(468.28) + i / 12));
      attrOn($("sc090-ls"), S(468.50), 0.8);
      tl.fromTo($("sc090-cam"), { scale: 1.04 }, { scale: 1.0, duration: 4.8, ease: "none", immediateRender: true }, S(468.28));
      [T(468.62), T(468.94)].forEach((c, i) => rise(words("sc090-dm")[i], c, { dur: 0.7, y: 10 }));
      out($("sc090-dm"), S(471.30), 0.3);
      [T(469.58), T(470.06)].forEach((c, i) => rise(words("sc090-sul")[i], c, { dur: 0.6, y: 8 }));
      // the USSR node greys out (doesn't matter)
      tl.to($("sc090-su"), { filter: "grayscale(1) brightness(0.55)", opacity: 0.45, borderColor: "#6b6f75", duration: 0.5, ease: C("none", 0.5) }, S(470.50));
      tl.to([$("sc090-sul")], { opacity: 0.4, duration: 0.5, ease: C("none", 0.5) }, S(470.50));
      tl.to($("sc090-ls"), { attr: { opacity: 0.15 }, duration: 0.5, ease: C("none", 0.5) }, S(470.50));
      ink(svg, "M890 700 Q700 600 600 455", S(471.64), 0.6, { color: BONE, width: 12, ease: C(E.out, 0.6) });
      [T(472.30), T(472.62)].forEach((c, i) => rise(words("sc090-usl")[i], c, { dur: 0.3, y: 8 }));
    })();
    whip($("sc090-shot"), $("sc091-shot"), S(473.02), { dir: -1, vertical: true });

    /* =================== C3S091 · 473.08–479.00 · because of the United States … more than enough support in the UN … not gonna get kicked out at all =================== */
    scene("sc091", 473.02, 479.02);
    ground("paper", S(473.02));
    (function () {
      const svg = $("sc091-svg");
      svg.innerHTML = `<path d="M950 380 L950 700" stroke="${INK}" stroke-width="5" stroke-dasharray="18 12"/>`;
      gsap.set($("sc091-bar"), { scaleX: 0 });
      tl.fromTo($("sc091-bar"), { scaleX: 0 }, { scaleX: 1, duration: 1.9, ease: C(E.out, 1.9), immediateRender: false }, S(474.68));
      tl.fromTo($("sc091-cam"), { x: 0 }, { x: -160, duration: 6.0, ease: "none", immediateRender: true }, S(473.02));
      [T(474.62), T(474.78), T(474.94), T(475.26)].forEach((c, i) => rise(words("sc091-t")[i], c, { dur: 0.7, y: 10 }));
      [T(477.58), T(477.98)].forEach((c, i) => rise(words("sc091-ko")[i], c, { dur: 0.4, y: 8 }));
    })();
    whip($("sc091-shot"), $("sc092-shot"), S(478.94), { dir: 1, flash: true });

