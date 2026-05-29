s='0.1'
       
Valid=True
cifre=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if s[0] in cifre or s[0]=='-' or s[0]=='+' or s[0]=='.':
    Valid=True

if len(s)==1 and s[0] in cifre:
    print( True)

elif len(s)==1 and s[0] not in cifre: print( False)

if s[0] in cifre :
    if s[1] in cifre or s[1]=='e' or s[1]=='E' or s[1]=='.':
        Valid=True
    else: print( False)

if s[0] not in cifre and s[0]=='-' or s[0]=='+' :
    if s[1] in cifre or s[1]=='.':
        Valid=True
    else: print( False)

if s[0] not in cifre and not s[0]=='-' or not s[0]=='+' or not s[1]=='.':
    if s[1] in cifre: 
        Valid=True
    else: 
        print( False)
        
    





print(Valid)

