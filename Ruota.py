import numpy as np
import matplotlib.pyplot as plt
import random
import math



def chiudi_tutto(evento):
    raise SystemExit






def nomi(num, names):

    for i in range(num):
        name=input(f'insert {i+1} = \n')
        names.append(name)

    return names






def perpara_cerchio(names, pos):
    angolo_spicchio=360/len(names)  

    posizione_nome=angolo_spicchio/2

    for i in range(len(names)):
        dati=int(posizione_nome+(i)*angolo_spicchio)
        pos.append(dati)

    return pos, angolo_spicchio





def posziono_nomi(angolo, names, grafico, pos):
        
        raggio_numeri = 0.6
    
        for n in range(len(names)):
            
    
            # Python vuole i radianti, non i gradi! Li convertiamo:
            angolo_rad = math.radians(pos[n])
    
         # 3. ASSEGNO LE COORDINATE X e Y
            x = raggio_numeri * math.cos(angolo_rad)
            y = raggio_numeri * math.sin(angolo_rad)

            grafico.text(x, y, str(names[n]), fontsize=8, ha='center', va='center', color='black')

        return grafico





def divisione_cerchio(names, angolo, grafico):
    for i in range(len(names)):
        linee = plt.Rectangle((0, 0), 0.9, 0.0005, fill=True, color='black')
        linee.set_angle(angolo*i)
        grafico.add_patch(linee)

    return grafico
    





def animazione(linea, grafico, angoli, names):
    
    angolo_corrente = 0                   
    velocita = random.uniform(20, 40)     
    attrito = 0.98                        

    
    while velocita > 0.1:                 


        angolo_corrente = angolo_corrente + velocita
        linea.set_angle(angolo_corrente)
        
        
        velocita = velocita * attrito 

        plt.pause(0.01) 
        
    
    
    
    angolo_fin=angolo_corrente    
        

    
    print("La ruota si è fermata!")
    
    return grafico, linea, angolo_fin







def festa(names, angolo_fin, grafico, angolo_spicchio):
    angolo_rimanente=int(angolo_fin%360)
    num_vincitore=int(angolo_rimanente/angolo_spicchio)

    vincitore=names[num_vincitore]

    grafico.text(0, 0, str(vincitore), fontsize=40, ha='center', va='center', color='black')

    return grafico





def main():
    posizioni=[]
    names=[]
    angoli=[]

    insert_number=int(input('Quanti sono gli elementi? \n'))

    names=nomi(insert_number, names)

    posizioni, angolo=perpara_cerchio(names, posizioni)

    print(names)
    print(posizioni)





    figura, grafico = plt.subplots(figsize=(12,6), num='By Gianmario Pelanda')
    grafico.set_xlim(-1, 1)
    grafico.set_ylim(-1, 1)
    grafico.set_aspect('equal')

    grafico=posziono_nomi(angolo, names, grafico, posizioni)
    linee=divisione_cerchio(names, angolo, grafico)
    C = plt.Circle((0, 0), 0.9, fill=False, edgecolor='black', linewidth=2)
    linea = plt.Rectangle((0, 0), 0.7, 0.005, fill=True, color='black')
    


    grafico.add_patch(linea)
    grafico.add_patch(C)
    
    
    grafico, linea, angolo_fin=animazione(linea, grafico, angolo, names)

    vincitore=festa(names, angolo_fin, grafico, angolo)

    plt.pause(0.1)

   
    

main()
plt.show()