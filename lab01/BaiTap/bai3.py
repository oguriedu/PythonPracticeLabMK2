r = float(input('Nhập bán kính: '))
h = float(input('Nhập chiều cao: '))
pi = 3.14
print('Diện tích xung quanh của hình trụ là: ',round(2*pi*r*h,2))
print('Diện tích toàn phần của hình trụ là: ',round(2*pi*r*r+2*pi*r*h,2))
print('Thể tích của khối trụ là: ',round(pi*r*r*h,2))