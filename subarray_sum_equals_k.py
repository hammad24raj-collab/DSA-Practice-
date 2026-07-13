nums = [1,2,3]
k = 3
prefix_sum = 0
dict = {0:1}
count = 0
for j in range(len(nums)):
    prefix_sum += nums[j]
    cur_val = prefix_sum - k
    if cur_val in dict:
        count += dict[cur_val] 
    if prefix_sum not in dict:
         dict[prefix_sum] = 1
    else:
        dict[prefix_sum] += 1
    
print(count)
         