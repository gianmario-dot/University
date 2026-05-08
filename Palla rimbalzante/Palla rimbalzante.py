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
    pp = Palla(-1, 0.8, 0.02, 0.1, 0.6)
    
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

    # Creo i dati per seno e coseno
    x = list(range(-100, 100, 1)) 
    x = [i/100 for i in x] 
    y = [math.sin(i*3.1415) for i in x] 
    y1 = [math.cos(i*3.1415) for i in x] 
    
    # Disegno le due curve
    a, = Grafico.plot(x, y) 
    b, = Grafico.plot(x, y1) 

    plt.show()
    input('Premi Invio per rimuovere il coseno...')  # Aspetta che l'utente prema Invio 

    
    plt.draw()     # Forza Matplotlib a disegnare subito la finestra
    plt.pause(5)   # Mette in pausa per 2 secondi (così puoi vederle entrambe)
    
    b.set_color('yellow')     # Rimuove l'onda del coseno!
    
   
    plt.show()

# Facciamo partire il programma
main()