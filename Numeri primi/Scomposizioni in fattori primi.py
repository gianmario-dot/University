#importo il modulo time per misurare il tempo di esecuzione del programma

import time

# 1. Chiedo l'input PRIMA di far partire il cronometro
N_input = int(input("Numero da scomporre= \n"))

# 2. Faccio partire il cronometro
start_time = time.process_time()

Divisori = []
Numeri_primi = [2]

# Cercatore di numeri primi (Usando le ottimizzazioni potenti!)
for j in range(3, N_input + 1, 2):
    primo_attuale = True
    
    # Usiamo direttamente la lista Numeri_primi e l'operatore Modulo (%)
    for i in Numeri_primi:
        if i * i > j:
            break
        if j % i == 0:
            primo_attuale = False
            break
            
    if primo_attuale == True:
        Numeri_primi.append(j)

# Troviamo quali di questi numeri primi dividono il nostro N_input
for x in Numeri_primi:
    if N_input % x == 0:
        Divisori.append(x)

# 3. LA NUOVA LOGICA FINALE:
# Se la lista dei divisori contiene un solo numero, ed è proprio N_input
# allora N_input non ha altri sottomultipli, quindi è lui stesso PRIMO!
if len(Divisori) == 1 and Divisori[0] == N_input:
    print('Numero primo: \n 1 ,', N_input)
else:
    print('Divisori: \n', Divisori)

# Stampo il tempo di esecuzione
print("Tempo di esecuzione: ", time.process_time() - start_time, "secondi")