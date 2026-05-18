#s="()[]{}"
s='{[()]}'
amici = {')': '(', ']': '[', '}': '{'}
B=False
boolean=[]
n=len(s)
for par in s:
    if par==amici.values():
        B=True
        boolean.append(B)


print(boolean)
        