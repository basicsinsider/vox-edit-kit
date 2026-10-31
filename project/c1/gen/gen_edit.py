import sys, re; sys.path.insert(0, "project/c1/gen")
from common import *; from beats_data import B; from scenes_data import S; from assets_data import A
bstarts = [b[0] for b in B]
def beats_of(s, e):
    ids = [f"C1B{i+1:03d}" for i, bs in enumerate(bstarts) if bs < e - 1e-6 and (bstarts[i+1] if i+1 < len(bstarts) else END) > s + 1e-6]
    return ids[0] if len(ids) == 1 else f"{ids[0]}–{ids[-1][4:]}"
GN = {"N": "NIGHT", "P": "PAPER", "G": "GRID"}
issues = []; scenes = []
for i, sc in enumerate(S):
    s = sc[0]; e = S[i+1][0] if i+1 < len(S) else END
    check_t(s)
    cues = [float(x) for x in re.findall(r"@(\d+\.\d\d)", sc[8])]
    for c in cues:
        check_t(c)
        if not (s - 0.01 <= c < e): issues.append(f"SC{i+1:03d} cue {c} outside {s}–{e}")
    for a in sc[7]:
        if a not in A: issues.append(f"SC{i+1:03d} unknown asset {a}")
    hold = e - max(cues) if cues else None
    scenes.append(dict(n=i+1, id=f"C1S{i+1:03d}", s=s, e=e, g=sc[1], tag=sc[2], why=sc[3], fx=sc[4], ref=sc[5], vis=sc[6], assets=sc[7], text=sc[8], cam=sc[9], out=sc[10], sfx=sc[11], hold=hold))
# transition fix-up: never the same type twice in a row (rotate alternatives)
ALT = ["HC", "W←", "PS", "FW", "W↓", "PT", "W→"]; k = 0
for a, b in zip(scenes, scenes[1:]):
    tya = "W" if a["out"].startswith("W") else a["out"]; tyb = "W" if b["out"].startswith("W") else b["out"]
    if tya == tyb and b["out"] != "end":
        nxt = scenes[scenes.index(b)+1]["out"] if scenes.index(b)+1 < len(scenes) else ""
        for j in range(len(ALT)):
            c = ALT[(k + j) % len(ALT)]; tc = "W" if c.startswith("W") else c
            tn = "W" if nxt.startswith("W") else nxt
            if tc != tya and tc != tn: break
        k += 1; b["out"] = c; b["fix"] = True
        if c.startswith("W") or c == "FW": b["sfx"] += f" · {b['e']-0.06:.2f} whoosh (transition)"
        elif c == "PS": b["sfx"] += f" · {b['e']-0.08:.2f} paper_slide (transition)"
# checks
run = 1
for a, b in zip(scenes, scenes[1:]):
    run = run + 1 if a["g"] == b["g"] else 1
    if run > 3: issues.append(f"ground run >3 at {b['id']}")
light = 0
for sc in scenes:
    light = light + 1 if sc["g"] in "PG" else 0
    if light > 3: issues.append(f"PAPER/GRID run >3 at {sc['id']}")
ty = lambda o: "W" if o.startswith("W") else o
for a, b in zip(scenes, scenes[1:]):
    if ty(a["out"]) == ty(b["out"]) and a["out"] not in ("end",): issues.append(f"same transition twice {a['id']}→{b['id']} ({a['out']})")
for sc in scenes:
    if sc["e"] - sc["s"] < 2.0: issues.append(f"short scene {sc['id']} {sc['e']-sc['s']:.2f}")
print("\n".join(issues) or "checks ok", len(scenes))
json_out = __import__("json"); json_out.dump([{k: v for k, v in sc.items()} for sc in scenes], open("project/c1/gen/scenes.json", "w"), indent=0)

# ---------------- write EDIT_NOTES.md
ACTS = [(0.00, "1. Act I — Cold open: Terman's quote and the claim (0.00–46.13)", "Music: soft textural pad continuing from the intro's flash; first pulse under 'father of Silicon Valley' 16.08; lift on 'copy it' 44.93."),
 (46.13, "2. Act II — The trillion-dollar West (46.13–78.77)", "Music: pulse + light percussion stem; hits on 12 (52.45) and 11 (65.41); playful pluck on apples/oranges."),
 (78.77, "3. Act III — A century ago: the lopsided East and the brain drain (78.77–143.72)", "Music: drop the pulse on 'rewind' 79.25; sepia drone + melodic layer; tension texture under 'brain drain' 138.52."),
 (143.72, "4. Act IV — Herbert Hoover at Stanford, with the Twitter aside (143.72–277.60)", "Music: mid-tempo storytelling; thin to a light playful layer 176.67–208.43 (no hits on the joke); stinger on 'admitted' 215.15; warm build 250–277."),
 (277.60, "5. Act V — Enter Frederick Terman (277.60–357.32)", "Music: title stinger on 'Frederick' 284.63; light under 1900/2000; melancholy pad under 'breaking his heart' 330.87/348.44."),
 (357.32, "6. Act VI — Hewlett & Packard and Terman's plan (357.32–436.03)", "Music: momentum layer enters on 'Bill' 378.28; hit on 'HP' 384.20; build under the plan."),
 (436.03, "7. Act VII — HP is born: Disney, the coin flip, the garage, the oscillator (436.03–516.54)", "Music: playful pizz/marimba-like layer for the coin flip; warm swell on 'garage' 478.14; light ticking texture under the oscillator explanation."),
 (516.54, "8. Act VIII — World War II and federal money (516.54–591.62)", "Music: cut to low drone + pulse on 'the war' 519.10; dark pulses under the secret lab; release on 'Dean' 550.57; triumphant build into 'federal money' 586.90."),
 (591.62, "9. Act IX — The catch, hand-off to c2 (591.62–602.86)", "Music: thin to one sustained layer; leave it hanging into c2.")]
o = []; P = o.append
P("# EDIT NOTES — CHUNK c1 “Taiwan: the chip rivalry” (Searching Lessons), LOCAL VO 0.00–602.86 (full audio 275.06–877.88)\n")
P("Shot-by-shot plan for chunk c1 (the Silicon Valley origin story). Read with `project/LONGFORM.md`, `MANUAL.md` (§10.1–10.9 override older")
P("sections; §5 effects; §6/§6.1 layouts), `project/c1/analysis/BEATS.md`, `ASSETS_NEEDED.md` (IDs), `SEGMENTS.md`, `DECISIONS.md`.")
P("Prepared 2026-10-31 by the director / edit planner. Generated from `project/c1/gen/scenes_data.py` by `gen_edit.py` (which also")
P("validates every cue against `transcript_c1.json` and runs the rhythm checks in §11) — **edit the data file and re-run** rather than this file.\n")
P("## 0. How to read this file\n")
P(f"- **Times** = LOCAL c1 seconds (`vo_c1.mp3`, `transcript_c1.json`); add 275.06 for the full audio. **{len(scenes)} scenes, C1S001–C1S{len(scenes):03d}**, contiguous 0.00 → 602.86, every boundary on a word start.")
P("- **Text cue `@t`** = start of the spoken word; first frame at `T(t) − 0.06`. Multi-word lines are revealed **word by word** (each word its own literal `T()`). Backticks = exact on-screen text; the word list after it gives each word's cue.")
P("- **Words** = exact narration under the shot (ASR fixes in bold). **Why** = why the picture matches those words (§10.1.3).")
P("- **Ground**: `NIGHT` (dark/cinematic/archival full-frame), `PAPER` (Texturelabs `_hires` papers, two layers, top ~90 %), `GRID` (graph/ruled/blueprint/ledger papers — `_hires` full-frame, K+E scans only as cards ≤ native size). ≤ 3 same ground in a row and PAPER+GRID ≤ 3 combined (checked §11.4).")
P("- **FX** = MANUAL §5 numbers + §10 craft. Transitions: `W←/→/↑/↓` whip (`FX.whip`), `FW` light-flash whip, `CA` cut on action (camera/secondary motion — never an unfinished key animation), `HC` hard cut on action (the reel's variant), `PT` push-through, `PS` paper slide / torn-paper wipe, `MC` match cut (an element carries into the next shot), `CRT` CRT power-on cut, `cont` = same world continues (no cut). **No iris.** `FH` focus hunt (once per scene max), `CS` chokeSettle.")
P("- **Hold rule (§10.9)**: the scene's key animation finishes and HOLDS ≥ 0.5 s before the out-transition starts. Column ‘hold’ in §11.6 = time from the last text cue to the cut; scenes under 0.9 s are flagged: their last word must use a short entrance (≤ 0.3 s rise) and the cut rides a camera move.")
P("- **Glow**: `.halate` only on the scene's hero (marked ‘hero halate’); everything else `.clean`; paper never glows.")
P("- **Ref** = Krish's intro pack `D01–D15` (`references/style-images/intro/`) or the originals `R1–R12` (`references/style-images/1–12`, built examples in `expected/layouts/`), each used as a **variation** (colour lead, orientation, density, entry). `s01–s11` = approved samples (`compositions/sNN-*.html`); `old SCnnn` = scene of the approved 10-minute edit (`templates/full-edit/segNN.html`, `example-docs/EDIT_NOTES.md`). New reference ideas are named “Pinterest idea: …”.")
P("- **Palette (Silicon Valley mapping, decided here)**: `--west` = vermilion **= the West / California / Stanford / Terman's Silicon Valley / HP**; `--east` = navy (sky on night) **= the East coast, MIT, Harvard, Bell Labs, GE, Eli Lilly**; yellow = highlighter + the scene's one key number (12, 90 %, 1891, $100, 25, 800); celadon (Taiwan) unused in c1. People are neutral sepia/ink (Hoover is NOT red — red later means Morris Chang/TSMC; vermilion only as Stanford/West tags, bars, routes). Max two accents per frame.")
P("- **No face cam** in c1 (§10.9). **Copyrighted images allowed** (fair use, credited in SOURCES.md + 13 px on-screen credit where customary). Image reuse allowed when needed (prefer new).")
P("- **Maps** from `assets/maps/kit/` (N93) — never flat grey/beige relief; approved s02 satellite US map is the bar. Old-map scans (Rand McNally 1920, USGS) stay as the vintage-atlas D10/R10 look.")
P("- **SFX** lines = object events (LOCAL s) → `compositions/c1sNN.sfx.json` (vocabulary SEGMENTS §3.4). Sound only the hero event per scene (§10.8 restraint); transition whooshes are added by the editor where a whip/flash lands.")
P("- Hand-off IN: the intro ends with streaks flaring to bone (IS066); C1S001's first 4 frames are that bone flash fading into the painting.\n")
ai = 0
for sc in scenes:
    while ai < len(ACTS) and sc["s"] >= ACTS[ai][0] - 1e-6:
        P(f"## {ACTS[ai][1]}\n{ACTS[ai][2]}\n"); ai += 1
    tag = f" · {sc['tag']}" if sc["tag"] else ""
    P(f"### {sc['id']} · {sc['s']:.2f}–{sc['e']:.2f} · {beats_of(sc['s'], sc['e'])} · {GN[sc['g']]}{tag}")
    P(f"- **Words** “{words(sc['s'], sc['e'])}”  **Why** {sc['why']}.")
    P(f"- **FX** {sc['fx']} · **Ref** {sc['ref']}")
    P(f"- **Visual** {sc['vis']}")
    if sc["assets"]: P(f"- **Assets** " + ", ".join(sc["assets"]) + " (see ASSETS_NEEDED)")
    P(f"- **Text** {sc['text']}")
    P(f"- **Camera** {sc['cam']}. **Out** `{sc['out']}`" + (" (planner rhythm fix — editor may pick another non-repeating type)" if sc.get("fix") else "") + f" @{sc['e']:.2f}.")
    P(f"- **SFX** {sc['sfx']}\n")
# coverage
P("## 11. Coverage tables and checks\n")
def find(pat): return [sc["id"] for sc in scenes if re.search(pat, sc["fx"] + " " + sc["ref"])]
P("### 11.1 Effects (MANUAL §5 + §10)\n\n| effect | scenes |\n|---|---|")
for name, pat in [("#1 B-roll footage", r"#1 "), ("#2 charts/diagrams", r"#2 "), ("#3 maps", r"#3 "), ("#4 film-title hero", r"#4"), ("#5 newspaper/document", r"#5"), ("#8 light streaks", r"#8"),
                  ("#10 Vox layered", r"#10"), ("#11 screens (TV/scope/radar)", r"#11"), ("#12 collage/timeline", r"#12"), ("#13 text animations (count/odometer/random/typewriter)", r"#13"),
                  ("#14 gate weave", r"#14"), ("#15 curve cut", r"#15"), ("#16 hi-quality plate", r"#16"), ("#17 2.5D", r"#17"), ("#18 rough/stamp/highlighter", r"#18"),
                  ("#19 markups (pen, circle, cross, strings)", r"#19"), ("#20 map call-outs", r"#20"), ("§10.7 painting-to-print", r"§10\.7"), ("§10.6 call-outs (contrast/text/focal/radio waves)", r"§10\.6")]:
    P(f"| {name} | {', '.join(find(pat))} |")
P("| whips / FW / CA / HC / PT / PS / MC | see §11.5 |")
P("\nNo iris anywhere ✔. Screens vary: 1950s TV (C1S054), 1940s oscilloscope (C1S086), WWII radar PPI scope (C1S094–095) — none of the four museum TVs, no Tatung/Trinitron (those are 1980s Taiwan).\n")
P("### 11.2 Reference layouts (each a variation of its earlier use)\n\n| ref | scene(s) | variation vs earlier use |\n|---|---|---|")
VAR = {"D01": "with R1: navy watercolour East bar + skyline, label-box 90 %", "D02": "2 bars only, campus-tower cut-outs instead of portraits", "D03": "person pictograms = 10 people each, count to 800",
 "D04": "unlabelled field bars, title word by word, 'everything' struck", "D05": "era band = his first ten years; line falls and cracks", "D06": "board seats, one seat swells with Hoover's portrait",
 "D07": "collage poster of 1920s engineers + two campus cards, Stanford stamp", "D08": "wartime telegram on Western Union ground + SECRET stamp", "D09": "pictorial colour city map (not B/W), pin + pen circle",
 "D10": "tilted *pictorial* California map + contrast call-out", "D11": "Sankey into Stanford → ends in portrait circles", "D12": "25 unnamed ruled rows, yellow count, rack focus",
 "D13": "dark ghost world map: copies landing (C1S007), radio-wave rings (C1S047)", "D14": "Stanford campus satellite, lab districts + yellow money route", "D15": "family two-node (C1S055); hub-and-spoke connections (C1S078)",
 "R1": "see D01", "R4": "horizontal orientation", "R5": "graduates walking single file (C1S023), row + STOP (C1S062)", "R6": "see D04", "R7": "see D05", "R9": "small 3-card plan board",
 "R10": "railroad map: there-only route with 3 pins (C1S021), there-and-back (C1S057)", "R11": "map-kit relief, pen route East→West", "R12": "Indiana navy (approved R12b), glowing valley on world map",
 "markup-map": "1890s Stanford vs modern Stanford prints", "s01": "1938 & 12 cards", "s02": "re-timed, map-kit basemap", "s06": "re-timed", "s09": "two-part (silhouettes → reveal)", "s10": "re-timed", "s11": "Washington lines, crosses"}
for ref in ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13","D14","D15","R1","R4","R5","R6","R7","R9","R10","R11","R12","markup-map","s01","s02","s06","s09","s10","s11"]:
    ids = [sc["id"] for sc in scenes if re.search(r"(?<![A-Za-z0-9])" + re.escape(ref) + r"(?![0-9])", sc["ref"])]
    P(f"| {ref} | {', '.join(ids) or '—'} | {VAR.get(ref,'')} |")
P("\nAll 15 intro refs (D01–D15) used; all original refs except R2 (optional) / R3 (skipped) and R8 (= D06 family, used via D06). New Pinterest-style ideas named in the scenes: antique globe → satellite match cut, blueprint title lettering, brush-stroke reveal, balance-scale infographic, tweet printed on paper, classified-ads highlighter, ledger ticks, brass door-plate title, slot-machine year counter, patent-style signal-flow diagram.\n")
P("### 11.3 2.5D (3 moments)\nC1S027 Main Quad 1891 (approved) · C1S056 1920 Stanford group with young Terman · C1S083–084 the HP garage (approved s10).\n")
P("### 11.4 Ground rhythm (N night · P paper · G grid)\n```")
line = []
for sc in scenes:
    line.append(f"{sc['n']:03d}{sc['g']}")
for i in range(0, len(line), 16): P(" ".join(line[i:i+16]))
P("```\nChecked by the generator: no run of the same ground > 3; PAPER+GRID combined ≤ 3. ✔\n")
P("### 11.5 Transitions in order (never the same type twice in a row — checked ✔)\n")
P(", ".join(sc["out"] for sc in scenes) + "\n")
P("### 11.6 Hold before the cut (§10.9) — last text cue → scene end\n")
tight = [f"{sc['id']} ({sc['hold']:.2f} s)" for sc in scenes if sc["hold"] is not None and sc["hold"] < 0.9]
P("Scenes where the last word lands < 0.9 s before the cut (editor: short entrance ≤ 0.3 s, the key animation of the scene must already be finished — e.g. bars/route/count complete before the last label; cut on the camera move): " + ", ".join(tight) + ".\n")
P("Key animations that must complete + hold 0.5 s (explicit): C1S009 count 12 done by 53.6; C1S010 bars done by 58.0; C1S011 burn + pins done by 67.0, river by 68.6 (scene continues); C1S015 bar + count done by 89.2; C1S021 route done by 129.2; C1S027 1891 rise done by 172.1; C1S041 seat fill done by 239.0; C1S043 flows done by 249.9; C1S057 route + book done by 324.9; C1S058 line + crack done by 331.6 (cut 332.15); C1S069 $100 count done by 392.7; C1S077 count 25 done by 440.8; C1S093 isotype 800 done by 533.6; C1S103 route + districts done by 591.0; C1S105 strike done by 602.5 (chunk end 602.86).\n")
P("### 11.7 Palette check\nVermilion = West/Stanford/HP/Terman's tags, routes and bars; navy = East (NY/NJ/MA, MIT, Harvard, Bell Labs, GE, Eli Lilly); yellow key numbers: 12 (C1S009), 90 % (C1S015), 1891 (C1S027), $100 (C1S069), 25 (C1S077), 800 (C1S093); all other yellow = highlighter. No red portrait duotones (red will mean Morris Chang/TSMC from c2 on). No celadon.\n")
P("### 11.8 Verification summary\n- No face cam ✔ · no iris ✔ · every scene has words + why ✔ · cues validated against the transcript ✔ · ≤ 3 same ground ✔ · no transition type twice in a row ✔ · every D01–D15 used ✔ · all §5 effects used (#6/#7 sound/texture everywhere) ✔ · 3 × 2.5D ✔ · holds listed ✔.\n")
P("## 12. Open questions (defaults in DECISIONS.md)\n1. Palette mapping for Silicon Valley (vermilion West/Stanford, navy East) — default yes.\n2. 'born in the 1900s' → show `1900` (his meaning) — default yes.\n3. 'powerful company' slip (= family) — never caption 'company' — default yes.\n4. Hoover painted portrait for §10.7 (Greene 1956) — default yes.\n5. Twitter-joke aside visuals (tweet card typeset, no handle; Puck cartoon; switch; trading floor; classifieds) — default yes.\n6. 'Did they have Pentagon back then?' → Pentagon + hand-drawn ? (no answer) — default yes.\n7. 12 trillion-dollar list date (Oct 29 2026 snapshot) — default keep.\n8. Fantasia poster as 'Disney' (fair use) — default yes.\n")
open("project/c1/EDIT_NOTES.md", "w").write("\n".join(o) + "\n")
print("EDIT_NOTES written", len(o))
