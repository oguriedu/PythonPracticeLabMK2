#Chương trình tính diện tích xung quanh, dt toàn phần và thể tích khối trụ 
r=float(input('Nhập bán kính khối trụ :'))
h=float(input('Nhập chiều cao khối trụ :'))
sxq=2*3.14*r*h
stp=2*3.14*r*r+2*3.14*r*h
v=3.14*r*r*h
print('Diện tích xung quanh hình trụ là: %0.2f'%sxq)
print('Diện tích toàn phần hình trụ là: %0.2f'%stp)
print('Thể tích hình trụ là:%0.2f'%v)