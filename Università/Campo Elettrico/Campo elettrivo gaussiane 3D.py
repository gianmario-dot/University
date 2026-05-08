#disegnare un campo elettrico generato da un qualche tipo di sorgente
#mettere sorgente dove voglio io con 
#GUI puoi inswerire bottoni o slidero o anche deigli oggetti non 'reali' ma anche gli eventi del mouse o della tastiera (si vedono le coordinate del mouse)

import matplotlib.pyplot as plt
#cosi importo tutta la sottolibreria
#import matplotlib.widgets as widgets
#posso anche importare solo la parte interessata come la textbox
from matplotlib.widgets import TextBox

#devo importare il modulo numpy per fare i conti con i vettori e le operazioni matriciali
import numpy as np
#ci permette di fare i conti diretti senza dover scrivere i cicli for per ogni operazione che rallenterebbero tutto


def seleziona_punti(figura, grafico, casella_txt):
    finito=False
    punti=[]

    def onclick(parametri):                                                    #funzione evento tiene quale tasto viene premuto (sinitro=1, tasto in mezzo=2 e tasto destro=3)
        nonlocal finito                                                        #tratta questa variabile come una globale e puoi modificarne il valore
        if parametri.button==1:                                                #il tasto sinitro posiziona carica il destro esce dal poszionamento
            carica=float(casella_txt.text)

            casella_txt.set_val=''
            punto=(parametri.xdata, parametri.ydata, carica)
            punti.append(punto)

            #aggiungo un pezzo che impedisca i clicchi accidentali fuori dal grafico (annulla click)
            if parametri.inaxes!=grafico:
                return



            if carica >0:
                colore = 'red'

            else:
                colore = 'blue'

            grafico.plot(parametri.xdata, parametri.ydata, 'o', markersize=5, color=colore)                 #disegna il punto dove cliccato

        elif parametri.button==3:                                                                            #altrimenti se posso metterne un numero x a seconda delle condizioni
            finito=True

        
        casella_txt.begin_typing()                                                                           #riporta il focus sulla casella di testo dopo ogni click


        return 
    
    

    #devo dire al programma di stare in ascolto dei click del mouse per segnarsi il punto
    codice= figura.canvas.mpl_connect('button_press_event', onclick)        #non ho messo le parentesi perchè non voglio che venga eseguita subito ma solo dopo che venga eseguita, ma non avendo parentesi non posso passargli niente
    
    #per passare le info devo quindi rendere o glboali tutti i dati o usare una peculiarità di python ovvero scrivrgli una funzione dntro all'altra e questa avrà tutte le variabili di quella esterna
    
    plt.pause(0.5)
    casella_txt.begin_typing()

    while not finito:                               #rimane all'infinto nella GUI a rilevare cosa serve
        plt.pause(0.1)
    figura.canvas.mpl_disconnect(codice)
    
    return punti



def calcola_campo(punti, x_g, y_g):

    #dato che ogni carica genera un campo ci serve sapere quante sono a generare il campo
    n_punti=len(punti)

    #creo array per le z
    #ottengo un array lungo come x_g ma pieno di zeri
    z_g=0*x_g

    #posso farlo in modo più python usando nunpy
    #z_g=np.zeros_like(x_g)


    #calcolo il campo come somma di ogni carica
    #ciclo sulle cariche
    for i in range(n_punti):
        
        #spacchetto la lista punti nelle parti che ci intressano
        x0, y0, carica=punti[i]

        #faccio generare una gaussiana
        z_g+=carica*np.exp(-(x_g-x0)**2/0.1-(y_g-y0)**2/0.1)

        #ora usiamo il campo elettrico reale, che è proporzionale alla carica e inversamente proporzionale alla distanza al quadrato
        #z_g+=carica/((x_g-x0)**2+(y_g-y0)**2)

    return z_g





def main():
    #parametri da eventualmente cambiare, si dovrebbe fare un file da leggere
    #numero di punti in cui calcolare il campo elettrico, più sono e più preciso sarà ma più lento sarà il programma
    nx=500
    ny=500

    figura, grafico = plt.subplots(num= 'By Gianmario Pelanda', figsize=(12,12))
    grafico.set_xlim(0,1)
    grafico.set_ylim(0,1)
    grafico.set_aspect('equal')

    #non dare le coordinate in pixel ma in funzione della dimensione della GUI
    coordinate=figura.add_axes([0.45, 0.9, 0.1, 0.05])
    casella_txt = TextBox(coordinate, 'Carica')

    #figura.canvas.draw()                                                    #calcola cosa disegnare nell'interfaccia grafica
    #l'abbiamo commeentqto perchè non è necessario, quando si disegna qualcosa di nuovo viene disegnato tutto da capo, quindi non serve disegnare prima la GUI e poi dopo i punti, basta disegnare tutto alla fine

    #creo la lista punti che racchiuderà la posizione della carica
    punti=seleziona_punti(figura, grafico, casella_txt)
    [print(i) for i in punti]


    #FASE 2 
    #leggo i valori massimi e minimi delle coordinate per creare una griglia di punti in cui calcolare il campo elettrico
    #cosi che se do un valore superiore a 1 o inferiore a 0 non mi da errore ma semplicemente mi disegna il campo elettrico in un area più grande o più piccola
    xmin, xmax= grafico.get_xlim()
    ymin, ymax= grafico.get_ylim()

    #creo arrays di coordinate x e y 
    #generiamo un sarie lineare di numeri equispaziati tra xmin e xmax, e tra ymin e ymax, con un numero di punti pari a nx e ny
    x=np.linspace(xmin, xmax, nx)
    y=np.linspace(ymin, ymax, ny)

    #combina la coordinate x e y in una griglia di punti, in modo da avere tutte le combinazioni possibili di x e y, che rappresentano i punti in cui calcolare il campo elettrico
    x_griglia, y_griglia= np.meshgrid(x, y)



    #ora devo calcolare z che rappresenta il campo elettrico in ogni punto della griglia, inizialmente lo imposto a zero
    #passo ala funzione calcola_campo i punti in cui sono posizionate le cariche e la griglia di punti in cui calcolare il campo elettrico, e questa mi restituisce un array con i valori del campo elettrico in ogni punto della griglia
    z_g=calcola_campo(punti, x_griglia, y_griglia)
    z_g1=np.log10(abs(z_g)%10)


    #creiamo il grafico 3D del campo elettrico, con x e y come coordinate e z come altezza, usando la funzione contourf che disegna le linee di livello del campo elettrico, con una mappa di colori per rappresentare i valori del campo elettrico
    grafico.remove()                                                                 #rimuove il grafico precedente per disegnare quello nuovo, altrimenti si sovrappongono e non si vede niente
    grafico1=figura.add_subplot(projection='3d')
    grafico1.plot_surface(x_griglia, y_griglia, z_g, cmap='plasma')

    #cs=grafico.contourf(x_griglia, y_griglia, z_g, levels=10, cmap='plasma')
    #cs=grafico.contourf(x_griglia, y_griglia, z_g1, levels=10, cmap='plasma')
    #figura.colorbar(cs, ax=grafico, label='Campo elettrico V/m')

    figura.canvas.draw()



main()
plt.show()