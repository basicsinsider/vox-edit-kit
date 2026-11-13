import sys,re
D='work/pd11/src/'
src=open(D+'pd11.src.html').read()
open('compositions/pd11.html','w').write(src.replace('__NJ_D__',open(D+'nj_d.txt').read()))
css=src[src.index('    #root {'):src.index('    /* sc1 steeples */')]
js=src[src.index('    const tl = gsap.timeline'):src.index('    /* =================== SC1')]
for sid in sys.argv[1:]:
    s=open(D+sid+'.src.html').read()
    s=s.replace('/*__COMMON_CSS__*/',css).replace('/*__HELPERS__*/',js.replace('611',sid[2:]+'1').replace('612',sid[2:]+'2'))
    open('compositions/%s.html'%sid,'w').write(s)
