import sys; sys.path.insert(0, "project/c1/gen")
from common import *; from beats_data import B
ACTS = [
 ("I. Cold open — Terman's quote and the claim", 0.00, 46.13, "C1B001–C1B008", "quote over an empty valley → attribution FRED TERMAN 1974 → 'greatest feat' → built Silicon Valley → the world wants to copy it", "reflective, grand, then proud", "soft textural pad from the intro's flash; first pulse under 'father of Silicon Valley' 16.08; lift on 'copy it' 44.93"),
 ("II. The trillion-dollar West", 46.13, 78.77, "C1B009–C1B014", "October 2026: 12 US trillion-dollar companies, 11 west of the Mississippi, Eli Lilly the holdout, apples vs oranges", "data-driven, confident, a little playful", "pulse + light percussion stem; hits on 12 (52.45), 11 (65.41); playful pluck on 'apples/oranges'"),
 ("III. A century ago — the lopsided East and the brain drain", 78.77, 143.72, "C1B015–C1B024", "rewind 100 years: 90% of GDP in the East; Silicon Valley changed it; 1920s Berkeley/Stanford grads had to go East to NY/NJ/MA, Bell Labs, GE; brain drain", "nostalgic → slightly tense", "drop the pulse on 'rewind' 79.25 (tape-rewind riser), sepia drone + melodic layer; tension texture under 'brain drain' 138.52"),
 ("IV. Herbert Hoover at Stanford (with the Twitter aside)", 143.72, 277.60, "C1B025–C1B048", "Terman teased; Hoover = first class 1891, campus under construction; joke on Twitter (no-try guys get golden opportunities); failed exams, Quaker, admitted; wife; Commerce → White House; runs Stanford's board; money; trusted people; 1925 business school; his 'don't go east' argument, first in the West", "storytelling, wry humour in the aside, then purposeful", "mid-tempo storytelling bed; strip to a light playful layer 176.67–208.43 (aside, no hits on the punchline); stinger on 'admitted' 215.15; warm build through 250–277"),
 ("V. Enter Frederick Terman", 277.60, 357.32, "C1B049–C1B062", "the father of Silicon Valley named; born 1900; Lewis Terman & the IQ test; Stanford → MIT → Stanford radio engineering; ten years of heartbreak; Hoover → president → Depression; students leaving East", "reveal → personal → melancholy", "title stinger on 'Frederick' 284.63; light/playful under 1900/2000; melancholy pad under 'breaking his heart' 330.87 and 348.44"),
 ("VI. Hewlett & Packard and Terman's plan", 357.32, 436.03, "C1B063–C1B079", "1938: two students too good to lose — Bill Hewlett & David Packard (HP); Packard at GE for $100/month, Hewlett about to go; Terman's plan: start any company in Palo Alto; Hewlett's thesis = audio oscillator; fellowship + Terman's own money", "rising hope, momentum", "momentum layer enters on 'Bill Hewlett' 378.28; reveal hit on 'HP' 384.20; build under the plan"),
 ("VII. HP is born — Disney, the coin flip, the garage, the oscillator", 436.03, 516.54, "C1B080–C1B094", "build the oscillator; list of 25 companies; connections; Disney first buyer; coin flip → Hewlett-Packard; HP everything; the garage; what an audio oscillator does; B2B test equipment", "playful, delightful, explanatory", "pizz/marimba-like playful layer for the coin flip; warm swell on the garage 478.14; light ticking texture under the oscillator explanation"),
 ("VIII. World War II and federal money", 516.54, 591.62, "C1B095–C1B105", "war interrupts; Terman runs the secret 800-person Harvard radar-jamming lab; back as Dean of Engineering; Washington connections pay handsomely; convinces the military to put research labs at Stanford; federal money flows in", "dark/urgent (war) → triumphant", "cut the bed to a low drone + pulse on 'the war' 519.10; dark pulses (Formations family) under the secret lab; release on 'Dean of Engineering' 550.57; triumphant build into 'federal money' 586.90"),
 ("IX. The catch (hand-off to c2)", 591.62, 602.86, "C1B106–C1B107", "even with the strongest government behind you, Stanford can't be best at everything", "reflective pivot, open question", "thin to a single sustained layer; leave it hanging into c2"),
]
SLIPS = [
 ("28.88–33.57", "C1B006", "“He. could arguably be put claim to building the Silicon Valley.” (garbled ‘can arguably lay claim to’)", "no text on the garbled clause; on screen only `building` + `Silicon Valley`"),
 ("67.41", "C1B012", "“west of the Mississippi River” (lowercase ‘west’)", "label WEST — fine"),
 ("71.81", "C1B013", "ASR “drop company” = **drug company**", "on screen `drug company`"),
 ("85.49", "C1B015", "“basically like very lopsided”", "on screen `lopsided` only"),
 ("92.85–93.49", "C1B016", "“on the on the coast” (repeat)", "no text on the repeat; `coast` once"),
 ("119.80–125.48", "C1B021", "“leave Western United States” (no article)", "label the region, don't caption the phrase"),
 ("133.72", "C1B023", "ASR “Bell Laps” = **Bell Labs**", "`Bell Labs`"),
 ("135.88–137.32", "C1B024", "“They were basically it was kind of a brain drain” (restart)", "only BRAIN DRAIN"),
 ("142.76", "C1B024", "“leaving West.” = leaving the West (going East)", "arrows/people move **East** (out of the West); never caption ‘leaving West’ alone"),
 ("148.12, 152.04, 260.48, 285.19", "C1B025/26/47/50", "ASR “Fred Turner / Turner / Frederick Turner” = **Terman**", "`Fred Terman`, `Frederick Terman`"),
 ("163.55", "C1B027", "ASR “Harbert Hoover” = **Herbert Hoover**", "`Herbert Hoover`"),
 ("170.35–171.47", "C1B028", "“in 1980, 1891.” (self-correction)", "show **1891** only, never 1980"),
 ("176.67–208.43", "C1B029–C1B034", "the Twitter-joke aside, loose grammar (“some flip switches”, “who was hiring people…”)", "visuals follow the joke literally; only key words on screen (`joke`, `Twitter`, `golden opportunity`, `achieved nothing`, `meme`); no tweet text quoting him beyond his own words"),
 ("224.08–226.00", "C1B039", "“He, you know, became uh became like”", "no text until `very successful`"),
 ("229.84", "C1B040", "“By the 20s” = 1920s", "on screen `the 20s` (his words) — not ‘1920s’"),
 ("235.52–236.88", "C1B041", "“board of trustee” = Board of Trustees", "`Board of Trustees`"),
 ("240.80–241.04, 246.88–247.44", "C1B042–43", "“he he”, “he he he”", "no text"),
 ("254.08–255.20", "C1B045", "“Stanford's business graduate program” = Stanford Graduate School of Business (founded 1925)", "kicker `business graduate program` (his words) + small object label `Stanford Graduate School of Business` on the building/letterhead only"),
 ("258.96–261.52", "C1B046", "“the argument we're gonna see for Turner make very soon” (= see Terman make)", "small `Terman` foreshadow only"),
 ("265.20", "C1B047", "ASR “going yeast” = going **east**", "`east`"),
 ("274.96–275.60", "C1B048", "“this was who were who first started saying this” (= he was the one who first…)", "only `first` + `the West`"),
 ("286.47", "C1B050", "“born in the 1900s” — he means the year **1900** (“very lucky year… like being born in 2000”)", "on screen `1900` (the year he describes); not a fact-check, it's the meaning of his own sentence"),
 ("290.15–290.47", "C1B051", "“like my brother” (personal aside)", "no text on ‘brother’ — a tiny `2000` only"),
 ("291.19–296.47", "C1B052", "“Where very easy to calculate how old you are. But uh yeah.”", "light visual, `easy` only; nothing on ‘But uh yeah’"),
 ("296.47–296.95", "C1B053", "“He he he's”", "—"),
 ("300.39", "C1B054", "ASR “Louis Terman” = **Lewis Terman**", "`Lewis Terman`"),
 ("301.59–301.91", "C1B054", "“was a s a Stanford psychologist”", "`Stanford psychologist`"),
 ("306.39–307.11", "C1B055", "“that you have ha you and I have probably taken”", "`you and I` optional; no text on the restart"),
 ("311.27–312.55", "C1B056", "“a very, very powerful, powerful company.” — means **family**", "**never caption ‘company’**; show `very powerful` over the family"),
 ("314.63", "C1B057", "ASR “Turnman” = **Terman**", "—"),
 ("318.79–321.83", "C1B058", "“went to East … and MIT” (= at MIT)", "labels `East`, `doctorate`, `MIT`"),
 ("332.95–337.35", "C1B060", "ASR “Hour saw” = **Hoover** saw; “who are very quickly becomes the president”", "`Hoover` → `president`"),
 ("340.23–342.44", "C1B061", "“where people. blame on Herbert Hoover for some reason”", "`Great Depression` + `blame` only; no editorial text"),
 ("357.88–358.68", "C1B063", "“nineteen thirty eight” (ASR spelled out)", "`1938`"),
 ("359.00–361.32", "C1B063", "“we're almost twelve years ahead in our story” (from ~1925/26)", "small `12 years ahead` label (his words) — no start year printed"),
 ("365.56–367.96", "C1B064", "“he wasn't willing to get them go to East”", "arrow East blocked; `East` label only"),
 ("373.32–376.68", "C1B065", "“especially if you're I think I'm watching a story about Silicon Valley” (garbled)", "no text on the garble; `Silicon Valley` tag on 376.12 only"),
 ("377.32–378.04", "C1B066", "“The students' name were”", "—"),
 ("391.16", "C1B069", "“around hundred dollars a month” (no ‘a’)", "`$100 a month` (yellow key number of the scene)"),
 ("404.35–404.83", "C1B073", "“here here in California”", "—"),
 ("423.63–426.51", "C1B076–77", "“some money, some money, some money, some money” (repeats ×4)", "playful: one coin stack per ‘some money’ (visual rhythm), text `some money` **once**"),
 ("443.47–445.87", "C1B081", "“on top of that, on top of that”", "—"),
 ("455.95–458.94", "C1B083", "“the company name is apparently gonna be. Uh decided by a coin flip.”", "`coin flip` only"),
 ("466.70", "C1B084", "ASR “NAS name” (= ‘last name’, likely). **Verify by ear.**", "no text on it"),
 ("481.82–487.90", "C1B087–88", "“the first company in Silicon Valley, which again, we don't have Silicon Valley yet”", "SILICON VALLEY with `yet` struck / `not yet` (his meaning)"),
 ("505.50–506.14", "C1B093", "“So it was it was”", "—"),
 ("513.50–515.74", "C1B094", "“creating test uh sound products”", "`sound products`"),
 ("521.61–522.41", "C1B095", "ASR “World War 2.” → **World War II**", "`World War II`"),
 ("522.97", "C1B096", "ASR “Kerman” = **Terman**", "—"),
 ("527.37–528.17", "C1B096", "“radio stuff”", "`radio`"),
 ("533.45–533.69", "C1B097", "“in Harvard” (= at Harvard)", "`Harvard`"),
 ("545.85–547.29", "C1B100", "“all throughout, all throughout World War II”", "—"),
 ("563.21–563.61", "C1B103", "“they're gonna pay very handsomely” (deliberate repeat for emphasis)", "the money visual intensifies on the repeat; no second text"),
 ("564.89–566.01", "C1B104", "“So he's like he convinces”", "—"),
 ("568.25–570.17", "C1B104", "“Did they have Pentagon back then? I don't know if they did,” (aside, unsure)", "Pentagon shown with a hand-drawn `?` — no answer, no date"),
 ("583.14–584.10", "C1B105", "“ahead, ahead, ahead.” (rhetorical repeat)", "three arrows, one per word — allowed: it is the rhythm of his line"),
 ("584.82–585.06", "C1B106", "“So that that solved”", "—"),
 ("597.94–599.46", "C1B107", "“Terman very quickly this, or maybe he knew this already, is like” (missing verb ‘realises’)", "never caption the gap; show `cannot be best at everything` from 600.98"),
]
ENT = [
 ("PERSON", "Frederick (Fred) Terman", "**West/Stanford accent** (vermilion). ASR Turner/Turnman/Kerman. 'father of Silicon Valley'", "C1B003, C1B025–26, C1B046, C1B049–C1B064, C1B074–C1B082, C1B096–C1B107", "14.32 (Fred), 14.88 (Terman), 147.64, 151.64, 260.48, 284.63 (Frederick), 314.63, 345.32, 396.28, 419.87, 522.97, 596.02"),
 ("PERSON", "Herbert Hoover", "neutral ink/bone (he's Stanford's side → small vermilion Stanford tag next to him, never a red portrait duotone — red is TSMC/Chang later); ASR 'Harbert', 'Hour'", "C1B026–C1B048, C1B060–61", "163.55 (Harbert), 165.31, 208.83, 333.11 (Hour), 341.40"),
 ("PERSON", "Lewis Terman", "father; ASR 'Louis'", "C1B054–56", "300.39"),
 ("PERSON", "Bill (William) Hewlett", "neutral, warm sepia; pair with Packard", "C1B066–C1B084", "378.60, 393.24, 411.23, 464.22"),
 ("PERSON", "David Packard", "neutral", "C1B066–C1B084", "379.96, 386.92, 465.42"),
 ("PERSON", "Hoover's wife (Lou Henry Hoover)", "**unnamed in VO** — show 'his wife' only; her name may appear as a tiny photo caption", "C1B038", "223.52 (wife)"),
 ("PERSON", "'some guy' (Twitter joke)", "generic — illustration, never a real person", "C1B030–C1B033", "183.63 (guy)"),
 ("PERSON", "'my brother' (narrator's)", "no visual of a real person", "C1B051", "290.47"),
 ("PERSON", "military / 'they' / the government", "neutral", "C1B097, C1B104–107", "530.49, 567.05, 571.45, 594.10"),
 ("INSTITUTION", "Stanford University", "**West accent (vermilion)** — ASR fine; Stanford's business graduate program = GSB (1925); Board of Trustees", "throughout", "112.20, 116.92, 118.92, 156.75, 169.47, 212.11, 215.95, 217.55, 235.52, 243.44, 253.12, 301.99, 317.91, 323.03, 549.77, 575.77, 590.42, 600.18"),
 ("INSTITUTION", "UC Berkeley", "neutral (gold/blue school colours NOT used — palette rule)", "C1B019–21", "110.28, 117.88"),
 ("INSTITUTION", "MIT", "**East (navy)**", "C1B058", "321.83"),
 ("INSTITUTION", "Harvard (secret lab of ~800 = Radio Research Laboratory, unnamed in VO)", "East (navy); don't print 'Radio Research Laboratory' as a title (not said) — a small object label on a document is OK", "C1B097", "533.69"),
 ("COMPANY", "12 trillion-dollar US companies (Oct 2026)", "data list reused: example-docs/analysis/BEATS.md §6", "C1B010–12", "52.45 (12), 55.41 (trillion)"),
 ("COMPANY", "Eli Lilly", "**East (navy)**, the holdout", "C1B013", "70.37"),
 ("COMPANY", "Bell Labs", "East", "C1B023", "133.32"),
 ("COMPANY", "General Electric", "East", "C1B023, C1B068", "134.28, 389.24"),
 ("COMPANY", "HP (Hewlett-Packard)", "West (vermilion) — the first Silicon Valley company; logo in its true form, then tinted", "C1B067, C1B083–C1B094", "384.20, 471.42, 472.46, 475.50"),
 ("COMPANY", "Disney", "neutral; first buyer/client", "C1B082, C1B089", "454.75, 488.62"),
 ("COMPANY", "'crazy hedge fund' / 'world leading company'", "generic", "C1B032–33", "196.91, 199.39"),
 ("PLACE", "Silicon Valley", "", "many", "3.68, 16.80, 33.01, 95.16, 102.28, 280.39, 376.12, 480.62, 483.26, 485.02"),
 ("PLACE", "the West / California / Western United States", "vermilion", "C1B007, C1B019, C1B021, C1B048, C1B073, C1B105", "37.73, 108.12, 124.04, 142.76, 277.04, 405.39, 577.53"),
 ("PLACE", "the East / East coast / New York, New Jersey, Massachusetts", "navy", "C1B016, C1B022, C1B047, C1B058, C1B062, C1B064", "90.77, 92.29, 93.65, 127.08, 127.56, 128.04, 128.76, 265.20, 319.35, 353.96, 367.96"),
 ("PLACE", "Mississippi River", "", "C1B012", "67.41"),
 ("PLACE", "Indianapolis", "", "C1B013", "72.77"),
 ("PLACE", "United States", "", "C1B010, C1B027, C1B098", "53.65, 162.75, 538.57"),
 ("PLACE", "Palo Alto", "", "C1B073", "406.91"),
 ("PLACE", "the garage (367 Addison Ave, Palo Alto — not named in VO)", "2.5D", "C1B087–88", "478.14, 487.90"),
 ("PLACE", "Washington", "", "C1B102", "555.45"),
 ("PLACE", "the Pentagon (aside)", "", "C1B104", "568.65"),
 ("PLACE", "White House", "", "C1B040", "233.04"),
 ("PLACE", "the world / countries around the world", "", "C1B002, C1B008, C1B048, C1B106", "8.16, 11.60, 42.61, 43.97, 273.92, 594.82"),
 ("PLATFORM", "Twitter", "typeset card, no real handles", "C1B029", "179.15"),
 ("DATE", "1974", "Terman's quote", "C1B004", "20.24"),
 ("DATE", "October 2026", "recording date", "C1B009", "50.93, 51.41"),
 ("DATE", "'a hundred years ago'", "don't print a year other than via the rewind counter 2026→1926? — he says 'a hundred years'; show `100 years` (count) only", "C1B015", "80.21"),
 ("DATE", "1920s / 'the 20s'", "", "C1B018, C1B040", "104.68, 229.84"),
 ("DATE", "1891", "**yellow key number** of its scene (callback to the approved 1891 sample)", "C1B028", "171.47"),
 ("DATE", "1925", "", "C1B045", "251.44"),
 ("DATE", "1900 / 2000", "", "C1B050–51", "286.47, 289.51"),
 ("DATE", "1938", "", "C1B063", "357.88"),
 ("DATE", "World War II", "", "C1B095, C1B100", "521.61, 547.29"),
 ("NUMBER", "12 companies / 11 companies / one holdout", "12 = yellow hero number (C1B010)", "C1B010–13", "52.45, 60.93, 64.85, 65.41, 69.01"),
 ("NUMBER", "$1 trillion", "", "C1B010", "55.41"),
 ("NUMBER", "90% of US GDP", "yellow key number of its scene", "C1B016", "87.33"),
 ("NUMBER", "24 years old", "", "C1B057", "313.43"),
 ("NUMBER", "first ten years", "", "C1B059, C1B062", "326.31, 347.48"),
 ("NUMBER", "twelve years ahead", "", "C1B063", "359.64"),
 ("NUMBER", "two students", "", "C1B064", "362.36"),
 ("NUMBER", "$100 a month", "yellow key number of its scene", "C1B069", "391.16"),
 ("NUMBER", "25 companies", "yellow key number of its scene", "C1B080", "440.03"),
 ("NUMBER", "about 800 people", "yellow key number of its scene", "C1B097", "532.57"),
 ("OBJECT", "the IQ test", "Lewis Terman, *The Measurement of Intelligence* (1916, Stanford–Binet)", "C1B055", "305.11"),
 ("OBJECT", "radio engineering", "Terman's textbook *Radio Engineering* (1932) is the true image", "C1B058, C1B096", "324.07, 527.37"),
 ("OBJECT", "Hewlett's thesis", "", "C1B074", "413.39"),
 ("OBJECT", "audio oscillator (HP 200A)", "", "C1B075, C1B080, C1B089–C1B094", "416.27, 437.79, 490.22"),
 ("OBJECT", "fellowship / money / his own money / funding", "", "C1B076–78", "421.95, 423.87, 430.67, 434.43"),
 ("OBJECT", "list of 25 companies", "", "C1B080", "439.63"),
 ("OBJECT", "coin (flip)", "", "C1B083, C1B085", "460.38, 470.14"),
 ("OBJECT", "HP computers / printers", "modern product photos (fair use)", "C1B085", "471.42, 472.46"),
 ("OBJECT", "enemy radars / jamming", "", "C1B098–99", "540.01, 541.21"),
 ("OBJECT", "research labs", "", "C1B105–106", "572.89, 589.38"),
 ("EVENT", "Great Depression", "", "C1B061", "338.95"),
 ("EVENT", "brain drain", "", "C1B024", "138.52"),
 ("CONCEPT", "B2B", "", "C1B093", "507.18"),
 ("CONCEPT", "federal money", "", "C1B106", "586.90"),
]
o = []
P = o.append
P("# BEATS — “Taiwan: the chip rivalry” (Searching Lessons), CHUNK c1 (local 0.00–602.86 = full audio 275.06–877.88)\n")
P("Source: `vo_c1.mp3` (= `input/Final Full Audio.mp3` 275.06–877.88, stream copy), word timings `transcript_c1.json` (Parakeet,")
P(f"{len(W)} words, w838 “When” @ 0.00 → w2591 “everything.” 602.18–602.82). **All times are LOCAL c1 seconds** (add 275.06 for the")
P("full audio). Word times = word **start**, 2 decimals. Prepared 2026-10-31 by the story analyst (generator: `project/c1/gen/gen_beats.py`).")
P("Binding rules: `project/LONGFORM.md`, MANUAL §10 (§10.9 long-form rules override older sections), `project/intro/BRIEF.md`.")
P("No face cam in this chunk (§10.9). No fact-checking: on screen = his words; only names are spelled correctly.\n")
P("This chunk retells the story of the earlier approved 10-minute edit (`example-docs/analysis/BEATS.md`, beats B001–B085) with a NEW")
P("voiceover: the words, order and emphasis differ (new: the 1974 Terman quote cold-open, the Twitter-joke aside, the coin flip, Disney,")
P("the garage, the oscillator explanation, WWII/Harvard, Washington money). Old beats are cross-referenced in §7 where the content matches.\n")
P("**Contents** 1 Beat sheet · 2 ASR fixes + narrator slips · 3 Entities · 4 Key-word cues · 5 Data · 6 Acts & tone · 7 Visual must show\n")
durs = []
rows = []
for i, b in enumerate(B):
    s = b[0]; e = B[i+1][0] if i+1 < len(B) else END
    durs.append(e - s)
    rows.append((f"C1B{i+1:03d}", s, e, words(s, e), b[1]))
P(f"Beat length: {len(B)} beats, median {sorted(durs)[len(durs)//2]:.1f} s, range {min(durs):.1f}–{max(durs):.1f} s. Contiguous 0.00 → {END}, every boundary on a word start.\n")
P("## 1. Beat sheet (corrected transcript)\n")
P("Words verbatim; ASR name fixes in **bold**; slips kept so text matches the audio (see §2b).\n")
P("| id | start | end | dur | spoken words (corrected) | viewer must understand |\n|---|---|---|---|---|---|")
for r in rows:
    P(f"| {r[0]} | {r[1]:.2f} | {r[2]:.2f} | {r[2]-r[1]:.1f} | {r[3]} | {r[4]} |")
P("\n## 2. ASR corrections and narrator slips\n")
P("**Rule (Krish):** names/places always spelled correctly on screen; everything else = exactly what he says. Cross-checked")
P("against the old edit's list (`example-docs/analysis/BEATS.md` §2a: Herbert Hoover, Frederick Terman, Lewis Terman, Vannevar Bush,")
P("Packard, AT&T, Board of Trustees). Vannevar Bush and AT&T are **not mentioned in c1**.\n")
P("### 2a. Name / word fixes (use in every on-screen text)\n")
P("| time | beat | ASR heard | on screen | note |\n|---|---|---|---|---|")
for r in [
 ("14.32–14.88", "C1B003", "Fred Terman", "**Fred Terman**", "correct; first mention (quote attribution)"),
 ("147.64–148.12", "C1B025", "Fred Turner", "**Fred Terman**", ""),
 ("151.64–152.04", "C1B026", "Fred Turner", "**Fred Terman**", ""),
 ("163.55", "C1B027", "Harbert Hoover", "**Herbert Hoover**", "reveal word"),
 ("170.35 / 171.47", "C1B028", "1980, 1891", "**1891**", "self-correction"),
 ("236.88", "C1B041", "board of trustee", "**Board of Trustees**", ""),
 ("260.48", "C1B046", "Turner", "**Terman**", ""),
 ("265.20", "C1B047", "yeast", "**east**", ""),
 ("284.63–285.19", "C1B050", "Frederick Turner", "**Frederick Terman**", "reveal (hero halate)"),
 ("300.39", "C1B054", "Louis Terman", "**Lewis Terman**", ""),
 ("314.63", "C1B057", "Turnman", "**Terman**", ""),
 ("333.11", "C1B060", "Hour", "**Hoover**", ""),
 ("341.40", "C1B061", "Herbert Hoover", "**Herbert Hoover**", "correct here"),
 ("71.81", "C1B013", "drop company", "**drug company**", "Eli Lilly"),
 ("133.72", "C1B023", "Bell Laps", "**Bell Labs**", ""),
 ("378.28–379.96", "C1B066", "Bill Hewlett and David Packard", "**Bill Hewlett**, **David Packard**", "correct"),
 ("384.20", "C1B067", "HP", "**HP** (Hewlett-Packard)", ""),
 ("416.27–416.75", "C1B075", "audio oscillator", "**audio oscillator**", "HP 200A (object label only)"),
 ("466.70", "C1B084", "NAS name", "— (likely “last name”)", "verify by ear; no text"),
 ("507.18", "C1B093", "B2B", "**B2B**", ""),
 ("521.61–522.41", "C1B095", "World War 2.", "**World War II**", ""),
 ("522.97", "C1B096", "Kerman", "**Terman**", ""),
 ("533.69", "C1B097", "Harvard", "**Harvard**", "correct"),
 ("550.57–551.21", "C1B101", "Dean of Engineering", "**Dean of Engineering**", ""),
 ("254.08–255.20", "C1B045", "business graduate program", "his words; object label **Stanford Graduate School of Business**", ""),
]:
    P("| " + " | ".join(r) + " |")
P("\n### 2b. Narrator slips / repeats / asides — keep in the audio, never emphasise on screen\n")
P("| time | beat | slip | handling |\n|---|---|---|---|")
for s in SLIPS: P("| " + " | ".join(s) + " |")
P("\nNo ‘uh/um’ tokens except 225.60, 295.19, 458.94, 514.70 (all inside slips above).\n")
P("## 3. Entities (beat ids + key-word timestamps, LOCAL s)\n")
P("Palette mapping for the Silicon Valley part (planner's decision, see EDIT_NOTES §0): **vermilion = the West / Stanford / Terman's")
P("Silicon Valley** (the `--west` token), **navy = the East** (the `--east` token: NY, NJ, MA, MIT, Harvard, Bell Labs, GE, Eli Lilly),")
P("yellow = highlighter + one key number. Celadon (Taiwan) is not needed in c1. People are neutral (sepia/ink) — only their tags carry")
P("the West/East colour.\n")
P("| type | entity | note | beats | key-word timestamps |\n|---|---|---|---|---|")
for e in ENT: P("| " + " | ".join(e) + " |")
P("\n## 4. Key word cues (on-screen emphasis, exact word start times)\n")
P("Text lands 0–120 ms **before** the listed time (default −0.06 s). CAPS = primary cue. Times = ASR token start (validated against")
P("`transcript_c1.json` by the generator).\n")
P("| id | cues (word start → on-screen word) |\n|---|---|")
for i, b in enumerate(B):
    P(f"| C1B{i+1:03d} | " + " · ".join(f"{w} @ **{t:.2f}**" for w, t in b[2]) + " |")
P("\n## 5. Data the story needs\n")
P("- **12 US companies worth > $1 trillion, October 2026** (C1B010–C1B013): reuse the dated list in")
P("  `example-docs/analysis/BEATS.md` §6 (companiesmarketcap.com, fetched 2026-10-29: NVIDIA, Apple, Microsoft, Alphabet, Amazon,")
P("  SpaceX, Broadcom, Meta, Tesla, **Eli Lilly (Indianapolis — the only one east of the Mississippi)**, Berkshire Hathaway, Micron).")
P("  The narration matches it (12 → 11 west + Eli Lilly). Source line on screen: `Market value, Oct 2026 · companiesmarketcap.com`.")
P("  If the editor builds after a market move, keep the narrated count (12/11/1) — the VO is the truth on screen.")
P("- Everything else is narrated without data (90 %, $100/month, 25 companies, ~800 people, 24, ten years, 1938, 1891, 1925, 1974,")
P("  1900/2000). Charts without narrated values are drawn as shapes only (no axis numbers).\n")
P("## 6. Story structure, acts and tone\n")
P("| act | time range (local) | beats | content | emotional tone | music / pacing guidance |\n|---|---|---|---|---|---|")
for a in ACTS: P(f"| {a[0]} | {a[1]:.2f}–{a[2]:.2f} | {a[3]} | {a[4]} | {a[5]} | {a[6]} |")
P("\nPacing: Acts II and VII are the lightest (data + playful); IV's Twitter aside (176.67–208.43, 32 s) must stay literal and quick")
P("(5–6 short shots) so the story doesn't stall; VIII is the darkest. Music family = the intro's Epidemic layered bed (`project/intro/music_cuesheet.json`).\n")
P("## 7. “Visual must show” — one line per beat\n")
P("Every visual matches the exact words under it (MANUAL §10.1.3). Old-edit beat cross-refs (`example-docs`) where the same content exists.\n")
OLD = {1:"—",3:"—",10:"B004",11:"B004–05",12:"B006",13:"B007",14:"B008",15:"B009",16:"B010",17:"B011",19:"B012–13",20:"B012–13",21:"B014",22:"B015",23:"B016",24:"B018",
 27:"B019",28:"B020–21",35:"B022",36:"B023–24",38:"B026",40:"B027–28",41:"B029",45:"B038",47:"B039",48:"B040",49:"B041",50:"B042",51:"B043",
 54:"B044",55:"B045",57:"B046",58:"B047–49",59:"B070",62:"B073",64:"B074",66:"B075",68:"B077",71:"B078",73:"B079",74:"B080",75:"B081",76:"B084–85",63:"B074",77:"B084–85",87:"B079–80 (garage)",89:"B081–82",92:"B082"}
P("| id | time | old beat (approx.) | visual must show |\n|---|---|---|---|")
for i, b in enumerate(B):
    s = b[0]; e = B[i+1][0] if i+1 < len(B) else END
    P(f"| C1B{i+1:03d} | {s:.2f}–{e:.2f} | {OLD.get(i+1,'new')} | {b[3]} |")
open("project/c1/analysis/BEATS.md", "w").write("\n".join(o) + "\n")
print("ok", len(B))
