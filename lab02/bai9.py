a = float(input('Nhập số KW tiêu thụ:'))
if a < 101:
    hs = 2000
elif a <201:
    hs = 2500
elif a < 300:
    hs = 3000
else:
    hs = 5000
print('Tiền điện=%0.4f đồng'%(hs*a))