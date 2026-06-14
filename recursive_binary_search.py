def binarySearch(arr,tar,str,end):
    if str > end:
        return -1
    mid = str + (end - str)//2
    if arr[mid] < tar:
        return binarySearch(arr,tar,mid+1,end)
    elif arr[mid] > tar:
        return binarySearch(arr,tar,str,mid-1)
    else:
        return arr[mid]  
    return -1     
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
tar = 20
print(binarySearch(arr,tar,0,len(arr)-1)) 