import math

x = float(input('Nhập giá trị x: '))
f = math.log(x, 4) + math.log(2, x)
print(f'Giá trị của biểu thức là: {f:.2f}')
