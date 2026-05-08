#la precisione aumenta come radice del numero di tentativi
#se ho una precisione del 10% con 10^6 tentativi per passare a 1% mi servono 10^12 tentativi

#faccio generare tutto la simulazione insieme e ci da il valore rispetto al vero 

#facciamo un grafico dove sulle y avremo l'avvicinamento a PI e sulla x i valori di tentativi (lograritimico)
#fare grafici ci costa del tempo e quindi bisogna scegliere come fare (lo aggiorniamo in scala logaritmica)

import matplotlib
matplotlib.use('TkAgg') # Forza l'uso di un backend più leggero e stabile

import matplotlib.pyplot as plt
import numpy as np




#impostazione grafico
ritardo=0.05
N=int(input('Numero tentativi='))




inside_count=0

iteration=[]       #creo le liste ocn le variabili che mi interessano
pi_values=[]
errors=[]




pi_exact=np.pi



#creo il grafico
figura, grafico = plt.subplots(2, 1, num= 'Calcolo di PI, by Gianmario Pelanda', figsize=(16,12))       #Metto due grafici in una sola riga una rsorta di matrice di grafci
grafico[0].axhline(pi_exact, color='red', linestyle='--', label='Valore esatto PI')                       #Creo una riga che mi mostri dove si trova il valore di PI
grafico[0].legend()                    #mostra la legenda del grafico (label)
grafico[0].set_xscale('log')
grafico[0].set_ylabel('Stima di PI')
grafico[0].grid()

grafico[1].set_xscale('log')
grafico[1].set_yscale('log')
grafico[1].set_ylabel('Errore')
grafico[1].set_xlabel('Numero iterazioni')
grafico[0].grid()

#nel grafico dell'errore faccio aggiungere il valore di PI ultimo misurato e l'errore attuale
Testo=grafico[1].text(50, 0.3, '', fontsize=11 )






#creo i plot che mi interessa visualizzare
g0,=grafico[0].plot(iteration, pi_values, 'go', linestyle='-', markersize=4)
g1,=grafico[1].plot(iteration, errors, 'go', linestyle='-', markersize=4 )


Io=1                                    #ogni quanto aggiornare il grafico
for i in range(1, N+1):                 #togliendo la partenza da 1 elimino N sommatorie
    x,y=np.random.uniform(-1, 1, 2)
    distance=x**2+y**2
    if distance<=1:
        inside_count+=1
        
    pi_greco=(inside_count/(i))*4      #crea l'aggiornamento logaritmico

    if i%Io==0:
        Io*=10**int(np.log10(i))
        iteration.append(i)
        pi_values.append(pi_greco)
        errore=abs(pi_exact-pi_greco)/pi_exact      #calcolo il valore dell'errore relativo
        errors.append(errore)
        g0.set_xdata(iteration)                   #aggiornare il grafico
        g0.set_ydata(pi_values)
        grafico[0].relim()                                #allunga il valore dell'asse
        grafico[0].autoscale_view()

        g1.set_xdata(iteration)                   
        g1.set_ydata(errors)
        grafico[1].relim()                                #allunga il valore dell'asse
        grafico[1].autoscale_view()

        Testo.set_text(f'valore di PI = {pi_greco:5.4f}  -  Errore =  {errore:4.2%}')
        figura.canvas.flush_events()
        plt.pause(ritardo)



plt.show()