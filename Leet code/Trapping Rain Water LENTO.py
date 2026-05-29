# Puoi testare entrambi gli array
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,3]

area = 0
i = 0

# Fino a quando non arriviamo alla penultima colonna
while i < len(height) - 1:
    
    # 1. CERCHIAMO IL MURO DESTRO (j)
    j = i + 1
    muro_trovato = False
    
    # Mandiamo avanti un esploratore per cercare un muro >= height[i]
    j_esploratore = i + 1
    while j_esploratore < len(height):
        if height[j_esploratore] >= height[i]:
            j = j_esploratore
            muro_trovato = True
            break
        j_esploratore += 1
        
    # 2. SE NON C'È UN MURO PIÙ ALTO, PRENDIAMO IL MASSIMO RIMANENTE
    # Questo risolve il problema dell'array [4, 2, 3]
    if not muro_trovato:
        max_rimanente = -1
        j_esploratore = i + 1
        while j_esploratore < len(height):
            if max_rimanente == -1 or height[j_esploratore] > height[max_rimanente]:
                max_rimanente = j_esploratore
            j_esploratore += 1
        j = max_rimanente

    # 3. LA TUA LOGICA ORIGINALE DI CALCOLO
    index = []
    sottraz = 0
    
    # Raccogliamo gli indici dei blocchi intermedi (come facevi tu)
    n = i + 1
    while n < j:
        index.append(n)
        n += 1
        
    # Sommiamo il "cemento" da sottrarre
    for n in index:
        sottraz += height[n]
        
    # L'altezza della pozzanghera è dettata dal più basso tra il muro i e il muro j
    altezza_acqua = min(height[i], height[j])
    
    # La tua formula originale! (altezza * base) - sottraz
    area += (altezza_acqua * (j - i - 1)) - sottraz
    
    # Aggiorniamo i per ripartire dal muro j
    i = j

print(area)