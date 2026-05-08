# Metodo di inserimento valore
N=int(input("Numero da testare= "))
primo= True

# Creo ciclo
for i in range(2,N):
    divisione=int(N/i)
    resto=divisione*i
    if resto==N:
        primo=False

print(primo)
