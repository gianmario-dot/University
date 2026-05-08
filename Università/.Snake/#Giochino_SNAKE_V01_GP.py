import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from matplotlib.widgets import Button, TextBox
import numpy as np

plt.rcParams['keymap.save'].remove('s')

figura, ax = plt.subplots(figsize=(10, 8), num='SNAKE v2 - By GP')
plt.subplots_adjust(right=0.7)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

punteggio = 0
nome_giocatore = "Babbo1"
classifica = []
gioco_attivo = False

testo_score = ax.text(0.05, 0.95, f'Punti: {punteggio}', transform=ax.transAxes, fontsize=14, fontweight='bold', color='darkblue')
testo_classifica = figura.text(0.75, 0.5, "CLASSIFICA:\nNessuno", fontsize=12, va='top')

ax_box = plt.axes([0.75, 0.85, 0.2, 0.05])
text_box = TextBox(ax_box, 'Nome: ', initial=nome_giocatore)

ax_button = plt.axes([0.75, 0.75, 0.2, 0.05])
btn_restart = Button(ax_button, 'Rigioca!')

serpente_coords = [[0, 0]]
corpo_grafico = []

testa_snake = Ellipse((0, 0), width=2.1, height=1.2, color='darkgreen', angle=0)
ax.add_patch(testa_snake)
corpo_grafico.append(testa_snake)

cibo_x = np.random.randint(-9, 10)
cibo_y = np.random.randint(-9, 10)
mela = Circle((cibo_x, cibo_y), 0.4, fill=True, color='red')
ax.add_patch(mela)

def salva_nome(testo):
    global nome_giocatore, gioco_attivo
    nome_giocatore = testo
    gioco_attivo = True
    text_box.set_active(False)
    figura.canvas.draw()

text_box.on_submit(salva_nome)

def mangiare(nuova_testa):
    global cibo_x, cibo_y, punteggio
    if nuova_testa[0] == cibo_x and nuova_testa[1] == cibo_y:
        punteggio += 100
        testo_score.set_text(f'Punti: {punteggio}')
        cibo_x = np.random.randint(-9, 10)
        cibo_y = np.random.randint(-9, 10)
        mela.center = (cibo_x, cibo_y)
        nuova_palla = Circle((serpente_coords[-1][0], serpente_coords[-1][1]), 0.6, color='green')
        ax.add_patch(nuova_palla)
        corpo_grafico.append(nuova_palla)
        return True
    return False

def Muovi_pallino(evento):
    global codice_tastiera
    
    if gioco_attivo == False:
        return
        
    if evento.key not in ['w', 'a', 's', 'd']:
        return

    head_object = corpo_grafico[0]
    nuova_testa = list(serpente_coords[0])

    if evento.key == 'w':
        nuova_testa[1] += 1
        head_object.set_angle(90)
    elif evento.key == 's':
        nuova_testa[1] -= 1
        head_object.set_angle(270)
    elif evento.key == 'a':
        nuova_testa[0] -= 1
        head_object.set_angle(180)
    elif evento.key == 'd':
        nuova_testa[0] += 1
        head_object.set_angle(0)

    if nuova_testa in serpente_coords or nuova_testa[0] > 10 or nuova_testa[0] < -10 or nuova_testa[1] > 10 or nuova_testa[1] < -10:
        testo_score.set_text(f'GAME OVER! Punti: {punteggio}')
        testo_score.set_color('red')
        
        classifica.append((nome_giocatore, punteggio))
        classifica.sort(key=lambda x: x[1], reverse=True)
        
        testo_top5 = "CLASSIFICA TOP 5:\n"
        for i, record in enumerate(classifica[:5]):
            testo_top5 += f"{i+1}. {record[0]} - {record[1]} pt\n"
        testo_classifica.set_text(testo_top5)
        
        figura.canvas.draw()
        figura.canvas.mpl_disconnect(codice_tastiera)
        return

    serpente_coords.insert(0, nuova_testa)
    
    if not mangiare(nuova_testa):
        serpente_coords.pop()

    for i in range(len(serpente_coords)):
        corpo_grafico[i].center = (serpente_coords[i][0], serpente_coords[i][1])

    figura.canvas.draw()

def riavvia_gioco(evento):
    global punteggio, serpente_coords, corpo_grafico, codice_tastiera, cibo_x, cibo_y, gioco_attivo
    
    gioco_attivo = False
    text_box.set_active(True)
    
    for pezzo in corpo_grafico:
        pezzo.remove()
    corpo_grafico.clear()
    
    punteggio = 0
    testo_score.set_text(f'Punti: {punteggio}')
    testo_score.set_color('darkblue')
    serpente_coords = [[0, 0]]
    
    nuova_testa = Ellipse((0, 0), width=1.5, height=0.8, color='darkgreen', angle=0)
    ax.add_patch(nuova_testa)
    corpo_grafico.append(nuova_testa)
    
    cibo_x = np.random.randint(-9, 10)
    cibo_y = np.random.randint(-9, 10)
    mela.center = (cibo_x, cibo_y)
    
    try:
        figura.canvas.mpl_disconnect(codice_tastiera)
    except:
        pass
    
    codice_tastiera = figura.canvas.mpl_connect('key_press_event', Muovi_pallino)
    figura.canvas.draw()

btn_restart.on_clicked(riavvia_gioco)
codice_tastiera = figura.canvas.mpl_connect('key_press_event', Muovi_pallino)

plt.show()