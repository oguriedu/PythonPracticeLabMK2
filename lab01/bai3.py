import math
r=float(input("mời nhập bán kính: "))
h=float(input("mời nhập chiều cao: "))
the_tich=h*r*r*3.14
s_xq=2*3.14*r*h
stp=the_tich+s_xq
print("diện tích toàn phần: ",round(stp,2))
print("thể tích khối trụ: ",round(the_tich,2))
print("diện tích xung quanh: ",round(s_xq,2))
