import math

def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số n: "))
if so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    i = n + 1
    while not so_nguyen_to(i):
        i += 1
    print(i, "là số nguyên tố gần nhất với", n)
