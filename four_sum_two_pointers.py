nums = [2,2,2,2,2]
target = 8
nums = sorted(nums)
pair = 0
s = set()
for i in range(len(nums)-3):
    for j in range(i+1,len(nums)-2):
        left = j + 1
        right = len(nums)-1
        while left < right:
             total = nums[i]+nums[j]+nums[left]+nums[right]
             if total == target:
                pair = nums[i],nums[j],nums[left],nums[right]
                left += 1
                right -= 1
                s.add(pair)
             elif total > target:  
                  right -= 1 
             else:
                  left += 1  
lists = [list(x) for x in s]                  
       
print(lists)