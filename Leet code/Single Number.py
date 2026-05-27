#Input: 
nums = [4,1,2,4,2]

#Output: 4

registro={}

# Creo ciclo con il registro
for i in nums:

    if i in registro:
        
        registro[i] += 1
    else:
        
        registro[i] = 1


# Controllo quale ha valore 1

for numero, contatore in registro.items():
    
    if contatore == 1:
        print(numero)



