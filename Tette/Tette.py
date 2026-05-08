import tkinter as tk
import math
import time

# --- Impostazioni base della finestra ---
WIDTH = 800
HEIGHT = 600

# Parametri base delle sfere
R = 100 # Raggio base cerchi esterni
r = 13  # Raggio base cerchi interni (ora è un terzo rispetto a prima)

# Posizioni centrali
cx_left = WIDTH // 2 - R - 10
cx_right = WIDTH // 2 + R + 10
cy_base = HEIGHT // 2

# Inizializzazione della finestra Tkinter
root = tk.Tk()
root.title("Animazione Sfere Deformabili - Tkinter")
root.geometry(f"{WIDTH}x{HEIGHT}")

# Creazione della tela (Canvas) dove disegneremo
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#FFCBA4", highlightthickness=0)
canvas.pack()

# --- Creazione degli oggetti grafici ---
outer_left = canvas.create_oval(0, 0, 0, 0, fill="#FFCBA4", outline="#ff6496")
inner_left = canvas.create_oval(0, 0, 0, 0, fill="#ff6496", outline="#961432")

outer_right = canvas.create_oval(0, 0, 0, 0, fill="#FFCBA4", outline="#ff6496")
inner_right = canvas.create_oval(0, 0, 0, 0, fill="#ff6496", outline="#961432")

# Salviamo il tempo di inizio per calcolare l'oscillazione fluida
start_time = time.time()

def animate():
    """Funzione che aggiorna le coordinate delle sfere creando l'animazione"""
    # Calcola il tempo trascorso (moltiplicato per 2 per regolare la velocità)
    t = (time.time() - start_time) * 2
    
    # L'onda sinusoidale oscilla tra -1 e 1
    oscillation = math.sin(t)
    
    # Deformazione e movimento verticale
    y_offset = 30 * oscillation
    dw = 20 * oscillation   # Si allarga e si stringe
    dh = -20 * oscillation  # Si schiaccia in verticale
    
    # --- Aggiornamento Sfera Sinistra ---
    # Cerchio Esterno (calcolo coordinate: x_min, y_min, x_max, y_max)
    canvas.coords(outer_left, 
                  cx_left - (R + dw), cy_base + y_offset - (R + dh),
                  cx_left + (R + dw), cy_base + y_offset + (R + dh))
    
    # Cerchio Interno (si deforma un po' meno)
    canvas.coords(inner_left, 
                  cx_left - (r + dw/3), cy_base + y_offset - (r + dh/3),
                  cx_left + (r + dw/3), cy_base + y_offset + (r + dh/3))

    # --- Aggiornamento Sfera Destra ---
    # Cerchio Esterno
    canvas.coords(outer_right, 
                  cx_right - (R + dw), cy_base + y_offset - (R + dh),
                  cx_right + (R + dw), cy_base + y_offset + (R + dh))
    
    # Cerchio Interno
    canvas.coords(inner_right, 
                  cx_right - (r + dw/3), cy_base + y_offset - (r + dh/3),
                  cx_right + (r + dw/3), cy_base + y_offset + (r + dh/3))

    # Richiama questa stessa funzione dopo 16 millisecondi (~60 Frame Per Secondo)
    root.after(16, animate)

# Avviamo il ciclo di animazione
animate()

# Mantiene la finestra aperta
root.mainloop()