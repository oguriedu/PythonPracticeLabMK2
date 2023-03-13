tnct=int(input('Nhập vào thâm niên công tác :'))
luongcb=1350000
if 0<tnct<12:
    luong=2.34*luongcb
elif 12<=tnct<36:
    luong=3.33*luongcb
elif 36<=tnct<60:
    luong=3.66*luongcb
else:
    luong=3.99*luongcb
print('Lương của bạn là :%d{:,}VNĐ'.format(luong))
