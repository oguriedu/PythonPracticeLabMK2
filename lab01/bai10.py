import math
x,y=map(float, input("Nhập giá trị x,y:").split())
f=math.sin(x)//((2*x+y)/math.cos(x)-x**y/(x-y))
print("Giá trị của biểu thức là: %0.2f"%f)