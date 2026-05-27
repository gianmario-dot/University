#Input: 
nums = [4,1,2,2,2]

#Output: 4

i=0
contatore=1
num=[]
n=len(nums)

for i in range(n):
    for j in range(n):
        if nums[i]==nums[j] and j!=i:
            contatore+=1
        

    if contatore==2:
        contatore=1
    else:
        num.append(nums[i])



   
print(num[0])