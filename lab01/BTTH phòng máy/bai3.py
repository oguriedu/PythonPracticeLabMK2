r=float(input('Nhập số đo bán kính:'))
h=float(input('Nhập số đo chiều cao:'))
sxq=2*3.14*r*h
stp=2*3.14*r*h+2*3.14*r**2
v=3.14*r**2*h
print('Diện tích xung quanh hình trụ là%0.2f'%sxq)
print('Diện tích toàn phần hình trụ là',stp)
print('Thể tích hình trụ là%0.2f'%v)

