n = 4
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end=" ")
    print("*",end=" ")
    if i > 1:
        for j in range(2*i-3):
            print("-",end=" ")
        print("*",end=" ")
    print()  
for i in range(n-1,0,-1):
    for j in range(i,n):
        print(" ",end=" ")
    print("*",end=" ")
    if i > 1:
        for j in range(2*i-3):
            print("-",end=" ")
        print("*",end=" ")
    print()      
       