import math 
x = float(input("Nhập giá rị của x: "))
a = (-x+math.sqrt(x**2+4))/(x**4+1)**(1/7)
print('Giá trị của biểu thức là: %0.2f ' %a)