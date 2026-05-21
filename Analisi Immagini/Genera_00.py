import numpy as np
import matplotlib.pyplot as plt
import configparser
import os

def chiudi_tutto(event):
    print("Closing the simulation")
    raise SystemExit

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    params = {
        'width': config.getint('SPAZIO', 'width'),
        'height': config.getint('SPAZIO', 'height'),
        'n_a': config.getint('AREE', 'n_aree'),
        'd_min': config.getfloat('AREE', 'd_min'),
        'd_max': config.getfloat('AREE', 'd_max'),
        'h_min': config.getfloat('AREE', 'h_min'),
        'saturazione': config.getfloat('GAUSSIANA', 'saturazione'),
        'esponente': config.getfloat('GAUSSIANA', 'esponente'),
        'nome_file': config.get('FILE', 'nome_file')
    }
    return params

def setup_grafico(params):
    width_px = params['width']
    height_px = params['height']
    dpi = 100
    figura, grafico = plt.subplots(figsize=(width_px / dpi/3, height_px / dpi/3), dpi=dpi, num='By Gianmario Pelanda')
    figura.canvas.mpl_connect('close_event', chiudi_tutto)
    grafico.set_xlim(0,width_px)
    grafico.set_ylim(0,height_px)
    grafico.set_aspect('equal') 
    return figura, grafico

def genera_funzione(params):
    n=params['n_a']
    x_max=params['width']+1
    y_max=params['height']+1

    w_max=params['d_max']
    w_min=params['d_min']
    h_min=params['h_min']
    p=params['esponente']

    x,y= np.meshgrid(np.arange(x_max), np.arange(y_max))
    z=np.zeros_like(x)

    for _ in range(n): 
        x0=np.random.uniform(0, x_max)
        y0=np.random.uniform(0, y_max)
        wy=np.random.uniform(w_min, w_max)
        wx=np.random.uniform(w_min, w_max)
        z0=np.random.uniform(h_min, 1)
        distanza_ellittica = np.sqrt(((x-x0)/wx)**2 + ((y-y0)/wy)**2)
        zi=np.exp(-distanza_ellittica**p)*z0
        z=z+zi
    z=np.minimum(z,params['saturazione'])
    z=z/np.max(z)*255+0.5
    z=z.astype(int)
    return z

def main():
    percorso=os.path.dirname(os.path.abspath(__file__))
    nome_completo=os.path.join(percorso,'Config_genera.ini')
    try:
        params=load_config(nome_completo)
        print(f"Configurazione caricata.")
        print(params)
    except Exception as errore:
        print(errore)
        exit()

    figura, grafico =setup_grafico(params)
    z=genera_funzione(params)
    immagine=grafico.imshow(z,cmap='gray',vmin=-1,vmax=255) 
    grafico.axis('off')
    grafico.figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
    
    percorso=os.path.dirname(os.path.abspath(__file__))
    nome_completo=os.path.join(percorso,params['nome_file'])
    plt.savefig(nome_completo, dpi=300, bbox_inches='tight', pad_inches=0)

    plt.show()

if __name__ == '__main__':
    main()

