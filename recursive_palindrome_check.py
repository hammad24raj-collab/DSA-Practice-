def fun(s,i,j):  
    if i > j:
        return True
    
    x = fun(s,i + 1,j - 1)
    if s[i] == s[j] and x:
        return True
    else:
         return False     
    
    
    
s = "abca"  
print(fun(s,0,len(s)-1))    