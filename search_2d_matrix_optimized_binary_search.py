matrix = [[1, 3, 5, 7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3

row = len(matrix)
colm = len(matrix[0])
left = 0
right = row * colm - 1
while left <= right:
    mid = left + (right - left)//2
    r = mid //colm
    c = mid % colm
    if target == matrix[r][c]:
        print("True")
        break
    elif target < matrix[r][c]:
        right = mid - 1
    elif target > matrix[r][c]: 
        left = mid + 1
else:        
    print("not found")