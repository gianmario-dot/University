# Metodo di inserimento valore

N=int(input("Numero da testare= "))
n=2


# Creazione variabile

primi=[]


#divisione per numeri primi

for i in range(2,N+1):
    if n%i!=0:
        primi.append(n)
    else: 
        n=n+1   
print(primi)       



