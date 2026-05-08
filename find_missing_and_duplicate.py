grid = [[1,3],
        [2,2]]
        
arr = []        
for row in grid:
    for val in row:
        arr.append(val)
        
s = set()
duplicate = -1

for val in arr:
    if val in s:
        duplicate = val
    s.add(val)
        
n = len(arr)
missing = -1

for i in range(1,n+1):
    if i not in s:
        missing = i
        
print("Missing",missing)       
print("Duplicate",duplicate)     