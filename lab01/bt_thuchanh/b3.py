r=float(input("số đo bán kính:"))
h=float(input("chiều cao:"))
s_xq=2*3.14*r*h
s_tp=2*3.14*r*r + s_xq
v=3.14*r*r*h
print("diện tích xq là:%0.2f"%s_xq)
print("diện tích tp là:%0.2f"%s_tp)
print("thể tích là:%0.2f"%v)