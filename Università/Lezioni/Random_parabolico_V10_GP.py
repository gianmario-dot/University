import numpy as np
import matplotlib.pyplot as plt
import random


salta_animazione = False

def chiudi_tutto(evento):
    raise SystemExit

# Controllo tastiera
def on_key(event):
    global salta_animazione
    if event.key == ' ' or event.key == 'space' or event.key == 'enter':
        salta_animazione = True
        print("\n TASTO PREMUTO:  Calcolo in corso... ")


def disegna_funzione(inizio, fine):
    # Creiamo set funz
    print("per compito parabola coeff a=1. b=-10, c=25")
    print("Scegli quale funzione vuoi graficare:")
    print("1: Parabola (x^2)")
    print("2: Cubo (x^3)")
    print("3: Logaritmo naturale (ln(x))")
    print("4: Iperbole (1/x)")
    print("5: Seno (sin(x))")
    print("6: Coseno (cos(x))")

    # input n funz
    scelta = input("\nInserisci il numero della funzione (1-6): ")

    
    x = np.linspace(inizio, fine, 1000)

    # impostazioni funz
    if scelta == '1':
        nome_funzione = "a*x^2 + b*x + c"
        print(nome_funzione)
        a = float(input('coefficente a = '))
        b = float(input('coefficente b = '))
        c = float(input('coefficente c = '))
        y_Funz = a*(x**2) + b*(x) + c

    elif scelta == '2':
        nome_funzione = "a*x^3 + b*x^2 + c*x + d"
        print(nome_funzione)
        a = float(input('coefficente a = '))
        b = float(input('coefficente b = '))
        c = float(input('coefficente c = '))
        d = float(input('coefficente d = '))
        y_Funz = a * x**3 + b * x**2 + c * x + d
        
    elif scelta == '3':
        nome_funzione = "y = a*ln(b*x + c)"
        print(nome_funzione)
        a=float(input('coefficente moltiplicativo a ='))
        b=float(input('coefficente b ='))
        c=float(input('traslazione su x, coeff c ='))
        y_Funz = a*np.log(b*x + c)
        
    elif scelta == '4':
        nome_funzione = "y = c + a/(x-b)"
        print(nome_funzione)
        a=float(input('costante di proporzionalità inversa a ='))
        b=float(input('traslazione su asse x,coef b ='))
        c=float(input('traslazione su y, coeff c ='))
        y_Funz = c + a / (x+b)
        
    elif scelta == '5':
        nome_funzione = "y = a*sin(b*x + c)"
        print(nome_funzione)
        a=float(input('Ampiezza a ='))
        b=float(input('Pulsazione,coef b ='))
        c=float(input('Fase iniziale (per coseno c=), coeff c ='))
        y_Funz = a*np.sin(b*x + c)

    elif scelta == '6':
        nome_funzione = "y = a*cos(b*x + c)"
        print(nome_funzione)
        a=float(input('Ampiezza a ='))
        b=float(input('Pulsazione,coef b ='))
        c=float(input('Fase iniziale (per coseno c=), coeff c ='))
        y_Funz = a*np.cos(b*x + c)
        
    else:
        print("Errore")
        y_Funz = x * 0
        nome_funzione = "Errore"

    return x, y_Funz, nome_funzione


def trova_numero(x, y_Funz, sample_size, inizio, fine, grafico1, grafico2):
    global salta_animazione 
    numeri_trovati = []
    
    tetto_massimo = np.max(y_Funz)
    tentativi_totali = 0 

    while len(numeri_trovati) < sample_size:
        tentativi_totali += 1
        
        x_rnd = random.uniform(inizio, fine)
        y_rnd = random.uniform(0, tetto_massimo)

        posizione = x_rnd - inizio
        percentuale_relativa = posizione / (fine - inizio)
        valore_x = int(percentuale_relativa * 999)

        altezza_curva = y_Funz[valore_x]

        
        if y_rnd <= altezza_curva:
            numeri_trovati.append(x_rnd)
            
            
            if not salta_animazione:
                grafico2.plot(x_rnd, y_rnd, 'go', markersize=3)
                
                if len(numeri_trovati) % 20 == 0:
                    grafico1.clear()
                    grafico1.hist(numeri_trovati, bins=30, range=(inizio, fine), color='orange', edgecolor='black')
                    grafico1.set_xlim(inizio, fine)
                    grafico1.set_title(f'Distribuzione (n={len(numeri_trovati)})')
                    grafico1.set_xlabel('Numbers')
                    grafico1.set_ylabel('Counts')
                    plt.pause(0.001)

        
        else: 
            if not salta_animazione:
                grafico2.plot(x_rnd, y_rnd, 'ro', markersize=3)
                if tentativi_totali % 50 == 0:
                    plt.pause(0.001)
                    
    return numeri_trovati


def main():
    global salta_animazione 

    inizio = int(input('Inserisci il limite minore del range dei numeri interessati = '))
    fine = int(input('Inserisci il limite maggiore del range dei numeri interessati  = '))
    sample_size = int(input('Quanti numeri distribuiti vuoi generare? (per compito 100000) = '))

    # salto animazione veloce
    scelta_animazione = input('Vuoi vedere animazione? (y/n) = ')
    if scelta_animazione.lower() == 'n':
        salta_animazione = True
   

    x, y_Funz, nome_funzione = disegna_funzione(inizio, fine)
    
    figura, (grafico1, grafico2) = plt.subplots(1, 2, figsize=(12, 6), num='Simulazione Monte Carlo', layout='constrained')

    
    figura.canvas.mpl_connect('key_press_event', on_key)
    figura.canvas.mpl_connect('close_event', chiudi_tutto)

    grafico2.plot(x, y_Funz, label=f'Funzione {nome_funzione}', color='blue', linewidth=2)
    grafico2.set_title("Randomizer")
    grafico2.set_xlim(inizio, fine)
    
    y_min = np.min(y_Funz)
    y_max = np.max(y_Funz)
    if y_max > 100 or y_min < -100:
        grafico2.set_ylim(-20, y_max + (y_max*0.1))
    else:
        grafico2.set_ylim(y_min - abs(y_min) - 1, y_max + abs(y_max*0.1) + 1)
        grafico2.legend()

    grafico1.set_xlim(inizio, fine)
    grafico1.set_title('Distribuzione (Premi SPAZIO per saltare animazione)')

    # simulazione
    numeri_trovati = trova_numero(x, y_Funz, sample_size, inizio, fine, grafico1, grafico2)

    # Disegno finale
    grafico1.clear()
    grafico1.hist(numeri_trovati, bins=100, range=(inizio, fine), color='orange', edgecolor='black')
    grafico1.set_xlim(inizio, fine)
    grafico1.set_title(f'Distribuzione FINALE (n={sample_size})')
    grafico1.set_xlabel('Numbers')
    grafico1.set_ylabel("Counts")
    
    # titolo finito di calcolare
    figura.suptitle("Simulazione Completata!", fontsize=16, fontweight='bold')
    
    plt.show()

main()