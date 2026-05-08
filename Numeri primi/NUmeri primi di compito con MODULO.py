# Input numero da testare
numero_test = int(input('Numero test: '))
Numeri_primi = [2]
j_max=0                                             #ultimo numero primo da usare perle divisioni

import time
start_time = time.process_time()

# Ciclo principale
for j in range(3, numero_test, 2):
    primi = True
    
    sqr_i=(j**0.5)                          #calcolo la radice quadrata di j e aggiungo 1 per evitare problemi di arrotondamento, in questo modo evito di dover fare il ciclo fino a j-1 e quindi il tempo di esecuzione sarà più veloce
    #while Numeri_primi[j_max] <= sqr_i:          #uso un ciclo while per trovare l'ultimo numero primo da usare per le divisioni, in questo modo evito di dover fare il ciclo fino a j-1 e quindi il tempo di esecuzione sarà più veloce
        #j_max+=1                                #incremento j_max fino a quando il numero primo in posizione j_max è minore della radice quadrata di j, in questo modo j_max sarà l'indice dell'ultimo numero primo da usare per le divisioni
    #abbiamo gsrantito che il numero successivo poosa essere ottenuto solo il successivo dei numeri primi    
    
    if Numeri_primi[j_max] <= sqr_i:
        j_max+=1

    for i in Numeri_primi:     
        if i>sqr_i:
            break
                #uso solo i numeri primi fino a j_max per le divisioni, in questo modo il tempo di esecuzione sarà più veloce

        if j % i == 0:
            primi = False
            break
        
 

    if primi == True:
        Numeri_primi.append(j)

end_time = time.process_time()
process_time = end_time - start_time
totale_primi = len(Numeri_primi)

print(Numeri_primi, '\n')
print('Tempo esecuzione \n', process_time, 'secondi')
print('Quantità numeri primi \n', totale_primi)


#dividendo solo per i numeri primi ho ottenuto 0.4 secondi di process_time
#mettendo la parte di radice sonop sceso a 0,03 secondi