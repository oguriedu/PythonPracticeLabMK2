import math
x,y=map(float,input("Nhập các giá trị x,y: ").split())
f=(-x+math.sqrt(x**2+4))/(x**4 +1)**(1/7)
print("Giá trị của f là: %0.2f"%f)