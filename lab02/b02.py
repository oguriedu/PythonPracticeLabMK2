import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Có hai nghiệm phân biệt: {x1} và {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Có một nghiệm kép: {x}")
else:
    print("Vô nghiệm.")
