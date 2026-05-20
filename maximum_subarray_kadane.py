nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
cur_sum = nums[0]
max_sum = nums[0]

for i in range(1,n):
    cur_sum = max(cur_sum + nums[i],nums[i])
    max_sum = max(max_sum,cur_sum)
         
print(max_sum)        
        
        
      