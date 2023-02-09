import math 
r=float(input("Nhập bán kính khối trụ:"))
h=float(input("Nhập chiều cao khối trụ:"))
dtich_xq=2*3.14*r*h
dtich_tp=int(2*3.14*r*h)+int(2*3.14*r**2)
the_tich=int(3.14*h*r**2)
print(round(dtich_xq,2))
print(round(dtich_tp,2))
print(round(the_tich,2))
