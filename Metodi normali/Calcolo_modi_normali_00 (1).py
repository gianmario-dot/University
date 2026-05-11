import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit

def disegna_modi_normali(posizioni,autovalori,autovettori,modo):  # routine di animazione dei modi normali

    def on_key(evento):  # con le frecce su e giù seleziono il modo da visualizzare. Con lo spazio fermo/attivo l'animazione
        nonlocal modo
        nonlocal ferma
        if evento.key==' ':
            ferma=not(ferma) 
        if evento.key=='up':
            if modo<len(autovalori):
                modo+=1
                aggiorna()
        if evento.key=='down':
            if modo>1:
                modo-=1
                aggiorna()
        return
    # nota: non è bellissimo rilanciare continuamente una funzione (aggiorna) senza aver chiuso l'istanza precedente. 
    # probabilmente se cambio centinaia di volte il modo, alla fine il programma va in crash. 
    # però è un metodo semplice e veloce per cui mi accontento!

    def aggiorna():   # routine di animazione vera e propria
        pos=np.array(posizioni)   # trasforma la lista con le posizioni in un array numpy
        spostamenti=[autovettori[:,modo-1]]
        spost=np.array(spostamenti).reshape(-1,2) # idem per il file con l'autovettore del modo da mostrare
        xmax=np.max(np.abs(pos))+np.max(np.abs(spost))  # calcolo i limiti massimo della figura

        # impostazioni del grafico
        grafico.clear()  # inzio pulendo tutto. serve per non avere 'rimasugli' quando cambio il modo
        grafico.set_aspect('equal', adjustable='box') # importante per non distorcere le direzioni dei vettori
        grafico.scatter(pos[:, 0], pos[:, 1], color='red', label=f'Normal mode n. {modo:02d}', zorder=5)
        grafico.set_xlim(-xmax,xmax)
        grafico.set_ylim(-xmax,xmax)
        grafico.axhline(0, color='black', lw=0.5, ls='--')
        grafico.axvline(0, color='black', lw=0.5, ls='--')
        grafico.grid(True, linestyle=':', alpha=0.6)
        grafico.set_title('Normal Modes')
        grafico.set_xlabel("X")
        grafico.set_ylabel("Y")
        # imposta le frecce che rappresentano gli spostamenti al tempo 0
        frecce=grafico.quiver(pos[:, 0], pos[:, 1], spost[:, 0], spost[:, 1], 
                    color='blue', angles='xy', scale_units='xy', scale=1, label=f'Energy = {autovalori[modo-1]:.2f}')
        grafico.legend()
        t=0  # ciclo di animazione
        while True:
            if not ferma:
                t+=0.1  # determina quanto fine sarà l'animazione
                fase=np.cos(t*np.pi)
                spost_t=spost*fase 
                frecce.set_UVC(spost_t[:,0],spost_t[:,1])  # aggiorno i vettori che mostrano gli spsostamenti nel tempo
            plt.pause(0.1)  # determina la velocità do aggioramento dell'immagine 

    # impostazioni del grafico
    fig,grafico=plt.subplots(figsize=(8, 6), num='By Franco Meinardi. Normal Modes')
    fig.canvas.mpl_connect('close_event', chiudi_tutto)
    fig.canvas.mpl_connect('key_press_event', on_key)
    ferma=False  # variabile che determina se l'animazione è attiva o in stand by
    aggiorna()
    plt.show()   # qui il programma non arriva mai per cui queste 2 istruzioni sono ridondanti
    return

# routine per proiettare gli autovalori corrispondenti all'autovalore 0, su due autovettori corrspondenti ...
# ... ad una "pura" traslazione su x e su y, più una rotazione intorno al centro di massa.
# in realtà, non esistendo autovalori esattamente uguali a 0 dato che la precsione di un calcolo numerico è limitata ...
# ... dalle cifre significative, la proiezione viene fatta per i primi 3 autovalori. Se ci fossero altri autovalori con energia molto ...
# ... bassa non è detto che funzioni bene. 
def sistema_traslazioni(autovettori):   
    dimens=len(autovettori[:,0])
    e1=np.arange(dimens)%2
    e1=e1/np.sqrt(dimens/2)  # e1 è una pura traslazione lungo x
    e2=np.arange(1,dimens+1)%2
    e2=e2/np.sqrt(dimens/2)  # e2 è una pura traslazione lungo y
    u3=autovettori[:,2]
    e3=u3-np.dot(e1,u3)*e1-np.dot(e2,u3)*e2
    e3=e3/np.dot(e3,e3)    # e3 è il terzo autovettore meno le proiezioni di e1 ed e2 su quest'ultimo. => e3 rappresenta la pura rotazione.
    autovettori[:,0]=e1
    autovettori[:,1]=e2
    autovettori[:,2]=e3
    return autovettori  # restituisco la matrice con gli autovettori in cui i primi 3 sono stati "routati"

def calcola_matrice(coordinate,masse,k_elastiche):  # calcolo della matrice dinamica come descritto negli appunti
    n=len(masse)
    K=np.zeros((2*n,2*n))  # matrice di rigidezza
    for i in range(n):
        for j in range(i+1,n):
            k_ij=k_elastiche[i][j]  # leggo le costanti elastiche che connettono ogni coppia di atomi
            if k_ij !=0:  # calcolo la matrice di rigidezza locale
                dx=coordinate[j][0]-coordinate[i][0] 
                dy=coordinate[j][1]-coordinate[i][1]

                L=np.sqrt(dx**2+dy**2)
                c=dx/L
                s=dy/L

                k_locale=k_ij*np.array([
                    [c*c,c*s],
                    [s*c,s*s]])
                
                K[2*i:2*i+2,2*j:2*j+2]-=k_locale   # copio i blocchi della matrice di rigidezza locale in quella complessiva
                K[2*j:2*j+2,2*i:2*i+2]-=k_locale

                K[2*i:2*i+2,2*i:2*i+2]+=k_locale
                K[2*j:2*j+2,2*j:2*j+2]+=k_locale

    D=np.zeros((2*n,2*n))    # divido la matrice di rigidezza per la masse in modo da ottenere la matrice dinamica
    for i in range(2*n):
        for j in range(2*n):
            f_masse=np.sqrt(masse[int(i/2)]*masse[int(j/2)])
            D[i,j]=K[i,j]/f_masse

    return D

root = tk.Tk()  #procedure per leggere interattivamente un file
root.withdraw() 
nome_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("ASCII", "*.txt"), ("Tutti i file", "*.*")],title="Open")

posizioni=[]
masse=[]
molle=[]
with open(nome_file,'r') as f:
    fine_atomi=False
    while not fine_atomi:   # leggo posizioni e masse degli atomi fino a quando non incontro il carattere "_"
        riga=f.readline().strip('\n')
        if riga !='_':
            righe=riga.split(',')
            posizioni.append([float(righe[0]),float(righe[1])])
            masse.append(float(righe[2]))
        else:
            fine_atomi=True
    
    for i in range(len(masse)):  # dal carattere "_" in poi leggo le costanti elastiche delle molle ...
        riga=f.readline().strip('\n')   # ... elimino da ogni riga il fine riga ...
        righe=riga.split(',')  # ... le splitto ...
        molle.append([float(c) for c in righe])   # metto il risultato nella matrice delle costanti elastice (matrice delle adiacenzze)

matrice_D=calcola_matrice(posizioni,masse,molle)   # lancio il calcolo della matrice dinamica ...
autovalori,autovettori=np.linalg.eigh(matrice_D)   # ... e ne trovo autovalori ed autovettori. 
print(autovalori,'\n\n')

autovettori=sistema_traslazioni(autovettori)       # ruoto quelli a energia 0 in modo da separare traslazioni e rotazione 

modo=len(autovalori)
disegna_modi_normali(posizioni,autovalori,autovettori,modo)  # lancio l'animazione







