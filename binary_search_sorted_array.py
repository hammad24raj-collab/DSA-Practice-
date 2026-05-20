arr = [12, 5, 19, 3, 8, 15, 1, 10]

hlpr = sorted(arr)
print(hlpr)
target = 3
left = 0
right = len(hlpr)-1

while left <= right:
    mid = left + (right - left)//2
    if target == hlpr[mid]:
       print("Found", target)
       break 
    elif target < hlpr[mid]:
       right = mid - 1
       
    elif target > hlpr[mid]:
       left = mid + 1  
    
else:
    print("Not Found")
      
    
    