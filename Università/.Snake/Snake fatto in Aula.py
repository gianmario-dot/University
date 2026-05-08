# Creo una matrice dove avrò tutti i bordi o cose che uccidono sè stesso) di valore 2 poi il cibo valore 1
# Fornisco numero quadratini

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat

plt.rcParams['keymap.save'].remove('s')


def chiudi_tutto(evento):
    raise SystemExit



def on_key(evento):

    global dx, dy

    if evento.key=='w':
        dx, dy=0,1
    if evento.key=='s':
        dx, dy=0,-1
    if evento.key=='a':
        dx, dy=-1,0
    if evento.key=='d':
        dx, dy=1,0



    return


def genera_cibo(nx, ny, lq, campo):
    while True:
        cx,cy=np.random.randint(1, nx-1), np.random.randint(1, ny-1)

        if campo[cx, cy]==0:
            campo[cx, cy]=1
            cibo=pat.Circle((cx*lq, cy*lq), lq/2, **stile_cibo)
            campo_gioco.add_patch(cibo)

            return cibo


stile_bordo={'edgecolor':'white', 'facecolor':'blue', 'linewidth':2}
stile_sepente={'edgecolor':'darkgreen', 'facecolor':'lightgreen', 'linewidth':2}
stile_cibo={'edgecolor':'darkred', 'facecolor':'red', 'linewidth':2}


# dettagli generali
nx, ny= 30, 20
lq= 30                      #lato quadratino
fx, fy=nx*30, ny*30
punteggio_totale=0
velocita=0
ritardo=0.5




campo=np.zeros((nx, ny), dtype=np.int32)








fig, campo_gioco=plt.subplots(figsize=(9,6), num='By GP')
fig.canvas.mpl_connect('close_event', chiudi_tutto)
fig.canvas.mpl_connect('key_press_event', on_key)
campo_gioco.set_xlim(0,nx*lq)
campo_gioco.set_ylim(0,ny*lq)
#campo_gioco.set_frame_on(False)
campo_gioco.set_xticks([])
campo_gioco.set_yticks([])
campo_gioco.set_title(f'Score ={punteggio_totale:06d} ---- Speed = {velocita:06d}')




# Limiti di campo di gioco
campo[:, 0]=2
campo[:, ny-1]=2
campo[0, :]=2
campo[nx-1, :]=2

for x in range(0, fx, lq):
    bordo=pat.Rectangle((x, 0), lq, lq, **stile_bordo)
    campo_gioco.add_patch(bordo)

    bordo=pat.Rectangle((x, fy-lq), lq, lq, **stile_bordo)
    campo_gioco.add_patch(bordo)


for y in range(0, fy, lq):
    bordo=pat.Rectangle((0, y), lq, lq, **stile_bordo)
    campo_gioco.add_patch(bordo)

    bordo=pat.Rectangle((fx-lq, y), lq, lq, **stile_bordo)
    campo_gioco.add_patch(bordo)






# Costruisco seprente
serpente=[(3, int(ny/2)),(4, int(ny/2)),(5, int(ny/2)), (6, int(ny/2))]
testa_x, testa_y=serpente[3]

pos_coda=[]

for i in range(0, 4):
    pos_coda.append(pat.Rectangle((serpente[i][0]*lq, serpente[i][1]*lq), lq, lq, **stile_sepente))
    campo_gioco.add_patch(pos_coda[i])


# Cibo
cibo=genera_cibo(nx, ny, lq, campo)





# Gioco
dx, dy=1, 0         #parte verso destra



while True:
    testa_x+=dx
    testa_y+=dy
    mangiato=False


    serpente.append((testa_x, testa_y))
    pos_coda.append(pat.Rectangle((serpente[-1][0]*lq, serpente[-1][1]*lq), lq, lq, **stile_sepente))
    campo_gioco.add_patch(pos_coda[-1])


    if mangiato==False:
        campo[serpente[0]]=0                #mi toglie il 2 dalla vecchia posizione
        
        pos_coda[0].remove()

        del pos_coda[0]
        del serpente[0]







    plt.pause(ritardo)




plt.show()