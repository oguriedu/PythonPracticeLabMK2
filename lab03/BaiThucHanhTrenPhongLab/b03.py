n = int(input("Nhap n: "))
if (n < 2):
    print(f"{n} Khong phai la so nguyen to")
flag = True
for i in range(2, n, 1):
    if(n % i == 0):
        flag = False
        print(f"{n} Khong phai la so nguyen to")
        break
else:
    print(f"{n} La so nguyen to")

if(flag == False):
    for i in range(n-1, 1, -1):
        for j in range(2, i, 1):
            if(i % j == 0):
                break
        else:
            print(f"{i} La so nguyen to gan nhat ben trai")
            break

    for i in range(n+1, 1000, 1):
        for j in range(2, i, 1):
            if(i % j == 0):
                break
        else:
            print(f"{i} La so nguyen to gan nhat ben phai")
            break
