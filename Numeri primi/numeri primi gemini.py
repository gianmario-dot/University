# 1. Chiediamo fino a che numero vogliamo arrivare
N = int(input("Fino a che numero vuoi cercare i primi? = "))

# 2. Creiamo una lista vuota per salvare i numeri primi che troveremo
primi = []

# 3. Ciclo principale: testiamo tutti i numeri 'n' partendo da 2 fino a 'N'
for n in range(2, N + 1):
    
    è_primo = True  # Partiamo dal presupposto che 'n' sia primo
    
    # 4. Ciclo secondario: proviamo a dividere 'n' per tutti i numeri prima di lui
    for i in range(2, n):
        if n % i == 0:        # Se il resto è zero, è divisibile!
            è_primo = False   # Allora NON è primo
            break             # Interrompiamo questo ciclo, inutile testare oltre
            
    # 5. Se dopo tutti i test è rimasto True, lo aggiungiamo alla lista
    if è_primo == True:
        primi.append(n)

# 6. Stampiamo il risultato finale
print(f"I numeri primi trovati sono: {primi}")