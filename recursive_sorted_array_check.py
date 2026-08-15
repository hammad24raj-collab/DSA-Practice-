arr = [1, 2, 4, 3, 5]


def fun(arr,n):
    
    if n == len(arr)-1:
        return True 
        
    x = arr[n]
    y = arr[n+1]

    result =  fun(arr,n+1) 
    
    if x > y:
        return False
        
    return result
 
       
print(fun(arr,0))    