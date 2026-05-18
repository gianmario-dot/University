
nums=[6,4,8,7,9,10,2,3]
target=5
length=len(nums)
for i in range(length-1):
    for j in range(i+1,length):
        if target<nums[i]+nums[j] and j<length-1 and nums[j+1]>nums[j]:
            continue
        elif target==nums[i]+nums[j]:
            print([i, j])
        
