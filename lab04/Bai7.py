def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // euclid(a, b)

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print("Bội chung nhỏ nhất của", a, "và", b, "là:", lcm(a, b))
