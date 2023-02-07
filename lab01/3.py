pi=3.14
r = float(input("Nhập bán kính của hình trụ: "))
h = float(input("Nhập chiều cao của hình trụ: "))

Sxq = 2 * pi * r * h
Stp = 2 * pi * r**2 + Sxq
V = (pi * r**2 * h) / 3

print(f"Diện tích xung quanh của hình trụ là: {Sxq:.2f}")
print(f"Diện tích toàn phần của hình trụ là: {Stp:.2f}")
print(f"Thể tích của hình trụ là: {V:.2f}")
