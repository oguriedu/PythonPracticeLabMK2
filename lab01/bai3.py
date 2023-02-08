#chương trình tính các giá trị liên quan đến hình trụ
import math
h=float(input("nhập chiều cao của khối trụ : "))
r=float(input("nhập bán kính của khối trụ : "))
Sxq=3.14*r*r*h
print("diện tích xung quanh của hình trụ là : ",Sxq)
Stp=2*3.14*r*r*h
print("diện tích toàn phần của hình trụ là : ",Stp)