import math
import matplotlib.pyplot as plt

# 1. Le Classi vanno sempre definite fuori, all'inizio del file!
class Palla:
    def __init__(self, x, y, vx, vy, raggio):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.raggio = raggio

def main():
    # Creiamo l'oggetto palla (ti servirà dopo per la fisica)
    pp = Palla(-1, 0.8, 0.02, 0.1, 0.2)
    
    # Variabili fisiche (pronte per il futuro)
    g = 0.02                              
    smorz = 0.8                           
    suolo = -0.8                          
    dt = 0.5
    ritardo = 0.05                        
    n_max = 500                           

    # Costruisco la figura e gli assi
    Figura, Grafico = plt.subplots(num='By Gianmario Pelanda')
    Grafico.set_xlim(-1, 1)
    Grafico.set_ylim(-1, 1)
    Grafico.set_aspect('equal')

    cerchio=plt.Circle((pp.x, pp.y), pp.raggio, color='blue')  # Crea un cerchio con centro (pp.x, pp.y) e raggio pp.raggio
    linea=plt.Rectangle((-1, suolo), 2, 0.01, color='black')  # Crea una linea orizzontale che rappresenta il suolo

    Grafico.add_patch(cerchio)  # Aggiunge il cerchio al grafico
    Grafico.add_patch(linea)    # Aggiunge la linea al grafico


    for i in range(n_max):
        pp.x += pp.vx * dt  # Aggiorna la posizione x della palla
        pp.y += pp.vy * dt  # Aggiorna la posizione y della palla
        pp.vy -= g * dt     # Applica l'effetto della gravità sulla velocità verticale

        if pp.y < suolo + pp.raggio:  # Controlla se la palla tocca il suolo
            pp.y = suolo + pp.raggio  # Posiziona la palla esattamente sul suolo
            pp.vy = -pp.vy * smorz     # Inverti e smorza la velocità verticale

        cerchio.center = (pp.x, pp.y)  # Aggiorna la posizione del cerchio nel grafico
        plt.draw()                     # Ridisegna il grafico con la nuova posizione
        plt.pause(ritardo)              # Pausa per creare l'effetto di animazione

    
    
    
   
    plt.show()

# Facciamo partire il programma
main()