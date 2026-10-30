<!doctype html>
<html lang="en">
<head><meta charset="UTF-8" /></head>
<body>
<template>
  <style>
    #root { position: absolute; inset: 0; overflow: hidden; background: var(--night); }
    .seg03-scene { position: absolute; inset: 0; overflow: hidden; visibility: hidden; }
    .seg03-paper { background: var(--paper); }
    .seg03-night { background: var(--night); }
    .seg03-abs { position: absolute; }
    .seg03-tx { position: absolute; inset: 0; pointer-events: none; }
    /* s08 card style (shared by every card in this segment) */
    .seg03-card { position: absolute; background: #f3ecdc; padding: 14px; filter: url(#seg03-rough); box-shadow: 0 18px 40px rgba(35,48,58,0.28); }
    .seg03-card .ph { position: relative; width: 100%; height: 100%; overflow: hidden; }
    .seg03-card img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: url(#seg03-tint-ink) contrast(1.05); }
    .seg03-card .ht { position: absolute; inset: 0; background-size: 520px auto; mix-blend-mode: multiply; opacity: 0.55; }
    .seg03-tag { position: absolute; background: var(--ink); color: var(--paper); padding: 10px 18px 8px; font-size: 22px; white-space: nowrap; }
    .seg03-tag .word { margin-right: 0.35em; }
    .seg03-shade-b { position: absolute; left: 0; right: 0; bottom: 0; height: 520px; background: linear-gradient(180deg, rgba(13,12,11,0), rgba(13,12,11,0.8)); }

    /* ---------- SC035 · R6 chart card ---------- */
    #seg03-sc035-bg { position: absolute; inset: -40px; background-size: cover; background-position: center 45%; filter: sepia(0.25) saturate(0.55) brightness(0.55) blur(2px); }
    #seg03-sc035-card { position: absolute; inset: 0; background: var(--paper); box-shadow: -40px 0 80px rgba(0,0,0,0.55); transform-origin: 50% 0%; }
    #seg03-sc035-ghost { position: absolute; right: -60px; bottom: -40px; width: 1100px; height: 571px; background-size: cover; filter: url(#seg03-tint-ink); opacity: 0.16; mix-blend-mode: multiply;
      -webkit-mask-image: radial-gradient(ellipse 55% 60% at 62% 62%, #000 35%, transparent 80%); mask-image: radial-gradient(ellipse 55% 60% at 62% 62%, #000 35%, transparent 80%); }
    #seg03-sc035-ghost .ht { position: absolute; inset: 0; background-size: 420px auto; mix-blend-mode: screen; opacity: 0.6; }
    #seg03-sc035-title { position: absolute; left: 140px; top: 150px; font-size: 92px; line-height: 1.05; color: var(--ink); }
    #seg03-sc035-title i { font-style: italic; color: var(--vermilion); }
    #seg03-sc035-sub { position: absolute; left: 144px; top: 268px; font-size: 46px; color: var(--ink-soft); }
    .seg03-sc035-lab { position: absolute; left: 166px; font-size: 24px; color: var(--ink); }
    .seg03-sc035-track { position: absolute; left: 144px; width: 1360px; height: 84px; }
    #seg03-sc035-before { top: 470px; border: 3px dashed rgba(24,34,47,0.45); }
    #seg03-sc035-after { top: 660px; }
    #seg03-sc035-afterfill { position: absolute; left: 0; top: 0; height: 100%; width: 860px; background: var(--vermilion); transform-origin: 0 50%; }
    #seg03-sc035-afterfill::after { content: ""; position: absolute; inset: 0; background: url('assets/textures/grain_02_norm.jpg'); background-size: 600px auto; mix-blend-mode: overlay; opacity: 0.5; }
    #seg03-sc035-axis { position: absolute; left: 144px; top: 800px; width: 1360px; height: 2px; background: var(--ink); transform-origin: 0 50%; }
    #seg03-sc035-axis0 { position: absolute; left: 143px; top: 440px; width: 2px; height: 362px; background: var(--ink); transform-origin: 50% 100%; }
    #seg03-sc035-end { position: absolute; left: 1030px; top: 664px; font-size: 54px; }
    #seg03-sc035-src { position: absolute; left: 144px; top: 830px; font-size: 22px; color: var(--ink-soft); }

    /* ---------- SC036 · Founding Grant document ---------- */
    #seg03-sc036-bg { position: absolute; inset: -60px; background-size: cover; background-position: center 25%; filter: url(#seg03-tint-night) blur(5px); opacity: 0.55; transform: scale(1.4) rotate(-7deg); }
    #seg03-sc036-cam { position: absolute; left: 0; top: 0; width: 1200px; height: 2051px; transform-origin: 0 0; }
    #seg03-sc036-page { position: absolute; left: 0; top: 0; width: 1200px; height: 2051px; transform-origin: 50% 30%; box-shadow: 0 40px 120px rgba(0,0,0,0.7); }
    #seg03-sc036-page img { position: absolute; inset: 0; width: 100%; height: 100%; filter: sepia(0.3) contrast(1.08) brightness(0.95); }
    #seg03-sc036-page .ht { position: absolute; inset: 0; background-size: 260px auto; mix-blend-mode: overlay; opacity: 0.45; }
    #seg03-sc036-page .pp { position: absolute; inset: 0; background-size: cover; mix-blend-mode: multiply; opacity: 0.3; }
    #seg03-sc036-marks { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
    #seg03-sc036-dim { position: absolute; inset: 0; background: linear-gradient(90deg, rgba(14,12,10,0) 38%, rgba(14,12,10,0.72) 60%, rgba(14,12,10,0.86)); }
    #seg03-sc036-against { position: absolute; left: 1230px; top: 300px; width: 640px; font-size: 76px; }
    #seg03-sc036-trust { position: absolute; left: 1226px; top: 410px; width: 680px; font-size: 128px; }
    #seg03-sc036-trust > div { white-space: nowrap; }
    #seg03-sc036-clip { position: absolute; left: 1290px; top: 96px; }
    #seg03-sc036-photo { position: relative; width: 470px; height: 620px; background: #ece4d2; padding: 16px 16px 54px; filter: url(#seg03-roughsm); box-shadow: 0 30px 80px rgba(0,0,0,0.65); }
    #seg03-sc036-photo img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 36%; filter: sepia(0.25) contrast(1.05); }
    #seg03-sc036-lower { position: absolute; left: 1250px; top: 800px; width: 640px; }
    #seg03-sc036-lower .a { font-size: 46px; color: #e8dccb; }
    #seg03-sc036-lower .b { font-size: 92px; margin-top: 2px; }

    /* ---------- SC037 · no charge (strike) ---------- */
    #seg03-sc037-stage { position: absolute; inset: 0; transform-origin: 50% 50%; }
    #seg03-sc037-kick { position: absolute; left: 0; right: 0; top: 250px; text-align: center; font-size: 26px; color: var(--ink-soft); }
    #seg03-sc037-no { position: absolute; left: 0; right: 0; top: 330px; text-align: center; font-size: 250px; color: var(--ink); }
    #seg03-sc037-for { position: absolute; left: 0; right: 0; top: 610px; text-align: center; font-size: 92px; color: var(--ink); }
    #seg03-sc037-marks { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
    #seg03-sc037-seal { position: absolute; right: 120px; top: 90px; width: 250px; height: 250px; border-radius: 50%; overflow: hidden; border: 3px solid var(--ink); box-shadow: 0 0 0 10px var(--paper), 0 0 0 12px rgba(24,34,47,0.5); }
    #seg03-sc037-seal img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 35%; filter: url(#seg03-tint-ink) contrast(1.15); }
    #seg03-sc037-seal .ht { position: absolute; inset: 0; background-size: 300px auto; mix-blend-mode: multiply; opacity: 0.7; }

    /* ---------- SC038 · iris chain of campuses ---------- */
    #seg03-sc038-weave { position: absolute; inset: -16px; }
    .seg03-sc038-shot { position: absolute; inset: 0; visibility: hidden; }
    .seg03-sc038-shot .plate { transform-origin: 50% 50%; }
    .seg03-sc038-shot .plate .img { filter: sepia(0.32) saturate(0.5) contrast(1.06) brightness(0.86); }
    .seg03-sc038-shot .plate .fringe { filter: sepia(0.32) saturate(0.5) contrast(1.06) brightness(0.86) blur(7px); }
    #seg03-sc038-sh2 .img, #seg03-sc038-sh2 .fringe { object-position: 50% 30%; }
    #seg03-sc038-sh4 .img, #seg03-sc038-sh4 .fringe { object-position: 0% 50%; }
    .seg03-sc038-lab { position: absolute; left: 110px; top: 90px; font-size: 24px; color: #e8dccb; visibility: hidden; }
    #seg03-sc038-comp { position: absolute; left: 0; right: 0; top: 640px; text-align: center; font-size: 190px; }
    #seg03-sc038-long { position: absolute; left: 0; right: 0; top: 840px; text-align: center; font-size: 72px; color: #e8dccb; }

    /* ---------- SC039 · money (choke + highlighter) ---------- */
    #seg03-sc039-fan { position: absolute; inset: 0; }
    .seg03-sc039-note { position: absolute; width: 640px; height: 274px; background: #f3ecdc; padding: 10px; box-shadow: 0 18px 40px rgba(35,48,58,0.3); filter: url(#seg03-roughsm); }
    .seg03-sc039-note .ph { position: relative; width: 100%; height: 100%; overflow: hidden; }
    .seg03-sc039-note img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: url(#seg03-tint-ink) contrast(1.12); }
    .seg03-sc039-note .ht { position: absolute; inset: 0; background-size: 380px auto; mix-blend-mode: multiply; opacity: 0.6; }
    #seg03-sc039-even { position: absolute; left: 130px; top: 360px; font-size: 64px; color: var(--ink-soft); }
    #seg03-sc039-massive { position: absolute; left: 124px; top: 440px; font-size: 132px; color: var(--ink); filter: url(#seg03-choke39); line-height: 1; }
    #seg03-sc039-massive .l2 { display: block; margin-top: 10px; }
    #seg03-sc039-hard { position: absolute; left: 130px; top: 740px; font-size: 60px; color: var(--ink); }

    /* ---------- SC040 · 1910s campus, weave ---------- */
    #seg03-sc040-weave { position: absolute; inset: -16px; }
    #seg03-sc040-plate { transform-origin: 50% 45%; }
    #seg03-sc040-plate .img { filter: sepia(0.45) saturate(0.45) contrast(1.1) brightness(0.8); object-position: 50% 60%; }
    #seg03-sc040-plate .fringe { filter: sepia(0.45) saturate(0.45) contrast(1.1) brightness(0.8) blur(7px); object-position: 50% 60%; }
    #seg03-sc040-vig { position: absolute; inset: -260px; background: radial-gradient(ellipse 70% 65% at 50% 50%, rgba(0,0,0,0) 35%, rgba(8,6,4,0.85) 100%); transform-origin: 50% 50%; }
    #seg03-sc040-issues { position: absolute; left: 110px; top: 690px; font-size: 110px; }
    #seg03-sc040-late { position: absolute; left: 116px; top: 850px; font-size: 64px; }
    #seg03-sc040-white { position: absolute; inset: 0; background: #f4eee2; opacity: 0; }

    /* ---------- SC041 · timeline + GSB card ---------- */
    #seg03-sc041-board { position: absolute; inset: 0; transform-origin: 50% 50%; }
    #seg03-sc041-kick { position: absolute; left: 160px; top: 96px; font-size: 26px; color: var(--ink); }
    #seg03-sc041-card { left: 770px; top: 170px; width: 800px; height: 470px; }
    #seg03-sc041-card img { object-position: 50% 62%; }
    #seg03-sc041-pin { position: absolute; left: 1145px; top: 136px; width: 52px; }
    #seg03-sc041-tag { left: 800px; top: 662px; font-size: 26px; }
    #seg03-sc041-pres { position: absolute; left: 1130px; top: 790px; width: 640px; text-align: right; font-size: 52px; color: var(--ink); }
    #seg03-sc041-lead { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
    .seg03-tl { position: absolute; left: 160px; top: 935px; width: 1600px; height: 80px; }
    .seg03-axis { position: absolute; left: 0; right: 0; top: 20px; height: 2px; background: var(--ink); transform-origin: 0 50%; }
    .seg03-tick { position: absolute; top: 12px; width: 2px; height: 18px; background: var(--ink); }
    .seg03-yr { position: absolute; top: 40px; font-size: 22px; color: var(--ink); transform: translateX(-50%); }
    .seg03-dot { position: absolute; top: 9px; left: 0; width: 24px; height: 24px; margin-left: -12px; border-radius: 50%; background: var(--vermilion); }
    .seg03-mark { position: absolute; top: -26px; width: 4px; height: 50px; background: var(--vermilion); margin-left: -2px; transform-origin: 50% 100%; }
    .seg03-mlab { position: absolute; top: -64px; font-size: 22px; color: var(--vermilion); transform: translateX(-50%); white-space: nowrap; }
    .seg03-gtag { position: absolute; top: -66px; font-size: 22px; color: var(--paper); background: #8a8f96; padding: 6px 12px 4px; transform: translateX(-50%); white-space: nowrap; }

    /* ---------- SC042/043 · US map ---------- */
    #seg03-map-cam { position: absolute; left: 0; top: 0; width: 6400px; height: 3200px; transform-origin: 0 0; }
    #seg03-map-base { position: absolute; inset: 0; width: 6400px; height: 3200px; filter: brightness(0.82) contrast(1.08) saturate(0.7); }
    .seg03-map-svg { position: absolute; left: 0; top: 0; width: 6400px; height: 3200px; overflow: visible; }
    #seg03-map-fills { mix-blend-mode: overlay; }
    .seg03-cloud { position: absolute; opacity: 0.6; }
    .seg03-cshadow { position: absolute; opacity: 0.28; filter: brightness(0) blur(18px); }
    .seg03-mlabel { position: absolute; white-space: nowrap; }
    #seg03-sc042-smart { left: 700px; top: 1560px; font-size: 120px; }
    #seg03-sc042-mit { left: 5790px; top: 950px; font-size: 92px; }
    #seg03-sc042-harv { left: 5730px; top: 810px; font-size: 92px; }
    #seg03-map-blur { position: absolute; inset: 0; }
    #seg03-sc043-marks { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
    #seg03-sc043-here { position: absolute; left: 820px; top: 300px; font-size: 250px; }
    #seg03-sc043-cal { position: absolute; left: 832px; top: 560px; font-size: 30px; color: #e8dccb; }
    #seg03-map-credit { position: absolute; right: 30px; bottom: 22px; font-size: 13px; letter-spacing: 0.08em; color: rgba(244,238,226,0.5); }

    /* ---------- SC044 · then vs now ---------- */
    #seg03-sc044-board { position: absolute; inset: 0; transform-origin: 50% 50%; }
    #seg03-sc044-deal { position: absolute; left: 160px; top: 70px; font-size: 72px; color: var(--ink); }
    #seg03-sc044-old { left: 150px; top: 230px; width: 700px; height: 420px; }
    #seg03-sc044-old img { object-position: 50% 62%; }
    #seg03-sc044-new { left: 1000px; top: 190px; width: 780px; height: 520px; }
    #seg03-sc044-new img { filter: url(#seg03-tint-warm) contrast(1.04); }
    #seg03-sc044-pin1 { position: absolute; left: 474px; top: 196px; width: 52px; }
    #seg03-sc044-pin2 { position: absolute; left: 1364px; top: 156px; width: 52px; }
    #seg03-sc044-otag { left: 176px; top: 672px; background: #8a8f96; }
    #seg03-sc044-tag { left: 1030px; top: 734px; font-size: 26px; }
    #seg03-sc044-dash { position: absolute; top: 20px; height: 2px; background: repeating-linear-gradient(90deg, var(--ink) 0 14px, transparent 14px 24px); transform-origin: 0 50%; }
    #seg03-sc044-now { position: absolute; top: 34px; font-size: 40px; color: var(--vermilion); transform: translateX(-50%); }
    #seg03-sc044-credit { position: absolute; right: 30px; bottom: 16px; font-size: 13px; letter-spacing: 0.08em; color: rgba(24,34,47,0.55); }

    /* ---------- SC045 · panorama + light leak ---------- */
    #seg03-sc045-weave { position: absolute; inset: -16px; }
    #seg03-sc045-pano { position: absolute; left: 0; top: -60px; height: 1200px; width: 7074px; }
    #seg03-sc045-pano .img { filter: sepia(0.4) saturate(0.5) contrast(1.08) brightness(0.72); }
    #seg03-sc045-pano .fringe { filter: sepia(0.4) saturate(0.5) contrast(1.08) brightness(0.72) blur(7px); }
    #seg03-sc045-leak { position: absolute; left: -700px; top: -200px; width: 3000px; height: 1500px; background-size: cover; mix-blend-mode: screen; opacity: 0;
      -webkit-mask-image: radial-gradient(ellipse 45% 55% at 50% 50%, #000 25%, transparent 72%); mask-image: radial-gradient(ellipse 45% 55% at 50% 50%, #000 25%, transparent 72%); }
    #seg03-sc045-shade { position: absolute; inset: 0; background: radial-gradient(ellipse 60% 45% at 50% 52%, rgba(10,9,8,0.6), rgba(10,9,8,0.1) 75%); }
    #seg03-sc045-over { position: absolute; left: 0; right: 0; top: 400px; text-align: center; font-size: 230px; }
    #seg03-sc045-marks { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }

    /* ---------- SC046 · a good start (streaks) ---------- */
    #seg03-sc046-glow { position: absolute; left: 210px; top: 90px; width: 1500px; height: 900px; background: radial-gradient(ellipse at center, rgba(255,140,70,0.18), rgba(255,100,40,0.05) 45%, transparent 70%); }
    #seg03-sc046-t { position: absolute; left: 0; right: 0; top: 440px; text-align: center; font-size: 190px; }
    #seg03-sc046-t .y { color: var(--yellow); text-shadow: 0 0 1px rgba(255,245,190,0.9), 0 0 7px rgba(255,170,40,0.6), 0 0 20px rgba(255,110,30,0.35), 0 0 46px rgba(255,80,20,0.2); }

    /* ---------- SC047 · 2.5D 1920s campus ---------- */
    #seg03-sc047-stage { position: absolute; inset: 0; perspective: 1200px; perspective-origin: 960px 540px; }
    #seg03-sc047-world { position: absolute; inset: 0; transform-style: preserve-3d; transform-origin: 960px 540px; }
    .seg03-sc047-layer { position: absolute; inset: 0; transform-origin: 960px 540px; }
    .seg03-sc047-layer img { position: absolute; display: block; }
    #seg03-sc047-bd { left: -40px; top: -150px; width: 2000px; height: 1280px; filter: sepia(0.35) brightness(0.62) saturate(0.7) blur(5px); }
    #seg03-sc047-sky { position: absolute; left: -400px; right: -400px; top: -500px; height: 1000px; background: linear-gradient(180deg, rgba(120,52,30,0.5), rgba(120,52,30,0) 100%); mix-blend-mode: soft-light; }
    #seg03-sc047-title { position: absolute; left: 0; right: 0; top: 40px; text-align: center; font-size: 168px; filter: url(#seg03-choke47); white-space: nowrap; }
    #seg03-sc047-tshade { position: absolute; left: -200px; right: -200px; top: -200px; height: 560px; background: radial-gradient(ellipse 50% 50% at 50% 60%, rgba(14,12,10,0.55), rgba(14,12,10,0) 75%); }
    #seg03-sc047-haze { position: absolute; left: -400px; right: -400px; top: -100px; height: 900px; background: radial-gradient(ellipse 60% 45% at 50% 30%, rgba(255,214,170,0.2), rgba(255,214,170,0) 70%); mix-blend-mode: screen; }
    #seg03-sc047-back { left: -40px; top: 40px; width: 2000px; height: 1280px; filter: sepia(0.3) saturate(0.75) contrast(1.06) brightness(0.74); }
    #seg03-sc047-front { left: -40px; top: 620px; width: 2000px; height: 699px; filter: sepia(0.3) saturate(0.75) contrast(1.06) brightness(0.74); }
    #seg03-sc047-ground { position: absolute; left: -300px; right: -300px; bottom: -120px; height: 520px; background: linear-gradient(180deg, rgba(20,19,18,0), rgba(20,19,18,0.92) 70%); }
    #seg03-sc047-rays { position: absolute; left: 400px; top: -300px; width: 1800px; height: 1500px; mix-blend-mode: soft-light; opacity: 0.5;
      background: repeating-conic-gradient(from 200deg at 80% 0%, rgba(255,226,180,0.0) 0deg, rgba(255,226,180,0.55) 2deg, rgba(255,226,180,0.0) 5deg, rgba(255,226,180,0.0) 9deg);
      -webkit-mask-image: radial-gradient(ellipse 70% 80% at 80% 0%, #000 20%, transparent 75%); mask-image: radial-gradient(ellipse 70% 80% at 80% 0%, #000 20%, transparent 75%); filter: blur(6px); }
    #seg03-sc047-another { position: absolute; left: 110px; top: 905px; font-size: 76px; }
    #seg03-sc047-card { position: absolute; left: 1556px; top: 520px; width: 250px; height: 330px; }
    #seg03-sc047-card img { object-position: 50% 18%; }
    #seg03-sc047-where { position: absolute; left: 1490px; top: 878px; font-size: 24px; color: #e8dccb; }

    #seg03-iris { z-index: 5; }
  </style>
  <div id="root" data-composition-id="seg03" data-vo-start="206.27" data-duration="89.96" data-width="1920" data-height="1080">
    <svg id="seg03-defs" width="0" height="0" style="position:absolute"></svg>

    <!-- ================= SC035 · 206.27–214.67 · PAPER · R6 chart ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc035" data-scene="SC035" style="visibility: visible">
      <div id="seg03-sc035-bg" style="background-image:url('assets/archival/modern/stanford_oval_main_quad_aerial_2007.jpg')"></div>
      <div id="seg03-sc035-card">
        <div id="seg03-sc035-ghost" style="background-image:url('assets/derived/seg03/inner_quad_west_2400.jpg')"><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div>
        <div id="seg03-sc035-title" class="t-serif">A <i>revenue</i> generation model</div>
        <div id="seg03-sc035-sub" class="t-serif-i">charging a little bit</div>
        <div class="seg03-sc035-lab t-label" id="seg03-sc035-lb" style="top: 432px">Before</div>
        <div class="seg03-sc035-track" id="seg03-sc035-before"></div>
        <div class="seg03-sc035-lab t-label" id="seg03-sc035-la" style="top: 622px">After</div>
        <div class="seg03-sc035-track" id="seg03-sc035-after"><div id="seg03-sc035-afterfill"></div></div>
        <div id="seg03-sc035-axis0"></div>
        <div id="seg03-sc035-axis"></div>
        <div id="seg03-sc035-end"><span class="label-box" id="seg03-sc035-endt">for classes</span></div>
        <div id="seg03-sc035-src" class="t-label">Stanford University · tuition</div>
        <div class="paper-tex" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>
        <div class="folds"></div>
        <div id="seg03-sc035-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg'); opacity: 0.25"></div>
      </div>
    </div>

    <!-- ================= SC036 · 214.67–225.63 · NIGHT · Founding Grant ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc036" data-scene="SC036">
      <div id="seg03-sc036-bg" style="background-image:url('assets/archival/documents/stanford_founding_grant_1885_heading_page.jpg')"></div>
      <div id="seg03-sc036-cam">
        <div id="seg03-sc036-page">
          <img src="assets/archival/documents/stanford_founding_grant_1885_heading_page.jpg" alt="" />
          <div class="pp" style="background-image:url('assets/textures/grain_01.jpg')"></div>
          <div class="ht" style="background-image:url('assets/textures/halftone_01_norm.jpg')"></div>
          <svg id="seg03-sc036-marks"></svg>
        </div>
      </div>
      <div id="seg03-sc036-dim"></div>
      <div id="seg03-sc036-against" class="t-serif-i halate">against the rule</div>
      <div id="seg03-sc036-trust"><div class="t-display halate" id="seg03-sc036-tr1">the trust</div><div class="t-display halate" id="seg03-sc036-tr2">document</div></div>
      <div id="seg03-sc036-clip"><div id="seg03-sc036-photo"><img src="assets/derived/seg03/leland_stanford_1874_1200.jpg" alt="" /></div></div>
      <div id="seg03-sc036-lower"><div class="a t-serif-i halate" id="seg03-sc036-la">its founder</div><div class="b t-display halate" id="seg03-sc036-lb">Leland Stanford</div></div>
      <div id="seg03-sc036-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_01_norm.jpg')"></div>
      <div id="seg03-sc036-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_02.jpg')"></div>
      <div class="vignette"></div>
    </div>

    <!-- ================= SC037 · 225.63–229.79 · PAPER · strike-through ================= -->
    <div class="seg03-scene seg03-paper" id="seg03-sc037" data-scene="SC037">
      <div id="seg03-sc037-stage">
        <div id="seg03-sc037-seal"><img src="assets/archival/hoover/stanford_memorial_church_c1920_quad1921.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div>
        <div id="seg03-sc037-no" class="t-display">no charge</div>
        <div id="seg03-sc037-for" class="t-serif-i">for students</div>
        <svg id="seg03-sc037-marks"></svg>
      </div>
      <div class="paper-tex" style="background-image:url('assets/textures/paper_cream_02.jpg')"></div>
      <div class="folds"></div>
      <div id="seg03-sc037-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg'); opacity: 0.25"></div>
    </div>

    <!-- ================= SC038 · 229.79–237.32 · NIGHT · shutter chain ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc038" data-scene="SC038">
      <div id="seg03-sc038-weave">
        <div class="seg03-sc038-shot" id="seg03-sc038-sh1"><div class="plate"><img class="img" src="assets/archival/terman/mit_campus_aerial_1925_great_dome.jpg" alt="" /><img class="fringe" src="assets/archival/terman/mit_campus_aerial_1925_great_dome.jpg" alt="" /></div></div>
        <div class="seg03-sc038-shot" id="seg03-sc038-sh2"><div class="plate"><img class="img" src="assets/derived/seg03/harvard_widener_1915_2400.jpg" alt="" /><img class="fringe" src="assets/derived/seg03/harvard_widener_1915_2400.jpg" alt="" /></div></div>
        <div class="seg03-sc038-shot" id="seg03-sc038-sh3"><div class="plate"><img class="img" src="assets/derived/seg03/throop_pasadena_2400.jpg" alt="" /><img class="fringe" src="assets/derived/seg03/throop_pasadena_2400.jpg" alt="" /></div></div>
        <div class="seg03-sc038-shot" id="seg03-sc038-sh4"><div class="plate"><img class="img" src="assets/derived/seg03/main_quad_pano_b_h1200.jpg" alt="" /><img class="fringe" src="assets/derived/seg03/main_quad_pano_b_h1200.jpg" alt="" /></div></div>
      </div>
      <div class="seg03-shade-b"></div>
      <div class="seg03-sc038-lab t-label halate" id="seg03-sc038-lab1">MIT · Cambridge, Mass.</div>
      <div class="seg03-sc038-lab t-label halate" id="seg03-sc038-lab2">Harvard · Cambridge, Mass.</div>
      <div class="seg03-sc038-lab t-label halate" id="seg03-sc038-lab3">Throop (Caltech) · Pasadena</div>
      <div class="seg03-sc038-lab t-label halate" id="seg03-sc038-lab4">Stanford · Main Quad</div>
      <div id="seg03-sc038-comp" class="t-display halate">competitive</div>
      <div id="seg03-sc038-long" class="t-serif-i halate">in the long term</div>
      <div id="seg03-sc038-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_01_norm.jpg')"></div>
      <div id="seg03-sc038-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_01.jpg')"></div>
      <div class="vignette" style="background: radial-gradient(ellipse 72% 68% at 50% 50%, rgba(0,0,0,0) 50%, rgba(8,6,4,0.65) 100%)"></div>
    </div>

    <!-- ================= SC039 · 237.32–244.28 · PAPER · money, choke + highlighter ================= -->
    <div class="seg03-scene seg03-paper" id="seg03-sc039" data-scene="SC039">
      <div id="seg03-sc039-fan">
        <div class="seg03-sc039-note" id="seg03-sc039-n1" style="left: 1180px; top: 170px"><div class="ph"><img src="assets/derived/seg03/gold_cert_1000_1400.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
        <div class="seg03-sc039-note" id="seg03-sc039n2" style="left: 1230px; top: 265px"><div class="ph"><img src="assets/derived/seg03/gold_cert_50_1400.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
        <div class="seg03-sc039-note" id="seg03-sc039-n3" style="left: 1270px; top: 360px"><div class="ph"><img src="assets/derived/seg03/gold_cert_20_1400.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
        <div class="seg03-sc039-note" id="seg03-sc039-n4" style="left: 1200px; top: 470px"><div class="ph"><img src="assets/derived/seg03/gold_cert_100_1400.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
      </div>
      <div id="seg03-sc039-even" class="t-serif-i">even a</div>
      <div id="seg03-sc039-massive" class="t-display">massive amount<span class="l2">of <span class="hl" id="seg03-sc039-hl" style="--hl:0">money</span></span></div>
      <div id="seg03-sc039-hard" class="t-serif-i">very hard to continue</div>
      <div class="paper-tex" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>
      <div class="folds"></div>
      <div id="seg03-sc039-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg'); opacity: 0.25"></div>
    </div>

    <!-- ================= SC040 · 244.28–249.00 · NIGHT · gate weave ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc040" data-scene="SC040">
      <div id="seg03-sc040-weave">
        <div class="plate" id="seg03-sc040-plate"><img class="img" src="assets/archival/hoover/stanford_campus_aerial_c1920_quad1921.jpg" alt="" /><img class="fringe" src="assets/archival/hoover/stanford_campus_aerial_c1920_quad1921.jpg" alt="" /></div>
      </div>
      <div id="seg03-sc040-vig"></div>
      <div id="seg03-sc040-issues" class="t-serif-i halate">issues</div>
      <div id="seg03-sc040-late" class="t-label halate yellow">late 1910s</div>
      <div id="seg03-sc040-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg')"></div>
      <div id="seg03-sc040-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_03.jpg'); opacity: 0.55"></div>
      <div id="seg03-sc040-white"></div>
    </div>

    <!-- ================= SC041 · 249.00–256.20 · PAPER · timeline + card ================= -->
    <div class="seg03-scene seg03-paper" id="seg03-sc041" data-scene="SC041">
      <div id="seg03-sc041-board">
        <div id="seg03-sc041-kick" class="t-label">the second thing</div>
        <svg id="seg03-sc041-lead"><path id="seg03-sc041-leadp" d="M1170 716 L1170 924" stroke="#18222f" stroke-width="2" stroke-dasharray="8 8" fill="none"/></svg>
        <div id="seg03-sc041-card" class="seg03-card"><div class="ph"><img src="assets/archival/hoover/stanford_arcade_c1920_quad1921.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
        <img id="seg03-sc041-pin" src="assets/icons/pin_vermilion_top.svg" alt="" />
        <div id="seg03-sc041-tag" class="seg03-tag t-label">Stanford Business Graduate Program</div>
        <div id="seg03-sc041-pres" class="t-serif-i">right before he becomes president</div>
        <div class="seg03-tl" id="seg03-sc041-tl">
          <div class="seg03-axis" id="seg03-sc041-axis"></div>
          <div id="seg03-sc041-ticks"></div>
          <div class="seg03-gtag t-label" id="seg03-sc041-tuit">tuition</div>
          <div class="seg03-mark" id="seg03-sc041-pmark"></div>
          <div class="seg03-mlab t-label" id="seg03-sc041-plab">president</div>
          <div class="seg03-dot" id="seg03-sc041-dot"></div>
        </div>
      </div>
      <div class="paper-tex" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>
      <div class="folds"></div>
      <div id="seg03-sc041-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg'); opacity: 0.28"></div>
    </div>

    <!-- ================= SC042–SC043 · 256.20–268.52 · NIGHT · map arcs + HERE ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc042" data-scene="SC042">
      <div id="seg03-map-blur">
      <div id="seg03-map-cam">
        <img id="seg03-map-base" src="assets/maps/us_basemap_desat.jpg" alt="" />
        <svg id="seg03-map-fills" class="seg03-map-svg" viewBox="0 0 6400 3200">
          <path d="{{WEST}}" fill="#e5482a" fill-opacity="0.34"/>
          <path d="{{EAST}}" fill="#23415e" fill-opacity="0.5"/>
        </svg>
        <svg id="seg03-map-lines" class="seg03-map-svg" viewBox="0 0 6400 3200">
          <path d="{{STATES}}" fill="none" stroke="#f4eee2" stroke-opacity="0.22" stroke-width="3"/>
          <path d="{{RIVER}}" fill="none" stroke="#a9c8de" stroke-opacity="0.55" stroke-width="7"/>
        </svg>
        <img class="seg03-cshadow" src="assets/maps/clouds/cloud_01_satellite.png" style="left:1620px;top:620px;width:2000px" alt="" />
        <img class="seg03-cloud" src="assets/maps/clouds/cloud_01_satellite.png" style="left:1560px;top:540px;width:2000px" alt="" />
        <img class="seg03-cshadow" src="assets/maps/clouds/cloud_03_satellite.png" style="left:3660px;top:1780px;width:1800px" alt="" />
        <img class="seg03-cloud" src="assets/maps/clouds/cloud_03_satellite.png" style="left:3600px;top:1700px;width:1800px" alt="" />
        <svg id="seg03-map-arcs" class="seg03-map-svg" viewBox="0 0 6400 3200">
          <defs><filter id="seg03-arcglow" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="10"/></filter></defs>
          <g id="seg03-arcs"></g>
          <g id="seg03-pin-stan" transform="translate(586 1456)">
            <circle id="seg03-pin-stan-halo" r="90" fill="none" stroke="#f2d33b" stroke-width="8" opacity="0.6"/>
            <circle r="44" fill="#e5482a" stroke="#f4eee2" stroke-width="10"/>
          </g>
          <g class="seg03-pin-e" id="seg03-pin-mit" transform="translate(5712 990)">
            <circle class="seg03-pin-e-halo" r="70" fill="none" stroke="#f4eee2" stroke-width="7" opacity="0.5"/>
            <circle r="34" fill="#23415e" stroke="#f4eee2" stroke-width="9"/>
          </g>
          <g class="seg03-pin-e" id="seg03-pin-harv" transform="translate(5650 920)">
            <circle class="seg03-pin-e-halo" r="70" fill="none" stroke="#f4eee2" stroke-width="7" opacity="0.5"/>
            <circle r="34" fill="#23415e" stroke="#f4eee2" stroke-width="9"/>
          </g>
          <g id="seg03-dots"></g>
        </svg>
        <div id="seg03-sc042-smart" class="seg03-mlabel t-serif-i halate">smart people</div>
        <div id="seg03-sc042-mit" class="seg03-mlabel t-display halate">MIT</div>
        <div id="seg03-sc042-harv" class="seg03-mlabel t-display halate">Harvard</div>
      </div>
      </div>
      <svg id="seg03-sc043-marks"></svg>
      <div id="seg03-sc043-here" class="t-display halate yellow">HERE</div>
      <div id="seg03-sc043-cal" class="t-label halate">Stanford, Calif.</div>
      <div id="seg03-sc042-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_01.jpg')"></div>
      <div id="seg03-sc042-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_01.jpg')"></div>
      <div class="vignette"></div>
      <div id="seg03-map-credit" class="t-label">Basemap: NASA Blue Marble</div>
    </div>

    <!-- ================= SC044 · 268.52–275.48 · PAPER · then vs now ================= -->
    <div class="seg03-scene seg03-paper" id="seg03-sc044" data-scene="SC044">
      <div id="seg03-sc044-board">
        <div id="seg03-sc044-deal" class="t-serif-i">a big deal</div>
        <div id="seg03-sc044-old" class="seg03-card"><div class="ph"><img src="assets/archival/hoover/stanford_arcade_c1920_quad1921.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
        <img id="seg03-sc044-pin1" src="assets/icons/pin_vermilion_top.svg" alt="" />
        <div id="seg03-sc044-otag" class="seg03-tag t-label">1925</div>
        <div id="seg03-sc044-new" class="seg03-card"><div class="ph"><img src="assets/archival/stanford_gsb/knight_management_center_2011.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png'); opacity: 0.3"></div></div></div>
        <img id="seg03-sc044-pin2" src="assets/icons/pin_vermilion_top.svg" alt="" />
        <div id="seg03-sc044-tag" class="seg03-tag t-label">Stanford Business graduate program</div>
        <div class="seg03-tl" id="seg03-sc044-tl">
          <div class="seg03-axis" id="seg03-sc044-axis"></div>
          <div id="seg03-sc044-ticks"></div>
          <div id="seg03-sc044-dash"></div>
          <div id="seg03-sc044-now" class="t-display">now</div>
          <div class="seg03-dot" id="seg03-sc044-dot"></div>
        </div>
      </div>
      <div class="paper-tex" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>
      <div class="folds"></div>
      <div id="seg03-sc044-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg'); opacity: 0.28"></div>
      <div id="seg03-sc044-credit" class="t-label">Photo: Steve Castillo, CC BY 3.0</div>
    </div>

    <!-- ================= SC045 · 275.48–285.16 · NIGHT · pano + light leak ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc045" data-scene="SC045">
      <div id="seg03-sc045-weave">
        <div id="seg03-sc045-pano"><div class="plate"><img class="img" src="assets/derived/seg03/main_quad_pano_b_h1200.jpg" alt="" /><img class="fringe" src="assets/derived/seg03/main_quad_pano_b_h1200.jpg" alt="" /></div></div>
      </div>
      <div id="seg03-sc045-leak" style="background-image:url('assets/textures/lightleak_01.jpg')"></div>
      <div id="seg03-sc045-shade"></div>
      <div id="seg03-sc045-over" class="t-display halate">overnight</div>
      <svg id="seg03-sc045-marks"></svg>
      <div id="seg03-sc045-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_02_norm.jpg')"></div>
      <div id="seg03-sc045-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_03.jpg'); opacity: 0.5"></div>
      <div class="vignette" style="background: radial-gradient(ellipse 72% 68% at 50% 50%, rgba(0,0,0,0) 50%, rgba(8,6,4,0.7) 100%)"></div>
    </div>

    <!-- ================= SC046 · 285.16–287.56 · NIGHT · streaks title ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc046" data-scene="SC046">
      <canvas id="seg03-sc046-streaks" class="streaks" style="filter: blur(2.5px);"></canvas>
      <div id="seg03-sc046-glow"></div>
      <div id="seg03-sc046-t" class="t-display halate">a <span class="y">good start</span></div>
      <div id="seg03-sc046-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_01.jpg')"></div>
      <div id="seg03-sc046-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_01.jpg')"></div>
      <div class="vignette"></div>
    </div>

    <!-- ================= SC047 · 287.56–296.23 · NIGHT · 2.5D 1920s campus ================= -->
    <div class="seg03-scene seg03-night" id="seg03-sc047" data-scene="SC047">
      <div id="seg03-sc047-stage">
        <div id="seg03-sc047-world">
          <div class="seg03-sc047-layer" id="seg03-sc047-L0"><img id="seg03-sc047-bd" src="assets/archival/stanford_1920s/layers/backdrop.jpg" alt="" /><div id="seg03-sc047-sky"></div></div>
          <div class="seg03-sc047-layer" id="seg03-sc047-L1"><div id="seg03-sc047-tshade"></div><div id="seg03-sc047-title" class="t-display halate">FREDERICK TERMAN</div></div>
          <div class="seg03-sc047-layer" id="seg03-sc047-Lh"><div id="seg03-sc047-haze"></div></div>
          <div class="seg03-sc047-layer" id="seg03-sc047-L2"><img id="seg03-sc047-back" src="assets/derived/seg03/students_back_soft.png" alt="" /></div>
          <div class="seg03-sc047-layer" id="seg03-sc047-L3"><img id="seg03-sc047-front" src="assets/derived/seg03/students_front_soft.png" alt="" /><div id="seg03-sc047-ground"></div></div>
        </div>
      </div>
      <div id="seg03-sc047-rays"></div>
      <div id="seg03-sc047-another" class="t-serif-i halate">another student</div>
      <div id="seg03-sc047-card" class="seg03-card"><div class="ph"><img src="assets/archival/terman/terman_frederick_1920_theta_xi_crop_2x.jpg" alt="" /><div class="ht" style="background-image:url('assets/textures/halftone_03.png')"></div></div></div>
      <div id="seg03-sc047-where" class="seg03-tag t-label">Stanford, 1910s–20s</div>
      <div id="seg03-sc047-grain" class="tx tx-grain" style="background-image:url('assets/textures/grain_01_norm.jpg')"></div>
      <div id="seg03-sc047-dust" class="tx tx-dust" style="background-image:url('assets/textures/dust_03.jpg')"></div>
      <div class="vignette"></div>
    </div>

    <svg id="seg03-iris" class="iris"></svg>
    <audio id="seg03-vo" class="temp-vo" src="vo10.mp3" data-start="0" data-duration="89.96" data-media-start="206.27" data-volume="1"></audio>
  </div>
  <script>
  (function () {
    const SEG = "seg03", SEG_START = 206.27, SEG_END = 296.23, DURATION = +(SEG_END - SEG_START).toFixed(2);
    const T = (s) => +(s - SEG_START).toFixed(3);
    const tl = gsap.timeline({ paused: true });
    const $ = (id) => document.getElementById(id);
    const C = (d, e) => FX.choppy(e || "power3.out", d, 12);
    // run fn with every FX.onFrame it registers gated to [a, b] (local seconds) so idle scenes cost nothing
    const gate = (a, b, fn) => {
      const orig = FX.onFrame;
      FX.onFrame = (f) => orig((t) => { if (t < a - 0.05 || t > b + 0.05) return; f(t); });
      try { return fn(); } finally { FX.onFrame = orig; }
    };
    const scene = (id, a, b, first) => {
      if (!first) tl.set("#" + id, { autoAlpha: 1 }, T(a));
      tl.set("#" + id, { autoAlpha: 0 }, T(b));
    };
    const defs = $("seg03-defs");
    FX.tintDefs(defs, "seg03-tint-ink", "#18222f", "#efe7d5");
    FX.tintDefs(defs, "seg03-tint-night", "#141312", "#6d665b");
    FX.tintDefs(defs, "seg03-tint-warm", "#2a2622", "#f4eee2");
    FX.roughDefs(defs, "seg03-rough", { freq: 0.04, scale: 6 });
    FX.roughDefs(defs, "seg03-roughsm", { freq: 0.05, scale: 5 });
    const choke39 = gate(T(237.32), T(244.28), () => FX.roughDefs(defs, "seg03-choke39", { freq: 0.05, scale: 4, choke: 0 }));
    const choke47 = gate(T(287.56), T(296.23), () => FX.roughDefs(defs, "seg03-choke47", { freq: 0.03, scale: 6, choke: 0 }));
    const iris = FX.iris($("seg03-iris"), { blades: 7, close: 0.15, hold: 2 / 24, open: 0.2 });
    const texture = (sc, seed, a, b, night) => gate(T(a), T(b), () => {
      FX.grain($(`seg03-${sc}-grain`), seed);
      if (night) FX.dust($(`seg03-${sc}-dust`), seed + 1, 2);
    });

    // ===== SC035 · R6 chart: "a revenue generation model" =====
    scene("seg03-sc035", 206.27, 214.67, true);
    texture("sc035", 351, 206.27, 214.67, false);
    // hand-off from seg02: the card finishes its slide in from the right
    tl.fromTo("#seg03-sc035-card", { x: 180 }, { x: 0, duration: 0.3, ease: "power3.out", immediateRender: true }, 0);
    tl.fromTo("#seg03-sc035-bg", { scale: 1.12 }, { scale: 1.16, duration: 0.6, ease: "none" }, 0);
    tl.fromTo("#seg03-sc035-ghost", { x: 40 }, { x: 0, duration: 8.4, ease: "none" }, 0);
    tl.fromTo("#seg03-sc035-axis0", { scaleY: 0 }, { scaleY: 1, duration: 0.4, ease: C(0.4) }, T(206.5));
    tl.fromTo("#seg03-sc035-axis", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: C(0.6) }, T(206.6));
    tl.fromTo("#seg03-sc035-lb, #seg03-sc035-la", { opacity: 0, x: -14 }, { opacity: 1, x: 0, duration: 0.25, stagger: 0.12, ease: C(0.25) }, T(207.0));
    tl.fromTo("#seg03-sc035-before, #seg03-sc035-after", { opacity: 0 }, { opacity: 1, duration: 0.2, stagger: 0.12 }, T(207.1));
    tl.fromTo("#seg03-sc035-src", { opacity: 0 }, { opacity: 1, duration: 0.3 }, T(207.4));
    gsap.set("#seg03-sc035-afterfill", { scaleX: 0 });
    gsap.set("#seg03-sc035-after", { outline: "3px dashed rgba(24,34,47,0.45)" });
    FX.text.rise(tl, [$("seg03-sc035-title")], T(209.23) - 0.06, { y: 18, dur: 0.55, blur: 6 });
    FX.text.rise(tl, [$("seg03-sc035-sub")], T(212.51) - 0.06, { y: 14, dur: 0.5, blur: 6 });
    tl.to("#seg03-sc035-afterfill", { scaleX: 1, duration: 1.3, ease: C(1.3, "power2.out") }, T(212.51) - 0.04);
    tl.fromTo("#seg03-sc035-end", { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(0.25, "back.out(2)") }, T(213.71) - 0.06);
    // fold away (12 fps) to reveal the dark desk of SC036
    tl.to("#seg03-sc035-card", { rotationX: 88, transformPerspective: 2200, opacity: 0.6, duration: 0.3, ease: C(0.3, "power2.in") }, T(214.67) - 0.3);

    // ===== SC036 · the Founding Grant, 1885 =====
    scene("seg03-sc036", 214.67, 225.63);
    texture("sc036", 361, 214.67, 225.63, true);
    const mk36 = gate(T(214.67), T(225.63), () => FX.markupDefs($("seg03-sc036-marks"), "seg03-sc036-rough"));
    $("seg03-sc036-marks").setAttribute("viewBox", "0 0 1920 1080");
    const cam36 = (cx, cy, z, sx) => ({ x: (sx || 960) - cx * z, y: 540 - cy * z, scale: z });
    tl.fromTo("#seg03-sc036-cam", cam36(600, 980, 0.5, 640), Object.assign(cam36(640, 760, 0.62, 660), { duration: 3.3, ease: "sine.inOut" }), T(214.67));
    tl.fromTo("#seg03-sc036-page", { rotationX: 16, rotationY: -10, rotation: -4, transformPerspective: 2600 }, { rotationX: 3, rotationY: -2, rotation: -1.2, duration: 6, ease: "power2.inOut" }, T(214.67));
    tl.to("#seg03-sc036-cam", Object.assign(cam36(670, 650, 0.92, 640), { duration: 1.4, ease: "power3.inOut" }), T(219.4));
    tl.to("#seg03-sc036-cam", Object.assign(cam36(680, 640, 0.98, 620), { duration: 3.6, ease: "none" }), T(220.8));
    tl.fromTo("#seg03-sc036-bg", { x: 0 }, { x: -70, duration: 11, ease: "none" }, T(214.67));
    FX.text.rise(tl, [$("seg03-sc036-against")], T(216.43) - 0.06, { dur: 0.6 });
    FX.text.fill(tl, $("seg03-sc036-tr1"), T(220.19) - 0.06, { per: 0.03, hold: 0.25, settle: 0.45 });
    FX.text.fill(tl, $("seg03-sc036-tr2"), T(220.59) - 0.06, { per: 0.03, hold: 0.25, settle: 0.45 });
    FX.markup.circle(tl, $("seg03-sc036-marks"), T(220.59), { cx: 675, cy: 650, rx: 540, ry: 190, rot: -3, color: "#e5482a", width: 9, filter: mk36, dur: 0.6, seed: 36 });
    tl.to("#seg03-sc036-against, #seg03-sc036-trust", { opacity: 0, duration: 0.3 }, T(223.2));
    tl.fromTo("#seg03-sc036-dim", { opacity: 0.35 }, { opacity: 1, duration: 0.6 }, T(223.1));
    tl.fromTo("#seg03-sc036-clip", { opacity: 0, x: 120, rotation: 8, scale: 1.06 }, { opacity: 1, x: 0, rotation: 2.5, scale: 1, duration: 0.5, ease: C(0.5) }, T(223.5));
    FX.text.rise(tl, [$("seg03-sc036-la")], T(224.19) - 0.06, { dur: 0.5 });
    tl.fromTo("#seg03-sc036-lb", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(224.59) - 0.06);
    FX.text.random(tl, $("seg03-sc036-lb"), T(224.59) - 0.06, { dur: 0.45, seed: 36 });

    // ===== SC037 · "no charge for students" — struck out =====
    scene("seg03-sc037", 225.63, 229.79);
    texture("sc037", 371, 225.63, 229.79, false);
    const mk37 = gate(T(225.63), T(229.79), () => FX.markupDefs($("seg03-sc037-marks"), "seg03-sc037-rough"));
    tl.fromTo("#seg03-sc037-stage", { scale: 1.0 }, { scale: 1.04, duration: 4.2, ease: "none" }, T(225.63));
    tl.fromTo("#seg03-sc037-seal", { opacity: 0, rotation: -14, scale: 0.8 }, { opacity: 1, rotation: -6, scale: 1, duration: 0.35, ease: C(0.35, "back.out(2)") }, T(225.75));
    tl.fromTo("#seg03-sc037-no", { opacity: 0, scale: 0.92 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(0.25, "back.out(2)") }, T(226.67) - 0.06);
    FX.text.rise(tl, [$("seg03-sc037-for")], T(227.47) - 0.06, { dur: 0.5, blur: 6 });
    FX.markup.underline(tl, $("seg03-sc037-marks"), T(228.43) - 0.04, { x1: 450, x2: 1480, y: 450, color: "#e5482a", width: 18, filter: mk37, dur: 0.3 });
    FX.markup.underline(tl, $("seg03-sc037-marks"), T(228.43) + 0.22, { x1: 470, x2: 1460, y: 478, color: "#e5482a", width: 12, filter: mk37, dur: 0.25 });
    iris.at(tl, T(229.79));

    // ===== SC038 · rival campuses, shutter chain =====
    scene("seg03-sc038", 229.79, 237.32);
    texture("sc038", 381, 229.79, 237.32, true);
    gate(T(229.79), T(237.32), () => FX.weave($("seg03-sc038-weave"), { amp: 1.4, flicker: 0.03, seed: 38 }));
    const cuts38 = [229.79, 231.25, 233.75, 235.6, 237.32];
    for (let k = 1; k <= 4; k++) {
      const a = cuts38[k - 1], b = cuts38[k];
      tl.set(`#seg03-sc038-sh${k}, #seg03-sc038-lab${k}`, { autoAlpha: 1 }, T(a));
      if (k < 4) tl.set(`#seg03-sc038-sh${k}, #seg03-sc038-lab${k}`, { autoAlpha: 0 }, T(b));
      tl.fromTo(`#seg03-sc038-sh${k} .plate`, { scale: 1.0 }, { scale: 1.08, duration: b - a + 0.3, ease: "none" }, T(a));
      tl.fromTo(`#seg03-sc038-lab${k}`, { y: 10, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }, T(a) + 0.12);
      if (k > 1) iris.at(tl, T(a));
    }
    tl.fromTo("#seg03-sc038-sh4 .img, #seg03-sc038-sh4 .fringe", { objectPosition: "0% 50%" }, { objectPosition: "40% 50%", duration: 1.8, ease: "none" }, T(235.6));
    FX.text.rise(tl, [$("seg03-sc038-comp")], T(232.19) - 0.06, { dur: 0.6 });
    FX.text.rise(tl, [$("seg03-sc038-long")], T(233.31) - 0.06, { dur: 0.6 });

    // ===== SC039 · "a massive amount of money" =====
    scene("seg03-sc039", 237.32, 244.28);
    texture("sc039", 391, 237.32, 244.28, false);
    const notes = ["#seg03-sc039-n1", "#seg03-sc039n2", "#seg03-sc039-n3", "#seg03-sc039-n4"];
    const rot0 = [-13, -5, 6, -2];
    notes.forEach((n, i) => {
      tl.fromTo(n, { opacity: 0, y: -90, rotation: rot0[i] - 8 }, { opacity: 1, y: 0, rotation: rot0[i], duration: 0.4, ease: C(0.4) }, T(237.4) + i * 0.22);
      // slow fan-out: each note slides apart at its own speed (12 fps)
      tl.to(n, { x: (i - 1.5) * 34, y: (i - 1.5) * 16, rotation: rot0[i] + (i - 1.5) * 2.5, duration: 4.8, ease: C(4.8, "sine.inOut") }, T(238.4));
      // money drains off the right edge
      tl.to(n, { x: 1400, rotation: rot0[i] + 14, duration: 0.55, ease: C(0.55, "power2.in") }, T(243.24) + (3 - i) * 0.16);
    });
    FX.text.rise(tl, [$("seg03-sc039-even")], T(240.52) - 0.06, { dur: 0.45, blur: 6 });
    tl.fromTo("#seg03-sc039-massive", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: true }, T(241.08) - 0.06);
    FX.choke(tl, choke39, T(241.08) - 0.06, 12, 0.5);
    const hl39 = { v: 0 };
    tl.fromTo(hl39, { v: 0 }, { v: 1, duration: 0.4, ease: C(0.4, "power2.inOut"), immediateRender: false, onUpdate: () => $("seg03-sc039-hl").style.setProperty("--hl", hl39.v) }, T(241.88) - 0.04);
    FX.text.rise(tl, [$("seg03-sc039-hard")], T(243.00) - 0.06, { dur: 0.45, blur: 6 });

    // ===== SC040 · 1910s campus, weave + flicker =====
    scene("seg03-sc040", 244.28, 249.00);
    texture("sc040", 401, 244.28, 249.00, true);
    gate(T(244.28), T(249.0), () => FX.weave($("seg03-sc040-weave"), { amp: 1.9, flicker: 0.06, seed: 40 }));
    tl.fromTo("#seg03-sc040-plate", { scale: 1.02 }, { scale: 1.09, duration: 4.8, ease: "none" }, T(244.28));
    tl.fromTo("#seg03-sc040-vig", { scale: 1.25 }, { scale: 0.92, duration: 4.7, ease: "sine.in" }, T(244.28));
    FX.text.rise(tl, [$("seg03-sc040-issues")], T(245.08) - 0.06, { dur: 0.6 });
    tl.fromTo("#seg03-sc040-late", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(248.12) - 0.06);
    FX.text.random(tl, $("seg03-sc040-late"), T(248.12) - 0.06, { dur: 0.4, seed: 40 });
    tl.fromTo("#seg03-sc040-white", { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: false }, T(249.0) - 3 / 24);

    // ===== SC041 · timeline: the business graduate program =====
    scene("seg03-sc041", 249.00, 256.20);
    texture("sc041", 411, 249.0, 256.2, false);
    const X = (yr) => ((yr - 1913) / 19) * 1600;   // shared Stanford axis: 1913..1932 across 1600 px
    const ticks = (host) => [1915, 1920, 1925, 1930].forEach((y) =>
      $(host).insertAdjacentHTML("beforeend", `<div class="seg03-tick" style="left:${X(y)}px"></div><div class="seg03-yr t-label" style="left:${X(y)}px">${y}</div>`));
    ticks("seg03-sc041-ticks");
    gsap.set("#seg03-sc041-tuit", { left: X(1920) });
    gsap.set("#seg03-sc041-pmark, #seg03-sc041-plab", { left: X(1929) });
    tl.fromTo("#seg03-sc041-board", { scale: 1.0 }, { scale: 1.03, duration: 7, ease: "none" }, T(249.0));
    tl.fromTo("#seg03-sc041-axis", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: C(0.6) }, T(249.0));
    tl.fromTo("#seg03-sc041-ticks > *", { opacity: 0 }, { opacity: 1, duration: 0.01, stagger: 0.06 }, T(249.1));
    tl.fromTo("#seg03-sc041-dot", { x: X(1915), scale: 0 }, { x: X(1915), scale: 1, duration: 0.3, ease: "back.out(3)" }, T(249.3));
    tl.fromTo("#seg03-sc041-kick", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(249.88) - 0.06);
    FX.text.random(tl, $("seg03-sc041-kick"), T(249.88) - 0.06, { dur: 0.4, seed: 41 });
    tl.to("#seg03-sc041-dot", { x: X(1920), duration: 0.5, ease: C(0.5, "power2.inOut") }, T(250.2));
    tl.fromTo("#seg03-sc041-tuit", { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.25, ease: C(0.25) }, T(250.5));
    FX.text.rise(tl, [$("seg03-sc041-pres")], T(250.76) - 0.06, { dur: 0.5, blur: 6 });
    tl.fromTo("#seg03-sc041-pmark", { scaleY: 0 }, { scaleY: 1, duration: 0.25, ease: C(0.25, "back.out(2)") }, T(251.64) - 0.06);
    tl.fromTo("#seg03-sc041-plab", { opacity: 0 }, { opacity: 1, duration: 0.2 }, T(251.64) - 0.06);
    tl.to("#seg03-sc041-dot", { x: X(1925), duration: 0.9, ease: C(0.9, "power2.inOut") }, T(252.9));
    tl.to("#seg03-sc041-pres", { opacity: 0, duration: 0.3 }, T(253.4));
    tl.fromTo("#seg03-sc041-card", { opacity: 0, y: -70, rotation: 7 }, { opacity: 1, y: 0, rotation: -2, duration: 0.45, ease: C(0.45) }, T(253.3));
    tl.fromTo("#seg03-sc041-pin", { opacity: 0, scale: 1.8, y: -30 }, { opacity: 1, scale: 1, y: 0, duration: 0.2, ease: C(0.2) }, T(253.72));
    tl.fromTo("#seg03-sc041-leadp", { opacity: 0 }, { opacity: 1, duration: 0.2 }, T(253.8));
    tl.fromTo("#seg03-sc041-tag", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(253.88) - 0.06);
    const w41 = FX.split($("seg03-sc041-tag"), "words").filter((w) => w.textContent.trim());
    [253.88, 254.52, 254.92, 255.56].forEach((t, i) =>
      tl.fromTo(w41[i], { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 1 / 12, ease: "none", immediateRender: true }, T(t) - 0.06));
    tl.to("#seg03-sc041-board", { x: -520, duration: 0.3, ease: C(0.3, "power2.in") }, T(256.2) - 0.3);

    // ===== SC042 · map: smart people leave for MIT / Harvard =====
    scene("seg03-sc042", 256.20, 268.52);
    texture("sc042", 421, 256.2, 268.52, true);
    const camM = (cx, cy, z) => ({ x: 960 - cx * z, y: 540 - cy * z, scale: z });
    const STAN = [586, 1456];
    const NS = "http://www.w3.org/2000/svg";
    const arcs = [
      { to: [5712, 990], cy: 260 }, { to: [5650, 920], cy: 520 }, { to: [5712, 990], cy: 760 },
    ].map((a, i) => {
      const d = `M${STAN[0]} ${STAN[1]} Q${(STAN[0] + a.to[0]) / 2} ${a.cy} ${a.to[0]} ${a.to[1]}`;
      const g = document.createElementNS(NS, "path");
      g.setAttribute("d", d); g.setAttribute("fill", "none"); g.setAttribute("stroke", "#f4eee2"); g.setAttribute("stroke-opacity", "0.35"); g.setAttribute("stroke-width", "26"); g.setAttribute("filter", "url(#seg03-arcglow)");
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d); p.setAttribute("fill", "none"); p.setAttribute("stroke", "#f4eee2"); p.setAttribute("stroke-width", "8"); p.setAttribute("stroke-dasharray", "4 18"); p.setAttribute("stroke-linecap", "round");
      $("seg03-arcs").appendChild(g); $("seg03-arcs").appendChild(p);
      const len = p.getTotalLength();
      const dot = document.createElementNS(NS, "g");
      dot.innerHTML = `<circle r="46" fill="#f4eee2" opacity="0.25"/><circle r="22" fill="#f4eee2" stroke="#141312" stroke-width="5"/>`;
      $("seg03-dots").appendChild(dot);
      g.setAttribute("stroke-dasharray", `${len} ${len}`);
      return { g, p, len, dot, prog: { v: 0 } };
    });
    const drawArc = (a) => {
      const L = a.len * a.prog.v;
      a.g.setAttribute("stroke-dashoffset", (a.len - L).toFixed(1));
      a.p.style.opacity = a.prog.v > 0.001 ? 1 : 0;
      // dotted line only behind the travelling dot: the dash pattern ends in a long gap
      a.p.setAttribute("stroke-dasharray", a.prog.v >= 0.999 ? "4 18" : buildDash(L));
      const pt = a.p.getPointAtLength(Math.max(0, Math.min(a.len, L)));
      a.dot.setAttribute("transform", `translate(${pt.x.toFixed(1)} ${pt.y.toFixed(1)})`);
      a.dot.style.opacity = a.prog.v > 0.001 && a.prog.v < 0.999 ? 1 : 0;
    };
    function buildDash(L) {
      const n = Math.max(0, Math.floor(L / 22));
      const parts = [];
      for (let k = 0; k < n; k++) parts.push(4, 18);
      parts.push(0, 99999);
      return parts.join(" ");
    }
    arcs.forEach(drawArc);
    gsap.set("#seg03-map-cam", camM(1920, 1420, 0.5));
    tl.fromTo("#seg03-map-cam", camM(1920, 1420, 0.5), Object.assign(camM(1800, 1440, 0.54), { duration: 4.3, ease: "none" }), T(256.2));
    tl.to("#seg03-map-cam", Object.assign(camM(3150, 1600, 0.34), { duration: 1.3, ease: "power2.inOut" }), T(260.6));
    tl.to("#seg03-map-cam", Object.assign(camM(4480, 1110, 0.5), { duration: 1.3, ease: "power2.inOut" }), T(261.95));
    tl.to("#seg03-map-cam", Object.assign(camM(4420, 1120, 0.52), { duration: 2.5, ease: "none" }), T(263.25));
    tl.fromTo(".seg03-cloud, .seg03-cshadow", { x: 0 }, { x: 300, duration: 12.4, ease: "none" }, T(256.2));
    tl.fromTo("#seg03-pin-stan-halo", { scale: 1, opacity: 0.7, transformOrigin: "50% 50%" }, { scale: 2.4, opacity: 0, duration: 1.2, repeat: 2, ease: "power2.out" }, T(256.4));
    FX.text.rise(tl, [$("seg03-sc042-smart")], T(260.84) - 0.06, { dur: 0.5, y: 40 });
    tl.to("#seg03-sc042-smart", { opacity: 0, duration: 0.3 }, T(262.0));
    arcs.forEach((a, i) => {
      tl.fromTo(a.prog, { v: 0 }, { v: 1, duration: 1.5, ease: C(1.5, "power1.inOut"), immediateRender: false, onUpdate: () => drawArc(a) }, T(260.84) + i * 0.18);
    });
    tl.fromTo("#seg03-pin-mit", { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.3, ease: "back.out(2.4)" }, T(262.20) - 0.06);
    tl.fromTo("#seg03-pin-harv", { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.3, ease: "back.out(2.4)" }, T(263.32) - 0.06);
    tl.fromTo("#seg03-pin-mit .seg03-pin-e-halo", { scale: 0.6, opacity: 0.7, transformOrigin: "50% 50%" }, { scale: 1.8, opacity: 0, duration: 1.0, ease: "power2.out" }, T(262.20));
    tl.fromTo("#seg03-pin-harv .seg03-pin-e-halo", { scale: 0.6, opacity: 0.7, transformOrigin: "50% 50%" }, { scale: 1.8, opacity: 0, duration: 1.0, ease: "power2.out" }, T(263.32));
    tl.fromTo("#seg03-sc042-mit", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.25, ease: C(0.25) }, T(262.20) - 0.06);
    tl.fromTo("#seg03-sc042-harv", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.25, ease: C(0.25) }, T(263.32) - 0.06);
    // whip back west (12 fps) — the dots fly home along their arcs
    tl.to("#seg03-sc042-mit, #seg03-sc042-harv", { opacity: 0, duration: 0.2 }, T(265.7));
    tl.to("#seg03-map-cam", Object.assign(camM(1129, 1456, 0.85), { duration: 0.7, ease: C(0.7, "expo.inOut") }), T(265.8));
    tl.fromTo("#seg03-map-blur", { filter: "blur(0px)" }, { filter: "blur(6px)", duration: 0.25, yoyo: true, repeat: 1, ease: "none", immediateRender: false }, T(265.9));
    arcs.forEach((a, i) => {
      tl.fromTo(a.prog, { v: 1 }, { v: 0, duration: 0.9, ease: C(0.9, "power2.inOut"), immediateRender: false, onUpdate: () => drawArc(a) }, T(265.75) + i * 0.08);
    });

    // ===== SC043 · "...something similar HERE" =====
    // (same scene container as SC042 — one continuous map camera; SC043 window 266.12–268.52)
    const mk43 = gate(T(266.12), T(268.52), () => FX.markupDefs($("seg03-sc043-marks"), "seg03-sc043-rough"));
    tl.to("#seg03-map-cam", Object.assign(camM(1129, 1456, 0.87), { duration: 2.0, ease: "none" }), T(266.5));
    FX.markup.circle(tl, $("seg03-sc043-marks"), T(267.4), { cx: 498, cy: 540, rx: 115, ry: 100, rot: -8, color: "#e5482a", width: 9, filter: mk43, dur: 0.45, seed: 43 });
    FX.markup.arrow(tl, $("seg03-sc043-marks"), T(267.6), { x1: 810, y1: 470, x2: 640, y2: 520, bend: -40, color: "#f4eee2", width: 7, head: 28, filter: mk43, dur: 0.3 });
    tl.fromTo("#seg03-sc043-here", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(267.96) - 0.06);
    FX.text.fill(tl, $("seg03-sc043-here"), T(267.96) - 0.06, { per: 0.04, hold: 0.25, settle: 0.3, hot: "#f4eee2", cool: "#f2d33b" });
    tl.fromTo("#seg03-sc043-cal", { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.25 }, T(268.1));
    tl.fromTo("#seg03-pin-stan-halo", { scale: 1, opacity: 0.9 }, { scale: 3, opacity: 0, duration: 0.5, ease: "power2.out", immediateRender: false }, T(267.9));

    // ===== SC044 · then vs now =====
    scene("seg03-sc044", 268.52, 275.48);
    texture("sc044", 441, 268.52, 275.48, false);
    const X44 = (yr) => ((yr - 1913) / 19) * 760;   // the 1913–32 axis compressed to the left; dashed run to "now"
    [1915, 1920, 1925, 1930].forEach((y) =>
      $("seg03-sc044-ticks").insertAdjacentHTML("beforeend", `<div class="seg03-tick" style="left:${X44(y)}px"></div><div class="seg03-yr t-label" style="left:${X44(y)}px">${y}</div>`));
    gsap.set("#seg03-sc044-axis", { right: 1600 - X44(1932) });
    gsap.set("#seg03-sc044-dash", { left: X44(1932), width: 1560 - X44(1932) });
    gsap.set("#seg03-sc044-now", { left: 1560 });
    tl.fromTo("#seg03-sc044-board", { y: 140, scale: 1.0 }, { y: 0, scale: 1.0, duration: 0.35, ease: C(0.35) }, T(268.52));
    tl.to("#seg03-sc044-board", { scale: 1.03, duration: 6.6, ease: "none" }, T(268.9));
    tl.fromTo("#seg03-sc044-old", { opacity: 0, x: -60, rotation: -8 }, { opacity: 1, x: 0, rotation: -3, duration: 0.4, ease: C(0.4) }, T(268.6));
    tl.fromTo("#seg03-sc044-pin1", { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.2, ease: C(0.2) }, T(268.95));
    tl.fromTo("#seg03-sc044-otag", { opacity: 0 }, { opacity: 1, duration: 0.2 }, T(269.05));
    tl.fromTo("#seg03-sc044-dot", { x: X44(1925), scale: 0 }, { x: X44(1925), scale: 1, duration: 0.3, ease: "back.out(3)" }, T(269.0));
    tl.fromTo("#seg03-sc044-new", { opacity: 0, x: 120, rotation: 9 }, { opacity: 1, x: 0, rotation: 2, duration: 0.45, ease: C(0.45) }, T(269.4));
    tl.fromTo("#seg03-sc044-pin2", { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.2, ease: C(0.2) }, T(269.8));
    tl.fromTo("#seg03-sc044-credit", { opacity: 0 }, { opacity: 1, duration: 0.3 }, T(269.5));
    FX.text.rise(tl, [$("seg03-sc044-deal")], T(271.08) - 0.06, { dur: 0.5, blur: 6 });
    tl.fromTo("#seg03-sc044-dash", { scaleX: 0 }, { scaleX: 1, duration: 2.1, ease: C(2.1, "power2.inOut") }, T(272.76));
    tl.to("#seg03-sc044-dot", { x: 1560, duration: 2.1, ease: C(2.1, "power2.inOut") }, T(272.76));
    tl.fromTo("#seg03-sc044-tag", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(272.76) - 0.06);
    const w44 = FX.split($("seg03-sc044-tag"), "words").filter((w) => w.textContent.trim());
    [272.76, 273.32, 274.12, 274.60].forEach((t, i) =>
      tl.fromTo(w44[i], { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 1 / 12, ease: "none", immediateRender: true }, T(t) - 0.06));
    tl.fromTo("#seg03-sc044-now", { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.25, ease: C(0.25, "back.out(2)") }, T(275.00) - 0.06);

    // ===== SC045 · "not overnight" — Main Quad pano, light leak, weave =====
    scene("seg03-sc045", 275.48, 285.16);
    texture("sc045", 451, 275.48, 285.16, true);
    gate(T(275.48), T(285.16), () => FX.weave($("seg03-sc045-weave"), { amp: 1.6, flicker: 0.04, seed: 45 }));
    const mk45 = gate(T(275.48), T(285.16), () => FX.markupDefs($("seg03-sc045-marks"), "seg03-sc045-rough"));
    tl.fromTo("#seg03-sc045-pano", { x: -200 }, { x: -1500, duration: 9.68, ease: "sine.inOut" }, T(275.48));
    tl.fromTo("#seg03-sc045-leak", { opacity: 0, x: -900 }, { opacity: 0.55, x: 200, duration: 6.5, ease: "sine.inOut" }, T(275.6));
    tl.to("#seg03-sc045-leak", { opacity: 0.25, x: 700, duration: 2.4, ease: "sine.inOut" }, T(282.1));
    tl.to("#seg03-sc045-leak", { opacity: 1, scale: 1.4, duration: 0.65, ease: "power2.in" }, T(284.5));
    tl.fromTo("#seg03-sc045-over", { opacity: 0 }, { opacity: 1, duration: 0.01 }, T(277.40) - 0.06);
    FX.text.random(tl, $("seg03-sc045-over"), T(277.40) - 0.06, { dur: 0.5, seed: 45 });
    FX.markup.underline(tl, $("seg03-sc045-marks"), T(280.92) - 0.04, { x1: 470, x2: 1450, y: 500, color: "#e5482a", width: 16, filter: mk45, dur: 0.35 });
    tl.to("#seg03-sc045-over", { opacity: 0.55, duration: 0.4 }, T(281.4));

    // ===== SC046 · "a good start" — streaks =====
    scene("seg03-sc046", 285.16, 287.95);
    texture("sc046", 461, 285.16, 287.95, true);
    gate(T(285.16), T(287.95), () => FX.streaks($("seg03-sc046-streaks"), { seed: 46, speed: 0.6, xfreq: 0.15, lo: 0.45, hi: 0.88, gamma: 2.3, tint: [255, 206, 160], gain: 1.2 }));
    tl.fromTo("#seg03-sc046-streaks", { opacity: 0.9 }, { opacity: 0.65, duration: 1.2, ease: "power2.out" }, T(285.16));
    tl.fromTo("#seg03-sc046-glow", { opacity: 0.4, scale: 0.9 }, { opacity: 1, scale: 1.05, duration: 2.4, ease: "sine.inOut" }, T(285.16));
    FX.text.rise(tl, [$("seg03-sc046-t")], T(286.76) - 0.06, { dur: 0.55, y: 20 });
    tl.to("#seg03-sc046-streaks, #seg03-sc046-glow", { opacity: 0.15, duration: 0.5, ease: "power2.in" }, T(287.4));

    // ===== SC047 · 2.5D 1920s campus · FREDERICK TERMAN =====
    scene("seg03-sc047", 287.56, 296.23);
    texture("sc047", 471, 287.56, 296.23, true);
    const P = 1200;
    [["#seg03-sc047-L0", -700], ["#seg03-sc047-L1", -300], ["#seg03-sc047-Lh", -150], ["#seg03-sc047-L2", 0], ["#seg03-sc047-L3", 220]].forEach(([sel, z]) =>
      gsap.set(sel, { z, scale: (P - z) / P }));
    // dissolve in from the streaks, then a slow dolly: push <= 1.14x on the subject layers, lateral parallax ~30 px
    tl.fromTo("#seg03-sc047", { opacity: 0 }, { opacity: 1, duration: 0.4, ease: "power1.inOut" }, T(287.56));
    tl.fromTo("#seg03-sc047-world", { x: 24, z: 0, rotationY: -0.8 }, { x: -24, z: 120, rotationY: 0.8, duration: 8.67, ease: "sine.inOut" }, T(287.56));
    tl.fromTo("#seg03-sc047-rays", { opacity: 0.3, x: 0 }, { opacity: 0.55, x: -60, duration: 8.67, ease: "none" }, T(287.56));
    FX.text.rise(tl, [$("seg03-sc047-another")], T(289.56) - 0.06, { dur: 0.6 });
    tl.to("#seg03-sc047-another", { opacity: 0, duration: 0.4 }, T(293.6));
    tl.fromTo("#seg03-sc047-title", { opacity: 0, y: 70 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, T(294.60) - 0.06);
    FX.choke(tl, choke47, T(294.60) - 0.06, 16, 0.6);
    tl.fromTo("#seg03-sc047-card", { opacity: 0, y: 60, rotation: 9, scale: 1.1 }, { opacity: 1, y: 0, rotation: 3, scale: 1, duration: 0.4, ease: C(0.4) }, T(295.32) - 0.12);
    tl.fromTo("#seg03-sc047-where", { opacity: 0, x: 16 }, { opacity: 1, x: 0, duration: 0.25, ease: C(0.25) }, T(295.32) - 0.06);

    FX.mount(tl, DURATION);
    window.__timelines = window.__timelines || {};
    window.__timelines[SEG] = tl;
  })();
  </script>
</template>
</body>
</html>
