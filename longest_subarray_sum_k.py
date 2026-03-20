nums = [1,2,1,0,1,1,0]
n = len(nums)
k = 4
lft = 0
length = 0
max_len = 0
sums = 0
for r in range(n):
    sums += nums[r]
    while sums > k:
        sums -= nums[lft]
        lft += 1
    length = r - lft + 1  
    if length > max_len:
        max_len = length 
print(max_len)