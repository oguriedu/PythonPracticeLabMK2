str = str(input("nhập chuỗi nhị phân:"))
kq = 0
m = len(str) - 1
for i in str:
    if int(i) == 1:
        kq += 2 ** m
    if int(i) != 1 or int(i) != 0:
        print("chuỗi không hợp lệ!")
    m -= 1
print(kq)