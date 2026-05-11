#Calcolo di tutte le permutazioni


def permutazioni(lista):
    if len(lista)==1:           #si parte dall'uscita così da ricostruire come andare
        return lista
    
    risultato=[]
    for i in range(len(lista)):
        elemento_fisso=lista[i]         #toglie l'elemento e fa fare le permutazioni
        resto=lista[:i]+lista[i+1:]                #dato che si ferma prima dell'ultimo posso mettere i e poi aggiungo dalla i in poi (se ascio solo i due punti arriva fino in fondo e non salta l'ultimo)

        permu_resto=permutazioni(resto)

        for p in permu_resto:
            risultato.append(elemento_fisso+p)
    
    return risultato

lista=['a', 'b', 'c', 'd']
tutte=permutazioni(lista)
[print(p) for p in tutte]
print('permutazioni totali =', len(tutte))