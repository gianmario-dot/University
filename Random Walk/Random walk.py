#Fare un progrmama MC che calcoli la distanz a cui mi sto spostando in un random walk



import matplotlib
matplotlib.use('Qt5Agg') # Forza il motore grafico avanzato
import matplotlib.pyplot as plt
import numpy as np
import random



class Setup:
    """Pannello di controllo del Random Walk"""
    def __init__(self):
        self.n_passi = 10000         # Quanti passi fare prima di azzerare
        self.L = 1.0               # Lunghezza del singolo passo
        self.n_ripetizioni = 5     # Quante volte ripetere l'esperimento
        self.pausa_grafico = 0.01  # Velocità dell'animazione
        self.play = True           # True o False per vedere tutti i puntini
        self.x_0=0
        self.y_0=0
        self.colors=['red', 'green', 'blue', 'cyan', 'magenta']

parametri = Setup()




def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit




# Controllo tastiera
def on_key(event):
    global parametri
    if event.key==' ':
        parametri.play=False

    elif event.key=='enter':
        parametri.play=True

    return




def genera_angolo():
    angolo_grad=random.randint(0,360)
    angolo_rad=np.radians(angolo_grad)

    return angolo_rad



def trova_punto(par, angolo, x, y, dx, dy, l_passo, media_lunghezza):
    

    l_x=par.L*np.cos(angolo)
    l_y=par.L*np.sin(angolo)

    x_n=par.x_0+l_x
    y_n=par.y_0+l_y

    delta_x=abs(x_n-0)
    delta_y=abs(y_n-0)

    lunghezza=(delta_x*delta_x+delta_y*delta_y)**0.5               #Teorema di Pitagora

    
    l_passo.append(lunghezza)
    media=np.mean(l_passo)

    media_lunghezza.append(media)




    dx.append(delta_x)
    dy.append(delta_y)
    x.append(x_n)
    y.append(y_n)

    return x_n, y_n, l_passo, media_lunghezza


    




def setta_nuovo_inizio(par, x_n, y_n):

    par.x_0=x_n
    par.y_0=y_n

    return par.x_0, par.y_0


class Vari:
    """Pannello di controllo del Random Walk"""
    def __init__(self):
        self.x =[0]        # Quanti passi fare prima di azzerare
        self.y = [0]              # Lunghezza del singolo passo
        self.dy = []     # Quante volte ripetere l'esperimento
        self.dx = [] # Velocità dell'animazione
        self.l_passo=[0]         # True o False per vedere tutti i puntini
        self.passo=[0]
        self.media_lunghezza=[0]
    
    



def main(parametri):

    #SETUP GRAFICO
    

    

    Figura, Grafico = plt.subplots(1,2,num='By GP - Ising Model (Interactive Model: Press UP to raise and DOWNN to lower the temperatura \n BIANCO spin SU, NERO sping GIù', figsize=(12,6),layout='constrained')  # l'opzione layout='constrained' serve a gestire automaticamente lo spazio all'interno della figura per evitare che gli elementi si sovrappongano.
    Figura.canvas.mpl_connect('close_event', chiudi_tutto)  # chiude tutto se chiudo la GUI
    Figura.canvas.mpl_connect('key_press_event', on_key)    

    Grafico[0].set_aspect('equal')    
    Grafico[0].set_position([0.1, 0.15, 0.35, 0.7])
    
    

    Grafico[1].set_position([0.55, 0.15, 0.35, 0.7]) #
    titolo_1 = Grafico[1].set_title('Media passi, lunghezza passi') 
    Grafico[1].set_xlabel('N passi')     # etichetta degli assi
    Grafico[1].set_ylabel('Lunghezza passi')
    

    


    for i in range(parametri.n_ripetizioni):
        parametri.x_0=0
        parametri.y_0=0

        #gestico le liste dentro il ciclo
        liste = Vari()

        colore=parametri.colors[i]
        
        # linea, scia di punti
        linea, = Grafico[0].plot([], [], color=colore, linewidth=1.5) 
        scia_punti, = Grafico[0].plot([], [], color=colore, marker='.', linestyle='none', markersize=3)

        # curva lunghezza, media
        curva,=Grafico[1].plot([], [], color=colore, linewidth=1)  
        #curva_med,=Grafico[1].plot([], [], color='black', linewidth=2)  
        titolo_0 = Grafico[0].set_title(f'Random walk, ciclo={i+1}') 

        
        somma_distanze = np.zeros(parametri.n_passi + 1)
        

        for l in range(parametri.n_passi):

            t=l+1
            liste.passo.append(t)

            angolo_rnd=genera_angolo()

            x_n, y_n, liste.l_passo, liste.media_lunghezza=trova_punto(parametri, angolo_rnd, liste.x, liste.y, liste.dx, liste.dy, liste.l_passo, liste.media_lunghezza)


            x_0, y_0=setta_nuovo_inizio(parametri, x_n, y_n)



            if parametri.play==True:

                linea.set_data([0, x_n], [0, y_n])
                scia_punti.set_data(liste.x, liste.y)

                Grafico[0].relim()
                Grafico[0].autoscale_view()

            
                curva.set_data(liste.passo, liste.l_passo)
                

                
                Grafico[1].relim()
                Grafico[1].autoscale_view()


                plt.pause(parametri.pausa_grafico)

        
            
        # Somma le distanze 
        somma_distanze = somma_distanze + np.array(liste.l_passo)

            
        linea.set_data([0, x_n], [0, y_n])
        scia_punti.set_data(liste.x, liste.y)
        curva.set_data(liste.passo, liste.l_passo)
            
        Grafico[0].relim()
        Grafico[0].autoscale_view()
        Grafico[1].relim()
        Grafico[1].autoscale_view()
        plt.pause(0.1) 

        



    # Calcola la media finale
    media_finale = somma_distanze / parametri.n_ripetizioni
    
    # Calcola la curva teorica 
    # (distanza tipica in 2D per passo costante L=1 e dt=1)
    tempi = np.arange(parametri.n_passi + 1)
    curva_teorica = np.sqrt(np.pi / 4) * parametri.L * np.sqrt(tempi)

    # Disegna le due curve sul Grafico[1]
    Grafico[1].plot(tempi, media_finale, color='black', linewidth=3, label='Media Simulata')
    Grafico[1].plot(tempi, curva_teorica, color='orange', linestyle='--', linewidth=2, label='Teoria')
    Grafico[1].legend()
    



    return





main(parametri)
plt.show()