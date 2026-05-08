# Modi di vibrazione normali delle molecole
# Legge di Hooke F=-kX



import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog



def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit





def apri_file():
    root = tk.Tk()
    root.withdraw() 
    # Apre la finestra "Open"
    nome_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("ASCII", "*.txt"), ("Tutti i file", "*.*")],title="Open")


    return nome_file





def leggi_file(nome_file, posizioni, masse, k_molle):

    with open(nome_file, 'r') as f:
        fine_file=False
        while not fine_file:
            riga=f.readline().strip('\n')                   # Strip serve per definire la fine riga
            if riga!='_':
                righe=riga.split(',')

                posizioni.append([float(righe[0]), float(righe[1])])
                masse.append(float(righe[2]))

            else:
                fine_file=True

            
        for i in range(len(masse)):
            riga=f.readline().strip('\n')  
            righe=riga.split(',')
            k_molle.append([float(c) for c in righe])

    return posizioni, masse, k_molle








def calcola_matrici(coordinate, masse, k_elastiche):
    n=len(masse)

    K=np.zeros((2*n, 2*n))
    for i in range(n):
        for j in range(i+1, n):
            k_ij=k_elastiche[i][j]

            if k_ij !=0:
                dx=coordinate[j][0]- coordinate[i][0]
                dy=coordinate[j][1]- coordinate[i][1]

                # Calcolo l'angolo rispetto agli assi
                l=np.sqrt(dx**2+dy**2)
                c=dx/l              # Coseno
                s=dy/l              # Seno

                # Moltiplico senso e coseno per il cubetto interessato
                k_locale=k_ij*np.array([
                    [c*c, c*s],
                    [s*c, s*s]
                ])


                # Aggiungo tutto alla matrice principale
                K[2*i:2*i+2, 2*j:2*j+2]-=k_locale
                K[2*j:2*j+2, 2*i:2*i+2]-=k_locale

                # Diagonali
                K[2*i:2*i+2, 2*i:2*i+2]+=k_locale
                K[2*j:2*j+2, 2*j:2*j+2]+=k_locale


    D=np.zeros((2*n, 2*n))

    for i in range(2*n):
        for j in range(2*n):
            
            fattore_masse=np.sqrt(masse[int(i/2)]*masse[int(j/2)])

            D[i, j]=K[i,j]/fattore_masse

    return D






def disegna_modi_normali(autovalori, autovettori, posizioni, modo):

    pos=np.array(posizioni)
    spostamenti=[autovettori[:,modo-1]]
    spost=np.array(spostamenti).reshape(-1,2)


    xmax=np.max(np.abs(pos))+np.max(np.abs(spost))


    fig,grafico=plt.subplots(figsize=(8, 6), num='By Gianmario Pelanda, Normal Modes')
    fig.canvas.mpl_connect('close_event', chiudi_tutto)
    fig.canvas.mpl_connect('key_press_event', on_key())



    # Disegna le masse 
    grafico.clear()
    grafico.set_aspect('equal', adjustable='box')       # Importante per non distorcere le direzioni dei vettori
    grafico.scatter(pos[:, 0], pos[:, 1], color='red', label=f'Normal mode n. {modo:02d}', zorder=5)
    grafico.set_xlim(-xmax,xmax)
    grafico.set_ylim(-xmax,xmax)
    grafico.axhline(0, color='black', lw=0.5, ls='--')
    grafico.axvline(0, color='black', lw=0.5, ls='--')
    grafico.grid(True, linestyle=':', alpha=0.6)
    grafico.set_title('Normal Modes')
    grafico.set_xlabel("X")
    grafico.set_ylabel("Y")

    # Imposta le frecce
    frecce=grafico.quiver(pos[:, 0], pos[:, 1], spost[:, 0], spost[:, 1], 
                color='blue', angles='xy', scale_units='xy', scale=1, label=f'Energy = {autovalori[modo]:.2f}')
    # Crea direttamente la freccia, vuole le posizioni iniziali x, y e poi lo spostamento sugli assi, 
    # mentre angles e scale servono per saoere come muoversi invece che usare dimensione finestra

    grafico.legend()









def main():

    nome_file=apri_file()
    

    posizioni=[]        # Creo l'array dove andranno le posizioni quando lette dal file
    masse=[]
    k_molle=[]



    posizioni, masse, k_molle= leggi_file(nome_file, posizioni, masse, k_molle)



    matrice_D=calcola_matrici(posizioni, masse, k_molle)

    # Calcoliamo autovettori e autovalori della matrice dinamica
    autovalori, autovettori=np.linalg.eigh(matrice_D)                           # eig, eigvals +h quando la matrice è hermitiana, li restituisce in modo crescente

    print(autovalori, '\n\n')

    # Parte grafica

    modo=len(autovalori)                   #Ultimo autovalore e modo a valore più alto

    disegna_modi_normali(autovalori, autovettori, posizioni, modo)




main()