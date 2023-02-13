pi = 3.14
r = float(input('Nhập số đo bán kính: '))
h = float(input('Nhập số đo chiều cao: '))
sxq = 2*pi*r*h
stp = 2*pi*r*h + 2*pi*r*r
v = pi*r*r*h
print(f'Diện tích xung quanh của khối trụ là {sxq:.2f}')
print(f'Diện tích toàn phần của khối trụ là {stp:.2f}')
print(f'Thể tích của khối trụ là {v:.2f}')
