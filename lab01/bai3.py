r, h = map(float,input('Nhập bán kính và chiều cao của hình trụ: ').split())
sxp = 2*3.14*r*h
stp = 2*3.14*r*h + 2*3.14*r*r
v = 3.14*r**2*h
print('Diện tích xung quanh của hình trụ là: %0.2f '%sxp)
print('Diện tihs toàn phần của hình trụ là: %0.2f'%stp)
print('Thể tích của hình trụ lag: %0.2f'%v)


