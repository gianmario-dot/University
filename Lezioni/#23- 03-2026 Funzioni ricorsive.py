#Funzioni ricorsive ovvero delle funzioni che richiamano se stesse
#usiamo come esempio i fattoriali

#n!=n(n-1)!
#scrittura ricorsiva

n=int(input('numero da fattoriale ='))
n=abs(n)

def fattoriale(n):
    if n==0:
        return 1
    
    return n*fattoriale(n-1)
    

print('n!=', fattoriale(n))