    /* ============ C6S042 · 201.96–206.68 · Presidential Office film (whip lands from below) ============ */
    scene("042", 201.96, 206.68);
    ground("night", 0);
    (function () {
      const sc = $("sc042");
      // c6s01 owns the whip ↑ (first half 201.80–201.96 + SFX); the footage arrives from below, blurred, sharp by 202.12
      gsap.set(sc, { y: 385, scale: 1.18, filter: "url(#c6s02-wb042)" });
      blurs["042"].setAttribute("stdDeviation", "0 40");
      tl.fromTo(sc, { y: 385, scale: 1.18 }, { y: 0, scale: 1, duration: 0.16, ease: "power3.out", immediateRender: false }, 0);
      const b = { v: 40 };
      tl.fromTo(b, { v: 40 }, { v: 0, duration: 0.16, ease: "power2.out", immediateRender: false, onUpdate: () => blurs["042"].setAttribute("stdDeviation", "0 " + b.v.toFixed(2)) }, 0);
      tl.set(sc, { filter: "none" }, 0.2);
      weave("sc042-wv", 201.96, 206.7, 4201);
      tl.fromTo("#c6s02-sc042-cam", { scale: 1.0 }, { scale: 1.06, duration: 4.3, ease: "none", immediateRender: false }, 0);
      tl.to("#c6s02-sc042-cam", { scale: 1.22, duration: 0.42, ease: FX.ease.in }, S(206.26));   // CA: the push accelerates into the cut
      line("sc042-k", [["the ", T(202.68)], ["message", T(202.84)]]);
      line("sc042-s", [["Taiwanese ", T(204.36)], ["leaders", T(205.16)]]);
    })();

    /* ============ C6S043 · 206.68–215.40 · the father's card → the son's card ============ */
    scene("043", 206.68, 215.45);
    ground("paper", S(206.68));
    (function () {
      torn($("sc043-dad"), 4301); torn($("sc043-son"), 4302);
      tl.fromTo("#c6s02-sc043-cam", { scale: 1.1 }, { scale: 1.0, duration: 1.4, ease: FX.ease.cam, immediateRender: false }, S(206.68));
      line("sc043-k", [["the ", T(207.00)], ["main ", T(207.16)], ["leader", T(207.40)]]);
      line("sc043-e", [["economically", T(209.32)]]);
      line("sc043-dn", [["Chiang Kai-shek's", T(211.32)]]);
      // the son's card slides out from behind the father's (12 fps), camera trucks right with it
      const dad = ["#c6s02-sc043-dad", "#c6s02-sc043-tp1", "#c6s02-sc043-tp2", "#c6s02-sc043-dn"];
      tl.to(["#c6s02-sc043-k", "#c6s02-sc043-e"], { opacity: 0, duration: 0.3 }, S(212.3));
      tl.to(dad, { x: -440, duration: 1.2, ease: C(FX.ease.inOut, 1.2) }, S(212.62));
      tl.fromTo("#c6s02-sc043-son", { x: 0, rotation: 2.5 }, { x: 560, rotation: 3.5, duration: 1.2, ease: C(FX.ease.out, 1.2), immediateRender: false }, S(212.70));
      tl.to("#c6s02-sc043-cam", { x: -120, duration: 1.8, ease: FX.ease.cam }, S(212.7));
      const sn = $("sc043-sn");
      sn.innerHTML = '<div id="c6s02-sc043-sa" class="t-label c62-ink" style="font-size:30px"></div><div id="c6s02-sc043-sb" class="t-display" style="font-size:58px;margin-top:14px;opacity:0"><span class="c62-lbox">CHIANG CHING-KUO</span></div>';
      line("sc043-sa", [["son", T(212.76)]], { dur: 0.7 });
      pop("sc043-sb", T(213.72) - L, { dur: 0.8, from: 0.7 });   // §10.9: done 214.46, holds to the whip (215.24)
    })();

    /* ============ C6S044 · 215.40–218.68 · Chiang Ching-kuo (1965 film) — hero name odometer ============ */
    whip("043", "044", S(215.40), { dir: 1 });
    scene("044", 215.40, 218.73);
    ground("night", S(215.40));
    (function () {
      weave("sc044-wv", 215.4, 218.75, 4401);
      tl.fromTo("#c6s02-sc044-cam", { scale: 1.12 }, { scale: 1.2, duration: 3.3, ease: "none", immediateRender: false }, S(215.40));
      // no text on "Not being racist"; the name locks on "Chiang Ching-kuo" (217.16) — done 217.85
      FX.text.odometer(tl, $("sc044-name"), T(217.16) - L, { dur: 0.5, stagger: 0.015, spins: 6, seed: 4402 });
    })();

    /* ============ C6S045 · 218.68–221.72 · split: father | son ============ */
    whip("044", "045", S(218.68), { dir: -1 });
    flash(S(218.68));
    scene("045", 218.68, 221.72);
    ground("paper", S(218.68));
    (function () {
      const svg = $("sc045-svg"), f = FX.markupDefs(svg, "c6s02-mk45", { boil: 4 });
      FX.markup.pen(tl, svg, S(218.95), { points: [[958, 30], [963, 380], [957, 720], [962, 1050]], width: 7, color: INK, filter: f, dur: 0.9, seed: 4501 });   // done 219.85
      tl.fromTo("#c6s02-sc045-l", { x: -40 }, { x: 0, duration: 1.4, ease: FX.ease.cam, immediateRender: false }, S(218.68));
      tl.fromTo("#c6s02-sc045-r", { x: 40 }, { x: 0, duration: 1.4, ease: FX.ease.cam, immediateRender: false }, S(218.68));
      line("sc045-t", [["the ", T(221.00)], ["contrast", T(221.16)]], { dur: 0.35 });
      tl.to("#c6s02-sc045-cam", { scale: 1.55, duration: 0.47, ease: FX.ease.in }, S(221.25));   // CA: the father's half pushes in
      tl.to("#c6s02-sc045-r", { opacity: 0, duration: 0.3 }, S(221.4));
    })();

    /* ============ C6S046 · 221.72–227.56 · the dad was the military guy (film) ============ */
    scene("046", 221.72, 227.61);
    ground("night", S(221.72));
    (function () {
      weave("sc046-wv", 221.72, 227.6, 4601);
      tl.fromTo("#c6s02-sc046-cam", { scale: 1.25 }, { scale: 1.02, duration: 0.9, ease: FX.ease.cam, immediateRender: false }, S(221.72));
      tl.to("#c6s02-sc046-cam", { scale: 1.08, duration: 4.8, ease: "none" }, S(222.62));
      line("sc046-k", [["the ", T(222.44)], ["dad", T(222.60)]]);
      line("sc046-m", [["MILITARY", T(223.24)]], { dur: 1.1 });
      line("sc046-s", [["most ", T(224.52)], ["successful ", T(224.76)], ["generals", T(225.24)]]);
    })();

    /* ============ C6S047 · 227.56–235.48 · isotype ring: all military ============ */
    whip("046", "047", S(227.56), { dir: -1 });
    scene("047", 227.56, 235.48);
    ground("paper", S(227.56));
    (function () {
      const ring = $("sc047-ring"), CX = 1260, CY = 540, R = 330, N = 10;
      div("", "position:absolute;left:" + (CX - 75) + "px;top:" + (CY - 75) + "px;width:150px;height:150px;border-radius:50%;border:6px solid " + INK + ";background:url('assets/c6/photos/chiang_kai_shek_portrait_uniform.jpg') center 14%/cover;filter:grayscale(1) sepia(0.2) contrast(1.15);box-shadow:0 10px 20px rgba(20,27,36,0.3)", ring);
      const icons = [];
      for (let i = 0; i < N; i++) {
        const a = -Math.PI / 2 + (i / N) * Math.PI * 2;
        icons.push(icon(ring, "general", CX + Math.cos(a) * R, CY + Math.sin(a) * R * 0.92));
      }
      icons.forEach((d, i) => tl.fromTo(d, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.35, ease: C(FX.ease.out, 0.35), immediateRender: true }, S(227.70) + i / 12));   // ring done 228.8
      // spokes: advisers around the ruler
      const sv = $("sc047-tw");
      // Taiwan outline (kit), faint celadon, on "this island"
      sv.innerHTML = '<g transform="translate(' + (CX - PD.twBoxW * 0.27) + ',' + (CY - 270) + ') scale(0.54)"><path d="' + PD.twBox + '" fill="' + CEL + '" fill-opacity="0.32" stroke="#6f9a84" stroke-width="5"/></g>';
      tl.fromTo(sv, { opacity: 0 }, { opacity: 1, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(232.55));
      line("sc047-r", [["ruling", T(229.32)]]);
      line("sc047-g", [["governing ", T(231.96)], ["of ", T(232.44)], ["this ", T(232.60)], ["island", T(232.76)]]);
      $("sc047-a").innerHTML = '<span class="c62-lbox" id="c6s02-sc047-ab"></span>';
      tl.fromTo("#c6s02-sc047-ab", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(233.32) - L);
      line("sc047-ab", [["ALL ", T(233.32)], ["MILITARY", T(233.64)]], { dur: 0.5, y: 0 });
      icons.forEach((d, i) => tl.to(d, { scale: 1.14, duration: 1 / 12, yoyo: true, repeat: 1 }, S(233.62) + (i % 5) / 24));
      line("sc047-gn", [["generals", T(234.52)]], { dur: 0.45 });
      tl.fromTo("#c6s02-sc047-cam", { rotation: 0, scale: 1 }, { rotation: 4, scale: 1.05, duration: 7.92, ease: "none", immediateRender: false }, S(227.56));   // CA: still rotating at the cut
    })();

    /* ============ C6S048 · 235.48–238.92 · the kid is an engineer ============ */
    scene("048", 235.48, 238.97);
    ground("night", S(235.48));
    (function () {
      tl.fromTo("#c6s02-sc048-cam", { scale: 1.0 }, { scale: 1.05, duration: 3.4, ease: "none", immediateRender: false }, S(235.48));
      tl.fromTo("#c6s02-sc048-cut", { x: 40, opacity: 0.0 }, { x: 0, opacity: 1, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(235.48));
      const bp = $("sc048-bp"), o = { color: BONE, width: 3, opacity: 0.55 };
      ink(bp, "M1240 120 A 300 300 0 1 1 1239 120", S(236.15), 0.9, o);                       // compass circle round the head
      ink(bp, "M860 430 L1660 438", S(236.30), 0.6, o);                                         // centre line
      ink(bp, "M1243 60 L1238 1060", S(236.40), 0.7, o);
      ink(bp, "M900 980 L900 1010 L1600 1006 L1600 976", S(236.55), 0.6, o);                    // dimension line
      ink(bp, "M1700 200 L1702 900 M1680 200 L1720 200 M1680 900 L1720 902", S(236.65), 0.7, o);
      ink(bp, "M1240 420 A 140 140 0 0 1 1380 560", S(236.8), 0.5, o);                           // arc   — all done 237.5
      line("sc048-d", [["very ", T(236.20)], ["different", T(236.36)]]);
      tl.fromTo("#c6s02-sc048-e", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(238.36) - L);
      FX.chokeSettle(tl, ch48, $("sc048-ew"), T(238.36) - L, 6, 0.25);   // settled 238.63
    })();

    /* ============ C6S049 · 238.92–244.28 · Shanghai → Moscow on a tilted atlas ============ */
    whip("048", "049", S(238.92), { dir: -1, vertical: true });
    scene("049", 238.92, 244.28);
    ground("paper", S(238.92));
    (function () {
      gsap.set("#c6s02-sc049-plane", { rotationX: 22, rotationZ: -2, scale: 1.18 });
      const cam = $("sc049-cam");
      gsap.set(cam, { scale: 0.48, x: -420, y: -20 });
      const svg = $("sc049-svg"), f = FX.markupDefs(svg, "c6s02-mk49", { boil: 12 });
      svg.setAttribute("viewBox", "0 0 " + PD.euW + " " + PD.euH);
      const fill = el("path", { d: PD.ussr, fill: RED, opacity: 0 }, svg); fill.style.mixBlendMode = "multiply";
      const rt = PD.route.map((p, i) => (i ? "L" : "M") + p[0] + " " + p[1]).join(" ");
      ink(svg, rt, S(238.98), 0.72, { color: YEL, width: 26, filter: f, opacity: 0.9, blend: "multiply", ease: C("sine.inOut", 0.72) });   // reaches Moscow 239.70
      const pin = $("sc049-pin"); pin.style.left = PD.moscowEU[0] + "px"; pin.style.top = PD.moscowEU[1] + "px";
      tl.fromTo(pin, { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.4, ease: C(FX.ease.out, 0.4), immediateRender: true }, S(239.62));
      line("sc049-mo", [["Moscow", T(239.64)]]);
      // camera pushes to Moscow, focus hunt as it lands
      tl.fromTo(cam, { scale: 0.48, x: -420, y: -20 }, { scale: 1.2, x: 960 - PD.moscowEU[0] * 1.2 + 120, y: 540 - PD.moscowEU[1] * 1.2 - 60, duration: 1.0, ease: FX.ease.cam, immediateRender: false }, S(239.45));
      FX.focusHunt(tl, $("sc049-tilt"), S(240.45), { dur: 0.7 });
      pop("sc049-yc", S(240.62), { dur: 1.0, from: 0.7 });
      line("sc049-ty", [["teenage ", T(240.68)], ["years", T(241.24)]]);
      // the Soviet Union: red outline (1960 borders) + red underline
      ink(svg, PD.ussr, S(242.80), 0.85, { color: RED, width: 7, opacity: 0.9 });   // done 243.65
      tl.to(fill, { attr: { opacity: 0.16 }, duration: 0.7, ease: C(FX.ease.out, 0.7) }, S(242.9));
      tl.to(cam, { scale: 0.62, x: -460, y: -20, duration: 1.7, ease: FX.ease.cam }, S(242.70));   // CA: still pulling back at the cut
      tl.to("#c6s02-sc049-yc", { opacity: 0, y: -40, duration: 0.4, ease: C(FX.ease.in, 0.4) }, S(242.6));
      line("sc049-su", [["Soviet ", T(242.84)], ["Union", T(243.24)]]);
      const ul = $("sc049-ul"), f2 = FX.markupDefs(ul, "c6s02-mk49b", { boil: 4 });
      FX.markup.pen(tl, ul, S(242.92), { points: [[108, 966], [300, 962], [470, 968]], width: 7, color: RED, filter: f2, dur: 0.45, seed: 4901 });
    })();

    /* ============ C6S050 · 244.28–247.64 · TIME, April 1927 (he turns on the communists) ============ */
    scene("050", 244.28, 247.64);
    ground("night", S(244.28));
    (function () {
      tl.fromTo("#c6s02-sc050-cam", { scale: 1.0, y: 0 }, { scale: 1.08, y: -40, duration: 3.4, ease: "none", immediateRender: false }, S(244.28));
      line("sc050-t", [["turns ", T(244.84)], ["on ", T(245.32)], ["the ", T(245.48)], ["communists", T(245.56)]]);
      tl.fromTo("#c6s02-sc050-flag", { opacity: 0, x: 260, rotation: 14 }, { opacity: 1, x: 0, rotation: 8, duration: 0.45, ease: C(FX.ease.out, 0.45), immediateRender: true }, S(246.38));   // "Soviet Union" — done 246.83, holds to the slide (247.19)
    })();

    /* ============ C6S051 · 247.64–254.45 · hostage for 12 years — the ledger ============ */
    slide("051", S(247.64), "bottom");
    scene("051", 247.19, 254.45);
    ground("paper", S(247.4));
    (function () {
      const bx = $("sc051-boxes"), boxes = [];
      for (let i = 0; i < 12; i++) {
        const x = 470 + (i % 6) * 120, y = 250 + Math.floor(i / 6) * 160;
        const b = div("", "position:absolute;left:" + x + "px;top:" + y + "px;width:84px;height:84px;border:4px solid " + INK + ";", bx);
        const fl = div("", "position:absolute;inset:6px;background:" + INK + ";opacity:0;", b);
        boxes.push(fl);
      }
      tl.fromTo("#c6s02-sc051-cam", { scale: 1.0 }, { scale: 1.06, duration: 6.8, ease: "none", immediateRender: false }, S(247.64));
      tl.fromTo("#c6s02-sc051-host", { opacity: 0, scale: 1.35 }, { opacity: 0.9, scale: 1, duration: 0.12, ease: "power2.in", immediateRender: true }, T(248.04) - L);
      FX.chokeSettle(tl, ch51, $("sc051-hw"), T(248.04) - L, 3, 0.3);   // settled 248.4
      tl.fromTo("#c6s02-sc051-n", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(248.84) - L);
      FX.text.count(tl, $("sc051-num"), T(248.84) - L, 1, 12, 0.72);   // 12 at 249.5
      boxes.forEach((b, i) => tl.fromTo(b, { opacity: 0 }, { opacity: 0.85, duration: 0.001, immediateRender: true }, S(248.80) + i / 16));   // last box 249.49
      line("sc051-st", [["stuck", T(250.29)]]);
      line("sc051-sd", [["to ", T(252.05)], ["study", T(252.13)]]);
      const svg = $("sc051-svg"), f = FX.markupDefs(svg, "c6s02-mk51", { boil: 4 });
      FX.markup.pen(tl, svg, S(253.74), { points: [[640, 198], [900, 192], [1130, 199]], width: 6, color: INK, filter: f, dur: 0.15, seed: 5101 });
      FX.markup.pen(tl, svg, S(253.80), { points: [[650, 214], [910, 210], [1120, 216]], width: 6, color: INK, filter: f, dur: 0.15, seed: 5102 });   // done 253.95 — holds 0.5 s (§10.9)
    })();

    /* ============ C6S052 · 254.45–262.53 · sent to a plant to work; his dad leads China ============ */
    scene("052", 254.45, 262.58);
    ground("night", S(254.45));
    (function () {
      weave("sc052-wv", 254.45, 262.6, 5201);
      tl.fromTo("#c6s02-sc052-cam", { scale: 1.0 }, { scale: 1.1, duration: 8.1, ease: "none", immediateRender: false }, S(254.45));
      torn($("sc052-dad"), 5202);
      tl.fromTo("#c6s02-sc052-dad", { opacity: 1, x: 620, rotation: 9 }, { x: 0, rotation: 3, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(259.10));
      pop("sc052-tp", S(260.0), { dur: 0.3, from: 1.4 });
      line("sc052-h", [["his ", T(259.17)], ["dad", T(259.33)]]);
      line("sc052-l", [["leader ", T(260.05)], ["of ", T(260.29)], ["China", T(260.45)]]);
      line("sc052-c", [["against ", T(261.49)], ["the ", T(261.73)], ["communists", T(261.89)]], { dur: 0.45 });
    })();

    /* ============ C6S053–054 · 262.53–272.85 · Moscow, 1917 plan: political school → classmates ============ */
    whip("052", "053", S(262.53), { dir: 1 });
    scene("053", 262.53, 272.85);
    ground("paper", S(262.53));
    (function () {
      gsap.set("#c6s02-sc053-plane", { rotationX: 12 });
      const cam = $("sc053-cam"), SX = 930, SY = 1560;
      gsap.set(cam, { scale: 0.75, x: 960 - 1300 * 0.75, y: 540 - 1250 * 0.75 });
      tl.fromTo(cam, { scale: 0.75, x: 960 - 1300 * 0.75, y: 540 - 1250 * 0.75 }, { scale: 1.15, x: 960 - SX * 1.15, y: 420 - SY * 1.15, duration: 3.8, ease: FX.ease.cam, immediateRender: false }, S(262.6));
      tl.fromTo("#c6s02-sc053-tag", { opacity: 0 }, { opacity: 1, duration: 0.3, immediateRender: true }, S(264.85));
      line("sc053-l", [["learns ", T(265.01)], ["a ", T(265.41)], ["lot", T(265.49)]]);
      const svg = $("sc053-svg"), f = FX.markupDefs(svg, "c6s02-mk53", { boil: 4 });
      svg.setAttribute("viewBox", "0 0 2740 2700");
      FX.markup.pen(tl, svg, S(266.12), { points: [[SX - 130, SY - 10], [SX - 90, SY - 85], [SX + 20, SY - 105], [SX + 130, SY - 60], [SX + 140, SY + 40], [SX + 50, SY + 95], [SX - 80, SY + 85], [SX - 140, SY + 20], [SX - 110, SY - 60]], width: 10, color: INK, filter: f, dur: 0.5, seed: 5301 });   // done 266.62
      line("sc053-p", [["political ", T(266.21)], ["school", T(266.53)]], { dur: 0.35 });
      // PS: two photo cards slide onto the map (C6S054 begins)
      tl.to(["#c6s02-sc053-tag", "#c6s02-sc053-l", "#c6s02-sc053-p"], { opacity: 0, duration: 0.25 }, S(266.75));
      tl.fromTo("#c6s02-sc053-veil", { opacity: 0 }, { opacity: 1, duration: 0.4, ease: C(FX.ease.out, 0.4), immediateRender: true }, S(266.6));
      gsap.set(["#c6s02-sc053-c1", "#c6s02-sc053-flip"], { y: 1100 });
      gsap.set("#c6s02-sc053-c2", { rotation: 3, rotationY: 0 });
      tl.fromTo("#c6s02-sc053-c1", { y: 1100 }, { y: 0, duration: 0.45, ease: C(FX.ease.inOut, 0.45), immediateRender: false }, S(266.48));
      tl.fromTo("#c6s02-sc053-flip", { y: 1100 }, { y: 0, duration: 0.45, ease: C(FX.ease.inOut, 0.45), immediateRender: false }, S(266.56));
      line("sc053-cl", [["classmates", T(268.13)]]);
      const br = $("sc053-br"), f2 = FX.markupDefs(br, "c6s02-mk54", { boil: 4 });
      FX.markup.pen(tl, br, S(268.10), { points: [[540, 182], [548, 156], [960, 150], [1388, 156], [1398, 182]], width: 6, color: INK, filter: f2, dur: 0.6, seed: 5401 });   // done 268.7
      // the face-down card flips to young Deng Xiaoping (12 fps)
      tl.to("#c6s02-sc053-c2", { rotationY: 180, duration: 0.25, ease: C("power1.inOut", 0.25) }, S(271.18));
      pop("sc053-dx", T(271.41) - L, { dur: 0.6, from: 0.7 });   // done 271.95
      tl.to($("sc053"), { scale: 1.1, transformOrigin: "1220px 450px", duration: 1.3, ease: FX.ease.in }, S(271.6));   // CA: push to Deng
    })();

    /* ============ C6S055 · 272.85–279.89 · the same person: young Deng → Deng 1979 (curve cut) ============ */
    scene("055", 272.85, 279.94);
    ground("night", S(272.85));
    (function () {
      const wrap = $("sc055-wrap");
      line("sc055-k", [["the ", T(272.85)], ["same ", T(273.01)], ["person", T(273.33)]]);
      FX.curveCut(tl, wrap, $("sc055-a"), $("sc055-b"), S(273.70), 1.0, { from: 1.0, to: 1.35 });   // cut at 274.20
      FX.focusHunt(tl, wrap, S(274.72), { dur: 0.7 });
      tl.to(wrap, { scale: 1.42, duration: 4.6, ease: "none" }, S(275.2));
      tl.fromTo("#c6s02-sc055-mao", { opacity: 0, x: 300 }, { opacity: 1, x: 0, duration: 0.7, ease: C(FX.ease.out, 0.7), immediateRender: true }, S(275.25));
      line("sc055-m", [["Mao ", T(275.41)], ["Zedong", T(275.81)]], { dur: 0.6 });
      tl.to(["#c6s02-sc055-mao", "#c6s02-sc055-m"], { opacity: 0, x: 300, duration: 0.5, ease: C(FX.ease.in, 0.5) }, S(276.6));
      line("sc055-o", [["open ", T(276.45)], ["up ", T(276.77)], ["China", T(276.93)]]);
      line("sc055-e", [["economy", T(279.41)]], { dur: 0.3 });
    })();

    /* ============ C6S056 · 279.89–285.09 · the Deng billboard, dusk (V6) ============ */
    whip("055", "056", S(279.89), { dir: -1 });
    scene("056", 279.89, 285.09);
    ground("night", S(279.89));
    (function () {
      const bb = $("sc056-bb"); bb.style.cssText += ";left:300px;top:230px;width:1320px;height:830px;background-size:1320px auto;background-position:0 0;filter:saturate(0.6) brightness(0.5) contrast(1.15) sepia(0.3);-webkit-mask-image:radial-gradient(ellipse 58% 56% at 50% 48%,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 58% 56% at 50% 48%,#000 70%,transparent 100%)";
      tl.fromTo(bb, { y: -40 }, { y: 120, duration: 5.3, ease: "none", immediateRender: false }, S(279.89));     // slow tilt up: near layer moves more
      tl.fromTo("#c6s02-sc056-sky", { y: 0 }, { y: 50, duration: 5.3, ease: "none", immediateRender: false }, S(279.89));
      // nothing on screen during "communism … or something" (slip) — the corrected phrase rises into the sky
      line("sc056-s", [["Socialism ", T(283.25)], ["with ", T(283.73)], ["Chinese ", T(283.89)], ["characteristics", T(284.29)]], { dur: 0.6 });
    })();

    /* ============ C6S057 · 285.09–291.73 · back to the classmates; Kuo learns a lot in Moscow ============ */
    scene("057", 285.09, 291.78);
    ground("paper", S(285.09));
    (function () {
      gsap.set("#c6s02-sc057-plane", { rotationX: 12 });
      const cam = $("sc057-cam");
      gsap.set(cam, { scale: 1.15, x: 960 - 930 * 1.15, y: 420 - 1560 * 1.15 });
      gsap.set("#c6s02-sc057-c1", { rotation: -3 }); gsap.set("#c6s02-sc057-c2", { rotation: 3 });
      tl.fromTo($("sc057"), { scale: 1.1, transformOrigin: "1220px 450px" }, { scale: 1.0, duration: 1.2, ease: FX.ease.cam, immediateRender: false }, S(285.09));
      const svg = $("sc057-svg"), f = FX.markupDefs(svg, "c6s02-mk57", { boil: 4 }); svg.setAttribute("viewBox", "0 0 2740 2700");
      line("sc057-cl", [["classmate", T(287.01)]]);
      tl.to(["#c6s02-sc057-c2", "#c6s02-sc057-dx"], { x: 1200, rotation: 12, duration: 0.8, ease: C(FX.ease.in, 0.8) }, S(287.0));   // gone 287.8
      tl.to("#c6s02-sc057-c1", { x: -230, rotation: -1, duration: 1.2, ease: C(FX.ease.inOut, 1.2) }, S(287.5));   // 288.7 — moves left so the Kremlin circle stays clear
      tl.to("#c6s02-sc057-cl", { opacity: 0, duration: 0.4, ease: C(FX.ease.in, 0.4) }, S(288.2));
      tl.fromTo("#c6s02-sc057-tag", { opacity: 0 }, { opacity: 1, duration: 0.25, immediateRender: true }, S(288.1));
      line("sc057-l", [["learns ", T(288.29)], ["a ", T(288.53)], ["lot", T(288.61)]]);
      tl.to(cam, { scale: 0.72, x: 960 - 1200 * 0.72, y: 500 - 1350 * 0.72, duration: 1.6, ease: FX.ease.cam }, S(288.9));
      tl.to("#c6s02-sc057-veil", { opacity: 0.3, duration: 1.2, ease: C(FX.ease.out, 1.2) }, S(288.9));
      tl.to("#c6s02-sc057-c1", { scale: 0.75, y: -60, duration: 1.4, ease: C(FX.ease.inOut, 1.4) }, S(288.9));   // done 290.3
      FX.markup.pen(tl, svg, S(290.80), { points: [[1180, 1180], [1290, 1150], [1420, 1210], [1440, 1330], [1330, 1420], [1170, 1400], [1110, 1290], [1150, 1200]], width: 10, color: INK, filter: f, dur: 0.4, seed: 5701 });   // Kremlin, on "in … Moscow" — done 291.20 (whip 291.56)
      line("sc057-m", [["Moscow", T(291.09)]], { dur: 0.3 });
    })();

    /* ============ C6S058 · 291.73–295.25 · engineer's notebook: politics / engineering ============ */
    whip("057", "058", S(291.73), { dir: -1, vertical: true });
    scene("058", 291.73, 295.25);
    ground("paper", S(291.73));
    (function () {
      tl.fromTo("#c6s02-sc058-cam", { scale: 1.0 }, { scale: 1.05, duration: 3.1, ease: "none", immediateRender: false }, S(291.73));
      const svg = $("sc058-svg"), f = FX.markupDefs(svg, "c6s02-mk58", { boil: 4 }); svg.setAttribute("viewBox", "0 0 1560 900");
      line("sc058-p", [["politics", T(292.61)]], { dur: 0.6 });
      FX.markup.pen(tl, svg, S(292.66), { points: [[106, 352], [300, 346], [500, 354]], width: 6, color: PEN, filter: f, dur: 0.45, seed: 5801 });
      tl.fromTo("#c6s02-sc058-tab1", { x: -60 }, { x: 0, duration: 0.5, ease: C(FX.ease.out, 0.5), immediateRender: true }, S(292.6));
      line("sc058-e", [["engineering", T(293.25)]], { dur: 0.6 });
      FX.markup.pen(tl, svg, S(293.30), { points: [[876, 352], [1150, 346], [1430, 356]], width: 6, color: PEN, filter: f, dur: 0.5, seed: 5802 });   // done 293.8
      tl.fromTo("#c6s02-sc058-tab2", { x: -60 }, { x: 0, duration: 0.5, ease: C(FX.ease.out, 0.5), immediateRender: true }, S(293.24));
      line("sc058-s", [["sees", T(294.53)]], { dur: 0.4 });
    })();

    /* ============ C6S059 · 295.25–303.41 · engineers in charge build industry (Vox layered) ============ */
    push("058", "059", S(295.25), 1780, 470);
    scene("059", 295.25, 303.46);
    ground("night", S(295.25));
    (function () {
      tl.fromTo("#c6s02-sc059-pa", { x: 0 }, { x: 70, duration: 8.2, ease: "none", immediateRender: false }, S(295.25));
      tl.fromTo("#c6s02-sc059-pb", { x: 0 }, { x: -60, duration: 8.2, ease: "none", immediateRender: false }, S(295.25));
      tl.fromTo("#c6s02-sc059-pc", { scale: 1.0 }, { scale: 1.05, duration: 8.2, ease: "none", immediateRender: false }, S(295.25));
      tl.fromTo("#c6s02-sc059-pd", { opacity: 0, y: -80, rotation: 10 }, { opacity: 1, y: 0, rotation: 4, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(301.5));   // "build industry" — done 302.5
      line("sc059-c", [["in ", T(297.41)], ["charge", T(297.65)]]);
      line("sc059-e", [["ENGINEERS", T(298.53)]], { dur: 1.0 });
      line("sc059-b", [["build ", T(301.65)], ["industry", T(302.05)]]);
      line("sc059-y", [["country", T(302.93)]], { dur: 0.3 });
    })();

    /* ============ C6S060 · 303.41–306.45 · the blueprint equation ============ */
    whip("059", "060", S(303.41), { dir: 1, vertical: true });
    scene("060", 303.41, 306.45);
    ground("paper", S(303.41));
    (function () {
      const g = $("sc060-grid"); let d = "";
      for (let x = 60; x < 1920; x += 120) d += "M" + x + " 0 L" + (x + 1) + " 1080 ";
      for (let y = 60; y < 1080; y += 120) d += "M0 " + y + " L1920 " + (y + 1) + " ";
      el("path", { d, stroke: BONE, "stroke-width": 1.5, fill: "none" }, g);
      const a2 = div("c62-abs t-display", "left:140px;top:400px;font-size:150px;color:var(--bone)", $("sc060-cam")); a2.id = "c6s02-sc060-a2";
      line("sc060-a", [["The ", T(303.41)], ["state ", T(303.49)], ["could ", T(303.81)], ["build", T(304.05)]], { dur: 0.5 });
      line("sc060-a2", [["industry", T(304.29)]], { dur: 0.6 });
      line("sc060-b", [["if ", T(304.69)], ["engineers ", T(305.01)], ["are ", T(305.49)], ["in ", T(305.73)], ["charge", T(305.97)]], { dur: 0.4 });
      const svg = $("sc060-svg"), f = FX.markupDefs(svg, "c6s02-mk60", { boil: 4 });
      FX.markup.pen(tl, svg, S(305.05), { points: [[770, 700], [880, 650], [870, 545], [730, 482]], width: 7, color: BONE, blend: "normal", filter: f, dur: 0.45, seed: 6001 });
      FX.markup.pen(tl, svg, S(305.45), { points: [[764, 458], [726, 482], [760, 512]], width: 7, color: BONE, blend: "normal", filter: f, dur: 0.15, seed: 6002 });   // arrow head — done 305.6
      tl.to("#c6s02-sc060-cam", { x: 260, duration: 0.4, ease: FX.ease.in }, S(306.05));   // CA: slide right into the cut
    })();

    /* ============ C6S061 · 306.45–313.66 · premier: make Taiwan an economic power (hero) ============ */
    scene("061", 306.45, 313.71);
    ground("night", S(306.45));
    (function () {
      tl.fromTo("#c6s02-sc061-cam", { scale: 1.0, x: -60 }, { scale: 1.07, x: 0, duration: 7.2, ease: "none", immediateRender: false }, S(306.45));
      line("sc061-c", [["in ", T(308.53)], ["charge", T(308.69)]]);
      line("sc061-t", [["Taiwan", T(310.13)]], { dur: 0.6 });
      const svg = $("sc061-svg"), f = FX.markupDefs(svg, "c6s02-mk61", { boil: 4 });
      FX.markup.pen(tl, svg, S(310.18), { points: [[106, 500], [250, 494], [400, 502]], width: 11, color: CEL, blend: "normal", filter: f, dur: 0.4, seed: 6101 });
      const e = $("sc061-e"); e.innerHTML = '<div id="c6s02-sc061-e1"></div><div id="c6s02-sc061-e2"></div>';
      line("sc061-e1", [["ECONOMIC", T(311.09)]], { dur: 1.0 });
      line("sc061-e2", [["POWER", T(311.49)]], { dur: 1.0 });   // done 312.43
    })();

    /* ============ C6S062 · 313.66–318.14 · the world doesn't recognise us — only Taiwan stays lit ============ */
    whip("061", "062", S(313.66), { dir: 1 });
    scene("062", 313.66, 318.14);
    ground("night", S(313.66));
    (function () {
      const cam = $("sc062-cam"), p = PD.patch, k = 4096 / 360;
      Object.assign($("sc062-patch").style, { left: p[0] + "px", top: p[1] + "px", width: p[2] + "px", height: p[3] + "px" });
      const tw = $("sc062-tw");
      Object.assign(tw.style, { left: ((119.3 + 180) * k) + "px", top: ((90 - 25.4) * k) + "px", width: (2.9 * k) + "px", height: (3.6 * k) + "px" });
      const TX = (120.95 + 180) * k, TY = (90 - 23.7) * k;
      const at = (s, ox, oy) => ({ scale: s, x: 960 + (ox || 0) - TX * s, y: 540 + (oy || 0) - TY * s });
      gsap.set(cam, at(5));
      tl.fromTo(cam, at(5), Object.assign(at(0.47), { x: 960 - 2048 * 0.47, y: 590 - 1024 * 0.47, duration: 1.9, ease: FX.ease.cam, immediateRender: false }), S(313.70));   // pull back to the world
      tl.fromTo("#c6s02-sc062-veil", { opacity: 0 }, { opacity: 0.62, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(314.10));   // the world dims
      tl.fromTo(tw, { filter: "drop-shadow(0 0 3px rgba(159,199,178,0.9))" }, { filter: "drop-shadow(0 0 26px rgba(159,199,178,1))", duration: 1.4, ease: "sine.inOut", immediateRender: true }, S(314.2));
      tl.to(cam, Object.assign(at(3.4), { duration: 1.2, ease: FX.ease.cam }), S(316.90));   // push back in on "become important again"
      tl.to(tw, { filter: "drop-shadow(0 0 7px rgba(190,230,205,1))", duration: 1.0, ease: "sine.inOut" }, S(316.9));
      line("sc062-w", [["the ", T(313.66)], ["world", T(313.90)]]);
      line("sc062-r", [["doesn't ", T(314.14)], ["recognize ", T(314.46)], ["us", T(314.94)]]);
      tl.to(["#c6s02-sc062-w", "#c6s02-sc062-r"], { opacity: 0, duration: 0.3 }, S(316.6));
      line("sc062-b", [["become ", T(316.94)], ["important ", T(317.34)], ["again", T(317.66)]], { dur: 0.35 });
    })();

    /* ============ C6S063–064 · 318.14–329.26 · cabinet table: reshuffle, generals → engineers ============ */
    slide("063", S(318.14), "bottom", 0.3);
    scene("063", 317.84, 329.26);
    ground("paper", S(318.0));
    (function () {
      const seats = $("sc063-seats"), CX = 1180, CY = 560, R = 370, N = 10, M = 11;
      const pos = (j) => { const a = -Math.PI / 2 + ((j + 1) / M) * Math.PI * 2; return [CX + Math.cos(a) * R, CY + Math.sin(a) * R]; };
      const cards = [];
      for (let i = 0; i < N; i++) {
        const [x, y] = pos(i);
        const c = div("", "position:absolute;left:" + (x - 62) + "px;top:" + (y - 72) + "px;width:124px;height:144px;background:#efe7d6;box-shadow:0 8px 16px rgba(20,27,36,0.28);transform-origin:50% 50%", seats);
        const g = icon(c, "general", 62, 74, 0.95), e = icon(c, "engineer", 62, 74, 0.95); e.style.opacity = 0;
        cards.push({ c, g, e, i });
      }
      // seat ticks + the premier's chair (celadon = the ROC government)
      const svg = $("sc063-svg"), f = FX.markupDefs(svg, "c6s02-mk63", { boil: 4 });
      ink(svg, "M1180 180 L1182 258", S(318.3), 0.35, { width: 5 });
      line("sc063-f", [["first", T(318.54)]]);
      // C6S063 reshuffle (12 fps): every seat card moves one place round the table
      cards.forEach(({ c, i }) => {
        const [x0, y0] = pos(i), [x1, y1] = pos((i + 3) % N);
        tl.to(c, { x: x1 - x0, y: y1 - y0, rotation: (i % 2 ? 6 : -6), duration: 0.7, ease: C(FX.ease.inOut, 0.7) }, S(320.84) + (i % 3) / 24);
        tl.to(c, { rotation: 0, duration: 0.3, ease: C(FX.ease.out, 0.3) }, S(321.6));
      });   // done 321.9
      line("sc063-c", [["change ", T(320.86)], ["the ", T(321.18)], ["cabinet", T(321.26)]]);
      tl.fromTo("#c6s02-sc063-table", { rotation: 0 }, { rotation: 6, duration: 11.1, ease: "none", immediateRender: false }, S(318.14));
      // C6S064: generals flip to engineers one by one (12 fps)
      tl.to(["#c6s02-sc063-f", "#c6s02-sc063-c"], { opacity: 0, duration: 0.3 }, S(324.3));
      line("sc063-e", [["ENGINEERS", T(324.78)]], { dur: 0.9 });
      cards.forEach(({ c, g, e }, k) => {
        const t0 = S(324.78) + k * 0.09;
        tl.to(c, { scaleX: 0, duration: 0.1, ease: C("power1.in", 0.1) }, t0);
        tl.set(g, { opacity: 0 }, t0 + 0.1); tl.set(e, { opacity: 1 }, t0 + 0.1);
        tl.to(c, { scaleX: 1, duration: 0.1, ease: C("power1.out", 0.1) }, t0 + 0.1);
      });   // last flip 325.79
      line("sc063-i", [["important ", T(325.74)], ["guys", T(326.06)]]);
      // the economic minister's seat: pen circle (seat card 0 ends at slot 3)
      const [mx, my] = pos(3);
      FX.markup.pen(tl, svg, S(327.38), { points: [[mx - 95, my - 10], [mx - 70, my - 95], [mx + 10, my - 112], [mx + 90, my - 70], [mx + 100, my + 30], [mx + 40, my + 100], [mx - 60, my + 98], [mx - 102, my + 30], [mx - 92, my - 40]], width: 8, color: INK, filter: f, dur: 0.6, seed: 6401 });   // done 327.98
      line("sc063-m", [["economic ", T(327.42)], ["minister", T(327.90)]], { dur: 0.6 });
      // camera eases toward the circled seat, then pushes through it (PT) into the dossier
      const a6 = 6 * Math.PI / 180, sx = CX + (mx - CX) * Math.cos(a6) - (my - CY) * Math.sin(a6), sy = CY + (mx - CX) * Math.sin(a6) + (my - CY) * Math.cos(a6);
      gsap.set("#c6s02-sc063-cam", { transformOrigin: sx + "px " + sy + "px" });
      tl.fromTo("#c6s02-sc063-cam", { scale: 1 }, { scale: 1.12, duration: 2.2, ease: FX.ease.cam, immediateRender: false }, S(326.6));
      $("sc063").dataset.ox = sx; $("sc063").dataset.oy = sy;
    })();

    /* ============ C6S065 · 329.26–337.26 · Sun Yun-suan's dossier ============ */
    push("063", "065", S(329.26), +$("sc063").dataset.ox, +$("sc063").dataset.oy);
    scene("065", 329.26, 337.31);
    ground("night", S(329.26));
    (function () {
      tl.fromTo("#c6s02-sc065-cam", { scale: 1.0, rotation: 0 }, { scale: 1.08, rotation: 1.2, duration: 8.0, ease: "none", immediateRender: false }, S(329.26));
      torn($("sc065-ph"), 6501);
      pop("sc065-nm", T(329.66) - L, { dur: 0.7, from: 0.8 });
      pop("sc065-bf", T(332.46) - L, { dur: 0.6, from: 1.3 });
      const pr = $("sc065-pr");
      typeWord(pr, "electric ", T(333.58) - L, 1 / 24);
      typeWord(pr, "engineer", T(334.22) - L, 1 / 24);
      // mini route China → Taiwan on the card (pen), celadon end
      const im = $("sc065-rt").previousElementSibling, rt = $("sc065-rt");
      [im, rt].forEach((n) => Object.assign(n.style, { left: "-230px", top: "-130px", width: "576px", height: "574px" }));
      rt.setAttribute("viewBox", "0 0 720 717");
      const f = FX.markupDefs(rt, "c6s02-mk65", { boil: 4 }); rt.setAttribute("viewBox", "0 0 720 717");
      const A = PD.miniNanjing, B = PD.miniTaipei;
      FX.markup.pen(tl, rt, S(335.86), { points: [A, [A[0] + 70, A[1] + 120], [B[0] - 50, B[1] - 40], B], width: 6, color: PEN, filter: f, dur: 0.6, seed: 6502 });   // done 336.46
      const dot = el("circle", { cx: B[0], cy: B[1], r: 13, fill: CEL, stroke: "#5f8a74", "stroke-width": 3, opacity: 0 }, rt);
      tl.to(dot, { attr: { opacity: 1 }, duration: 0.15 }, S(336.5));
      Object.assign($("sc065-ch").style, { left: "40px", top: "70px" }); Object.assign($("sc065-tw").style, { left: "240px", top: "236px" });
      line("sc065-ch", [["China", T(335.82)]], { dur: 0.4 });
      line("sc065-tw", [["Taiwan", T(336.70)]], { dur: 0.2 });
    })();

    /* ============ C6S066 · 337.26–341.82 · he fixed the energy grid; the nationalists flee over ============ */
    whip("065", "066", S(337.26), { dir: -1, vertical: true });
    scene("066", 337.26, 341.82);
    ground("paper", S(337.26));
    (function () {
      const gr = $("sc066-grid"); let d = "";
      for (let x = 40; x < 1920; x += 80) d += "M" + x + " 0 L" + (x + 1) + " 1080 ";
      for (let y = 40; y < 1080; y += 80) d += "M0 " + y + " L1920 " + (y + 1) + " ";
      el("path", { d, stroke: BONE, "stroke-width": 1.2, fill: "none" }, gr);
      tl.fromTo("#c6s02-sc066-cam", { scale: 1.0 }, { scale: 1.05, duration: 4.6, ease: "none", immediateRender: false }, S(337.26));
      const svg = $("sc066-svg"), SC = 0.88, OX = 1310, OY = 100;
      const g = el("g", { transform: "translate(" + OX + "," + OY + ") scale(" + SC + ")" }, svg);
      ink(g, PD.twBox, S(337.30), 0.9, { color: BONE, width: 4.5 });   // island outline — done 338.2
      const P = PD.twCities, q = (k) => P[k];
      const links = [["keelung", "taipei"], ["taipei", "yilan"], ["taipei", "hsinchu"], ["hsinchu", "taichung"], ["taichung", "sunmoon"], ["taichung", "chiayi"], ["sunmoon", "chiayi"], ["chiayi", "tainan"], ["tainan", "kaohsiung"], ["sunmoon", "hualien"], ["yilan", "hualien"], ["hualien", "taitung"], ["kaohsiung", "taitung"]];
      links.forEach(([a, b], i) => { const A = q(a), B = q(b); ink(g, "M" + A[0] + " " + A[1] + " Q" + ((A[0] + B[0]) / 2 + 12) + " " + ((A[1] + B[1]) / 2 - 8) + " " + B[0] + " " + B[1], S(338.44) + (i % 5) * 0.06, 0.6, { color: YEL, width: 4.5, opacity: 0.9 }); });   // done 339.28
      Object.keys(P).forEach((k, i) => {
        const r = el("rect", { x: P[k][0] - 10, y: P[k][1] - 10, width: 20, height: 20, fill: BONE, stroke: "#0f1318", "stroke-width": 3 }, g);
        tl.fromTo(r, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(338.9) + i / 24);
      });   // substations done 339.4
      line("sc066-f", [["fixed", T(337.98)]]);
      $("sc066-g").innerHTML = '<div id="c6s02-sc066-g1"></div><div id="c6s02-sc066-g2"></div>';
      line("sc066-g1", [["ENERGY", T(338.46)]]);
      line("sc066-g2", [["GRID", T(338.86)]]);
      pop("sc066-photo", S(340.0), { dur: 0.7, from: 0.8 });
      line("sc066-n", [["nationalists", T(340.06)]]);
      line("sc066-fl", [["fleeing ", T(340.86)], ["over", T(341.26)]], { dur: 0.4 });
      // small ships arrive from the west (12 fps) — still sailing at the cut (CA)
      const sh = $("sc066-ships");
      [[640, 330], [600, 470], [700, 610], [560, 720]].forEach(([x, y], i) => {
        const s = div("", "position:absolute;left:" + x + "px;top:" + y + "px;width:90px;height:40px", sh, '<svg viewBox="0 0 90 40" style="width:90px;height:40px"><path d="M4 22 L86 22 L74 36 L14 36 Z" fill="#f2ede3"/><rect x="30" y="8" width="26" height="14" fill="#f2ede3"/><rect x="40" y="0" width="7" height="9" fill="#f2ede3"/></svg>');
        tl.fromTo(s, { x: -260, opacity: 0 }, { x: 260, opacity: 1, duration: 1.4, ease: C("power1.out", 1.4), immediateRender: true }, S(340.6) + i * 0.08);
      });
    })();

    /* ============ C6S067 · 341.82–350.86 · K. T. Li: physicist → treasury, the money guy ============ */
    scene("067", 341.82, 350.91);
    ground("night", S(341.82));
    (function () {
      tl.fromTo("#c6s02-sc067-fold", { x: 600, rotation: 8 }, { x: 0, rotation: 3, duration: 1.2, ease: C(FX.ease.out, 1.2), immediateRender: false }, S(341.82));
      tl.fromTo("#c6s02-sc067-cam", { scale: 1.0, x: 0 }, { scale: 1.06, x: 0, duration: 6.6, ease: "none", immediateRender: false }, S(341.82));
      torn($("sc067-ph"), 6701);
      tl.fromTo("#c6s02-sc067-ph", { opacity: 0, y: -60, rotation: -4 }, { opacity: 1, y: 0, rotation: 2, duration: 0.6, ease: C(FX.ease.out, 0.6), immediateRender: true }, S(344.2));
      pop("sc067-nm", T(344.30) - L, { dur: 0.7, from: 0.8 });
      typeWord($("sc067-ph1"), "physicist", T(345.66) - L, 1 / 24);
      const svg = $("sc067-svg"), f = FX.markupDefs(svg, "c6s02-mk67", { boil: 4 }); svg.setAttribute("viewBox", "0 0 1100 690");
      FX.markup.pen(tl, svg, S(347.58), { points: [[420, 266], [520, 258], [640, 262]], width: 6, color: PEN, filter: f, dur: 0.22, seed: 6702 });
      typeWord($("sc067-tr"), "treasury", T(347.74) - L, 1 / 24);
      // the money: 1946 Taiwan banknotes fan out from behind the folder (12 fps)
      const notes = $("sc067-notes");
      [-14, 2, 18].forEach((r, i) => {
        const n = div("", "position:absolute;left:1180px;top:560px;width:560px;height:290px;background:url('assets/c4/documents/old_taiwan_dollar_500_1946_back.jpg') center/cover;box-shadow:0 14px 28px rgba(0,0,0,0.55);transform-origin:0% 100%;filter:saturate(0.55) sepia(0.2) brightness(0.9)", notes);
        tl.fromTo(n, { x: -420, rotation: 0 }, { x: 0, rotation: r, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(348.58) + i / 12);
      });   // done 349.55
      tl.to("#c6s02-sc067-cam", { x: -120, duration: 1.6, ease: FX.ease.cam }, S(348.6));
      line("sc067-mg", [["money ", T(348.62)], ["guy", T(348.94)]]);
      typeWord($("sc067-cb"), "cabinet", T(350.22) - L, 1 / 24);   // done 350.45
    })();

    /* ============ C6S068–069 · 350.86–362.06 · cork board: engineers' cabinet → many projects ============ */
    whip("067", "068", S(350.86), { dir: -1 });
    scene("068", 350.86, 362.11);
    ground("night", S(350.86));
    (function () {
      const board = $("sc068-board"), pins = $("sc068-pins"), svg = $("sc068-svg");
      svg.setAttribute("viewBox", "0 0 2600 1300");
      const people = [
        { x: 330, y: 200, img: "assets/c6/photos/sun_yun_suan_premier_portrait_colour.jpg", bp: "center 18%" },
        { x: 760, y: 560, img: "assets/c6/derived/c6s02/kt_li_crop.jpg", bp: "center 12%" },
        { x: 1150, y: 170, ico: 1 }, { x: 1260, y: 600, ico: 1 }, { x: 470, y: 770, ico: 1 },
      ];
      const P = people.map((p, i) => {
        const c = div("", "position:absolute;left:" + p.x + "px;top:" + p.y + "px;width:250px;height:310px;background:#efe7d6;box-shadow:0 18px 30px rgba(0,0,0,0.55);transform:rotate(" + ((i % 2) ? 3 : -3) + "deg)", board);
        if (p.img) div("", "position:absolute;left:16px;top:16px;right:16px;bottom:16px;background:url('" + p.img + "') " + p.bp + "/cover;filter:grayscale(1) sepia(0.2) contrast(1.1)", c);
        else { const d = div("", "position:absolute;left:16px;top:16px;right:16px;bottom:16px;background:#e2d8c4", c); icon(d, "engineer", 109, 139, 1.7); }
        const pn = document.createElement("img"); pn.src = "assets/icons/pin_bone_top.svg"; pn.className = "c62-pin"; pn.style.left = (p.x + 125) + "px"; pn.style.top = (p.y + 10) + "px"; pins.appendChild(pn);
        const t0 = S(350.92) + i * 0.16;
        tl.fromTo(c, { opacity: 0, y: -40, scale: 1.08 }, { opacity: 1, y: 0, scale: 1, duration: 0.25, ease: C(FX.ease.out, 0.25), immediateRender: true }, t0);
        tl.fromTo(pn, { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.17, ease: C(FX.ease.out, 0.17), immediateRender: true }, t0 + 0.2);
        return [p.x + 125, p.y + 30];
      });   // all pinned 351.8
      // ENGINEERS tag in the middle; ink strings from every face to it
      const tag = div("t-display", "position:absolute;left:820px;top:380px;padding:16px 26px 8px;background:#efe3b8;color:#141b24;font-size:58px;box-shadow:0 12px 22px rgba(0,0,0,0.5);transform:rotate(-2deg)", board, "ENGINEERS");
      tl.fromTo(tag, { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(FX.ease.out, 0.25), immediateRender: true }, T(354.14) - L);
      P.forEach(([x, y], i) => ink(svg, "M" + x + " " + y + " Q" + ((x + 960) / 2) + " " + ((y + 420) / 2 + 40) + " 960 420", S(354.2) + i * 0.08, 0.6, { color: "#2a2f38", width: 4 }));   // done 355.12
      line("sc068-b", [["bunch ", T(351.58)], ["of ", T(351.74)], ["other ", T(351.90)], ["people", T(352.14)]]);
      line("sc068-c", [["cabinet", T(356.14)]]);
      // C6S069 — crane right: strings run out to many project cards; one is the chip
      tl.to(["#c6s02-sc068-b", "#c6s02-sc068-c"], { opacity: 0, duration: 0.3 }, S(357.3));
      const cam = $("sc068-cam");
      tl.fromTo(cam, { x: 0, y: 0, scale: 1 }, { x: -40, y: -30, scale: 1.02, duration: 6.4, ease: "none", immediateRender: false }, S(350.86));
      tl.to(cam, { x: -640, y: -60, scale: 0.96, duration: 1.8, ease: FX.ease.cam }, S(357.45));
      const projs = [
        { x: 1720, y: 180, ico: "assets/c4/icons/factory.svg" }, { x: 2050, y: 330, ico: "assets/c4/icons/bulb.svg" },
        { x: 1760, y: 560, ship: 1 }, { x: 2120, y: 720, chip: 1 }, { x: 1740, y: 880, road: 1 },
      ];
      let chipCard = null;
      projs.forEach((p, i) => {
        const c = div("", "position:absolute;left:" + p.x + "px;top:" + p.y + "px;width:250px;height:200px;background:#efe7d6;box-shadow:0 16px 28px rgba(0,0,0,0.55);transform:rotate(" + ((i % 2) ? -2 : 3) + "deg)", board);
        if (p.ico) div("", "position:absolute;left:65px;top:40px;width:120px;height:120px;background:url('" + p.ico + "') center/contain no-repeat;opacity:0.85", c);
        if (p.ship) c.innerHTML = '<svg viewBox="0 0 90 40" style="position:absolute;left:45px;top:60px;width:160px;height:72px"><path d="M4 22 L86 22 L74 36 L14 36 Z" fill="#141b24"/><rect x="30" y="8" width="26" height="14" fill="#141b24"/><rect x="40" y="0" width="7" height="9" fill="#141b24"/></svg>';
        if (p.road) c.innerHTML = '<svg viewBox="0 0 100 80" style="position:absolute;left:55px;top:40px;width:140px;height:112px"><path d="M30 80 L45 0 L55 0 L70 80 Z" fill="#141b24"/><path d="M50 8 L50 20 M50 32 L50 46 M50 58 L50 74" stroke="#efe7d6" stroke-width="4"/></svg>';
        if (p.chip) { div("", "position:absolute;left:14px;top:14px;right:14px;bottom:14px;background:url('assets/c3/photos/fairchild_micrologic_series_01.jpg') center/cover;filter:saturate(0.6) contrast(1.05)", c); chipCard = c; }
        const pn = document.createElement("img"); pn.src = "assets/icons/pin_bone_top.svg"; pn.className = "c62-pin"; pn.style.left = (p.x + 125) + "px"; pn.style.top = (p.y + 8) + "px"; pins.appendChild(pn);
        const t0 = S(357.95) + i * 0.14;
        tl.fromTo(c, { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.25, ease: C(FX.ease.out, 0.25), immediateRender: true }, t0);
        tl.fromTo(pn, { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.17, ease: C(FX.ease.out, 0.17), immediateRender: true }, t0 + 0.2);
        ink(svg, "M1080 430 Q" + ((1080 + p.x + 125) / 2) + " " + ((430 + p.y) / 2 + 60) + " " + (p.x + 125) + " " + (p.y + 26), S(358.4) + i * 0.1, 0.6, { color: "#2a2f38", width: 4 });   // done 359.4
      });
      line("sc068-i", [["important ", T(358.38)], ["role", T(358.62)]]);
      line("sc068-p", [["a ", T(359.02)], ["lot ", T(359.10)], ["of ", T(359.26)], ["projects", T(359.42)]]);
      tl.to(["#c6s02-sc068-i", "#c6s02-sc068-p"], { opacity: 0, duration: 0.3 }, S(360.6));
      // rack to the chip card: push + focus hunt; label-box on its words
      tl.to(cam, { x: 960 - 2245 * 1.3, y: 540 - 820 * 1.3, scale: 1.3, duration: 0.8, ease: FX.ease.cam }, S(360.55));
      FX.focusHunt(tl, cam, S(361.0), { dur: 0.6 });
      const lb = div("t-display", "position:absolute;left:2040px;top:940px;font-size:40px;white-space:nowrap", board, '<span class="c62-lbox" id="c6s02-sc068-lb"></span>');
      tl.fromTo("#c6s02-sc068-lb", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(360.94) - L);
      line("sc068-lb", [["technological ", T(360.94)], ["project", T(361.50)]], { dur: 0.25, y: 0 });   // done 361.69
      if (chipCard) tl.to(chipCard, { boxShadow: "0 16px 28px rgba(0,0,0,0.55), 0 0 0 8px #f2d33b", duration: 0.2 }, S(360.9));
    })();

    /* ============ C6S070 · 362.06–368.78 · Taiwanese already on the island; the nationalists arrive ============ */
    whip("068", "070", S(362.06), { dir: -1 });
    flash(S(362.06));
    scene("070", 362.06, 368.78);
    ground("paper", S(362.06));
    (function () {
      const cam = $("sc070-cam"), K0 = 0.4;
      gsap.set(cam, { scale: K0, x: 1300 - 1600 * K0, y: 540 - 1650 * K0 });
      tl.fromTo(cam, { scale: K0, x: 1300 - 1600 * K0, y: 540 - 1650 * K0 }, { scale: 0.44, x: 1300 - 1600 * 0.44, y: 540 - 1650 * 0.44, duration: 6.8, ease: "none", immediateRender: false }, S(362.06));
      const box = $("sc070-dots");
      PD.fmDots.forEach(([x, y], i) => {
        const d = div("c62-dot", "left:" + (x - 42) + "px;top:" + (y - 42) + "px;width:84px;height:84px;background:" + CEL + ";border:8px solid #6f9a84;opacity:0", box);
        tl.fromTo(d, { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(FX.ease.out, 0.25), immediateRender: true }, S(364.66) + Math.floor(i / 2) / 16);
      });   // done 366.1
      pop("sc070-lg1", S(364.62), { dur: 0.4 });
      line("sc070-tp", [["Taiwanese ", T(364.70)], ["people", T(365.42)]]);
      line("sc070-al", [["already ", T(366.06)], ["on ", T(366.54)], ["the ", T(366.70)], ["island", T(366.86)]]);
      // ink dots (the nationalists) arrive from the west — still arriving at the cut (CA)
      PD.fmDots.filter((_, i) => i % 3 === 1).forEach(([x, y], i) => {
        const d = div("c62-dot", "left:" + (x + 20) + "px;top:" + (y - 10) + "px;width:70px;height:70px;background:" + INK + ";opacity:0", box);
        tl.fromTo(d, { opacity: 0, x: -1500 }, { opacity: 1, x: 0, duration: 1.3, ease: C(FX.ease.inOut, 1.3), immediateRender: true }, S(367.55) + (i % 4) / 24);
      });
      pop("sc070-lg2", S(367.6), { dur: 0.4 });
      line("sc070-na", [["nationalists", T(367.66)]], { dur: 0.6 });
    })();

    /* ============ C6S071 · 368.78–376.05 · elites rise to the governing level ============ */
    scene("071", 368.78, 376.10);
    ground("paper", S(368.78));
    (function () {
      const svg = $("sc071-svg"), f = FX.markupDefs(svg, "c6s02-mk71", { boil: 4 });
      const tiers = [{ y: 300, w: 640 }, { y: 560, w: 960 }, { y: 820, w: 1240 }], CX = 1250;
      tiers.forEach((t, i) => FX.markup.pen(tl, svg, S(368.85) + i * 0.15, { points: [[CX - t.w / 2, t.y + 3], [CX, t.y - 3], [CX + t.w / 2, t.y + 4]], width: 6, color: INK, filter: f, dur: 0.45, seed: 7100 + i }));
      const box = $("sc071-dots"), D = 46;
      const mk = (x, y, col) => div("c62-dot", "left:" + (x - D / 2) + "px;top:" + (y - D / 2) + "px;width:" + D + "px;height:" + D + "px;background:" + (col === "c" ? CEL : INK) + ";" + (col === "c" ? "border:4px solid #6f9a84;" : ""), box);
      const row = (y, n, w) => Array.from({ length: n }, (_, i) => [CX - w / 2 + (i + 0.5) * (w / n), y - 34]);
      const top = row(300, 12, 640), mid = row(560, 16, 960), bot = row(820, 20, 1240);
      top.forEach((p, i) => { if (i < 8) mk(p[0], p[1], "i"); });
      mid.forEach((p, i) => mk(p[0], p[1], i % 3 === 0 ? "c" : "i"));
      const climbers = [];
      bot.forEach((p, i) => { const d = mk(p[0], p[1], "c"); if (i % 5 === 2) climbers.push(d); });
      const all = Array.from(box.children);
      all.forEach((d, i) => tl.fromTo(d, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(369.0) + Math.floor(i / 4) / 24));   // grid done 369.6
      line("sc071-el", [["elites", T(369.90)]]);
      // four celadon dots climb into the four empty top-tier seats (12 fps)
      climbers.forEach((d, i) => {
        const p0 = bot[[2, 7, 12, 17][i]], p1 = top[8 + i];
        tl.to(d, { x: p1[0] - p0[0], y: p1[1] - p0[1], duration: 1.2, ease: C(FX.ease.inOut, 1.2) }, S(371.30) + i / 12);
      });   // done 372.75
      line("sc071-ru", [["rise ", T(371.33)], ["up", T(371.81)]]);
      tl.fromTo("#c6s02-sc071-gl", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(372.29) - L);
      $("sc071-gl").innerHTML = '<span class="c62-lbox" id="c6s02-sc071-glb"></span>';
      line("sc071-glb", [["GOVERNING ", T(372.29)], ["LEVEL", T(372.77)]], { dur: 0.5, y: 0 });
      line("sc071-de", [["decisions", T(374.53)]]);
      tl.fromTo("#c6s02-sc071-cam", { y: 0 }, { y: 70, duration: 1.4, ease: FX.ease.cam, immediateRender: false }, S(371.3));
    })();

    /* ============ C6S072 · 376.05–379.89 · still a one-party state ============ */
    whip("071", "072", S(376.05), { dir: 1, vertical: true });
    scene("072", 376.05, 379.89);
    ground("night", S(376.05));
    (function () {
      tl.fromTo("#c6s02-sc072-cam", { scale: 1.0 }, { scale: 1.06, duration: 3.9, ease: "none", immediateRender: false }, S(376.05));
      // KMT emblem (Blue Sky, White Sun), redrawn in neutral bone/ink
      const em = $("sc072-emb"); let rays = "";
      for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6, b1 = a - 0.13, b2 = a + 0.13; rays += '<path d="M' + (Math.cos(b1) * 44).toFixed(1) + " " + (Math.sin(b1) * 44).toFixed(1) + " L" + (Math.cos(a) * 86).toFixed(1) + " " + (Math.sin(a) * 86).toFixed(1) + " L" + (Math.cos(b2) * 44).toFixed(1) + " " + (Math.sin(b2) * 44).toFixed(1) + ' Z" fill="#f2ede3"/>'; }
      em.innerHTML = '<circle r="98" fill="#1b2230" stroke="#f2ede3" stroke-width="3"/>' + rays + '<circle r="44" fill="#1b2230"/><circle r="37" fill="#f2ede3"/>';
      tl.fromTo(em, { opacity: 0, scale: 0.7, rotation: -20 }, { opacity: 0.92, scale: 1, rotation: 0, duration: 1.0, ease: C(FX.ease.out, 1.0), immediateRender: true }, S(376.3));
      line("sc072-o", [["ONE-", T(376.93)], ["PARTY ", T(377.17)], ["STATE", T(377.57)]]);
      line("sc072-c", [["change", T(378.53)]], { dur: 0.6 });
      line("sc072-d", [["down ", T(379.01)], ["the ", T(379.25)], ["line", T(379.33)]], { dur: 0.4 });
      const svg = $("sc072-svg"), f = FX.markupDefs(svg, "c6s02-mk72", { boil: 4 });
      FX.markup.pen(tl, svg, S(378.98), { points: [[760, 880], [920, 872], [1120, 878], [1260, 870]], width: 7, color: BONE, blend: "normal", filter: f, dur: 0.32, seed: 7201 });
      FX.markup.pen(tl, svg, S(379.28), { points: [[1222, 840], [1264, 870], [1224, 902]], width: 7, color: BONE, blend: "normal", filter: f, dur: 0.1, seed: 7202 });   // arrow done 379.38, holds 0.5 s; CA = camera push
    })();

    /* ============ C6S073 · 379.89–385.17 · the reason … "I don't know where I heard this" (lamp-lit shelf) ============ */
    scene("073", 379.89, 385.17);
    ground("night", S(379.89));
    (function () {
      // a lamp-lit shelf of history books: spines drawn as paper-textured blocks (no invented titles)
      const sh = $("sc073-shelf"), r = FX.rng(7300), cols = ["#3b3127", "#4a3b2c", "#2c2a26", "#5a4632", "#33302b", "#6b5a43", "#2a2e33", "#4c4237"];
      div("", "position:absolute;left:-100px;top:840px;width:2400px;height:60px;background:linear-gradient(180deg,#5a4532,#2a1f16);box-shadow:0 20px 40px rgba(0,0,0,0.7)", sh);
      let x = -60, book = null;
      for (let i = 0; i < 30; i++) {
        const w = 60 + Math.floor(r() * 70), h = 420 + Math.floor(r() * 300);
        const b = div("", "position:absolute;left:" + x + "px;top:" + (840 - h) + "px;width:" + w + "px;height:" + h + "px;background:" + cols[i % cols.length] + ";box-shadow:inset -6px 0 10px rgba(0,0,0,0.45), inset 4px 0 6px rgba(255,255,255,0.06)", sh);
        div("", "position:absolute;inset:0;background:url('assets/textures/paper_fiber_01.jpg') center/cover;mix-blend-mode:multiply;opacity:0.5", b);
        div("", "position:absolute;left:8px;right:8px;top:" + (40 + Math.floor(r() * 30)) + "px;height:3px;background:rgba(214,190,140,0.55)", b);
        div("", "position:absolute;left:8px;right:8px;bottom:50px;height:3px;background:rgba(214,190,140,0.45)", b);
        if (i === 18) book = { x: x + w / 2, y: 840 - h / 2, el: b };
        x += w + 4;
      }
      tl.fromTo("#c6s02-sc073-cam", { x: 0, filter: "blur(5px)" }, { x: -160, filter: "blur(0px)", duration: 5.3, ease: FX.ease.cam, immediateRender: false }, S(379.89));
      FX.focusHunt(tl, $("sc073-shelf"), S(381.6), { dur: 0.8 });
      line("sc073-r", [["the ", T(380.13)], ["reason", T(380.21)]]);
      line("sc073-c", [["change", T(382.21)]]);
      // no text on the aside; the one book slides out of the shelf toward us
      tl.to(book.el, { y: 40, scale: 1.08, boxShadow: "0 30px 50px rgba(0,0,0,0.8)", duration: 1.0, ease: C(FX.ease.out, 1.0) }, S(383.3));   // done 384.3, holds before the push-through (384.83)
      $("sc073").dataset.ox = book.x - 160; $("sc073").dataset.oy = book.y;
    })();

    /* ============ C6S074 · 385.17–390.45 · Sarah Paine — Asian history ============ */
    push("073", "074", S(385.17), +$("sc073").dataset.ox, +$("sc073").dataset.oy);
    scene("074", 385.17, 390.50);
    ground("paper", S(385.17));
    (function () {
      torn($("sc074-ph"), 7401);
      tl.fromTo("#c6s02-sc074-cam", { scale: 1.0, x: 0 }, { scale: 1.04, x: -30, duration: 5.3, ease: "none", immediateRender: false }, S(385.17));
      tl.fromTo("#c6s02-sc074-n", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(386.29) - L);
      $("sc074-n").innerHTML = '<span class="c62-lbox" id="c6s02-sc074-nb"></span>';
      line("sc074-nb", [["SARAH ", T(386.29)], ["PAINE", T(386.69)]], { dur: 0.5, y: 0 });
      tl.fromTo("#c6s02-sc074-map", { opacity: 1, x: 900, rotation: 12 }, { x: 0, rotation: 5, duration: 0.8, ease: C(FX.ease.out, 0.8), immediateRender: true }, S(388.9));   // done 389.7
      line("sc074-a", [["Asian ", T(389.49)], ["history", T(389.89)]], { dur: 0.35 });
    })();

    /* ============ C6S075–076 · 390.45–401.41 · "we are China" → the mainland burns red; BEING TAIWANESE ============ */
    whip("074", "075", S(390.45), { dir: 1 });
    scene("075", 390.45, SEG_END);
    ground("night", S(390.45));
    (function () {
      const cam = $("sc075-cam"), W = PD.eaW, H = PD.eaH;
      const svg = $("sc075-svg"); svg.setAttribute("viewBox", "0 0 " + W + " " + H);
      svg.innerHTML = `<defs>
        <filter id="c6s02-b76" filterUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}" color-interpolation-filters="sRGB">
          <feImage href="assets/maps/burn_a.png" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="none" result="n"/>
          <feColorMatrix id="c6s02-b76m" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 -12.5" result="t"/>
          <feComposite in="SourceGraphic" in2="t" operator="in"/></filter>
        <filter id="c6s02-c76" filterUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}" color-interpolation-filters="sRGB">
          <feImage href="assets/maps/burn_a.png" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="none" result="n"/>
          <feColorMatrix id="c6s02-c76a" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 -10.3" result="e"/>
          <feColorMatrix id="c6s02-c76b" in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 -12.5" result="l"/>
          <feComposite in="e" in2="l" operator="arithmetic" k1="0" k2="1" k3="-1" k4="0" result="ring"/>
          <feFlood flood-color="#f2b25c" result="fl"/><feComposite in="fl" in2="ring" operator="in" result="r2"/>
          <feComposite in="r2" in2="SourceAlpha" operator="in"/></filter></defs>
        <image id="c6s02-sc075-cel" href="assets/c6/derived/c6s02/claim_china_celadon.png" x="0" y="0" width="${W}" height="${H}" opacity="0"/>
        <image href="assets/c6/derived/c6s02/claim_china_red.png" x="0" y="0" width="${W}" height="${H}" opacity="0.72" filter="url(#c6s02-b76)"/>
        <image href="assets/c6/derived/c6s02/claim_china_red.png" x="0" y="0" width="${W}" height="${H}" filter="url(#c6s02-c76)"/>
        <path d="${PD.eaChina}" fill="none" stroke="#f2ede3" stroke-opacity="0.35" stroke-width="2.5"/>`;
      const tw = $("sc075-tw"), bx = PD.eaTwBox;
      Object.assign(tw.style, { left: bx[0] + "px", top: bx[1] + "px", width: bx[2] + "px", height: bx[3] + "px", filter: "drop-shadow(0 0 4px rgba(159,199,178,0.9))" });
      const at = (s, cx, cy, oy) => ({ scale: s, x: 960 - cx * s, y: 540 + (oy || 0) - cy * s });
      gsap.set(cam, at(0.72, 1500, 860));
      tl.fromTo(cam, at(0.72, 1500, 860), Object.assign(at(0.62, 1548, 860, 10), { duration: 3.6, ease: FX.ease.cam, immediateRender: false }), S(390.45));   // pull back to the whole claim
      // the claim: all of China + Taiwan in celadon (ROC), watercolour-soft fade at 12 fps
      tl.to("#c6s02-sc075-cel", { attr: { opacity: 0.62 }, duration: 1.0, ease: C(FX.ease.out, 1.0) }, S(390.85));
      tl.to(tw, { opacity: 1, duration: 1.0, ease: C(FX.ease.out, 1.0) }, S(390.85));
      line("sc075-wc", [["we ", T(391.73)], ["are ", T(391.81)], ["China", T(392.05)]]);
      line("sc075-wr", [["the ", T(392.45)], ["world ", T(392.61)], ["recognizes ", T(392.85)], ["us", T(393.41)]]);
      Object.assign($("sc075-tp").style, { left: "1480px", top: "880px" });
      line("sc075-tp", [["Taiwanese ", T(394.61)], ["people", T(395.25)]], { dur: 0.6 });
      // C6S076 — "not China anymore": the mainland burns from celadon to red (PRC); only Taiwan stays celadon
      tl.to(["#c6s02-sc075-wc", "#c6s02-sc075-wr", "#c6s02-sc075-tp"], { opacity: 0, duration: 0.3 }, S(395.9));
      line("sc075-nc", [["not ", T(397.97)], ["China ", T(398.13)], ["anymore", T(398.53)]]);
      const M = (o) => "0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  12 0 0 0 " + o.toFixed(3);
      const b = { v: -12.5 };
      tl.fromTo(b, { v: -12.5 }, { v: 1.2, duration: 1.5, ease: C("power1.inOut", 1.5), immediateRender: false, onUpdate: () => { $("b76m").setAttribute("values", M(b.v)); $("c76a").setAttribute("values", M(b.v + 2.2)); $("c76b").setAttribute("values", M(b.v)); } }, S(397.95));   // done 399.45
      tl.to("#c6s02-sc075-cel", { attr: { opacity: 0.2 }, duration: 1.5, ease: "none" }, S(398.0));
      tl.to("#c6s02-sc075-nc", { opacity: 0, duration: 0.3 }, S(399.5));
      // push from the mainland onto Taiwan, focus hunt as it lands
      tl.to(cam, Object.assign(at(2.4, PD.eaTwC[0], PD.eaTwC[1], -60), { duration: 1.0, ease: FX.ease.cam }), S(398.6));
      FX.focusHunt(tl, cam, S(399.6), { dur: 0.55 });
      tl.to(tw, { filter: "drop-shadow(0 0 10px rgba(190,230,205,1))", duration: 0.8, ease: "sine.inOut" }, S(399.6));
      line("sc075-bt", [["BEING ", T(400.21)], ["TAIWANESE", T(400.45)]], { dur: 0.15, y: 10 });   // settled 400.54
      tl.to(cam, Object.assign(at(2.5, PD.eaTwC[0], PD.eaTwC[1], -60), { duration: 1.1, ease: "none" }), S(400.15));
      // whip ↓ — first half only (c6s03 lands the paper chart from above); SFX in this file at 401.33
      const sc = $("sc075");
      tl.set(sc, { filter: "url(#c6s02-wb075)" }, S(401.24));
      tl.fromTo(sc, { y: 0, scale: 1 }, { y: 700, scale: 1.18, duration: 0.16, ease: "power3.in", immediateRender: false }, S(401.25));
      const wb = { v: 0 };
      tl.fromTo(wb, { v: 0 }, { v: 90, duration: 0.16, ease: "power2.in", immediateRender: false, onUpdate: () => blurs["075"].setAttribute("stdDeviation", "0 " + wb.v.toFixed(2)) }, S(401.25));
    })();

    // every scene except the first starts display:none (layout-dependent FX were built above, MANUAL §4.2)
    Array.from(document.querySelectorAll("#c6s02-sc043, #c6s02-sc044, #c6s02-sc045, #c6s02-sc046, #c6s02-sc047, #c6s02-sc048, #c6s02-sc049, #c6s02-sc050, #c6s02-sc051, #c6s02-sc052, #c6s02-sc053, #c6s02-sc055, #c6s02-sc056, #c6s02-sc057, #c6s02-sc058, #c6s02-sc059, #c6s02-sc060, #c6s02-sc061, #c6s02-sc062, #c6s02-sc063, #c6s02-sc065, #c6s02-sc066, #c6s02-sc067, #c6s02-sc068, #c6s02-sc070, #c6s02-sc071, #c6s02-sc072, #c6s02-sc073, #c6s02-sc074, #c6s02-sc075")).forEach((e) => gsap.set(e, { display: "none" }));
