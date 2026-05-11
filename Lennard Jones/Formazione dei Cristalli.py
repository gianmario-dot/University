# Formazione dei Cristalli
# Dati due atomi dividiamo con Bohr-Opp dividiamo nucleare ed elettronico
# Risolvo Schroedinger cambiando le distanze fino a quando non trovo minimo
# Fitto i punti con una curva che li approssimi in modo adeguato

import matplotlib.pyplot as plt
import numpy as np
import configparser
import os
from matplotlib.animation import FFMpegWriter  # libreria per la creazione di video




def chiudi_tutto(event):
    print("Closing the simulation...")
    raise SystemExit




def load_config(file_path):
    config = configparser.ConfigParser()            # Crea oggetto che contiene la categoria e la chiave con il valore corrispondente
    config.read(file_path)


    # Parametri Generali
    params = {
        'width': config.getfloat('SPAZIO', 'width'),
        'height': config.getfloat('SPAZIO', 'height'),
        'n_a': config.getint('SPAZIO', 'n_atomi_a'),
        'n_b': config.getint('SPAZIO', 'n_atomi_b'),
        'mode': config.get('SPAZIO', 'init_mode'),
        'dt': config.getfloat('SIMULAZIONE', 'dt'),
        'steps': config.getint('SIMULAZIONE', 'steps'),
        'cutoff': config.getfloat('SIMULAZIONE', 'cutoff'),
        'dist_min': config.getfloat('SIMULAZIONE', 'dist_min'),
        'vel_max': config.getfloat('SIMULAZIONE', 'velocita_max'),
        'fps': config.getint('SIMULAZIONE', 'fps'),
        'dpi': config.getint('SIMULAZIONE', 'dpi'),
        'nome_file': config.get('SIMULAZIONE', 'nome_file'),
        'seme': config.getint('SIMULAZIONE', 'seme'),
    }


    # Proprietà Atomi (Masse e Colori)
    # Usiamo 0 per A e 1 per B
    params['colors'] = [config.get('ATOMO_A', 'colore'), config.get('ATOMO_B', 'colore')]

    # Matrici Lennard-Jones (sigma e epsilon)
    # Struttura: mat[id_tipo1][id_tipo2]
    s_aa = config.getfloat('ATOMO_A', 'sigma_aa')
    s_ab = config.getfloat('ATOMO_A', 'sigma_ab')
    s_bb = config.getfloat('ATOMO_B', 'sigma_bb')
    
    e_aa = config.getfloat('ATOMO_A', 'epsilon_aa')
    e_ab = config.getfloat('ATOMO_A', 'epsilon_ab')
    e_bb = config.getfloat('ATOMO_B', 'epsilon_bb')

    # Convertiamo le matrici in array NumPy prima di restituirle (è veloce perchè i dizionario contiene ...
    # ... solo il puntatore alla matrice)
    params['sigmas'] = np.array([[s_aa, s_ab], 
                                 [s_ab, s_bb]])
    
    params['epsilons'] = np.array([[e_aa, e_ab], 
                                   [e_ab, e_bb]])
    
    params['masses'] = np.array([config.getfloat('ATOMO_A', 'massa'), 
                                 config.getfloat('ATOMO_B', 'massa')])

    return params




def setup_graphics(params):
    # Creiamo la figura e il grafico con le dimensioni e DPI del file ini
    figura, grafico = plt.subplots(figsize=(8, 8), dpi=params['dpi'], num='By Gianmrio Pelanda - Crystal\'s Formation')
    
    # Impostiamo i limiti degli assi in base alle dimensioni dello spazio
    grafico.set_xlim(0, params['width'])
    grafico.set_ylim(0, params['height'])
    
    # Etichette in inglese
    grafico.set_title("Lennard-Jones Crystal Formation Simulation")
    grafico.set_xlabel("x [Distance Units]")
    grafico.set_ylabel("y [Distance Units]")
    
    # Aspect ratio uguale per non deformare il cristallo (i cerchi devono essere cerchi)
    grafico.set_aspect('equal')

    # Connessione dell'evento di chiusura
    figura.canvas.mpl_connect('close_event', chiudi_tutto)
    
    return figura, grafico







def inizializzazione(params):
    n_a=params['n_a']
    n_b=params['n_b']
    n_tot=n_a+n_b
    
    posizioni=np.zeros((n_tot, 2))
    tipi=np.array([0]*n_a+[1]*n_b)

    # Dobbiamo capire quale è la minima distanza a cui stanno gli atomi
    # Sappiamo che la distanza di equilibrio è sigma (1,5 o 2 sigma)
    dist_minima=params['dist_min']*np.max(params['sigmas'])**2                    # Usiamo il più grande dei parametri dato che sono più atomi


    # Generiamo le x e le y
    count=0
    troppi=0
    np.random.seed(params['seme'])

    while count<n_tot:
        # Gestione bordi
        margine=0.05

        # Abbiamo usato un seme cosi che se non cambia il smee la rarndomizzaizone sarà sempre uguale 
        # e cosi la simulazione (per cambiare simulazione devo cambiare seme)
        new_pos = np.array([np.random.uniform(margine*params['width'], (1-margine)*params['width']), 
                            np.random.uniform(margine*params['height'], (1-margine)*params['height'])])

        # Verifico se posso accettare le posizioni
        if count==0:
            posizioni[0]=new_pos
            count+=1
        
        else: 
            diff=posizioni[:count]-new_pos              # Vettore 
            dist_sq=np.sum(diff**2, axis=1)             # Scrivo l'asse poichè voglio sommare sulle righe

            if np.all(dist_sq>dist_minima):
                posizioni[count]=new_pos
                count+=1

            troppi+=1
             # Dato che è randomico potrei a un certo punto finire lo spazio e non riuscire più a mettere gli atomi mantenendo le distanze minime
            if troppi>1000*n_tot:
                print(f'Troppi atomi non c\'è spazio, sono arrivato a {count}')
                raise SystemExit

            

    # Genero le velocita
    velocita=((np.random.rand(n_tot, 2))-0.5)*params['vel_max']               # Genera per ogni atomo una velocità x e y con valori tra -0.5 e 0.5 più il valore dal file 




    return posizioni, velocita, tipi







def update_plot(grafico, scatt_object, pos, tipo):

    for t, scatt in enumerate(scatt_object):
        mask=(t==tipo)
        scatt.set_offsets(pos[mask])


    plt.draw()
    plt.pause(0.001)

    return









def main():
   
    # Trova il file e leggwe quello corretto
    percorso=os.path.dirname(os.path.abspath(__file__))
    nome_completo=os.path.join(percorso, 'Config.ini')

    # Routine cotnrollo errore
    try:
        # Passo alla funzuione dizionario i parametri
        params=load_config(nome_completo)
        print(params)

    # Gestione errore con motivo errore
    except Exception as errore:
        print(errore)
        exit()          # Istruzione operative system
   


    pos, vel, tipo=inizializzazione(params)


    # Inizializzazione grafica
    figura, grafico=setup_graphics(params)


    # Creazione oggetti chd si muovono atomi 1 e 2 srappresentati dai colori diversi
    scatt_object=[]

    for t in range(2):               # 2 perche sono i 2 possibili atomi
        mask=(t==tipo)               # Fa confronto t e tipo e quindi sarà solo True e False e avremo un array di solo vero e falso 

        # Se mask è vero prende le coordinate
        scatt=grafico.scatter(pos[mask][0], pos[mask][1], c=params['colors'][t], edgecolors='black', linewidths=1, label=f'Type {t}')          
        
        scatt_object.append(scatt)


        grafico.legend(loc='upper right')


        # Aggiornamento del grafico
        update_plot(grafico, scatt_object, pos, tipo)


    
    



if __name__ == '__main__':
    main()
    plt.show()
