nums=[1,1,2]
n=len(nums)

for i in range(n-1):
    for j in range(i+1, n):
        if nums[i]==nums[j]:
            nums[j]=''
print(nums)