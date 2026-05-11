
#classe oggwetti e assegnazione parametri 
class palla:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

   
    #creo oggetto palla, devo per forza mettere prima self e poi i parametri che voglio assegnare con nomi a piacere, in questo caso x, y, vx e vy.

    #funzione muovi prende i valori di palla e li muove spostando la palla
    #prende self.x e la muovo di velocità per tempo
    def muovi(self, dt):
     self.x+=self.vx*dt
     self.y+=self.vy*dt

pallone=palla(0, 0, 1, 2)

#mostra spostamento palla lungo un asse (es y)
pallone.muovi(1)

print()
