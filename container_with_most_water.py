height = [1,8,6,2,5,4,8,3,7]
n = len(height)
width = 0
area = 0
max_area = 0
h1 = 0
h2 = n - 1
while h1 < h2:
     width =  h2 - h1 
     area = width * min(height[h1], height[h2] )
     max_area = max(max_area,area) 
         
     if height[h1] < height[h2]:
        h1 += 1
     else:
        h2 -= 1   
        
print(max_area)