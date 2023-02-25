#Tính tổng
n = int(input("Nhap so phan tu chuoi dan dau : "))
while n<0:
    n = int(input("Nhap lai :  "))
s = 0
for i in range(1, n+1):
    if (i%2) != 0:
        s += (1/i)
    elif (i%2) == 0:
        s -= (1/i)
print("Tong chuoi dan dau co ", n, "phan tu la: ", s)