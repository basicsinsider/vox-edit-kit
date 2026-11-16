# Keep list for the NVIDIA ("Is the chip ban working?") raw takes — project/nvidia/raw_transcript.json (8372 words; the three
# parts on one raw timeline, see parts.json). Written by the lead after reading every phrase (media/dump_p*.txt) and
# re-transcribing unclear windows (gen/asr_win.sh). Each entry:
#   (part, start phrase, time hint in PART-local seconds, end phrase, note [, {in/out} override in part-local seconds])
# kept words = first match of `start` at/after the hint .. end of the first match of `end` at/after that start.
# Everything not listed is cut (false starts, retakes, slips, asides to the editor). Phrases use the RAW ASR spelling.
import json, re
SPEC = [
 # ---------------- part 1 (face cam) ----------------
 (1, "Is the chip ban actually working", 4.4, "wasn't supposed to Again", "cold open, 2nd take of the question"),
 (1, "We don't even know if he knew", 30.6, "going on or not", "2nd take"),
 (1, "But considering that the government", 42, "success or not", ""),
 (1, "take a look at this video from a few months ago", 60.3, "from a few months ago", "'Just a few months ago,' + 'It's' cut"),
 (1, "If you walked into a shopping mall", 61, "to make a server", "'and that server is then sold to a company or a research.' false start cut"),
 (1, "And that server is then sold to an AI company", 99, "doing similar things", "retake"),
 (1, "So if the chips are already", 145, "all the world's chips", "", {"out": 164.70}),
 (1, "Before the ban that figure", 165.5, "just around 17%", "1st 'Before the ban' cut", {"in": 165.78}),
 (1, "And as if this wasn't bad enough Chinese AI models are now catching up to the US", 174, "insanely cheap", "2nd take"),
 (1, "So when you look at the whole picture it kinda raises", 201, "why do we still have it", "4th take ('What am I' cut)"),
 (1, "So to judge this question", 211, "behind the chip ban", ""),
 (1, "What was the hope for the people", 217, "a mistake or not", "short 'What was the hope?' cut"),
 (1, "But before we do all of that let me just quickly", 226, "what the Americans are making", "2nd take"),
 (1, "This law was passed on October 7th", 250.5, "October 7th 2022", "'It was passed.' cut"),
 (1, "now I'm sure you guys know this", 259.6, "President Biden initially introduced", "2nd take"),
 (1, "Now we'll talk about all this back and forth", 289, "high-tech US chips", "'But legally speaking, I'll go cut that out.' cut"),
 (1, "Now listening to all of this", 300, "fair part of that whole equation", ""),
 (1, "but before that I want to make clear", 319, "like race or gender", "repeated 'But before that,' cut; 'then that's perfectly leader' slip cut"),
 (1, "Then that's perfectly legal in the United States", 335, "to another country that's perfectly legal", ""),
 (1, "but for argument let's go deeper", 347.5, "chip ban was ever introduced", "first 'But' cut"),
 (1, "And few companies that are allowed", 360, "France calling this out too", "'and then we have E' cut"),
 (1, "and then we even have companies in the global south", 385, "think of chips like Urani", "(he says 'uranium')"),
 (1, "now I'm sure you guys know that you can do a lot of good things with uranium", 403, "ban is working or not", "2nd take"),
 (1, "so to figure out this answer we first need to agree", 448, "little bit of a different answer", "repeat cut"),
 (1, "So I have picked out the top three answers", 493, "keep score with me", "after the water break"),
 (1, "Now you might have noticed there's a fourth row", 510, "and it's empty", ""),
 (1, "I'm just leaving it there blank on purpose", 522, "what success should look like", "3rd take"),
 (1, "So if we get to that we'll fill that in", 537.9, "Let's get started", "3rd take"),
 (1, "Now the first thing some of you guys might be wondering", 543, "doesn't actually make the chips", "'Now the first question some of you guys might be' cut"),
 (1, "In fact NVIDIA chips aren't even made in the United States", 551.5, "gets the chips and who doesn't", "2nd take"),
 (1, "And on top of that the machines and software that are being used to design and manufacture these chips in Taiwan", 597, "need American stuff to make chips", "3rd take ('Let me say that again')"),
 (1, "so now that we have that out of the way", 633, "chip ban for a reason", ""),
 (1, "Let's look at how it was started", 656, "how it was started", "'Let's look at some numbers.' cut"),
 (1, "As I said before the ban was started in 2022 and it started by the government", 662, "do whatever it wants", "2nd take"),
 (1, "at the time this band was introduced", 693, "at least financially speaking", ""),
 (1, "China at that point was about a quarter of their entire sales", 723, "without breaking the law", "retake ('Okay, let me do that again')"),
 (1, "of course the administration was not happy", 762, "this new chip is now illegal", ""),
 (1, "So guess what NVIDIA does Within a few days or I think a few weeks they design another chip which", 781, "continued for a while and", "2nd take; 'it it' stutter", {"out": 811.14}),
 (1, "it became so bad that at one point", 811.4, "going into China", "PC aside kept", {"in": 811.48}),
 (1, "and this is the kind of stuff that usually happens", 822, "always slow to catch up", "'And this something usually h' cut"),
 (1, "was considering PlayStation as a supercomputer", 837, "being overly broad", "'So at one point, government was con-' false start cut; in before the 2nd 'so at one point'", {"in": 835.80}),
 (1, "None the less That's not the focus", 858, "story at hand", "one 'Nonetheless'"),
 (1, "Now even after the ban chips were still getting into China", 869, "really hard to police", "('banned, and it was happening' runs together - kept whole)"),
 (1, "First of all it's just so many people doing this", 945, "doing this", ""),
 (1, "how do you stop that many people", 949, "for back then prices but", "'How do you spot' cut"),
 (1, "You could sell it for a double the price overseas", 999, "how easy it is to carry an iPhone", "repeat cut"),
 (1, "from the government's point of view first of all", 1016, "do they really want to be", "'So from government points of view,' cut"),
 (1, "spending those resources on individual people", 1022.5, "making 300 bucks", "'spent uh' cut", {"in": 1022.335}),
 (1, "he or she is not running like a dedicated smuggling operation", 1035, "smuggling operation", "'He's not running like, or' cut", {"in": 1035.935}),
 (1, "That's why the government has really focused", 1048, "after people who are", "'g-' stutter cut", {"out": 1054.19}),
 (1, "doing this in a big way", 1054.3, "server companies in the United States", "'Prosecutors say this.' cut", {"in": 1054.50}),
 (1, "Now the case is still ongoing so I'll refrain", 1063, "he would use", "stammered 'hair.. ha.. ha..' cut", {"out": 1095.22}),
 (1, "hai dryer to peel off the", 1095.6, "peel off the", "'suits uh' cut", {"in": 1095.74, "out": 1097.375}),
 (1, "barcode from real chips", 1098, "while he was doing all of this", "'the the' -> one", {"in": 1098.0}),
 (1, "the warehouse camera was recording", 1108, "especially in South East Asia", ""),
 (1, "That means if the goal of the first metric", 1145, "it's not working", ""),
 (1, "So if I stop the video right here", 1174, "researching this thing initially", "'Why would we still' cut"),
 (1, "but it does raise an important question", 1184, "keeping this policy in place", "'And this is where.' cut"),
 (1, "So there has to be something that we're missing", 1200, "the US has in AI", "'Equation is different.' cut"),
 (1, "If you look at it this way then the equation changes", 1247, "trying to achieve", "end of part 1 (note to the editor cut)"),
 # ---------------- part 2 (audio only) ----------------
 (2, "Let me explain what I mean", 0, "This is called training", "'I guess a pretty easy definition.' aside cut"),
 (2, "It sounds but to do this type of training", 21.5, "how big this system is", "(he says 'It sounds pretty simple, but')"),
 (2, "NVIDIA's newest system comes as a rack", 33, "normal people have", "'And one rack weigh' cut"),
 (2, "and one rack weighs around", 42, "I'm sure in other countries'", "'home homes' -> one"),
 (2, "homes use less electricity", 55, "a frontier AI company needs", "'like 1,000,' cut"),
 (2, "like thousands of these racks", 71, "months on all because they didn't have enough chips", "repeat cut"),
 (2, "And the founder himself is kind of admitting", 193, "American labs because", "'they are' cut"),
 (2, "they only have one twentieth", 206.6, "They have more", "'ER' cut"),
 (2, "AI researchers than the United States", 213.6, "we'll talk about that in a second", "(he says 'that's what counts')"),
 (2, "But the third way to measure the lead is in terms of time", 300, "figure out a way to distill these models", "2nd take"),
 (2, "It's now a lot quicker for AI companies", 644.3, "making the same argument but", "repeat cut; 'Jen W' cut"),
 (2, "Jensen Huan is definitely biased", 766, "more money for his company", "'Rightly slow.' cut"),
 (2, "Rightly so Every CEO", 775, "according to the US government", ""),
 (2, "some private companies actually put that estimate", 855, "strongest chip they have but", "'Some private and' cut; 'they are not' cut"),
 (2, "they were now allowed to sell", 895, "you can argue", "'it's it's' -> one"),
 (2, "it's a good plan right", 921, "allowed to sell into China", "'Right now, roughly 600,000 of these' false start cut"),
 (2, "right now roughly 600,000 chips are sitting", 945, "company could produce 100 chips and", "'only three of them or' cut"),
 (2, "only 30 of them would work", 1020.5, "That way they can make", "'make.. make' -> one", {"out": 1048.617}),
 (2, "money at a lower price", 1049, "Topic for a different video the basics is", "'is is' -> one", {"in": 1049.842}),
 (2, "the most important thing is you need a lot of volume", 1060.8, "we can debate about", "'common secret' cut"),
 (2, "commerce secretary is not actually helping", 1250, "so close to American models", "end of part 2"),
 # ---------------- part 3 (face cam) ----------------
 (3, "The funniest part of all this", 2, "out of the country", "'That means these Chinese AI employees,' cut"),
 (3, "that means AI employees are actually flying", 17, "Chinese access to these data centers", "repeat cut"),
 (3, "That way China will not be able to have that as an advantage during the war", 90.5, "understand the whole thing better", "2nd take"),
 (3, "Keeping the drama of the affair", 130, "let us know", "'uh' cut", {"in": 130.117}),
 (3, "it's interesting always reading comments", 140, "see you in the next video", "sign-off; 'Uh' cut", {"in": 140.187}),
]
PARTS = json.load(open('project/nvidia/parts.json')); OFF = {p['part']: p['offset'] for p in PARTS}

def norm(t):
    return re.sub(r"^[^\w$%]+|[^\w%]+$", "", t.lower().replace("’", "'"))

def resolve(path='project/nvidia/raw_transcript.json', with_overrides=False):
    w = json.load(open(path)); toks = [norm(x['text']) for x in w]
    def find(ph, i0):
        p = [norm(t) for t in ph.split()]
        for i in range(i0, len(w) - len(p) + 1):
            if toks[i:i + len(p)] == p: return i, i + len(p) - 1
        raise ValueError(f"not found: {ph!r} after w{i0}")
    keep = []; last = -1; ov = {}
    for part, s, hint, e, note, *o in SPEC:
        g = hint + OFF[part]
        i0 = next(i for i, x in enumerate(w) if x['start'] >= g - 1.0)
        a, _ = find(s, max(i0, last + 1)); _, b = find(e, a)
        if w[a]['part'] != part or w[b]['part'] != part: raise ValueError(f"crosses parts: {s!r}..{e!r}")
        if b - a > 1200: raise ValueError(f"suspiciously long range {s!r}..{e!r}: w{a}-w{b}")
        keep.append((a, b, note)); last = b
        if o: ov[(a, b)] = {k: v + OFF[part] for k, v in o[0].items()}
    return (keep, ov) if with_overrides else keep

if __name__ == '__main__':
    w = json.load(open('project/nvidia/raw_transcript.json')); n = 0
    for a, b, note in resolve():
        n += b - a + 1; p = w[a]['part']
        print(f"p{p} w{a}-w{b} {w[a]['start']-OFF[p]:.2f}-{w[b]['end']-OFF[p]:.2f} | {' '.join(x['text'] for x in w[a:a+9])} ... {' '.join(x['text'] for x in w[max(a,b-4):b+1])}")
    print('kept words', n, 'of', len(w))
