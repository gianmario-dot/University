import time
start_time = time.process_time()



#definisco la funzione che disegna 
def disegna_ds(lato):
    n_lato=abs(int(lato))

    
    if n_lato<=3:
       print('il lato del quadrato deve essere pù lungo di 3')
       return
    
    n=(n_lato-2)//2
    print(ds_prima_stringa(n_lato))

    for i in range(0,n-1):
     print(ds_seconda_stringa(n_lato))

    print(ds_terza_stringa(n_lato))

    for i in range(0,n):
     print(ds_seconda_stringa(n_lato))

    print(ds_prima_stringa(n_lato))



def ds_prima_stringa(n_lato):
    stringa='+ '
    n=(n_lato-2)             #

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='-- '

    stringa+='+'

    return stringa




def ds_seconda_stringa(n_lato):
    stringa='|'
    n_lungo=int(((2*n_lato)+(n_lato-3))/2)-1       

    for i in range(0,n_lungo):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+=' '

    stringa+='|'

    for i in range(0,n_lungo):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+=' '


    stringa+='|'

    return stringa



def ds_terza_stringa(n_lato):
    stringa='|'
    n_lungo=int(((2*n_lato)+(n_lato-3))/2)-1       

    for i in range(0,n_lungo):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='_'

    stringa+='|'

    for i in range(0,n_lungo):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='_'


    stringa+='|'

    return stringa

def disegna(lato):
    n_lato=abs(int(lato))

  
    
    if n_lato<=3:
       print('il lato del quadrato deve essere pù lungo di 3')
       return
    
    n=(n_lato-3)//2
    print(prima_stringa(n_lato))

    for i in range(0,n):
     print(seconda_stringa(n_lato))

    print(prima_stringa(n_lato))

    for i in range(0,n):
     print(seconda_stringa(n_lato))

    print(prima_stringa(n_lato))


def prima_stringa(n_lato):
    stringa='+ '
    n=(n_lato-3)//2              #

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='- '

    stringa+='+ '

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='- '


    stringa+='+ '

    return stringa




def seconda_stringa(n_lato):
    stringa='| '
    n=(n_lato-3)//2              #

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='  '

    stringa+='| '

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+='  '


    stringa+='|'

    return stringa



#costruisco la funzione MAIN che costruisce la stringaa
def main():
    # 1. Prendo l'input e lo trasformo SUBITO in numero intero
    lato = int(input('Lunghezza lato quadrato: \n'))
    
    # 2. Indentazione corretta (4 spazi)
    if lato % 2 == 0:
        # Se è PARI, chiamo la nuova funzione
        disegna_ds(lato)
    else:
        # Altrimenti (è DISPARI), chiamo la funzione vecchia
        disegna(lato)


#poi posso richiamare la funzione main per eseguirla
main()



end_time = time.process_time()
process_time = end_time - start_time

print('Tempo esecuzione \n', process_time, 'secondi')