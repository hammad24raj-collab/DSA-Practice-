intervals = [[1, 3],
             [2, 6],
             [8, 10],
             [15,18]]
intervals.sort()
result = []

for i in range(len(intervals)):
    
    # agar result empty hai ya overlap nahi hai
    if not result or result[-1][1] < intervals[i][0]:
        result.append(intervals[i])
        
    else:
        # overlap hai → merge karo
        result[-1][1] = max(result[-1][1], intervals[i][1])

print(result)