#Creiamo il programma che fa stessa cosa di random.shuffle

import random



lista=['a', 'b', 'c', 'd', 'e', 'f', 'g']


def Franco_shuffle(lista):

    lung=len(lista)

    if lung==1:
        return [lista]
    
    pos_random=int(random()*lung)                   #numero randomico tra 0 e 1
    scelto=lista(pos_random)

    new_l=lista[:pos_random]+lista[pos_random+1:]

    return lista(pos_random)+Franco_shuffle(new_l)



L_mes=Franco_shuffle(lista)

print(L_mes)