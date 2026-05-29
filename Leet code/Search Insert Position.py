def searchInsert(nums, target):
    sinistra = 0
    destra = len(nums) - 1

    while destra>=sinistra:
        medio=(destra+sinistra)//2
        if nums[medio]<target:
            sinistra= medio + 1

        elif nums[medio]>target:
            destra= medio - 1
            
           
        else:
            return medio
    
    return sinistra

#Input: 
nums = [1,3,5,6]
target = 5

#Output: 2

p=searchInsert(nums, target)

print(p)
