#porta al disegno di un quadrato di lato N inserito nell'input 

#obiettivo 1 scrivere un programma solido (che faccia quindi le cose giuste, ogni volta)

#tempo di esecuzione
import time
start_time = time.process_time()


#definisco la funzione che disegna 
def disegna(lato):
    n_lato=abs(int(lato))

    if n_lato%2==0:
        print('il lato del quadrato dovrebbe essere dispari')
        return
    
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
    lato = input('Lunghezza lato quadrato: \n')
    disegna(lato)
    return


#poi posso richiamare la funzione main per eseguirla
main()



end_time = time.process_time()
process_time = end_time - start_time

print('Tempo esecuzione \n', process_time, 'secondi')
