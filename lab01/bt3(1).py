#Tính diện tích xung quanh và diện tích toàn phần và thể tích của khối trụ
r = float(input('Nhập bán kính của khối trụ: '))
h = float(input('Nhập chiều cao của khối trụ: '))
Sxq = 2*3.14 * r * h
Stp = Sxq + 2*3.14*(r**2)
V = 3.14*h*(r**2)
print('Diện tích xung quanh của khối trụ là: ',round(Sxq,2),'Diện tích toàn phần của khối trụ là: ',round(Stp,2),'Thể tích của khối trụ là: ',round(V,2), sep = '\n')