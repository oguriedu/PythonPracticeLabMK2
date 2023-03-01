import math


n = int(input("Nhap n: "))
if (n <= 0):
    print("Yeu cau nhap n lon hon 0")
else:
    sum_a = 0
    sum_b = 0
    sum_c = 0
    i = 1
    while i <= n+1:
        if i % 2 == 0:
            sum_a = sum_a + 1/i
        else:
            sum_a = sum_a - 1/i
        sum_b = sum_b + 1/(i*(i+1))
        if i > 1:
            sum_c = sum_c + 1/math.sqrt(i)
        i = i + 1
    print(f"S = 1/1 - 1/2 + 1/3 - ... = {sum_a}")
    print(f"S = 1/(1*2) + 1/(2*3) + 1/(3*4) + ... = {sum_b}")
    print(f"S = 1/sqrt(2) + 1/sqrt(3) + 1/sqrt(4) + ... = {sum_c}")
