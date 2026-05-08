#Commesso Viaggiatore

#Ci sono un saco di città e bisogna calcolare la lunghezza dei percorsi e calcolare la piu breve
#si usa un montecarlo che genera un numero di peemutazioni da analizzare

import matplotlib.pyplot as plt
import random

def chiudi_tutto(event):
    raise SystemExit()



def seleziona_punti(Figura, Grafico):
    punti = []
    finito = False
    
    def onclick(event):
        nonlocal finito #funzione evento tiene quale tasto viene premuto (sinitro=1, tasto in mezzo=2 e tasto destro=3)
        #tratta questa variabile come una globale e puoi modificarne il valore
        #il tasto sinitro posiziona carica il destro esce dal poszionamento

        if not event.inaxes:
            return

        if event.button == 1:
            punto = (event.xdata, event.ydata)
            punti.append(punto)

            print("aggiunto:", punto)

            Grafico.plot(event.xdata, event.ydata,'o', color='black', markersize=8)

        elif event.button == 3:

            finito = True
  
    cid=Figura.canvas.mpl_connect('button_press_event', onclick)

    while not finito:
        plt.pause(0.1)

    Figura.canvas.mpl_disconnect(cid)

    return punti





def permutazioni(lista):   # "lista" è la lista da permutare
    if len(lista)==1:      # se la lista ha un solo elemento restituisce tutte le sue permutazioni cioè la lista stessa
        return [lista]
    
    risultato=[]           # creo una lista vuota dove metterò tutte le permutazioni di "lista"
    for i in range(len(lista)):   # per ogni elemento della lista da permutare ...
        elemento_fisso=lista[i]   # fisso l'iesimo elemento ...
        resto=lista[:i]+lista[i+1:]   # costruisco la lista degli elementi restanti = "resto"

        per_resto=permutazioni(resto)   # calcolo le permutazioni della lista "resto" rilanciando la funzione

        for p in per_resto:  # aggiungo a "risultato" oggetti costituiti dall'elemento fisso + tutte le sue permutazioni
            risultato.append([elemento_fisso]+p)

    return risultato       # restituisco la lista "risultato" che contine tutte le permutazioni della lista "lista"





def crea_percorsi(n_punti):
    elementi_interni=list(range(1,n_punti))
    permutazioni_interni=permutazioni(elementi_interni)
    percorsi=[[0,*perm,n_punti] for perm in permutazioni_interni]
    #print(percorsi)
    return percorsi



def crea_percorsi_random(ultimo, n_random):
    elementi_interni=list(range(1, ultimo))
    percorsi=[]

    for i in range(n_random):
        random.shuffle(elementi_interni)
        percorsi.append([0, *elementi_interni, ultimo])


    
    return percorsi




def calcola_lunghezza(x, y):
    lunghezza=0

    for i in range(len(x)-1):                      #uso uno in meno perche i segmenti sono uno meno della lunghezza della classe dato che tra punto e iniziale non voglio siano uniti
        dx=x[i+1]-x[i]
        dy=y[i+1]-y[i]                             #ho trovato le distanze per x e y di ogni segmemnto

        lunghezza+=(dx*dx+dy*dy)**0.5               #Teorema di Pitagora



    return lunghezza





def disegna_percorsi(grafico, percorsi, punti, colore):
    l_min=1e300
    l_max=-1                                    #assegno dei valori subito superabili

    #percorso finto
    per,=grafico.plot(0,0, 'red', linewidth=2, zorder=2)

    per_min,=grafico.plot(0,0, colore, linewidth=4, zorder=1)


    #disegno i percorsi
    #invece che cancellare tutto e ridisegnare modifico solo il valore della variabile cosi da non dover rifare tutto tutte le votle
    #devo creare un percorso finto iniziale che viene aggiornato   PER,

    


    for strada in percorsi:                     #ciclo che crea il percorso e la lunghezza
        x=[punti[i][0] for i in strada]         #prende le x dei punti e crea la lista
        y=[punti[i][1] for i in strada]         #prende le y dei punti e crea la lista
        per.set_data(x,y)

        lunghezza=calcola_lunghezza(x, y)

        #colcolo lunghezze corte e lunghe
        if lunghezza < l_min:
            l_min=lunghezza
            per_min.set_data(x,y)
            grafico.set_title(f'L_min = {l_min:.2f} \n L_max = {l_max:.2f}')


        if lunghezza > l_max:
            l_max=lunghezza
            grafico.set_title(f'L_min = {l_min:.2f} \n L_max = {l_max:.2f}')

        plt.pause(0.001)

    return l_min, l_max







def main():
    punti=[]

    Figura, Grafico = plt.subplots(num='By GP', figsize=(9,6))
    Grafico.set_xlim(0,1)
    Grafico.set_ylim(0, 1)
    Grafico.set_aspect('equal')
    punti = seleziona_punti(Figura, Grafico)
    n_punti = len(punti)
    Grafico.plot(*punti[0],'go',  markersize=8)
    Grafico.plot(*punti[n_punti-1],'ro', markersize=8)
    plt.show(block=False)
    Figura.canvas.mpl_connect('close_event', chiudi_tutto)

    if input('Calcolo esatto s/n ')=='s':
        percorsi=crea_percorsi(n_punti-1)   
        l_min, l_max=disegna_percorsi(Grafico, percorsi, punti, colore='green')                 #creo l'effettiva routine che calcola le lunghezze del percorso
        print(l_min, l_max)

    n_random=int(input('Quanti percorsi random vuoi testare ='))
    percorsi=crea_percorsi_random(n_punti-1, n_random)
    l_min, l_max=disegna_percorsi(Grafico, percorsi, punti, colore='salmon') 

    plt.show()

main()