nums = [1,3,5,6]
target = 7

left = 0
right = len(nums)-1


while right >= left:
    mid = left + (right - left)//2
    
    if target == nums[mid]:
        print(mid)
        break 
        
    elif target < nums[mid]:
        right = mid - 1 
        
    elif target > nums[mid]:
        left = mid + 1
        
else:
    print(left)  