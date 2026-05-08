# Input numero da testare
numero_test = int(input('Numero test: '))
Numeri_primi = [2]

import time
start_time = time.process_time()

# Ciclo principale
for j in range(3, numero_test + 1, 2):
    primi = True
    
    # Ciclo interno (le divisioni)
    for i in Numeri_primi:
        if i * i > j:
            break

        #Divisione = int(j / i)
        #Resto = i * Divisione
        resto=j % i
        if resto == 0:
            primi = False
            break
            
  
    # Questo 'if' deve stare ALLINEATO col 'for i', non dentro di esso!
    if primi == True:
        Numeri_primi.append(j)

end_time = time.process_time()
process_time = end_time - start_time

print(Numeri_primi)
print('Tempo esecuzione', process_time, 'secondi')


#dividendo solo per i numeri primi ho ottenuto 0.4 secondi di process_time
#mettendo la parte di radice sonop sceso a 0,03 secondi