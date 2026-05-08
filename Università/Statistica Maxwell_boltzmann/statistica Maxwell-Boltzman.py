# statistica Maxwell-Boltzman
# ci saranno fluttuazioni simili a MonteCarlo per costruzione della fisica su cui si basa
# tutte le particelle si muovono nella stessa direzione e ogni volta che si uratno cambiano direzione, verso e velocità
# creiamo un istogramma con il numero di velocità e quante particellle la hanno e vediamo che super velocemente arriviamo a boltzman

# vedremo come far sia vedere in diretta l'animazione ma anche come salvarla e mostrarla in un playyer video

import matplotlib
matplotlib.use('Qt5Agg') # Forza il motore grafico avanzato
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter  
import imageio_ffmpeg
# Diciamo a Matplotlib esattamente dove si trova il file eseguibile di ffmpeg
plt.rcParams['animation.ffmpeg_path'] = imageio_ffmpeg.get_ffmpeg_exe()




# Classe per i parametri della simulazione
class parametri:
    def __init__(self, N=200, R=0.1, M=0.7, v=4, Lato=20, t_step=0.05, termal_sp=1, binning=20, nome_file=r'C:\Programmazione\Statistica Maxwell-boltzmann\video_simul_001.mp4' ):
        self.N = N  # Numero di particelle
        self.R = R  # Raggio delle particelle
        self.M = M  # Massa delle particelle 
        self.v = v  # Modulo della velocità delle particelle
        self.Lato = Lato  # Lato della scatola
        self.t_step = t_step  # Intervallo di tempo per l'aggiornamento della posizione (secondi per ogni ciclo) (step piccoli lenta ma tanti urti, step velcoi veloce ma perdo urti), ho fatt che t*V=raggio
        # self.termal_sp=termal_sp 
        self.binning = binning   # binning dei dati (in quante parte/barre dividere l'istogramma)
        self.nome_file=nome_file

par=parametri()    

# Classe per posizione e velocita degli atomi
class atomi:
 def __init__(self, n):
    self.x=np.zeros(n)
    self.y=np.zeros(n)
    self.vx=np.zeros(n)
    self.vy=np.zeros(n)
    self.urti=np.zeros(n, dtype=int)                            #gli dico che sono interi cosi che possiamo far cambiare colore
    #slef urti serve per togliere i dimeri creanfo un tempo di cooling prima dell'urto successivo
    





def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit





# Calcola la distribuzione teorica per una data temeperatura (in unità di Kb)
def Maxwell_Boltzman(par, vel, KbT):
    f_v=vel*np.exp((-1/2*par.M*(vel)**2)/KbT)
    
    # Fattore normalizzazione
    f_v_norm=f_v*par.N/np.sum(f_v)

    return f_v_norm



# Faccio muovere le particelle e urti pareti
def update(par, He):
    He.x+=He.vx*par.t_step
    He.y+=He.vy*par.t_step

    #urti pareti, verifico una condizione logica (se x minore di 0 è fuori dalla particella) trovta la risposta la mette in un vettore, 
    # lo fa per ogni particella e da il valore indice della particella per cui si è verificato l'impatto

    # X pareti verticali
    impatto=He.x<=0
    He.vx[impatto]=-He.vx[impatto]

    impatto=He.x>=par.Lato
    He.vx[impatto]=-He.vx[impatto]

    # Y pareti orizzontatali
    impatto=He.y<=0
    He.vy[impatto]=-He.vy[impatto]

    impatto=He.y>=par.Lato
    He.vy[impatto]=-He.vy[impatto]
    

    # Urti particelle tra loro
    
    for i in range(par.N):

        if He.urti[i]==0:

            for j in range(i+1, par.N):
                    He=check_collision(par, He, i, j)


    He.urti[:]=np.maximum(He.urti-1, 0)

    return He



def check_collision(par, He, i, j):
    r_urto=2*par.R                  #se la distanza è minore del doppio del raggio ottengo un urto

    #non facciamo in modo super rigoroso poixhè dato che è la routine più time-consuming cerco di ridurre il tempo di calcolo e velocizzo il processo
    # Usiamo urti completamente elastici dove il centro di massa procede di moto uniforme mentre cambiano le velocità sulle congiungenti fino a scambiarsi le velovità e le direzioni (urto elastico)

    # Delta distanza
    delta=[He.x[i]-He.x[j], He.y[i]-He.y[j]]

    #distanza= modulo delta
    distanza=np.linalg.norm(delta)

    # Calcolo il versore direzione
    direzione=delta/distanza

    #controllo urto
    if distanza<r_urto:
        v_rel=[He.vx[i]-He.vx[j], He.vy[i]-He.vy[j]]                # Vettore delle velocità relative

        # Faccio prodotto scalare con versore distanza per trovare proiezione
        proiezione_v_rel=np.dot(v_rel, direzione)*direzione

        He.vx[i]-=proiezione_v_rel[0]
        He.vy[i]-=proiezione_v_rel[1]
        He.vx[j]+=proiezione_v_rel[0]
        He.vy[j]+=proiezione_v_rel[1]

        He.urti[i], He.urti[j]=10, 10

    
    return He

        







def main(par):

    He=atomi(par.N)



    # metodo non giusto perchè numpy è super efficcente con gli array
    #for i in range(par.N):
        #He.x[i]=np.random.uniform(0, par.Lato, 1)
        #He.y[i]=np.random.uniform(0, par.Lato, 1)

    # uso potenza di numpy
    He.x[:]=np.random.uniform(1/3*par.Lato, 2/3*par.Lato, par.N)
    He.y[:]=np.random.uniform(1/3*par.Lato, 2/3*par.Lato, par.N)

    He.vx[:]=par.v/np.sqrt(2)
    He.vy[:]=par.v/np.sqrt(2)

    v_max=4*par.v

    KbT=(par.M*(par.v)**2)/2



    # Creazione della figura
        
    Figura, (Grafico1, Grafico2) = plt.subplots(1, 2, figsize=(12, 6), num='By Gianmario Pelanda - 2D Maxwell- Boltzman Didtribution', layout='constrained')

    
    # Creo colori che poi faccio palette
    color_a=[0.0,0.0,1.0]
    color_b=[1.0,0.0,1.0]

    palette=np.array([color_a, color_b, color_b, color_b, color_b, color_b, color_b, color_b, color_b, color_b, color_b])


    Figura.canvas.mpl_connect('close_event', chiudi_tutto)

    # Configurazione del grafico delle particelle
    Grafico1.set_position([0.1, 0.15, 0.35, 0.7])
    Grafico1.set_xlim(0, par.Lato)          #coordinate che dipendono dalla fienstra e non pixel
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
    velocita = np.sqrt(He.vx[:]**2 + He.vy[:]**2)       #serve per ca,biar ele velocità iniziale se non le voglio tutte uguali
    n, bins_edges, barre = Grafico2.hist(velocita, bins=par.binning, range=(0,v_max), alpha=0.7, color='lightblue', edgecolor='darkblue', linewidth=2)


    # Trovo i centri dei bins cosi da sapere per cosa calcolare la curva teorica
    vel=((bins_edges[1:]+bins_edges[:-1])/2)



    # Funzione Maxwell-Boltzmann
    M_B=Maxwell_Boltzman(par, vel, KbT)


    linea, = Grafico2.plot(vel, M_B, 'r-', linewidth=2, label="Maxwell-Boltzmann")
    Grafico2.legend()
    Grafico2.set_ylim(0, np.max(M_B)*1.2)

    
    writer = FFMpegWriter(fps=24, codec='h264', bitrate=5000)
    #plt.pause(5)            #possibilità di mettere la finestra a tutto schermo e mi da il tempo di farlo
    
    with writer.saving(Figura, par.nome_file, dpi=160):
        for step in range(100000000):
            writer.grab_frame() # salva frame
            
            update(par, He) 

            scatola.set_offsets(np.c_[He.x[:], He.y[:]])


            nuovo_colore=palette[He.urti]
            scatola.set_facecolor(nuovo_colore)




            #creo l'array velocità delle particelle cosi da poterlo graficare nell'istogramma
            velocita=np.sqrt(He.vx[:]**2+He.vy[:]**2)


            #creo l'istogramma
            n,_=np.histogram(velocita, bins=par.binning, range=(0, v_max))              
            
            #metto n,_ perchè non mi serve il secondo output che è l'array dei bordi dei bins, lo faccio ogni volta per aggiornare i dati dell'istogramma, 
            # se invece facessi barre.set_height() non funzionerebbe perchè le barre sono già state create e non si aggiornano con i nuovi dati, invece facendo 
            # l'istogramma ogni volta aggiorno i dati e quindi le barre si aggiornano di conseguenza



            for i in range(len(barre)):
                barre[i].set_height(n[i])





            Grafico2.set_title(f'Speed Distribution -- T = {KbT:.2F} -- Step = {step:04d}')

            plt.pause(0.001)
            


main(par)