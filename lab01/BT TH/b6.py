import math
U=220
I=2.7
gia_dien=7000
t=float(input('thời gian sử dụng đèn(giây): '))
dien_nang_tieu_thu=(U*I*t)/(3.6*10**6)
tien_dien=dien_nang_tieu_thu*7000
print('tiền điện phải trả:',tien_dien,"đồng")
