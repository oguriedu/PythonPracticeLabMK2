import math
def bieuthuc(x):
    bt=(-x+math.sqrt(x**2+4))/(x**4+1)**(1/7)
    return bt
x=int(input("Nhập số x vào đây: "))
print("giá trị của biểu thức trên là: ",round(bieuthuc(x),2))