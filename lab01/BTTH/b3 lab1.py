r=float(int(input("Nhập bán kính: ")))
h=float(int(input("Nhập chiều cao: ")))
pi=3.14
#tính diện tích xung quanh hình trụ
Sxq=2*pi*r*h
#tính diện tích toàn phần hình trụ
Stp=2*pi*r**2
#tính thể tích hình trụ
V=pi*h*r**2
print(f'Diện tích xung quanh hình trụ là: {Sxq:.2f}')
print(f'Diện tích toàn phần hình trụ là: {Stp:.2f}')
print(f'Thể tích hình trụ là: {V:.2f}')