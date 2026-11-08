# Keep list for the Paraguay raw take (project/paraguay/raw_transcript.json, 6232 words incl. the 91-95 s patch).
# Written by the lead after reading every phrase (project/paraguay/media/dump.txt). Each entry:
#   (start phrase, time hint s, end phrase, note) -> kept words = first match of `start` at/after the hint .. end of the first
#   match of `end` at/after that start. Everything not listed is cut (false starts, retakes, slips, edit notes, asides).
# resolve() turns it into inclusive word-id ranges (same shape as Ivan's KEEP).
import json, re
SPEC = [
 ("That's a congressman in Paraguay", 0, "house arrest instead", "cold open (over the X clip)"),
 ("The country is falling apart", 18, "this singular bank", "'falling up' slip cut"),
 ("and just for comparison only about 10% of US", 36, "60% figure", "2nd take of 'and just for comparison'"),
 ("You'd have to add up", 49, "plus the smaller ones", "'You'd have to add in' false start cut"),
 ("and then some regional ones and then you get", 55, "true scale of the problem", "repeated 'and then some regional ones' cut"),
 ("Because you see these individual", 90, "individual", "line the full-file ASR missed (patched)"),
 ("accounts that people had", 93, "under the national insurance", "'accounts, accounts' repetition cut"),
 ("Much like FDIC that we have here", 100, "that we have here", "2nd 'much like FDIC' kept"),
 ("and because of this insurance 97%", 105, "how we got here", "repeated 'and because of this insurance' cut"),
 ("Now I don't know about you guys but to me Paraguay has been", 155, "especially since the World Cup", "3rd take (after 'let me do the sentence again')"),
 ("they did surprisingly well in the Soccer World Cup and then they became", 170, "whole saga was", "3rd take of the World Cup line"),
 ("After this", 187, "After this", "'twit' slip cut"),
 ("tweet was put out", 188, "skin color", "'So, yeah. Anyways. Okay, let me go and see...' cut"),
 ("Now I feel like the country", 207, "But that's not the case", "repeated 'But but that's not the case' cut"),
 ("outside of this joke", 218, "they wanted to carry out", "'Even then,' cut"),
 ("It was on the right path and it was being trusted", 252, "world investors", "take 1"),
 ("and the economy was growing", 262, "the economy was growing", "from the retake ('Okay, let me say that again' cut)"),
 ("the first half of this year was the strongest growth it has ever had", 266, "country's history", "final take"),
 ("so good news was all around but among all this good news there", 284, "no one knew about", "2nd take"),
 ("That news was that one of the biggest banks in the country was hiding", 294, "its problems", "final take"),
 ("So let me give you some background", 316, "important parts of the story", "improvised '1950, I'm just kidding' joke kept"),
 ("The bank was started a long time ago", 329, "that's what the company was", "'what was it called? I forget the name. Freak.' cut"),
 ("It was called Credit Central", 353, "Credit Central", "name lands after the cut"),
 ("But since this was not a bank", 375, "the leadership changes", "'Uh' cut"),
 ("a new member of the family", 394, "this company was producing", "'like a global not a glob and try to c' cut"),
 ("and try to create like a national conglomerate", 405, "where the problem starts from", "'But nonetheless, let's continue with the story' cut"),
 ("By 2020 around COVID times", 478, "the bank that we are talking about", "edit note ('hopefully we show the logo...Edit node over') cut"),
 ("Weno", 505, "Weno", "the bank's name"),
 ("This was gonna be like a modern bank", 515, "online banking", ""),
 ("This new bank starts doing really well", 545, "online focused", "after 3 false starts; 'So it has everything...was want' cut"),
 ("And on top of that it's running like crazy promos", 557, "problem down the line", "'And that's why I'm sharing with you guys' cut"),
 ("for now the bank is on a very good trajectory", 622, "for any company when the president of the country", "'Now,' cut"),
 ("when the president of the country is one of your investors", 688, "buying something that's four times bigger", "repetition cut"),
 ("Now this acquisition did not go according to plan", 748, "I'm sure other real estate", "'other type of extent expenses...' cut"),
 ("And on top of that the bank they buy was struggling", 773, "was struggling", ""),
 ("and on top of that the bank had already used a lot of their cash to survive", 783, "much bigger than them and on top of that", "2nd take; in after the 'uh' (RMS)", {"in": 783.66}),
 ("it's in a much worse position", 794, "should have been", "'it's this' cut"),
 ("luckily for Wano though", 830, "Institute for Paraguay", "2nd take ('for Uano though' false start cut)"),
 ("this is just pensions for citizens", 862, "Now on top of this there was also", "'Pensions for' false start cut"),
 ("a condition around the fund", 911, "from government agencies", "'a law. When I say law, there was also' cut"),
 ("Now with the benefit of hindsight", 972, "In Paraguay", "'they have this un of the requirement' cut"),
 ("This is like a pretty strong law", 1001, "given out in loans", ""),
 ("Now all this time until the very end", 1029, "was saying that", "'this was' slip cut"),
 ("it was following all these ratios", 1033, "which no one actually did until recently", "repeated 'if you start looking closely...' cut"),
 ("it's like suspiciously good", 1058, "guess what it was", ""),
 ("now this is where we come back to the beginning of the story and remember how", 1097, "this is not illegal", "2nd take; 'Uh' cut"),
 ("a bank can technically give money", 1136, "that's illegal Now", "first 'Now' kept, then a whispered 2nd 'now' + 12 s pause cut"),
 ("this law is about to become", 1170, "doing stuff illegally", "'The group company,' cut next", {"in": 1171.22}),
 ("the family that owns the whole thing", 1214, "not supposed to loan the money to", ""),
 ("In reality this problem should not", 1256, "bad mistake on our part", "'This was this was' repetition cut"),
 ("this was a bad loan", 1285, "when I walked into the class", "improvised accounting-teacher story kept; 'or when everyone walked into the class' cut"),
 ("was basically you guys know what happens", 1296, "this is bad loan we're gonna", "'we gonna' cut"),
 ("write it down They just issued", 1328, "too big to fail", "'Okay all right' + 2 failed takes of the 300 million line cut; 'fail.' really ends 1347.4", {"out": 1347.62}),
 ("By the end of it all they had given out more than 300 million dollars using this", 1411, "This actually has a name Merry Gound", "final take"),
 ("Now luckily the central bank did catch on", 1426, "the loan was a piece of shit", "'Can we bleep the shit part?' = Krish's edit note: bleep 'shit' (DECISIONS)"),
 ("No one actually wants to buy it", 1494, "This new company had no money", "'It had like' repetition cut"),
 ("it had like $100,000 less", 1529, "somehow ends up in this new company", "'that this new company uses.' cut"),
 ("So around $79 million", 1542, "paying us $80 million for it", "'So maybe you just let it let us let us survive even more' cut"),
 ("people on the ground who were investigating", 1563, "sent the report to", "'The people,' + 'the CEO or' cut"),
 ("the head of the central bank But guess what", 1580, "understand what's going on here", ""),
 ("Investigations are still going on so I don't", 1609, "what's going on here", "'Maybe, okay? Maybe.' + repeated line cut"),
 ("So now I'm sure some of you guys", 1628, "buried by the head of the bank", "'How does this whole thing fall apart? Well' false start cut"),
 ("the guy who wrote", 1640, "and they just kept on investigating", "'or two months after nothing was made of this report' cut"),
 ("to find everything else", 1668, "the media that the country has", "repeated 'kept on investigating' cut"),
 ("Now when this report is made public", 1685, "it just", "'sp' slip cut"),
 ("breaks the political", 1706, "breaks the political", "stammered first 'back' (1710.34-1710.48) cut", {"out": 1710.31}),
 ("back of the country", 1710, "is this bank actually good", "'done? Because this is one of the biggest bank' cut", {"in": 1710.50}),
 ("Cause this is one of the biggest banks in the country", 1734, "biggest banks in the country", ""),
 ("Now while all this investigation is going on", 1758, "go through their checklist", "'Well, for Paraguay, is that how you say it? Paraguay, yeah.' cut"),
 ("Well for Paraguay that assessment", 1824, "Or if the whole government is like that", "'or if the whole whole whole sore...' cut"),
 ("So that's why the central bank could not", 1872, "you're gonna be criminally held liable", "1st phrasing kept"),
 ("whenever the thing blows apart", 1917, "criminal charges in the future", "'Or you could be criminally held liable' cut; 'So if you combine all this.' false start cut", {"in": 1917.80}),
 ("So if you combine all of this", 1938, "Everyone who", "'deb' slip cut"),
 ("deposited with the bank", 1963, "in the future", "'Bank's done.' false start cut"),
 ("Well one thing was clear", 1988, "as I said before", "'a lot of people had the money in' cut"),
 ("lot of people had their money in this bank", 2002, "protest all over the place", ""),
 ("Now regulators have come up with different solutions as to how", 2045, "they don't have any of their accounts", "1st 'Now regulators...' cut; 'They' cut"),
 ("I'm sure they'll figure it out", 2063, "I'm sure they'll figure it out", "'They this was their first bank account, so let's see.' cut (stutter run into the next word); out before the next 'but'", {"out": 2065.95}),
 ("But it creates chaos uncertainty and people are scared", 2073, "rejects his resignation and then", "'it's creates chaos...actually going surprise' cut"),
 ("impeaches him", 2091, "impeaches him", "'indicts him, or wait,' cut"),
 ("so now he", 2097, "investigation is ongoing", "retake start 'The Senate rejects his uh resignation and then impeach him,' cut"),
 ("the head of the board former CEO", 2101, "involved in different", "'The board' cut"),
 ("different companies and banks", 2113, "we'll find out more but definitely", "'oh different' cut (RMS)", {"in": 2115.04}),
 ("a very interesting story that came out", 2121, "so very young", "repeated 'definitely' cut"),
 ("people do stupid shit when they're young", 2136, "not happy about so she", "first 'so people do stupid shit very' cut"),
 ("she's going viral on social media", 2151, "already mad about", "end"),
]

def norm(t):
    return re.sub(r"^[^\w$%]+|[^\w%]+$", "", t.lower().replace("’", "'"))

def resolve(path='project/paraguay/raw_transcript.json', with_overrides=False):
    w = json.load(open(path)); toks = [norm(x['text']) for x in w]
    def find(ph, i0):
        p = [norm(t) for t in ph.split()]
        for i in range(i0, len(w) - len(p) + 1):
            if toks[i:i + len(p)] == p: return i, i + len(p) - 1
        raise ValueError(f"not found: {ph!r} after w{i0}")
    keep = []; last = -1; ov = {}
    for s, hint, e, note, *o in SPEC:
        i0 = next(i for i, x in enumerate(w) if x['start'] >= hint - 1.0)
        a, _ = find(s, max(i0, last + 1)); _, b = find(e, a)
        if b - a > 400: raise ValueError(f"suspiciously long range {s!r}..{e!r}: w{a}-w{b}")
        keep.append((a, b, note)); last = b
        if o: ov[(a, b)] = o[0]
    return (keep, ov) if with_overrides else keep

KEEP = None
OVERRIDES = {}
if __name__ == '__main__':
    w = json.load(open('project/paraguay/raw_transcript.json'))
    for a, b, n in resolve():
        print(f"w{a}-w{b} {w[a]['start']:.2f}-{w[b]['end']:.2f} | {' '.join(x['text'] for x in w[a:b+1])[:110]} ... {w[b]['text']}")
