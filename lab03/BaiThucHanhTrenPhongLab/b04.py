n = int(input("Nhap n: "))
if (n < 2):
    print("Yeu cau nhap n lon hon 1")
else:
    print("Cac so nguyen to nho hon hoac bang n: ")
    for i in range(n, 1, -1):
        for j in range(2, i, 1):
            if(i % j == 0):
                break
        else:
            print(i)
