from algoritmos import *
from sokoban import *

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
    print(exp)