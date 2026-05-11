#calcolare un integrale di un ipersuperficie

import numpy as np

a=1
n_rnd=1000                    #numero di tentativi random
d_max=100
errore=[]


for n in range(1, d_max+1):
    integ_vero=2*a**3/3*(2*a)**(n-1)*n
    MC=0
    for i in range(n_rnd):
        x=np.random.uniform(-a, a, n)           #calcolo il valore della dimensione con metodo montecarlo
        MC_1=x@x                                #numpy sa fare i prodotti vettoriali
        MC+=MC_1                                #calcolo il valore di ogni punto 
    
    iperV=(2*a)**n/n_rnd      #calcolo la base del ipercubo
    integ_MC=MC*iperV
    errore.append(abs(integ_vero-integ_MC)/integ_vero)
    print(f'Ciclo = {n:0d}, Errore = {errore[n-1]:7.5%}')


