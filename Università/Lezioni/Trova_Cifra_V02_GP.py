import random

def main():
     
    n_cifre=int(input('Quante cifre devono avere i numeri? \n'))
    n_input=int(input('N_max \n'))
    n_searched=int(input('Numero ricercato \n'))

    random_num=[]
    n_to_search=[]
    len_lista=random.randint(0, n_input)
    inside_count=0

    #lunghezza lista randomica
    for i in range(len_lista):
        n_rand=random.randint((10**(n_cifre-1)), (10**n_cifre)-1)
        random_num.append(n_rand)

    #numero singolo da analizzare
    for i in random_num:
        num_singolo=i
        inside_count+=trova_cifra(num_singolo, n_searched)
    

    print(random_num)
    print(inside_count)

#Funzione ricorsiva che taglia lultimo numero lo analizza e poi ricomincia con il numero mozzato
def trova_cifra(num_singolo, n_searched):
    resto=num_singolo%10
    num_mozzato=num_singolo//10

    if num_singolo==0:
        return 0
    
    if resto==n_searched:
        return 1+trova_cifra(num_mozzato, n_searched)
    
    return 0+trova_cifra(num_mozzato, n_searched)
    


main()