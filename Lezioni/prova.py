import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Prepariamo la nostra "tela" e il grafico vuoto
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title("Simulazione di un'onda (es. vibrazione atomica)")
ax.set_xlabel("Spazio")
ax.set_ylabel("Ampiezza")
ax.grid(True)

# Creiamo una linea iniziale "vuota" che aggiorneremo
x = np.linspace(0, 10, 200)
linea, = ax.plot([], [], color='blue', lw=2)

# 2. La funzione magica che crea i fotogrammi
def aggiorna_fotogramma(tempo):
    # L'onda si sposta in avanti in base al "tempo"
    y = np.sin(x - tempo/5.0) 
    
    # Aggiorniamo i dati della linea
    linea.set_data(x, y)
    return linea,

# 3. Facciamo partire l'animazione!
# frames = numero di fotogrammi
# interval = millisecondi di pausa tra un fotogramma e l'altro (più è basso, più è veloce)
animazione = FuncAnimation(fig, aggiorna_fotogramma, frames=500, interval=2)

# 4. Mostriamo il risultato a schermo
plt.show()
