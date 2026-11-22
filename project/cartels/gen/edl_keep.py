# Keep list for the US vs Cartels raw VO (project/cartels/raw_transcript.json, Parakeet, 4249 words, input/vo_raw.wav 1486.15 s).
# Written by the lead after reading every phrase (work/asr/ct/dump.txt). Each entry:
#   (start phrase, time hint s, end phrase, note [, {in/out} override]) -> kept words = first match of `start` at/after the hint
#   (and after the previous range) .. end of the first match of `end` at/after that start. Everything not listed is cut.
import json, re
SPEC = [
 # ---- cold open / chapter 1 ----
 ("That's a baseball game in Mexico", 0, "in the middle of the city", "cold open; '…cartel gunmen are setting fire.' 1st take cut"),
 ("And all over the town cartel gunmen were setting cars", 0, "had come for one man", "2nd take"),
 ("Al Chapo Isidro And yes", 0, "small stuff with the cartel", "1st 'Al Chapo' cut"),
 ("Then he worked his way up to being a gunman", 0, "Beltrand Levas", "repeated 'Then he worked his way up to being' cut"),
 ("These brothers were partners", 0, "the same team the Sinaloa Cartel", ""),
 ("but in 2008 something interesting happened", 0, "This war is where he makes his name", "'But in tot,' cut"),
 ("In 2010 his men set up an ambush", 0, "straight shot towards Arizona", ""),
 ("cocaine meth heroin and later on fentanyl", 0, "matters the most for this story", "1st 'Cocaine, meth, heroin, and' cut"),
 ("He had become so big", 0, "He had become so big", "1st take of the line (keep only the opening words)"),
 ("that by 2013 even the US Treasury", 0, "its own cartel Meaning", "'but he had become so big' cut"),
 ("in the US eyes", 0, "how he got it", "2nd 'meaning' cut"),
 ("You see his name comes from a slang", 0, "how he operates", ""),
 ("Now the weirdest part of his story", 0, "a couple of years earlier in 2012", "'he had been already' cut (2nd 'he had' kept)"),
 ("he had already been charged with drug trafficking", 0, "in your own head", ""),
 ("but for years he just kept operating", 0, "if the government thinks a criminal like government was thinking about these cartels before this order", "'But for here's' cut"),
 ("then the government's job is basically to arrest you", 0, "with these terrorist cartels Meaning", "'Then the government job is basically to' cut"),
 ("legally speaking the government is treating", 0, "had to do with drugs", "'legally meaning, or' cut"),
 # ---- tariffs, transfers ----
 ("You see unlike China or India or Korea", 0, "running their cartels from prison", "1st take of the American-prison line cut"),
 ("Well they can't really do all that when they're in an American prison", 0, "spy drones over Mexico", "2nd take kept whole"),
 ("Looking for these fentanyl laps These drones", 0, "knew about the flight", "'looking for these fentanyl fentanyl laps.' cut"),
 ("This is where we need to talk about the CIA mission", 0, "different set of rules than the military", "'This is where we know' cut"),
 ("The military has strict laws about who it can and can't work with", 0, "can't work with", "2 false starts cut"),
 ("The CIA can pretty much work with anybody", 0, "from the Mexican border", "1st CIA take cut"),
 ("It was called the joint intraagency task force counter cartel", 0, "this January", "1st 'It was called the joined intraagency tasks force.' cut"),
 ("And the general who runs it has compared the mission to the campaigns against Al Qaeda and ISIS", 0, "here's your guy", "1st 'and the general…the ISIS' take cut"),
 ("here's where he sleeps", 0, "the US military started", "'here's where he' cut"),
 ("blowing up small boats", 0, "were carrying drugs", "'bull the US military started' cut"),
 ("now these strikes are controversial but as of last month", 0, "Officials who have talked to reporters behind the scenes", "'Now, these strikes are controversial, but it is' cut"),
 ("have said that the CIA intelligence", 0, "catching El Mencho", "'have said that the CI int' cut"),
 ("and of course just two days after the raid in the State", 0, "around the Mexican federal government", "'And then of course just two days after the raid' cut"),
 # ---- Chihuahua ----
 ("the way around was a man named", 0, "one problem with this guy", "'The way around was a main' cut"),
 ("a few months before CIA started working with him", 0, "helping the Americans right away", "'A few months before this, the CIA' cut"),
 ("first he introduces an American to the state police", 0, "to the state police", "'First he' cut"),
 ("and tells them that this guy is here to help build", 0, "so they can blend in easily", "1st 'and tells them that this guy is here' cut"),
 ("More importantly though they usually have tablets with them on these raids", 0, "give directions and intelligence", "1st tablets take + 'And apparently this is' cut"),
 ("but on one raid on a cartel safe house one of the Americans", 0, "to hide their faces", "3 stuttered starts cut"),
 ("They find the lab and it's empty", 0, "been used recently", "1st 'They find the lab, but it's empty.' cut"),
 ("With gas tanks and tubes of chemicals everywhere", 0, "falls about 300 feet", "1st 'with gas tanks…chemical everywhere' cut"),
 ("Killing everyone inside including two officers", 0, "in a firefight with the Navy", "1st 'killing everyone inside' cut"),
 # ---- the capture ----
 ("So piece by piece the people around him", 0, "had pretty cool names", "1st 'So piece by piece.' cut"),
 ("One is the National Guard Special Forces unit who go by wolves", 0, "who go by wolves", "1st wolves take cut"),
 ("and the other is the Army Special Forces unit", 0, "at the start comes from", "'And the army' cut"),
 ("A firefighter told reporters", 0, "treat their wounded", "repeated 'That's where the baseball game…' cut"),
 ("and while all of that was going on Al Chapo Isidro", 0, "plane to Mexico City", "2 false starts cut"),
 ("the next morning government put out this video", 0, "stay in Mexico for very long", "1st 'The next morning government put out this' cut"),
 ("He has been charged in Washington DC since 2012", 0, "slowed down just a bit", "1st 'He has been charged in Washington, DC.' cut; to the end"),
]
def norm(t):
    return re.sub(r"^[^\w$%]+|[^\w%]+$", "", t.lower().replace("’", "'"))

def resolve(path='project/cartels/raw_transcript.json', with_overrides=False):
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

if __name__ == '__main__':
    w = json.load(open('project/cartels/raw_transcript.json'))
    for a, b, n in resolve():
        print(f"w{a}-w{b} {w[a]['start']:.2f}-{w[b]['end']:.2f} | {' '.join(x['text'] for x in w[a:a+8])} ... {' '.join(x['text'] for x in w[b-5:b+1])}")
