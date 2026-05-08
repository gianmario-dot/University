# statistica Maxwell-Boltzman
# ci saranno fluttuazioni simili a MonteCarlo per costruzione della fisica su cui si basa
# tutte le particelle si muovono nella stessa direzione e ogni volta che si uratno cambiano direzione, verso e velocità
# creiamo un istogramma con il numero di velocità e quante particellle la hanno e vediamo che super velocemente arriviamo a boltzman

# vedremo come far sia vedere in diretta l'animazione ma anche come salvarla e mostrarla in un playyer video

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter           

def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit

# Calcola la distribuzione teorica per una data temeperatura (in unità di Kb)


def main():
    # Classe per i parametri della simulazione
    class parametri:
        def __init__(self, N=200, R=0.1, M=0.7, v=2, Lato=20, t_step=0.05, termal_sp=1, binning=25, nome_file=r'C:\Users\Admin\Documents\Didattica\Programmazione\Materiale\Maxwell\output_03.avi' ):
            self.N = N  # Numero di particelle
            self.R = R  # Raggio delle particelle
            self.M = M  # Massa delle particelle 
            self.v = v  # Modulo della velocità delle particelle
            self.Lato = Lato  # Lato della scatola
            self.t_step = t_step  # Intervallo di tempo per l'aggiornamento della posizione (secondi per ogni ciclo) (step piccoli lenta ma tanti urti, step velcoi veloce ma perdo urti), ho fatt che t*V=raggio
          # self.termal_sp=termal_sp 
            self.binning = binning   # binning dei dati (in quante parte/barre dividere l'istogramma)
            self.nome_file=nome_file

    # Classe per posizione e velocita degli atomi
    class atomi:
        def __init__(self, n):
            self.x=np.zeros(n)
            self.y=np.zeros(n)
            self.vx=np.zeros(n)
            self.vy=np.zeros(n)
            self.urti=np.zeros(n, dtype=int)

    
       # Creazione della figura
        
    Figura, (Grafico1, Grafico2) = plt.subplots(1, 2, Figurasize=(12, 6), num='By Franco Meinardi - 2D Maxwell- Boltzman Didtribution', layout='constrained')

    # Collegamento dell'evento "key_press_event"
    # Figura.canvas.mpl_connect('key_press_event', on_key)
    Figura.canvas.mpl_connect('close_event', chiudi_tutto)

    # Configurazione del grafico delle particelle
    Grafico1.set_position([0.1, 0.15, 0.35, 0.7])
    Grafico1.set_xlim(0, par.Lato)
    Grafico1.set_ylim(0, par.Lato)
    Grafico1.set_title("Particles in a Box")

    # Inizializzazione dei punti
    scatola = Grafico1.scatter(He.x[:], He.y[:], s=10, c='b')

    # Configurazione dell'istogramma a destra
    Grafico2.set_position([0.55, 0.15, 0.35, 0.7])
    Grafico2.set_xlim(0, v_max)
    Grafico2.set_title(f'Speed Distribution. T = {KbT:.2F}')
    Grafico2.set_xlabel('Speed')
    Grafico2.set_ylabel("Counts")

    # Creazione dell'istogramma
    velocita = np.sqrt(He.vx[:]**2 + He.vx[:]**2)
    n, bins_edges, barre = Grafico2.hist(velocita, bins=par.binning, range=(0,v_max), alpha=0.7, color='lightblue', edgecolor='darkblue', linewidth=2)

    

    linea, = Grafico2.plot(vel, M_B, 'r-', linewidth=2, label="Maxwell-Boltzmann")
    Grafico2.legend()
    Grafico2.set_ylim(0, np.max(M_B)*1.2)

    # Animazione
    writer = FFMpegWriter(fps=30, codec='mpeg4')
    plt.pause(5)
    
    with writer.saving(fig, par.nome_file, dpi=166):
        for step in range(100000000):
            writer.grab_frame() # salva frame
            
                
            Grafico2.set_title(f'Speed Distribution -- T = {KbT:.2F} -- Step = {step:04d}')

            plt.pause(0.001)
            
main()