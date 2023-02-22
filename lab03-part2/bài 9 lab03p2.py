import math
from tabulate import tabulate
n = int (input('nhập số nguyên dương n: '))
tong = []
if n <= 0:
    print('nhập sai, mời nhập lại!!')
else:
    S4 = 0
    for i in range(1, n+1):
        S4 += math.pow(i, 2)

    S5 = 0
    for j in range(n+1):
        S5 +=math.pow((2*j+1), 3)

    S6 = 0
    for k in range(1, n+1):
        S6 += math.pow(2*k, 4)
        
tong.append([S4, S5, S6])
name = ['S4', 'S5', 'S6' ]
print (tabulate(tong, headers=name, tablefmt='fancy_grid'))
