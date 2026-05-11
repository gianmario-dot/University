#10 righe di compito
#presa una lista con n mumeri interi con k cifre 
# tra 0 e n_max dato dall'utente
#utente fornisce numero cercato (tra 0 e 9) 
#programma deve dire quante volte appare nella lista

import random

n_cifre=int(input('Quante cifre devono avere i numeri? \n'))
n_input=int(input('N_max \n'))
n_searched=int(input('Numero ricercato \n'))

random_num=[]
n_to_search=[]
n_to_search_str=[]
inside_count=0

len_lista=random.randint(0, n_input)

for i in range(len_lista):
    n_rand=random.randint((10**(n_cifre-1)), (10**n_cifre)-1)
    random_num.append(n_rand)

for n in random_num:
    n_intero=str(n)

    for x in n_intero:
        x_int=int(x)
        if x_int==n_searched:
            inside_count+=1
    



print(random_num)
print(inside_count)