import math
from tabulate import tabulate
r = float(input('nhập bán kính: '))
h = float(input('nhập chiều cao: '))
data = []
# tính diện tích xung quanh
Sxq = 2*3.14*r*h
a = round(Sxq, 2)

# tính diện tích toàn phần
Stp = 2*3.14*math.pow(r, 2) + Sxq
b = round(Stp, 2)

# tính thể tích 
V = 3.14*math.pow(r, 2)*h
c = round(V, 2)

data.append([a, b, c])
col_name = ['diện tích xung quanh', 'diện tích toàn phần', 'thể tích']
print (tabulate(data, headers=col_name, tablefmt='fancy_grid'))