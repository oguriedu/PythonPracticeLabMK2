import math

x = float(input("Nhap x: "))
n = 100
result = 1
while n > 1:
    result = result - (x**(10**-4))/(n*(n - 1))
    n = n - 1

print(result)
