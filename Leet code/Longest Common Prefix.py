strs =["flower","flow","flight"]

parola_chiave = strs[0]
prefix = ""        
for i in range(len(parola_chiave)):
    lettera_corrente = parola_chiave[i]
    for parola in strs:
        if i == len(parola) or parola[i] != lettera_corrente:
            print(prefix)
    prefix += lettera_corrente

