# gcd : hàm để tính ước chung lớn nhất
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# lcm : hàm để tính bội chung nhỏ nhất
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Nhập vào hai số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Tìm bội chung nhỏ nhất, ước chung lớn nhất và in kết quả
print("Bội chung nhỏ nhất của", a, "và", b, "là:", lcm(a, b))
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd(a, b))
