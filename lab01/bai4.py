import math
x = int(input('nhập vào giá trị x:'))

f = (-x + math.sqrt(x*x+4))/(x**4 + 1)**(1/7)
print('giá trị của f=%0.2f'%(f))