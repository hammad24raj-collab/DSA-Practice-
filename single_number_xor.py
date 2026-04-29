nums = [4,1,2,1,2]
ans = 0
for i in range(len(nums)):
    ans = ans ^ nums[i]
    
print(ans)   
    