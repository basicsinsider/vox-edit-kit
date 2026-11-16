# EDIT NOTES — the lead's shot plan, all segments (master seconds; boundaries on sentence starts from `script_clean.txt`)

How to read: each row = one scene. `FC` = Sam on camera (framing W wide 1.0 / M medium 1.25 / C close 1.5). `ref:` = the inspo
reference that scene is REBUILT from (`references/inspo-assets/img/<id>.*`, MANUAL §6.1 — structure only, our fonts/palette/motion).
Times are sentence starts; snap every cut and cue to exact word starts in `transcript_nv.json`. Editors refine this into
`EDIT_NOTES_nvsNN.md` (add exact cues, transitions, SFX) and may split/merge scenes for craft, but: keep the picture↔words match, the
reference ids, the motifs, the face-cam share, and never add narration captions. "RESEARCH" = take the true item from RESEARCH.md /
`assets/nvidia/shared/*`; if it isn't there, use the fallback given — never fabricate.

## nvs01 — 0.000–109.250 · cold open + the Hong Kong / Shenzhen video (intro: no Sam 0–10 s, then 1–2 s pops)
| # | time | words (gist) | picture — why it matches | ground / effect / ref |
|---|---|---|---|---|
| 001 | 0.00–2.80 | "Is the chip ban actually working?" | Hero title built on the question: an NVIDIA GPU (cutout, volt rim light) on night, an ice hand-drawn line slamming across it; title "IS THE CHIP BAN WORKING?" word by word (cold-open caption line — allowed) | night; halate on the title only; ref: `ast_290885ff9bcc4687` (title card with banner) |
| 002 | 2.80–11.12 | "the government really cares about people who are breaking the chip ban" | Commerce Dept / DOJ building + real enforcement headlines stacking (RESEARCH: smuggling arrests) — the government caring = prosecutions | Vox layered background #10 + article cards; ref: `ast_2b0b05b6a7bd471a` (article header, torn paper) |
| 003 | 11.12–20.96 | "NVIDIA CEO Jensen Huang just had to step down… alleged Chinese spy… chips it wasn't supposed to" | ONLY real published headlines about it (shared/news story 1) with highlighter on the published words + Jensen Huang halftone portrait. Fallback if none found: Jensen portrait treatment + NVIDIA logo, name tag "JENSEN HUANG · NVIDIA CEO", no other text | paper; ref: `ast_4b76d56ab5214313` (headline collage, yellow highlight, red arrows) |
| 004 | 20.96–25.44 | "Again, we don't even know if he knew…" | FC pop (M) | face cam |
| 005 | 25.44–34.24 | "it's been a few years since this ban was implemented" | timeline strip 2022 → 2026 with a small "OCT 2022" flag and the BIS rule first page (shared/docs) sliding under | paper, timeline #12 |
| 006 | 34.24–38.72 | "hard to figure out if it is a success or not" | FC pop (C) | face cam |
| 007 | 38.72–40.64 | "Take a look at this video from a few months ago." | FC pop (W) pointing the viewer → cut on action into a phone/monitor frame | face cam → screen |
| 008 | 40.64–54.96 | Hong Kong mall: banned NVIDIA GPUs at US prices; no shortage of these cards | footage/photos of a Hong Kong computer mall + boxed RTX/A-series cards on shelves inside a modern monitor frame with a hand-drawn arrow + label "HONG KONG"; price tags compare (only "same price as the US" as a = sign of two equal tags, no invented numbers) | ref: `ast_1aa75f10abbb4a75` (screen + yellow "visual evidence" annotation), screen = laptop/monitor (2020s) |
| 009 | 54.96–63.53 | "From Hong Kong… a short ferry ride into mainland China… Shenzhen… biggest electronics market on the planet" | pearl_river_delta satdesat map: HONG KONG pin → volt glowing ferry route across the bay → SHENZHEN pin; push into the Huaqiangbei aerial, label "HUAQIANGBEI" | night map; route ref: `ast_c0cbc15573184e83` (glowing route + waypoints); zoom box ref: `ast_671f213364e14029` |
| 010 | 63.53–72.81 | "every building has a room full of NVIDIA GPUs… one job, run AI" | 2.5D Huaqiangbei market set (shared/places layers) → photo plates of stalls/GPU counters, whip between | 2.5D #17 then plates #16 |
| 011 | 72.81–82.41 | "eight of these cards make a server → sold to an AI company, a university, maybe the Chinese military" | isotype build: 8 GPU icons slot into a server chassis (count 1→8), then three arrows to icons: AI company / university / military (labels as he says them) | paper isotype #2/R5 |
| 012 | 82.41–84.97 | "Now, there is a caveat in all of this." | FC pop (M) | face cam |
| 013 | 84.97–94.33 | can't be a big AI player with individual chips; "massive servers that weigh two tons" | scale comparison: single card → 8-GPU server → full rack cutout rising huge, weight counter "2 TONS" (key number yellow) | night, product cutouts, count #13 |
| 014 | 94.33–98.01 | "even those servers are somehow moving into China" | southeast_asia night map: rack icons travelling along volt routes into red China | map routes #3 |
| 015 | 98.01–109.25 | "likely what Megaspeed was doing… other companies in Singapore, Malaysia, other Asian countries" | real Megaspeed headline (shared/news story 2) pinned over the map at SINGAPORE; then pins/labels SINGAPORE, MALAYSIA pulse; end on a camera drift (cut on action) | ref: `ast_b30b6aa33937428e` (tactical map, heat overlay, labels) |

## nvs02 — 109.250–229.500 · the puzzle, the title question, what the ban is (pops until 162.2, then ≈35 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 109.37–115.56 | "if the chips are already making their way into China, what does that say about the ban?" | FC pop (M→C punch at the question) | face cam |
| 002 | 115.56–130.84 | Jensen's podcast: "China is now producing 60 % of all the world's chips… before the ban 17 %" | Jensen Huang halftone portrait left; right a two-bar chart 17 % (before the ban) → 60 % (now), bars red (China), 60 % counts up in yellow; small tag "JENSEN HUANG, ON A PODCAST" (name tag, not a caption) | paper; ref: `ast_1b3c60efa9fc4241` (halftone portrait + bold type) + bars ref `ast_3d5f46c4c01248c5` |
| 003 | 130.84–142.04 | Chinese AI models catching up faster than expected; "way cheaper, insanely cheap" | two lines converging (ice = US models, red = Chinese models), then price tags: Chinese model price shrinking (no invented figures — a relative bar) | night line chart; ref: `ast_06720d0b255d4d29` (curve on black with milestones) |
| 004 | 142.04–146.36 | "it kinda raises an important question" | FC pop (C) | face cam |
| 005 | 146.36–151.80 | "Was the chip ban a mistake? And if it was, why do we still have it?" | TITLE CARD — the video's title question (the one allowed title text): "WAS THE CHIP BAN A MISTAKE?" on the job-card design | ref: `ast_e1ede4fafbd84a66` (ink bar title over document texture, two colour blocks) |
| 006 | 151.80–162.28 | "go through the reasoning behind the chip ban… then decide" | FC (W then M at 156.68 join) — last intro pop, 2 short shots | face cam |
| 007 | 162.28–167.88 | "let me give you an overview of what exactly the chip ban really is" | the real BIS rule page (shared/docs, 7 Oct 2022) tilts in as a document, camera push to its title | newspaper/document #5, two paper layers |
| 008 | 167.88–185.59 | a US law stopping the most powerful AI chips going to China; "most powerful" matters; also the machines that make chips | pacific night map: UNITED STATES (ice) → CHINA (red); a volt chip travels and hits an ice barrier line at mid-Pacific; label "MOST POWERFUL AI CHIPS" on the chip tier (chart label); then a lithography-machine icon stopped at the same barrier | map + markup #20 |
| 009 | 185.59–190.95 | "passed on October 7th… October 7th, 2022" | date card "OCTOBER 7, 2022" odometer on the rule's header (document text); hold through the aside (no visual for the aside) | paper, odometer #13 |
| 010 | 190.95–195.67 | "Trump and Biden don't really agree on a lot." | FC (M) | face cam |
| 011 | 195.67–205.19 | introduced under Biden, continued under Trump | Biden and Trump cutouts in profile facing apart, the rule document chained between them; name tags | ref: `ast_4b7fb0fe0a134429` (two leaders in profile + object between) |
| 012 | 205.19–218.39 | Trump admin extended it, rolled it back to the original, then weaker than Biden's | a horizontal "strength of the ban" gauge: marker at BIDEN 2022 → moves up (extended) → back → below (weaker); labels as he says | paper chart, choppy moves |
| 013 | 218.39–229.50 | "we'll talk about all this back and forth later… the ban is still in place, China cannot buy high-tech US chips" | FC (M, 4 s) → stamp "STILL IN PLACE" on the rule document (document stamp) | face cam → paper |

## nvs03 — 229.500–362.292 · is it fair? (≈35 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 229.60–243.44 | "is this ban even fair? … free and fair trade country… why is it banning China from buying American stuff?" | FC (M → C at 235.12) 6 s; then a balance scale: US flag medallion vs China flag medallion, a chip on the US pan | ref: `ast_0659daaead12498d` (balance scale with medallions) |
| 002 | 243.44–251.68 | "the fair part… no one has a right to buy any product" | FC (W) | face cam |
| 003 | 251.68–266.40 | "if someone doesn't want to sell me something… perfectly legal… same applies overseas" | simple shop-counter diagram: seller icon, product, buyer icon; seller slides the product back (a hand-drawn ✗ on the sale arrow); then the same diagram with two country outlines (US → China) | paper, icons, markup #19 |
| 004 | 266.40–271.20 | "If a country doesn't want to sell… perfectly legal." | FC (M) | face cam |
| 005 | 271.20–283.04 | "China itself has already banned Google, Facebook, YouTube for years… way before any US chip ban" | china night map filled red; the three logos fly toward it and stop at the border with ✗ marks; small year tags from RESEARCH (chart labels) | ref: `ast_d02865717c824c47` (3D relief China in bold red) |
| 006 | 283.04–296.15 | companies allowed in must partner with a Chinese company and hand over trade secrets and technology | diagram: foreign company card + Chinese partner card joined into "JOINT VENTURE"; a blueprint/document slides from one to the other | paper, collage #12 |
| 007 | 296.15–314.47 | IP theft; not just the US — Germany, the UK, France; Global South; WTO cases | world_night map: pins GERMANY, UK, FRANCE light up as named, then Global South pins; WTO logo + real WTO case headline/doc if in shared; else just the logo with label "TRADE CASES AT THE WTO" | map callouts #20 |
| 008 | 314.47–319.75 | "let's go even deeper… think of chips like uranium" | FC (C) | face cam |
| 009 | 319.75–335.11 | uranium: nuclear energy vs nuclear bomb; enriched uranium export heavily controlled | split screen: cooling tower/power plant photo (left) vs mushroom cloud archival (right), yellowcake/pellet in the centre; label "ENRICHED URANIUM — EXPORT CONTROLLED" | night, archival weave #14 on the bomb, plates #16 |
| 010 | 335.11–343.91 | "Chips and AI are kinda like the same thing… good things… bad things" | the same split with a GPU in the centre (match cut on the centre object) | curve cut #15 |
| 011 | 343.91–351.83 | the US doesn't want China to have its best stuff while China talks about invading Taiwan | east_asia satdesat: tilted terrain of the Taiwan Strait, CHINA red, TAIWAN labelled, arrows across the strait | ref: `ast_4f6fcd9750634ef3` (3D terrain + military pieces) — arrows instead of tanks |
| 012 | 351.83–362.29 | "hopefully this gives you a sense… the main question is really if that ban is working or not" | FC (M → C at 358.94) | face cam |

## nvs04 — 362.292–472.667 · the scoreboard; why the US gets to decide (≈35 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 362.38–376.62 | "agree on what working means… everyone gives a different answer" | FC (M) 5 s → three blank answer cards fanning out (no text) with question marks | face cam → paper |
| 002 | 376.62–386.06 | "top three answers… analyze the success" | FC (W) | face cam |
| 003 | 386.06–405.66 | "score everything on this scoreboard… a fourth row at the bottom and it's empty… leaving it blank on purpose" | THE SCOREBOARD full intro (MOTIFS.md): rows 1–3 reveal as he says "top three", row 4 highlighted empty at 391.02–394.86 | night; motif |
| 004 | 405.66–412.62 | "Let's get started. … NVIDIA doesn't actually make the chips." | FC (C → M) | face cam |
| 005 | 412.62–422.27 | "aren't even made in the United States, they're made in Taiwan. So how does the US get to decide?" | pacific sat map: push from the US to TAIWAN, zoom box on Hsinchu → `aerial_hsinchu_park` with TSMC label | ref: `ast_671f213364e14029` (satellite + zoom box) |
| 006 | 422.27–434.75 | designing chips — important, very hard, NVIDIA is really good, "worth so much" | chip blueprint/floorplan drawing itself (paper_blueprint), NVIDIA logo; a market-value bar rising (no figure unless RESEARCH gives one he implies — he gives none → unlabeled rising bar with NVIDIA logo) | blueprint paper, draw-on |
| 007 | 434.75–444.75 | "designed in the United States… NVIDIA's intellectual property… one way the US controls" | NVIDIA HQ photo (Santa Clara) plate with label; an "IP" document stamped | plates #16 |
| 008 | 444.75–453.63 | machines and software used to design and make the chips in Taiwan are American or Western made | fab cleanroom footage in a monitor; tool icons tagged with flags (US / Western) | screen + labels |
| 009 | 453.63–462.67 | "made using American technology → the American government gets a say" | flow diagram: AMERICAN TECHNOLOGY → CHIP → "WHO CAN BUY IT?" gate in ice | paper flow |
| 010 | 462.67–472.67 | "according to one former official… every chip on the planet is under American law" | FC (M) 4 s → world_night globe/map with ice rings spreading from Washington over every chip pin | radio-wave rings §10.6.7 |

## nvs05 — 472.667–559.583 · job one; the line (≈35 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 472.75–476.03 | "let's look at job number one" | JOB card "JOB ONE" (title-card design) | ref: `ast_e1ede4fafbd84a66` |
| 002 | 476.03–488.78 | "job one is keeping the chips out of China… called a chip ban for a reason. Let's look at how it started." | FC (M → W at 483.66) | face cam |
| 003 | 488.78–509.34 | 2022: the government draws a line on a ranking — weakest to most powerful; above: cannot sell; below: can | THE LINE motif: ladder builds, `drawLine` at "drew a line right here", zones labelled as he says them | paper; motif; ref: `ast_ebb77f26d0fc4b3f` (grid with one highlighted row + callout) |
| 004 | 509.34–518.46 | "the line basically covered two chips… two of the best AI chips NVIDIA had" | motif: A100 and H100 cards above the line → `ban` both; product cutouts beside them | motif |
| 005 | 518.46–523.18 | "From NVIDIA's point of view, this was devastating" | FC (C) | face cam |
| 006 | 523.18–531.02 | "China… about a quarter of their entire sales" | waffle 10×10: 25 squares turn red (China), label "CHINA — A QUARTER OF SALES" | ref: `ast_0b23d2c7a06c4bb3` (waffle chart with callout) |
| 007 | 531.02–538.73 | demand exploding all around the world; had to get that revenue | exponential volt curve shooting up | ref: `ast_06720d0b255d4d29` |
| 008 | 538.73–548.33 | "they design a brand new chip, very quickly… made specifically to get around this law" | FC (M) 4 s → chip blueprint being redrawn fast | face cam → blueprint |
| 009 | 548.33–559.58 | "the NVIDIA chip was right there on the line… the most powerful chip they could without breaking the law" | motif: A800 / H800 added just under the line (camera punch-in on the gap between card and line) | motif, cut on action |

## nvs06 — 559.583–647.042 · the line moves; cat and mouse (≈35 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 559.69–565.53 | "the administration was not happy, but it took them some time to respond" | FC (M) | face cam |
| 002 | 565.53–574.17 | a year later the line moves below the new chip → illegal | motif: `moveLine` down past A800/H800 → banned; small date tag from RESEARCH | motif |
| 003 | 574.17–585.53 | "guess what NVIDIA does? … another chip right below this new line" | FC (C) 2 s → motif: H20 added under the new line | face cam → motif |
| 004 | 585.53–598.76 | Commerce Secretary "at the time": QUOTE "we can keep playing this game… ban the new chip the very next day" | Gina Raimondo portrait (ice frames) + pull-quote; show the REAL quote wording from RESEARCH (her words, with attribution/date), underlined word by word as Sam paraphrases; if RESEARCH's wording differs a lot, show only her name tag + "DECEMBER 2023" | ref: `ast_0455523fccc84f71` (official portrait, geometric colour frames, institutional photos); painting-to-print §10.7 |
| 005 | 598.76–612.36 | cat and mouse continued; "regular video game chips that I probably have in this PC — oh you guys can't see it" banned | FC (W, he gestures at the PC) through the aside; then RTX 4090 cutout dropping above the line (motif `ban`) | face cam → motif |
| 006 | 612.36–623.00 | "this usually happens with regulation… the 90s… harder to export supercomputers… slow to catch up" | 1990s supercomputer photo in a period CRT monitor; export-control document | vintage screen #11 (era-correct) |
| 007 | 623.00–631.08 | government considered the PlayStation a supercomputer; couldn't export without a licence | PlayStation 2 cutout hero + real period headline (shared/news story 5) with highlighter; "EXPORT LICENCE REQUIRED" stamp on a licence form (shared/docs BIS-748P) | ref: `ast_e2a78874f76a4410` (letterhead document) + `ast_309797d0b3974b01` (bold headline article) |
| 008 | 631.08–647.04 | AI regulation in the US; "not saying regulation is bad… overly broad. Nonetheless… back to the story" | FC (M → C at 642.76) | face cam |

## nvs07 — 647.042–775.250 · individuals carry chips (≈40 % FC — personal stories)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 647.16–662.59 | chips still got in; individuals taking them when visiting or moving back | airport/customs footage; pacific map: small volt dots (people) crossing US → China | map + plates |
| 002 | 662.59–668.27 | people buying chips from random people on Facebook Marketplace | a marketplace-style listing card of a used graphics card (our own neutral UI with the Facebook Marketplace logo tag; real screenshot only if in shared/places) | paper UI card |
| 003 | 668.27–683.71 | "Imagine this video bombs. I have no money to pay rent. I sell the chip… $1,000–$2,000… maybe he takes it to China… perfectly legal" | FC (M/C alternating at joins) — the joke stays on him | face cam |
| 004 | 683.71–696.35 | taking it to China is illegal, "really hard to police… so many people" | isotype crowd of traveller icons each with a small box; a single officer icon; ✗ can't-catch-all | isotype R5 |
| 005 | 696.35–714.03 | how hard would you punish them; they may not know it's a law; not a geopolitical fight | FC (W → M) | face cam |
| 006 | 714.03–728.88 | "$2,000 here → sell in China for $2,300 or $2,500 → pays for the ticket a little" | flat-lay: boarding pass, passport, a boxed card; price tags $2,000 → $2,300 / $2,500 count up; "+$300" in yellow | ref: `ast_acc78b28b2d84747` (travel flat-lay with pinned photos/stamps) |
| 007 | 728.88–748.96 | common tactic; 2010s iPhone bought in the US, double the price overseas; "I'm not saying I did it, but I was young" | early-2010s iPhone cutout on scattered polaroids, price tag ×2; then FC (C) for the confession joke from 744.08 | ref: `ast_e8562eb310434ee1` (scattered polaroids, spotlit); face cam |
| 008 | 748.96–756.88 | "paying off my ticket for free… how easy it is to carry an iPhone" | FC (M) | face cam |
| 009 | 756.88–775.25 | limited resources to police; person making 300 bucks, not a dedicated smuggling operation | resources bar: small budget split across thousands of travellers vs one big target; "$300" tag | paper chart |

## nvs08 — 775.250–864.750 · the big fish (≈30 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 775.36–782.89 | "the government focused on the bigger picture… people doing this in a big way" | FC (M) | face cam |
| 002 | 782.89–792.81 | government arrested a co-founder of one of the biggest US server companies; case ongoing | CASE FILE board: real DOJ press release / headline (shared/news story 7), the company logo, the person's photo only if RESEARCH confirms identity; tag "CASE ONGOING — ALLEGED" | ref: `ast_8693d810270e43fd` (case-file flat lay with polaroids + notes) |
| 003 | 792.81–808.09 | ~$1.5 billion of servers to a fake Southeast Asian company passing them to China, "pretending it's in South Korea" | southeast_asia night map: servers leave the US (inset) → pin in Southeast Asia (name per RESEARCH) → red route into CHINA; "$1.5 BILLION" yellow counter (his number) | ref: `ast_b30b6aa33937428e`; route `ast_c0cbc15573184e83` |
| 004 | 808.09–815.29 | auditors are supposed to check the servers go where they should | FC (W) | face cam |
| 005 | 815.29–831.29 | hair dryer to peel barcodes off real chips onto fake/older ones; a room pretending they're running | step diagram on the board: hair dryer cutout → sticker peels → sticks on a dummy server; polaroid of a server room; red string between cards | ref: `ast_1587dee18be645e2` (cork board, pinned photos, notes) with string (R9) |
| 006 | 831.29–846.84 | the warehouse camera recorded it; the video is public; "very damning" | security-monitor frame: the real surveillance still/clip if published (shared), else a typeset "CCTV — WAREHOUSE" empty monitor with scanlines over a blurred warehouse photo and a circle markup | screen #11 modern CCTV; ref: `ast_1aa75f10abbb4a75` |
| 007 | 846.84–864.75 | Megaspeed probably similar; "no one knows for sure"; others in Southeast Asia | FC (M) 6 s → map again: several ? pins across Southeast Asia | face cam → map |

## nvs09 — 864.750–935.000 · verdict on job one; the pivot (≈40 % FC; last shot is B-roll)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 864.84–880.84 | "if the goal is to keep chips out of China, it's kind of a failure: small chips get in, big chips get in" | china map red with two volt inflows: small (cards, by plane) and big (racks, by ship) both crossing the ice barrier line | map #3 |
| 002 | 880.84–889.75 | "enforcement being weak… doesn't change the result… it's not working" | SCOREBOARD: row 1 stamped ✗ at "not working" | motif |
| 003 | 889.75–898.07 | "if I stop the video here you'd say this whole thing is a joke… what I was thinking when I started researching" | FC (M) | face cam |
| 004 | 898.07–913.11 | "if a random YouTuber like me can find this, the government knows… two presidents keep this policy" | FC (C) to 905.51 → Biden + Trump cutouts either side of the rule document (reuse nvs02 look, different layout) | face cam → collage |
| 005 | 913.11–921.99 | "something we're missing… question the premise of point one" | FC (W → M) | face cam |
| 006 | 921.99–935.00 | "Maybe the goal is to keep the lead the US has in AI… some chips flowing into China don't change that" | race-track/lead chart: ice (US) marker far ahead of red (China) marker on a compute axis; a few volt chips trickle to China and its marker barely moves. END on this (B-roll), camera still drifting | night chart, cut on action |

## nvs10 — 935.000–1046.000 · why scale is the point (NO face cam from here to nvs22)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 935.11–952.54 | building an AI company: take the whole internet, feed it to the chips, let it practice for months — training | explainer collage on grid paper: web pages/books pour into a chip, a calendar flipping months; hand-lettered sticky label "TRAINING" on his word | ref: `ast_c5efacef3dbd4abf` (science collage, sticky-note labels on grid paper) |
| 002 | 952.54–964.06 | you need an insane number of chips working together in a cluster | one chip → grid of thousands of chip icons linking with lines (isotype, count up) | night isotype |
| 003 | 964.06–976.54 | NVIDIA's newest system: a rack the size of a refrigerator; 3,000 pounds, like a small car | blueprint: rack cutout with schematic dimension lines next to a refrigerator outline (same height); then a scale tipping: rack vs small car, "3,000 LB" | ref: `ast_b79f39f3b42f48f8` (photo + technical blueprint overlay) |
| 004 | 976.54–985.50 | same electricity as 100 homes | rack with a power cable feeding a 10×10 grid of house icons lighting up, "100 HOMES" | isotype R5 |
| 005 | 985.50–994.46 | liquid cooling — plumbing and a bunch of other stuff | isometric cutaway of a data hall: racks, coolant pipes drawn in ice, pumps; labels "LIQUID COOLING", "PLUMBING" | ref: `ast_91abea88b76c4b43` (isometric diagram on blueprint grid with hand sketches) |
| 006 | 994.46–1003.66 | a frontier AI company needs thousands of these racks | 2.5D data-center aisle (shared/hardware layers) dolly; counter of racks | 2.5D #17 |
| 007 | 1003.66–1014.65 | why it's so hard to smuggle the numbers China needs | a suitcase with one card vs a wall of racks — scale gag: the suitcase icon tiny beside the rack field | paper comparison |
| 008 | 1014.65–1023.61 | a single data center in Memphis uses as much power as 800,000 homes | us night map → zoom box MEMPHIS → `aerial_memphis_xai_colossus`; "800,000 HOMES" key number; label per RESEARCH (xAI Colossus) | ref: `ast_671f213364e14029` |
| 009 | 1023.61–1035.45 | that one site has more compute than everything China has smuggled combined | two bars: MEMPHIS (volt, tall) vs "EVERYTHING SMUGGLED INTO CHINA" (red, shorter) | paper bars R6 |
| 010 | 1035.45–1046.00 | compared with China's biggest data center: about 7 % | bar shrink: China's biggest = 7 % of the Memphis bar, "7%" | same chart develops |

## nvs11 — 1046.000–1174.583 · the ban is working: compute share; life inside China
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1046.09–1051.61 | "in this sense the ban is working… really, really well" | volt data-hall plate, slow push (breather, hero light) | night plate #16 + streaks |
| 002 | 1051.61–1069.80 | 2022: US ≈ 60 % of AI computing power → now close to 80; China only about 1 % (counting its own chips) | bars over time: US 60 → 80 (ice), China 1 % (red sliver); title "SHARE OF THE WORLD'S AI COMPUTING POWER" | ref: `ast_3d5f46c4c01248c5` (bar chart on cream, serif title with italic word) |
| 003 | 1069.80–1080.44 | smuggling some, but nowhere near the US companies; see the result inside China | china night map, relief, red; pins for the companies that follow, each connected to a logo card | ref: `ast_3c804bab5fc04bfb` (relief map with pins linked to portrait cards) |
| 004 | 1080.44–1090.84 | one of the biggest AI companies cut what it sold by 80 % | card of that company (RESEARCH; if unverified: unnamed "A TOP CHINESE AI COMPANY") with capacity bar dropping 80 % | chart on map |
| 005 | 1090.84–1101.48 | ByteDance (TikTok's owner) turns features off during holidays to save compute | ByteDance + TikTok logos; phone UI of feature toggles switching off (our neutral UI), calendar holiday mark | phone screen |
| 006 | 1101.48–1114.92 | DeepSeek went dark for about 12 hours in spring… | DeepSeek logo on a dark server-status screen: "12 HOURS" timer; real outage headline if in shared | ref: `ast_309797d0b3974b01` |
| 007 | 1114.92–1130.91 | founder to investors (leaked transcript — grain of salt): two years behind, one twentieth of the compute | transcript pages in hands with highlighter on body lines ONLY if a real published transcript text exists in shared; else typeset neutral pages with no readable invented quotes + Liang Wenfeng photo, tags "LEAKED CALL — UNVERIFIED", "2 YEARS BEHIND", "1/20 OF THE COMPUTE" (chart labels) | ref: `ast_29cb2d6f990c442a` (documents with yellow highlights, hands, flat lay) |
| 008 | 1130.91–1139.79 | China has more AI researchers but not enough chips | isotype: researchers China > US; chips China ≪ US | isotype |
| 009 | 1139.79–1153.39 | irony: China has way more electricity than the US but nothing to use it on | power-line plates + two bars ELECTRICITY: China ≫ US | ref: `ast_cba454c51d9a4a1c` (atlas spread with small charts) |
| 010 | 1153.39–1174.58 | the US has all the chips but can't build data centers: no public support, not enough electricity; "both sides… unique ways" | mirror layout: US column (chips ✓, power ✗) vs China column (power ✓, chips ✗) | paper matrix |

## nvs12 — 1174.583–1260.375 · three ways to measure the lead
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1174.67–1180.59 | "three different ways to track the lead" | three numbered tabs (1 CHIPS · 2 TESTS · 3 TIME) on the job-card design, only the numbers first, each word on cue | title-card family |
| 002 | 1180.59–1187.95 | by chips, American companies win: 20 times more | chip-stack isotype: US stack 20 units vs China 1, "20×" | isotype |
| 003 | 1187.95–1215.42 | by tests: Chinese models were ~30 points behind, today 3 points; "without enough chips" | dual line chart: US (ice) and China (red) scores over years; bracket gap "30 POINTS" → "3 POINTS" | ref: `ast_d3d145bc2ebb47ad` (line chart with filled area + end labels) |
| 004 | 1215.42–1231.90 | by time: 7–8 months to match; steady for three years | timeline ruler: US model today, China's matching model 7 months later; three years of rows all ≈ 7 months | timeline #12 |
| 005 | 1231.90–1242.06 | Chinese companies want you to look at the second way | tab 2 lifts, red spotlight (contrast call-out) | §10.6.3 |
| 006 | 1242.06–1260.38 | labs build models to succeed on the tests; tests should judge equally | exam metaphor: an exam sheet where the model already has the answer key (student-desk flat lay, pencil ticks) | paper collage |

## nvs13 — 1260.375–1356.292 · the government's own test; caveats
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1260.47–1277.43 | the US government ran its own tests nobody had seen; Chinese models good but not as good as claimed | the real NIST CAISI report cover/chart (shared/docs) as a document reveal, push to the chart; if missing: a sealed-envelope "UNSEEN QUESTIONS" graphic | document #5 |
| 002 | 1277.43–1292.23 | without the questions ahead of time the gap is larger than on the public test | paired bars: PUBLIC TEST gap (small) vs UNSEEN TEST gap (larger) | paper bars |
| 003 | 1292.23–1312.08 | the other side: maybe the test was built to show that; but it says Chinese models are really good, just not as good | balance of two argument cards; the government seal on one | paper |
| 004 | 1312.08–1341.36 | "I apologize for the caveats… easy to make a video saying America is winning / China is winning… lots on YouTube… I want the big picture" | wall of video-thumbnail frames (our own blank thumbnails with flags, no real titles) half ice half red; then pull back to a wide "big picture" of the whole board | collage, camera pull |
| 005 | 1341.36–1356.29 | "Shouldn't the gap be much larger, considering Chinese models have 5 % of the chips?" | question chart: chips 5 % (tiny red bar) vs scores almost equal — a visual mismatch with a "?" markup | markup #19 |

## nvs14 — 1356.292–1445.542 · smuggling as a hidden factor; the suspicious chart
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1356.40–1372.79 | factors people don't talk about publicly: smuggling; "one twentieth" claimed ≠ real | an iceberg: declared chips above water, undeclared below | night illustration |
| 002 | 1372.79–1388.95 | you don't say you got it illegally — especially when your revenue comes from America | mugshot-board style cards of anonymous silhouettes with "NO COMMENT" tape… keep it light: company cards with a finger-to-lips; US consumer market map glowing | ref: `ast_716e2cc68e364ca5` (ID photos with labels on dark surface) — silhouettes/logos, no real faces |
| 003 | 1388.95–1404.95 | the US consumer market is massive; they want to sell in the US; can't admit smuggled chips | us night map, ice glow, app icons flowing China → US | map |
| 004 | 1404.95–1426.46 | when DeepSeek's model came out, experts said it used a lot more NVIDIA chips than it admits | real headline (shared/news story 11) with highlighter; DeepSeek logo; stack of GPUs: "ADMITTED" small vs "ESTIMATED" larger (labels only; numbers only if he says them — he doesn't) | ref: `ast_4b76d56ab5214313` |
| 005 | 1426.46–1445.54 | "Take a look at this chart": Chinese models upgrade right after American ones; "suspicious" | step chart: ice steps (US releases) followed shortly by red steps each time; arrows between each pair; final circle markup | ref: `ast_d3d145bc2ebb47ad`; markups #19 |

## nvs15 — 1445.542–1572.417 · distillation
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1445.66–1454.30 | "Chinese models are basically copying the American models… called distillation" | lab-notebook collage: big flask (US model) dripping into a small flask (Chinese model); sticky label "DISTILLATION" on his word | ref: `ast_c5efacef3dbd4abf` |
| 002 | 1454.30–1467.66 | you can ask an AI anything — also how its thinking works | chat window (our neutral UI): question bubble → answer; then a question aimed at a brain diagram | phone/laptop screen |
| 003 | 1467.66–1481.19 | safeguards; cat and mouse | lock on the chat; key shapes trying; lock changes | icon animation |
| 004 | 1481.19–1494.71 | tens of thousands of fake accounts reverse-engineering a new model | isotype wall of account avatars (masked) multiplying, counter "TENS OF THOUSANDS" | isotype R5 night |
| 005 | 1494.71–1504.31 | their model becomes nearly as good without the time or money | two cost bars: TRAIN FROM SCRATCH (tall) vs DISTILL (short) | bars |
| 006 | 1504.31–1519.83 | big US AI companies complained publicly; top companies — who hate each other — | real statements/headlines (shared/news story 12); logos OpenAI, Anthropic, Google apart | ref: `ast_2b0b05b6a7bd471a` |
| 007 | 1519.83–1545.94 | now working together: share information about attacks, and the fixes | three logos link with drawn lines; an alert pulse passes from one to the others | radio-wave rings / string |
| 008 | 1545.94–1558.66 | harder to distill, quicker to shut down | shield closing over the flask from scene 001 | callback |
| 009 | 1558.66–1572.42 | the gap is widening again a little in the last few months | line chart tail: gap bracket 3 → opens slightly | ref: `ast_d3d145bc2ebb47ad` |

## nvs16 — 1572.417–1698.208 · score 1–1; Jensen's argument
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1572.50–1595.23 | back to the scorecard: second job, keep the American lead — it is working; "one to one" | SCOREBOARD: row 2 ✓ at "it is working"; tally "1 — 1" | motif |
| 002 | 1595.23–1602.35 | "job three… a completely different way of looking at this" | JOB card "JOB THREE" | title-card family |
| 003 | 1602.35–1610.35 | the person making this argument "was" the CEO of NVIDIA, Jensen Huang | Jensen grid-collage portrait: tiles of his photo with volt squares, name tag | ref: `ast_71a7df7876064062` (grid collage portrait with colour squares) |
| 004 | 1610.35–1625.55 | refuse to sell → China builds its own → you created a competitor | flow: US chip blocked at the line → a red factory rises in China → a red chip appears (Huawei colour, no logo yet) | map/diagram |
| 005 | 1625.55–1636.59 | smartest move: no ban, so every Chinese AI company is built on American chips and software | Chinese company cards all sitting on a volt foundation slab labelled "AMERICAN CHIPS + SOFTWARE" | diagram |
| 006 | 1636.59–1650.03 | every AI engineer learns to code on NVIDIA; like the same keyboard | hands at a keyboard, keys lifting; code lines | ref: `ast_05ca6a314e6642fa` (hands at keyboard with floating keys) |
| 007 | 1650.03–1661.74 | switching systems = redoing the whole thing; no one switches | a building lifted off one foundation — cracks; "REDO EVERYTHING" chart label | illustration |
| 008 | 1661.74–1688.14 | logical — but he's biased: wants to sell more chips; fiduciary duty | Jensen on stage photo with revenue arrow; "CEO" tag; a scale tilting with money | ref: `ast_0455523fccc84f71` (portrait + colour frames) in volt |
| 009 | 1688.14–1698.21 | biased doesn't mean wrong; let's evaluate | his argument card set on the scale, level again | callback |

## nvs17 — 1698.208–1822.167 · 95 → 0; Huawei; Lutnick
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1698.30–1711.27 | job three = keep China hooked; before the ban NVIDIA had ~95 % of China's AI-chip market | waffle 100 squares: 95 volt | ref: `ast_0b23d2c7a06c4bb3` |
| 002 | 1711.27–1736.87 | after: NVIDIA says 0 % — technically; practically, smuggling and rerouting | waffle empties to 0; then ghost volt squares flicker back with "?" (smuggled) | same chart develops |
| 003 | 1736.87–1752.79 | who sells instead? Huawei — banned from the US for spying a few years ago; blowing up inside China | Huawei logo hero on china map; Huawei HQ/store plate; real 2019 headline if in shared | ref: `ast_d02865717c824c47` |
| 004 | 1752.79–1771.70 | ~200,000 chips last year (US government); private estimates > half a million; 1.5 million expected this year | growth curve with milestones 200,000 → 500,000+ → 1.5 MILLION (yellow) | ref: `ast_06720d0b255d4d29` (curve with dated milestones) |
| 005 | 1771.70–1783.46 | a random person helping China without realizing it — the current Commerce Secretary | Commerce building → Howard Lutnick portrait reveal, name tag | ref: `ast_0455523fccc84f71` |
| 006 | 1783.46–1801.46 | last summer the administration allowed a stronger chip (not the strongest) | THE LINE motif (compact reuse): line nudged up, one more chip allowed below it (chip name per RESEARCH) | motif |
| 007 | 1801.46–1822.17 | Lutnick on live TV — QUOTE: "we're not selling them our best stuff, not our second best, not even our third best… so they can stay addicted to the American technology" | TV-news monitor with the real clip/still (shared) or his portrait; pull-quote with HIS published words (RESEARCH), underlined word by word; "addicted" highlighted yellow | painting-to-print §10.7; TV screen #11 modern |

## nvs18 — 1822.167–1893.917 · China blocks the chips; volume and yield
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1822.26–1835.87 | good plan or not, he didn't have to say it publicly; what does the Chinese government do? | Xi/Zhongnanhai plate + the Lutnick quote card being read (card slides across to the China side) | Vox layered #10 |
| 002 | 1835.87–1853.47 | China blocks NVIDIA chips; ~600,000 sit at a port; the CCP gives no permission to take delivery | container port plate; giant numerals "600,000" built into the stacks/cranes; customs gate closed in red | ref: `ast_db095fac62b54549` (huge numbers integrated with architecture) |
| 003 | 1853.47–1868.19 | why, if China wants to win the AI war? what a chip company needs to succeed | question on the port image → cut to a fab exterior | plates |
| 004 | 1868.19–1882.27 | Huawei is successful; the most important thing is volume | order tickets stacking up into a tall pile at a factory gate, "VOLUME" axis label | paper isotype |
| 005 | 1882.27–1893.92 | yield: of 100 chips, how many actually work | wafer with 100 dies: good ones light volt, bad ones dark; counter "x / 100" | wafer chart (waffle) |

## nvs19 — 1893.917–1991.333 · Texas, TSMC, volume first
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1894.02–1906.10 | the chip industry was created in Texas, by Texas Instruments | us atlas map → TEXAS → Dallas; founder-card: Jack Kilby photo with red-outlined cutout + TI building + big "1958" | ref: `ast_8453bcb46af0421b` ("IT ALL STARTS HERE" founder timeline card) |
| 002 | 1906.10–1919.94 | 50s–70s: a good yield was 10 %; later 30 % (100 made, 30 work) | the wafer chart: 10 lit → 30 lit, era tags | wafer chart |
| 003 | 1919.94–1931.54 | now 99.3 / .5 / .7 % — all TSMC in Taiwan, "destroying it" | wafer nearly all lit, "99%+"; TSMC fab aerial/photo | wafer + plate |
| 004 | 1931.54–1953.83 | TSMC took all the volume, sold under cost, learned, profit → next factory → next generation | flywheel diagram: VOLUME → YIELD → LOWER COST → PROFIT → NEXT FAB, drawn on as he says each | paper flow, loop |
| 005 | 1953.83–1967.75 | volume before better — opposite of other industries | two tracks: OTHER INDUSTRIES (better → volume) vs CHIPS (volume → better) | paper |
| 006 | 1967.75–1991.33 | Beijing forces NVIDIA out → Chinese AI companies buy Huawei → more orders → better yield → next generation | the flywheel recoloured red with the Huawei logo, spinning up; NVIDIA chip pushed off the china map | callback + map |

## nvs20 — 1991.333–2103.000 · 60 % of chips ≠ 60 % of power
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 1991.43–2015.80 | Jensen on a podcast: China makes 60 % of the world's chips — scary; 17 % before 2022 | callback to nvs02's 17 → 60 chart, now full-frame with a globe of chips, 60 % red | bars (variation) |
| 002 | 2015.80–2022.04 | so the ban made China a big player — supporting NVIDIA's argument? | Jensen card + ✓? tentative mark | callback |
| 003 | 2022.04–2040.28 | iPhone 1 vs iPhone 18: both iPhones, one much stronger | first iPhone cutout vs newest iPhone cutout on a scale / spec bars | product cutouts, night |
| 004 | 2040.28–2059.32 | a country making lots of iPhone 1s; nobody wants iPhone 1 | crate isotype: thousands of old iPhones (red) vs few new ones | isotype |
| 005 | 2059.32–2077.03 | look at computing power: China ≈ 10 % of the world's | waffle: 60 % of CHIPS (count) morphs to 10 % of COMPUTING POWER | ref: `ast_0b23d2c7a06c4bb3` |
| 006 | 2077.03–2103.00 | the CCP wants to fix exactly this: not buying allowed NVIDIA chips, forcing orders to Huawei, up the value chain | value-chain staircase: Huawei climbing steps from "OLDER CHIPS" to "NEXT GENERATION"; NVIDIA crates left at the port | paper staircase |

## nvs21 — 2103.000–2182.542 · job three verdict; the loophole opens
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 2103.11–2126.87 | no US chips, no good Huawei chips yet — how are Chinese models so close? a fourth level | puzzle board: two crossed-out supply arrows into a Chinese lab that still glows; "?" | night diagram |
| 002 | 2126.87–2146.98 | scorecard, level three: keeping China hooked — not working; the Commerce Secretary isn't helping | SCOREBOARD: row 3 ✗ | motif |
| 003 | 2146.98–2158.02 | "level four… a big loophole… kept it till the end" | JOB card "LEVEL FOUR" + row 4 of the scoreboard fills "The renting loophole" | title-card + motif |
| 004 | 2158.02–2182.54 | a data center doesn't have to be next to the company using it; built in the middle of nowhere; stretch it far | us night map: a city and a data center in empty land joined by a fibre line that stretches… and keeps stretching off the map westward | map, long ease |

## nvs22 — 2182.542–2267.958 · Malaysia
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 2182.66–2198.99 | lots of data centers in Malaysia, rented by Chinese companies; the most powerful chips in the world | southeast_asia map with MALAYSIA magenta-style highlight in neutral + volt pins; push into `aerial_johor_data_centers` | ref: `ast_b15cdcc28a634241` (3D topo with one country highlighted, pins, city labels) |
| 002 | 2198.99–2208.59 | someone builds it — a Malaysian company, an American company, "maybe even the Commerce Secretary himself"; "that news just came out" | owner cards flipping: MALAYSIAN FIRM / AMERICAN FIRM / Lutnick portrait with the real headline (shared/news story 15) if found; else his portrait with "?" | cards on aerial |
| 003 | 2208.59–2222.19 | owner rents to a Chinese company that logs in or flies down | isometric data hall with a "FOR RENT" tag; a login cable from CHINA and a plane arc | ref: `ast_91abea88b76c4b43` |
| 004 | 2222.19–2236.35 | perfectly legal: Malaysian law, Chinese law, US law; the renting loophole wasn't addressed | three law books/stamps ✓ ✓ ✓; then the rule document with a hole literally cut in it | paper documents |
| 005 | 2236.35–2250.66 | they tried fixing it, then decided it's smarter to let them rent; big business | rising rent-receipt stack | paper |
| 006 | 2250.66–2267.96 | Chinese firms rent about as much compute abroad as they have at home | two equal bars: INSIDE CHINA = RENTED ABROAD | bars; end on B-roll |

## nvs23 — 2267.958–2402.000 · flying the data; the debate; sign-off (≈40 % FC)
| # | time | words | picture | ground / effect / ref |
|---|---|---|---|---|
| 001 | 2268.18–2280.58 | funniest part: the Chinese government holds Chinese AI companies back — citizens' data can't leave the country | FC (M) 6 s → china map with a red data wall around it | face cam → map |
| 002 | 2280.58–2307.31 | employees fly to Malaysia with the data, train, bring the model back, run it on weaker chips | route animation CHINA → MALAYSIA: plane with a suitcase of hard drives; there: racks train (progress bar); return leg: a small "MODEL" file; back home on older chips | ref: `ast_c0cbc15573184e83` (glowing route with labelled waypoints) |
| 003 | 2307.31–2313.95 | people argue both sides: keep it or take it away | FC (W) | face cam |
| 004 | 2313.95–2330.03 | side one: good — fewer orders for Huawei, so it never catches up | debate layout: two profiles facing apart with the Malaysia data center between; side-one card with the Huawei flywheel slowing | ref: `ast_4b7fb0fe0a134429` |
| 005 | 2330.03–2351.55 | side two: the chips are outside China — in a war over Taiwan the US can shut the data centers off | map: Taiwan Strait tension + a big ice switch flipping OFF over the Malaysia site, the lines to China go dark | ref: `ast_4f6fcd9750634ef3` |
| 006 | 2351.55–2365.87 | "I don't know how to rank this part"; debate picked up since the Jensen story | FC (C) with the compact SCOREBOARD beside him: row 4 gets "?" at "don't know how to rank" | face cam + motif |
| 007 | 2365.87–2394.84 | comment below; "I'm not an expert… researched to understand the policy" | FC (M/W alternating at joins); one cutaway (2372–2377) to the full scoreboard final state | face cam |
| 008 | 2394.84–2402.00 | "That's all I have… My name is Sam. I'll see you in the next video." | FC (W) to 2400.6 → fade to night with the Searching Lessons end card if one exists in the repo (else plain night), by 2402.0 | face cam, designed ending |

## Reference coverage (inspo ids used → segments)
`ast_290885ff9bcc4687` nvs01 · `ast_2b0b05b6a7bd471a` nvs01, 15 · `ast_4b76d56ab5214313` nvs01, 14 · `ast_1aa75f10abbb4a75` nvs01, 08 ·
`ast_c0cbc15573184e83` nvs01, 08, 23 · `ast_671f213364e14029` nvs01, 04, 10 · `ast_b30b6aa33937428e` nvs01, 08 · `ast_1b3c60efa9fc4241` nvs02 ·
`ast_3d5f46c4c01248c5` nvs02, 11 · `ast_06720d0b255d4d29` nvs02, 05, 17 · `ast_e1ede4fafbd84a66` title cards (02, 05, 12, 16, 21) ·
`ast_4b7fb0fe0a134429` nvs02, 23 · `ast_0659daaead12498d` nvs03 · `ast_d02865717c824c47` nvs03, 17 · `ast_4f6fcd9750634ef3` nvs03, 23 ·
`ast_ebb77f26d0fc4b3f` THE LINE (05, 06) · `ast_0b23d2c7a06c4bb3` nvs05, 17, 20 · `ast_0455523fccc84f71` nvs06, 16, 17 ·
`ast_e2a78874f76a4410` + `ast_309797d0b3974b01` nvs06, 11 · `ast_acc78b28b2d84747` + `ast_e8562eb310434ee1` nvs07 ·
`ast_8693d810270e43fd` + `ast_1587dee18be645e2` nvs08 · `ast_c5efacef3dbd4abf` nvs10, 15 · `ast_b79f39f3b42f48f8` nvs10 ·
`ast_91abea88b76c4b43` nvs10, 22 · `ast_3c804bab5fc04bfb` nvs11 · `ast_29cb2d6f990c442a` nvs11 · `ast_cba454c51d9a4a1c` nvs11 ·
`ast_d3d145bc2ebb47ad` nvs12, 14, 15 · `ast_716e2cc68e364ca5` nvs14 · `ast_71a7df7876064062` nvs16 · `ast_05ca6a314e6642fa` nvs16 ·
`ast_db095fac62b54549` nvs18 · `ast_8453bcb46af0421b` nvs19 · `ast_b15cdcc28a634241` nvs22.
Not used (don't fit this story): Roman Empire, Spain, Finland, UK/France, Stockholm, Den Osse, India portrait, Pasteur, Machu Picchu, WWI,
Nando's, 1917/Alexander posters, Malcolm X, missing-girl clippings, Washington Post, portrait collage, Apple-style… (see INDEX.md).
