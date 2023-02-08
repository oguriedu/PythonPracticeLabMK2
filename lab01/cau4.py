import math
x=float(input('Nhập giá trị x :'))
bt=float((-x+math.sqrt(x*x+4))/(x*x*x*x+1)**(1/7))
print(f'Giá trị biểu thức là:{bt:.2f}')