#Fare un progrmama MC che calcoli la distanz a cui mi sto spostando in un random walk



import matplotlib
matplotlib.use('Qt5Agg') # Forza il motore grafico avanzato
import matplotlib.pyplot as plt
import numpy as np
import random



class Setup:
    """Pannello di controllo del Random Walk"""
    def __init__(self):
        self.n_passi = 100        # Quanti passi fare prima di azzerare
        self.L = 1.0     # Lunghezza del singolo passo
        self.n_ripetizioni = 5     # Quante volte ripetere l'esperimento
        self.pausa_grafico = 0.01  # Velocità dell'animazione
        self.mostra_scia = True    # True o False per vedere tutti i puntini
        self.x_0=0
        self.y_0=0
        self.colors=['red', 'green', 'blue', 'black', 'pink']

# avvia il programma con il pannello di controllo
parametri = Setup()




def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit




# Controllo tastiera
def on_key(event):
    

    return 



def genera_angolo():
    angolo_grad=random.randint(0,360)
    angolo_rad=np.radians(angolo_grad)

    return angolo_rad



def trova_punto(par, angolo, x, y, dx, dy):
    

    delta_x=par.L*np.cos(angolo)
    delta_y=par.L*np.sin(angolo)

    

    

    x_n=par.x_0+delta_x
    y_n=par.y_0+delta_y

    dx.append(delta_x)
    dy.append(delta_y)
    x.append(x_n)
    y.append(y_n)

    return x_n, y_n,


    




def setta_nuovo_inizio(par, x_n, y_n):

    par.x_0=x_n
    par.y_0=y_n

    return par.x_0, par.y_0



    



def main(parametri):

    #SETUP GRAFICO
    

    

    Figura, Grafico = plt.subplots(1,2,num='By GP - Ising Model (Interactive Model: Press UP to raise and DOWNN to lower the temperatura \n BIANCO spin SU, NERO sping GIù', figsize=(12,6),layout='constrained')  # l'opzione layout='constrained' serve a gestire automaticamente lo spazio all'interno della figura per evitare che gli elementi si sovrappongano.
    Figura.canvas.mpl_connect('close_event', chiudi_tutto)  # chiude tutto se chiudo la GUI
    Figura.canvas.mpl_connect('key_press_event', on_key)    # uso la tastira per aumentare/diminuire T

    Grafico[0].set_aspect('equal')     # questo grafico mostrerà l'orientazione degli spin (binanco/nero per spin su/giù)
    Grafico[0].set_position([0.1, 0.15, 0.35, 0.7])
    titolo_0 = Grafico[0].set_title('Random walk, ciclo=') # il titolo mostrerà il valore dell'energia e della temperatura
    

    Grafico[1].set_position([0.55, 0.15, 0.35, 0.7]) # questo grafico mostrerà la magnetizzazione (energia) nel tempo e la temperatura
    titolo_1 = Grafico[1].set_title('Media passi, lunghezza passi') # il titolo mostrerà il valore della magnetizzazione e della temperatura
    Grafico[1].set_xlabel('N passi')     # etichettadegli assi
    Grafico[1].set_ylabel('Lunghezza passi')
    

    


    for i in range(parametri.n_ripetizioni):
        parametri.x_0=0
        parametri.y_0=0

        x=[0]
        y=[0]
        dx=[]
        dy=[]
        

        colore=parametri.colors[i]
        
        #linea
        linea, = Grafico[0].plot([], [], color=colore, linewidth=1.5) 
        
        # scia di punti
        scia_punti, = Grafico[0].plot([], [], color=colore, marker='.', linestyle='none', markersize=3)

        curva_med,=Grafico[1].plot([], [], color=colore, linewidth=1)  # creo una curva vuota che verrà aggiornata per mostrare la megnetiizzazione

        for l in range(parametri.n_passi):

           

            angolo_rnd=genera_angolo()

            x_n, y_n=trova_punto(parametri, angolo_rnd, x, y, dx, dy)


            x_0, y_0=setta_nuovo_inizio(parametri, x_n, y_n)
            

            linea.set_data([0, x_n], [0, y_n])

            scia_punti.set_data(x, y)

            curva_med.set_data([dx], [dy])


            Grafico[0].relim()
            Grafico[0].autoscale_view()

            Grafico[1].relim()
            Grafico[1].autoscale_view()


            plt.pause(0.01)

            




    return





main(parametri)
plt.show()