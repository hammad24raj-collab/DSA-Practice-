nums = [1,3,2,6,-1,4,1,8,2]
n = len(nums)
k = 5
window = sum(nums[:k])
avr = window/k
avrg = []
avrg.append(avr)
for r in range(k,n):
    window = window - nums[r-k] + nums[r]
    avr = window/k  
    avrg.append(avr) 
print(avrg)

    