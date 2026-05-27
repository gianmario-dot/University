a='11'
b='1'


i=0

minimo=min(a,b, key=len)
massimo=max(a,b, key=len)


res=massimo

for i in range(len(minimo)):
    if a[-1-i]==b[-1-i]=='1':
        res[-1-i]=0
        res[-2-i]=1

print(res)