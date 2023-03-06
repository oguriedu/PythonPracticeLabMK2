n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

# Tính tổng S4
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1

# Tính tổng S5
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2

# Tính tổng S6
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2

print("Tổng S4 =", S4)
print("Tổng S5 =", S5)
print("Tổng S6 =", S6)