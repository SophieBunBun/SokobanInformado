from algoritmos import *
from sokoban import *

linha1="##########\n"
linha2="#........#\n"
linha3="#..$..+..#\n"
linha4="#........#\n"
linha5="##########\n"
mundoS=linha1+linha2+linha3+linha4+linha5
s=Sokoban(situacaoInicial=mundoS)
res, W, exp = IW_beam_search(s,s.h_inutil_2)
print('Expandidos:',exp)
