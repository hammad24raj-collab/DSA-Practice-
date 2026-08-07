def fun(s):
    if s == "":
        return ""
    
    x = fun(s[1:])  
    return x + s[0]
 
 
s = "python"    
print(fun(s))    