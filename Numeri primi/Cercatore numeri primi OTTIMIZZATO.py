#importo il modulo time per misurare il tempo di esecuzione del programma

import time
start_time=time.process_time()


#Cercatore numeri primi
N_input=int(input("Numero massimo entro il quale cercare= "))
primi= True
Numeri_primi=[2] #aggiungo 2 alla lista dei numeri primi, in questo modo posso far partire il ciclo for da 3 e saltare i numeri pari, in questo modo il tempo di esecuzione sarà più veloce

# Creo ciclo
                                    # 3) faccio partire il ciclo da 3 perche pari non possono essere primi e uso incremento 2 per saltare i numeri pari, in questo modo il ciclo for iterera solo sui numeri dispari, e quindi il tempo di esecuzione sarà più veloce
for j in range(3,N_input+1,2):      #il ciclo parte da 2 perchè 0 e 1 non sono numeri primi, e arriva fino a N_input+1 perchè il range arriva fino a N_input-1
    primi= True                     #voglio verificare che j sia primo e poi uso il ciclo for per verificare se j è divisibile per i numeri da 2 a j-1, se j è divisibile per uno di questi numeri allora non è primo e quindi setto primi a False
    for i in range(2,j):            #se j è divisibile per i allora j non è primo, quindi setto primi a False e esco dal ciclo for, se j non è divisibile per nessuno dei numeri da 2 a j-1 allora j è primo e quindi aggiungo j alla lista dei numeri primi
      divisione=int(j/i)            #uscito dal ciclo si riparte dal j successivo del ciclo superiore1
      resto=divisione*i
      if resto==j:
         primi=False
         break                      #2) uso break per uscire dal ciclo for quando j è divisibile per i, in questo modo il tempo di esecuzione sarà più veloce, perchè non devo continuare a verificare se j è divisibile per gli altri numeri da 2 a j-1
      
    if primi==True:
       Numeri_primi.append(j)
      



print(Numeri_primi)
print('tempo di esecuzione= ',process_time, 'secondi')

#tempo di esecuzione non ottimizzato (10'000 numeri) 30.703125 secondi
#2) tempo di esecuzione (10'000 numeri)  3.703125 secondi
#3) tempo di esecuzione (10'000 numeri)  3.421875 secondi