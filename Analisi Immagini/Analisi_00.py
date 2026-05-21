import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter as tk
from tkinter import filedialog



def chiudi_tutto(_):
    print("Closing the simulation")
    raise SystemExit





def analisi_immagine(soglia,imm,mappa, real_time):

    #Sub routine che controlla se nell'intorno di un punto interessante è stato già verificato se no lo senga da vedere
    def segna_intorno(a, b):
        nonlocal stack

        for m in range(a-1, a+2):
            for n in range(b-1, b+2):
                if imm[m, n, 1]==0:
                    stack.append([m,n])     # Se non visto aggiungo



    # Scansione su tutte le righe e su tutte le colonne
    h,w,_=imm.shape          # Categorizzo così altezza (h), larghezza (w) e canali (c)

    # Creo matricce che analizza se punti già analizzati e se sono sopra o sotto soglia
    # Distruggo la vecchia immagine e riempo di zeri nei canali blu e verde SOLO PERCHE IN SCALA GRIGI NON FUNZIONA SE A COLORI
    imm[:,:,1]=0      # Usato?
    imm[:,:,1]=0      # Sopra o sotto soglia?

    # Matrici aree e stack
    area=[]
    stack=[]

    # Faccio scansione
    for i in range(1, w):
        for j in range(1, h):

            # Verifico se già stato usato
            if imm[i, j, 1]==0:

                # Continuo analisi
                # Dico che usato
                imm[i,j,1]=0.5      # Cambio il colore così da veirficarlo
                
                if imm[i, j, 0]> soglia:
                    imm[i,j,2]=1        # Rendo colorata l'area così da vederla graficamente
                    
                    # Aggiungo alla lista area la nuova area da contare
                    area.append(1)
                    
                    # Sistema controllo dei vicini
                    segna_intorno(i, j)

                    while len(stack)>0:         # Continuo fino a quando non ho finito i vicini LIFO
                        n=len(stack)
                        x,y=stack[n-1][:]       # Estrai coordinate puntii ultimo posto stack
                        stack.pop()             # Elimino utlimo elemento

                        imm[x, y, 1]=0.5        # Segno il punto come usato

                        # Controllo se sopra sotto soglia
                        if imm[x, y, 0] > soglia:
                            imm[x,y, 2]=1       # Cambio colore per vederlo

                            area[-1]+=1         # Incrementa area

                            segna_intorno(x, y)

        if real_time=='y':
            mappa.set_data(imm)                     # Aggiornamento grafico per vederlo poi tolgo per efficenze
            plt.pause(0.001)

        mappa.set_data(imm)

    return area






def main():
    root = tk.Tk()  # procedure per leggere interattivamente un file
    root.withdraw()
    percorso_file = filedialog.askopenfilename(title="Image Selection PNG", filetypes=[("Immagini PNG", "*.png")])
    if not percorso_file:
        print("Nessun file selezionato.")
        raise SystemExit
    

    # Lettura dell'immagine tramite Matplotlib. mpimg.imread restituisce un array NumPy 
    #  n x m con 3 (RGB) o 4 (RGB+trasparenza) canali. La presenza del quarto canale 
    #  dipende solo dal fatto che l'immagine lo avesso o meno. 
    img_array = mpimg.imread(percorso_file)
    

    # Attenzione: Matplotlib legge i PNG convertendo i valori dei pixel tra 0.0 e 1.0 (float32) 
    #  invece del classico range 0-255 (uint8). Se voglio leggere jpeg e bmp devo ricordarmi 
    #  loro non sono convertiti. 
 

    altezza, larghezza, canali = img_array.shape
    # se non avessi conosciuto il metodo shape, avrei potuto leggere un valore 
    # alla volta con dei banali altezza=len(img_array[:,0,0]), larghezza=len(img_array[0,:,0]), etc.

    # Creazione di matrice vuoto con le stesse specifiche di tipo (dtype) ma 2 pixel più alta/larga
    img_con_bordo = np.zeros((altezza + 2, larghezza + 2, canali), dtype=img_array.dtype)
    

    # Se presente il canale Alfa, impostiamo l'opacità del bordo al massimo (1.0). E' solo per estetica.
    if canali == 4:
        img_con_bordo[:, :, 3] = 1.0


    # Inserimento dell'immagine al centro
    img_con_bordo[1:altezza+1, 1:larghezza+1] = img_array


    # Creo il grafico
    figura, (grafico1, grafico2) = plt.subplots(1,2, figsize=(14, 6),num='By Gianmario Pelanda')
    figura.canvas.mpl_connect('close_event', chiudi_tutto)
    

    mappa=grafico1.imshow(img_con_bordo)
    grafico1.axis('off')  
    grafico1.set_title(f"Image")


    soglia=float(input('Valore della soglia (0-1)= '))
    real_time=input('Mostra scansione in tempo reale? (y/n)')



    risultati=analisi_immagine(soglia,img_con_bordo,mappa, real_time)

    grafico2.hist(risultati, bins=10, color='skyblue', edgecolor='black')


    grafico2.set_title(f'Area Distribution (N_Tot = {len(risultati)})')
    grafico2.set_xlabel('Area')
    grafico2.set_ylabel('Number')

    # Ottimizza gli spazi tra i due grafici per evitare sovrapposizioni
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()