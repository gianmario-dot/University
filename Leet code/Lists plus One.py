#digits=[9]

digits = [9, 9, 9]

   
digits[-1]+=1

for i in range(len(digits)):
    
    if digits[-1-i]==10:
        try: 
            digits[-1-i]=0
            digits[-2-i]+=1

        except:
            digits[-1-i]=0
            digits.insert(0,1)
                

print(digits)


    
