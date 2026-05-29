def firstMissingPositive(nums):
    nums.sort()
    i=1
    while len(nums):
        if i in nums:
            i+=1
        else: return i


#Input: 
nums = [11,8,7,9,12]

#Output: 1

p=firstMissingPositive(nums)

print(p)