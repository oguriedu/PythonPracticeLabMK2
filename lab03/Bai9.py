n = 0
while n <= 0:
    n = int(input("Nhập số nguyên dương n: "))

S4 = 0
for i in range(1, n+1):
    S4 += i ** 2

S5 = 0
for i in range(1, 2*n+2, 2):
    S5 += i ** 3

S6 = 0
for i in range(2, 2*n+1, 2):
    S6 += i ** 4

print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)