nums = [2,0,2,1,1,0]
n = len(nums)
r = 0
m = 0
l = n - 1

while m <= l:
    if nums[m] == 2:
        nums[l],nums[m] = nums[m],nums[l]
        l -= 1
    elif nums[m] == 0:
        nums[r],nums[m] = nums[m],nums[r]
        m += 1
        r += 1 
    elif nums[m] == 1:
        m += 1   
    
print(nums)        
            
    