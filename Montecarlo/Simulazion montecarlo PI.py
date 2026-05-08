#simulazioni Montecarlo, sono delle approssimazioni che fungono da soluzione a dei problemi che non si trovano calcolando

import matplotlib.pyplot as plt
import numpy as np

#impostazione grafico
ritardo=0.0001
N=int(input('Numero tentativi='))

figura, grafico = plt.subplots(num= 'By Gianmario Pelanda', figsize=(12,12))
grafico.set_xlim(-1,1)
grafico.set_ylim(-1,1)
grafico.set_aspect('equal')
cerchio=plt.Circle((0, 0), 1, color='blue', fill=False)
grafico.add_patch(cerchio)

#ETICHETTA PER VALORE DI PI
testo= grafico.text(-1, 1.1, '', fontsize=12)

inside_count=0
for i in range(N):
    x,y=np.random.uniform(-1, 1, 2)
    distance=x**2+y**2
    if distance<=1:
        inside_count+=1
        grafico.plot(x, y, 'ro', markersize=5)
    else:
        grafico.plot(x, y, 'bo', markersize=5)

    pi_greco=((inside_count)/(i+1))*4
    testo.set_text(pi_greco)

    plt.pause(ritardo)

plt.show()