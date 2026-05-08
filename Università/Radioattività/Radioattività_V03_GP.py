#radioattività di un oggetto tempo di vita 
# #tau=1s
#dt=0.1s 
#prob= 0.1/1
#genero un numero casuale se questo che esce è minore della probabilità decade se no faccio passare un altro tau e 
#creo un array dove metto tutto fino al decadimento
#poi cambio atomo e via

#I=exp(dt/tau)

import matplotlib.pyplot as plt
import numpy as np

# Impostazioni fisiche
N = 100000
tau = 1.0        
dt = 0.1         
dt_max = 50      

#Creazione dizionario automatico con ciclo
decadimenti = {passo: 0 for passo in range(1, dt_max + 1)}

#montecarlo
for i in range(N):
    for passo in range(1, dt_max + 1):
        n_rnd = np.random.uniform(0, 1)
        prob = dt / tau  
        if n_rnd < prob:
            decadimenti[passo] += 1
            break

#array np
passi_x = np.array(list(decadimenti.keys()))
valori_simulati = np.array(list(decadimenti.values()))

#CALCOLO TEORICO
tempi = (passi_x - 1) * dt
valori_teorici = N * (dt / tau) * np.exp(-tempi / tau)


figura, grafico = plt.subplots(figsize=(10, 8))

#Disegniamo barre 
grafico.bar(passi_x, valori_simulati, color='cornflowerblue', label='Simulazione Monte Carlo')
grafico.plot(passi_x, valori_teorici, color='red', linewidth=2, linestyle='--', label='Curva Teorica ($e^{-t/\\tau}$)')

grafico.set_title('Decadimento Radioattivo: Simulazione vs Teoria', fontsize=14, fontweight='bold')
grafico.set_xlabel('Passi temporali (1 passo = 0.1s)', fontsize=12) 
grafico.set_ylabel('Numero di atomi decaduti', fontsize=12)
grafico.legend()
grafico.grid(axis='y', linestyle='--', alpha=0.7)



def onclick(parametri):      
                                                
        if grafico.get_yscale()=='linear':   
            grafico.set_yscale('log')                                           
            
        elif  grafico.get_yscale()=='log':   
            grafico.set_yscale('linear') 

        figura.canvas.draw()

             
codice= figura.canvas.mpl_connect('button_press_event', onclick)
             
     
plt.show() 