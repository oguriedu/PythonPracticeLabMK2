import math
from tabulate import tabulate
n = int (input('nhập số nguyên dương n: '))
Sa = 0; i = 1
while i<=n:
    if i%2==1: Sa+=1/i
    else: Sa-=1/i
    i += 1

Sb = 0; j = 2
while j <= n+1:
    Sb += 1/((j-1)*j)
    j += 1

Sc = 0; k = 2
while k <= n+1:
    Sc += 1/math.sqrt(k)
    k += 1

list = []
list.append([Sa, Sb, Sc])
name = ['Sa', 'Sb', 'Sc']
print(tabulate(list, headers=name, tablefmt='fancy_grid'))