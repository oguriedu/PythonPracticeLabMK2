pi=3.14
r=float(input('bán kính khối trụ: '))
h=float(input('chiều cao khối trụ: '))
Sxq=2*r*pi*h
Stp=2*r*pi*h+2*pi*r**2
V=pi*r**2*h
print('diện tích xung quanh của khối trụ: %0.2f'%Sxq,'(đvdt)')
print('diện tích toàn phần của khối trụ: %0.2f'%Stp,'(đvdt)')
print('thể tích của khối trụ:%0.2f'%V,'(đvdt)')