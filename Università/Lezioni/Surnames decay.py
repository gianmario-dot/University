# Velocità con cui si perdono i cognomi generazione dopo generazione
# Per i cognomi generiamo dei numeri interi che è piu comodo delle stringhe a cui corrisponde il cognome di una lista
# Eliminiamo le femmine (cit, professore Meinards)

import numpy as np
import matplotlib.pyplot as plt


import matplotlib
matplotlib.use('TkAgg')




def chiudi_tutto(evento):
    print('fine')

    s_n=input('vuoi slavare i dati (Y/N)? \n')


    #if s_n=='s':
        # with open('dati.txt', 'w')



    raise SystemExit

class par:
        def __init__(self, n):
            self.n_pers=10000
            self.n_surn=1000

class persone:
        def __init__(self, n):
            self.sex=np.zeros(n, dtype=int)
            self.surname=np.zeros(n, dtype=int)

def conta_cognomi(lista):
    n=len(lista)
    vivi=np.zeros(n)

    for i in range(n):
        vivi[lista[i]]+=1

    vivi_tot=0
    for i in range(n): 
         if vivi[i]!=0:
              vivi_tot+=1

    return vivi_tot

def elimina_femmine(lista):
    n=len(lista.sex)
    shift=0                                         # 0 = maschio
    for i in range(n):
          if lista.sex[i]==0:
               lista.surname[shift]=lista.surname[i] # CORRETTO: surn -> surname
               lista.sex[shift]=0
               shift+=1

    return lista, shift                              # CORRETTO: rimosso +1

def nascite(pers, n_vivi, new_pers):
    n=len(new_pers.sex)

    for i in range(n):
         new_pers.sex[i]=np.random.randint(0,2)                           # CORRETTO: rimosso size=n
         new_pers.surname[i]=np.random.choice(pers.surname[:n_vivi])      # CORRETTO: rimosso size=n, surn->surname

    return new_pers

def main(): # CORRETTO: rimosso il passaggio di classi come argomenti
    
    # Costruisco fisicamente le variabili a partire dalle tue classi
    parametri = par(0)
    cognomi=np.arange(0, parametri.n_surn)
    
    new_persone=persone(parametri.n_pers)
    pers=persone(parametri.n_pers)

    # Inizializzo le variabili dell'oggetto pers
    pers.sex=np.random.randint(0,2, size=parametri.n_pers)
    pers.surname=np.random.choice(cognomi, size=parametri.n_pers)

    fig, grafico = plt.subplots(figsize=(12, 6),  num=' By Gianmario Pelanda - Surnames decay')
    fig.canvas.mpl_connect('close_event', chiudi_tutto) # CORRETTO: evemt -> close_event

    generazione=[]
    totale_cognomi=[]

    for i in range(100000000000000):
        generazione.append(i)
        
        # CORRETTO: Devi contare i cognomi di 'pers' non di 'par'
        totale_cognomi.append(conta_cognomi(pers.surname)) 

        # aggiornamento grafico solo quando cambia effettivamente perdiamo cognomi
        if i > 0 and totale_cognomi[i] != totale_cognomi[i-1]:            
            grafico.clear()
            grafico.bar(generazione, totale_cognomi, log=True)
            grafico.set_xscale('log')
            grafico.set_xlabel('Generations')
            grafico.set_ylabel('Surname')

            grafico.set_title(f'Step {i}: N-surname = {totale_cognomi[i]}')

            plt.pause(0.0001)

        

        # CORRETTO: la variabile vera in questo momento è 'pers', non la classe 'persone'
        pers, n_vivi = elimina_femmine(pers)
        
        # Blocco di sicurezza vitale: se nascono zero maschi il codice esplode perché non ci sono padri!
        if n_vivi == 0:
            print("Estinzione totale dei maschi!")
            break
            
        pers = nascite(pers, n_vivi, new_persone)

        if totale_cognomi[i] == 1:
            break

    plt.show()


main()

        
        

      