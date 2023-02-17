n = int(input("Nhập n = "))
i = 2
print("thừa số nguyên tố của",n,"là: ")
while n !=1:
    
    if n % i == 0:
        print(i,end = " ")
        n = n // i
    else:
        i = i + 1