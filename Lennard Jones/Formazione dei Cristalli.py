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




def main():
   
    # Trova il file e leggwe quello corretto
    percorso=os.path.dirname(os.path.abspath('__file__'))
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
   








if __name__ == '__main__':
    main()