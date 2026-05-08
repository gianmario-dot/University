#Commesso Viaggiatore

#Ci sono un saco di città e bisogna calcolare la lunghezza dei percorsi e calcolare la piu breve
#si usa un montecarlo che genera un numero di peemutazioni da analizzare

import matplotlib.pyplot as plt

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
            


            grafico.plot(parametri.xdata, parametri.ydata, 'o', markersize=5, color='black')                 #disegna il punto dove cliccato

        elif parametri.button==3:                                                                            #altrimenti se posso metterne un numero x a seconda delle condizioni
            finito=True

        
        casella_txt.begin_typing()                                                                           #riporta il focus sulla casella di testo dopo ogni click


        return 
    

    

def permutazioni(lista):
    if len(lista)==1:           #si parte dall'uscita così da ricostruire come andare
        return lista
    
    risultato=[]
    for i in range(len(lista)):
        elemento_fisso=lista[i]         #toglie l'elemento e fa fare le permutazioni
        resto=lista[:i]+lista[i+1:]                #dato che si ferma prima dell'ultimo posso mettere i e poi aggiungo dalla i in poi (se ascio solo i due punti arriva fino in fondo e non salta l'ultimo)

        permu_resto=permutazioni(resto)

        for p in permu_resto:
            risultato.append(elemento_fisso+p)
    
    return risultato





def crea_percorsi(n_punti):
    elementi_interni=list(range(1, n_punti))
    permutazioni_interni=permutazioni(elementi_interni)
    percorsi=[(1,*perm,n_punti)  for perm in permutazioni_interni]            #dove l'asterisco serve per spacchettare la lista e prendere i singoli valori



def main():
    punti=[]


    figura, grafico = plt.subplots(num= 'By Gianmario Pelanda', figsize=(12,12))
    grafico.set_xlim(0,1)
    grafico.set_ylim(0,1)
    grafico.set_aspect('equal')

    punti=seleziona_punti(figura, grafico)
    n_punti= len(punti)
    grafico.plot(punti[0], 'bo', markersize=8)
    grafico.plot(punti[n_punti-1], 'bo', markersize=8)
    plt.show(block=False)

    if input('Calcolo esatto s/n')=='s':
        percorsi=crea_percorsi(len(punti))                   #creo la funzione che calcola tutti i possibili percorsi
        print(n for n in percorsi)

