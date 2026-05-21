import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter  # libreria per la creazione di video
import numpy as np
import configparser
import os

def chiudi_tutto(event):
    print("Closing the simulation")
    raise SystemExit

def load_config(file_path):
    config = configparser.ConfigParser()
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
        'raffreddamento': config.getfloat('SIMULAZIONE', 'raffreddamento'),
        'dist_min': config.getfloat('SIMULAZIONE', 'dist_min'),
        'vel_max': config.getfloat('SIMULAZIONE','velocita_max'),
        'fps': config.getint('SIMULAZIONE', 'fps'),
        'dpi': config.getint('SIMULAZIONE', 'dpi'),
        'step_salva': config.getint('SIMULAZIONE', 'step_salva'),
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

    # Convertiamo le matrici in array NumPy prima di restituirle (è veloce perchè i dizionario contiene 
    #  solo il puntatore alla matrice)
    params['sigmas'] = np.array([[s_aa, s_ab], 
                                 [s_ab, s_bb]])
    
    params['epsilons'] = np.array([[e_aa, e_ab], 
                                   [e_ab, e_bb]])
    
    params['masses'] = np.array([config.getfloat('ATOMO_A', 'massa'), 
                                 config.getfloat('ATOMO_B', 'massa')])

    return params

def setup_grafico(params):
    # Creiamo la figura e il grafico con le dimensioni e DPI del file ini
    figura, grafico = plt.subplots(figsize=(8, 8), dpi=params['dpi'], num='By Franco Meinardi: Lennard Jones')
    
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

def inizializza(params):
    n_a=params['n_a']
    n_b=params['n_b']
    n_tot=n_a+n_b
    posizioni=np.zeros((n_tot,2))
    tipi=np.array([0]*n_a+[1]*n_b)

    dist_minima=(params['dist_min']*np.min(params['sigmas']))**2    # cambiata un po'

    count=0
    troppi=0
    np.random.seed(params['seme'])
    while count<n_tot:
        margine=0.05
        new_pos=np.array(
            [np.random.uniform(margine*params['width'], (1-margine)*params['width']),
             np.random.uniform(margine*params['height'],(1-margine)*params['height'])])
        if count==0:
            posizioni[0]=new_pos
            count+=1
        else:
            diff=posizioni[:count]-new_pos
            dist_sq=np.sum(diff**2,axis=1)
            if np.all(dist_sq>dist_minima):
                posizioni[count]=new_pos
                count+=1
        troppi+=1
        if troppi>1000*n_tot:
            print(f'Troppi atomi. Sono arrivato a {count}')
            raise SystemExit

    velocita=(np.random.rand(n_tot,2)-0.5)*params['vel_max']
    return posizioni, velocita, tipi

def update_plot(grafico,scatt_object,pos,tipo):
    for t, scatt in enumerate(scatt_object):
        mask =(t==tipo)
        scatt.set_offsets(pos[mask])

    plt.draw()
    plt.pause(0.001)
    return

def calcola_forze(pos,tipi,params):
    n_total = len(tipi)
    forze = np.zeros_like(pos)
    
    sigmas = params['sigmas']
    epsilons = params['epsilons']
    cutoff_sq = params['cutoff']**2

    for i in range(n_total):
        dist = pos[i+1:] - pos[i]
        dist_sq = np.sum(dist**2, axis=1)

        mask = dist_sq < cutoff_sq
        if not np.any(mask):
            continue
            
        tipo_i = tipi[i]
        tipi_j = tipi[i+1:][mask]
        
        s = sigmas[tipo_i, tipi_j]
        e = epsilons[tipo_i, tipi_j]

        r = np.sqrt(dist_sq[mask])
        
        sr = s / r
        sr6 = sr**6
        sr12 = sr6**2

        f_scalar = -(24 * e * (2 * sr12 - sr6) / (r**2))[:, np.newaxis]
        
        f_vectors = f_scalar * dist[mask]
        
        forze[i] += np.sum(f_vectors, axis=0)
        forze[i+1:][mask] -= f_vectors
        
    return forze

def gestisci_rimbalzi(pos,vel,params):
    w,h=params['width'],params['height']

    mask_x_low=pos[:,0]<=0
    mask_x_high=pos[:,0]>=w
    vel[mask_x_low,0]*=-1
    vel[mask_x_high,0]*=-1
    pos[mask_x_low,0]=0.01
    pos[mask_x_high,0]=w-0.
    
    mask_y_low=pos[:,1]<=0
    mask_y_high=pos[:,1]>=h
    vel[mask_y_low,1]*=-1
    vel[mask_y_high,1]*=-1
    pos[mask_y_low,1]=0.01
    pos[mask_y_high,1]=h-0.01

    return

def main():
    percorso=os.path.dirname(os.path.abspath(__file__))
    nome_completo=os.path.join(percorso,'Config.ini')
    try:
        params=load_config(nome_completo)
        print(f"Configurazione caricata. Simulazione di {params['n_a'] + params['n_b']} particelle.")
        print(params)
    except Exception as errore:
        print(errore)
        exit()

    pos, vel, tipi=inizializza(params)
    figura, grafico=setup_grafico(params)
    scatt_object=[]
    for t in range(2):
        mask=(t==tipi)
        scatt=grafico.scatter(pos[mask,0],pos[mask,1], c=params['colors'][t],edgecolors='black', linewidths=1, label=f'Type {t}')
        scatt_object.append(scatt)

    grafico.legend(loc='upper right')
    update_plot(grafico,scatt_object,pos,tipi)
    plt.pause(3)

    nome_file_animazione=os.path.join(percorso,params['nome_file'])
    nome_file_configurazione=nome_file_animazione+'.ini'
    nome_file_animazione+='.avi'
    with open(nome_file_configurazione, 'w') as f:
        for chiave, valore in params.items():
            stringa=chiave+ '= ' + str(valore) +'\n'
            f.write(stringa)
    
    writer = FFMpegWriter(fps=params['fps'], codec='mpeg4')
    with writer.saving(figura, nome_file_animazione, params['dpi']):

        forze=calcola_forze(pos,tipi,params)

        dt=params['dt']
        m=params['masses'][tipi][:,np.newaxis]
        for i in range(params['steps']):
            acc=forze/m
            pos+=vel*dt+0.5*acc*dt**2
            vel += 0.5 * acc * dt

            gestisci_rimbalzi(pos,vel,params)  #XXXXXXXXXXXXXXXXXX Spostato
            """ vel+=acc*dt

            forze=calcola_forze(pos,tipi,params)
            nuova_acc=forze/m
            nuova_vel+=nuova_acc*dt
            vel=(vel+nuova_vel)/2
            """
            forze=calcola_forze(pos,tipi,params)
            nuova_acc=forze/m
            vel += 0.5 * nuova_acc * dt

            vel*=params['raffreddamento']

            if i % params['step_salva']==0:     # XXXXXXXX mancava ==0
                m = params['masses'][tipi][:, np.newaxis]   # XXXXX aggiunto
                ke = 0.5 * np.sum(m * vel**2)/(params['n_a'] + params['n_b'])
                update_plot(grafico,scatt_object,pos,tipi)
                grafico.set_title(f'Step = {i:04d} -- Energy = {ke:6.2e}')
                writer.grab_frame()
                plt.pause(0.001)

    plt.show()

if __name__ == '__main__':
    main()
    plt.show()
