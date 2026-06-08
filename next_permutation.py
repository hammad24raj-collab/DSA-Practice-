nums = [1,2,3]
pivot = -1
for i in range(len(nums)-2,-1,-1):
    
    if nums[i] < nums[i+1]:
        pivot = i
        break
if pivot == -1:
    nums.reverse()
else:    
    for j in range(len(nums)-1,pivot,-1):   
       if nums[j] > nums[pivot]:
          nums[j],nums[pivot] = nums[pivot],nums[j]
          break
    nums[pivot + 1: ] = list(reversed(nums[pivot+1:]))  
print(nums)
