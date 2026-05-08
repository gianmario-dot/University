#importo il modulo time per misurare il tempo di esecuzione del programma

import time
start_time=time.process_time()


#Cercatore numeri primi
N_input=int(input("Numero massimo entro il quale cercare= "))
primi= True
Numeri_primi=[]

# Creo ciclo

for j in range(2,N_input+1):        #il ciclo parte da 2 perchè 0 e 1 non sono numeri primi, e arriva fino a N_input+1 perchè il range arriva fino a N_input-1
    primi= True                     #voglio verificare che j sia primo e poi uso il ciclo for per verificare se j è divisibile per i numeri da 2 a j-1, se j è divisibile per uno di questi numeri allora non è primo e quindi setto primi a False
    for i in range(2,j):            #se j è divisibile per i allora j non è primo, quindi setto primi a False e esco dal ciclo for, se j non è divisibile per nessuno dei numeri da 2 a j-1 allora j è primo e quindi aggiungo j alla lista dei numeri primi
      divisione=int(j/i)            #uscito dal ciclo si riparte dal j successivo del ciclo superiore1
      resto=divisione*i
      if resto==j:
         primi=False
    if primi:
       Numeri_primi.append(j)
print(Numeri_primi)
end_time=time.process_time()
process_time=end_time-start_time


print('tempo di esecuzione= ',process_time, 'secondi')

#tempo di esecuzione 30.703125 secondi