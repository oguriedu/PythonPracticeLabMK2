import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def find_closest_prime(n):
    if n < 2:
        return 2
    i = 1
    while True:
        if is_prime(n-i):
            return n-i
        if is_prime(n+i):
            return n+i
        i += 1

n = int(input("Nhập số n: "))
if is_prime(n):
    print(n, "là số nguyên tố")
else:
    closest = find_closest_prime(n)
    print(n, "không phải là số nguyên tố")
    print("Số nguyên tố gần nhất là:", closest)
    
