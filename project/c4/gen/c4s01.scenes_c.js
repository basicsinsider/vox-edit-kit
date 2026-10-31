    /* war-room atlas (motif master, C4S022 + C4S025): same plate, same pins (celadon = ROC/Taiwan, red = CCP), pen front line */
    function warRoom(id, a, b, dur, t0) {
      const K = 17.0667, ll = (lon, lat) => [(lon + 180) * K, (90 - lat) * K];
      const at = (o) => { const [x, y] = ll(o.lon, o.lat); return { x: 960 - x * o.z, y: 540 - y * o.z, scale: o.z }; };
      tl.fromTo($(id + "-cam"), at(a), Object.assign(at(b), { duration: dur, ease: "none", immediateRender: true }), t0);
      const svg = $(id + "-svg");
      const roc = [[121.5, 24.5], [-5.5, 7.5], [34.0, -13.5], [11.6, -0.8], [45.0, 24.0], [-9.4, 6.4], [46.9, -19.0]];
      const ccp = [[116.4, 39.9], [35.0, -6.4], [-10.9, 10.4], [3.0, 28.0], [-4.0, 17.6], [45.3, 5.0], [15.3, -1.0]];
      const pins = { roc: [], ccp: [] };
      roc.forEach(([lon, lat], i) => { const [x, y] = ll(lon, lat); pins.roc.push(pin(svg, x, y, CEL, 24, `${SEG}-${id}-pr${i}`)); });
      ccp.forEach(([lon, lat], i) => { const [x, y] = ll(lon, lat); pins.ccp.push(pin(svg, x, y, RED, 24, `${SEG}-${id}-pc${i}`)); });
      return { ll, at, svg, pins };
    }
    const wr22 = warRoom("sc022", { lon: 52, lat: 12, z: 0.66 }, { lon: 58, lat: 11, z: 0.7 }, 7.44, S(120.0));
    wr22.pins.roc.forEach((p, i) => tl.fromTo(p, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(124.92) + i / 12));
    wr22.pins.ccp.forEach((p, i) => tl.fromTo(p, { attr: { opacity: 0 } }, { attr: { opacity: 1 }, duration: 0.001, immediateRender: true }, S(125.80) + i / 12));
    (function () {   // pen front line squiggling through Africa and the Middle East (the 'diplomatic war')
      const mk = wr22.svg, f = gated(122.6, 127.6, () => FX.markupDefs(mk, "c4s01-mk022", { boil: 4 })); mk.setAttribute("viewBox", "0 0 6144 3072");
      const pts = [[30, 36], [24, 30], [16, 24], [20, 16], [12, 9], [20, 3], [26, -4], [20, -10], [28, -18], [24, -28]].map(([lon, lat]) => wr22.ll(lon, lat));
      FX.markup.pen(tl, mk, S(122.75), { points: pts, dur: 1.2, width: 11, color: INK, filter: f, seed: 221, jitter: 14 });
    })();

    /* =================== C4S025 · 139.71–144.83 · while they are competing with the CCP to … win favors overseas =================== */
    scene("sc025", 139.71, 144.83);
    ground("paper", S(139.71));
    (function () {
      const w = warRoom("sc025", { lon: 30, lat: 14, z: 0.44 }, { lon: 20, lat: 10, z: 0.4 }, 4.84, S(139.71));
      tl.to($("sc025-cam"), Object.assign(w.at({ lon: -20, lat: 10, z: 0.4 }), { duration: 0.3, ease: E.in }), S(144.55));   // HC: whip-fast pan → hard cut
      const f = gated(140.2, 144.9, () => FX.markupDefs(w.svg, "c4s01-mk025", { boil: 4 })); w.svg.setAttribute("viewBox", "0 0 6144 3072");
      const race = (from, tos, col, t, seed) => tos.forEach(([lon, lat], i) => {
        const [x1, y1] = w.ll(from[0], from[1]), [x2, y2] = w.ll(lon, lat), mx = (x1 + x2) / 2, my = Math.min(y1, y2) - 260 - i * 60;
        FX.markup.pen(tl, w.svg, t + i * 0.18, { points: [[x1, y1 - 60], [mx, my], [x2, y2 - 60]], dur: 1.1, width: 14, color: col, filter: f, seed: seed + i, jitter: 10, blend: "normal" });
      });
      race([121.5, 24.5], [[-5.5, 7.5], [34.0, -13.5], [-58, -23], [-84, 12]], "#5f9479", S(140.30), 251);
      race([116.4, 39.9], [[35.0, -6.4], [-10.9, 10.4], [-77, 21], [3, 28]], RED, S(141.10), 261);
      rise($("sc025-comp"), T(140.35), { dur: 0.8, y: 12 });
      pop($("sc025-ccpb"), T(141.15), 0.8);
      rise($("sc025-ov"), T(143.87), { dur: 0.4, y: 8 });
    })();

    /* =================== C4S026 · 144.83–147.87 · this is where we have to back up just a little bit more =================== */
    scene("sc026", 144.83, 147.87);
    ground("night", S(144.83));
    (function () {
      const imgs = ["assets/c4/derived/c4s01/eurasia_night.jpg", "assets/c4/photos/eisenhower_chiang_motorcade_taipei_1960.jpg", "assets/c4/photos/un_general_assembly_hall_wide_emblem.jpg",
        "assets/c4/photos/mao_proclaims_prc_1949_tiananmen.jpg", "assets/c4/derived/c4s01/africa_night.jpg", "assets/c4/photos/un_security_council_1962_stevenson_chamber.jpg",
        "assets/c4/photos/eisenhower_chiang_motorcade_taipei_1960.jpg", "assets/c4/photos/mao_proclaims_prc_1949_tiananmen.jpg"];
      $("sc026-strip").innerHTML = imgs.map((s) => `<div class="k-fr"><img src="${s}" alt="" /></div>`).join("");
      gated(144.7, 148.0, () => FX.weave($("sc026-weave"), { amp: 2.2, flicker: 0.09, seed: 2601 }));
      tl.fromTo($("sc026-strip"), { y: -3700 }, { y: 0, duration: 3.04, ease: "none", immediateRender: true }, S(144.83));   // frames run backwards (downwards)
      tl.fromTo($("sc026-scr"), { opacity: 0.25 }, { opacity: 0.45, duration: 3.0, ease: "none", immediateRender: true }, S(144.83));
      FX.text.random(tl, $("sc026-b1"), T(146.19), { dur: 0.35, seed: 26 });
      FX.text.random(tl, $("sc026-b2"), T(146.43), { dur: 0.25, seed: 27 });
    })();
    whip($("sc026-shot"), $("sc027-shot"), S(147.87), { dir: -1 });

    /* =================== C4S027 · 147.87–154.83 · Taiwan was actually ruled by Japan before the ROC came over, before World War II =================== */
    scene("sc027", 147.87, 154.83);
    ground("paper", S(147.87));
    (function () {
      tl.fromTo($("sc027-cam"), { scale: 1.0 }, { scale: 1.06, duration: 6.6, ease: "none", immediateRender: true }, S(147.87));
      tl.to($("sc027-cam"), { scale: 1.3, x: 200, duration: 0.36, ease: E.in }, S(154.47));       // CA: push into the poster
      [T(150.27), T(150.91), T(151.15)].forEach((c, i) => rise(words("sc027-rbj")[i], c, { dur: 0.7, y: 14 }));
      tl.fromTo($("sc027-roc"), { x: 0 }, { x: -330, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, T(152.67));
      tl.fromTo($("sc027-ax"), { scaleX: 0 }, { scaleX: 1, duration: 0.8, ease: C(E.out, 0.8), immediateRender: true }, S(153.20));
      tl.fromTo($("sc027-tick"), { scaleY: 0 }, { scaleY: 1, duration: 0.3, ease: C(E.out, 0.3), immediateRender: true }, S(153.95));
      [T(154.03), T(154.27), T(154.51)].forEach((c, i) => show(words("sc027-ww")[i], c));
    })();

    /* =================== C4S028 · 154.83–161.39 · Japan took over the island of Taiwan in 1890s, during the Meiji era =================== */
    scene("sc028", 154.83, 161.39);
    ground("night", S(154.83));
    (function () {
      tl.fromTo($("sc028-cam"), { scale: 1.2, x: 150 }, { scale: 1.16, x: -150, duration: 6.56, ease: E.cam, immediateRender: true }, S(154.83));
      FX.text.odometer(tl, $("sc028-yr"), T(157.31), { dur: 0.7, stagger: 0.05, seed: 1895 });
      tl.to($("sc028-yr"), { opacity: 0, duration: 0.35 }, S(158.75));
      gated(158.2, 161.5, () => FX.roughDefs(defs, "c4s01-rough028", { freq: 0.03, scale: 7 }));   // torn-paper edge (permanent boil allowed on torn edges)
      tl.fromTo($("sc028-card"), { opacity: 0, y: 80, rotation: 10 }, { opacity: 1, y: 0, rotation: 4, duration: 0.9, ease: C(E.out, 0.9), immediateRender: true }, S(158.37));
      [T(158.43), T(159.15)].forEach((c, i) => rise(words("sc028-me")[i], c, { dur: 0.8, y: 10 }));
    })();
    whip($("sc028-shot"), $("sc029-shot"), S(161.39), { dir: 1, vertical: true });

    /* =================== C4S029 · 161.39–164.43 · and this rule continues until the end of World War II =================== */
    scene("sc029", 161.39, 164.43);
    ground("paper", S(161.39));
    (function () {
      tl.fromTo($("sc029-cam"), { scale: 1.0, x: 0 }, { scale: 1.03, x: -20, duration: 3.04, ease: "none", immediateRender: true }, S(161.39));
      tl.to($("sc029-cam"), { scale: 1.1, x: -80, duration: 0.3, ease: E.in }, S(164.13));    // CA
      show($("sc029-y"), S(161.45));
      tl.fromTo($("sc029-band"), { scaleX: 0 }, { scaleX: 1, duration: 1.7, ease: C(E.inOut, 1.7), immediateRender: true }, S(161.55));
      rise($("sc029-rule"), T(161.79), { dur: 0.6, y: 6 });
      tl.fromTo($("sc029-mark"), { scaleY: 0 }, { scaleY: 1, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(163.10));
      [T(163.15), T(163.31), T(163.47), T(163.79), T(164.03)].forEach((c, i) => show(words("sc029-end")[i], c));
    })();

    /* =================== C4S030–C4S031 · 164.43–174.35 · problems with Japanese rule … Japanese history in China … pretty brutal =================== */
    scene("sc030", 164.43, 174.70);
    ground("night", S(164.43));
    (function () {
      const cam = $("sc030-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.05, duration: 6.9, ease: "none", immediateRender: true }, S(164.43));
      tl.fromTo($("sc030-a"), { x: -20 }, { x: 25, duration: 7.0, ease: "none", immediateRender: true }, S(164.43));
      tl.fromTo($("sc030-b"), { x: 30, y: 0 }, { x: -20, y: -15, duration: 7.0, ease: "none", immediateRender: true }, S(164.43));
      rise($("sc030-pr"), T(165.39), { dur: 0.9, y: 12 });
      tl.to($("sc030-pr"), { opacity: 0, duration: 0.4 }, S(168.6));
      [T(169.47), T(170.03), T(170.43), T(170.59)].forEach((c, i) => show(words("sc030-jh")[i], c));
      tl.to($("sc030-jh"), { opacity: 0, duration: 0.3 }, S(171.6));
      // C4S031 — punch-in 10 %, the veil hard-cuts at the push's peak speed, BRUTAL chokes in and settles
      tl.to(cam, { scale: 1.16, duration: 0.4, ease: E.in }, S(171.39));
      tl.to(cam, { scale: 1.19, duration: 2.6, ease: "none" }, S(171.79));
      FX.contrastCallout(tl, $("sc031-veil"), S(171.72), { ellipse: [520, 450, 360, 270], feather: 40, color: "rgba(24,23,21,1)", strength: 0.7 });
      const ch = gated(173.4, 174.4, () => FX.roughDefs(defs, "c4s01-ch031", { freq: 0.04, scale: 7, choke: 0 }));
      show($("sc031-br"), T(173.63));
      FX.chokeSettle(tl, ch, $("sc031-br"), T(173.63), 12, 0.4, "none");
    })();

    /* =================== C4S032 · 174.35–181.55 · not as bad as some of the worst stories … doesn't mean there wasn't any brutality =================== */
    scene("sc032", 174.20, 181.55);
    (function () {
      tl.fromTo($("sc032-shot"), { x: -1990, rotation: -2 }, { x: 0, rotation: 0, duration: 0.5, ease: C(E.out, 0.5), immediateRender: true }, S(174.20));   // PS: paper slides in from the left
      ground("paper", S(174.35));
      tl.fromTo($("sc032-cam"), { scale: 1.0, x: 0 }, { scale: 1.07, x: -20, duration: 7.2, ease: "none", immediateRender: true }, S(174.35));
      [T(176.67), T(176.99)].forEach((c, i) => rise(words("sc032-ws")[i], c, { dur: 0.8, y: 12 }));
      const mk = $("sc032-mk"), f = gated(180.2, 181.7, () => FX.markupDefs(mk, "c4s01-mk032", { boil: 4 }));
      FX.markup.circle(tl, mk, S(180.45), { cx: 1005, cy: 395, rx: 135, ry: 165, rot: -8, dur: 0.55, color: INK, width: 7, filter: f, seed: 321 });
      rise($("sc032-br"), T(180.51), { dur: 0.5, y: 8 });
    })();
    whip($("sc032-shot"), $("sc033-shot"), S(181.55), { dir: 1, flash: true });

    /* =================== C4S033 · 181.55–184.67 · But there were positives from the Japanese rule =================== */
    scene("sc033", 181.55, 184.67);
    ground("night", S(181.55));
    (function () {
      const img = $("sc033-img");
      tl.fromTo($("sc033-cam"), { scale: 1.0 }, { scale: 1.08, duration: 3.12, ease: "none", immediateRender: true }, S(181.55));
      tl.fromTo(img, { filter: "grayscale(1) sepia(0) brightness(0.55) contrast(1.15)" }, { filter: "grayscale(1) sepia(0.62) brightness(0.92) contrast(1.05)", duration: 1.4, ease: C(E.out, 1.4), immediateRender: true }, S(182.45));
      gated(182.3, 184.8, () => FX.streaks($("sc033-str"), { seed: 331, speed: 0.5, tint: [255, 206, 158], lo: 0.4, gain: 1.1 }));
      tl.fromTo($("sc033-str"), { opacity: 0 }, { opacity: 0.55, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, S(182.40));
      rise($("sc033-pos"), T(182.51), { dur: 0.9, y: 14 });
    })();
    whip($("sc033-shot"), $("sc034-shot"), S(184.67), { dir: 1 });

    /* =================== C4S034–C4S035 · 184.67–194.74 · infrastructure: railways, ports, hydropower, electricity … primary school … a system =================== */
    scene("sc034", 184.67, 194.74);
    ground("paper", S(184.67));
    (function () {
      const cam = $("sc034-cam");
      tl.fromTo(cam, { x: 0, y: 0, scale: 1 }, { x: -40, duration: 2.9, ease: "none", immediateRender: true }, S(184.67));
      tl.to(cam, { x: -560, duration: 1.9, ease: E.cam }, S(187.80));
      tl.to(cam, { x: -660, duration: 0.9, ease: E.cam }, S(190.45));
      tl.to(cam, { x: 0, y: 141, scale: 0.738, duration: 1.5, ease: E.cam }, S(192.10));     // C4S035: pull back — the whole system
      tl.to(cam, { x: 10, y: 146, scale: 0.73, duration: 1.1, ease: "none" }, S(193.60));
      pop($("sc034-boxb"), T(186.75), 0.9);
      const card = (id, t, r0, r1) => tl.fromTo($(id), { opacity: 0, y: -50, rotation: r0, scale: 1.08 }, { opacity: 1, y: 0, rotation: r1, scale: 1, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, t);
      card("sc034-rail", T(187.87), -9, -3);
      card("sc034-port", T(188.43), 8, 2.5);
      card("sc034-hydro", T(188.91), -7, -2);
      card("sc034-elec", T(189.71), 9, 3);
      card("sc035-school", T(190.75), -8, -2.5);
      // electricity card: a pen pylon + power line + bulb (graphic; no Japanese-era power-line photo reachable)
      const pyl = $("sc034-pyl"), INKP = "#2a3140";
      ink(pyl, "M120 330 L170 60 L220 330 M138 230 L202 230 M150 160 L190 160 M110 90 L230 90 M95 110 L245 110", S(189.75), 0.5, { color: INKP, width: 5 });
      ink(pyl, "M110 90 Q60 120 0 110 M230 90 Q300 130 392 120", S(189.95), 0.4, { color: INKP, width: 3 });
      ink(pyl, "M300 190 Q300 150 330 150 Q360 150 360 190 Q360 215 345 230 L345 250 L315 250 L315 230 Q300 215 300 190 Z M318 262 L342 262", S(190.05), 0.4, { color: INKP, width: 5 });
      show($("sc035-sch2"), T(191.23));
      [T(191.55), T(191.71)].forEach((c, i) => rise(words("sc035-ps")[i], c, { dur: 0.6, y: 10 }));
      // pen lines connect every card into one network (C4S035)
      const net = $("sc035-net"), f = gated(192.3, 194.8, () => FX.markupDefs(net, "c4s01-mk035", { boil: 4 })); net.setAttribute("viewBox", "0 0 2600 1080");
      const c = { rail: [440, 520], port: [1040, 630], hydro: [1640, 475], elec: [2160, 680], school: [2240, 260], box: [560, 170] };
      [["box", "rail"], ["rail", "port"], ["port", "hydro"], ["hydro", "school"], ["hydro", "elec"], ["port", "elec"], ["box", "hydro"]].forEach(([a, b], i) =>
        FX.markup.pen(tl, net, S(192.40) + i * 0.12, { points: [c[a], [(c[a][0] + c[b][0]) / 2, (c[a][1] + c[b][1]) / 2 - 40], c[b]], dur: 0.6, width: 6, color: INK, filter: f, seed: 351 + i, jitter: 8 }));
      show($("sc035-sysb"), T(193.63));
      [T(193.63), T(193.87)].forEach((c2, i) => show(words("sc035-sys")[i], c2));
    })();
    whip($("sc034-shot"), $("sc036-shot"), S(194.74), { dir: 1, vertical: true });

    /* =================== C4S036 · 194.74–199.14 · That gave Taiwan a shot at being pretty good economy =================== */
    scene("sc036", 194.74, SEG_END);
    ground("night", S(194.74));
    (function () {
      // pans right→left over 6.0 s with the camera ease, so it is still moving at the c4s02 hand-off (199.14 → see NOTES)
      tl.fromTo($("sc036-cam"), { x: 0 }, { x: -2066, duration: 6.0, ease: E.cam, immediateRender: true }, S(194.74));
      [T(196.18), T(196.42)].forEach((c, i) => rise(words("sc036-as")[i], c, { dur: 0.8, y: 12 }));
      [T(198.10), T(198.42)].forEach((c, i) => rise(words("sc036-ge")[i], c, { dur: i ? 0.2 : 0.5, y: 8 }));
    })();
