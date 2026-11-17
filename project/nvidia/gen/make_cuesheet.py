#!/usr/bin/env python3
"""Writes project/nvidia/music_cuesheet.json — the sound designer's cue sheet for "NVIDIA" (Is the chip ban actually working?),
master seconds 0–2402.0 (VO 2400.62 s + 1.4 s designed tail). Edit the tables here and re-run
(python3 project/nvidia/gen/make_cuesheet.py), then rebuild the beds (SOUND_PLAN.md §6).
offset = read position inside the Epidemic file at the layer's start, chosen so a track's own builds / peaks / drops
(assets/audio/epidemic/ANALYSIS.md, quoted in SOUND_PLAN.md §1) land on the words named in the notes (script_clean.txt times).
Key family: C minor (+ its relative Eb major) — every track measured C minor on the WAVs (r 0.64–0.87).
Glue drone: Flute (Daniella Ljungsberg), bass + instruments — pulse 1.1 / 1.4 (tempo-free), stems sum to the full mix (−78 dB).
BINDING limits (MANUAL §0, §10.8 "Music limits", Krish 2026-11-13) are hard settings at the bottom: bed_lu_under_vo 22, vo_duck
gap 20 / gap_fast 18 / ceiling 20, pause_lift_db 0. Never set them looser."""
import json, os

# per-act balance trims (dB on every layer of the act) from act_levels.py: aim −20…−24 LU re the VO while he speaks
TRIM = {}

DR = "flute"   # C-minor drone; its bass stem carries it (instruments stem is a faint flute air 14 LU under)


def L(cue, track, stem, start, end, offset, rel, fi=1.5, fo=1.5, auto=None, note="", file=None):
    rel = round(rel + TRIM.get(cue, 0.0), 2)
    d = dict(cue=cue, track=track, stem=stem, start=start, end=end, offset=round(offset, 3), rel_lu=rel,
             fade_in=fi, fade_out=fo)
    if auto: d["auto"] = auto
    if note: d["note"] = note
    if file: d["file"] = file
    return d


def glue(cue, start, end, offset, rel=-20.0, fi=3.0, fo=4.0, note="glue under the join"):
    return L(cue, DR, "bass", start, end, offset, rel, fi, fo, note=note)


LEN = 2402.0

layers = [
    # ================= N1 cold open (nvs01 0–109.4): the question → the CEO news → HK mall → Shenzhen → servers → caveat → Megaspeed
    L("N1", "seventy_seven_cycles", "instruments", 0.0, 115.5, 0.0, -16, 2.0, 3.0,
      auto=[[0, 0], [36, 0], [38.7, 0], [82, 0], [83.5, -2], [90, -2], [91, 0]],
      note="cold electronic pulse from frame 1 (file steady 0–54) under 'Is the chip ban actually working?' 0.16 and the CEO news; "
           "its 54–67 peak = 'a short ferry ride…Shenzhen' 54.96 → 'the biggest electronics market on the planet' 59.85 → 'a room "
           "full of NVIDIA GPUs' 63.5; thinner on 'Now, there is a caveat' 82.4; its 99–107 drop + 107–118 quiet = 'other "
           "companies in Singapore, in Malaysia' 101.8 → 'So if the chips are already making their way into China' 109.37"),
    L("N1", "seventy_seven_cycles", "melody", 0.0, 108.0, 0.0, -19, 2.0, 2.5,
      auto=[[0, -3], [38, -3], [40.6, 0], [82, 0], [83.5, -3], [108, -3]],
      note="melody low under the sensitive CEO lines (11–25), up on 'If you walked into a shopping mall in Hong Kong' 40.64"),
    L("N1", "seventy_seven_cycles", "bass", 38.7, 107.0, 38.7, -21, 1.5, 2.0,
      note="bass enters on 'Take a look at this video' 38.72 (the footage); out with the file's drop"),
    glue("N1", 100.0, 124.0, 30.0, -21, note="glue under the 77 Cycles → Unsolved Issues join"),
    # ================= N2 intro question (nvs02 109.4–162.3): 60 % / 17 % → catching up → 'Was the chip ban a mistake?'
    L("N2", "unsolved_issues", "instruments", 112.0, 163.0, 95.5, -17, 2.5, 3.0,
      note="dark contemporary classical: steady under 'the NVIDIA CEO…60% of all the world's chips' 115.6 / '17%' 127.2; its "
           "126–129 build + 129–133 peak land on 'raises an important question' 142.0 → 'Was the chip ban a mistake?' 146.36–148.28 "
           "(stinger); its 133–140 drop = 'why do we still have it?' 148.3; steady tail under the plan of the video → out at 162.3"),
    L("N2", "unsolved_issues", "melody", 127.0, 158.0, 110.5, -19.5, 2.0, 3.0, note="the question's melody, 'Before the ban…17%' → 'mistake?'"),
    L("N2", "unsolved_issues", "bass", 135.0, 160.0, 118.5, -22, 2.0, 2.5),
    glue("N2", 152.0, 176.0, 60.0, -21, note="glue into the overview ('let me just quickly give you an overview' 162.28)"),
    # ================= N3 what the ban is (nvs02 162.3–229.5): a US law → machines → October 7th 2022 → Biden/Trump → back and forth
    L("N3", "cinema_neon", "full", 162.6, 229.6, 0.0, -19, 2.5, 1.5,
      auto=[[162.6, 0], [204, 0], [205.5, -2], [228, -2]],
      note="Washington-paperwork colour (contemporary classical, dreamy/mysterious; full mix — its stems are 10–17 LU under it): "
           "quiet entry 0–8 under 'Chip ban is basically a US law' 167.9; 'October 7th…Not that October 7th' 185.6–188; thinner "
           "under the dense extended / rolled back passage 205–229; out on 'is this ban even fair?' 229.6"),
    glue("N3", 222.0, 246.0, 90.0, -21),
    # ================= N4 is it fair? (nvs03 229.6–314.5): free trade → no right to buy → China banned Google… → IP theft, WTO
    L("N4", "the_investigator", "instruments", 231.0, 314.5, 44.0, -16.5, 2.0, 2.5,
      auto=[[231, 0], [238, 0], [240, -1.5], [250, -1.5], [251, 0]],
      note="'mysterious / classical crossover' investigation colour (stems sum to the full: −20.6 dB): quiet 44–54 entry under "
           "'some of you guys may be wondering'; its 54–57 build on 'this is where we have to talk about the fair part' 243.4; "
           "steady 57–110 under 'China itself has already banned…Google, Facebook, YouTube' 271.2 → partnerships 283 → IP theft "
           "296.2 → Germany, the UK, France, WTO 303.4; fades on 'let's go even deeper' 314.5"),
    L("N4", "the_investigator", "bass", 244.0, 314.5, 57.0, -20, 2.0, 2.5),
    L("N4", "the_investigator", "melody", 266.0, 312.0, 79.0, -20, 2.0, 2.5, note="melody from 'But for our argument, let's go deeper' 271.2"),
    glue("N4", 306.0, 330.0, 120.0, -20),
    # ================= N5 uranium (nvs03 314.5–362.4): chips like uranium → bomb → enriched uranium → AI → Taiwan → 'the main question'
    L("N5", "subconscious", "full", 316.0, 352.5, 195.0, -20, 3.0, 2.5,
      note="the dark dual-use weight (full mix; stems ≈ 10 LU under it): its 211 s peak arrives under 'like create a nuclear bomb' "
           "325 → 'enriched uranium is heavily controlled' 329.5 → AI 335–339 → 'invading a US ally, Taiwan' 343.9–351; out before "
           "'that's not the main question' 357.1 — drone only for 'is that ban working or not' 358.9"),
    glue("N5", 345.0, 378.0, 150.0, -19.5, note="the breath before the scoreboard: drone alone 352.5–363"),
    # ================= N6 the scoreboard + design (nvs04 362.4–472.7): define 'working' → top three → scoreboard → 4th row blank → design IP → American law
    L("N6", "gnomon", "instruments", 363.0, 472.6, 0.0, -17, 2.5, 0.4,
      note="cold mysterious pulse (drums stem not used — Gnomon's full is drum-led): quiet 0–12 under 'what working actually means'; "
           "steady 12–73 under the top three answers → 'this scoreboard' 386.1 → 'a fourth row…empty' 391 → 'Let's get started' 405.7 "
           "→ 'NVIDIA doesn't actually make the chips…made in Taiwan' 406.6–417.6; its 73–88 drop/quiet = 'designs of chips' 422–441; "
           "88–95 build → 95–119 peak = 'In fact, according to one former official…every chip on the planet is under American law' "
           "462.7–469.2; cut on 'let's look at job number one' 472.75"),
    L("N6", "gnomon", "melody", 375.0, 472.6, 12.0, -18.5, 2.0, 0.4),
    L("N6", "gnomon", "bass", 451.0, 472.6, 88.0, -21, 1.5, 0.4, note="bass with the build into 'every chip on the planet'"),
    glue("N6", 466.0, 492.0, 30.0, -20, note="glue under the Gnomon → Shifting Angles join ('job number one')"),
    # ================= N7 job one: THE LINE (nvs05–06 472.7–647.2): the line → two chips → devastating → a chip on the line → moved → 'the very next day'
    L("N7", "shifting_angles", "instruments", 473.5, 529.0, 61.0, -16, 2.5, 2.5,
      note="restless contemporary-classical cat-and-mouse: quiet 61–69, its 69–72 build on 'it's called a chip ban for a reason' "
           "483.7, steady 72–110 under 'drawing a line' 488.8 → the ranking board → 'covered two chips' 509.3; its 110 drop = "
           "'devastating…a quarter of their entire sales' 518.5–523; out before the file's silence"),
    L("N7", "shifting_angles", "bass", 484.0, 529.0, 71.5, -20, 2.0, 2.5),
    glue("N7", 520.0, 548.0, 45.0, -20, note="floor under 'the demand…is exploding' 531 → 'they had to do something' 536"),
    L("N7", "shifting_angles", "instruments", 536.0, 603.5, 123.0, -16, 2.0, 0.6,
      note="second pass: quiet 123–128, its 128–131 build = 'Very quickly…a brand new chip' 542.5; steady 131–149 = 'right there "
           "on the line' 548.3; 149–184 PEAK = 'the administration moves the line below this new chip' 565.5 → 'another chip' 575.6 "
           "→ 'the commerce secretary…we can keep playing this game' 585.5 → the quote; its 184–190 drop lands on 'ban the new chip "
           "that you launch…the very next day' 593–598.8"),
    L("N7", "shifting_angles", "bass", 536.0, 603.5, 123.0, -20, 2.0, 0.6),
    L("N7", "shifting_angles", "drums", 562.0, 597.5, 149.0, -24, 2.0, 0.6, note="light drums only under the peak (stem −17.3 LUFS: kept 7 dB under the instruments)"),
    # ================= N8 the PC aside → PlayStation → individuals → Facebook Marketplace → $2,000 → iPhone memory (nvs06–07 598.8–775.3)
    L("N8", "hidden_room", "instruments", 600.0, 731.0, 0.0, -18, 3.0, 3.0,
      auto=[[600, 0], [698, 0], [700, -2], [712, -2], [713, 0]],
      note="floating electro colour for the asides (wry, personal): quiet 0–20 under the PC aside 604 'oh you guys can't see it'; "
           "steady 20–123 under the 90s supercomputer / PlayStation rule 615–631 → individuals carrying chips 647 → Facebook "
           "Marketplace 662.6 → 'Imagine this video bombs' 669.5 → '$2,000…$2,300 or $2,500' 720–725; the file's 123–128 drop = "
           "'That's how people look at it' 727.7. The VO is at its quietest here (700–880: −36…−38 LUFS per 10 s) — the duck follows it"),
    L("N8", "hidden_room", "bass", 647.0, 728.0, 47.0, -22, 2.0, 2.5, note="bass from 'Now, even after the ban, chips were still getting into China' 647.2"),
    glue("N8", 722.0, 790.0, 20.0, -21, fi=4.0, fo=4.0,
         note="drone alone for the iPhone memory 734.6–756 ('I'm not saying I did it, but I was young') and 'limited resources…300 bucks'"),
    # ================= N9 the big fish (nvs08 775.3–864.8): co-founder arrested → $1.5 billion → fake company → hair dryer → the warehouse camera
    L("N9", "operation", "instruments", 776.0, 866.0, 24.5, -16.5, 3.0, 1.5,
      auto=[[776, 0], [806, 0], [808, -1.5], [826, -1.5], [827, 0]],
      note="dark caper pulse (C minor): steady 24–83 under 'They want to go after people who are doing this in a big way' 779.5 → "
           "'arrested a co-founder' 782.9 → '$1.5 billion worth of servers' 792.8 → 'pretending like it's in South Korea' 802; thinner "
           "under the auditors / hair-dryer explanation 808–826; its 83–112 PEAK = 'The warehouse camera was recording all of this' "
           "834.7 → 'So he was caught' 838.7 → 'very damning' → Megaspeed 846.8; its 112–116 drop = the verdict 864.8"),
    L("N9", "operation", "melody", 800.0, 866.0, 48.5, -19.5, 2.0, 1.5),
    L("N9", "operation", "bass", 776.0, 866.0, 24.5, -21, 3.0, 1.5),
    L("N9", "operation", "drums", 834.0, 864.0, 82.5, -25, 1.0, 1.5, note="drums only under the camera peak, far under the instruments (stem −14.3 is the loudest)"),
    # ================= N10 VERDICT job one ✗ (nvs09 864.8–935.1): 'it's not working' → a joke? → why keep it → keep the LEAD
    glue("N10", 860.0, 902.0, 60.0, -19.5, fi=3.0, fo=4.0,
         note="near-silence for the verdict: 'small chips are getting in, big chips are getting in' 864.8 → '…it's not working' 889.0 (stinger)"),
    L("N10", "unsolved_issues", "instruments", 890.0, 936.0, 100.0, -17.5, 3.0, 2.0,
      note="the title question's theme returns (rhyme: 'Was the chip ban a mistake?' ↔ 'So why do they still have this ban?' 905.5); "
           "its 126–129 build + 129–133 peak land on 'Maybe the goal of the chip ban isn't about keeping chips out' 918.2 → "
           "'Maybe the goal is to keep the lead that the US has in AI' 922.0; its 133–140 drop under 'the equation changes' 926"),
    L("N10", "unsolved_issues", "melody", 905.0, 934.0, 115.0, -20, 2.5, 2.0),
    glue("N10", 928.0, 950.0, 90.0, -20, note="glue across the part-2 boundary ('Let me explain what I mean' 935.1)"),
    # ================= N11 job two: scale (nvs10 935.1–1046.1): training → cluster → the rack = a refrigerator, 3,000 lb, 100 homes → Memphis → 7 %
    L("N11", "pinnacle", "full", 936.5, 1047.0, 16.0, -19, 3.0, 1.0,
      note="the server-hall colour (ambient drone pulses; full mix: stems 6–18 LU under it, Σ ≠ full): steady 20–72 under training "
           "→ cluster → 'the size of a refrigerator' 964 → '3,000 pounds' 971 → '100 homes' 976.5 → liquid cooling 985.5; its 72–90 "
           "quiet = 'thousands of these racks' 994.5 → 'so hard to smuggle' 1003.7; 90–96 build → 96–121 PEAK = 'a single data center "
           "in Memphis…800,000 homes' 1016.2 → 'more computing power than everything China has smuggled' 1023.6 → '7%' 1035–1046; "
           "its drop = 'So, in this sense, the ban is working' 1046.1"),
    glue("N11", 1040.0, 1056.0, 110.0, -20),
    # ================= N12 the ban works (nvs11 1046.1–1174.6): 60 % → 80 % → China 1 % → cut sales 80 % → ByteDance → DeepSeek dark → leaked call → irony
    L("N12", "seventy_seven_cycles", "instruments", 1047.5, 1174.6, 0.0, -17, 2.0, 2.5,
      note="the cold-open pulse returns (rhyme: the chips that got in ↔ how few they are): steady 0–54 under '60% … close to 80' "
           "1051.6–1060 → 'China only has about 1%' 1063.6 → '80%' 1080 → ByteDance 1090.8; its 54–67 peak = 'DeepSeek itself went "
           "dark for about 12 hours' 1105.6; 83–99 peak = 'more AI researchers…not enough chips, and that's what counts' 1134–1139; "
           "its 99–118 drop/quiet = the irony about electricity 1139.8–1168; out on 'let's get back to the story' 1172.7"),
    L("N12", "seventy_seven_cycles", "bass", 1050.0, 1146.0, 2.5, -21.5, 2.0, 2.5),
    L("N12", "seventy_seven_cycles", "melody", 1100.0, 1146.0, 52.5, -20, 2.0, 2.5, note="melody only through DeepSeek → the leaked call"),
    glue("N12", 1166.0, 1186.0, 140.0, -20),
    # ================= N13 three ways to measure the lead → tests → the US government's unseen test → caveats (nvs12–13 1174.6–1356.3)
    L("N13", "cinema_neon", "full", 1176.0, 1261.0, 57.0, -20.5, 2.5, 2.5,
      auto=[[1176, 0], [1230, 0], [1232, -2], [1259, -2]],
      note="the explainer colour of the overview returns for the three ways to measure (charts world): chips 20× 1180.6 → test "
           "scores, '30 points…three points' 1198–1205 → 'seven to eight months' 1224.4; thinner under 'building models to succeed "
           "in these tests' 1242–1260 (dense)"),
    L("N13", "subconscious", "full", 1259.0, 1357.0, 81.0, -21, 2.5, 2.5,
      auto=[[1259, 0], [1276, 0], [1278, -2], [1300, -2], [1302, 0]],
      note="mystery for 'the US government itself recently ran its own tests that no one has seen' 1260.5 (file steady 81–177); "
           "thinner under the unseen-questions explanation 1277–1300; caveats 1312–1341 → 'Shouldn't the gap…be much larger?' 1346.8"),
    glue("N13", 1250.0, 1270.0, 160.0, -20),
    glue("N13", 1349.0, 1364.0, 175.0, -20),
    # ================= N14 the factors nobody says aloud → the chart → distillation → labs share attacks → gap widening (nvs14–15 1356.3–1572.5)
    L("N14", "the_investigator", "instruments", 1357.0, 1453.5, 57.0, -17, 2.5, 1.5,
      note="the investigation colour of 'is it fair?' returns (rhyme): steady under smuggling 1360.8 → 'you're not gonna publicly "
           "say that' 1374 → 'DeepSeek used a lot more NVIDIA chips' 1405; its 133–146 PEAK = 'Take a look at this chart' 1428.6 → "
           "'always upgrading right after American models' 1435.3 → 'The trend is suspicious' 1442.3; its 153–157 drop = "
           "'this is called distillation' 1451.7"),
    L("N14", "the_investigator", "bass", 1357.0, 1453.5, 57.0, -20.5, 2.5, 1.5),
    L("N14", "the_investigator", "melody", 1405.0, 1453.0, 105.0, -20, 2.0, 1.5),
    glue("N14", 1446.0, 1462.0, 190.0, -20),
    L("N14", "shifting_angles", "instruments", 1454.0, 1512.0, 131.0, -16.5, 2.0, 2.5,
      note="the cat-and-mouse track of THE LINE returns for the second cat-and-mouse game: steady 131–149, its 149–184 PEAK = "
           "'It's like a cat and mouse game' 1473.7 → 'tens of thousands of fake accounts' 1484.2 → 'apply that whole brain' 1489.9; "
           "its 184–190 drop = 'top companies are now working together' 1509.4"),
    L("N14", "shifting_angles", "bass", 1454.0, 1512.0, 131.0, -20.5, 2.0, 2.5),
    L("N14", "breath_by_breath", "instruments", 1511.0, 1596.0, 46.0, -17.5, 3.0, 1.0,
      note="hopeful contemporary classical for the turn: 'they are now working together' 1519.8 → Anthropic, OpenAI, Google 1536.6 "
           "→ 'the gap…is widening again just a little bit' 1558.7–1572; its 114 s PEAK lands on the scoreboard: 'Second job is to "
           "keep the American lead. In that sense, it is working' 1576.6–1582.5 → 'So the score is one to one' 1589.1–1590.9 "
           "(stinger) → 'The second job is successful' 1593.1; out on 'let's go to job three' 1595.2"),
    L("N14", "breath_by_breath", "melody", 1540.0, 1596.0, 75.0, -19.5, 2.5, 1.0),
    L("N14", "breath_by_breath", "bass", 1560.0, 1596.0, 95.0, -21.5, 2.0, 1.0),
    glue("N14", 1588.0, 1606.0, 30.0, -20, note="glue into job three"),
    # ================= N15 job three: Jensen's argument (nvs16 1595.2–1698.2): a competitor → hooked on American chips/software → keyboard → biased
    L("N15", "the_northern_cliff", "instruments", 1596.0, 1748.0, 22.0, -16.5, 2.5, 2.0,
      note="hopeful suspense (Erasmus Talbot, the City Phases composer): quiet 22–57 under 'the CEO of NVIDIA, Jensen Huang' 1602.4 "
           "→ 'a competitor that did not exist before' 1621.4; its 57–60 build = 'every Chinese AI company is built on American chips' "
           "1631; steady 60–85 under the keyboard analogy 1646–1657; its 85–89 drop = 'this sounds like a very logical argument…biased' "
           "1661.7 (quiet 89–120 under the fiduciary aside); 120–128 build = 'Job three is basically keeping China hooked' 1698.3; "
           "128–168 PEAK = '95%' 1704 → '0%' 1711.3 → 'who is selling China chips' 1736.9 → 'the answer is Huawei' 1742.2; drop 168"),
    L("N15", "the_northern_cliff", "melody", 1631.0, 1748.0, 57.0, -19, 2.0, 2.0, auto=[[1631, 0], [1660, 0], [1663, -3], [1693, -3], [1697, 0]]),
    L("N15", "the_northern_cliff", "bass", 1696.0, 1748.0, 122.0, -21, 2.0, 2.0),
    glue("N15", 1740.0, 1756.0, 60.0, -20),
    # ================= N16 Huawei scales → the Commerce Secretary → Lutnick's quote → China blocks → 600,000 at a port (nvs17–18 1742–1855)
    L("N16", "gnomon", "instruments", 1745.0, 1857.0, 12.0, -17.5, 2.0, 1.5,
      note="the 'American law' pulse returns for Washington's own move: steady 12–73 under '200,000 chips' 1752.8 → 'half a "
           "million' 1758 → 'one and a half million' 1764 → 'a random person helping out China' 1771.7 → 'the current commerce "
           "secretary' 1778.7 → 'a stronger chip' 1783.5; its 73–88 drop/quiet = the Lutnick quote 1801.5–1820.3 ('so they can stay "
           "addicted to the American technology' 1815.5); 88–95 build → 95–119 PEAK = 'If you're a Chinese government…' 1829.4 → "
           "'China itself is kind of blocking NVIDIA chips' 1835.9 → '600,000 chips are sitting on a port' 1844.9; its drop = "
           "'Why is the CCP doing this?' 1853.5"),
    L("N16", "gnomon", "melody", 1745.0, 1857.0, 12.0, -19, 2.0, 1.5, auto=[[1745, 0], [1799, 0], [1801.5, -4], [1820, -4], [1822, 0]]),
    L("N16", "gnomon", "bass", 1821.0, 1857.0, 88.0, -21, 1.5, 1.5),
    glue("N16", 1850.0, 1866.0, 80.0, -20),
    # ================= N17 volume → yield → Texas Instruments → 10 % / 30 % / 99.x % → TSMC → 'volume before you get better' (nvs18–20 1855–2026)
    L("N17", "cinema_neon", "full", 1856.0, 2027.0, 0.0, -20.5, 3.0, 2.5,
      auto=[[1856, 0], [1940, 0], [1942, -2], [1968, -2], [1970, 0]],
      note="the explainer colour once more (lessons, charts, history): quiet entry, steady under 'the most important thing…is "
           "volume' 1873.8 → 'yield' 1882.3 → Texas 1897.5–1906 → '10%' 1906–1912 → '30%' 1912.9 → '99.3%' 1919.9 → TSMC 1926.8; "
           "thinner under the dense 'volume before you get better' 1940–1968; the file's 167–173 drop = 'explain how you look at the "
           "chip industry as a whole' 2022"),
    glue("N17", 2016.0, 2034.0, 100.0, -20),
    # ================= N18 60 % again → iPhone 1 vs iPhone 18 → computing power 10 % → the CCP's plan (nvs20 2026–2103)
    L("N18", "hidden_room", "instruments", 2027.0, 2104.0, 20.0, -18, 2.5, 2.0,
      note="the wry aside colour of the PlayStation rule returns (rhyme: PlayStation ↔ iPhone 1): 'Imagine you have an iPhone 1' "
           "2026.7 → 'iPhone 18' 2029.5 → 'they're both iPhones' 2037 → 'look at the computing power' 2065.2 → '10%' 2066.8 → 'Not as "
           "scary' 2074 → the CCP's plan 2077–2103"),
    L("N18", "hidden_room", "bass", 2060.0, 2104.0, 53.0, -22, 2.0, 2.0),
    glue("N18", 2096.0, 2156.0, 120.0, -19.5, fi=3.0, fo=4.0, note="floor under 'more questions…than answers' 2103 → the scoreboard → level four"),
    # ================= N19 more questions → the fourth level → SCOREBOARD job three ✗ → 'let's talk about level four' (nvs21 2103–2147)
    L("N19", "unsolved_issues", "instruments", 2105.0, 2151.0, 120.0, -18, 3.0, 2.0,
      note="the question theme, third time: 'how the hell are Chinese companies getting so close' 2108.8–2123; its 154–161 peak = "
           "'I don't think it's working' 2138.3–2140 (stinger) → 'Commerce Secretary is not actually helping' 2142; its 165–171 drop "
           "= 'let's talk about level four' 2147.0"),
    # ================= N20 level four: the loophole → Malaysia → renting → 'perfectly legal' → flying with the data → the debate (nvs21–23 2147–2351.6)
    L("N20", "across", "instruments", 2150.0, 2352.0, 18.0, -16.5, 4.0, 0.8,
      auto=[[2150, 0], [2205, 0], [2207, -1.5], [2236, -1.5], [2238, 0], [2312, 0], [2314, -1.5], [2340, -1.5], [2342, 0]],
      note="'Across' (Harbours & Oceans, ambient floating suspense, nearly tempo-free: pulse 2.8, bass 1.2): quiet 18–48 under "
           "'a loophole…we kept it till the end' 2149–2158 → data centers 'in the middle of nowhere' 2167 → 'stretch this argument "
           "really far away' 2177.2; its 48–52 build lands on 'a lot of data centers in Malaysia' 2182.7; thinner under 'someone "
           "perfectly legal owns that data center…' 2208–2236; its 134–143 build = 'The funniest part of all this' 2268.2, 143–154 "
           "peak = 'AI employees are actually flying to Malaysia with…the information' 2280.6; 175–180 build = the debate 2307.3; "
           "thinner under the two arguments 2313–2340; dips for the scoreboard '?' 2351.55"),
    L("N20", "across", "bass", 2180.0, 2352.0, 48.0, -20.5, 2.0, 0.8),
    L("N20", "across", "melody", 2266.0, 2352.0, 134.0, -19, 2.0, 0.8, note="melody from 'The funniest part' 2268.2 (active only 37 % of the file)"),
    # ================= N21 outro: '?' → comments → 'My name is Sam' → fade to night by 2402.0 (nvs23 2351.6–2402)
    L("N21", "across", "instruments", 2351.0, LEN, 219.0, -19.5, 0.8, 4.5,
      auto=[[2351, 0], [2390, 0], [2398.5, -3], [LEN, -6]],
      note="the same track continues, a touch lower, under the honest '?' and the comment request (its quiet 253–275 tail); "
           "fades with the picture to 2402.0"),
    glue("N21", 2344.0, LEN, 140.0, -20, fi=4.0, fo=5.0, note="drone floor to the end"),
]

stingers = [
    dict(file="swell_reverse_timpani_cymbal", t=147.72, sync="loudest", rel_lu=-30, note="TITLE QUESTION: swell peaks on 'Was the chip ban a mistake?'"),
    dict(file="boom_dark_cinematic_low_hit", t=889.0, sync="loudest", rel_lu=-28, note="SCOREBOARD job one ✗: '…it's not working.'"),
    dict(file="boom_sub_bass_clean_01", t=1590.5, sync="loudest", rel_lu=-31, note="SCOREBOARD job two ✓: 'So the score is one to one' (felt, not heard)"),
    dict(file="boom_dark_cinematic_low_hit", t=2139.62, sync="loudest", rel_lu=-28, note="SCOREBOARD job three ✗: 'I don't think it's working'"),
    dict(file="riser_reverse_cymbal_short", t=2354.19, sync="loudest", rel_lu=-31, note="SCOREBOARD row four '?': 'I don't know how to rank this part'"),
]

marker_edits = []   # phase 2: fix editors' markers here ({t, type, action: drop|retype, to, note})

sheet = dict(
    length=LEN,
    doc="Layered Epidemic bed for 'NVIDIA — Is the chip ban actually working?' (Searching Lessons). Master seconds of "
        "project/nvidia/media/vo_nv.wav (= vo_nv.mp3). Generated by project/nvidia/gen/make_cuesheet.py — edit there. Key family C minor "
        "(+ Eb major). Acts N1–N21 = SOUND_PLAN.md §2 (from SEGMENTS.md §3). Binding music limits (MANUAL §10.8): bed VO − 22 LU, "
        "vo_duck gap 20 / gap_fast 18 / ceiling 20, no pause lifts.",
    # ---- BINDING (MANUAL §0, §10.8 "Music limits", Krish 2026-11-13) — never loosen
    bed_lu_under_vo=22.0,
    pause_lift_db=0.0,
    vo_duck=dict(gap=20.0, gap_fast=18.0, ceiling=20.0, margin=0.7, attack=0.05, release=0.4, max_cut=-30.0, passes=3),
    layers=layers, stingers=stingers, ducks=[], bleeps=[], marker_edits=marker_edits)

assert sheet["bed_lu_under_vo"] >= 22 and sheet["vo_duck"]["gap"] >= 20 and sheet["vo_duck"]["gap_fast"] >= 18 \
    and sheet["vo_duck"]["ceiling"] >= 20 and sheet["pause_lift_db"] == 0, "binding music limits loosened"
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "music_cuesheet.json")
json.dump(sheet, open(out, "w"), indent=1)
print("wrote", os.path.normpath(out), len(layers), "layers,", len(stingers), "stingers")
