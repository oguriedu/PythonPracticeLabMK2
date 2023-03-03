n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập n > 0: '))
S4 = 0
for i in range(1,n + 1):
    S4+=i**2
print('Tổng S4 =', S4)
S5 = 0
for i in range(0,n + 1):
    S5+=(2*n+1)**3
print('Tổng S5 =', S5)
S6 = 0
for i in range(1,n + 1):
    S6+=(2*n)**4
print('Tổng S6 =', S6)