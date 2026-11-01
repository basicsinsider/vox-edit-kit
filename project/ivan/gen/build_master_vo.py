"""Master timeline = edited VO with silent slots for the script's three clip inserts.
vo_ivan_master.wav (VO samples untouched, silence inserted), transcript_ivan_master.json (times shifted),
project/ivan/inserts.json (slot start/dur in master time + what goes there)."""
import json, numpy as np, soundfile as sf
E = json.load(open('project/ivan/edl_frames.json'))
by = {}
for s in E['segments']: by.setdefault(tuple(s['w']), s)
INS = [((392, 410), 8.0, 'protest chants (script: insert 0:02-0:10 of the BBC doc)'),
       ((1419, 1449), 18.0, 'dubbed video clip (script: BBC doc 0:58-1:16) after Kirillov attack line'),
       ((1804, 1875), 11.0, 'fast-paced clip (script: BBC doc 4:05-4:16) after the cargo-truck line — Spiderweb footage')]
x, sr = sf.read('vo_ivan.wav', dtype='int16')
pts = sorted((by[k]['edit_in'], d, n) for k, d, n in INS)
out = []; prev = 0; shift = 0.0; slots = []
for t, d, n in pts:
    i = round(t * sr); out += [x[prev:i], np.zeros((round(d * sr), x.shape[1]), np.int16)]; prev = i
    slots.append({'edit_t': t, 'master_start': round(t + shift, 3), 'dur': d, 'what': n}); shift += d
out.append(x[prev:]); y = np.concatenate(out); sf.write('vo_ivan_master.wav', y, sr, subtype='PCM_16')
def m(t):
    s = 0.0
    for p in slots:
        if t >= p['edit_t'] - 1e-6: s += p['dur']
    return round(t + s, 3)
w = json.load(open('transcript_ivan.json'))
for q in w: q['start'], q['end'] = m(q['start']), m(q['end'])
json.dump(w, open('transcript_ivan_master.json', 'w'))
json.dump({'length': round(len(y) / sr, 3), 'slots': slots, 'note': 'facecam (edited-VO time) = master time minus the durations of slots that start at or before it'}, open('project/ivan/inserts.json', 'w'), indent=1)
print(len(y) / sr, slots)
