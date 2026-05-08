# Modi di vibrazione normali delle molecole
# Legge di Hooke F=-kX

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit

def calcola_matrici(coordinate, masse, k_elastiche):
    n = len(masse)
    K = np.zeros((2*n, 2*n))
    
    for i in range(n):
        for j in range(i+1, n):
            k_ij = k_elastiche[i][j]
            if k_ij != 0:
                dx = coordinate[j][0] - coordinate[i][0]
                dy = coordinate[j][1] - coordinate[i][1]

                # Calcolo l'angolo rispetto agli assi
                l = np.sqrt(dx**2 + dy**2)
                c = dx/l              # Coseno
                s = dy/l              # Seno

                # Moltiplico seno e coseno per il blocco interessato
                k_locale = k_ij * np.array([
                    [c*c, c*s],
                    [s*c, s*s]
                ])

                # Aggiungo tutto alla matrice di rigidezza
                K[2*i:2*i+2, 2*j:2*j+2] -= k_locale
                K[2*j:2*j+2, 2*i:2*i+2] -= k_locale

                # Diagonali
                K[2*i:2*i+2, 2*i:2*i+2] += k_locale
                K[2*j:2*j+2, 2*j:2*j+2] += k_locale

    D = np.zeros((2*n, 2*n))
    for i in range(2*n):
        for j in range(2*n):
            fattore_masse = np.sqrt(masse[int(i/2)] * masse[int(j/2)])
            D[i, j] = K[i, j] / fattore_masse

    return D

def sistema_traslazioni(autovettori):
    dimens = len(autovettori[:, 0])
    
    # e1: Traslazione asse X (Corretto)
    e1 = np.arange(dimens) % 2
    e1 = e1 / np.sqrt(dimens / 2)

    # e2: Traslazione asse Y (Corretto il +1 nelle parentesi per le dimensioni)
    e2 = (np.arange(dimens) + 1) % 2
    e2 = e2 / np.sqrt(dimens / 2)

    # e3: Rotazione (Corretto Gram-Schmidt aggiungendo * e2 alla fine)
    u3 = autovettori[:, 2]
    e3 = u3 - np.dot(e1, u3)*e1 - np.dot(e2, u3)*e2
    
    # Normalizzazione VERA (Aggiunta la radice quadrata)
    e3 = e3 / np.sqrt(np.dot(e3, e3))

    # Inserimento sicuro colonna per colonna
    autovettori[:, 0] = e1
    autovettori[:, 1] = e2
    autovettori[:, 2] = e3

    return autovettori


def disegna_modi_normali(autovalori, autovettori, pos, modo):
    # 1. VARIABILI CONDIVISE
    # Creiamo questi "contenitori" vuoti per far comunicare le funzioni tra loro
    # senza creare cicli infiniti annidati.
    ferma = False
    frecce = None
    spost = None

    def on_key(evento):
        nonlocal modo, ferma
        if evento.key == ' ':
            ferma = not ferma

        elif evento.key == 'up':
            if modo < len(autovalori):
                modo += 1
                aggiorna()  # Ricalcola la statica ed ESCE. Nessun loop qui dentro!

        elif evento.key == 'down':
            if modo > 1:
                modo -= 1
                aggiorna()  # Ricalcola la statica ed ESCE. Nessun loop qui dentro!

    def aggiorna():
        nonlocal frecce, spost
        
        pos_array = np.array(pos)
        spostamenti = [autovettori[:, modo-1]]
        spost = np.array(spostamenti).reshape(-1, 2)

        x_max = np.max(np.abs(pos_array)) + np.max(np.abs(spost))

        grafico.clear()
        grafico.set_aspect('equal', adjustable='box')
        grafico.scatter(pos_array[:, 0], pos_array[:, 1], color='red', label=f'Normal mode n. {modo:02d}', zorder=5)
        grafico.set_xlim(-x_max, x_max)
        grafico.set_ylim(-x_max, x_max)
        grafico.axhline(0, color='black', lw=0.5, ls='--')
        grafico.axvline(0, color='black', lw=0.5, ls='--')
        grafico.grid(True, linestyle=':', alpha=0.6)
        grafico.set_title('Normal Modes')
        grafico.set_xlabel("X")
        grafico.set_ylabel("Y")

        # Creiamo le frecce e le salviamo nella variabile "frecce" di livello superiore
        frecce = grafico.quiver(pos_array[:, 0], pos_array[:, 1], spost[:, 0], spost[:, 1], 
                                color='blue', angles='xy', scale_units='xy', scale=1, 
                                label=f'Energy = {autovalori[modo-1]:.2f}')
        grafico.legend()

    # --- SETUP INIZIALE GRAFICO ---
    fig, grafico = plt.subplots(figsize=(8, 6), num='By Gianmario Pelanda, Normal Modes')
    fig.canvas.mpl_connect('close_event', chiudi_tutto)
    fig.canvas.mpl_connect('key_press_event', on_key)

    aggiorna() # Disegniamo la molecola per la prima volta

    # =========================================================
    # IL MOTORE DELL'ANIMAZIONE (L'Architettura Corretta)
    # È un singolo loop globale che non si accumula mai.
    # =========================================================
    t = 0
    while True:
        if not ferma:
            t += 0.1  # Il tempo scorre regolarmente
            fase = np.cos(t * np.pi)
            spost_t = spost * fase
            # Modifichiamo solo le frecce senza ricreare l'intero grafico
            frecce.set_UVC(spost_t[:, 0], spost_t[:, 1])

        # Matplotlib aggiorna lo schermo (0.05 è un frame rate fluido, circa 20fps)
        plt.pause(0.05) 


# =========================================================
# PROGRAMMA PRINCIPALE (LETTURA FILE)
# =========================================================
root = tk.Tk()
root.withdraw() 
nome_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("ASCII", "*.txt"), ("Tutti i file", "*.*")], title="Open")

posizioni = []
masse = []
k_molle = []

with open(nome_file, 'r') as f:
    fine_file = False
    while not fine_file:
        riga = f.readline().strip('\n')
        if riga != '_':
            righe = riga.split(',')
            posizioni.append([float(righe[0]), float(righe[1])])
            masse.append(float(righe[2]))
        else:
            fine_file = True
            
    # Dal carattere "_" in poi leggo le costanti elastiche
    for i in range(len(masse)):
        riga = f.readline().strip('\n')  
        righe = riga.split(',')
        # Corretto l'uso delle parentesi quadre per creare una vera lista
        k_molle.append([float(c) for c in righe])


# 1. Calcolo la matrice dinamica
matrice_D = calcola_matrici(posizioni, masse, k_molle)

# 2. Diagonalizzo (Autovalori e Autovettori)
autovalori, autovettori = np.linalg.eigh(matrice_D)
print("Autovalori (Energia): \n", autovalori, '\n\n')

# 3. Forzo i primi 3 modi a essere Traslazioni/Rotazioni pure
autovettori = sistema_traslazioni(autovettori)

# 4. Lancio la grafica partendo dal modo più energetico
modo = len(autovalori) 
disegna_modi_normali(autovalori, autovettori, posizioni, modo