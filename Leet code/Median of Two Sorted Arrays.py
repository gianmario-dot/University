nums1=[1,3,4]
nums2=[2,5]

n1 = len(nums1)
n2 = len(nums2)
n = n1 + n2
pd = n % 2
fine = int(n / 2) + 1

c1 = 0
c2 = 0
unita = []

for i in range(fine):
    if c1 < n1 and c2 < n2:
        if nums1[c1] < nums2[c2]:
            unita.append(nums1[c1])
            c1 += 1
        else:
            unita.append(nums2[c2])
            c2 += 1
    elif c1 == n1:
        unita.append(nums2[c2])
        c2 += 1
    elif c2 == n2:  
        unita.append(nums1[c1])
        c1 += 1


if pd == 0:
    print( (unita[-1] + unita[-2]) / 2.0 )
else: 
    print(float(unita[-1]))
