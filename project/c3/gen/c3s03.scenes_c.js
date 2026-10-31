    /* =================== C3S104 · 550.59–556.59 · Now, as years pass, there's decolonization that's happening inside of Africa =================== */
    scene("sc104", 550.53, 556.59);
    ground("night", S(550.53));
    (function () {
      const svg = $("sc104-svg"), cam = $("sc104-cam"), A = MAPS.africa.geo, K = A.k;
      const ll = (lon, lat) => [(lon - A.lon0) * K, (A.lat1 - lat) * K];
      const at = (lon, lat, z) => { const [x, y] = ll(lon, lat); return { x: 960 - x * z, y: 540 - y * z, scale: z }; };
      const D = MAPS.africa.d;
      // colonial blocks c.1950 (each drawn as one grey halftone mass with a bone rim); independent states only outlined
      const BLOCKS = [["mauritania", "senegal", "mali", "guinea", "c_te_d_ivoire", "burkina_faso", "niger", "benin"], ["chad", "central_african_rep", "congo", "gabon"],
        ["cameroon", "togo"], ["morocco", "algeria", "tunisia"], ["w_sahara", "eq_guinea"], ["ghana", "nigeria", "sierra_leone", "gambia"], ["kenya", "uganda", "tanzania"],
        ["zambia", "malawi", "zimbabwe"], ["sudan", "s_sudan"], ["dem_rep_congo", "rwanda", "burundi"], ["angola", "mozambique", "guinea_bissau"],
        ["somalia", "somaliland", "djibouti"], ["libya"], ["botswana", "lesotho", "eswatini", "namibia"], ["madagascar"]];
      const INDEP = ["egypt", "ethiopia", "eritrea", "liberia", "south_africa"];
      // independence order (assets/c3/data/africa_independence.json, grouped by year)
      const ORDER = ["libya", "sudan", "s_sudan", "morocco", "tunisia", "ghana", "guinea", "cameroon", "togo", "senegal", "mali", "madagascar", "dem_rep_congo", "somalia", "somaliland",
        "benin", "niger", "burkina_faso", "c_te_d_ivoire", "chad", "central_african_rep", "congo", "gabon", "nigeria", "mauritania", "sierra_leone", "tanzania", "rwanda", "burundi",
        "algeria", "uganda", "kenya", "malawi", "zambia", "gambia", "botswana", "lesotho", "eswatini", "eq_guinea", "guinea_bissau", "angola", "mozambique", "djibouti", "zimbabwe", "namibia"];
      let h = `<g fill="none" stroke="${BONE}" stroke-width="5" stroke-opacity="0.75">${INDEP.map((k) => `<path d="${D[k]}"/>`).join("")}</g>`;
      BLOCKS.forEach((b) => {
        h += `<g>${b.map((k) => `<path d="${D[k]}" fill="none" stroke="${BONE}" stroke-width="12" stroke-opacity="0.7"/>`).join("")}${b.map((k) => `<path id="c3s03-a104f-${k}" d="${D[k]}" fill="url(#c3s03-ht-col)" stroke="none"/>`).join("")}</g>`;
      });
      h += `<g id="c3s03-sc104-new" filter="url(#c3s03-glowS)">${ORDER.map((k) => `<path id="c3s03-a104b-${k}" d="${D[k]}" fill="${BONE}" fill-opacity="0.1" stroke="${BONE}" stroke-width="6" opacity="0"/>`).join("")}</g>`;
      svg.innerHTML = h;
      ORDER.forEach((k, i) => {
        const t = S(553.15) + Math.floor(i / 2) / 12;
        tl.fromTo($("a104f-" + k), { attr: { "fill-opacity": 1 } }, { attr: { "fill-opacity": 0 }, duration: 0.001, immediateRender: true }, t);
        attrOn($("a104b-" + k), t);
      });
      tl.fromTo(cam, at(18, 2, 0.375), Object.assign(at(16, 4, 0.47), { duration: 5.7, ease: E.cam, immediateRender: true }), S(550.53));
      tl.to(cam, Object.assign(at(16, 4, 0.55), { duration: 0.36, ease: E.in }), S(556.23));
      rise($("sc104-dc"), T(553.09), { dur: 1.0, y: 14 });
      rise($("sc104-af"), T(555.73), { dur: 0.5, y: 8 });
    })();

    /* =================== C3S105 · 556.59–560.64 · Very far away from China, but unfortunately. =================== */
    scene("sc105", 556.59, 560.66);
    ground("paper", S(556.59));
    (function () {
      const plane = $("sc105-plane"), svg = $("sc105-svg");
      const [ax, ay] = wll(-1, 7), [bx, by] = wll(116.4, 39.9);
      const qx = (ax + bx) / 2, qy = Math.min(ay, by) - 520;
      svg.innerHTML = `<mask id="c3s03-m105" maskUnits="userSpaceOnUse" x="0" y="0" width="6144" height="3072"><path id="c3s03-m105p" d="M${ax} ${ay} Q${qx} ${qy} ${bx} ${by}" stroke="#fff" stroke-width="40" fill="none"/></mask>
        <path d="M${ax} ${ay} Q${qx} ${qy} ${bx} ${by}" stroke="${INK}" stroke-width="12" stroke-dasharray="44 28" fill="none" mask="url(#c3s03-m105)"/>
        <circle cx="${ax}" cy="${ay}" r="22" fill="${INK}"/><circle id="c3s03-sc105-pb" cx="${bx}" cy="${by}" r="22" fill="${INK}" opacity="0"/>`;
      const mp = $("m105p"), L = mp.getTotalLength ? 2600 : 2600; mp.setAttribute("stroke-dasharray", `${L} ${L}`); mp.setAttribute("stroke-dashoffset", L);
      tl.fromTo(mp, { attr: { "stroke-dashoffset": L } }, { attr: { "stroke-dashoffset": 0 }, duration: 1.6, ease: C(E.inOut, 1.6), immediateRender: true }, S(556.85));
      attrOn($("sc105-pb"), S(558.40));
      // tilted atlas (D10): scale 0.62, tipped back 42°, panned from West Africa to China
      const z = 0.62, P = (x, y) => ({ x: 960 - x * z, y: 620 - y * z });
      gsap.set(plane, { rotationX: 42, scale: z, transformOrigin: "0 0" });
      tl.fromTo(plane, P(ax + 300, ay - 300), Object.assign(P(bx - 500, by), { duration: 1.5, ease: E.cam, immediateRender: true }), S(556.65));
      tl.to(plane, Object.assign(P(bx - 380, by + 40), { duration: 2.45, ease: "none" }), S(558.15));
      tl.to(plane, Object.assign(P(bx - 200, by + 60), { duration: 0.25, ease: E.in }), S(560.40));
      [T(556.85), T(557.17)].forEach((c, i) => rise(words("sc105-fa")[i], c, { dur: 0.7, y: 10 }));
      rise($("sc105-cn"), T(557.73), { dur: 0.6, y: 8 });
    })();
    whip($("sc105-shot"), $("sc106-shot"), S(560.58), { dir: -1 });

    /* =================== C3S106 · 560.64–568.56 · That decolonization is gonna have a drastic impact on this fight … between the CCP and the ROC =================== */
    scene("sc106", 560.58, 568.70);
    ground("night", S(560.58));
    (function () {
      gated(560.5, 568.7, () => FX.weave($("sc106-pl"), { amp: 1.1, flicker: 0.04, seed: 106 }));
      tl.fromTo($("sc106-cam"), { scale: 1.0 }, { scale: 1.07, duration: 8.1, ease: "none", immediateRender: true }, S(560.58));
      [T(562.66), T(563.30)].forEach((c, i) => rise(words("sc106-di")[i], c, { dur: 0.8, y: 10 }));
      out($("sc106-di"), S(565.60), 0.3);
      tl.to($("sc106-cam"), { filter: "brightness(0.35)", duration: 0.5, ease: C("none", 0.5) }, S(566.10));
      pop($("sc106-ccpb"), T(566.42), 0.8);
      pop($("sc106-rocb"), T(567.70), 0.3);
    })();

    /* =================== C3S107 · 568.56–576.80 · every new country … being born in Africa … has now a new vote =================== */
    scene("sc107", 568.31, 576.80);
    ground("paper", S(568.40));
    slideIn($("sc107-shot"), S(568.50));
    (function () {
      const svg = $("sc107-svg"), cx = 1080, cy = 780, rows = [230, 278, 326, 374, 422, 470], N = 110;
      const tot = rows.reduce((a, r) => a + r, 0), pts = [];
      rows.forEach((r) => { const n = Math.round(N * r / tot); for (let k = 0; k < n; k++) { const a = Math.PI * (1 - k / (n - 1)); pts.push([cx + r * Math.cos(a), cy - r * Math.sin(a), a]); } });
      pts.sort((p, q) => q[2] - p[2]);
      const rng = FX.rng(10700), isNew = new Set();
      while (isNew.size < 28) isNew.add(Math.floor(rng() * pts.length));
      let j = 0;
      pts.forEach((p, i) => {
        if (isNew.has(i)) {
          svg.insertAdjacentHTML("beforeend", `<circle id="c3s03-n107-${j}" cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="15" fill="${INK}" opacity="0"/>`);
          const el = $("n107-" + j), t = S(571.14) + Math.floor(j / 2) / 12;
          tl.fromTo(el, { attr: { opacity: 0, r: 4 } }, { attr: { opacity: 1, r: 15 }, duration: 0.25, ease: C(E.out, 0.25), immediateRender: true }, t);
          j++;
        } else svg.insertAdjacentHTML("beforeend", `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="13" fill="#ddd3bf" stroke="${INK}" stroke-width="3" opacity="0.75"/>`);
      });
      svg.insertAdjacentHTML("beforeend", `<path d="M${cx - 520} ${cy + 26} L${cx + 520} ${cy + 26}" stroke="${INK}" stroke-width="3" opacity="0.5"/>`);
      const cam = $("sc107-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.04, duration: 8.1, ease: "none", immediateRender: true }, S(568.31));
      tl.to(cam, { scale: 1.1, duration: 0.3, ease: E.in }, S(576.50));
      [T(569.86), T(570.10)].forEach((c, i) => rise(words("sc107-nc")[i], c, { dur: 0.8, y: 10 }));
      rise($("sc107-bo"), T(571.14), { dur: 0.8, y: 10 });
      [T(575.86), T(576.18)].forEach((c, i) => rise(words("sc107-nv")[i], c, { dur: 0.3, y: 6 }));
      gsap.set($("sc107-hl"), { scaleX: 0 });
      tl.fromTo($("sc107-hl"), { scaleX: 0 }, { scaleX: 1, duration: 0.36, ease: "sine.inOut", immediateRender: false }, S(575.92));
      tl.fromTo($("sc107-bal"), { opacity: 0, scale: 0.7, rotation: -10 }, { opacity: 1, scale: 1, rotation: 4, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(575.86));
    })();

    /* =================== C3S108 · 576.80–584.48 · inside of the UN General Assembly … very useful if you can somehow get that vote on your side =================== */
    scene("sc108", 576.80, 584.62);
    ground("night", S(576.80));
    (function () {
      const stack = (el, col) => { el.innerHTML = [0, 1, 2, 3].map((k) => `<div class="k-ballot" style="top:${30 - k * 9}px; left:${(k % 2) * 6 - 3}px; transform:rotate(${(k % 2 ? 2 : -2.5)}deg)"><div class="bd" style="background:${col}"></div><div class="ln" style="top:40px"></div><div class="ln" style="top:70px; right:70px"></div></div>`).join(""); };
      stack($("sc108-sl"), RED); stack($("sc108-sr"), CEL);
      tl.fromTo($("sc108-cam"), { scale: 1.0 }, { scale: 1.07, duration: 7.7, ease: "none", immediateRender: true }, S(576.80));
      [T(577.54), T(577.94), T(578.34)].forEach((c, i) => rise(words("sc108-un")[i], c, { dur: 0.8, y: 14 }));
      out($("sc108-un"), S(580.45), 0.35);
      rise($("sc108-us"), T(580.98), { dur: 0.8, y: 10 });
      out($("sc108-us"), S(582.40), 0.3);
      tl.fromTo($("sc108-sl"), { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(581.60));
      tl.fromTo($("sc108-sr"), { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: C(E.out, 0.6), immediateRender: true }, S(581.75));
      tl.fromTo($("sc108-one"), { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: C(E.out, 0.4), immediateRender: true }, S(582.55));
      tl.to($("sc108-one"), { x: 556, y: 32, rotation: 3, duration: 0.75, ease: C(E.inOut, 0.75) }, S(583.20));
      [T(583.70), T(583.94)].forEach((c, i) => rise(words("sc108-ys")[i], c, { dur: 0.3, y: 6 }));
    })();

    /* =================== C3S109 · 584.48–591.92 · explain just quickly how the UN works because everyone knows … watching this podcast =================== */
    scene("sc109", 584.23, 591.94);
    ground("paper", S(584.30));
    slideIn($("sc109-shot"), S(584.42), { from: "y", dist: -1200, rot: 0 });
    (function () {
      const cam = $("sc109-cam");
      tl.fromTo(cam, { scale: 1.0 }, { scale: 1.02, duration: 2.6, ease: "none", immediateRender: true }, S(584.23));
      tl.to(cam, { scale: 1.45, duration: 1.6, ease: E.cam }, S(586.82));
      tl.to(cam, { scale: 1.52, duration: 3.45, ease: "none" }, S(588.42));
      FX.focusHunt(tl, cam, S(588.30), { dur: 0.8 });
      tl.fromTo($("sc109-po"), { y: 0 }, { y: -10, duration: 7.6, ease: "none", immediateRender: true }, S(584.23));
      [T(586.82), T(586.98), T(587.14), T(587.62)].forEach((c, i) => rise(words("sc109-hw")[i], c, { dur: 0.7, y: 10 }));
    })();
    whip($("sc109-shot"), $("sc110-shot"), S(591.86), { dir: 1, vertical: true });

    /* =================== C3S110 · 591.92–597.44 · that there's a veto in UN permanent members. So the United States, the UK, =================== */
    scene("sc110", 591.86, 597.60);
    ground("night", S(591.86));
    (function () {
      tl.fromTo($("sc110-cam"), { scale: 1.0 }, { scale: 1.08, duration: 5.7, ease: "none", immediateRender: true }, S(591.86));
      tl.set($("sc110-a"), { opacity: 0 }, S(594.30));
      tl.fromTo($("sc110-b"), { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, S(594.30));
      tl.fromTo($("sc110-veto"), { opacity: 0, scale: 1.12 }, { opacity: 1, scale: 1, duration: 1.0, ease: C(E.out, 1.0), immediateRender: true }, T(592.50));
      [T(593.78), T(594.18)].forEach((c, i) => rise(words("sc110-pm")[i], c, { dur: 0.7, y: 10 }));
      pop($("sc110-fus"), S(595.38), 0.7); rise($("sc110-lus"), T(595.38), { dur: 0.6, y: 8 });
      pop($("sc110-fuk"), S(596.58), 0.5); rise($("sc110-luk"), T(596.58), { dur: 0.4, y: 8 });
    })();

    /* =================== C3S111 · 597.44–602.02 · France, China, and now Russia, but back then it was the Soviet Union. (→ c4) =================== */
    scene("sc111", 597.19, SEG_END);
    ground("paper", S(597.30));
    slideIn($("sc111-shot"), S(597.38));
    (function () {
      tl.fromTo($("sc111-cam"), { scale: 1.07 }, { scale: 1.0, duration: 4.83, ease: "none", immediateRender: true }, S(597.19));
      pop($("sc111-ffr"), S(597.38), 0.7); rise($("sc111-lfr"), T(597.38), { dur: 0.7, y: 8 });
      pop($("sc111-fcn"), S(598.26), 0.8); rise($("sc111-lcn"), T(598.26), { dur: 0.8, y: 8 });
      pop($("sc111-flip"), S(599.86), 0.8); rise($("sc111-lru"), T(599.86), { dur: 0.8, y: 8 });
      // card flip: Russia → USSR
      const fl = $("sc111-flip");
      tl.to(fl, { rotationY: 90, duration: 0.13, ease: "power2.in" }, S(601.14));
      tl.set($("sc111-fru"), { opacity: 0 }, S(601.27)); tl.set($("sc111-fsu"), { opacity: 1 }, S(601.27));
      tl.fromTo(fl, { rotationY: -90 }, { rotationY: 0, duration: 0.14, ease: "power2.out", immediateRender: false }, S(601.27));
      out($("sc111-lru"), S(601.02), 0.12);
      [T(601.14), T(601.46)].forEach((c, i) => rise(words("sc111-lsu")[i], c, { dur: 0.3, y: 6 }));
    })();
