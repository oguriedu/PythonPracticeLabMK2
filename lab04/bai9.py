a = int(input("Nhập một số nguyên dương: "))
a1 = 0

while a > 0:
    a2 = a % 10
    a1 += a2
    a //= 10

print("Tổng các chữ số của số vừa nhập là:", a1)