n = int(input("Nhập số nguyên dương n: "))

binary_str = ""
while n > 0:
    remainder = n % 2
    binary_str = str(remainder) + binary_str
    n = n // 2
print(f"Số {n} chuyển sang nhị phân là: {binary_str}")
