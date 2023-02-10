#Viết phương trình tính diện tích xung quanh,diện tích toàn phần,thể tích khối trụ
import math 
h=float(input("nhập chiều cao của khối trụ: "))
r=float(input("nhập bán kính của khối trụ: "))
#tính diện tích xung quanh
Sxq=2*3.14*r*h
#Tính diện tích toàn phần
Stp=2*3.14*r*h + 2*3.14*r*r
#Thể tích khối trụ
v=3.14*r*r*h
#In kết quả ra màn hình
print("diện tích xung quanh của khối trụ là: ",Sxq)
print("diện tích toàn phần của khối trụ là: ",Stp)
print("Thể tích hình trụ là :",v)