#Allinamaneto spin e calcolo delle propeiètà amgnetiche del materiale
#Faremo un reticolo con spin randomico su o giù, poi gira l'orientamento di u atomo a caso e verifica se ci guadangi o merno (primi vicini)
#Devo minimizzare l'energia di Helmutz e verificare ocn la pro della statistica di Bolztman per vedere se gira o meno lo spin
#più sara bassa la T maggiore sarà la possibilità che si giri nella direzione sfavorevole
#si dovrebbe vedere una transizione di fase tra all'ineamento casuale a una mangetizzazione netta




# Con un Monte Carlo simuliamo la magnetizzazione di un cristallo e la sua transizione di fase alla  
#  temperatura di Curie. Nella cartella c'è una micro-dispensa sulla fisica di questi sistemi 
#  e su cume simularli. Sempre nella cartella c'è anche l'articolo originale in cui per la 
#  prima volta è stata fatta una simmulazione Montecarlo con un computer (a valvole).

# Questa volta scriviamo il codice da "fisici" piuttosto che da "informatici"
# => Codice tutto "dritto" senza main, e con un minimo di funzioni solo dove sono proprio necessarie.
# Usiamo anche variabili globali per i paramteri chiave che serviranno un po' dappertutto.

import matplotlib
matplotlib.use('Qt5Agg') # Forza il motore grafico avanzato
import matplotlib.pyplot as plt
import numpy as np

# Parametri 
l_griglia=100
T=3.0
J=1                     #decisione paramgnetico o ferrmagnetico (1 --> paramagnetico)




def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit




# Controllo tastiera
def on_key(event):
    global T                    #autorizzazione a cambiare la variabile globale
    if event.key=='up':
        T+=0.1
    elif event.key=='w':
        T+=10

    elif event.key=='down':
        T-=0.1
    elif event.key=='s':
        T-=10

    return 




#SETUP GRAFICO

Figura, Grafico = plt.subplots(1,2,num='By GP - Ising Model (Interactive Model: Press UP to raise and DOWNN to lower the temperatura \n BIANCO spin SU, NERO sping GIù', figsize=(12,6),layout='constrained')  # l'opzione layout='constrained' serve a gestire automaticamente lo spazio all'interno della figura per evitare che gli elementi si sovrappongano.
Figura.canvas.mpl_connect('close_event', chiudi_tutto)  # chiude tutto se chiudo la GUI
Figura.canvas.mpl_connect('key_press_event', on_key)    # uso la tastira per aumentare/diminuire T

Grafico[0].set_aspect('equal')     # questo grafico mostrerà l'orientazione degli spin (binanco/nero per spin su/giù)
Grafico[0].set_position([0.1, 0.15, 0.35, 0.7])
titolo_0 = Grafico[0].set_title('E = , T =') # il titolo mostrerà il valore dell'energia e della temperatura

Grafico[1].set_position([0.55, 0.15, 0.35, 0.7]) # questo grafico mostrerà la magnetizzazione (energia) nel tempo e la temperatura
titolo_1 = Grafico[1].set_title('M = , T =') # il titolo mostrerà il valore della magnetizzazione e della temperatura
Grafico[1].set_xlabel('Time Steps')     # etichettadegli assi
Grafico[1].set_ylabel('Magnetization')
curva_mag,=Grafico[1].plot([], [],'salmon',linewidth=1)  # creo una curva vuota che verrà aggiornata per mostrare la megnetiizzazione

G2=Grafico[1].twinx()             # creo un secondo grafico gemello per mostrare la temperatura (non posso mettere due curve nello stesso grafico perchè le ordinate sono diverse)
G2.set_position([0.55, 0.15, 0.35, 0.7])  # in teoria non dovrebbe servire ma a volte senza quessta seconda dichiarazione succedono dei casini
G2.set_ylabel('Temperature')     # nome dell'asse y del secondo grafico
curva_temp,=G2.plot([], [],'darkgreen',linewidth=1)   # creo una curva vuota che verrà aggiornata per mostrare la temperatura









#PARTE MATEMATICA - FISICA


#INIZIALIZZAZIONE GRAFICA SPIN
#Uso delle matrici che sono enormente più efficenti, rimependola dei valori randomici di spin
#disegnamo la matrice (CONTURF=  prende gli array di x e y e affetta il grafico 3D portandolo in 2D, IMG= non ha le colonne x, y prende drettmente la matrice z e riempe con i colori proporzionali)
#a livello computazionale conturf è molto piu pesante ma molto più smooth


spin=np.random.choice([-1, 1], size=(l_griglia, l_griglia))

immagine=Grafico[0].imshow(spin, cmap='gray', vmin=-1, vmax=1)



#EVOLUZIONE
#faccio simulazione infinita tanto ho la x per chiudere
#ogni quanto aggionro la simulazione? ogni spin? ogni spin esagerato, tempo del MonteCarlo --> convenzione = muovere tutti i gradi del sistema (10k atomi= 10k tempo montecarlo)

step_per_frame=l_griglia*l_griglia
x=[]
Temp=[]
E_M=[]

E0=0            #valore iniziale energia, lo considero 0 per comodità

for frame in range(1000000000000):
    for k in range(step_per_frame):
        i=np.random.randint(0, l_griglia)
        j=np.random.randint(0, l_griglia)
        s=spin[i, j]
        dE=2*J*s*(spin[(i+1)%l_griglia, j]+spin[(i-1)%l_griglia, j]+spin[i, (j+1)%l_griglia] + spin[i, (j-1)%l_griglia])                         #calcolo se l'energia è favorevole o meno al cambio dello psin
        #verifico se accettare o meno l'inversione
        if dE<0 or np.random.rand()<np.exp(-dE/T):              #se favorevole energia o se lo dice boltzamn
            spin[i, j]*=(-1)
            E0+=dE

    mag=np.mean(spin)

    immagine.set_data(spin)
    titolo_0 = Grafico[0].set_title(f'E = {E0:.2f} , T = {T:.1f} °C')


    x.append(frame)
    E_M.append(mag)
    Temp.append(T)

    curva_mag.set_data(x, E_M)
    curva_temp.set_data(x, Temp)
    titolo_1 = Grafico[1].set_title(f'M = {mag:.2f} , T = {T:.1f} °C')


    Grafico[1].relim()
    Grafico[1].autoscale_view()

    G2.relim()
    G2.autoscale_view()


    plt.pause(0.01)

plt.show()