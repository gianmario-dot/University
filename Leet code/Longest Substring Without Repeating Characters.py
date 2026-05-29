def lengthOfLongestSubstring(s):

    lista=[]
    j=0
    i=1
    n=len(s)
    if n>0:
        for x in s:
            lista.append(x)
    else: return 0

    while j<n:
        
        if i<n and s[i] not in lista[j]:
            lista[j]+=s[i]
            i+=1
        else:
                
                j+=1
                i=j+1

    massimo=max(lista, key=len)
    return len(massimo)


s='abcabcabc'
s='pwwekw'
p=lengthOfLongestSubstring(s)

print(p)