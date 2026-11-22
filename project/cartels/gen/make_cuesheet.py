#!/usr/bin/env python3
"""Writes project/cartels/music_cuesheet.json — the sound designer's cue sheet for "US vs Cartels" (Searching Lessons),
master seconds 0–1341.912 (= the 24 fps master; VO project/cartels/media/vo_ct.wav is 1341.870 s, so the bed holds 0.04 s past it).
Edit the tables here and re-run (python3 project/cartels/gen/make_cuesheet.py), then rebuild the beds (SOUND_PLAN.md §6).
offset = read position inside the Epidemic file at the layer's start, chosen so a track's own builds / peaks / drops
(assets/audio/epidemic/ANALYSIS.md, quoted in SOUND_PLAN.md §1) land on the words named in the notes (word times from
transcript_ct.json, master seconds).
Key family: G minor (+ its relative Bb major) — every track measured G minor on the WAVs (r 0.72–0.94); the drone measures
Bb major (Bb–C–D–F, inside G minor).
Glue drone: Zone of Deception (DEX 1200), instruments stem only — pulse 2.0 (tempo-free; a pad reads 2.6, a 120-bpm click 14).
BINDING limits (MANUAL §0, §10.8 "Music limits", Krish 2026-11-13) are hard settings at the bottom: bed_lu_under_vo 22, vo_duck
gap 20 / gap_fast 18 / ceiling 20, pause_lift_db 0, sfx_limit 14. Never set them looser."""
import json, os

# per-act balance trims (dB on every layer of the act) from act_levels.py: aim −20…−24 LU re the VO while he speaks.
# First pass (2026-11-22): none — set after the 0–180 s test / the phase-2 whole-length build (SOUND_PLAN §5).
TRIM = {"C2": 3.0, "C3": 4.0}   # 0–180 s test 2026-11-22, untrimmed: C1 −24.2, C2 −26.3, C3 −26.9 LU re VO (quiet file openings)

DR = "zone_of_deception"   # Bb-major drone (instruments stem); its peaks sit at 75–80, 84–90, 117–131, 164–172, 210–215 s
_GLUE_OFS = [30.0, 136.0, 179.0, 36.0, 140.0, 182.0, 44.0, 186.0]   # steady/quiet windows of the drone file
_g = [0]


def L(cue, track, stem, start, end, offset, rel, fi=1.5, fo=1.5, auto=None, note="", file=None):
    rel = round(rel + TRIM.get(cue, 0.0), 2)
    d = dict(cue=cue, track=track, stem=stem, start=start, end=end, offset=round(offset, 3), rel_lu=rel,
             fade_in=fi, fade_out=fo)
    if auto: d["auto"] = auto
    if note: d["note"] = note
    if file: d["file"] = file
    return d


def glue(cue, start, end, rel=-21.0, fi=3.0, fo=4.0, offset=None, note="glue under the join"):
    if offset is None:
        offset = _GLUE_OFS[_g[0] % len(_GLUE_OFS)]
        _g[0] += 1
    return L(cue, DR, "instruments", start, end, offset, rel, fi, fo, note=note)


LEN = 1341.912

layers = [
    # ================= C1 COLD OPEN (cts01 0–68.2): ballpark → helicopters → burning trucks → "come for one man" → El Chapo Isidro → caught → "help from the United States"
    L("C1", "db_cooper", "instruments", 0.0, 65.0, 52.0, -16, 0.4, 2.5,
      note="urgent dark drone-pulse from frame 1 (file steady 10–80) under 'That's a baseball game in Mexico' 0.24 → fans ducking → "
           "'there's a gunfight going on' 15–18; its 80–84 build = 'the Mexican army had come for one man' 32.1 → 84–94 PEAK = "
           "'one man' 35.4 → 'El Chapo Isidro' 36.2 → 'not related'; 97–110 peak = FBI's 10 most wanted 50.2 → '$5 million' 53.8; "
           "its 110–117 drop = 'By the end of the night, the Mexican army had him' 57.9–61.2; out by 65 (file end 117)"),
    L("C1", "db_cooper", "bass", 0.0, 65.0, 52.0, -20, 0.4, 2.5),
    L("C1", "db_cooper", "drums", 18.4, 58.5, 70.4, -25, 1.5, 1.5,
      note="muted percussion only from 'This is what was happening outside. Those military helicopters…' 18.4 to the drop"),
    glue("C1", 56.0, 82.0, -20.5, fi=3.0, fo=4.0, offset=30.0,
         note="drone alone under 'they said they got him with the help from the United States' 61.2–68.15 (stinger 67.35) → 'not a one-time thing'"),
    # ================= C2 NOT A ONE-TIME THING → THE QUESTION (cts02 68.2–122.9): Mencho, CIA raid, 70+ boats, Maduro → "Is this a war on cartels?" → TITLE
    L("C2", "perplexed", "full", 68.5, 123.5, 33.7, -19.5, 3.0, 2.0,
      auto=[[68.5, 0], [104, 0], [106, -1.5], [108.5, -1.5], [109.5, 0]],
      note="the QUESTION theme (G minor, r 0.94; full mix — stems 5 LU under it, Σ ≠ full): steady 33–74 under the list "
           "'Just this February…El Mencho' 73.9 → 'April…CIA helped out' 85.4 → '70 boats' 92.1 → 'captured the country's president' "
           "98.4–108; its 74 s PEAK arrives on 'So this all raises a pretty simple question' 109.0 → 'Is this a war on cartels?' "
           "112.8–114.8 → 'And is this actually working?' 115.7–116.8 (swell stinger) → 'start with the guy from last night' → out 123.5"),
    L("C2", "perplexed", "bass", 104.0, 123.5, 69.2, -22, 2.5, 2.0, note="bass (pulse 1.7, nearly tempo-free) thickens the question"),
    glue("C2", 117.0, 137.0, note="glue under the Perplexed → Running through the Dark join ('His name is Fausto Isidro' 123.6)"),
    # ================= C3 SINALOA (cts02–03 122.9–172.8): born 1982 → 'Silicon Valley of drug trafficking' → the 90s → teenager → Beltrán Leyvas gunman → same team
    L("C3", "running_through_the_dark", "instruments", 123.5, 174.5, 0.0, -17.5, 3.0, 2.5,
      note="the Sinaloa colour (acoustic, dark, mysterious; Σ stems = full, −9 dB): quiet entry 0–10 under 'born in 1982 in northern "
           "Sinaloa' 123.6–128; steady 10–86 under 'the Silicon Valley of Mexican drug trafficking' 130.7 → the 90s 139.2 → 'one of "
           "the only jobs that was paying well' 149 → 'as a teenager' 154 → 'a gunman for…the Beltrán Leyvas' 158.9–165.6 → "
           "'the Sinaloa Cartel' 169.6; out before 'But in 2008' 172.8"),
    L("C3", "running_through_the_dark", "melody", 129.5, 172.0, 6.0, -20.5, 2.5, 2.0,
      note="melody (the guitar/plucked line, pulse 14) from 'Sinaloa is kinda like the Silicon Valley' 129.0"),
    glue("C3", 166.0, 190.0, note="glue under the turn to the war ('in 2008, something interesting happened' 172.8)"),
    # ================= C4 THE WAR (cts03 172.8–223.9): 2008 split → civil war → armed wing → 2010 Sonora ambush → 28-year-old boss → brothers fall
    L("C4", "symmetry", "instruments", 172.5, 228.0, 69.5, -17, 2.5, 2.0,
      note="dark orchestral-hybrid weight (Christoffer Moe Ditlevsen; Σ stems = full, −25.5 dB): its 69–82 quiet under 'One of the "
           "brothers got arrested…gave him up' 174–183; 82–85 build = 'there's a civil war between the groups' 183.1–188; steady "
           "85–99 under 'running the armed wing' 188.5 → 'shooting and killing' 195.8 → 'This war is where he makes his name' 199.8; "
           "its 99 s PEAK lands on 'In 2010, his men set up an ambush in the desert in Sonora' 202.1 → '20 to 30 men' 206.5 → "
           "'one of the big bosses' 211.7 → 'arrested or killed one by one' 219.0; out on 'But Isidro survives' 223.9"),
    L("C4", "symmetry", "bass", 188.0, 228.0, 85.0, -21, 2.0, 2.0, note="bass from the armed wing 188.5"),
    L("C4", "symmetry", "melody", 199.5, 226.0, 96.5, -20, 2.0, 2.0, note="melody with the peak, 'This war is where he makes his name' 199.8"),
    glue("C4", 220.0, 240.0),
    # ================= C5 THE ROUTES (cts03 223.9–264.2): survives → north of Sinaloa → routes by boat/coast/highway → 'straight shot towards Arizona' → fentanyl → Treasury 2013
    L("C5", "running_through_the_dark", "instruments", 224.5, 264.5, 72.0, -17.5, 3.0, 2.0,
      note="the Sinaloa colour returns (his own territory, the routes map): steady 72–86 under 'He takes over the north of Sinaloa' "
           "228.6; its 86–122 PEAK lands on 'a straight shot towards Arizona' 238.4–242.1 → 'Cocaine, meth, heroin…fentanyl' 242.1 → "
           "'fentanyl is the drug that matters the most' 245.8 → 'even the US Treasury' 252.6 → 'a cartel boss now' 259.5"),
    L("C5", "running_through_the_dark", "melody", 236.0, 264.5, 83.5, -20.5, 2.5, 2.0),
    glue("C5", 258.0, 278.0, note="glue into the nickname ('Now let's talk about his nickname' 264.2)"),
    # ================= C6 THE NICKNAME + WALKED OUT (cts04 264.2–358.2): two stories → arrested 2011/2014/2014/2015, walked out → 'figure out why' → Dec 2024 stash → one ton → FBI list
    L("C6", "have_we_met_before", "melody", 264.5, 358.5, 0.0, -19, 3.0, 2.0,
      auto=[[264.5, 0], [327.5, 0], [329.0, -2], [332.0, -2], [333.0, 0]],
      note="the wry investigative pulse (sneaking, mysterious; Sam smiles here): quiet 2–34 under the nickname stories 264.2–298 "
           "('clearing bushes with machete' 280.2); steady 34–108 under 'he's actually been caught before multiple times' 298.2 → "
           "the four arrests 303.6 → 'all four times, he walked out' 310.9 → 'charged…by the US government' 313.6–323; −2 dB under "
           "'You guys can figure out why in your own head' 329.4 (the joke breathes); 'December 2024…a massive fentanyl stash' 335.7 "
           "→ 'One ton' 349.7 → FBI's 10 most wanted 357.0"),
    L("C6", "have_we_met_before", "instruments", 298.0, 358.5, 33.5, -21, 2.5, 2.0, note="instruments (pulse 2.9) join with the arrests 298.2"),
    glue("C6", 350.0, 372.0, note="glue into Washington ('a month after Trump took the office again' 358.3)"),
    # ================= C7 WASHINGTON (cts05–06 358.2–470.5): day-one order → terrorist label → 'crime to help you' → armed conflict, al-Qaeda → targets → pressure → tariffs → 25 %
    L("C7", "timepass", "full", 358.5, 471.5, 5.0, -19.5, 3.0, 1.5,
      auto=[[358.5, 0], [394, 0], [396, -1.5], [414, -1.5], [415.5, 0]],
      note="the policy pulse (Marten Moses, sneaking/restless; full mix — stems 6.5 LU under it): 12–15 build on 'his very first day' "
           "366.5 → steady 15–69 under 'terrorist organizations' 370.4 → 'eight different…groups' 372.3 → 'much bigger than just a "
           "label' 382.6 (−1.5 dB under the dense 'crime for anyone to help you…' 396–414) → 'armed conflict' 419.9; its 69–74 "
           "drop + 74–90 quiet = 'the way it treated Al Qaeda' 425.8 → 'They are targets now' 431.7 → 'pressure on Mexico'; 90–95 "
           "build = 'Liberation Day and all the tariffs' 440.1; steady 95–117 = 'a 25% tariff because of fentanyl' 455.7 → 'sells "
           "more stuff to the United States than any other country' 463; its 117 drop = 'a huge threat to their economy' 470"),
    glue("C7", 464.0, 488.0, note="glue under the Timepass → Triple Fault join ('the president of Mexico gets on her phone' 473.7)"),
    # ================= C8 THE PRISONERS (cts06 470.5–540.4): Sheinbaum's call → troops → 29 prisoners on a plane → 1985 DEA murder → 40 years → 26 + 37 → American prison
    L("C8", "triple_fault", "full", 471.0, 516.0, 64.0, -20, 3.0, 2.0,
      note="crime-scene pulse (Robert Ruth; full mix — stems 4.5 LU under): steady 64–98 under 'gets on her phone' 476 → 'The deal did "
           "not just stop there' 482.7 → '29 of the biggest cartel prisoners…on a plane' 492.4 → 'a 1985 murder of an American DEA "
           "agent' 501.5; its 98–103 PEAK = 'chasing for 40 years' 507.6 → 'they got it because of tariffs' 509; drop 103–109 = "
           "'26 more prisoners' 510.6; out at 516 (file end 109)"),
    L("C8", "triple_fault", "instruments", 515.0, 541.0, 20.0, -21, 3.0, 2.5,
      note="its tempo-free instruments (pulse 2.1) carry 'I'm pretty sure this will just continue' 518.6 → 'running their cartels from "
           "prison' 528.5 → 'when they're in an American prison' 539.3"),
    glue("C8", 506.0, 548.0, -21.5, fi=4.0, fo=4.0, note="floor under the prison explanation and into THE DEAL"),
    # ================= C9 THE DEAL + CIA + TASK FORCE (cts07 540.4–651.5): unwritten deal → spy drones → CIA rules → task force in Arizona → 'Narco Hunters' → target package
    L("C9", "acrolith", "instruments", 541.0, 651.8, 0.2, -17, 2.0, 1.5,
      note="the spy pulse (Anthony Earls, dark/sneaking; stems used as delivered): steady 0–58 under 'an unwritten deal' 543.1 → "
           "'American forces will not come into Mexico, at least officially' 547.2 → 'Americans can find the bad guys' 553 → 'spy "
           "drones over Mexico' 567.8 → 'cameras in the sky' 571 → 'the CIA mission' 577 → 'a very different set of rules' 585.4 → "
           "'can pretty much work with anybody' 594.5; its 58–61 peak = 'lead to a bigger target' 598.4 → 'important part of the "
           "story later' 601.7; 69–74 peak = 'a new military team based in southern Arizona' 608.2 → 'joint interagency task force' "
           "613.5; its 74–77 drop = the beat before 'So let's just call it Narco Hunters' 619.1–621.6 (the joke); steady 77–111 under "
           "'Al Qaeda and ISIS' 627 → 'target package' 638.2 → 'here's your guy, here's where he sleeps' 639.6 → 'handed off to "
           "someone in Mexico' 646.9; out on 'Then we talk about the third piece' 651.5"),
    L("C9", "acrolith", "bass", 561.5, 651.8, 20.7, -21, 2.0, 1.5, note="bass from 'The US gets to work on its side of the deal' 561.6"),
    glue("C9", 644.0, 664.0),
    # ================= C10 BOATS → MADURO → EL MENCHO (cts08 651.5–711.3): boat strikes → 'another level' → Caracas → Maduro to New York → Brooklyn → the system ready → biggest catch
    L("C10", "db_cooper", "instruments", 652.0, 711.6, 57.7, -17.5, 3.0, 1.5,
      auto=[[652, -1.5], [665, -1.5], [666.0, -3], [674, -3], [674.3, 0]],
      note="the cold open's night pulse returns for the raid on Caracas (rhyme: night helicopters ↔ night helicopters): steady under "
           "'that's the boats' 655.8 → 'September 2025…small boats in the Caribbean' 656.7; −3 dB under 'controversial…close to 250 "
           "people who have been killed' 666–674 (no weight on deaths); its 80–84 build = 'the whole thing goes up to another level' "
           "674.2 → 84–94 PEAK = 'US forces fly into Caracas' 679.6 → 'Nicolas Maduro' 683 → 'fly him to New York' → 'a jail in "
           "Brooklyn' 689.8; 97–110 peak = 'a very big message to every single cartel boss' 691.4 → 'the system…was ready' 702.4; "
           "its 110–117 drop = 'Of course, we're talking about El Mencho' 709.1–711.3 (sub stinger)"),
    L("C10", "db_cooper", "bass", 673.0, 711.6, 78.7, -21, 2.0, 1.5, note="bass with the build into Caracas (no drums this time)"),
    glue("C10", 704.0, 726.0, note="glue under the credit debate's entry ('The story is crazy as to how he was caught' 711.3)"),
    # ================= C11 WHO GETS THE CREDIT (cts08 711.3–768.5): Mexican operation vs CIA 'instrumental' → State of the Union → 'do more than hand off information?'
    L("C11", "triple_fault", "instruments", 712.0, 769.0, 40.0, -19.5, 3.0, 1.0,
      note="the tempo-free crime-scene texture of the prisoner flights returns (rhyme: what the US gets out of Mexico): 'a major "
           "success' 717.4 → 'a Mexican operation with Mexican soldiers' 720 → 'the American side is telling a bit of a different "
           "story' 729.9 → 'CIA intelligence was instrumental' 738.9 → 'State of the Union' 745 → 'a big part or a small part' 751.6"),
    L("C11", "triple_fault", "full", 740.0, 769.0, 68.0, -21.5, 3.0, 1.0,
      note="its full band under 'the State of the Union address, President Trump himself' 741.7 → 'an interesting question arises' "
           "760.7 → 'What if the US wants to do more than just hand off information?' 763.7–768.5 (cut on the question)"),
    glue("C11", 762.0, 786.0, -20.5, note="drone carries the question into Chihuahua ('that was already happening in a state called Chihuahua' 768.5)"),
    # ================= C12 CHIHUAHUA + ZUANY (cts09 768.5–891.6): below Texas → El Paso → NYT → Zuany → visa cancelled → witnesses → why the CIA used him → visa back
    L("C12", "mortal_separation", "melody", 769.0, 892.0, 0.0, -19, 3.0, 1.5,
      auto=[[769, 0], [819, 0], [821, -2], [846, -2], [847.5, 0]],
      note="crime-scene suspense (Sage Oursler; the file's shape IS this segment): quiet 0–16 under 'a state called Chihuahua' "
           "772.9 → 'right below Texas and New Mexico' 773.9 → El Paso 776.2; 16–30 steady/build under 'a big New York Times "
           "investigation' 781.5 → 'a man named Guillermo Zuany' 790.6–794.1; 30–42 PEAK = 'The CIA liked him' 798.6 → 'pair CIA "
           "officers with state police units' 803.7 → 'just one problem' 809.8; its 42–51 drop = 'canceled his American visa' 812.3–"
           "818.8; 51–68 quiet (−2 dB) under the accusations 820–846 ('Four witnesses' 830.1 → 'ordered him killed' → 'Witness "
           "Protection' 839–847: respectful, no push); 68–77 build → 77–95 PEAK = 'why would the CIA work with a guy like this?' "
           "847.6 → 'bought off pretty much everyone' 857.3 → 'hard to find someone who's clean' 864; 103–108 build → 108–114 peak = "
           "'he can get us in the door' 872 → 'very cooperative' 880; its 114–122 drop = 'his US visa just came back automatically' "
           "884.4–891.4"),
    L("C12", "mortal_separation", "bass", 785.0, 892.0, 16.0, -21.5, 2.5, 1.5, auto=[[785, 0], [819, 0], [821, -3], [846, -3], [847.5, 0]]),
    L("C12", "mortal_separation", "instruments", 846.0, 892.0, 77.0, -21, 2.0, 1.5, note="instruments only under the second peak (why the CIA used him)"),
    glue("C12", 884.0, 904.0),
    # ================= C13 THE RAIDS (cts10 891.6–947.1): Zuany helps → an American trains them → CIA on raids, blending in → tablets → the safe house → the phone, the questioning
    L("C13", "acrolith", "instruments", 891.8, 947.5, 68.5, -17.5, 2.0, 2.0,
      note="the spy pulse of THE DEAL returns (rhyme: 'the CIA can work with anybody' ↔ CIA officers on Mexican raids): its 69–74 peak = "
           "'Zuany starts helping the Americans right away' 891.6 → 'introduces an American to the state police' 894.8; 74–77 drop; "
           "steady 77–111 under the training 901.3 → 'going on raids with the Mexican unit' 908 → 'blending in…jackets with the state "
           "logo' 912–921 → 'tablets' 924.0 → 'live in real time' 926.4; its 111–117 PEAK = 'on one raid on a cartel safe house' "
           "934.3–937 → 'covered the entrance with his rifle' → 'the phone they seized…questionings' 942.2; drop 117–124 → out 947.5"),
    L("C13", "acrolith", "bass", 900.0, 947.5, 76.7, -21, 2.0, 2.0),
    glue("C13", 940.0, 962.0, note="glue under 'Now the situation wasn't as rosy as it sounded' 947.1"),
    # ================= C14 THE FAILED RAIDS (cts10 947.1–976.2): not according to plan → the bar, the boss already left → tip-offs
    L("C14", "have_we_met_before", "melody", 948.0, 977.0, 40.0, -19.5, 3.0, 2.0,
      note="the wry pulse of 'walked out four times' returns (rhyme: corruption; 'You guys can figure out why'): 'not going according to "
           "plan' 951.6 → 'went to a bar to grab a cartel boss' 956.7 → 'visibly annoyed the Americans' 962 → 'somebody was tipping "
           "off the targets' 968.6 → 'this Zuany guy who's helping the Americans' 972–976"),
    L("C14", "have_we_met_before", "instruments", 948.0, 977.0, 40.0, -21.5, 3.0, 2.0),
    glue("C14", 970.0, 990.0),
    # ================= C15 THE APRIL OPERATION (cts11 976.2–1006.4): the biggest CIA operation → meth lab in the mountains → convoy of 60+ → empty lab → the night drive
    L("C15", "what_lurks_below", "instruments", 976.5, 1006.2, 17.0, -18, 3.0, 0.8,
      note="dark, sad crime-scene colour (Jon Björk): steady 17–47 under 'the biggest CIA operation…in the state of Chihuahua' 976.2 "
           "→ 'a huge meth lab deep in the mountains' 985.0 → 'Four CIA officers join a convoy of more than 60' 986.9 → 'it's empty' "
           "995.9 → 'gas tanks and tubes of chemicals' → 'the long drive back in the middle of the night' 1001.1–1006.4; out before "
           "'This is when one of the trucks just goes off a cliff' 1006.4 (the music stops — the sombre beat)"),
    L("C15", "what_lurks_below", "bass", 983.0, 1006.2, 23.5, -21.5, 2.0, 0.8, note="bass from 'The job is to find a huge meth lab' 983.7"),
    # ================= C16 THE CLIFF (cts11 1006.4–1018): one of the trucks goes off a cliff → 300 feet → everyone inside killed, two CIA officers — NEAR-SILENCE
    glue("C16", 1003.0, 1024.0, -21.0, fi=3.0, fo=4.0, offset=140.0,
         note="SOMBRE: the drone alone (no pulse, no stinger, no crash sound) for 'one of the trucks just goes off a cliff' 1006.4–1009.9 → "
              "'falls about 300 feet' → 'Killing everyone inside, including two officers' 1012.2–1015; editors: wind_pines / night "
              "ambience only"),
    # ================= C17 THE SCANDAL (cts11 1018–1078.4): Zuany's instructions → 'no clue' → political fight → resignations → AG arrested → Zuany on the run (in the US)
    L("C17", "what_lurks_below", "instruments", 1017.0, 1079.0, 46.0, -18.5, 4.0, 1.0,
      auto=[[1017, -2], [1030, -2], [1032, 0]],
      note="the same track returns after the breath, sadder (instruments only, −2 dB under 'his instructions were to get the American "
           "bodies out' 1017–1032): 'it quickly started a scandal' 1040.8 → 'they had no clue that the CIA was operating inside of "
           "Mexico' 1045–1051 → 'a political fight' 1060 → 'both had to resign…the attorney general actually got arrested' 1066–1072; "
           "its 97–104 PEAK = 'But Zuany is still on the run' 1072.1–1074.3 → 'he's here in the United States' 1076; drop 104–111 → "
           "out on 'the net closing' 1078.4"),
    L("C17", "what_lurks_below", "bass", 1050.0, 1079.0, 79.0, -21.5, 2.5, 1.0),
    glue("C17", 1072.0, 1096.0, -20.5, fi=3.0, fo=4.0, note="the drone alone under 'you can actually see the net closing around El Chapo Isidro' 1078.4–1084"),
    # ================= C18 THE NET CLOSES → THE CAPTURE (cts12 1078.4–1192.6): right-hand man → father → money people → number two → Trump–Sheinbaum → Friday → Lobos & Murciélagos → ring → arrest → plain white house
    L("C18", "honesty_matters", "instruments", 1092.0, 1199.0, 0.0, -18, 3.0, 2.5,
      note="the chase-suspense of the capture (Kikoru; G minor): steady 3–39 under 'his right hand man up in the mountains of Sinaloa' "
           "1084.9 → 'the man's father' 1090.4 → 'his money people one at a time' 1100 → 'his number two…was killed' 1103.5 → 'piece by "
           "piece' 1113.5 → 'Trump and President Sheinbaum met face to face' 1116.9; its 39–59 quiet = 'officially trade' 1123.9 → "
           "'the cartels are running Mexico' 1128.1 → 'on Friday, The mission was on' 1136.8–1138.1 → 'Revolution Day' 1143.2; "
           "59–64 build = 'pretty cool names' 1147 → 'wolves' 1154.1; steady 64–74 = 'the bats' 1159 → 'used technology to pin down' "
           "1159.9; its 74–98 PEAK = 'came in from several directions…a ring around the house' 1168.2–1173.6 → 'hit with some "
           "gunfire' 1175.6 → 'they arrested him' 1180.3 (stinger) → 'his new number two' → 'nothing special' 1186; steady 98–112 "
           "under 'a plain house with white walls in the same area where he grew up' 1188.8–1192.6"),
    L("C18", "honesty_matters", "bass", 1092.0, 1199.0, 0.0, -21.5, 3.0, 2.5),
    L("C18", "honesty_matters", "melody", 1151.0, 1192.5, 59.0, -20, 2.5, 2.0, note="melody from the build ('pretty cool names' 1147 → the wolves)"),
    L("C18", "honesty_matters", "drums", 1165.0, 1187.0, 73.0, -25, 2.0, 2.0, note="muted drums only under the raid peak"),
    glue("C18", 1186.0, 1206.0),
    # ================= C19 THE AFTERMATH (cts13 1192.6–1244.5): 'two days ago' → region goes crazy → trucks burning, roads blocked → the ballpark callback → grocery stores → clinic → Air Force plane → the 30-s video
    L("C19", "db_cooper", "instruments", 1197.0, 1244.5, 69.5, -17, 3.0, 2.5,
      note="the cold open's night pulse, third and last time — by design ('That's where the baseball game you saw at the start comes "
           "from' 1211.5): steady under 'right after the arrest, the region went crazy' 1199.5–1203.5 → 'burning trucks and blocking "
           "roads' 1203.5 → 'a gas station'; its 80–84 build → 84–94 PEAK = 'the baseball game' 1212.1 → 'thousands of people hid "
           "inside grocery stores' 1214.5 → 'armed men stormed a public clinic' 1220.5; 97–110 peak = 'loaded onto an air force plane "
           "to Mexico City' 1226–1232 → 'the government put out this video' 1233.1; its 110–117 drop = 'a 30 second long video…he "
           "keeps his head down' 1236–1243.5"),
    L("C19", "db_cooper", "bass", 1197.0, 1244.5, 69.5, -20.5, 3.0, 2.5),
    L("C19", "db_cooper", "drums", 1209.0, 1238.0, 81.5, -25, 2.0, 2.0, note="muted percussion with the callback, as in the cold open"),
    glue("C19", 1238.0, 1258.0),
    # ================= C20 THE AMBASSADOR + EXTRADITION (cts13 1244.5–1286.3): the ambassador's post → 'constant cooperation and trust' → 'keep on hunting' → charged in DC since 2012 → extradition → 92 sent
    L("C20", "timepass", "full", 1244.5, 1286.8, 15.0, -20.5, 3.0, 2.0,
      note="Washington's policy pulse returns (rhyme: US pressure → the US side's victory lap and the extradition): 'the American "
           "ambassador…a former Green Beret and CIA officer' 1244–1248 → 'results like these don't happen overnight' 1252.4 → 'constant "
           "cooperation and trust' 1255.1 → 'we're gonna keep on hunting these bosses' 1257.8 → 'charged in Washington, DC since 2012' "
           "1269.4 → 'extradited to the United States' 1276.5 → 'Mexico has already sent 90 some guys' 1278.4 → 'any special "
           "treatments' 1282.3"),
    glue("C20", 1280.0, 1300.0, note="glue into the big question ('So now we get to the big question' 1286.3)"),
    # ================= C21 IS THIS WORKING? → END (cts14 1286.3–1341.9): the question → Narcos joke → 'mostly yes' → weaker drugs, fewer deaths → bosses caught faster → Mexico doing it → not going away → 'slowed down just a bit'
    L("C21", "perplexed", "full", 1286.5, 1299.5, 66.0, -20, 2.5, 3.0,
      note="the QUESTION theme returns, once (rhyme: 'And is this actually working?' 115.7 ↔ 'Is this working?' 1288.5 (riser "
           "stinger) → 'a great new season of Narcos on Netflix' 1292–1295.6 → 'But is this actually working?' 1296.4)"),
    L("C21", "the_determination", "melody", 1297.0, 1336.5, 52.0, -19.5, 3.0, 3.5,
      auto=[[1297, 0], [1322.5, 0], [1324.5, -3], [1336.5, -3]],
      note="reflective, hopeful but unresolved (Anna Dager & Hanna Ekström; Σ stems = full, −9.7 dB): steady 52–101 under 'for the "
           "first time in a long time, the answer is mostly yes' 1299–1303.2 → 'The drugs…are weaker…fewer Americans are dying' "
           "1305.2 → 'caught or killed faster' 1311.8 → 'Mexico is actually doing the catching' 1318.1; −3 dB from 'all this doesn't "
           "mean cartels are going away' 1323.8 → 'twelve billion dollars a year' 1329.2 → 'a long line of guys who want the top job'; "
           "melody leaves under 'I'm sure the drug smuggling will continue' 1334.4"),
    L("C21", "the_determination", "bass", 1301.0, LEN, 56.0, -21.5, 3.0, 5.0,
      auto=[[1301, 0], [1334, 0], [1338, -3], [LEN, -6]],
      note="bass + drone to the end: 'at least for now it seems like it has slowed down just a bit' 1336.6–1341.5 — no cadence, no stinger"),
    glue("C21", 1318.0, LEN, -20.5, fi=4.0, fo=4.5, offset=182.0, note="drone floor to the end (unresolved)"),
]

stingers = [
    dict(file="boom_sub_bass_clean_01", t=67.35, sync="loudest", rel_lu=-31,
         note="COLD OPEN payoff: '…with the help from the United STATES' (felt, not heard)"),
    dict(file="swell_reverse_timpani_cymbal", t=116.07, sync="loudest", rel_lu=-30,
         note="TITLE QUESTION: swell peaks on 'And is this actually WORKING?' (the title card)"),
    dict(file="boom_cinematic_deep", t=682.73, sync="loudest", rel_lu=-30,
         note="MADURO: '…capture the country's PRESIDENT, Nicolas Maduro'"),
    dict(file="boom_sub_bass_clean_01", t=710.73, sync="loudest", rel_lu=-31,
         note="'Of course, we're talking about El MENCHO' (felt only — a death, no triumph)"),
    dict(file="boom_dark_cinematic_low_hit", t=1180.31, sync="loudest", rel_lu=-29,
         note="THE CAPTURE: 'they ARRESTED him'"),
    dict(file="riser_reverse_cymbal_short", t=1289.11, sync="loudest", rel_lu=-31,
         note="THE QUESTION returns: 'Is this WORKING?'"),
]

marker_edits = []   # phase 2: fix editors' markers here ({t, type, action: drop|retype, to, note})

sheet = dict(
    length=LEN,
    doc="Layered Epidemic bed for 'US vs Cartels' (Searching Lessons). Master seconds of project/cartels/media/vo_ct.wav "
        "(= vo_ct.mp3). Generated by project/cartels/gen/make_cuesheet.py — edit there. Key family G minor (+ Bb major). Cues C1–C21 = "
        "SOUND_PLAN.md §2 (from SEGMENTS.md §3). Binding music limits (MANUAL §10.8): bed VO − 22 LU, vo_duck gap 20 / gap_fast 18 / "
        "ceiling 20, no pause lifts, sfx_limit 14.",
    # ---- BINDING (MANUAL §0, §10.8 "Music limits", Krish 2026-11-13) — never loosen
    bed_lu_under_vo=22.0,
    pause_lift_db=0.0,
    vo_duck=dict(gap=20.0, gap_fast=18.0, ceiling=20.0, margin=0.7, attack=0.05, release=0.4, max_cut=-30.0, passes=3),
    sfx_limit=dict(gap=14.0, margin=1.0),
    layers=layers, stingers=stingers, ducks=[], bleeps=[], marker_edits=marker_edits)

assert sheet["bed_lu_under_vo"] >= 22 and sheet["vo_duck"]["gap"] >= 20 and sheet["vo_duck"]["gap_fast"] >= 18 \
    and sheet["vo_duck"]["ceiling"] >= 20 and sheet["sfx_limit"]["gap"] >= 14 and sheet["pause_lift_db"] == 0, "binding music limits loosened"
# sanity: every layer reads inside its file (ANALYSIS.json durations), ends ≤ LEN, starts < ends
_ana = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "assets/audio/epidemic/ANALYSIS.json")))
for l in layers:
    assert 0 <= l["start"] < l["end"] <= LEN + 1e-6, l
    dur = _ana[l["track"]]["stems"][l["stem"]]["dur_s"]
    assert l["offset"] + (l["end"] - l["start"]) <= dur + 1.0, (l["cue"], l["track"], l["stem"], l["offset"], dur)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "music_cuesheet.json")
json.dump(sheet, open(out, "w"), indent=1)
print("wrote", os.path.normpath(out), len(layers), "layers,", len(stingers), "stingers")
