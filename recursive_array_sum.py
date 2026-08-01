def fun(arr,n):
    if n == len(arr):
        return 0
        
    x = fun(arr,n+1)
    
    
    return x + arr[n]
    

arr = [2, 4, 6, 8]     
         
print(fun(arr,0))