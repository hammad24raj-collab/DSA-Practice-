prices = [7,1,5,3,6,4]
minp = prices[0]
max_vl = 0
for maxp in range(1,len(prices)):
    currentp = prices[maxp] - minp
    if prices[maxp] < minp:
        minp = prices[maxp]
    max_vl = max(currentp,max_vl)    
print(max_vl)