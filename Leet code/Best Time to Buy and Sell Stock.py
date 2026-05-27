prices=[7,1,5,3,6,4]
prices =[7,6,4,3,1]

#Output 5
#Output 0

sordi_giadagnati = 0

prezzo_minimo = prices[0] 

for prezzo_attuale in prices:
    
    if prezzo_attuale < prezzo_minimo:
        prezzo_minimo = prezzo_attuale
        
    
    elif prezzo_attuale - prezzo_minimo > sordi_giadagnati:
        sordi_giadagnati = prezzo_attuale - prezzo_minimo

print(sordi_giadagnati)