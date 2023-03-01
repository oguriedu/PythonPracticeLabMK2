n = int(input('Nhập số n = '))
P = int(1)
for i in range(1, n+1):
    P *= i
print(n, '!=', P)
