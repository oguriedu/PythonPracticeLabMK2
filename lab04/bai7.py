def gcd(a, a1):
    if a1 == 0:
        return a
    else:
        return gcd(a1, a % a1)
def lcm(a, a1):
    return (a * a1) // gcd(a, a1)

a = int(input("Nhập số nguyên thứ nhất: "))
a1 = int(input("Nhập số nguyên thứ hai: "))
print("Bội chung nhỏ nhất của", a, "và", a1, "là:", lcm(a, a1))
print("Ước chung lớn nhất của", a, "và", a1, "là:", gcd(a, a1))