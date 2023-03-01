a = 1
b = 1

while a == 1 or b == 1:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
max = a
if a < b:
    max = b

i = 2
while i <= max:
    if a % i == 0 and b % i == 0:
        print(f"Uoc chung nho nhat: {i}")
        break
    i = i + 1
else:
    print("Khong co uoc chung")
