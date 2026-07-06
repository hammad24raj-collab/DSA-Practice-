nums = [1,2,3,4]
ans = [1]*len(nums)
l = 1
r = 1

for i in range(len(nums)-1):
    ans[i+1] = l*nums[i] 
    l = ans[i+1]
for j in range(len(nums)-1,-1,-1):  
    ans[j]*=r
    r*=nums[j]
    
print(ans)