"""Build compositions/ivs01.html from project/ivan/gen/ivs01_template.html (inlines map paths). Run from repo root."""
import json
d = json.load(open('assets/ivan/ivs01/derived/paths.json'))
need = ['moscow', 'kyiv', 'kharkiv', 'belgorod', 'voronezh', 'ryazan', 'kursk', 'nizhny_novgorod', 'saratov', 'ivanovo',
        'rostov_on_don', 'volgograd', 'engels_airbase', 'dyagilevo_airbase', 'ivanovo_severny_airbase']
m = {'ee': {'ru': d['ee']['ru'], 'ua': d['ee']['ua'], 'places': {k: d['ee']['places'][k] for k in need}}, 'ru': {'ru': d['ru']['ru'], 'ua': d['ru']['ua']}}
src = open('project/ivan/gen/ivs01_template.html').read().replace('__PATHS__', json.dumps(m, separators=(',', ':')))
open('compositions/ivs01.html', 'w').write(src)
print('compositions/ivs01.html', len(src))
