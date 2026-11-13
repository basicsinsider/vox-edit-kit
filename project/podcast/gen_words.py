"""Print raw-transcript words with ids: gen_words.py <first_id> <last_id>  ->  id:text(start) ..."""
import json, sys
w = json.load(open('project/podcast/raw_transcript.json')); a, b = int(sys.argv[1]), int(sys.argv[2])
print(' '.join(f"{x['id']}:{x['text']}({x['start']:.2f}{'|gap%.1f' % (w[x['id']+1]['start']-x['end']) if x['id']+1 < len(w) and w[x['id']+1]['start']-x['end'] > 0.6 else ''})" for x in w[a:b + 1]))
