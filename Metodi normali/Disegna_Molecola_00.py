# Disegna il campo elettrico generato da una distribuzione di cariche defiita tramite click del mouse
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
import tkinter as tk
from tkinter import filedialog

def chiudi_tutto(evento):   # chiude il programma se si chiude la finestra grafica
    raise SystemExit

def inserisci_costanti_elastiche(Figura,Grafico,casella_txt,punti):
 
    def onclick(parametri):  # funzione attivata dal click del mouse
        nonlocal finito   # 'nonlocal' permette la modifica di una variabile della funzion madre che altrimenti sarrebbe accessibile solo in lettura
        nonlocal primo_click
        nonlocal punto1
        #nonlocal molle
        if parametri.inaxes!=Grafico:  # se il click è avvunuto fuori dal grafico ... non fare nulla 
            return
        if parametri.button==1:  # se si è clickato il tato sx, leggi la posizione e il valore della carica e aggiungilo in punti[]
            try:   # non fatto a lezione. Se si verifica un errore lo gestisce.
                carica=float(casella_txt.text)
                minimo=1e300
                if primo_click:
                    for i in range(n_punti):
                        distanza=(parametri.xdata-punti[i][0])**2+(parametri.ydata-punti[i][1])**2
                        if distanza<minimo:
                            minimo=distanza
                            primo_click=False
                            punto1=i
                            #disegna_linea=True
                else:
                    for i in range(n_punti):
                        distanza=(parametri.xdata-punti[i][0])**2+(parametri.ydata-punti[i][1])**2
                        if distanza<minimo:
                            minimo=distanza
                            primo_click=True
                            punto2=i
                            #disegna_linea=False
                    molle[punto1,punto2]=float(casella_txt.text)
                    molle[punto2,punto1]=float(casella_txt.text)      
                    Grafico.plot([punti[punto1][0],punti[punto2][0]],[punti[punto1][1],punti[punto2][1]],color='black', linewidth=3)                                             
                    linea.set_data([10,10],[10,10])


            except:        # gestione dell'errore
                casella_txt.set_val('')
                casella_txt.begin_typing()
                return
        elif parametri.button==3:   # e si è clickato il tato dx, segnala che è ora di uscire
            finito=True
        casella_txt.begin_typing()   # riporta il focus sulla TextBox
        return molle



    def on_move(parametri):
        if primo_click:
            return
        linea.set_data([punti[punto1][0],parametri.xdata],[punti[punto1][1],parametri.ydata])
        
        return


  
    finito=False   # mi serve per capire quando uscire
    primo_click=True
    #disegna_linea=False
    n_punti=len(punti)
    molle=np.zeros((n_punti,n_punti))
    punto1=0
    codice=Figura.canvas.mpl_connect('button_press_event',onclick)   # Connette la funzione onclick all'evento 'button_press_event' dell'oggetto figura)
    forza=Figura.canvas.mpl_connect('motion_notify_event',on_move)
    linea,=Grafico.plot([10,10],[10,10],color='black')
    casella_txt.begin_typing() # porta il focus sulla TextBox
    casella_txt.set_val('2')
    while not finito:  # Resta sempre sulla GUI fino a quando il parametro finito diventa vero
        plt.pause(0.1)
    Figura.canvas.mpl_disconnect(codice)  # Disconette l'evento dall'oggetto Figura 
    return molle

# Funzione per leggere dal click del mouse le coordinate delle cariche e dal TextBox il loro valore 
def seleziona_punti(Figura,Grafico,casella_txt):
    finito=False   # mi serve per capire quando uscire
    punti=[]  # lista con posizione x,y e carica delle cariche] 
    def onclick(parametri):  # funzione attivata dal click del mouse
        nonlocal finito   # 'nonlocal' permette la modifica di una variabile della funzion madre che altrimenti sarrebbe accessibile solo in lettura
        if parametri.inaxes!=Grafico:  # se il click è avvunuto fuori dal grafico ... non fare nulla 
            return
        if parametri.button==1:  # se si è clickato il tato sx, leggi la posizione e il valore della carica e aggiungilo in punti[]
            try:   # non fatto a lezione. Se si verifica un errore lo gestisce.
                carica=float(casella_txt.text)
                minimo=1e300
                for i in np.arange(-1,1.1,0.1):
                    for j in np.arange(-1,1.1,0.1):
                        distanza=(parametri.xdata-i)**2+(parametri.ydata-j)**2
                        if distanza<minimo:
                            punto=(i,j,carica)
                            minimo=distanza
                
                punti.append(punto)

                Grafico.plot(punto[0],punto[1],'o',markersize=5, color='red')
            except:        # gestione dell'errore
                casella_txt.set_val('')
                casella_txt.begin_typing()
                return
        elif parametri.button==3:   # e si è clickato il tato dx, segnala che è ora di uscire
            finito=True
        casella_txt.begin_typing()   # riporta il focus sulla TextBox
        return
  
    codice=Figura.canvas.mpl_connect('button_press_event',onclick)   # Connette la funzione onclick all'evento 'button_press_event' dell'oggetto figura)
    casella_txt.begin_typing() # porta il focus sulla TextBox
    casella_txt.set_val('1')
    while not finito:  # Resta sempre sulla GUI fino a quando il parametro finito diventa vero
        plt.pause(0.1)
    Figura.canvas.mpl_disconnect(codice)  # Disconette l'evento dall'oggetto Figura 
    return punti

def main():
    # Setting del GUI
    Figura, Grafico = plt.subplots(num='By Franco Meinardi',figsize=(10,5))
    Grafico.set_xlim(-1,1)
    Grafico.set_ylim(-1, 1)
    Grafico.set_aspect('equal')
    coordinate=Figura.add_axes([0.45,0.9,0.1,0.05])
    Grafico.set_xticks([-1,-0.5,0,0.5,1])
    Grafico.set_yticks([-1,-0.5,0,0.5,1])
    Grafico.set_xticks(np.linspace(-1,1,21),minor=True)
    Grafico.set_yticks(np.linspace(-1,1,21),minor=True)
    Grafico.grid(True,which='major', color='gray', linewidth=0.8, linestyle='--')
    Grafico.grid(True,which='minor', color='lightgray', linewidth=0.6, linestyle=':')
    Figura.canvas.mpl_connect('close_event',chiudi_tutto)  # Disconette l'evento dall'oggetto Figura 

    casella_txt=widgets.TextBox(coordinate,'Mass ')


    # Fase 1: legge interattivamente valore e posizione degli atomi
    punti=seleziona_punti(Figura,Grafico,casella_txt)
    [print(i) for i in punti]

    # Fase 2: legge interattivamente valore costanti elastiche
    n_punti=len(punti)
    molle=np.zeros((n_punti,n_punti))
    casella_txt.label.set_text('Elastic Constant')
    molle=inserisci_costanti_elastiche(Figura,Grafico,casella_txt,punti)
    print('_______________')
    print(molle)

    root = tk.Tk()  #procedure per leggere interattivamente un file
    root.withdraw() 
    nome_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("ASCII", "*.txt"), ("Tutti i file", "*.*")],title="Open")

    # scrivo il file in modo che venga letto dal visualizzatore di modeli
    with open(nome_file,'w') as f:

        for i in range(n_punti):
            riga=f'{punti[i][0]:5.2f},{punti[i][1]:5.2f},{punti[i][2]:5.2f}\n'
            f.write(riga)
        
        f.write('_\n')

        for i in range(n_punti):
            riga=''
            for j in range(n_punti):
                riga+=f'{molle[i][j]:5.2f}'
            riga=riga[-1]+'\n'
            f.write(riga)




   


main()
plt.show()


Grafico.plot([punti[punto1][0],punti[punto2][0]],[punti[punto1][1],punti[punto2][1]],color='black', linewidth=3)
