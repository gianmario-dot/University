import math
import matplotlib.pyplot as plt
import time
import datetime

def main():

    ora_corrente=datetime.datetime.now().hour
    minuti_correnti=datetime.datetime.now().minute
    secondi_correnti=datetime.datetime.now().second
    giono_corrente=datetime.datetime.now().day
    indice_giorno_settimana=datetime.datetime.now().weekday()


    figura, grafico = plt.subplots(num='By Gianmario Pelanda')
    grafico.set_xlim(-1.2, 1.2)
    grafico.set_ylim(-1.2, 1.2)
    grafico.set_aspect('equal')

    figura.patch.set_facecolor('black')
    grafico.axis('off')



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
    
    #ore=(12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    ore={12: 'GP', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI'}
    raggio_numeri = 0.77
    
    for i in ore:
        angolo_gradi = 90 - (i * 30)
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad = math.radians(angolo_gradi)
    
        # 3. ASSEGNO LE COORDINATE X e Y
        x = raggio_numeri * math.cos(angolo_rad)
        y = raggio_numeri * math.sin(angolo_rad)
    
        grafico.text(x, y, str(ore[i]), fontsize=20, ha='center', va='center', color='silver')


    ore={1: 'lun', 2: 'mar', 3: 'mer', 4: 'gio', 5: 'ven', 6: 'sab', 7: 'dom'}
    raggio_numeri = 0.18
    
    for i in ore:
        angolo_gradi = 90 - (i * (360/7))
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad = math.radians(angolo_gradi)
    
        # 3. ASSEGNO LE COORDINATE X e Y
        x = raggio_numeri * math.cos(angolo_rad)
        y = raggio_numeri * math.sin(angolo_rad)+0.35
    
        grafico.text(x, y, str(ore[i]), fontsize=6.5, ha='center', va='center', color='silver')


    
    grafico.text(0.4425, -0.005, giono_corrente, fontsize=10, ha='center', va='center', color='silver')
    
   


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
    larghezza_mn_line = 0.04
    altezza_mn_line = 0.1
    larghezza_hr_line= 0.005
    altezza_hr_line= 0.2

    cerchio_or = plt.Circle((qo.x, qo.y), qo.raggio, fill=True, edgecolor='silver', facecolor='#143860', linewidth=7)
    ln_sc = plt.Rectangle((0, 0), -larghezza_sc/2, altezza_sc, fill=True, color='silver')
    ln_hr = plt.Rectangle((0, 0), -larghezza_hr/2, altezza_hr, fill=True, color='silver')
    ln_mn = plt.Rectangle((0, 0), -larghezza_mn/2, altezza_mn, fill=True, color='silver')
    cerchio_cr = plt.Circle((0, 0), 0.05, fill=True, color='silver')
    #cerchio_day= plt.Circle((0, -0.35), 0.23, fill=False, color='silver')
    #cerchio_hr= plt.Circle((-0.35, 0), 0.23, fill=False, color='silver')
    #cerchio_gr= plt.Circle((0., 0.35), 0.23, fill=False, color='silver')
    sc_line = plt.Rectangle((0, 0), -larghezza_mn_line/2, altezza_mn_line, fill=True, color='silver')
    hr_line = plt.Rectangle((-0.35, 0), -larghezza_hr_line, altezza_hr_line, fill=True, color='silver')
    am_pm = plt.Rectangle((0, -0.35), 0.005, 0.2, fill=True, color='silver')
    separatore = plt.Rectangle((-0.21/2, -0.35), 0.21, 0.0001, fill=True, color='silver')
    ret_giorno = plt.Rectangle((0.32, -0.06), 0.25, 0.12, fill=False, color='silver')
    indx_gr = plt.Rectangle((0, 0.35), 0.005, 0.17, fill=True, color='silver')

    grafico.add_patch(cerchio_or)
    
    
    grafico.add_patch(sc_line)
    #grafico.add_patch(cerchio_day)
    #grafico.add_patch(cerchio_hr)
    grafico.add_patch(indx_gr)
    grafico.add_patch(hr_line)
    grafico.add_patch(ret_giorno)
    grafico.add_patch(separatore)
    grafico.add_patch(am_pm)
    grafico.add_patch(ln_mn)
    grafico.add_patch(ln_hr)
    grafico.add_patch(ln_sc)
    grafico.add_patch(cerchio_cr)




    teta_sc = 0
    teta_hr= -(ora_corrente*30)
    teta_mn= -(minuti_correnti*6)


    # Partiamo da zero per fare i conti precisi con la tua logica
    ln_sc.set_angle(teta_sc)
    ln_mn.set_angle(teta_mn)
    ln_hr.set_angle(teta_hr)

    teta_am_pm =-(ora_corrente*15)
    am_pm.set_angle(teta_am_pm)

    ore_day={12: '24', 1: '6', 2: '12', 3: '18'}
    raggio_numeri = 0.14
    
    for n in ore_day:
        angolo_gradi = 90 - (n * 90)
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad = math.radians(angolo_gradi)
    
        # 3. ASSEGNO LE COORDINATE X e Y
        x = raggio_numeri * math.cos(angolo_rad)
        y = raggio_numeri * math.sin(angolo_rad) - 0.35

        grafico.text(x, y, str(ore_day[n]), fontsize=8, ha='center', va='center', color='silver')


    for l in range(indice_giorno_settimana):
        angolo_gradi_gr = 90 - (l * (360/7))
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad_gr = math.radians(angolo_gradi_gr)
    

    indx_gr.set_angle(angolo_rad_gr)


    ore_day={12: '60', 1: '15', 2: '30', 3: '45'}
    raggio_numeri = 0.14
    
    for n in ore_day:
        angolo_gradi = 90 - (n * 90)
    
        # Python vuole i radianti, non i gradi! Li convertiamo:
        angolo_rad = math.radians(angolo_gradi)
    
        # 3. ASSEGNO LE COORDINATE X e Y
        x = raggio_numeri * math.cos(angolo_rad)-0.35
        y = raggio_numeri * math.sin(angolo_rad) 

        grafico.text(x, y, str(ore_day[n]), fontsize=8, ha='center', va='center', color='silver')

    
    raggio_mn=0.9

    for i in range(60):
        # 1. 360 gradi / 60 minuti = 6 gradi per ogni tacca
        angolo_gradi = 90 - (i * 6)
        angolo_rad = math.radians(angolo_gradi)

        if i % 5 == 0:
            spessore = 3
            raggio_interno = 0.90 # Più lunga verso il centro
        else:
            spessore = 1
            raggio_interno = 0.95 # Più corta

        # punto sul bordo esterno del cerchio
        x_est = raggio_mn * math.cos(angolo_rad)
        y_est = raggio_mn * math.sin(angolo_rad)

        #punto più interno
        x_int = raggio_interno * math.cos(angolo_rad)
        y_int = raggio_interno * math.sin(angolo_rad)

        grafico.plot([x_int, x_est], [y_int, y_est], color='silver', linewidth=spessore)



    raggio_sc=0.23

    for i in range(60):
        # 1. 360 gradi / 60 minuti = 6 gradi per ogni tacca
        angolo_gradi = 90 - (i * 6)
        angolo_rad = math.radians(angolo_gradi)

        if i % 5 == 0:
            spessore = 1
            raggio_interno = 0.19 # Più lunga verso il centro
        else:
            spessore = 0.5
            raggio_interno = 0.21 # Più corta

        # punto sul bordo esterno del cerchio
        x_est = raggio_sc * math.cos(angolo_rad)-0.35
        y_est = raggio_sc * math.sin(angolo_rad)

        #punto più interno
        x_int = raggio_interno * math.cos(angolo_rad)-0.35
        y_int = raggio_interno * math.sin(angolo_rad)

        grafico.plot([x_int, x_est], [y_int, y_est], color='silver', linewidth=spessore)



    
    centro_y = -0.35      # Spostiamo tutto in basso
    raggio_esterno_24 = 0.23

    for y in range(24):
        # 1. 360 gradi / 24 ore = 15 gradi per ogni tacca
        # Partiamo da 90 (le ore 12/24 in alto) e andiamo in senso orario (-)
        angolo_gradi = 90 - (y * 15)
        angolo_rad = math.radians(angolo_gradi)

        # 2. Tacche spesse ogni 6 ore (0, 6, 12, 18)
        if y % 6 == 0:
            spessore = 2
            raggio_interno_24 = 0.19 # Tacca più lunga
        else:
            spessore = 0.5
            raggio_interno_24 = 0.21 # Tacca più corta

        # 3. Calcolo i punti X e Y e li traslo in basso aggiungendo centro_y
        x_est = raggio_esterno_24 * math.cos(angolo_rad)
        y_est = raggio_esterno_24 * math.sin(angolo_rad) + centro_y

        x_int = raggio_interno_24 * math.cos(angolo_rad)
        y_int = raggio_interno_24 * math.sin(angolo_rad) + centro_y

        # 4. Tiro la linea
        grafico.plot([x_int, x_est], [y_int, y_est], color='silver', linewidth=spessore, zorder=2)
   


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

    hr_line.set_angle(nuovo_sc)
            
    plt.pause(0.01)
        

main()