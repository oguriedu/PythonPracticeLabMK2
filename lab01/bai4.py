#chương trình tính giá trị biểu thức
import math
x = float(input("nhập số x = "))
f=((-x)+math.sqrt(x**2+4))/(x**4+1)**(2/7)
print("giá trị của biểu thức là : %0.2f"%f)