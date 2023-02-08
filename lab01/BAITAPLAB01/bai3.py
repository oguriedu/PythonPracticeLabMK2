r=float(input("Nhập số đo bán kính: "))
h=float(input("Nhập số đo chiều cao: "))
dt_xq=2*3.14*r*h
dt_tp=2*3.14*r**2+dt_xq
v=3.14*h*r**2
print("Diện tích xung quanh của khối trụ là: %0.2f"%dt_xq)
print("Diện tích toàn phần của khối trụ là: %0.2f"%dt_tp)
print("Thể tích khối trụ là: %0.2f"%v)