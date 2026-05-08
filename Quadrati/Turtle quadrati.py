import turtle

# --- LE TUE FUNZIONI ORIGINALI ---
def prima_stringa(n_lato):
    stringa = '+'
    n = (n_lato - 3) // 2              
    for i in range(0, n):         
        stringa += '-'
    stringa += '+'
    for i in range(0, n):         
        stringa += '-'
    stringa += '+'
    return stringa

def seconda_stringa(n_lato):
    stringa = '|'
    n = (n_lato - 3) // 2              
    for i in range(0, n):         
        stringa += ' '
    stringa += '|'
    for i in range(0, n):         
        stringa += ' '
    stringa += '|'
    return stringa

# --- LA TUA FUNZIONE DISEGNA ---
def disegna(lato):
    n_lato = abs(int(lato))

    if n_lato % 2 == 0:
        print('Il lato del quadrato dovrebbe essere dispari')
        return
    
    if n_lato <= 3:
       print('Il lato del quadrato deve essere più lungo di 3')
       return
    
    n = (n_lato - 3) // 2

   
    # ---- SETUP DI TURTLE ----
    schermo = turtle.Screen()
    
    # --- TRUCCO PER METTERE LA FINESTRA IN PRIMO PIANO ---
    finestra_tk = schermo.getcanvas().winfo_toplevel()
    finestra_tk.attributes('-topmost', True)   # La spinge sopra tutte le altre finestre
    finestra_tk.attributes('-topmost', False)  # La "sblocca" così puoi rimpicciolirla dopo
    # -----------------------------------------------------

    schermo.title("Il Quadrato Matematico")
    
    schermo.bgcolor("black")  # Sfondo nero da vero hacker

    t = turtle.Turtle()
    t.shape("turtle")         # Diamo al cursore la forma di una vera tartaruga
    t.color("lime")           # Colore del testo e della tartaruga
    t.speed(0.515)                # Velocità media per vederla muoversi
    t.penup()                 # Alziamo la penna per non tirare righe quando va a capo

    # Coordinate di partenza (in alto a sinistra)
    asse_y = 150
    t.goto(-100, asse_y)

    # Funzione interna che usa la tartaruga come "stampante"
    def scrivi_su_schermo(testo):
        nonlocal asse_y
        # Scrive la stringa con un font monospazio
        t.write(testo, font=("Courier", 20, "bold"))
        asse_y -= 15          # Scendiamo di 30 pixel lungo l'asse Y (andiamo a capo)
        t.goto(-100, asse_y)  # Riportiamo la tartaruga all'inizio della nuova riga

    # --- IL TUO IDENTICO CICLO LOGICO ---
    scrivi_su_schermo(prima_stringa(n_lato))

    for i in range(0, n):
        scrivi_su_schermo(seconda_stringa(n_lato))

    scrivi_su_schermo(prima_stringa(n_lato))

    for i in range(0, n):
        scrivi_su_schermo(seconda_stringa(n_lato))

    scrivi_su_schermo(prima_stringa(n_lato))

    # Fine: chiude la finestra grafica quando ci clicchi sopra
    schermo.exitonclick()

# --- FUNZIONE PRINCIPALE ---
def main():
    lato = input('Lunghezza lato quadrato: \n')
    disegna(lato)

# Facciamo partire il programma
main()