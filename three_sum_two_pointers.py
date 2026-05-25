nums = [-1,0,1,2,-1,-4]
n = len(nums)           
sort = sorted(nums)
pair = 0
s = set()
for i in range(n-2):
    left = i + 1
    right = n - 1
    while left < right:
        total = sort[i]+sort[left]+sort[right]
        if total == 0:
           pair = sort[i],sort[left],sort[right]
           s.add(pair)
           left += 1
           right -= 1
        elif total > 0:
            right -= 1
        else:
            left += 1     
        
print(s)   
