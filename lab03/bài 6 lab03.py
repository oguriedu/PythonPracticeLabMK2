import math
n = int(input("Nhập số n: "))
sum = 0
for i in range(1, n+1):
    sum += math.pow(i, 3)
print("Tổng bậc 3 của", n, "số nguyên đầu tiên là", sum)
