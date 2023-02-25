n = 6
 
print("Ve tam giac sao deu:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()