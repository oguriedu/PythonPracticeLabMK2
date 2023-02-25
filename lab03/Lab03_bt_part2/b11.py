n=int(input('cạnh tam giác :'))
print(" tam giac deu:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()
print("tam giác đều rỗng :")
for z in range(1, n+1):
    for m in range(1,n+1-z):
        print(" ", end = " ")
    for x in range(1,z+1):
         print("*",end=" ")
    print()
        
        
    