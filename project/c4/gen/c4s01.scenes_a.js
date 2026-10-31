    /* =================== C4S001 · 0.00–8.00 · All of them have a veto … jurisdiction of the Security Council =================== */
    scene("sc001", 0, 8.00);
    ground("night", 0);
    (function () {
      const cam = $("sc001-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.03, duration: 0.88, ease: "none", immediateRender: true }, 0);
      tl.to(cam, { scale: 1.11, duration: 0.3, ease: E.in }, S(0.88));            // punch-in; the veil hard-cuts at its peak speed
      tl.to(cam, { scale: 1.15, duration: 6.4, ease: "none" }, S(1.18));
      tl.to(cam, { scale: 1.42, y: 60, duration: 0.42, ease: E.in }, S(7.58));    // CA: push on into the table top → the top-down diagram
      FX.contrastCallout(tl, $("sc001-veil"), S(1.14), { ellipse: [1000, 975, 1000, 200], feather: 50, color: "rgba(26,25,23,1)", strength: 0.7 });
      const ch = gated(0, 2.0, () => FX.roughDefs(defs, "c4s01-ch001", { freq: 0.04, scale: 7, choke: 0 }));
      $("sc001-veto").style.filter = "url(#c4s01-ch001)";
      tl.fromTo($("sc001-veto"), { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, T(1.14));
      FX.chokeSettle(tl, ch, $("sc001-veto"), T(1.14), 12, 0.6, "blur(0.45px)");
      tl.to($("sc001-veto"), { opacity: 0, duration: 0.5, ease: "power1.in" }, S(5.3));
      const mk = $("sc001-mk"), f = gated(0, 8.1, () => FX.markupDefs(mk, "c4s01-mk001", { boil: 4 }));
      FX.markup.circle(tl, mk, S(6.10), { cx: 990, cy: 905, rx: 860, ry: 175, rot: -2, dur: 0.9, color: BONE, width: 7, filter: f, seed: 101 });
      [T(6.82), T(7.30)].forEach((c, i) => rise(words("sc001-sc")[i], c, { dur: 0.45, y: 10 }));
    })();

    /* =================== C4S002–C4S003 · 8.00–21.31 · 5 permanent + 6 rotating = 11 · one vote · a veto beats 10 =================== */
    scene("sc002", 8.00, 21.66);
    ground("paper", S(8.00));
    (function () {
      const svg = $("sc002-svg"), cx = 960, cy = 520, R = 290, RS = 392;
      const P = (r, a) => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)];
      const arc = (r, a0, a1) => { const p0 = P(r, a0), p1 = P(r, a1); return `M${p0[0].toFixed(1)} ${p0[1].toFixed(1)} A${r} ${r} 0 1 1 ${p1[0].toFixed(1)} ${p1[1].toFixed(1)}`; };
      svg.innerHTML = `<path d="${arc(R, 205, -25)}" fill="none" stroke="${INK}" stroke-width="64" stroke-linecap="butt" opacity="0.9"/>
        <path d="${arc(R, 205, -25)}" fill="none" stroke="#ddd3bf" stroke-width="50" stroke-linecap="butt"/>
        <path d="${arc(R - 60, 200, -20)}" fill="none" stroke="${INK}" stroke-width="2" stroke-dasharray="6 10" opacity="0.4"/>`;
      // seats: 5 permanent at the top, 3 + 3 rotating on the arms
      const perm = [134, 112, 90, 68, 46], rot = [156, 178, 200, 24, 2, -20];
      const seats = [];
      perm.forEach((a, i) => seats.push({ a, perm: true, i }));
      rot.forEach((a, i) => seats.push({ a, perm: false, i }));
      seats.forEach((s, k) => {
        const [x, y] = P(RS, s.a);
        svg.insertAdjacentHTML("beforeend", `<g id="c4s01-seat${k}" opacity="0"><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="36" fill="${s.perm ? INK : PAPER}" stroke="${INK}" stroke-width="6"/></g>`);
        s.x = x; s.y = y; s.el = document.getElementById("c4s01-seat" + k);
      });
      seats.filter((s) => s.perm).forEach((s, i) => tl.fromTo(s.el, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(8.30) + i / 12));
      seats.filter((s) => !s.perm).forEach((s, i) => tl.fromTo(s.el, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(10.78) + i / 12));
      [T(8.26), T(8.74)].forEach((c, i) => rise(words("sc002-perm")[i], c, { dur: 0.7, y: 10 }));
      [T(10.74), T(11.06)].forEach((c, i) => rise(words("sc002-rot")[i], c, { dur: 0.7, y: 10 }));
      show($("sc002-11b"), T(12.66));
      FX.text.count(tl, $("sc002-n"), T(12.66), 0, 11, 0.4);
      rise($("sc002-mem"), T(12.98), { dur: 0.2, y: 6 });                          // §10.9: spoken in the last 0.5 s → short entrance
      tl.fromTo($("sc002-cam"), { scale: 1.14 }, { scale: 1.0, duration: 1.3, ease: E.cam, immediateRender: true }, S(8.00));
      tl.to($("sc002-cam"), { scale: 1.02, duration: 5.5, ease: "none" }, S(9.30));
      // C4S003 — one vote each (a tick per seat)
      tl.to([$("sc002-11"), $("sc002-mem"), $("sc002-perm"), $("sc002-rot")], { opacity: 0, duration: 0.3 }, S(13.75));
      seats.forEach((s, k) => {
        const ox = s.x + (s.x - cx) * 0.2, oy = s.y + (s.y - cy) * 0.2;
        ink(svg, `M${ox - 12} ${oy - 2} L${ox - 3} ${oy + 9} L${ox + 14} ${oy - 12}`, S(14.35) + k / 24, 0.18, { color: INK, width: 5 });
      });
      [T(14.29), T(14.53)].forEach((c, i) => rise(words("sc003-ov")[i], c, { dur: 0.6, y: 10 }));
      tl.to($("sc003-ov"), { opacity: 0, duration: 0.3 }, S(16.0));
      // the veto: a permanent seat stamps VETO
      const ch = gated(15.9, 17.0, () => FX.roughDefs(defs, "c4s01-ch003", { freq: 0.045, scale: 7, choke: 0 }));
      show($("sc003-stamp"), T(16.05));
      tl.fromTo($("sc003-stamp"), { scale: 1.35 }, { scale: 1, duration: 0.25, ease: "power2.in", immediateRender: true }, T(16.05));
      FX.chokeSettle(tl, ch, $("sc003-stamp"), T(16.05), 9, 0.5, "none");
      tl.fromTo($("sc003-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: "sine.inOut", immediateRender: true }, S(16.40));
      seats[2].el.querySelector("circle").setAttribute("stroke-width", "10");
      // the resolution card in the middle
      tl.fromTo($("sc003-card"), { opacity: 0, y: 30, rotation: -8 }, { opacity: 1, y: 0, rotation: -3, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(17.55));
      // ten seats say yes (12 fps wave): a fat check in every other seat
      seats.filter((s, k) => k !== 2).forEach((s, i) => {
        const c = s.perm ? PAPER : INK;
        ink(svg, `M${s.x - 15} ${s.y + 1} L${s.x - 4} ${s.y + 13} L${s.x + 17} ${s.y - 14}`, S(19.17) + Math.floor(i / 2) / 12, 0.12, { color: c, width: 7 });
      });
      tl.fromTo($("sc003-10"), { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.7, ease: C(E.out, 0.7), immediateRender: true }, T(19.17));
      // …and it's not gonna pass: cross over the card
      const mk = $("sc003-mk"), f = gated(20.3, 21.7, () => FX.markupDefs(mk, "c4s01-mk003", { boil: 4 }));
      FX.markup.cross(tl, mk, S(20.53), { x: 960, y: 555, s: 110, dur: 0.12, color: INK, width: 14, filter: f });
      [T(20.53), T(20.61), T(20.85)].forEach((c, i) => show(words("sc003-np")[i], c));
      tl.to($("sc002-cam"), { scale: 0.98, duration: 7.5, ease: "none" }, S(14.8));
      tl.to($("sc002-shot"), { x: -1990, rotation: -2, duration: 0.38, ease: E.in }, S(21.27));   // PS: paper slides away left, night underneath
    })();

    /* =================== C4S004 · 21.31–25.79 · That's not how things are in the General Assembly … a lot more jurisdiction =================== */
    scene("sc004", 21.27, 25.79);
    ground("night", S(21.45));
    (function () {
      tl.fromTo($("sc004-a"), { scale: 0.96 }, { scale: 1.0, duration: 0.7, ease: "none", immediateRender: true }, S(21.27));
      const mid = FX.curveCut(tl, $("sc004-wrap"), $("sc004-a"), $("sc004-b"), S(21.98), 0.84, { from: 1, to: 1.5 });
      show($("sc004-cr"), mid);
      tl.to($("sc004-wrap"), { scale: 0.2294, duration: 2.45, ease: E.cam }, S(22.84));   // pull out to the whole hall (lands 25.29)
      tl.to($("sc004-wrap"), { scale: 0.215, duration: 0.5, ease: "none" }, S(25.29));
      FX.focusHunt(tl, $("sc004-b"), S(23.10), { dur: 0.8 });
      [T(22.85), T(23.33)].forEach((c, i) => rise(words("sc004-gen")[i], c, { dur: 0.8, y: 14 }));
      tl.to($("sc004-gen"), { opacity: 0, duration: 0.3 }, S(24.10));
      [T(24.13), T(24.21), T(24.45), T(24.61)].forEach((c, i) => show(words("sc004-jur")[i], c));
    })();

    /* =================== C4S005 · 25.79–32.11 · General Assembly has a jurisdiction over who should get what seat (2.5D) =================== */
    scene("sc005", 25.79, 32.22);
    (function () {
      const P = 1200, Z = { L0: -420, L1: -140, L2: 180 };
      for (const [k, z] of Object.entries(Z)) gsap.set($("sc005-" + k), { z, scale: (P - z) / P });
      const cam = $("sc005-cam");
      tl.fromTo(cam, { x: 70, z: -90, rotationY: 2.2 }, { x: -30, z: 120, rotationY: -1.2, duration: 3.9, ease: E.cam, immediateRender: true }, S(25.79));
      tl.to(cam, { x: -40, z: 136, duration: 0.25, ease: "none" }, S(29.69));
      tl.to(cam, { x: -90, y: -40, z: 230, duration: 0.42, ease: E.in }, S(29.79));       // push; the veil hard-cuts at its peak (30.09)
      tl.to(cam, { x: -110, y: -50, z: 250, duration: 1.8, ease: "none" }, S(30.21));
      FX.focusHunt(tl, $("sc005-stage"), S(30.24), { dur: 0.8 });
      FX.contrastCallout(tl, $("sc005-veil"), S(30.09), { ellipse: [1150, 860, 270, 130], feather: 30, color: "rgba(26,25,23,1)", strength: 0.66 });
      rise($("sc005-jur"), T(28.53), { dur: 0.9, y: 12 });
      [T(30.05), T(30.45), T(30.69), T(31.01)].forEach((c, i) => show(words("sc005-who")[i], c));
      show($("sc005-seat"), T(31.33));
      tl.fromTo($("sc005-seathl"), { scaleX: 0 }, { scaleX: 1, duration: 0.2, ease: "sine.inOut", immediateRender: true }, S(31.36));
    })();
    whip($("sc005-shot"), $("sc006-shot"), S(32.22), { dir: 1 });   // §10.9: "seat" highlight lands 31.56, holds

    /* =================== C4S006 · 32.11–37.87 · a vote in the General Assembly decides who the Chinese seat belongs to =================== */
    scene("sc006", 32.22, 37.87);
    (function () {
      tl.fromTo($("sc006-cam"), { scale: 1.0 }, { scale: 1.08, duration: 5.76, ease: "none", immediateRender: true }, S(32.11));
      FX.focalBlur(tl, $("sc006-blur"), [
        { t: S(32.11), x: 470, y: 330, r: 210 },
        { t: S(32.95), x: 560, y: 650, r: 190, dur: 1.2 },          // the nameplate below the presidency card
        { t: S(34.55), x: 480, y: 280, r: 250, dur: 1.0 },          // cut to the delegate: the man in the Chinese seat
      ]);
      rise($("sc006-vote"), T(32.93), { dur: 0.9, y: 12 });
      tl.to($("sc006-vote"), { opacity: 0, duration: 0.3 }, S(35.2));
      [T(35.49), T(35.73), T(36.21)].forEach((c, i) => rise(words("sc006-cs")[i], c, { dur: 0.8, y: 14 }));
    })();
    whip($("sc006-shot"), $("sc007-shot"), S(37.87), { dir: -1, flash: true });

    /* =================== C4S007 · 37.87–43.15 · ever since the CCP started claiming that they're China, every single year =================== */
    scene("sc007", 37.87, 43.15);
    ground("paper", S(37.87));
    (function () {
      tl.fromTo($("sc007-cam"), { x: 0 }, { x: -30, duration: 5.3, ease: "none", immediateRender: true }, S(37.87));
      tl.fromTo($("sc007-crowd"), { y: 30 }, { y: -10, duration: 5.3, ease: "none", immediateRender: true }, S(37.87));
      tl.fromTo($("sc007-gate"), { y: -20 }, { y: 16, duration: 5.3, ease: "none", immediateRender: true }, S(37.87));
      tl.fromTo($("sc007-mao"), { scale: 1.0 }, { scale: 1.04, duration: 5.3, ease: "none", immediateRender: true }, S(37.87));
      pop($("sc007-ccpb"), T(39.49), 0.9);
      rise($("sc007-china"), T(41.65), { dur: 0.8, y: 12 });
      [T(42.29), T(42.53), T(42.77)].forEach((c, i) => show(words("sc007-eye")[i], c));
      tl.fromTo($("sc007-cal"), { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(41.95));
      [4, 3, 2, 1].forEach((k, i) => tl.fromTo($("sc007-pg" + k), { scaleY: 1, opacity: 1 }, { scaleY: -0.05, opacity: 0, duration: 1 / 6, ease: C("none", 1 / 6), immediateRender: false }, S(42.35) + i * 0.25));
    })();

    /* =================== C4S008 · 43.15–48.59 · especially from the Warsaw Pact … close to China or close to the CCP =================== */
    scene("sc008", 43.15, 48.70);
    ground("night", S(43.15));
    (function () {
      const svg = $("sc008-svg"), cam = $("sc008-cam"), K = 45.5111;
      const ll = (lon, lat) => [(lon - 2) * K, (62 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      svg.insertAdjacentHTML("beforeend", `<defs><clipPath id="c4s01-gdr"><path d="${MAPS.eurasia.gdr_clip}"/></clipPath>
        <filter id="c4s01-glowb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
        <g id="c4s01-sc008-wpg" opacity="0" filter="url(#c4s01-glowb)"></g><g id="c4s01-sc008-cng" opacity="0" filter="url(#c4s01-glowb)"></g>`);
      const wpg = $("sc008-wpg"), cng = $("sc008-cng");
      const wp = ["poland", "czechia", "slovakia", "hungary", "romania", "bulgaria", "albania", "russia", "ukraine", "belarus", "lithuania", "latvia", "estonia", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan"];
      pathsFill(wpg, "eurasia", wp, `fill="url(#c4s01-ht-bone)" stroke="${BONE}" stroke-width="5" stroke-opacity="0.8"`, "c4s01-wp-");
      wpg.insertAdjacentHTML("beforeend", `<path d="${MAPS.eurasia.d.germany}" clip-path="url(#c4s01-gdr)" fill="url(#c4s01-ht-bone)" stroke="${BONE}" stroke-width="5" stroke-opacity="0.8"/>`);
      pathsFill(cng, "eurasia", ["china"], `fill="url(#c4s01-ht-red)" stroke="${RED}" stroke-width="7"`, "c4s01-cn8-");
      tl.fromTo(cam, at(26, 52, 0.95), Object.assign(at(30, 50, 0.85), { duration: 2.4, ease: "none", immediateRender: true }), S(43.15));
      tl.to(cam, Object.assign(at(72, 39, 0.52), { duration: 1.7, ease: E.cam }), S(45.55));
      tl.to(cam, Object.assign(at(73, 39, 0.515), { duration: 1.4, ease: "none" }), S(47.25));
      FX.focusHunt(tl, cam, S(47.10), { dur: 0.7 });
      // Warsaw Pact lights up (12 fps steps), glow edge
      tl.fromTo(wpg, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.5, ease: C("none", 0.5), immediateRender: true }, S(44.55));
      [T(44.53), T(45.17)].forEach((c, i) => rise(words("sc008-wp")[i], c, { dur: 0.8, y: 10 }));
      // pen arrow from the bloc to China
      const [x1, y1] = ll(48, 50), [x2, y2] = ll(98, 37);
      const d = `M${x1.toFixed(0)} ${y1.toFixed(0)} Q${((x1 + x2) / 2).toFixed(0)} ${(y1 - 520).toFixed(0)} ${x2.toFixed(0)} ${y2.toFixed(0)}`;
      ink(svg, d, S(46.55), 0.9, { color: BONE, width: 16, ease: "sine.inOut" });
      const ang = Math.atan2(y2 - (y1 - 520), x2 - (x1 + x2) / 2), h = 90;
      ink(svg, `M${(x2 - h * Math.cos(ang - 0.5)).toFixed(0)} ${(y2 - h * Math.sin(ang - 0.5)).toFixed(0)} L${x2.toFixed(0)} ${y2.toFixed(0)} L${(x2 - h * Math.cos(ang + 0.5)).toFixed(0)} ${(y2 - h * Math.sin(ang + 0.5)).toFixed(0)}`, S(47.40), 0.2, { color: BONE, width: 16 });
      tl.fromTo(cng, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.25, ease: C("none", 0.25), immediateRender: true }, S(47.75));
      pop($("sc008-ccpb"), T(47.73), 0.3);
      tl.to(cam, Object.assign(at(80, 41, 0.6), { duration: 0.3, ease: E.in }), S(48.50));   // push → vertical whip
    })();
    whip($("sc008-shot"), $("sc009-shot"), S(48.70), { dir: 1, vertical: true });   // §10.9: China fill lands 48.00, holds

    /* =================== C4S009 · 48.59–54.67 · bring up a resolution … kick out this government that's sitting in Taiwan =================== */
    scene("sc009", 48.70, 54.67);
    ground("paper", S(48.70));
    (function () {
      const cam = $("sc009-cam");
      const at = (cx, cy, z) => ({ x: 960 - cx * z, y: 540 - cy * z, scale: z });
      tl.fromTo(cam, at(700, 860, 0.56), Object.assign(at(705, 900, 0.6), { duration: 1.0, ease: "none", immediateRender: true }), S(48.70));
      tl.to(cam, Object.assign(at(760, 1395, 1.12), { duration: 1.5, ease: E.cam }), S(49.70));
      tl.to(cam, Object.assign(at(770, 1400, 1.17), { duration: 3.2, ease: "none" }), S(51.20));
      tl.to(cam, Object.assign(at(780, 1250, 1.2), { duration: 0.36, ease: E.in }), S(54.31));   // CA: page slides up
      FX.focusHunt(tl, $("sc009-stage"), S(51.20), { dur: 0.7 });
      tl.fromTo($("sc009-page").querySelector(".ht"), { opacity: 0.15 }, { opacity: 0.4, duration: 1.5, ease: "none", immediateRender: true }, S(49.7));
      // text contrast call-out: the page dims, only the 'expel' lines come back through a feathered left→right wipe
      const key = $("sc009-key");
      key.style.clipPath = "polygon(810px 1342px, 1200px 1342px, 1200px 1391px, 1292px 1391px, 1292px 1434px, 160px 1434px, 160px 1391px, 810px 1391px)";
      const st = { p: -60 }, f = () => { const m = `linear-gradient(90deg, #000 ${st.p}%, transparent ${st.p + 60}%)`; key.style.maskImage = m; key.style.webkitMaskImage = m; };
      f();
      tl.fromTo($("sc009-dim"), { opacity: 0 }, { opacity: 0.8, duration: 0.9, ease: E.out, immediateRender: true }, S(50.85));
      tl.to(st, { p: 100, duration: 0.8, ease: E.inOut, onUpdate: f }, S(51.10));
      const mk = $("sc009-mk"), fp = gated(51.8, 54.8, () => FX.markupDefs(mk, "c4s01-mk009", { boil: 4 })); mk.setAttribute("viewBox", "0 0 1400 1808");
      FX.markup.pen(tl, mk, S(51.95), { points: [[812, 1392], [1000, 1394], [1196, 1390]], dur: 0.5, width: 5, color: INK, filter: fp, seed: 91 });
      FX.markup.pen(tl, mk, S(52.45), { points: [[166, 1436], [600, 1440], [1000, 1437], [1290, 1434]], dur: 0.8, width: 5, color: INK, filter: fp, seed: 92 });
      rise($("sc009-res"), T(49.01), { dur: 0.9, y: 10 });
      [T(50.85), T(51.17)].forEach((c, i) => rise(words("sc009-ko")[i], c, { dur: 0.7, y: 12 }));
      tl.fromTo($("sc009-twr"), { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.25, ease: C(E.out, 0.25), immediateRender: true }, T(54.05));
      tl.fromTo($("sc009-twu"), { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(54.12));
    })();

    /* =================== C4S010 · 54.67–59.07 · and let's give the CCP the Chinese seat, including the permanent veto =================== */
    scene("sc010", 54.67, 59.07);
    (function () {
      tl.fromTo($("sc010-cam"), { scale: 1.06, y: 40 }, { scale: 1.0, y: 0, duration: 1.0, ease: E.cam, immediateRender: true }, S(54.67));
      tl.to($("sc010-cam"), { scale: 1.02, duration: 3.4, ease: "none" }, S(55.67));
      $("sc010-chair").innerHTML = CHAIR;
      tl.fromTo($("sc010-chair"), { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(54.70));
      pop($("sc010-ccpb"), T(55.33), 0.8);
      const svg = $("sc010-svg"), f = gated(56.0, 59.2, () => FX.markupDefs(svg, "c4s01-mk010", { boil: 4 }));
      FX.markup.pen(tl, svg, S(56.10), { points: [[640, 790], [900, 730], [1150, 740], [1300, 800]], dur: 0.6, width: 7, color: INK, filter: f, seed: 101 });
      FX.markup.pen(tl, svg, S(56.68), { points: [[1255, 768], [1302, 802], [1250, 830]], dur: 0.15, width: 7, color: INK, filter: f, seed: 102, jitter: 2 });
      tl.to($("sc010-chair"), { x: 940, duration: 1.0, ease: C(E.inOut, 1.0) }, S(56.30));     // the seat moves ROC → CCP, lands 57.30
      [T(56.13), T(56.53)].forEach((c, i) => rise(words("sc010-cs")[i], c, { dur: 0.8, y: 12 }));
      [T(57.81), T(58.37)].forEach((c, i) => rise(words("sc010-pv")[i], c, { dur: i ? 0.2 : 0.6, y: 8 }));
    })();
    whip($("sc010-shot"), $("sc011-shot"), S(59.07), { dir: -1 });

    /* =================== C4S011 · 59.07–65.39 · every year this resolution is very heavily defeated … a habit =================== */
    scene("sc011", 59.07, 65.39);
    ground("night", S(59.07));
    (function () {
      const land = [[S(59.15), -60, -40, -6], [S(60.40), 50, -10, 4], [S(61.35), -20, 20, -2.5], [S(62.05), 30, 0, 2.5]];
      land.forEach(([t, x, y, r], k) => tl.fromTo($("sc011-d" + k), { opacity: k ? 0 : 1, x: x * 3, y: y - 260, rotation: r * 2, scale: 1.12 },
        { opacity: 1, x, y, rotation: r, scale: 1, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, t));
      [0, 1, 2].forEach((k) => gsap.set($("sc011-s" + k), { opacity: 0 }));
      const ch = gated(62.4, 63.3, () => FX.roughDefs(defs, "c4s01-ch011", { freq: 0.045, scale: 7, choke: 0 }));
      $("sc011-s3").style.filter = "url(#c4s01-ch011)";
      show($("sc011-s3"), T(62.53));
      tl.fromTo($("sc011-s3"), { scale: 1.4 }, { scale: 1, duration: 0.25, ease: "power2.in", immediateRender: true }, T(62.53));
      FX.chokeSettle(tl, ch, $("sc011-s3"), T(62.53), 9, 0.5, "none");
      tl.fromTo($("sc011-cam"), { scale: 1.0, y: 30, rotation: 0 }, { scale: 1.08, y: -10, rotation: -1.2, duration: 6.3, ease: "none", immediateRender: true }, S(59.07));
      [T(59.25), T(59.57)].forEach((c, i) => rise(words("sc011-ey")[i], c, { dur: 0.8, y: 10 }));
      tl.to($("sc011-ey"), { opacity: 0, duration: 0.3 }, S(62.2));
      rise($("sc011-hab"), T(64.93), { dur: 0.22, y: 8 });
      tl.to($("sc011-d3"), { x: 900, rotation: 10, duration: 0.3, ease: E.in }, S(65.12));   // CA: top page slides out
    })();

    /* =================== C4S012 · 65.39–70.72 · they bring it up, it gets defeated … how the votes are falling down =================== */
    scene("sc012", 65.39, 70.72);
    ground("paper", S(65.39));
    (function () {
      const svg = $("sc012-svg");
      const pts = [[200, 300], [330, 318], [460, 312], [590, 338], [720, 350], [850, 372], [980, 380], [1110, 410], [1240, 432], [1370, 470], [1500, 520], [1630, 640], [1760, 800]];
      const thr = 700;
      const d = "M" + pts.map((p) => p.join(" ")).join(" L");
      svg.innerHTML = `<defs><clipPath id="c4s01-c12"><rect id="c4s01-c12r" x="0" y="0" width="200" height="1080"/></clipPath></defs>
        <path d="M180 900 L1800 900" stroke="${INK}" stroke-width="4" opacity="0.8"/><path d="M180 240 L180 900" stroke="${INK}" stroke-width="4" opacity="0.8"/>
        <path d="M180 ${thr} L1800 ${thr}" stroke="${INK}" stroke-width="4" stroke-dasharray="18 14" opacity="0.65"/>
        <path d="${d} L1760 ${thr} L200 ${thr} Z" fill="${INK}" opacity="0.12" clip-path="url(#c4s01-c12)"/>`;
      const line = ink(svg, d, S(65.60), 4.4, { color: INK, width: 8, ease: "none" });
      tl.fromTo(svg.querySelector("#c4s01-c12r"), { attr: { width: 200 } }, { attr: { width: 1760 }, duration: 4.4, ease: "none", immediateRender: true }, S(65.60));
      // a tick (one defeat a year) pops on every point as the line passes it (12 fps)
      pts.forEach((p, i) => {
        svg.insertAdjacentHTML("beforeend", `<circle id="c4s01-p12-${i}" cx="${p[0]}" cy="${p[1]}" r="11" fill="${PAPER}" stroke="${INK}" stroke-width="5" opacity="0"/>`);
        tl.fromTo(document.getElementById("c4s01-p12-" + i), { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(65.60) + 4.4 * i / (pts.length - 1));
      });
      rise($("sc012-def"), T(66.69), { dur: 0.8, y: 10 });
      [T(69.38), T(69.94), T(70.26)].forEach((c, i) => rise(words("sc012-vfd")[i], c, { dur: i < 2 ? 0.5 : 0.2, y: 10 }));
      tl.fromTo($("sc012-cam"), { x: 30 }, { x: -40, duration: 5.3, ease: "none", immediateRender: true }, S(65.39));
    })();
    whip($("sc012-shot"), $("sc013-shot"), S(70.72), { dir: -1, vertical: true });
