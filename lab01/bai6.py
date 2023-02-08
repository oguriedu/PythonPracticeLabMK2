#chương trình tính tiền điện cho một bóng đèn
import math
U=220
I=2.7
time_use = float(input('nhập thời gian sử dụng bóng đèn của hộ gia đình là : '))
dien_nang_tieu_thu =(U*I*time_use)/3600000
tien_dien=dien_nang_tieu_thu*7000
print("tiền điện khi sử dụng bóng đèn đó là : ",tien_dien)