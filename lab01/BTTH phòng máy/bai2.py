s=float(input('Mời bạn nhập số giây:'))
m=s//60
h=s//3600
d=s//86400
print('{:<20}{:<12}{:<30}'.format('Ngày','Gio','Phút'))
print('{:<20}{:<12}{:<30}'.format(d,h,m))