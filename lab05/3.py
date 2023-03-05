# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))

# Chuyển đổi n sang hệ nhị phân
binary = ""
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

# In ra kết quả là chuỗi nhị phân
print("Kết quả: ", binary)
