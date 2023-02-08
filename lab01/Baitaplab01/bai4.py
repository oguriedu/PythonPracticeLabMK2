import math
x = float(input('Nhập giá trị của x:'))
fx=((-x)+(math.pow((x**2)+4,0.5)))/(math.pow((x**4+1),(1/7)))
print('Giá trị của biểu thức là:',round(fx,2))
