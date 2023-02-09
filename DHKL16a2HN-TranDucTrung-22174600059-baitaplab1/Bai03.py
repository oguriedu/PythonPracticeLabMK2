r=float(input("Nhập bán kính khối trụ: "))
h=float(input("Nhập chiều cao khối trụ: "))
pi=3.14
sxq=2*pi*r*h
stp=(2*pi*r*h)+(2*pi*r**2)
v=pi*r**2*h
print("Diện tích xung quanh khối trụ: %0.2f"%sxq)
print("Diện tích toàn phần khối trụ: %0.2f"%stp)
print("Thể tích khối trụ: %0.2f"%v)