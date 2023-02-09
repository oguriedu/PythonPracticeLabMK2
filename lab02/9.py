KW=int(input('Nhập số KW điện tiêu thụ:  '))
if 0<=KW<=100:
    t=KW*2000
elif 100<KW<=200:
    t=200000+(KW-100)*2500
elif 200<KW<=300:
    t=200000+250000+(KW-300)*3000
elif KW>300:
    t=200000+250000+300000+(KW-300)*5000
print('Tiền điện tháng này là {:,} Đồng'.format(t))