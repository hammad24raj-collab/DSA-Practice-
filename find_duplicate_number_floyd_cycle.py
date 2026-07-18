nums = [1,3,4,2,2]
slow = 0
fast = 0
start = 0
while True:
    slow = nums[slow]
    fast = nums[fast]
    fast = nums[fast]
    if slow == fast:
          break 
while True:
    slow = nums[slow]
    start = nums[start]
    if start == slow:
        break
print(start) 