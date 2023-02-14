import math
pi=3.14
r=float(input(" nhập bán kính đáy :"))
h= float(input(" nhập chiều cao khối trụ :"))
Sxq= 2*pi*r*h
Stp= 2*pi*r*h + 2*pi*r**2
V= h*pi*r**2
print (" diện tích xung quanh của khối trụ = : %0.2f"%Sxq)
print (" diện tích toàn phần của khối trụ = : %0.2f"%Stp)
print (" THỂ Tích của khối trụ = : %0.2f"%V)
