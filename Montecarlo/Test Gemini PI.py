import matplotlib.pyplot as plt
import numpy as np

# Impostazione grafico
ritardo = 0.001
N = int(input('Numero tentativi = '))

inside_count = 0
iteration = []
pi_values = []
errors = []
pi_exact = np.pi

# Creo il grafico
figura, grafico = plt.subplots(2, 1, num='Calcolo di PI, by Gianmario Pelanda', figsize=(12, 10))
grafico[0].axhline(pi_exact, color='red', linestyle='--', label='Valore esatto PI')
grafico[0].legend()
grafico[0].set_xscale('log')
grafico[0].set_ylabel('Stima di PI')
grafico[0].grid()

grafico[1].set_xscale('log')
grafico[1].set_yscale('log')
grafico[1].set_ylabel('Errore')
grafico[1].set_xlabel('Numero iterazioni')
grafico[1].grid()

Testo = grafico[1].text(0.1, 0.8, '', transform=grafico[1].transAxes, fontsize=11, bbox=dict(facecolor='white', alpha=0.8))

g0, = grafico[0].plot([], [], 'go', linestyle='-', markersize=4)
g1, = grafico[1].plot([], [], 'bo', linestyle='-', markersize=4)

Io = 1  # Partiamo da 1 per il grafico logaritmico

for i in range(1, N + 1):
    # Genera un punto alla volta (come facevate in classe)
    x, y = np.random.uniform(-1, 1, 2)
    distance = x**2 + y**2
    if distance <= 1:
        inside_count += 1
        
    # LOGICA LOGARITMICA CORRETTA:
    # Aggiorna il grafico solo quando 'i' raggiunge esattamente 'Io' (1, 10, 100, 1000...)
    if i == Io:
        pi_greco = (inside_count / i) * 4
        
        iteration.append(i)
        pi_values.append(pi_greco)
        errore = abs(pi_exact - pi_greco) / pi_exact
        errors.append(errore)
        
        # Aggiorno i dati delle linee
        g0.set_data(iteration, pi_values)
        g1.set_data(iteration, errors)
        
        grafico[0].relim()
        grafico[0].autoscale_view()
        grafico[1].relim()
        grafico[1].autoscale_view()

        Testo.set_text(f'N = {i:,} | PI = {pi_greco:5.6f} | Errore = {errore:4.3%}')
        
        plt.pause(ritardo)
        
        # Moltiplichiamo Io per 10 in modo pulito! 
        # Il prossimo aggiornamento sarà 10 -> 100 -> 1000 -> 10000
        Io *= 10  
        
    # --- IL SEGRETO PER NON FAR BLOCCARE WINDOWS ---
    # Tra 1 milione e 10 milioni c'è un sacco di tempo. 
    # Questo comando invisibile dice a Windows "Sono ancora vivo" senza rallentare troppo il grafico.
    elif i % 100000 == 0:
        figura.canvas.flush_events()

print(f"Finito! Valore finale di PI: {(inside_count / N) * 4}")
plt.show()