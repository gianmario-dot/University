from vpython import canvas, sphere, vector, rate, sin
import time

# --- Impostazioni base della scena 3D ---
# VPython aprirà automaticamente una finestra nel tuo browser per mostrare il 3D
scene = canvas(width=800, height=600, background=vector(1.0, 0.80, 0.64)) # Sfondo #FFCBA4

# Parametri base delle sfere
R = 2.0         # Raggio base sfere esterne
r = R / 3.0     # Raggio sfere interne (esattamente un terzo)

# --- Creazione degli oggetti 3D ---
# Colore esterno: #ff6496. Usiamo opacity=0.4 per renderle trasparenti (effetto vetro)
color_outer = vector(1.0, 0.39, 0.59)
# Colore interno: #961432.
color_inner = vector(0.59, 0.08, 0.20)

# Sfere Sinistre
outer_left = sphere(pos=vector(-3, 0, 0), radius=R, color=color_outer, opacity=0.4)
inner_left = sphere(pos=vector(-3, 0, 0), radius=r, color=color_inner)

# Sfere Destre
outer_right = sphere(pos=vector(3, 0, 0), radius=R, color=color_outer, opacity=0.4)
inner_right = sphere(pos=vector(3, 0, 0), radius=r, color=color_inner)

# Tempo di inizio
start_time = time.time()

# --- Ciclo di Animazione ---
while True:
    rate(60) # Fissa a 60 FPS
    
    # Calcolo del tempo e dell'oscillazione
    t = (time.time() - start_time) * 2
    osc = sin(t)
    
    # Movimento verticale
    y_offset = 1.5 * osc
    
    # Deformazione 3D (schiacciamento verticale, allargamento su asse X e Z)
    dw = 0.5 * osc
    dh = -0.5 * osc
    
    # Calcolo delle nuove dimensioni (lunghezza, altezza, profondità)
    # In VPython le dimensioni si impostano con il diametro (raggio * 2)
    outer_size = vector((R + dw)*2, (R + dh)*2, (R + dw)*2)
    inner_size = vector((r + dw/3)*2, (r + dh/3)*2, (r + dw/3)*2)
    
    # Applica le deformazioni
    outer_left.size = outer_size
    outer_right.size = outer_size
    
    inner_left.size = inner_size
    inner_right.size = inner_size
    
    # Applica il movimento verticale (asse Y)
    outer_left.pos.y = y_offset
    inner_left.pos.y = y_offset
    
    outer_right.pos.y = y_offset
    inner_right.pos.y = y_offset