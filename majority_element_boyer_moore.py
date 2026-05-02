arr = [3, 3, 4, 2, 3, 3, 5]
n = len(arr)
appear = n/2
freq = 0
ans = 0
for i in range(n):
    if freq == 0:
        ans = arr[i]
    if ans == arr[i]:
        freq += 1
    else:
        ans != arr[i]   
        freq -= 1
print(ans)          
            
        
    