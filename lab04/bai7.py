# Nhập vào hai số nguyên dương
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a > b:
    bscnn = a
else:
    bscnn = b
while True:
    if bscnn % a == 0 and bscnn % b == 0:
        break
    bscnn += 1
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn)