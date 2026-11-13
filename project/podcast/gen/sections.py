"""The edit plan: intro segments + the necessary edited sections after 5:46, defined in RAW seconds (analyst notes) and resolved to
MASTER seconds (transcript_pd.json, 30 fps frame grid). Writes project/podcast/sections.json and prints a table.
Each row: (comp id, editor, raw_t0, raw_t1, title, why it is needed / what to show, rating, inspo asset ids)"""
import json
S = [
 # ---- INTRO: full documentary edit (Krish rule 1) --------------------------------------------------------------------------
 ('pd01','ED01',   0.0,  113.9,'Intro 1 — 1983, Tsao\'s insight, the phone boom and bust, the foundry idea','full edit','INTRO','6af0421b 62b64549 2ebb47ad 255d4d29 b76c4b43'),
 ('pd02','ED02', 113.9,  230.1,'Intro 2 — the board says yes with one condition; the unnamed executive; New York; the Q&A aside','full edit','INTRO','455f4813 ccc84f71 73184e83 ab8146d1 b57b4e0e'),
 ('pd03','ED03', 230.1,  348.7,'Intro 3 — the board turns cold; two years later, across the street; Morris Chang, TSMC; betrayal and rivalry','full edit','INTRO','a9fc4241 0a134429 549d4839 8a634241 fbd84a66'),
 # ---- SECTIONS ---------------------------------------------------------------------------------------------------------------
 ('pd04','ED04', 452.4,  462.0,'Fred Terman, "father of Silicon Valley"','main character of the next 30 min introduced: portrait + name + nickname','B','ccc84f71'),
 ('pd05','ED04', 476.8,  569.0,'12 trillion-dollar companies map → 1926 GDP 90/10 → brain drain west→east','Sam says "this is the map" and quizzes on it; two number comparisons; geography + 5 names','A','9b4c4611 a06c4bb3 73184e83'),
 ('pd06','ED04', 594.0,  603.8,'Herbert Hoover, Stanford first class 1891','new person; Sunkit asks "Hoover the president?"','B','ccc84f71 f3ea432e'),
 ('pd07','ED05', 895.2,  959.5,'Frederick Terman: born 1900, father invented the IQ test; 1924 → MIT; MIT + Harvard in Boston','character re-enters with 3 facts, then the Boston geography he will copy','B','566a46e7 9b4c4611'),
 ('pd08','ED05',1030.2, 1046.3,'Vannevar Bush, founder of Raytheon','new person, hard-to-spell name + company','B','ccc84f71'),
 ('pd09','ED05',1124.3, 1146.8,'1938: Bill Hewlett and David Packard (HP revealed on Sunkit\'s answer)','two new people + date; reveal','B','f3ea432e'),
 ('pd10','ED05',1173.1, 1215.0,'The audio oscillator; what Terman gave them (money, fellowship, 25 companies, first client Disney)','unfamiliar object the next minutes depend on + a 4-item list','A','b76c4b43 3dbd4abf'),
 ('pd11','ED06',1387.8, 1456.5,'"Steeples of excellence" (4 fields → silicon); 1947 Bell Labs: Shockley, Bardeen, Brattain; how a transistor switches','coined term + list; three names + date; Sam: "probably not the best explanation" → diagram','A','b76c4b43 6af0421b 8e364ca5'),
 ('pd12','ED06',1541.2, 1566.6,'Shockley moves to Palo Alto (his mother) and starts a company','the "why here" argument is geographic: map Bell Labs → Palo Alto next to Stanford','B','b57b4e0e 64e14029'),
 ('pd13','ED06',1617.0, 1673.0,'Stanford\'s 8,000 acres (25% of San Francisco) can never be sold → 99-year leases','numbers + a rule + the workaround','B','9381944c b76c4b43'),
 ('pd14','ED07',1834.2, 1873.9,'The wiring problem: tens of thousands of transistors glued together by hand','abstract engineering problem; needs to be seen','A','3dbd4abf b76c4b43'),
 ('pd15','ED07',1892.9, 1936.2,'The Traitorous Eight leave Shockley → Fairchild Semiconductor','famous group photo, the name, a key number','B','455f4813 8e364ca5 10434ee1'),
 ('pd16','ED08',1964.0, 2083.0,'Jack Kilby\'s integrated circuit at Texas Instruments; germanium vs silicon, Robert Noyce; semiconductor → why it is called Silicon Valley','new people + the core technical idea + the payoff of act one','A','f3ea432e ad12498d 3dbd4abf'),
 ('pd17','ED09',2097.3, 2123.4,'Moore\'s Law: transistors per chip double every two years, price stays the same','a numeric law → the doubling chart','A','255d4d29'),
 ('pd18','ED09',2229.0, 2269.4,'California: non-competes illegal — accidentally written into its code; New York hires David Dudley Field','legal term defined + map California vs the rest','B','7c824c47 f76a4410'),
 ('pd19','ED09',2327.1, 2371.4,'The Field Code: New York does not adopt it; his brother takes it to California','two-state story New York → California','A','73184e83 f76a4410'),
 ('pd20','ED09',2531.3, 2568.4,'1971: Taiwan is kicked out of the UN (chapter opener)','chapter turn: date + event + map','A','62b64549 7c824c47'),
 ('pd21','ED10',2656.2, 2698.3,'ROC vs CCP in WWII; the "four policemen"; permanent seat on the Security Council','two acronyms defined for the first time; 4-item build over Sunkit\'s quiz','B','ccbe41e5 e2d14822'),
 ('pd22','ED10',2756.2, 2771.3,'The CCP wins the civil war; the ROC government flees to Taiwan','the geography + acronyms the rest of the episode depends on','A','7c824c47 813e40ef'),
 ('pd23','ED10',2826.0, 2845.2,'Who recognises whom: US allies recognise Taiwan as the true China','world split in two blocs','B','e2d14822 813e40ef'),
 ('pd24','ED10',2956.6, 2994.3,'Japan takes Taiwan in the 1890s: railways, ports, hydropower, electricity, schooling','date + map + 5-item list + archive','B','8689427d 1d9a4a1c'),
 ('pd25','ED11',3029.5, 3038.2,'1950s–1965: roughly $1.5 billion in American aid','key number + years','B','255d4d29'),
 ('pd26','ED11',3173.9, 3200.0,'Chiang Kai-shek — a one-party state (and Mao as the contrast)','new person, name hard to catch by ear','A','ccc84f71 0a134429'),
 ('pd27','ED11',3284.6, 3298.8,'The slogan: "Come, come, come to NTU; go, go, go to America"','a quoted slogan','B','fbd84a66 566a46e7'),
 ('pd28','ED11',3359.1, 3411.5,'Asia\'s first special economic zones: import with no tariffs, assemble, export with no taxes','mechanism → flow diagram','B','b76c4b43 5fc04bfb'),
 ('pd29','ED12',3553.8, 3611.7,'July 1971: Kissinger "gets sick" in Pakistan and secretly flies to China','route map with the hidden leg revealed','A','73184e83 64e14029'),
 ('pd30','ED12',3736.4, 3759.2,'Decolonisation in Africa: every new country is a new vote in the General Assembly','map of new states = votes','B','813e40ef a06c4bb3'),
 ('pd31','ED12',3864.2, 3889.6,'July (secret trip) → October (the vote); the US ambassador to the UN is George H.W. Bush','timeline with two events + new person','A','255d4d29 ccc84f71'),
 ('pd32','ED12',3975.7, 4006.0,'The "important question": you need 66%, not a majority — and it is defeated','procedure + a number','A','a06c4bb3 d0fc4b3f'),
 ('pd33','ED13',4106.8, 4239.6,'The walkout: Bush head in hands, delegates dancing (Tanzania); the seat goes to the PRC; Japan pulls recognition the next day, the US in 1979; Chiang Kai-shek: "stay dignified and strengthen ourselves"','he describes a famous photograph; then a cascade of events and a quoted line','A','8be645e2 b5214313 566a46e7 96a54925'),
 ('pd34','ED13',4270.4, 4279.8,'Chiang Ching-kuo, the son','second, similar-sounding name','B','ccc84f71'),
 ('pd35','ED13',4318.3, 4334.8,'His classmate in Moscow: Deng Xiaoping (reveal on the name)','reveal of a new person','B','8e364ca5'),
 ('pd36','ED14',4418.6, 4458.6,'The cabinet of engineers: Sun Yun-suan (energy grid) and K.T. Li (the money guy)','two new people with roles','A','8e364ca5 ccc84f71'),
 ('pd37','ED14',4511.3, 4539.3,'The Ten Major Projects: ports, roads, steel mills, shipyards, railways, nuclear plants','titled list','B','5fc04bfb b76c4b43'),
 ('pd38','ED14',4702.9, 4724.9,'Pan Wen-yuan, an RCA man','new key person + company','A','ccc84f71 b57b4e0e'),
 ('pd39','ED14',4980.9, 5063.5,'Pan\'s verdict: Taiwan offers only cheap labour → move up the value chain; the two answers: four years, ten million dollars','abstract "value chain" + the two key numbers of the decision','A','d0fc4b3f ad12498d'),
 ('pd40','ED15',5144.7, 5160.4,'TSMC, the "Taiwanese shield"','jump to today + geography','B','7c824c47'),
 ('pd41','ED15',5211.4, 5223.7,'A research institute: government-funded, outside government control, spinning out private companies','the mechanism for everything that follows','B','b76c4b43'),
 ('pd42','ED15',5317.9, 5336.8,'The copycats: Silicon Alley, Fen, Wadi, Saxony, Plateau, Glen','six place + name pairs in 19 s','A','5fc04bfb 8a634241'),
 ('pd43','ED15',5374.2, 5404.5,'Boston\'s Route 128: MIT, Harvard, Pentagon money; Digital Equipment Corporation','geography + four names','A','9381944c 9b4c4611'),
 ('pd44','ED15',5499.3, 5608.8,'Clayton Christensen, The Innovator\'s Dilemma: the theory in a chart','new person + an abstract theory','A','2ebb47ad 255d4d29'),
]
T = json.load(open('transcript_pd.json')); R = json.load(open('project/podcast/raw_transcript.json')); FPS = 30
byraw = {w['raw_id']: w for w in T}
def m_at(raw_t, end=False):
    """master time of the first kept word whose raw start >= raw_t (frame-snapped, a few frames early)"""
    for w in T:
        if R[w['raw_id']]['start'] >= raw_t - 0.12: return w
    return None
out = []
for cid, ed, a, b, title, why, rating, refs in S:
    wa = m_at(a); wb = m_at(b)
    t0 = 0.0 if a == 0 else int((wa['start'] - 0.12) * FPS) / FPS
    t1 = (T[-1]['end'] + 1.5) if wb is None else int((wb['start'] - 0.12) * FPS) / FPS
    out.append({'id': cid, 'editor': ed, 'start': round(t0, 4), 'end': round(t1, 4), 'dur': round(t1 - t0, 4), 'first_word': wa['id'], 'first_text': wa['text'],
                'raw': [a, b], 'title': title, 'why': why, 'rating': rating, 'refs': ['ast_…' + r for r in refs.split()]})
for i in range(1, 3): out[i]['start'] = out[i - 1]['end']; out[i]['dur'] = round(out[i]['end'] - out[i]['start'], 4)
json.dump({'fps': FPS, 'length': json.load(open('project/podcast/edl_frames.json'))['length'], 'sections': out}, open('project/podcast/sections.json', 'w'), indent=1)
tot = {}
for o in out:
    print(f"{o['id']} {o['editor']} {o['start']:8.2f}–{o['end']:8.2f} ({o['dur']:6.2f}s) [{o['rating']}] {o['title'][:70]}  «{o['first_text']}»")
    tot[o['editor']] = tot.get(o['editor'], 0) + o['dur']
print({k: round(v) for k, v in tot.items()}, 'total', round(sum(tot.values())), 's')
