import math
from tabulate import tabulate
n = int (input('nhập số n: '))
if n <=0:
    print('nhập sai, mời nhập lại!!')
else:
    i = 1; S4 = 0
    while i<=n:
        S4 += i**2
        i += 1
        
    S5 = 0; j = 0
    while j<=n:
        S5 += math.pow(2*j+1, 3)
        j += 1

    S6 = 0; k = 0
    while k<=n:
        S6 += math.pow(2*k, 4)
        k += 1
        
list = []
list.append([S4, S5, S6])
name = ['S4', 'S5', 'S6']
print (tabulate(list, headers=name, tablefmt='fancy_grid'))