from algoritmos import *
from sokoban import *

 	

p=ProblemaGrafoHs()
res, exp = beam_search(p,2,p.h1)
if res==None:
    print('Nope')
else:
    print(res.path_cost)

p=ProblemaGrafoHs()
res, exp = beam_search(p,2,p.h1)
if res==None:
    print('Nope')
else:
    print(exp)


p=ProblemaGrafoHs()
res, exp = beam_search(p,2,p.h1)
if res==None:
    print('Nope')
else:
    print(res.solution())

p=ProblemaGrafoHs()
res, W, exp = IW_beam_search(p,p.h2)
if res==None:
    print('Nope')
else:
    print(W)


linha1="##########\n"
linha2="#........#\n"
linha3="#..$..+..#\n"
linha4="#........#\n"
linha5="##########\n"
mundoS=linha1+linha2+linha3+linha4+linha5
s=Sokoban(situacaoInicial=mundoS)
res, exp = beam_search(s,1,s.h_inutil_1)
if res:
    print(res.solution())
else:
    print('No solution!')

linha1="##########\n"
linha2="#........#\n"
linha3="#..$..+..#\n"
linha4="#........#\n"
linha5="##########\n"
mundoS=linha1+linha2+linha3+linha4+linha5
s=Sokoban(situacaoInicial=mundoS)
res, exp = beam_search(s,3,s.h_inutil_2)
if res:
    print(res.solution())
else:
    print('No solution!')

 	
linha1="##########\n"
linha2="#........#\n"
linha3="#..$..+..#\n"
linha4="#........#\n"
linha5="##########\n"
mundoS=linha1+linha2+linha3+linha4+linha5
s=Sokoban(situacaoInicial=mundoS)
res, W, exp = IW_beam_search(s,s.h_inutil_2)
print('Expandidos:',exp)