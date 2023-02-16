import math
def kiemtra(n):
    if n < 2:
        return False
    a = int(math.sqrt(n))
    for i in range(2, a + 1):
        if (n % i) == 0:
            return False
    return True

n = int(input('Nhap vao so nguyen duong n = '))
print('Cac so nguyen to khong qua ', n, ' la:')
if n >= 2:
    print(2)
    for i in range(3, n + 1):
        if kiemtra(i):
            print(i)
        i = i + 2