#porta al disegno di un quadrato di lato N inserito nell'input 

#obiettivo 1 scrivere un programma solido (che faccia quindi le cose giuste, ogni volta)

#tempo di esecuzione
import time
start_time = time.process_time()


#definisco la funzione che disegna 
def disegna(lato, diz):
    n_lato=abs(int(lato))

    if n_lato%2==0:
        print('il lato del quadrato dovrebbe essere dispari')
        return
    
    if n_lato<=3:
       print('il lato del quadrato deve essere pù lungo di 3')
       return
    
    n=(n_lato-3)//2
    stringa1=stringa(n_lato, diz['spigolo'], diz['orizzontale'])
    stringa2=stringa(n_lato, diz['verticale'], diz['spazio'])


    print(stringa1)

    for i in range(0,n):
     print(stringa2)

    print(stringa1)

    for i in range(0,n):
     print(stringa2)

    print(stringa1)




def stringa(n_lato, diz1, diz2):
    stringa=diz1
    n=(n_lato-3)//2              #

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+= diz2

    stringa+= diz1

    for i in range(0,n):         #ciclo che si occupo di costruire la stringa iniziale con i -
      stringa+= diz2


    stringa+= diz1

    return stringa



#costruisco la funzione MAIN che costruisce la stringaa
def main():
    lato = input('Lunghezza lato quadrato: \n')
    diz={'spigolo':' ', 'orizzontale':' ', 'verticale':' ', 'spazio':' '}

    for chiave in diz:
       diz[chiave]=input('Carattere per '+chiave+': \n') 

    disegna(lato, diz)
    return


#poi posso richiamare la funzione main per eseguirla
main()



end_time = time.process_time()
process_time = end_time - start_time

print('Tempo esecuzione \n', process_time, 'secondi')
