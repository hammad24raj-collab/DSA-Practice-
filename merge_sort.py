arr = [3, 13, 15, 11]


def m_sort(arr,left, right):
    if left == right:
        return 
    
    mid = left + (right - left)//2
    
    m_sort(arr,left, mid)
    m_sort(arr,mid+1,right)
    
    temp = []
    
    i = left
    j = mid + 1
    
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])   
            j += 1
            
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
               
    k = left    
    for x in temp:
        arr[k] = x
        k += 1
        
    
    
print(m_sort(arr,0,len(arr)-1)) 
print(arr)