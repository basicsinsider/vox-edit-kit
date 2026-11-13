"""Master-time words: pd_words.py <t0> <t1>  ->  text@start per word (master seconds, transcript_pd.json)."""
import json, sys
a, b = float(sys.argv[1]), float(sys.argv[2])
print(' '.join(f"{w['text']}@{w['start']:.2f}" for w in json.load(open('transcript_pd.json')) if a <= w['start'] <= b))
