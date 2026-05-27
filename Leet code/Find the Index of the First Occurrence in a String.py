n='leeto'
h='leetcode'
i=0
j=0
s=''
while i<len(n):
    if n[i]==h[j]:
        s=s+h[j]
        j+=1
        i+=1
    else: j+=1
if s==n:
    print(i-len(n))
else: print(-1)

