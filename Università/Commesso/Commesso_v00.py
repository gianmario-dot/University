#Commesso Viaggiatore

#Ci sono un saco di città e bisogna calcolare la lunghezza dei percorsi e calcolare la piu breve
#si usa un montecarlo che genera un numero di peemutazioni da analizzare

import matplotlib.pyplot as plt

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

            Grafico.plot(event.xdata, event.ydata,'ro', markersize=8)

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
    print(percorsi)
    return percorsi


def main():
    punti=[]

    Figura, Grafico = plt.subplots(num='By Franco Meinardi', figsize=(9,6))
    Grafico.set_xlim(0,1)
    Grafico.set_ylim(0, 1)
    Grafico.set_aspect('equal')
    punti = seleziona_punti(Figura, Grafico)
    n_punti = len(punti)
    Grafico.plot(*punti[0],'bo', markersize=8)
    Grafico.plot(*punti[n_punti-1],'bo', markersize=8)
    plt.show(block=False)

    if input('Calcolo esatto s/n ')=='s':
        percorsi=crea_percorsi(n_punti-1)   
        [print(p) for p in percorsi] 


    plt.show()

main()