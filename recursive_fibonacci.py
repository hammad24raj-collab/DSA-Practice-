n = 7

def fun(n):
    if n == 0:
        return 0
        
    if n == 1:
        return 1
    
    x = fun(n-1)
    y = fun(n-2)
    
    return x + y
    
print(fun(n))