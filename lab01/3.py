pi=3.14
r = float(input("Nhập bán kính của hình trụ: "))
h = float(input("Nhập chiều cao của hình trụ: "))

S_xq = 2 * pi * r * h
S_tp = 2 * pi * r**2 + S_xq
V = (pi * r**2 * h) / 3

print(f"Diện tích xung quanh của hình trụ là: {S_xq:.2f}")
print(f"Diện tích toàn phần của hình trụ là: {S_tp:.2f}")
print(f"Thể tích của hình trụ là: {V:.2f}")
