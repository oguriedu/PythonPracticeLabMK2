t=int(input('Nhập thời gian sử dụng bóng đèn (giây):'))
U = 220
I = 2.7
P = U * I
dien_su_dung = P * t / 3600
tien_dien = dien_su_dung * 7000 / 1000
print(f'Tiền điện phải trả là {tien_dien:.2f} đồng')