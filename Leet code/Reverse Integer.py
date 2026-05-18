x=1234
segno=1
if x<0:
    segno=-1
    x=-x

stringa=str(x)
n=len(stringa)

new_stringa=''

for i in range(n):
    new_stringa += (stringa[n-i-1])

x=int(new_stringa)*segno

if x<-2**31 or x>2**31-1:
    print(0)
else: print(x)