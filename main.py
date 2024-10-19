from algoritmos import *
from sokoban import *

p=ProblemaGrafoHs()
res, exp = beam_search(p,2,p.h1)
print(exp)
if res==None:
    print('Nope')
else:
    print(res.path_cost)

linha1="##########\n"
linha2="#........#\n"
linha3="#..$..+..#\n"
linha4="#........#\n"
linha5="##########\n"
mundoS=linha1+linha2+linha3+linha4+linha5
s=Sokoban(situacaoInicial=mundoS)
res, exp = beam_search(s,3,s.h_inutil_2)
print (exp)
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
