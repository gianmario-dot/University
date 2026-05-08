
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle
#from matplotlib.widgets import TextBox

plt.rcParams['keymap.save'].remove('s')



figura, grafico = plt.subplots(num='By Gianmario Pelanda')
grafico.set_xlim(-10, 10)
grafico.set_ylim(-10, 10)
grafico.set_aspect('equal')

#figura.patch.set_facecolor('black')
#grafico.axis('off')


lunghezza=2


coordinate=[0, 0, 1, 90]
raggio=0.3

cibo_x=np.random.randint(-9,9)
cibo_y=np.random.randint(-9,9)



mela = Circle((cibo_x, cibo_y), raggio, fill=True, color='red')
grafico.add_patch(mela)

snake = Ellipse((coordinate[0],coordinate[1]), width=coordinate[2], height=0.7, angle=0, fill=True, color='green', linewidth=7)
grafico.add_patch(snake)








#WASD
def Muovi_pallino(evento):
    # evento.key contiene la lettera premuta sulla tastiera (sempre in minuscolo!)
    if evento.key == 'w':
        coordinate[1]+=1
        snake.set_angle(90)

    elif evento.key== 's':
        coordinate[1]-=1
        snake.set_angle(270)

    elif evento.key== 'a':
        coordinate[0]-=1
        snake.set_angle(180)

    elif evento.key== 'd':
        coordinate[0]+=1
        snake.set_angle(0)
    
    snake.center = (coordinate[0], coordinate[1])
    
    mangiare()

    # 3. Ridisegna il grafico (allineato fuori dagli if/elif!)
    figura.canvas.draw()


def mangiare():
    global lunghezza, cibo_x, cibo_y 
    punteggio=0
    
    if coordinate[0] == cibo_x and coordinate[1] == cibo_y:
        
        punteggio+=100
        lunghezza += 1
        snake.set_width(lunghezza)
        
        # 2. Spostiamo la mela in un posto nuovo a caso!
        cibo_x = np.random.randint(-9, 10)
        cibo_y = np.random.randint(-9, 10)
        mela.center = (cibo_x, cibo_y)

        testo= grafico.text(-1, 1.1, 'Punteggio=', punteggio, fontsize=12)


codice_tastiera = figura.canvas.mpl_connect('key_press_event', Muovi_pallino)
             
     
plt.show() 