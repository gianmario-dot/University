#Input: 
nums = [1,2,3,1]

#Output: 2

for i in range(1,len(nums)):
        try:
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                print(i)
                
        except: print(len(nums)-1)

print(0)