import math
import matplotlib.pyplot as plt
import time

def main():

    figura, grafico = plt.subplots(num='By Gianmario Pelanda')
    grafico.set_xlim(-1.2, 1.2)
    grafico.set_ylim(-1.2, 1.2)
    grafico.set_aspect('equal')



    class quadrante:
        def __init__(self, x, y, raggio):
            self.x = x
            self.y = y
            self.raggio = raggio
            
    class orario:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class ore_qo:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    ore=[12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    raggio_numeri = 0.85
    
    for i in ore:
        angolo_gradi = 90 - (i * 30)
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad = math.radians(angolo_gradi)
    
        # 3. ASSEGNO LE COORDINATE X e Y
        x = raggio_numeri * math.cos(angolo_rad)
        y = raggio_numeri * math.sin(angolo_rad)
    
        grafico.text(x, y, str(i), fontsize=14, fontweight='bold', ha='center', va='center')


    qo = quadrante(0, 0, 1)
    sc = orario(0, 0)
    hr = orario(0, 0)
    mn = orario(0, 0)

    
    larghezza_sc = 0.02
    altezza_sc = 0.95
    larghezza_mn = 0.04
    altezza_mn = 0.7
    larghezza_hr = 0.08
    altezza_hr = 0.4

    cerchio_or = plt.Circle((qo.x, qo.y), qo.raggio, fill=False, color='black', linewidth=2)
    ln_sc = plt.Rectangle((0, 0), larghezza_sc, altezza_sc, fill=True, color='red')
    ln_hr = plt.Rectangle((0, 0), larghezza_hr, altezza_hr, fill=True, color='black')
    ln_mn = plt.Rectangle((0, 0), larghezza_mn, altezza_mn, fill=True, color='black')
    cerchio_cr = plt.Circle((0, 0), 0.05, fill=True, color='black')

    grafico.add_patch(cerchio_or)
    grafico.add_patch(ln_mn)
    grafico.add_patch(ln_hr)
    grafico.add_patch(ln_sc)
    grafico.add_patch(cerchio_cr)

    # Partiamo da zero per fare i conti precisi con la tua logica
    ln_sc.set_angle(0)
    ln_mn.set_angle(0)
    ln_hr.set_angle(0)
    


    plt.ion()
    plt.show()
    # Stampo il numero sul grafico alle coordinate appena calcolate
        # (ha='center' e va='center' centrano la scritta esattamente sul punto (X,Y))
    
    tempo_precedente = time.time()

    
    while True:
        tempo_attuale = time.time()

        if tempo_attuale - tempo_precedente >= 1.0: 
            
            # 1. Leggo l'angolo vecchio, aggiungo 6, e lo riassegno
            nuovo_sc = ln_sc.get_angle() - 6
            ln_sc.set_angle(nuovo_sc)
            
            # 2. SE i secondi hanno fatto un giro completo...
            if ln_sc.get_angle() >= 360:
                ln_sc.set_angle(0)
                
                # ...faccio scattare l'ingranaggio dei minuti (+6 gradi)
                nuovo_mn = ln_mn.get_angle() - 6
                ln_mn.set_angle(nuovo_mn)

                # 3. SE i minuti hanno fatto un giro completo...
                if ln_mn.get_angle() >= 360:
                    ln_mn.set_angle(0) # Azzero l'ingranaggio!
                    
                    
                    nuovo_hr = ln_hr.get_angle() - 30
                    ln_hr.set_angle(nuovo_hr)

            figura.canvas.draw()
            figura.canvas.flush_events()

            # Resetto il cronometro
            tempo_precedente = tempo_attuale 
            
        plt.pause(0.01)

main()