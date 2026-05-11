import matplotlib.pyplot as plt
import numpy as np

# Impostazioni fisiche
N = 1000000        
tau = 1.0        
dt = 0.1         
dt_max = 50      
aggiorna_ogni = 200  # Aggiorniamo il grafico ogni 200 atomi calcolati per non bloccare il PC

# Inizializzazione dati
decadimenti = {passo: 0 for passo in range(1, dt_max + 1)}
passi_x = np.array(list(decadimenti.keys()))
tempi = (passi_x - 1) * dt

# --- PREPARAZIONE GRAFICO ANIMATO ---
plt.ion() # Attiva la modalità interattiva
figura, grafico = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})

# Creiamo le barre e la linea inizialmente vuote (tutte a zero)
barre_sim = grafico[0].bar(passi_x, np.zeros(dt_max), color='cornflowerblue', label='Simulazione')
linea_teo, = grafico[0].plot(passi_x, np.zeros(dt_max), color='red', linestyle='--', linewidth=2, label='Teoria')

grafico[0].set_title('Decadimento Radioattivo in Diretta', fontsize=14, fontweight='bold')
grafico[0].set_ylabel('Numero di atomi decaduti')
grafico[0].legend()
grafico[0].grid(axis='y', linestyle='--', alpha=0.7)

# Barre dell'errore (inizialmente a zero)
barre_err = grafico[1].bar(passi_x, np.zeros(dt_max), color='orange')
grafico[1].set_xlabel('Passi temporali (1 passo = 0.1s)')
grafico[1].set_ylabel('Errore Assoluto')
grafico[1].grid(axis='y', linestyle='--', alpha=0.7)

# Fissiamo l'asse X per non farlo "ballare" durante l'animazione
grafico[0].set_xlim(0, dt_max + 1)
grafico[1].set_xlim(0, dt_max + 1)
plt.tight_layout()

# --- CICLO DI SIMULAZIONE IN DIRETTA ---
atomi_calcolati = 0

for i in range(1, N + 1):
    # Logica di decadimento per il singolo atomo
    for passo in range(1, dt_max + 1):
        if np.random.uniform(0, 1) < (dt / tau):
            decadimenti[passo] += 1
            break

    atomi_calcolati += 1

    # --- AGGIORNAMENTO GRAFICO (Il battito cardiaco) ---
    if atomi_calcolati % aggiorna_ogni == 0 or atomi_calcolati == N:
        valori_simulati = np.array(list(decadimenti.values()))
        
        # Calcoliamo la teoria in base agli atomi processati FINORA (così cresce insieme alle barre!)
        valori_teorici = atomi_calcolati * (dt / tau) * np.exp(-tempi / tau)
        errore = np.abs(valori_simulati - valori_teorici)

        # 1. Alziamo le singole barre della simulazione
        for indice, barra in enumerate(barre_sim):
            barra.set_height(valori_simulati[indice])
            
        # 2. Aggiorniamo la linea rossa teorica
        linea_teo.set_data(passi_x, valori_teorici)

        # 3. Alziamo le singole barre dell'errore
        for indice, barra in enumerate(barre_err):
            barra.set_height(errore[indice])

        # 4. Adattiamo l'altezza dell'asse Y dinamicamente
        for ax in grafico:
            ax.relim()
            ax.autoscale_view()

        # Respiro per Windows
        plt.pause(0.01)

# Fine simulazione
plt.ioff()
print("Simulazione completata!")
plt.show()