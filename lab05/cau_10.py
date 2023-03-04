n = str(input("Nhap chuoi nhi phan:"))
kq = 0
m = len(n) - 1
for i in n:
    if int(i) == 1:
        kq += 2 ** m
    if int(i) != 1 or int(i) != 0:
        print("Ban nhap sai chuoi")
    m -= 1
print(kq)