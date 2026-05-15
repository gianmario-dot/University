nums1=[1,3,4]
nums2=[2,5]
n1=len(nums1)
n2=len(nums2)
merged=[]
for i in range(n1+n2):
    for j in range(n2):
        if nums1 and nums2 and i<n1-1 and nums1[i]<nums2[j] :
            merged.append(nums1[0])
            
        elif nums1 and nums2 and i<n1-1 and nums2[j]<nums1[i+1]:
            merged.append(nums2[0]),

        

print(merged)