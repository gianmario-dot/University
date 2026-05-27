s ="hope    day  "
i=0
let=[]
risult=0


s=s.strip()

while i<len(s):
        try:
                if s[-1-i]!=' ':
                        i+=1
                        
                else: print(i)

        except: print(len(s))

print(i)     
