bk=float(input('Nhập bán kính của hình trụ:'))
cc=float(input('Nhập chiều cao của hình trụ:'))
sxq=2*3.14*bk*cc
stp=sxq+2*3.14*(bk**2)
tt=3.14*(bk**2)*cc
print('##############################################################')
print('Diện tích xung quanh của hình trụ là:',round(sxq,2))
print('Diện tích toàn phần của hình trụ là:',round(stp,2))
print('Thể tích của hình trụ là:',round(tt,2))