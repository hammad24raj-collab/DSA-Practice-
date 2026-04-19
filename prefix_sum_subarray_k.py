arr = [4, 2, 2,  7,  8,  1,  2,  8,  1,  0]
k = 8
n = len(arr)
hmap = {0:-1} 
max_len = 0
prfx = 0
for r in range(n):
    prfx += arr[r]
    if prfx not in hmap:
        hmap[prfx] = r 
    target = prfx - k 
    if target in hmap: 
        max_len = max(r - hmap[target],max_len)
    
print(max_len)